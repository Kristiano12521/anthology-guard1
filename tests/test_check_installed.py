from __future__ import annotations

import contextlib
import io
import json
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
    clean = {"CI": "", "GITHUB_ACTIONS": "", "ANTHOLOGY_MO2": ""}
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
            env={"CI": "", "GITHUB_ACTIONS": "", "ANTHOLOGY_MO2": ""},
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

    def test_mo2_from_env_when_no_arg(self):
        self._addon("fix_env")
        self._package(
            "fix_env",
            mod_id="fix_env",
            built=datetime(2026, 9, 1, 13, 0, 0),
        )
        script = self.addon / "fix_env" / "gamedata" / "scripts" / "fix_env.script"
        os.utime(script, (1_725_000_000, 1_725_000_000))
        code, out = run_main(
            ["--addon-root", str(self.addon)],
            env={
                "CI": "",
                "GITHUB_ACTIONS": "",
                "ANTHOLOGY_MO2": str(self.mo2),
            },
        )
        self.assertEqual(code, 0)
        self.assertIn(str(self.mo2), out)

    def test_mo2_missing_message(self):
        with mock.patch("check_installed.read_local_mo2", return_value=None):
            code, out = run_main(
                ["--addon-root", str(self.addon)],
                env={"CI": "", "GITHUB_ACTIONS": "", "ANTHOLOGY_MO2": ""},
            )
        self.assertEqual(code, 2)
        self.assertIn("Путь к MO2 не задан", out)
        self.assertIn("local.json", out)

    def test_mo2_from_local_json(self):
        config = self.root / "local.json"
        config.write_text(
            json.dumps({"mo2": str(self.mo2)}),
            encoding="utf-8",
        )
        self._addon("fix_cfg")
        self._package(
            "fix_cfg",
            mod_id="fix_cfg",
            built=datetime(2026, 9, 1, 13, 0, 0),
        )
        script = self.addon / "fix_cfg" / "gamedata" / "scripts" / "fix_cfg.script"
        os.utime(script, (1_725_000_000, 1_725_000_000))
        mo2, source = check_installed.resolve_mo2(
            None,
            env={"ANTHOLOGY_MO2": ""},
            config_path=config,
        )
        self.assertEqual(mo2, self.mo2)
        self.assertEqual(source, "local.json")

    def test_clone_like_mtime_skips_comparison(self):
        stamp = 1_725_100_000
        # достаточно файлов с почти одинаковым mtime
        for i in range(check_installed.CLONE_MTIME_MIN_FILES):
            mod_id = f"fix_clone_{i}"
            self._addon(mod_id, mtime=stamp + (i % 3))
        self._package(
            "fix_clone_0",
            mod_id="fix_clone_0",
            built=datetime(2020, 1, 1, 0, 0, 0),
        )
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertIsNotNone(report.mtime_untrusted)
        self.assertIn("git clone", report.mtime_untrusted or "")
        self.assertEqual(report.packages[0].status, "skipped")
        self.assertEqual(report.missing, [])

    def test_reinstall_lists_archive(self):
        import _pack_kristiano_aio as k

        built = datetime(2026, 9, 1, 12, 0, 0)
        newer = int((built + timedelta(hours=2)).timestamp())
        self._addon("fix_reinst", mtime=newer)
        self._package("fix_reinst", mod_id="fix_reinst", built=built)
        build = self.root / "build"
        build.mkdir()
        archive = build / "fix_reinst-1.0.0.zip"
        archive.write_bytes(b"PK")
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        items = check_installed.reinstall_items(
            report, build_root=build, addon_root=self.addon
        )
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].archive, archive)
        code, out = run_main(
            [
                str(self.mo2),
                "--addon-root",
                str(self.addon),
                "--build-root",
                str(build),
                "--reinstall",
            ],
            env={"CI": "", "GITHUB_ACTIONS": "", "ANTHOLOGY_MO2": ""},
        )
        self.assertEqual(code, 1)
        self.assertIn("заменить существующий", out)
        self.assertIn("fix_reinst-1.0.0.zip", out)
        self.assertNotIn(k.AIO_NAME, out)

    def test_reinstall_groups_missing_into_aio(self):
        import _pack_kristiano_aio as k

        self._addon("fix_need_aio")
        build = self.root / "build"
        build.mkdir()
        archive = build / f"{k.AIO_NAME}.zip"
        archive.write_bytes(b"PK")
        with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
            report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        items = check_installed.reinstall_items(
            report, build_root=build, addon_root=self.addon
        )
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].label, k.AIO_NAME)
        self.assertEqual(items[0].archive, archive)

    def test_reinstall_aio_once_despite_many_sources(self):
        """AIO с несколькими sources — один блок в «переустановить», с причиной и архивом."""
        import _pack_kristiano_aio as k
        import re

        built = datetime(2026, 9, 1, 12, 0, 0)
        newer = int((built + timedelta(hours=2)).timestamp())
        source_ids = [f"fix_aio_src_{i}" for i in range(8)]
        for mod_id in source_ids:
            self._addon(mod_id, mtime=newer)
        mo2_name = f"{k.AIO_NAME} NEW"
        self._package(mo2_name, mod_id=k.AIO_NAME, built=built)
        build = self.root / "build"
        build.mkdir()
        archive = build / f"{k.AIO_NAME}.zip"
        archive.write_bytes(b"PK")
        with mock.patch(
            "check_installed.source_mod_ids",
            return_value=source_ids,
        ):
            with mock.patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False):
                report = check_installed.check_installed(self.mo2, addon_root=self.addon)
        self.assertEqual(report.packages[0].status, "outdated")
        self.assertEqual(len(report.packages[0].source_mods), 8)
        items = check_installed.reinstall_items(
            report, build_root=build, addon_root=self.addon
        )
        aio_items = [i for i in items if i.label == mo2_name]
        self.assertEqual(len(aio_items), 1)
        self.assertEqual(aio_items[0].reason, "устарел")
        self.assertEqual(aio_items[0].archive, archive)
        out = check_installed.format_report(
            report, self.mo2, build_root=build, addon_root=self.addon
        )
        reinstall = out.split("переустановить", 1)[1]
        label_lines = re.findall(
            rf"^  {re.escape(mo2_name)}$", reinstall, flags=re.MULTILINE
        )
        self.assertEqual(len(label_lines), 1, reinstall)
        self.assertIn("причина: устарел", reinstall)
        self.assertIn("архив:", reinstall)
        self.assertIn(k.AIO_NAME + ".zip", reinstall)
        # блок «устарел» тоже один раз
        outdated = out.split("устарел:", 1)[1].split("\n\n", 1)[0]
        self.assertEqual(outdated.count(mo2_name), 1)


class ResolveMo2Tests(unittest.TestCase):
    def test_cli_wins_over_env(self):
        mo2, source = check_installed.resolve_mo2(
            Path("D:/from/cli"),
            env={"ANTHOLOGY_MO2": "D:/from/env"},
            config_path=Path("/nonexistent/local.json"),
        )
        self.assertEqual(mo2, Path("D:/from/cli"))
        self.assertEqual(source, "cli")

    def test_env_wins_over_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / "local.json"
            config.write_text('{"mo2": "D:/from/config"}', encoding="utf-8")
            mo2, source = check_installed.resolve_mo2(
                None,
                env={"ANTHOLOGY_MO2": "D:/from/env"},
                config_path=config,
            )
        self.assertEqual(mo2, Path("D:/from/env"))
        self.assertEqual(source, "env")


if __name__ == "__main__":
    unittest.main()
