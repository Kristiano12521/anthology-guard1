import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import _pack_kristiano_aio as packer  # noqa: E402


def write(path: Path, text: str = "x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def zip_names(archive: Path) -> list[str]:
    with zipfile.ZipFile(archive) as zf:
        return zf.namelist()


class PackKristianoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.addon_root = root / "addon"
        self.out_dir = root / "build"
        self.addon_root.mkdir()
        self.out_dir.mkdir()

        write(
            self.addon_root / "keep_me" / "gamedata" / "scripts" / "keep_me.script",
            "-- aio keep\n",
        )
        write(self.addon_root / "keep_me" / "CHANGELOG.md", "## [2.1.0]\n")
        write(
            self.addon_root / "also_keep" / "gamedata" / "configs" / "items" / "mod_also.ltx",
            "[also]\n",
        )

        for mod_id, marker in (
            ("context_menu_overhaul_anthology", "cmo_only"),
            ("quickqk_task_complete", "quickqk_only"),
            ("fix_st2_footstep", "st2_only"),
        ):
            write(
                self.addon_root / mod_id / "gamedata" / "scripts" / f"{marker}.script",
                f"-- {marker}\n",
            )
            write(self.addon_root / mod_id / "CHANGELOG.md", "## [3.2.1]\n")
            write(self.addon_root / mod_id / "meta.ini", "version=0.0.0\ninstallationFile=old.zip\n")

        write(
            self.addon_root / "fix_bhs_fdda_loot" / "gamedata" / "scripts" / "skip_loot.script",
            "-- skipped\n",
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def pack(self) -> None:
        code = packer.main(["--addon-root", str(self.addon_root), "--out", str(self.out_dir)])
        self.assertEqual(code, 0)

    def test_aio_excludes_skip_and_separate(self):
        self.pack()
        aio = self.out_dir / f"{packer.AIO_NAME}.zip"
        self.assertTrue(aio.is_file())
        names = zip_names(aio)
        self.assertIn("gamedata/scripts/keep_me.script", names)
        self.assertIn("gamedata/configs/items/mod_also.ltx", names)
        self.assertTrue(any(name.startswith("gamedata/") for name in names))
        self.assertFalse(any(name.startswith(packer.AIO_NAME) for name in names))
        self.assertNotIn("gamedata/scripts/cmo_only.script", names)
        self.assertNotIn("gamedata/scripts/quickqk_only.script", names)
        self.assertNotIn("gamedata/scripts/st2_only.script", names)
        self.assertNotIn("gamedata/scripts/skip_loot.script", names)

    def test_separate_zips_layout_and_version(self):
        self.pack()
        for mod_id, mo2_name in packer.SEPARATE.items():
            archive = self.out_dir / f"{mo2_name}.zip"
            self.assertTrue(archive.is_file(), msg=archive.name)
            names = zip_names(archive)
            self.assertTrue(any(n.startswith("gamedata/") for n in names), msg=names)
            self.assertFalse(any(n.startswith(mo2_name) for n in names), msg=names)
            self.assertIn("meta.ini", names)
            with zipfile.ZipFile(archive) as zf:
                meta = zf.read("meta.ini").decode("utf-8")
            self.assertIn("version=3.2.1", meta)

        addons = {p.name for p in packer.aio_addons(self.addon_root)}
        self.assertEqual(addons, {"also_keep", "keep_me"})
        self.assertTrue(addons.isdisjoint(packer.SEPARATE))
        self.assertTrue(addons.isdisjoint(packer.SKIP))


if __name__ == "__main__":
    unittest.main()
