from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import build_prune  # noqa: E402
import pack_bhs  # noqa: E402

# Минимальный MAG Redux для patch_seqload — те же якоря, что в test_pack_bhs.py.
SEQLOAD_SOURCE = """----------------------------------------------------------------
-- Sequential (alternating) magazine loading.
----------------------------------------------------------------
local presets = {}

local function take_one_round(pool)
	while #pool.boxes > 0 do
		local box = pool.boxes[1]
		local count = box:ammo_get_count()
		if count > 1 then
			box:ammo_set_count(count - 1)
			pool.total = pool.total - 1
			return true
		elseif count == 1 then
			alife_release_id(box:id())
			table.remove(pool.boxes, 1)
			pool.total = pool.total - 1
			return true
		else
			table.remove(pool.boxes, 1)
		end
	end
	return false
end

	-- Don't double-schedule.
	if in_progress[mag_id] then return end

	-- Don't show a second time if we're already loading this mag.
	if in_progress[obj:id()] then return false end
	return true

	-- If a gradual load is already running on this mag, ignore further clicks.
	if in_progress[mag_id] then return end
"""


def write(path: Path, text: str = "x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def stage_minimal_bhs_repo(root: Path) -> None:
    """Временный reference/addons + overlay, как setUp в test_pack_bhs.py."""
    vendor = root / "reference" / "addons" / "BusyHands_vendor"
    write(vendor / "scripts" / "vendor_bhs.script")
    write(vendor / "scripts" / "fix_bhs_fdda_loot.script", "-- loot sidecar\n")
    write(vendor / "scripts" / "mon_sleep.script", "-- mon_sleep\n")
    write(vendor / "scripts" / "guaranteed_loot.script", "-- guaranteed_loot\n")
    write(
        vendor / "configs" / "scripts" / "stancia_1" / "aes_crow_spawner.ltx",
        "[aes_crow_spawner]\n",
    )
    write(
        root / "reference" / "addons" / "mags_redux" / "scripts" / "sequential_load_magazine.script",
        SEQLOAD_SOURCE,
    )
    overlay = root / "addon" / "anthology_busyhands_stability_fix"
    scripts = overlay / "gamedata" / "scripts"
    write(scripts / pack_bhs.MAIN_OVERLAY)
    write(overlay / "CHANGELOG.md", "## [0.9.9]\n")
    write(overlay / "meta.ini", "vendor_source=BusyHands_vendor\nversion=0.0.0\n")
    (root / "build").mkdir(exist_ok=True)


class BuildPruneTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.build = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _touch(self, name: str, mtime: int) -> Path:
        path = self.build / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if name.endswith(".zip") or "/" not in name and not name.endswith(".zip"):
            if not name.endswith(".zip") and not path.exists():
                path.mkdir(exist_ok=True)
                (path / "BUILD_INFO.txt").write_text("x\n", encoding="utf-8")
            elif name.endswith(".zip"):
                path.write_text("zip\n", encoding="utf-8")
        os.utime(path, (mtime, mtime))
        return path

    def test_classify_bhs_patterns(self) -> None:
        self.assertEqual(
            build_prune.classify_build_name("Anthology_BusyHands_Stability_Fix_v0_6_7"),
            f"mod:{build_prune.BHS_MOD_ID}",
        )
        self.assertEqual(
            build_prune.classify_build_name("Anthology_BusyHands_Stability_Fix_v0_6_7.zip"),
            f"mod:{build_prune.BHS_MOD_ID}",
        )
        self.assertEqual(
            build_prune.classify_build_name("anthology_busyhands_stability_fix-0.6.4.zip"),
            f"mod:{build_prune.BHS_MOD_ID}",
        )

    def test_cleanup_before_build_removes_all_group_artifacts(self) -> None:
        old_dir = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2", 10)
        old_zip = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_3.zip", 20)
        other_zip = self._touch("anthology_busyhands_stability_fix-0.6.4.zip", 30)
        keep = self._touch("keep_me", 40)

        deleted = build_prune.cleanup_before_build(
            self.build,
            f"mod:{build_prune.BHS_MOD_ID}",
            keep_old=False,
        )

        self.assertEqual(
            {p.name for p in deleted},
            {
                "Anthology_BusyHands_Stability_Fix_v0_6_2",
                "Anthology_BusyHands_Stability_Fix_v0_6_3.zip",
                "anthology_busyhands_stability_fix-0.6.4.zip",
            },
        )
        self.assertFalse(old_dir.exists())
        self.assertFalse(old_zip.exists())
        self.assertFalse(other_zip.exists())
        self.assertTrue(keep.exists())

    def test_cleanup_before_build_keep_old(self) -> None:
        old_zip = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2.zip", 10)
        deleted = build_prune.cleanup_before_build(
            self.build,
            f"mod:{build_prune.BHS_MOD_ID}",
            keep_old=True,
        )
        self.assertEqual(deleted, [])
        self.assertTrue(old_zip.exists())

    def test_pack_bhs_cleans_old_versions(self) -> None:
        repo = self.build / "repo"
        stage_minimal_bhs_repo(repo)

        stale = repo / "build" / "Anthology_BusyHands_Stability_Fix_v0_6_2.zip"
        stale.write_text("old\n", encoding="utf-8")
        stale2 = repo / "build" / "anthology_busyhands_stability_fix-0.6.1.zip"
        stale2.write_text("old\n", encoding="utf-8")

        with contextlib.redirect_stdout(io.StringIO()):
            archive = pack_bhs.pack(repo, keep_old=False)

        self.assertTrue(archive.is_file())
        self.assertEqual(archive.name, "Anthology_BusyHands_Stability_Fix_v0_9_9.zip")
        self.assertFalse(stale.exists())
        self.assertFalse(stale2.exists())


if __name__ == "__main__":
    unittest.main()
