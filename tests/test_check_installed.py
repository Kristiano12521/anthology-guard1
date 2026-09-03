from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import check_installed  # noqa: E402


def run_main(argv: list[str], env: dict[str, str] | None = None) -> tuple[int, str]:
    buf = io.StringIO()
    clean = {"CI": "", "GITHUB_ACTIONS": ""}
    if env:
        clean.update(env)
    with mock.patch.dict(os.environ, clean, clear=False):
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            code = check_installed.main(argv)
    return code, buf.getvalue()


class ParseBuildInfoTests(unittest.TestCase):
    def test_basic_fields(self):
        info = check_installed.parse_build_info(
            "\n".join(
                [
                    "mod_id: fix_example",
                    "version: 1.2.3",
                    "built: 2026-09-01T12:30:00",
                    "gamedata_files: 4",
                    "",
                ]
            )
        )
        self.assertEqual(info.mod_id, "fix_example")
        self.assertEqual(info.version, "1.2.3")
        self.assertEqual(info.built, datetime(2026, 9, 1, 12, 30, 0))

    def test_indented_vendor_lines_ignored(self):
        info = check_installed.parse_build_info(
            "\n".join(
                [
                    "mod_id: Anthology_BusyHands_Stability_Fix",
                    "version: 0.6.7",
                    "built: 2026-08-31T10:00:00",
                    "vendor_full_files:",
                    "  scripts/mon_sleep.script: 100 bytes",
                    "overlay: addon/anthology_busyhands_stability_fix",
                    "",
                ]
            )
        )
        self.assertEqual(info.mod_id, "Anthology_BusyHands_Stability_Fix")
        self.assertNotIn("scripts/mon_sleep.script", info.raw)


class CheckInstalledTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.mo2 = self.root / "mo2"
        self.mods = self.mo2 / "mods"
        self.addon = self.root / "addon"
        self.mods.mkdir(parents=True)
        self.addon.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _addon(self, mod_id: str, *, mtime: int | None = None) -> Path:
        path = self.addon / mod_id
        script = path / "gamedata" / "scripts" / f"{mod_id}.script"
        script.parent.mkdir(parents=True, exist_ok=True)
        script.write_text(f"-- {mod_id}\n", encoding="utf-8")
        if mtime is not None:
            os.utime(script, (mtime, mtime))
        return path

    def _package(
        self,
        mo2_name: str,
        *,
        mod_id: str,
        built: datetime,
        version: str = "1.0.0",
    ) -> Path:
        path = self.mods / mo2_name
        path.mkdir(parents=True, exist_ok=True)
        (path / "BUILD_INFO.txt").write_text(
            "\n".join(
                [
                    f"mod_id: {mod_id}",
                    f"version: {version}",
                    f"built: {built.isoformat(timespec='seconds')}",
                    "target: Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return path

    def test_current_when_built_after_source(self):
        base = int(datetime(2026, 9, 1, 12, 0, 0).timestamp())
        self._addon("fix_alpha", mtime=base)
        self._package(
            "fix_alpha",
            mod_id="fix_alpha",
            built=datetime(2026, 9, 1, 13, 0, 0),
        )
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertEqual(len(report.packages), 1)
        self.assertEqual(report.packages[0].status, "current")
        self.assertEqual(report.missing, [])

    def test_outdated_when_source_newer(self):
        built = datetime(2026, 9, 1, 12, 0, 0)
        newer = int((built + timedelta(hours=2)).timestamp())
        self._addon("fix_beta", mtime=newer)
        self._package("fix_beta", mod_id="fix_beta", built=built)
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertEqual(report.packages[0].status, "outdated")

    def test_missing_aio_member(self):
        self._addon("fix_gamma")
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertIn("fix_gamma", report.missing)

    def test_skip_and_separate_not_missing(self):
        import _pack_kristiano_aio as k

        for mod_id in k.SKIP:
            self._addon(mod_id)
        for mod_id in k.SEPARATE:
            self._addon(mod_id)
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        for mod_id in k.SKIP:
            self.assertNotIn(mod_id, report.missing)
        for mod_id in k.SEPARATE:
            self.assertNotIn(mod_id, report.missing)

    def test_aio_covers_member_and_compares_sources(self):
        import _pack_kristiano_aio as k

        built = datetime(2026, 9, 1, 12, 0, 0)
        older = int((built - timedelta(hours=1)).timestamp())
        newer = int((built + timedelta(hours=1)).timestamp())
        self._addon("fix_in_aio", mtime=older)
        self._addon("fix_fresh", mtime=newer)
        self._package(k.AIO_NAME, mod_id=k.AIO_NAME, built=built)
        with mock.patch(
            "check_installed.source_mod_ids",
            return_value=["fix_in_aio", "fix_fresh"],
        ):
            with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
                report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertEqual(report.packages[0].status, "outdated")
        self.assertNotIn("fix_in_aio", report.missing)
        self.assertNotIn("fix_fresh", report.missing)

    def test_ci_skips_mtime_comparison(self):
        base = int(datetime(2026, 9, 1, 12, 0, 0).timestamp())
        self._addon("fix_delta", mtime=base + 10_000)
        self._package(
            "fix_delta",
            mod_id="fix_delta",
            built=datetime(2026, 9, 1, 12, 0, 0),
        )
        with mock.patch.dict(os.environ, {"CI": "true", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertIsNotNone(report.mtime_untrusted)
        self.assertEqual(report.packages[0].status, "skipped")
        self.assertEqual(report.missing, [])
        code, out = run_main(
            [str(self.mo2), "--addon-root", str(self.addon)],
            env={"CI": "true", "GITHUB_ACTIONS": ""},
        )
        self.assertEqual(code, 0)
        self.assertIn("mtime недостоверен", out)
        self.assertIn("Сравнивать с addon/ нечего", out)
        self.assertNotIn("устарел:", out)

    def test_no_mtime_flag(self):
        self._addon("fix_eps")
        self._package(
            "fix_eps",
            mod_id="fix_eps",
            built=datetime(2026, 1, 1, 0, 0, 0),
        )
        code, out = run_main(
            [str(self.mo2), "--addon-root", str(self.addon), "--no-mtime"],
            env={"CI": "", "GITHUB_ACTIONS": ""},
        )
        self.assertEqual(code, 0)
        self.assertIn("mtime недостоверен", out)

    def test_cli_outdated_exit_one(self):
        built = datetime(2026, 9, 1, 12, 0, 0)
        self._addon("fix_zeta", mtime=int((built + timedelta(days=1)).timestamp()))
        self._package("fix_zeta", mod_id="fix_zeta", built=built)
        code, out = run_main(
            [str(self.mo2), "--addon-root", str(self.addon)],
            env={"CI": "", "GITHUB_ACTIONS": ""},
        )
        self.assertEqual(code, 1)
        self.assertIn("устарел:", out)

    def test_missing_mods_dir(self):
        code, out = run_main(
            [str(self.root / "empty"), "--addon-root", str(self.addon)],
            env={"CI": "", "GITHUB_ACTIONS": ""},
        )
        self.assertEqual(code, 2)
        self.assertIn("Нет такой папки MO2", out)

    def test_bhs_mod_id_maps_to_overlay(self):
        from build_prune import BHS_MOD_ID

        built = datetime(2026, 9, 1, 12, 0, 0)
        self._addon(BHS_MOD_ID, mtime=int((built - timedelta(hours=1)).timestamp()))
        self._package(
            "Anthology_BusyHands_Stability_Fix_v0_6_7",
            mod_id=check_installed.BHS_BUILD_MOD_ID,
            built=built,
        )
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertEqual(report.packages[0].status, "current")
        self.assertEqual(report.packages[0].source_mods, [BHS_MOD_ID])


if __name__ == "__main__":
    unittest.main()
