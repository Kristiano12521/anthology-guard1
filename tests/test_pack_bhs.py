import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import pack_bhs  # noqa: E402

# Минимальный исходник, в котором есть все якоря patch_seqload.
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


# Имена как в addon/anthology_busyhands_stability_fix/gamedata/scripts/.
OVERLAY_SCRIPTS = [
    "anthology_busyhands_stability_fix.script",
    "zzzz_zzz_anthology_bhs_repair_capture_vendor_base.script",
    "zzzzzz_anthology_bhs_crow_spawner_patch.script",
    "zzzzzz_anthology_bhs_dotmarks_patch.script",
    "zzzzzz_anthology_bhs_fdda_patch.script",
    "zzzzzz_anthology_bhs_find_close_cover_patch.script",
    "zzzzzz_anthology_bhs_item_repair_patch.script",
    "zzzzzz_anthology_bhs_repair_recursion_fix.script",
    "zzzzzz_anthology_bhs_sortingplus_patch.script",
    "zzzzzz_anthology_bhs_trader_autoinject_patch.script",
    "zzzzzz_anthology_bhs_trader_furniture_distance_patch.script",
]


def overlay_zip_name(name: str) -> str:
    if name == pack_bhs.MAIN_OVERLAY:
        return pack_bhs.MAIN_ZIP
    return name


class PackBhsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        vendor = self.repo / "reference" / "addons" / "BusyHands_vendor"
        write(vendor / "scripts" / "vendor_bhs.script")
        write(vendor / "scripts" / "fix_bhs_fdda_loot.script", "-- loot sidecar\n")
        write(vendor / "scripts" / "sequential_load_magazine.script", "-- already in BHS pack\n")
        write(
            self.repo / "reference" / "addons" / "mags_redux" / "scripts" / "sequential_load_magazine.script",
            SEQLOAD_SOURCE,
        )
        overlay = self.repo / "addon" / "anthology_busyhands_stability_fix"
        scripts = overlay / "gamedata" / "scripts"
        for name in OVERLAY_SCRIPTS:
            write(scripts / name)
        write(overlay / "CHANGELOG.md", "## [0.9.9]\n")
        write(overlay / "meta.ini", "version=0.0.0\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_zip_name_follows_overlay_changelog(self):
        overlay = self.repo / "addon" / "anthology_busyhands_stability_fix"
        version = pack_bhs.detect_version(overlay)
        self.assertEqual(version, "0.9.9")
        self.assertNotEqual(version, pack_bhs.VENDOR_SOURCE_VERSION)
        expected = f"{pack_bhs.packed_name(version)}.zip"
        archive = pack_bhs.pack(self.repo)
        self.assertEqual(archive.name, expected)
        info = (self.repo / "build" / pack_bhs.packed_name(version) / "BUILD_INFO.txt").read_text(
            encoding="utf-8"
        )
        self.assertIn("version: 0.9.9", info)

    def test_mo2_layout_and_contents(self):
        archive = pack_bhs.pack(self.repo)
        with zipfile.ZipFile(archive) as zf:
            names = zf.namelist()
        self.assertIn("gamedata/scripts/vendor_bhs.script", names)
        self.assertIn("gamedata/scripts/sequential_load_magazine.script", names)
        for name in OVERLAY_SCRIPTS:
            self.assertIn(f"gamedata/scripts/{overlay_zip_name(name)}", names)
        self.assertIn("CHANGELOG.md", names)
        self.assertIn("meta.ini", names)
        self.assertTrue(all(not name.startswith(pack_bhs.OUT_STEM) for name in names))
        self.assertNotIn("gamedata/scripts/fix_bhs_fdda_loot.script", names)
        self.assertNotIn("gamedata/scripts/anthology_bhs_fdda_patch.script", names)
        self.assertNotIn(f"gamedata/scripts/{pack_bhs.MAIN_OVERLAY}", names)

    def test_vendor_folder_uses_source_version_not_overlay(self):
        preferred = (
            self.repo
            / "reference"
            / "addons"
            / pack_bhs.packed_name(pack_bhs.VENDOR_SOURCE_VERSION)
        )
        preferred.mkdir(parents=True)
        write(preferred / "scripts" / "from_vendor_version.script")
        archive = pack_bhs.pack(self.repo)
        with zipfile.ZipFile(archive) as zf:
            names = zf.namelist()
        self.assertIn("gamedata/scripts/from_vendor_version.script", names)
        self.assertNotIn("gamedata/scripts/vendor_bhs.script", names)
        self.assertEqual(archive.name, "Anthology_BusyHands_Stability_Fix_v0_9_9.zip")

    def test_rejects_source_with_build_info(self):
        preferred = (
            self.repo
            / "reference"
            / "addons"
            / pack_bhs.packed_name(pack_bhs.VENDOR_SOURCE_VERSION)
        )
        preferred.mkdir(parents=True)
        write(preferred / "scripts" / "vendor_bhs.script")
        write(
            preferred / "BUILD_INFO.txt",
            "mod_id: Anthology_BusyHands_Stability_Fix\nversion: 0.6.4\n",
        )
        with self.assertRaises(SystemExit) as ctx:
            pack_bhs.pack(self.repo)
        self.assertIn("BUILD_INFO.txt", str(ctx.exception))
        self.assertIn("own pack", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
