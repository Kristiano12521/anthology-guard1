import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import xraylog  # noqa: E402

SAMPLES = REPO_ROOT / "logs" / "samples"


def parse(name: str) -> xraylog.LogReport:
    report = xraylog.LogReport(SAMPLES / name)
    report.parse(context_lines=40)
    return report


class LuaCrashTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = parse("crash_lua_nil.log")

    def test_detects_crash(self):
        self.assertTrue(self.report.crashed)
        self.assertEqual(self.report.fields["Function"], "CScriptEngine::lua_error")

    def test_classified_as_lua(self):
        crash_class, hints = self.report.classify()
        self.assertEqual(crash_class, "Lua error")
        self.assertTrue(any("anth_squad_manager.script:212" in hint for hint in hints))

    def test_extracts_frames_in_order(self):
        refs = self.report.lua_refs()
        self.assertEqual(refs[0], "anth_squad_manager.script:212")
        self.assertIn("anth_squad_manager.script:88", refs)

    def test_context_drops_noise_and_keeps_signal(self):
        context = "\n".join(self.report.context)
        self.assertIn("simulation tick 2", context)
        self.assertNotIn("phase cmem", context)

    def test_warnings_are_grouped(self):
        warnings = dict(self.report.warnings)
        texture_warning = next(k for k in warnings if "Can't find texture" in k)
        self.assertEqual(warnings[texture_warning], 3)

    def test_markdown_card_is_self_contained(self):
        card = self.report.to_markdown(max_warnings=10, warnings_only=False)
        self.assertIn("FATAL ERROR", card)
        self.assertIn("Куда смотреть", card)
        self.assertIn("anth_squad_manager.script:212", card)


class ConfigCrashTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = parse("crash_missing_section.log")

    def test_classified_as_missing_section(self):
        crash_class, hints = self.report.classify()
        self.assertEqual(crash_class, "конфиг: нет секции")
        self.assertTrue(any("refindex.py section wpn_ak74_anth_custom" in hint for hint in hints))

    def test_extracts_section_name(self):
        self.assertEqual(self.report.missing_section(), "wpn_ak74_anth_custom")

    def test_no_false_lua_frames(self):
        self.assertEqual(self.report.lua_refs(), [])


class CleanSessionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = parse("clean_session.log")

    def test_no_crash_reported(self):
        self.assertFalse(self.report.crashed)
        crash_class, _ = self.report.classify()
        self.assertEqual(crash_class, "вылета в логе нет")

    def test_warnings_still_collected(self):
        self.assertTrue(any("ui_icon_anth_pda" in text for text in self.report.warnings))


class CliTests(unittest.TestCase):
    def test_json_output_is_valid(self):
        import contextlib
        import io

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = xraylog.main([str(SAMPLES / "crash_lua_nil.log"), "--json"])
        self.assertEqual(code, 0)
        payload = json.loads(buffer.getvalue())
        self.assertEqual(payload["class"], "Lua error")
        self.assertTrue(payload["crashed"])

    def test_missing_file_returns_error_code(self):
        import contextlib
        import io

        with contextlib.redirect_stderr(io.StringIO()):
            code = xraylog.main([str(SAMPLES / "nope.log")])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
