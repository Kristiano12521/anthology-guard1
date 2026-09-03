from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import xraylog  # noqa: E402

SAMPLES = REPO_ROOT / "logs" / "samples"
FIXTURES = REPO_ROOT / "tests" / "fixtures"
ADDON_MINE = FIXTURES / "addon_mine"


def parse(name: str, *, addon_dir: Path | None = None) -> xraylog.LogReport:
    report = xraylog.LogReport(SAMPLES / name, addon_dir=addon_dir)
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
        self.assertEqual(groups[1].culprit, "sound_theme.script")
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
        mine_at = card.index("## Мои моды")
        errors_at = card.index("## Нефатальные ошибки")
        warnings_at = card.index("## Предупреждения")
        self.assertLess(mine_at, errors_at)
        self.assertLess(errors_at, warnings_at)
        self.assertIn("`axr_main.script` ×2", card)
        self.assertIn("`sound_theme.script` ×1", card)
        self.assertIn("Триггер:", card)
        self.assertIn("dxml_core.script", card)


class CulpritScriptTests(unittest.TestCase):
    def test_skips_abort_wrapper_and_c_frames(self):
        frames = [
            "... _g.script (line: 672) in function 'abort'",
            "... sound_theme.script (line: 644) in function <... sound_theme.script:614>",
            "[C]: in function 'object_sound'",
            "... sound_theme.script (line: 877) in function <... sound_theme.script:868>",
            "[C]: in function 'section_for_each'",
            "... sound_theme.script (line: 885) in function 'load_sound'",
            "... bind_stalker.script (line: 107) in function <... bind_stalker.script:100>",
        ]
        self.assertEqual(xraylog.culprit_script(frames), "sound_theme.script")

    def test_callback_set_keeps_axr_main(self):
        frames = [
            "... axr_main.script (line: 253) in function 'callback_set'",
            "... _g.script (line: 104) in function 'RSC'",
            "... dxml_core.script (line: 27) in function 'RegisterScriptCallback'",
            "... mas_scope_detach.script (line: 106) in function 'on_game_start'",
            "... axr_main.script (line: 359) in function 'on_game_start'",
            "... _g.script (line: 82) in function <... _g.script:73>",
        ]
        self.assertEqual(xraylog.culprit_script(frames), "axr_main.script")

    def test_skips_axr_main_dispatcher_after_abort(self):
        frames = [
            "... _g.script (line: 672) in function 'abort'",
            "... axr_main.script (line: 100) in function 'dispatch'",
            "... my_mod.script (line: 10) in function 'foo'",
        ]
        self.assertEqual(xraylog.culprit_script(frames), "my_mod.script")

    def test_all_infra_falls_back_to_top_frame(self):
        frames = [
            "... _g.script (line: 672) in function 'abort'",
            "[C]: in function 'lua_error'",
            "... axr_main.script (line: 359) in function 'on_game_start'",
            "... _g.script (line: 82) in function <... _g.script:73>",
        ]
        self.assertEqual(xraylog.culprit_script(frames), "_g.script")


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
        self.assertIn("## Мои моды", card)
        self.assertIn("## Нефатальные ошибки", card)
        self.assertNotIn("## Предупреждения", card)
        self.assertNotIn("## FATAL ERROR", card)
        self.assertNotIn("## Последние строки лога", card)

    def test_missing_file_returns_error_code(self):
        with contextlib.redirect_stderr(io.StringIO()):
            code = xraylog.main([str(SAMPLES / "nope.log")])
        self.assertEqual(code, 2)


class ArchiveCardTests(unittest.TestCase):
    def test_name_includes_date_and_source_stem(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = xraylog.unique_archive_path(
                Path(tmp),
                Path(r"C:\Users\someone\AppData\xray_barkid.log"),
                analyzed_on=date(2026, 8, 31),
            )
            self.assertEqual(path.name, "2026-08-31_xray_barkid.md")

    def test_collision_adds_numeric_suffix(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            (dest / "2026-08-31_xray_barkid.md").write_text("first\n", encoding="utf-8")
            second = xraylog.unique_archive_path(
                dest, Path("xray_barkid.log"), analyzed_on=date(2026, 8, 31)
            )
            self.assertEqual(second.name, "2026-08-31_xray_barkid-2.md")
            second.write_text("second\n", encoding="utf-8")
            third = xraylog.unique_archive_path(
                dest, Path("xray_barkid.log"), analyzed_on=date(2026, 8, 31)
            )
            self.assertEqual(third.name, "2026-08-31_xray_barkid-3.md")

    def test_windows_copy_suffix_stripped_from_archive_name(self):
        """Лог «xray_mg9000 (1).log» → stem без « (1)»; коллизия даёт -2, не скобки."""
        self.assertEqual(
            xraylog.archive_source_stem(Path(r"C:\tmp\xray_mg9000 (1).log")),
            "xray_mg9000",
        )
        self.assertEqual(
            xraylog.archive_source_stem(Path("xray_mg9000 (12).log")),
            "xray_mg9000",
        )
        self.assertEqual(
            xraylog.archive_source_stem(Path("xray_mg9000.log")),
            "xray_mg9000",
        )
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            bare = xraylog.unique_archive_path(
                dest,
                Path("xray_mg9000 (1).log"),
                analyzed_on=date(2026, 9, 3),
            )
            self.assertEqual(bare.name, "2026-09-03_xray_mg9000.md")
            bare.write_text("first\n", encoding="utf-8")
            second = xraylog.unique_archive_path(
                dest,
                Path("xray_mg9000 (2).log"),
                analyzed_on=date(2026, 9, 3),
            )
            self.assertEqual(second.name, "2026-09-03_xray_mg9000-2.md")
            self.assertNotIn(" (", second.name)

    def test_markdown_header_has_filename_not_absolute_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / "Users" / "UniqueUserXYZ" / "AppData"
            fake.mkdir(parents=True)
            src = SAMPLES / "crash_lua_nil.log"
            dest = fake / "xray_barkid.log"
            shutil.copy(src, dest)
            report = xraylog.LogReport(dest)
            report.parse(context_lines=40)
            card = report.to_markdown(
                max_warnings=10, warnings_only=False, analyzed_on=date(2026, 8, 31)
            )
            header = "\n".join(card.splitlines()[:8])
            self.assertIn("- Файл: `xray_barkid.log`", header)
            self.assertIn("- Дата разбора: 2026-08-31", header)
            self.assertNotIn("UniqueUserXYZ", header)
            self.assertNotIn("Users", header)
            self.assertNotIn(str(dest), header)
            self.assertNotIn(dest.as_posix(), header)

    def test_markdown_header_strips_windows_path(self):
        report = parse("crash_lua_nil.log")
        report.path = Path(r"C:\Users\someone\AppData\xray_barkid.log")
        card = report.to_markdown(
            max_warnings=10, warnings_only=False, analyzed_on=date(2026, 8, 31)
        )
        header = "\n".join(card.splitlines()[:8])
        self.assertIn("# Карточка лога — xray_barkid.log", header)
        self.assertIn("- Файл: `xray_barkid.log`", header)
        self.assertNotIn("Users", header)
        self.assertNotIn("someone", header)
        self.assertNotIn("AppData", header)

    def test_archive_flag_writes_card_and_prints_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = xraylog.main(
                    [
                        str(SAMPLES / "crash_lua_nil.log"),
                        "--archive",
                        "--archive-dir",
                        str(dest),
                    ]
                )
            self.assertEqual(code, 0)
            files = list(dest.glob("*.md"))
            self.assertEqual(len(files), 1)
            expected = f"{date.today().isoformat()}_crash_lua_nil.md"
            self.assertEqual(files[0].name, expected)
            self.assertIn(expected, buffer.getvalue())
            card = files[0].read_text(encoding="utf-8")
            self.assertIn("- Дата разбора:", card)
            self.assertIn("- Файл: `crash_lua_nil.log`", card)


class MineSectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.log_path = FIXTURES / "xraylog_mine.log"
        self.report = xraylog.LogReport(self.log_path, addon_dir=ADDON_MINE)
        self.report.parse(context_lines=40)

    def test_loaded_mod_is_present(self) -> None:
        assert self.report.mod_scan is not None
        self.assertIn("mod_loaded", self.report.mod_scan.present)
        self.assertTrue(self.report.mod_scan.present["mod_loaded"].loaded_hint)
        self.assertIn("fix_trader_restock_callback", self.report.mod_scan.present)
        self.assertTrue(self.report.mod_scan.present["fix_trader_restock_callback"].loaded_hint)

    def test_failed_mod_has_failure_marker(self) -> None:
        assert self.report.mod_scan is not None
        presence = self.report.mod_scan.present["mod_failed"]
        self.assertTrue(presence.has_failures)
        self.assertIn("guard NOT installed", next(iter(presence.failure_lines)))

    def test_missing_mod_listed_as_absent(self) -> None:
        assert self.report.mod_scan is not None
        self.assertIn("mod_missing", self.report.mod_scan.absent)
        self.assertNotIn("mod_missing", self.report.mod_scan.present)

    def test_markdown_mine_before_nonfatal(self) -> None:
        report = parse("nonfatal_traceback.log", addon_dir=ADDON_MINE)
        card = report.to_markdown(max_warnings=10, warnings_only=False)
        self.assertLess(card.index("## Мои моды"), card.index("## Нефатальные ошибки"))

    def test_errors_only_includes_mine_with_loaded_mod(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = xraylog.main(
                [
                    str(self.log_path),
                    "--errors-only",
                    "--addon-dir",
                    str(ADDON_MINE),
                ]
            )
        self.assertEqual(code, 0)
        card = buffer.getvalue()
        self.assertIn("## Мои моды", card)
        self.assertIn("trader_on_restock added", card)
        self.assertIn("Send wrap installed", card)
        self.assertIn("`fix_trader_restock_callback`", card)
        self.assertIn("`mod_loaded`", card)
        self.assertIn("### Не появились в логе", card)
        self.assertIn("`mod_missing`", card)
        self.assertNotIn("## Предупреждения", card)
        self.assertNotIn("## Последние строки лога", card)

    def test_warnings_only_includes_mine_section(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = xraylog.main(
                [
                    str(self.log_path),
                    "--warnings-only",
                    "--addon-dir",
                    str(ADDON_MINE),
                ]
            )
        self.assertEqual(code, 0)
        card = buffer.getvalue()
        self.assertIn("## Мои моды", card)
        self.assertIn("trader_on_restock added", card)
        self.assertNotIn("## FATAL ERROR", card)

    def test_mine_flag_outputs_only_mine_section(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = xraylog.main(
                [
                    str(self.log_path),
                    "--mine",
                    "--addon-dir",
                    str(ADDON_MINE),
                ]
            )
        self.assertEqual(code, 0)
        card = buffer.getvalue()
        self.assertIn("# Мои моды — xraylog_mine.log", card)
        self.assertIn("### Не появились в логе (1)", card)
        self.assertIn("`mod_missing`", card)
        self.assertIn("### С отказами (1)", card)
        self.assertIn("`mod_failed`", card)
        self.assertIn("### В логе без отказов (2)", card)
        self.assertIn("`mod_loaded`", card)
        self.assertIn("`fix_trader_restock_callback`", card)
        self.assertNotIn("## Нефатальные ошибки", card)
        self.assertNotIn("## FATAL ERROR", card)

    def test_json_includes_mod_scan(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = xraylog.main(
                [
                    str(self.log_path),
                    "--json",
                    "--addon-dir",
                    str(ADDON_MINE),
                ]
            )
        self.assertEqual(code, 0)
        payload = json.loads(buffer.getvalue())
        self.assertIn("mod_missing", payload["mods"]["absent"])
        self.assertIn("mod_loaded", payload["mods"]["present"])


if __name__ == "__main__":
    unittest.main()
