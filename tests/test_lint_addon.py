from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta
from pathlib import Path
from unittest.mock import patch

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

    def test_load_order_prefix_on_ltx_is_error(self):
        self.assertIn("ORDER-001", self.codes)
        finding = next(f for f in self.findings if f.code == "ORDER-001")
        self.assertEqual(finding.severity, "error")
        self.assertTrue(finding.path.endswith(".ltx"))

    def test_script_load_order_prefix_is_warning(self):
        self.assertIn("ORDER-002", self.codes)
        finding = next(f for f in self.findings if f.code == "ORDER-002")
        self.assertEqual(finding.severity, "warn")
        self.assertTrue(finding.path.endswith(".script"))

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

    def test_no_warnings_except_unverified(self):
        warns = [f for f in self.findings if f.severity == "warn"]
        self.assertEqual({f.code for f in warns}, {"VERIFY-001"}, msg=[f.format() for f in warns])


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
        self.assertIn("ORDER-002", codes)


def _minimal_addon(root: Path, name: str, *, meta_extra: str = "") -> Path:
    addon = root / name
    scripts = addon / "gamedata" / "scripts"
    configs = addon / "gamedata" / "configs" / "items"
    scripts.mkdir(parents=True)
    configs.mkdir(parents=True)
    (addon / "meta.ini").write_text(
        "[General]\nversion=1.0.0\n" + meta_extra, encoding="utf-8"
    )
    (addon / "CHANGELOG.md").write_text("# fixture\n", encoding="utf-8")
    return addon


class LoadOrderScriptTests(unittest.TestCase):
    def test_justification_in_first_ten_lines_suppresses_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = _minimal_addon(Path(tmp), "order_ok")
            script = addon / "gamedata" / "scripts" / "zzzz_after_magazine.script"
            script.write_text(
                "-- load-order: после sequential_load_magazine.script\n"
                "function on_game_start() end\n",
                encoding="cp1251",
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView())
            self.assertNotIn("ORDER-002", {f.code for f in findings})
            self.assertNotIn("ORDER-001", {f.code for f in findings})

    def test_justification_after_line_ten_does_not_suppress(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = _minimal_addon(Path(tmp), "order_late")
            script = addon / "gamedata" / "scripts" / "zzzz_late.script"
            header = "\n".join(f"-- pad {i}" for i in range(1, 11))
            script.write_text(
                header + "\n-- load-order: после foo.script\nfunction on_game_start() end\n",
                encoding="cp1251",
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView())
            self.assertIn("ORDER-002", {f.code for f in findings})

    def test_comment_without_target_does_not_suppress(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = _minimal_addon(Path(tmp), "order_empty")
            script = addon / "gamedata" / "scripts" / "zzzz_empty.script"
            script.write_text(
                "-- load-order: после\nfunction on_game_start() end\n",
                encoding="cp1251",
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView())
            self.assertIn("ORDER-002", {f.code for f in findings})


class VendorForkTests(unittest.TestCase):
    def _make_noisy_fork(self, root: Path, *, vendor_fork: bool) -> Path:
        extra = "vendor_fork=1\n" if vendor_fork else ""
        addon = _minimal_addon(root, "fork_mod" if vendor_fork else "plain_mod", meta_extra=extra)
        (addon / "NOTES.txt").write_text("extra docs\n", encoding="utf-8")
        (addon / "gamedata" / "scripts" / "itms_manager.script").write_text(
            "function on_game_start()\n"
            '  RegisterScriptCallback("actor_on_first_update", function() end)\n'
            "end\n",
            encoding="utf-8",
        )
        (addon / "gamedata" / "configs" / "items" / "items_food.ltx").write_text(
            "[food]\ncalories = 1\n", encoding="utf-8"
        )
        return addon

    def test_silences_replacement_and_stray_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._make_noisy_fork(Path(tmp), vendor_fork=True)
            codes = {f.code for f in lint_addon.lint(addon, build_reference())}
            self.assertNotIn("LUA-001", codes)
            self.assertNotIn("LTX-001", codes)
            self.assertNotIn("STRUCT-005", codes)

    def test_keeps_other_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._make_noisy_fork(Path(tmp), vendor_fork=True)
            codes = {f.code for f in lint_addon.lint(addon, build_reference())}
            self.assertIn("LUA-002", codes)
            self.assertIn("VERIFY-001", codes)

    def test_without_flag_still_reports_noise(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._make_noisy_fork(Path(tmp), vendor_fork=False)
            codes = {f.code for f in lint_addon.lint(addon, build_reference())}
            self.assertIn("LUA-001", codes)
            self.assertIn("LTX-001", codes)
            self.assertIn("STRUCT-005", codes)
            self.assertIn("LUA-002", codes)

    def test_summary_mentions_fork_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_noisy_fork(root, vendor_fork=True)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                lint_addon.main(
                    [
                        "fork_mod",
                        "--addon-root",
                        str(root),
                        "--reference",
                        str(FIXTURE_REFERENCE),
                    ]
                )
            self.assertIn("профиле форка", buf.getvalue())


class Fork001Tests(unittest.TestCase):
    ORIGIN = "Vendor_Original_v1"

    def _write(self, path: Path, name: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"-- {name}\n", encoding="utf-8")

    def _pair(
        self,
        root: Path,
        *,
        origin_files: list[str],
        our_files: list[str],
        vendor_source: str | None,
    ) -> tuple[Path, Path]:
        origin = root / "reference" / "addons" / self.ORIGIN
        for relpath in origin_files:
            self._write(origin.joinpath(*relpath.split("/")), relpath)
        extra = "vendor_fork=1\n"
        if vendor_source is not None:
            extra += f"vendor_source={vendor_source}\n"
        addon = _minimal_addon(root, "fork_mod", meta_extra=extra)
        for relpath in our_files:
            self._write(addon / "gamedata" / Path(*relpath.split("/")), relpath)
        return addon, root / "reference"

    def _fork001(self, addon: Path, reference_root: Path) -> list:
        return [
            f
            for f in lint_addon.lint(
                addon, lint_addon.ReferenceView(), verify=False, reference_root=reference_root
            )
            if f.code == "FORK-001"
        ]

    def test_missing_original_file_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon, ref = self._pair(
                Path(tmp),
                origin_files=["scripts/core.script", "scripts/gone.script"],
                our_files=["scripts/core.script"],
                vendor_source=self.ORIGIN,
            )
            hit = self._fork001(addon, ref)
            self.assertEqual(len(hit), 1)
            self.assertEqual(hit[0].severity, "warn")
            self.assertIn("gone.script", hit[0].message)
            self.assertNotIn("core.script", hit[0].message)

    def test_prefixed_rename_is_not_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon, ref = self._pair(
                Path(tmp),
                origin_files=["scripts/keep_me.script", "scripts/also_keep.script"],
                our_files=["scripts/zzzzzz_keep_me.script", "scripts/aaa_also_keep.script"],
                vendor_source=self.ORIGIN,
            )
            hit = self._fork001(addon, ref)
            self.assertEqual(hit, [], msg=[f.format() for f in hit])

    def test_our_addition_is_not_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon, ref = self._pair(
                Path(tmp),
                origin_files=["scripts/core.script"],
                our_files=["scripts/core.script", "scripts/our_extra.script"],
                vendor_source=self.ORIGIN,
            )
            hit = self._fork001(addon, ref)
            self.assertEqual(hit, [], msg=[f.format() for f in hit])

    def test_without_vendor_source_is_silent_except_notice(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon, ref = self._pair(
                Path(tmp),
                origin_files=["scripts/core.script", "scripts/gone.script"],
                our_files=["scripts/core.script"],
                vendor_source=None,
            )
            hit = self._fork001(addon, ref)
            self.assertEqual(len(hit), 1)
            self.assertEqual(hit[0].severity, "warn")
            self.assertIn("vendor_source", hit[0].message)
            self.assertNotIn("gone.script", hit[0].message)


class CrossModTests(unittest.TestCase):
    _CMO_DIR = Path("gamedata") / "configs" / "plugins" / "context_menu_overhaul"
    _BASE = "[functor_icons]\na=1\n[label_icons]\na=1\n[groups]\na=1\n[colors]\na=1\n"
    _PATCH = "![functor_icons]\na=1\n![label_icons]\na=1\n![groups]\na=1\n![colors]\na=1\n"

    def _cmo_pair(self, root: Path) -> tuple[Path, Path]:
        cmo = _minimal_addon(root, "context_menu_overhaul_anthology")
        burn = _minimal_addon(root, "burnshit_inventory_destroy")
        (cmo / self._CMO_DIR).mkdir(parents=True, exist_ok=True)
        (cmo / self._CMO_DIR / "menu.ltx").write_text(self._BASE, encoding="utf-8")
        (burn / self._CMO_DIR).mkdir(parents=True, exist_ok=True)
        (burn / self._CMO_DIR / "mod_menu_burnshit_inventory_destroy.ltx").write_text(
            self._PATCH, encoding="utf-8"
        )
        return cmo, burn

    def test_resolve_dltx_maps_patch_to_original(self):
        target = lint_addon.resolve_dltx_target(
            "configs/plugins/context_menu_overhaul/mod_menu_burnshit_inventory_destroy.ltx",
            {"configs/plugins/context_menu_overhaul": {"menu"}},
            set(),
        )
        self.assertEqual(target, "configs/plugins/context_menu_overhaul/menu.ltx")

    def test_conflict_on_same_gamedata_path_and_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            cmo, burn = self._cmo_pair(Path(tmp))
            findings = lint_addon.cross_conflicts([cmo, burn])
            self.assertEqual(len(findings), 1)
            finding = findings[0]
            self.assertEqual(finding.code, "CROSS-001")
            self.assertEqual(finding.severity, "warn")
            self.assertEqual(finding.path, "configs/plugins/context_menu_overhaul/menu.ltx")
            for section in ("colors", "groups", "functor_icons", "label_icons"):
                self.assertIn(f"[{section}]", finding.message)
            self.assertIn("burnshit_inventory_destroy", finding.message)
            self.assertIn("context_menu_overhaul_anthology", finding.message)
            self.assertIn("MO2", finding.message)

    def test_same_section_in_different_files_is_not_conflict(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            escape = _minimal_addon(root, "fix_escape")
            garbage = _minimal_addon(root, "fix_garbage")
            scripts = Path("gamedata") / "configs" / "scripts"
            (escape / scripts).mkdir(parents=True, exist_ok=True)
            (garbage / scripts).mkdir(parents=True, exist_ok=True)
            (escape / scripts / "l01_escape.ltx").write_text("[sr_idle]\na=1\n", encoding="utf-8")
            (garbage / scripts / "l02_garbage.ltx").write_text("[sr_idle]\na=1\n", encoding="utf-8")
            self.assertEqual(lint_addon.cross_conflicts([escape, garbage]), [])

    def test_cli_cross_reports_conflict(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._cmo_pair(root)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = lint_addon.main(
                    [
                        "--cross",
                        "--addon-root",
                        str(root),
                        "--reference",
                        str(root / "missing_reference"),
                    ]
                )
            out = buf.getvalue()
            self.assertEqual(code, 0)
            self.assertIn("CROSS-001", out)
            self.assertIn("Перекрёстные конфликты", out)
            self.assertIn("порядок в MO2", out)

    def test_without_flag_does_not_report_cross(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._cmo_pair(root)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                lint_addon.main(
                    [
                        "--addon-root",
                        str(root),
                        "--reference",
                        str(root / "missing_reference"),
                    ]
                )
            out = buf.getvalue()
            self.assertNotIn("CROSS-001", out)
            self.assertNotIn("Перекрёстные конфликты", out)


class VerifiedMetaTests(unittest.TestCase):
    def _addon_with_script(self, root: Path, name: str, *, meta_extra: str = "") -> tuple[Path, Path]:
        addon = _minimal_addon(root, name, meta_extra=meta_extra)
        script = addon / "gamedata" / "scripts" / f"{name}.script"
        script.write_text("function on_game_start() end\n", encoding="utf-8")
        return addon, script

    def _stamp(self, path: Path, when: date) -> None:
        ts = datetime.combine(when, datetime.min.time()).timestamp()
        os.utime(path, (ts, ts))

    def test_missing_keys_warns_unverified(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon, _ = self._addon_with_script(Path(tmp), "never_played")
            findings = [f for f in lint_addon.lint(addon, lint_addon.ReferenceView()) if f.code == "VERIFY-001"]
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].severity, "warn")
            self.assertEqual(findings[0].message, "в игре не проверялся")

    def test_fresh_keys_no_verify_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            today = date.today()
            extra = (
                f"verified_date={today.isoformat()}\n"
                "verified_build=Anthology 2.1 / Modded Exes MT test\n"
                "verified_note=загрузка сейва и меню\n"
            )
            addon, script = self._addon_with_script(Path(tmp), "fresh_mod", meta_extra=extra)
            self._stamp(script, today)
            changelog = addon / "CHANGELOG.md"
            self._stamp(changelog, today + timedelta(days=30))
            findings = [f for f in lint_addon.lint(addon, lint_addon.ReferenceView()) if f.code == "VERIFY-001"]
            self.assertEqual(findings, [])

    def test_stale_after_verified_date_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            verified = date.today() - timedelta(days=7)
            extra = (
                f"verified_date={verified.isoformat()}\n"
                "verified_build=Anthology 2.1 / Modded Exes MT test\n"
                "verified_note=старый прогон\n"
            )
            addon, script = self._addon_with_script(Path(tmp), "stale_mod", meta_extra=extra)
            self._stamp(script, date.today())
            findings = [f for f in lint_addon.lint(addon, lint_addon.ReferenceView()) if f.code == "VERIFY-001"]
            self.assertEqual(len(findings), 1)
            self.assertEqual(
                findings[0].message,
                f"изменён после последней проверки в игре: {verified.isoformat()}",
            )

    def test_unverified_cli_lists_only_pending(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            today = date.today()
            old = today - timedelta(days=10)
            missing, _ = self._addon_with_script(root, "aaa_missing")
            fresh, fresh_script = self._addon_with_script(
                root,
                "bbb_fresh",
                meta_extra=f"verified_date={today.isoformat()}\n",
            )
            self._stamp(fresh_script, today)
            stale, stale_script = self._addon_with_script(
                root,
                "ccc_stale",
                meta_extra=f"verified_date={old.isoformat()}\n",
            )
            self._stamp(stale_script, today)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = lint_addon.main(
                    ["--unverified", "--addon-root", str(root), "--reference", str(root / "none")]
                )
            out = buf.getvalue()
            self.assertEqual(code, 0)
            self.assertIn("aaa_missing: в игре не проверялся", out)
            self.assertIn(f"ccc_stale: изменён после последней проверки в игре: {old.isoformat()}", out)
            self.assertNotIn("bbb_fresh", out)
            self.assertIsNotNone(missing)
            self.assertIsNotNone(fresh)
            self.assertIsNotNone(stale)

    def _cli(self, root: Path, extra: list[str], env: dict[str, str]) -> tuple[int, str]:
        buf = io.StringIO()
        with patch.dict(os.environ, env, clear=False):
            with contextlib.redirect_stdout(buf):
                code = lint_addon.main(
                    extra
                    + [
                        "--addon-root",
                        str(root),
                        "--reference",
                        str(root / "none"),
                    ]
                )
        return code, buf.getvalue()

    def test_no_verify_flag_skips_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._addon_with_script(root, "never_played")
            code, out = self._cli(
                root,
                ["never_played", "--no-verify"],
                {"CI": "", "GITHUB_ACTIONS": ""},
            )
            self.assertEqual(code, 0)
            self.assertNotIn("VERIFY-001", out)
            self.assertNotIn("в игре не проверялся", out)
            self.assertIn("Проверка в игре пропущена: --no-verify", out)

    def test_ci_env_skips_verify(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._addon_with_script(root, "never_played")
            code, out = self._cli(
                root,
                ["never_played"],
                {"CI": "true", "GITHUB_ACTIONS": ""},
            )
            self.assertEqual(code, 0)
            self.assertNotIn("VERIFY-001", out)
            self.assertNotIn("в игре не проверялся", out)
            self.assertIn("Проверка в игре пропущена: переменная CI", out)

    def test_unverified_runs_when_mtime_untrusted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._addon_with_script(root, "aaa_missing")
            code, out = self._cli(
                root,
                ["--unverified"],
                {"CI": "true", "GITHUB_ACTIONS": ""},
            )
            self.assertEqual(code, 0)
            self.assertIn("aaa_missing: в игре не проверялся", out)
            self.assertIn("mtime в этом окружении недостоверен", out)
            self.assertIn("переменная CI", out)


class TimeEventLintTests(unittest.TestCase):
    def _script(self, root: Path, name: str, source: str, encoding: str = "utf-8") -> Path:
        addon = _minimal_addon(root, name)
        script = addon / "gamedata" / "scripts" / f"{name}.script"
        script.write_text(source, encoding=encoding)
        return addon

    def test_named_functor_without_return_true_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "leak_event",
                "local function retry_install()\n"
                "    return false\n"
                "end\n"
                "function on_game_start()\n"
                '    CreateTimeEvent("mod", "late", 1, retry_install)\n'
                "end\n",
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)
            hit = [f for f in findings if f.code == "LUA-006"]
            self.assertEqual(len(hit), 1)
            self.assertEqual(hit[0].severity, "warn")
            self.assertIn("retry_install", hit[0].message)

    def test_named_functor_with_return_true_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "ok_event",
                "local function repair_tick()\n"
                "    return true\n"
                "end\n"
                "function on_game_start()\n"
                '    CreateTimeEvent("mod", "tick", 1, repair_tick)\n'
                "end\n",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-006", codes)
            self.assertNotIn("LUA-007", codes)

    def test_return_helper_that_returns_true_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "return_helper",
                "local function finish_repair()\n"
                "    return true\n"
                "end\n"
                "function repair_tick()\n"
                "    return finish_repair()\n"
                "end\n"
                "function on_game_start()\n"
                '    CreateTimeEvent("mod", "tick", 1, repair_tick)\n'
                "end\n",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-006", codes)

    def test_self_create_then_return_true_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "dead_retry",
                "local EVENT_ID = \"mod\"\n"
                "local REPAIR_ACTION = \"tick\"\n"
                "function repair_tick()\n"
                "    CreateTimeEvent(EVENT_ID, REPAIR_ACTION, 1, repair_tick)\n"
                "    return true\n"
                "end\n"
                "function on_game_start()\n"
                "    CreateTimeEvent(EVENT_ID, REPAIR_ACTION, 1, repair_tick)\n"
                "end\n",
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)
            hit = [f for f in findings if f.code == "LUA-007"]
            self.assertEqual(len(hit), 1)
            self.assertIn("repair_tick", hit[0].message)

    def test_reset_then_return_false_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "reset_retry",
                "function repair_tick()\n"
                "    if done then return true end\n"
                '    ResetTimeEvent("mod", "tick", 1)\n'
                "    return false\n"
                "end\n"
                "function on_game_start()\n"
                '    CreateTimeEvent("mod", "tick", 1, repair_tick)\n'
                "end\n",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-006", codes)
            self.assertNotIn("LUA-007", codes)

    def test_create_other_event_then_return_true_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "other_event",
                "local function late()\n"
                "    return true\n"
                "end\n"
                "local function first()\n"
                '    CreateTimeEvent("mod", "late", 1, late)\n'
                "    return true\n"
                "end\n"
                "function on_game_start()\n"
                '    CreateTimeEvent("mod", "first", 0, first)\n'
                "end\n",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-007", codes)

    def test_alife_id_scan_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "id_scan",
                "local MAX_ALIFE_ID = 65534\n"
                "local function scan()\n"
                "    for id = 1, MAX_ALIFE_ID do\n"
                "        alife():object(id)\n"
                "    end\n"
                "end\n",
            )
            findings = lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)
            hit = [f for f in findings if f.code == "LUA-008"]
            self.assertEqual(len(hit), 1)
            self.assertGreater(hit[0].line, 0)

    def test_commented_alife_scan_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "id_scan_comment",
                "-- ZIP scanned for id = 1, 65534 on every first_update\n"
                "function on_game_start() end\n",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-008", codes)

    def test_alife_scan_justification_before_loop_suppresses(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "id_scan_ok",
                "local MAX_ALIFE_ID = 65534\n"
                "local function scan()\n"
                "    -- alife-scan: запасной путь, iterate_objects отказал\n"
                "    for id = 1, MAX_ALIFE_ID do\n"
                "        alife():object(id)\n"
                "    end\n"
                "end\n",
                encoding="cp1251",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-008", codes)

    def test_alife_scan_justification_in_file_header_does_not_suppress(self):
        with tempfile.TemporaryDirectory() as tmp:
            pad = "\n".join(f"-- pad {i}" for i in range(1, 8))
            addon = self._script(
                Path(tmp),
                "id_scan_header",
                "-- alife-scan: запасной путь, iterate_objects отказал\n"
                f"{pad}\n"
                "local MAX_ALIFE_ID = 65534\n"
                "local function scan()\n"
                "    for id = 1, MAX_ALIFE_ID do\n"
                "        alife():object(id)\n"
                "    end\n"
                "end\n",
                encoding="cp1251",
            )
            self.assertIn(
                "LUA-008",
                {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)},
            )

    def test_alife_scan_justification_without_reason_does_not_suppress(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "id_scan_empty",
                "local MAX_ALIFE_ID = 65534\n"
                "local function scan()\n"
                "    -- alife-scan: запасной путь,\n"
                "    for id = 1, MAX_ALIFE_ID do\n"
                "        alife():object(id)\n"
                "    end\n"
                "end\n",
                encoding="cp1251",
            )
            self.assertIn(
                "LUA-008",
                {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)},
            )


class Lua003LintTests(unittest.TestCase):
    def _script(self, root: Path, name: str, source: str) -> Path:
        addon = _minimal_addon(root, name)
        (addon / "gamedata" / "scripts" / f"{name}.script").write_text(source, encoding="utf-8")
        return addon

    def test_on_xml_read_without_unregister_is_silent(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "modxml_ok",
                "function on_xml_read()\n"
                '    RegisterScriptCallback("on_xml_read", strip_pair)\n'
                "end\n",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LUA-003", codes)

    def test_other_callback_without_unregister_still_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "mixed_cb",
                "function on_xml_read()\n"
                '    RegisterScriptCallback("on_xml_read", strip_pair)\n'
                "end\n"
                "function on_game_start()\n"
                '    RegisterScriptCallback("actor_on_update", tick)\n'
                "end\n",
            )
            hit = [
                f
                for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)
                if f.code == "LUA-003"
            ]
            self.assertEqual(len(hit), 1)
            self.assertIn("actor_on_update", hit[0].message)
            self.assertNotIn("on_xml_read", hit[0].message)

    def test_pcall_unregister_does_not_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = self._script(
                Path(tmp),
                "pcall_unreg",
                "local function register_destroy(self)\n"
                '    RegisterScriptCallback("game_object_on_net_destroy", self)\n'
                "end\n"
                "local function unregister_destroy(self)\n"
                '    pcall(UnregisterScriptCallback, "game_object_on_net_destroy", self)\n'
                "end\n",
            )
            hit = [
                f
                for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)
                if f.code == "LUA-003"
            ]
            self.assertEqual(len(hit), 1)
            self.assertIn("game_object_on_net_destroy", hit[0].message)

    def test_inventory_antifreeze_still_warns(self):
        addon = REPO_ROOT / "addon" / "seamless_inventory_sort_anthology"
        findings = lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)
        hit = [
            f
            for f in findings
            if f.code == "LUA-003" and "inventory_antifreeze" in f.path.replace("\\", "/")
        ]
        self.assertEqual(len(hit), 1)
        self.assertIn("game_object_on_net_destroy", hit[0].message)


class LogPresenceTests(unittest.TestCase):
    def test_top_level_printf_detected(self):
        source = (
            'local LOG_TAG = "[demo_mod]"\n'
            'local VERSION = "1.0.0"\n'
            'printf("%s loaded v%s", LOG_TAG, VERSION)\n'
            "function on_game_start() end\n"
        )
        self.assertTrue(lint_addon.has_presence_log_marker(source))

    def test_on_game_start_early_log_detected(self):
        source = (
            'local LOG_TAG = "[demo_mod]"\n'
            "function on_game_start()\n"
            '    printf("%s loaded", LOG_TAG)\n'
            "    if false then end\n"
            "end\n"
        )
        self.assertTrue(lint_addon.has_presence_log_marker(source))

    def test_install_only_log_is_not_presence(self):
        source = (
            'local LOG_TAG = "[demo_mod]"\n'
            "local function log(fmt, ...)\n"
            '    printf(LOG_TAG .. " " .. fmt, ...)\n'
            "end\n"
            "local function install()\n"
            '    log("wrapped")\n'
            "end\n"
            "install()\n"
            "function on_game_start()\n"
            "    install()\n"
            "end\n"
        )
        self.assertFalse(lint_addon.has_presence_log_marker(source))

    def test_mcm_script_excluded_from_mod_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = _minimal_addon(Path(tmp), "presence_mcm")
            (addon / "gamedata" / "scripts" / "presence_mcm_mcm.script").write_text(
                'function on_mcm_load() return {} end\n', encoding="utf-8"
            )
            self.assertEqual(lint_addon.mod_presence_script_paths(addon), [])

    def test_log001_disabled_in_linter(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = _minimal_addon(Path(tmp), "presence_silent")
            (addon / "gamedata" / "scripts" / "presence_silent.script").write_text(
                "function on_game_start()\n"
                "    if true then end\n"
                "end\n",
                encoding="utf-8",
            )
            codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertNotIn("LOG-001", codes)

    def test_log001_fires_when_enabled(self):
        with tempfile.TemporaryDirectory() as tmp:
            addon = _minimal_addon(Path(tmp), "presence_missing")
            (addon / "gamedata" / "scripts" / "presence_missing.script").write_text(
                "function on_game_start()\n"
                "    if true then end\n"
                "end\n",
                encoding="utf-8",
            )
            with patch.object(lint_addon, "LOG_PRESENCE_CHECK_ENABLED", True):
                codes = {f.code for f in lint_addon.lint(addon, lint_addon.ReferenceView(), verify=False)}
            self.assertIn("LOG-001", codes)

    def test_current_addon_failures_above_threshold(self):
        count, _failed = lint_addon.count_presence_log_failures(REPO_ROOT / "addon")
        self.assertGreater(count, 10)
        self.assertFalse(lint_addon.LOG_PRESENCE_CHECK_ENABLED)


if __name__ == "__main__":
    unittest.main()
