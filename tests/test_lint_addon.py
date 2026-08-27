import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import lint_addon  # noqa: E402

FIXTURES = REPO_ROOT / "tests" / "fixtures"
FIXTURE_REFERENCE = FIXTURES / "reference"


def build_reference() -> lint_addon.ReferenceView:
    return lint_addon.ReferenceView.load(FIXTURE_REFERENCE)


class BadAddonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.findings = lint_addon.lint(FIXTURES / "addon_bad", build_reference())
        cls.codes = {finding.code for finding in cls.findings}

    def test_full_config_replacement_is_error(self):
        self.assertIn("LTX-001", self.codes)

    def test_duplicate_base_section_is_error(self):
        self.assertIn("LTX-003", self.codes)

    def test_patch_for_unknown_section_warns(self):
        self.assertIn("LTX-004", self.codes)

    def test_unmatched_patch_filename_warns(self):
        self.assertIn("LTX-002", self.codes)

    def test_script_copy_of_base_game_warns(self):
        self.assertIn("LUA-001", self.codes)

    def test_anonymous_callback_is_error(self):
        self.assertIn("LUA-002", self.codes)

    def test_missing_unregister_warns(self):
        self.assertIn("LUA-003", self.codes)

    def test_untrottled_actor_update_warns(self):
        self.assertIn("LUA-004", self.codes)

    def test_mcm_load_in_wrong_file_is_error(self):
        self.assertIn("MCM-001", self.codes)

    def test_unguarded_ui_mcm_warns(self):
        self.assertIn("MCM-002", self.codes)

    def test_option_without_val_is_error(self):
        self.assertIn("MCM-003", self.codes)

    def test_load_order_prefix_is_error(self):
        self.assertIn("ORDER-001", self.codes)

    def test_missing_meta_and_changelog_warn(self):
        self.assertIn("STRUCT-002", self.codes)
        self.assertIn("STRUCT-003", self.codes)

    def test_findings_carry_location(self):
        dup = next(f for f in self.findings if f.code == "LTX-003")
        self.assertTrue(dup.path.endswith("mod_items_food_bad.ltx"))
        self.assertGreater(dup.line, 0)


class GoodAddonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.findings = lint_addon.lint(FIXTURES / "addon_good", build_reference())

    def test_no_errors(self):
        errors = [f for f in self.findings if f.severity == "error"]
        self.assertEqual(errors, [], msg=[f.format() for f in errors])

    def test_no_warnings_either(self):
        warns = [f for f in self.findings if f.severity == "warn"]
        self.assertEqual(warns, [], msg=[f.format() for f in warns])


class EncodingTests(unittest.TestCase):
    def test_utf8_cyrillic_game_file_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = Path(tmp) / "enc_mod"
            scripts = addon / "gamedata" / "scripts"
            scripts.mkdir(parents=True)
            (addon / "meta.ini").write_text("[General]\nversion=1.0.0\n", encoding="utf-8")
            (addon / "CHANGELOG.md").write_text("# enc\n", encoding="utf-8")
            (scripts / "enc_mod.script").write_text(
                '-- комментарий на русском\nfunction on_game_start() end\n', encoding="utf-8"
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView())
            self.assertIn("ENC-002", {f.code for f in findings})

    def test_bom_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = Path(tmp) / "bom_mod"
            scripts = addon / "gamedata" / "scripts"
            scripts.mkdir(parents=True)
            (scripts / "bom_mod.script").write_bytes(
                b"\xef\xbb\xbffunction on_game_start() end\n"
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView())
            self.assertIn("ENC-001", {f.code for f in findings})


class EmptyReferenceTests(unittest.TestCase):
    def test_checks_needing_reference_are_skipped(self):
        findings = lint_addon.lint(FIXTURES / "addon_bad", lint_addon.ReferenceView())
        codes = {f.code for f in findings}
        # Без исходников сборки нельзя знать, что файл её дублирует.
        self.assertNotIn("LTX-001", codes)
        self.assertNotIn("LUA-001", codes)
        # А эти проверки не зависят от reference/ и должны сработать всё равно.
        self.assertIn("LUA-002", codes)
        self.assertIn("ORDER-001", codes)


if __name__ == "__main__":
    unittest.main()
