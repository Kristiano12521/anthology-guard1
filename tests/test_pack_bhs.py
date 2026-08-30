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


class PackBhsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        vendor = self.repo / "reference" / "addons" / "BusyHands_vendor"
        write(vendor / "scripts" / "vendor_bhs.script")
        write(vendor / "scripts" / "fix_bhs_fdda_loot.script", "-- loot sidecar\n")
        write(
            self.repo / "reference" / "addons" / "mags_redux" / "scripts" / "sequential_load_magazine.script",
            SEQLOAD_SOURCE,
        )
        overlay = self.repo / "addon" / "anthology_busyhands_stability_fix"
        write(overlay / "gamedata" / "scripts" / "anthology_bhs_fdda_patch.script")
        write(overlay / "gamedata" / "scripts" / "anthology_busyhands_stability_fix.script")
        write(overlay / "CHANGELOG.md", "## [0.6.4]\n")
        write(overlay / "meta.ini", "version=0.6.4\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_zip_name_includes_version(self):
        expected = f"Anthology_BusyHands_Stability_Fix_v{pack_bhs.VERSION.replace('.', '_')}.zip"
        self.assertEqual(f"{pack_bhs.OUT_NAME}.zip", expected)
        archive = pack_bhs.pack(self.repo)
        self.assertEqual(archive.name, expected)

    def test_mo2_layout_and_contents(self):
        archive = pack_bhs.pack(self.repo)
        with zipfile.ZipFile(archive) as zf:
            names = zf.namelist()
        self.assertIn("gamedata/scripts/vendor_bhs.script", names)
        self.assertIn("gamedata/scripts/sequential_load_magazine.script", names)
        self.assertIn("gamedata/scripts/zzzzzz_anthology_bhs_fdda_patch.script", names)
        self.assertIn("gamedata/scripts/zzzzzz_anthology_busyhands_stability_fix.script", names)
        self.assertIn("CHANGELOG.md", names)
        self.assertIn("meta.ini", names)
        self.assertTrue(all(not name.startswith(pack_bhs.OUT_NAME) for name in names))
        self.assertNotIn("gamedata/scripts/fix_bhs_fdda_loot.script", names)
        self.assertNotIn("gamedata/scripts/anthology_bhs_fdda_patch.script", names)


if __name__ == "__main__":
    unittest.main()
