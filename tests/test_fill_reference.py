import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import fill_reference  # noqa: E402
from test_xdb_unpack import build_archive, build_uncompressed_archive  # noqa: E402


def run_fill(game: Path, reference: Path, *extra: str) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
        code = fill_reference.main(
            [str(game), "--reference", str(reference), *extra]
        )
    return code, buffer.getvalue()


class PathFilterTests(unittest.TestCase):
    def test_keeps_scripts_configs_text(self):
        self.assertEqual(
            fill_reference.dest_relative("scripts\\axr_main.script"),
            "scripts/axr_main.script",
        )
        self.assertEqual(
            fill_reference.dest_relative("gamedata/configs/items/food.ltx"),
            "configs/items/food.ltx",
        )
        self.assertEqual(
            fill_reference.dest_relative("text/rus/st_items.xml"),
            "text/rus/st_items.xml",
        )
        self.assertEqual(
            fill_reference.dest_relative("configs/text/eng/ui.xml"),
            "configs/text/eng/ui.xml",
        )
        self.assertEqual(
            fill_reference.dest_relative("materials\\materials.ltx"),
            "materials/materials.ltx",
        )
        self.assertEqual(
            fill_reference.dest_relative("gamedata/materials/material_pairs.ltx"),
            "materials/material_pairs.ltx",
        )

    def test_configs_scripts_keeps_configs_prefix(self):
        self.assertEqual(
            fill_reference.dest_relative("configs\\scripts\\garbage\\logic.ltx"),
            "configs/scripts/garbage/logic.ltx",
        )

    def test_skips_assets_and_directories(self):
        self.assertIsNone(fill_reference.dest_relative("textures\\ui\\icon.dds"))
        self.assertIsNone(fill_reference.dest_relative("meshes\\actors\\stalker.ogf"))
        self.assertIsNone(fill_reference.dest_relative("sounds\\music\\theme.ogg"))
        self.assertIsNone(fill_reference.dest_relative("shaders\\r3\\foo.ps"))
        self.assertIsNone(fill_reference.dest_relative("levels\\l01_escape\\level"))
        self.assertIsNone(fill_reference.dest_relative("scripts\\"))
        self.assertIsNone(fill_reference.dest_relative("configs/"))
        self.assertIsNone(fill_reference.dest_relative("materials/"))
        self.assertIsNone(fill_reference.dest_relative(""))

    def test_should_keep_rejects_zero_size(self):
        self.assertFalse(fill_reference.should_keep("scripts\\foo.script", size_real=0))
        self.assertTrue(fill_reference.should_keep("scripts\\foo.script", size_real=10))
        self.assertTrue(fill_reference.should_keep("materials\\materials.ltx", size_real=10))
        self.assertFalse(fill_reference.should_keep("textures\\a.dds", size_real=99))


class ClassifyTests(unittest.TestCase):
    def test_anthology_in_filename(self):
        db = Path("C:/game/db")
        self.assertEqual(
            fill_reference.classify_archive(db / "scripts_anthology.db0", db),
            "anthology",
        )
        self.assertEqual(
            fill_reference.classify_archive(db / "configs" / "configs.db0", db),
            "anomaly",
        )

    def test_anthology_in_parent_folder(self):
        db = Path("/game/db")
        archive = db / "packs_anthology" / "scripts.db0"
        self.assertEqual(fill_reference.classify_archive(archive, db), "anthology")


class FillPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.game = self.root / "game"
        self.db = self.game / "db"
        self.reference = self.root / "reference"
        (self.reference / "addons" / "keep_me").mkdir(parents=True)
        self.sentinel = self.reference / "addons" / "keep_me" / "marker.txt"
        self.sentinel.write_text("stay", encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _put_archive(self, relative: str, files: dict[str, bytes]) -> Path:
        path = self.db / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(build_uncompressed_archive(files))
        return path

    def test_dry_run_writes_nothing(self):
        self._put_archive(
            "scripts/scripts.db0",
            {
                "scripts\\hello.script": b"-- hello",
                "textures\\skip.dds": b"DDS",
            },
        )
        code, out = run_fill(self.game, self.reference, "--dry-run")
        self.assertEqual(code, 0, msg=out)
        self.assertIn("scripts/hello.script", out)
        self.assertNotIn("textures/skip.dds", out)
        self.assertFalse((self.reference / "anomaly" / "scripts" / "hello.script").exists())
        self.assertTrue(self.sentinel.exists())

    def test_extracts_to_anomaly_and_skips_assets(self):
        self._put_archive(
            "mixed.db0",
            {
                "scripts\\a.script": b"function a() end",
                "configs\\items\\x.ltx": b"[x]\n",
                "meshes\\body.ogf": b"mesh",
                "sounds\\hit.ogg": b"ogg",
            },
        )
        code, out = run_fill(self.game, self.reference)
        self.assertEqual(code, 0, msg=out)
        anomaly = self.reference / "anomaly"
        self.assertEqual(
            (anomaly / "scripts" / "a.script").read_bytes(), b"function a() end"
        )
        self.assertEqual((anomaly / "configs" / "items" / "x.ltx").read_bytes(), b"[x]\n")
        self.assertFalse((anomaly / "meshes").exists())
        self.assertFalse((anomaly / "sounds").exists())
        self.assertIn("refindex.py build", out)

    def test_anthology_archive_goes_to_anthology_tree(self):
        self._put_archive(
            "scripts/scripts_anthology.db0",
            {"scripts\\anth.script": b"-- anth"},
        )
        code, out = run_fill(self.game, self.reference)
        self.assertEqual(code, 0, msg=out)
        dest = self.reference / "anthology" / "scripts" / "anth.script"
        self.assertTrue(dest.exists(), msg=out)
        self.assertFalse((self.reference / "anomaly" / "scripts" / "anth.script").exists())

    def test_idempotent_second_run(self):
        self._put_archive(
            "scripts.db0",
            {"scripts\\once.script": b"-- once"},
        )
        run_fill(self.game, self.reference)
        dest = self.reference / "anomaly" / "scripts" / "once.script"
        code, out = run_fill(self.game, self.reference)
        self.assertEqual(code, 0, msg=out)
        self.assertIn("без изменений: 1", out)
        self.assertEqual(dest.read_bytes(), b"-- once")
        self.assertEqual(len(list((self.reference / "anomaly" / "scripts").iterdir())), 1)

    def test_does_not_touch_addons(self):
        self._put_archive("scripts.db0", {"scripts\\x.script": b"x"})
        run_fill(self.game, self.reference)
        self.assertEqual(self.sentinel.read_text(encoding="utf-8"), "stay")
        self.assertEqual(
            [p.relative_to(self.reference / "addons").as_posix() for p in (self.reference / "addons").rglob("*") if p.is_file()],
            ["keep_me/marker.txt"],
        )

    def test_extracts_materials(self):
        self._put_archive(
            "mods.db0",
            {
                "materials\\materials.ltx": b"[default]\n",
                "gamedata\\materials\\material_pairs.ltx": b"[pair]\n",
                "textures\\skip.dds": b"DDS",
            },
        )
        code, out = run_fill(self.game, self.reference)
        self.assertEqual(code, 0, msg=out)
        anomaly = self.reference / "anomaly"
        self.assertEqual((anomaly / "materials" / "materials.ltx").read_bytes(), b"[default]\n")
        self.assertEqual(
            (anomaly / "materials" / "material_pairs.ltx").read_bytes(), b"[pair]\n"
        )
        self.assertFalse((anomaly / "textures").exists())
        self.assertNotIn("пропущено", out)

    def test_skip_summary_at_end(self):
        garbage = bytes([18]) + b"x"
        path = self.db / "broken.db0"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(
            build_archive(
                {
                    "scripts\\bad.script": (garbage, 40),
                    "scripts\\ok.script": b"-- ok",
                }
            )
        )
        code, out = run_fill(self.game, self.reference)
        self.assertEqual(code, 0, msg=out)
        self.assertEqual(
            (self.reference / "anomaly" / "scripts" / "ok.script").read_bytes(), b"-- ok"
        )
        self.assertFalse((self.reference / "anomaly" / "scripts" / "bad.script").exists())
        self.assertIn("пропущено 1: lzo truncated (1)", out)

    def test_missing_db_dir(self):
        empty_game = self.root / "empty"
        empty_game.mkdir()
        code, out = run_fill(empty_game, self.reference)
        self.assertEqual(code, 2)
        self.assertIn("db/", out)


if __name__ == "__main__":
    unittest.main()
