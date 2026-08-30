import contextlib
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import build_addon  # noqa: E402
import lint_addon  # noqa: E402
import new_addon  # noqa: E402


def run(func, argv) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
        code = func(argv)
    return code, buffer.getvalue()


class NewAddonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addon_root = Path(self.tmp.name) / "addon"
        self.addon_root.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def create(self, mod_id: str, *extra: str) -> Path:
        code, out = run(
            new_addon.main, [mod_id, "--addon-root", str(self.addon_root), *extra]
        )
        self.assertEqual(code, 0, msg=out)
        return self.addon_root / mod_id

    def test_placeholders_replaced_in_names_and_content(self):
        mod = self.create("my_test_mod", "--title", "My Test Mod")
        script = mod / "gamedata" / "scripts" / "my_test_mod.script"
        mcm = mod / "gamedata" / "scripts" / "my_test_mod_mcm.script"
        self.assertTrue(script.exists())
        self.assertTrue(mcm.exists())
        text = script.read_text(encoding="cp1251")
        self.assertIn("My Test Mod", text)
        self.assertNotIn("__MOD_ID__", text)
        self.assertIn('id = "my_test_mod"', mcm.read_text(encoding="cp1251"))

    def test_meta_and_changelog_created(self):
        mod = self.create("my_test_mod")
        self.assertIn("version=1.0.0", (mod / "meta.ini").read_text(encoding="utf-8"))
        self.assertTrue((mod / "CHANGELOG.md").exists())

    def test_diag_script_is_opt_in(self):
        mod = self.create("my_test_mod")
        self.assertFalse((mod / "gamedata" / "scripts" / "my_test_mod_diag.script").exists())
        diag_mod = self.create("my_diag_mod", "--diag")
        diag = diag_mod / "gamedata" / "scripts" / "my_diag_mod_diag.script"
        self.assertTrue(diag.exists())
        self.assertIn("DIAGNOSTIC ONLY", diag.read_text(encoding="cp1251"))

    def test_optional_parts_can_be_skipped(self):
        mod = self.create("lean_mod", "--no-mcm", "--no-ltx")
        scripts = {p.name for p in (mod / "gamedata" / "scripts").iterdir()}
        self.assertEqual(scripts, {"lean_mod.script"})
        self.assertFalse((mod / "gamedata" / "configs").exists())

    def test_generated_addon_passes_lint(self):
        mod = self.create("clean_mod")
        findings = lint_addon.lint(mod, lint_addon.ReferenceView())
        self.assertEqual([f.format() for f in findings], [])

    def test_rejects_load_order_prefix(self):
        code, out = run(
            new_addon.main, ["zzzz_hack", "--addon-root", str(self.addon_root)]
        )
        self.assertEqual(code, 2)
        self.assertIn("Префиксы", out)

    def test_rejects_invalid_id(self):
        code, _ = run(new_addon.main, ["My Mod", "--addon-root", str(self.addon_root)])
        self.assertEqual(code, 2)

    def test_refuses_to_overwrite_without_force(self):
        self.create("my_test_mod")
        code, out = run(
            new_addon.main, ["my_test_mod", "--addon-root", str(self.addon_root)]
        )
        self.assertEqual(code, 2)
        self.assertIn("--force", out)


class BuildAddonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.addon_root = base / "addon"
        self.build_root = base / "build"
        self.empty_reference = base / "reference"
        self.addon_root.mkdir()
        self.empty_reference.mkdir()
        run(new_addon.main, ["my_test_mod", "--addon-root", str(self.addon_root)])

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def build(self, *extra: str) -> tuple[int, str]:
        return run(
            build_addon.main,
            [
                "my_test_mod",
                "--addon-root",
                str(self.addon_root),
                "--out",
                str(self.build_root),
                "--reference",
                str(self.empty_reference),
                *extra,
            ],
        )

    def test_build_produces_gamedata_and_metadata(self):
        code, out = self.build()
        self.assertEqual(code, 0, msg=out)
        mod_build = self.build_root / "my_test_mod"
        self.assertTrue((mod_build / "gamedata" / "scripts" / "my_test_mod.script").exists())
        self.assertTrue((mod_build / "meta.ini").exists())
        info = (mod_build / "BUILD_INFO.txt").read_text(encoding="utf-8")
        self.assertIn("mod_id: my_test_mod", info)
        self.assertIn("version: 1.0.0", info)

    def test_version_comes_from_changelog(self):
        changelog = self.addon_root / "my_test_mod" / "CHANGELOG.md"
        changelog.write_text("# Mod\n\n## [2.3.1] - 2026-02-02\n\nchanged\n", encoding="utf-8")
        code, out = self.build()
        self.assertEqual(code, 0, msg=out)
        meta = (self.build_root / "my_test_mod" / "meta.ini").read_text(encoding="utf-8")
        self.assertIn("version=2.3.1", meta)

    def test_zip_layout_is_mo2_ready(self):
        code, out = self.build("--zip")
        self.assertEqual(code, 0, msg=out)
        archive = self.build_root / "my_test_mod-1.0.0.zip"
        self.assertTrue(archive.exists())
        with zipfile.ZipFile(archive) as zf:
            names = zf.namelist()
        self.assertIn("gamedata/scripts/my_test_mod.script", names)
        self.assertIn("meta.ini", names)

    def test_install_copies_into_mods_folder(self):
        mods = Path(self.tmp.name) / "mo2mods"
        mods.mkdir()
        code, out = self.build("--install", str(mods))
        self.assertEqual(code, 0, msg=out)
        self.assertTrue((mods / "my_test_mod" / "gamedata" / "scripts" / "my_test_mod.script").exists())

    def test_lint_errors_block_the_build(self):
        broken = self.addon_root / "my_test_mod" / "gamedata" / "configs" / "zzzz_bad.ltx"
        broken.parent.mkdir(parents=True, exist_ok=True)
        broken.write_text("[dummy]\nkey = 1\n", encoding="cp1251")
        code, out = self.build()
        self.assertEqual(code, 1)
        self.assertIn("ORDER-001", out)
        code, out = self.build("--force")
        self.assertEqual(code, 0, msg=out)


if __name__ == "__main__":
    unittest.main()
