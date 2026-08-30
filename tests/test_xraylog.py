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

    def test_no_nonfatal_section_in_markdown(self):
        card = self.report.to_markdown(max_warnings=10, warnings_only=False)
        self.assertNotIn("Нефатальные ошибки", card)


class NonfatalTracebackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = parse("nonfatal_traceback.log")

    def test_no_crash_but_repeating_errors(self):
        self.assertFalse(self.report.crashed)
        crash_class, hints = self.report.classify()
        self.assertEqual(crash_class, "вылета нет, есть повторяющиеся ошибки (2 групп)")
        self.assertTrue(any("Нефатальные ошибки" in hint for hint in hints))

    def test_groups_by_signature_without_line_numbers(self):
        groups = self.report.nonfatal_errors
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0].count, 2)
        self.assertEqual(groups[0].culprit, "axr_main.script")
        self.assertIn("trying to set callback actor_on_item_use to nil function", groups[0].trigger)
        self.assertTrue(
            any("mas_scope_detach.script (line: 106)" in frame for frame in groups[0].frames)
        )
        self.assertEqual(groups[1].count, 1)
        self.assertEqual(groups[1].culprit, "_g.script")
        self.assertEqual(groups[1].trigger, "")
        self.assertTrue(any("sound_theme.script" in frame for frame in groups[1].frames))

    def test_traceback_lines_excluded_from_warnings(self):
        warning_text = " ".join(self.report.warnings)
        self.assertNotIn("STACK TRACEBACK", warning_text)
        self.assertNotIn("trying to set callback", warning_text)
        self.assertNotIn("-----", warning_text)
        self.assertTrue(any("ui_icon_anth_pda" in text for text in self.report.warnings))
        self.assertTrue(any("my_fix_weapon_jam" in text for text in self.report.warnings))

    def test_markdown_lists_errors_before_warnings(self):
        card = self.report.to_markdown(max_warnings=10, warnings_only=False)
        self.assertNotIn("## FATAL ERROR", card)
        errors_at = card.index("## Нефатальные ошибки")
        warnings_at = card.index("## Предупреждения")
        self.assertLess(errors_at, warnings_at)
        self.assertIn("`axr_main.script` ×2", card)
        self.assertIn("Триггер:", card)
        self.assertIn("dxml_core.script", card)


class FatalSampleRegressionTests(unittest.TestCase):
    def test_lua_crash_classification_unchanged(self):
        report = parse("crash_lua_nil.log")
        crash_class, _ = report.classify()
        self.assertTrue(report.crashed)
        self.assertEqual(crash_class, "Lua error")
        self.assertEqual(report.nonfatal_errors, [])
        card = report.to_markdown(max_warnings=10, warnings_only=False)
        self.assertIn("## FATAL ERROR", card)
        self.assertNotIn("Нефатальные ошибки", card)

    def test_config_crash_classification_unchanged(self):
        report = parse("crash_missing_section.log")
        crash_class, _ = report.classify()
        self.assertTrue(report.crashed)
        self.assertEqual(crash_class, "конфиг: нет секции")
        self.assertEqual(report.nonfatal_errors, [])
        card = report.to_markdown(max_warnings=10, warnings_only=False)
        self.assertIn("## FATAL ERROR", card)
        self.assertNotIn("Нефатальные ошибки", card)


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
        self.assertEqual(payload["nonfatal_groups"], 0)

    def test_errors_only_hides_warnings_and_fatal(self):
        import contextlib
        import io

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = xraylog.main([str(SAMPLES / "nonfatal_traceback.log"), "--errors-only"])
        self.assertEqual(code, 0)
        card = buffer.getvalue()
        self.assertIn("## Нефатальные ошибки", card)
        self.assertNotIn("## Предупреждения", card)
        self.assertNotIn("## FATAL ERROR", card)

    def test_missing_file_returns_error_code(self):
        import contextlib
        import io

        with contextlib.redirect_stderr(io.StringIO()):
            code = xraylog.main([str(SAMPLES / "nope.log")])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
