"""Tests for tools/mod_mine.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from mod_mine import ModCatalogEntry, scan_log_for_mods


class LoadHintTests(unittest.TestCase):
    def test_initialized_counts_as_loaded_hint(self) -> None:
        catalog = {
            "seamless_inventory_sort_anthology": ModCatalogEntry(
                "seamless_inventory_sort_anthology",
                ("[seamless_inventory_sort_anthology]",),
            ),
        }
        scan = scan_log_for_mods(
            ["[seamless_inventory_sort_anthology] loaded v1.5.6"],
            catalog,
        )
        self.assertTrue(scan.present["seamless_inventory_sort_anthology"].loaded_hint)

    def test_probe_presence_line_matches_mod_id(self) -> None:
        catalog = {
            "fix_fdda_mcm_paths": ModCatalogEntry(
                "fix_fdda_mcm_paths",
                ("[fix_fdda_mcm_paths]", "fix_fdda_mcm_paths_presence.script"),
            ),
        }
        scan = scan_log_for_mods(
            ["[fix_fdda_mcm_paths] loaded v1.0.0"],
            catalog,
        )
        self.assertIn("fix_fdda_mcm_paths", scan.present)
        self.assertTrue(scan.present["fix_fdda_mcm_paths"].loaded_hint)


if __name__ == "__main__":
    unittest.main()
