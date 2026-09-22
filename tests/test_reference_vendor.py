from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import fill_reference_addons  # noqa: E402
import lint_addon  # noqa: E402
from test_fill_reference import run_fill  # noqa: E402
from test_xdb_unpack import build_uncompressed_archive  # noqa: E402


def _write(path: Path, text: str = "x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ResolveVendorSourceTests(unittest.TestCase):
    def test_prefers_vendor_over_addons(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "reference"
            name = "BusyHands_vendor"
            vendor = root / "vendor" / name
            addons = root / "addons" / name
            _write(vendor / "scripts" / "a.script", "-- from vendor\n")
            _write(addons / "scripts" / "a.script", "-- from addons\n")
            found = lint_addon.resolve_vendor_source(root, name)
            self.assertEqual(found, vendor)

    def test_falls_back_to_addons(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "reference"
            name = "Burn_Shit"
            addons = root / "addons" / name
            _write(addons / "scripts" / "a.script")
            found = lint_addon.resolve_vendor_source(root, name)
            self.assertEqual(found, addons)

    def test_missing_returns_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "reference"
            root.mkdir()
            self.assertIsNone(lint_addon.resolve_vendor_source(root, "nope"))


class FillLeavesVendorAloneTests(unittest.TestCase):
    def test_fill_reference_does_not_touch_vendor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            game = root / "game"
            db = game / "db"
            reference = root / "reference"
            vendor_marker = reference / "vendor" / "KeepMe" / "scripts" / "sentinel.script"
            _write(vendor_marker, "-- do not delete\n")
            archive = db / "configs.xdb0"
            archive.parent.mkdir(parents=True)
            archive.write_bytes(
                build_uncompressed_archive({"scripts\\hello.script": b"-- hello"})
            )
            code, out = run_fill(game, reference)
            self.assertEqual(code, 0, msg=out)
            self.assertTrue(vendor_marker.is_file())
            self.assertEqual(vendor_marker.read_text(encoding="utf-8"), "-- do not delete\n")
            self.assertIn("reference/vendor/", out)

    def test_fill_addons_prune_does_not_touch_vendor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            mo2 = root / "mo2"
            mods = mo2 / "mods"
            profile = mo2 / "profiles" / "Default"
            profile.mkdir(parents=True)
            (mo2 / "ModOrganizer.ini").write_text(
                "[General]\nselected_profile=@ByteArray(Default)\n",
                encoding="utf-8",
            )
            (profile / "modlist.txt").write_text("+SomeMod\n", encoding="utf-8")
            gamedata = mods / "SomeMod" / "gamedata" / "scripts"
            _write(gamedata / "a.script", "-- a\n")
            reference = root / "reference"
            vendor_marker = (
                reference / "vendor" / "BusyHands_v0" / "scripts" / "keep.script"
            )
            _write(vendor_marker, "-- vendor keep\n")
            stale = reference / "addons" / "StaleMod" / "scripts" / "old.script"
            _write(stale, "-- stale\n")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
                code = fill_reference_addons.main(
                    [
                        str(mo2),
                        "--reference",
                        str(reference),
                        "--prune",
                        "--yes",
                    ]
                )
            out = buffer.getvalue()
            self.assertEqual(code, 0, msg=out)
            self.assertTrue(vendor_marker.is_file())
            self.assertEqual(
                vendor_marker.read_text(encoding="utf-8"), "-- vendor keep\n"
            )
            self.assertFalse(stale.exists())
            self.assertIn("reference/vendor/", out)


class Fork001VendorPathTests(unittest.TestCase):
    def test_fork_finds_origin_under_vendor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            origin_name = "Vendor_Original_v1"
            origin = root / "reference" / "vendor" / origin_name
            _write(origin / "scripts" / "core.script")
            _write(origin / "scripts" / "gone.script")
            addon = root / "addon" / "fork_mod"
            _write(
                addon / "meta.ini",
                f"vendor_fork=1\nvendor_source={origin_name}\n",
            )
            _write(addon / "gamedata" / "scripts" / "core.script")
            findings = [
                f
                for f in lint_addon.lint(
                    addon,
                    lint_addon.ReferenceView(),
                    verify=False,
                    reference_root=root / "reference",
                )
                if f.code == "FORK-001"
            ]
            self.assertEqual(len(findings), 1)
            self.assertIn("gone.script", findings[0].message)


class PackBhsVendorDirTests(unittest.TestCase):
    def test_pack_uses_reference_vendor_first(self):
        from test_pack_bhs import (  # noqa: PLC0415
            OVERLAY_SCRIPTS,
            SEQLOAD_SOURCE,
            VENDOR_NAME,
            pack_quiet,
            write,
            write_overlay_meta,
            write_vendor_full_files,
        )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            vendor = repo / "reference" / "vendor" / VENDOR_NAME
            write(vendor / "scripts" / "from_vendor_dir.script")
            write_vendor_full_files(vendor)
            decoy = repo / "reference" / "addons" / VENDOR_NAME
            write(decoy / "scripts" / "from_addons_decoy.script")
            write_vendor_full_files(decoy)
            write(
                repo
                / "reference"
                / "addons"
                / "mags_redux"
                / "scripts"
                / "sequential_load_magazine.script",
                SEQLOAD_SOURCE,
            )
            overlay = repo / "addon" / "anthology_busyhands_stability_fix"
            for name in OVERLAY_SCRIPTS:
                write(overlay / "gamedata" / "scripts" / name)
            write(overlay / "CHANGELOG.md", "## [0.9.9]\n")
            write_overlay_meta(overlay)
            archive = pack_quiet(repo)
            with zipfile.ZipFile(archive) as zf:
                names = zf.namelist()
            self.assertIn("gamedata/scripts/from_vendor_dir.script", names)
            self.assertNotIn("gamedata/scripts/from_addons_decoy.script", names)


if __name__ == "__main__":
    unittest.main()
