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

import _pack_kristiano_aio as packer  # noqa: E402
import pack_bhs  # noqa: E402

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


def zip_names(archive: Path) -> list[str]:
    with zipfile.ZipFile(archive) as zf:
        return zf.namelist()


class PackKristianoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.addon_root = root / "addon"
        self.out_dir = root / "build"
        self.addon_root.mkdir()
        self.out_dir.mkdir()

        write(
            self.addon_root / "keep_me" / "gamedata" / "scripts" / "keep_me.script",
            "-- aio keep\n",
        )
        write(self.addon_root / "keep_me" / "CHANGELOG.md", "## [2.1.0]\n")
        write(
            self.addon_root / "also_keep" / "gamedata" / "configs" / "items" / "mod_also.ltx",
            "[also]\n",
        )

        for mod_id, marker in (
            ("context_menu_overhaul_anthology", "cmo_only"),
            ("quickqk_task_complete", "quickqk_only"),
            ("fix_st2_footstep", "st2_only"),
        ):
            write(
                self.addon_root / mod_id / "gamedata" / "scripts" / f"{marker}.script",
                f"-- {marker}\n",
            )
            write(self.addon_root / mod_id / "CHANGELOG.md", "## [3.2.1]\n")
            write(self.addon_root / mod_id / "meta.ini", "version=0.0.0\ninstallationFile=old.zip\n")

        write(
            self.addon_root / "fix_bhs_fdda_loot" / "gamedata" / "scripts" / "skip_loot.script",
            "-- skipped\n",
        )
        write(
            self.addon_root
            / "anthology_busyhands_stability_fix"
            / "gamedata"
            / "scripts"
            / pack_bhs.MAIN_OVERLAY,
            "-- bhs overlay\n",
        )
        write(self.addon_root / "anthology_busyhands_stability_fix" / "CHANGELOG.md", "## [0.6.7]\n")
        write(
            self.addon_root / "anthology_busyhands_stability_fix" / "meta.ini",
            "vendor_source=BusyHands_vendor\nversion=0.0.0\n",
        )

        vendor = self.addon_root.parent / "reference" / "addons" / "BusyHands_vendor"
        write(vendor / "scripts" / "vendor_bhs.script")
        write(vendor / "scripts" / "fix_bhs_fdda_loot.script", "-- loot sidecar\n")
        write(vendor / "scripts" / "mon_sleep.script", "-- mon_sleep\n")
        write(vendor / "scripts" / "guaranteed_loot.script", "-- guaranteed_loot\n")
        write(
            vendor / "configs" / "scripts" / "stancia_1" / "aes_crow_spawner.ltx",
            "[aes_crow_spawner]\n",
        )
        write(
            self.addon_root.parent
            / "reference"
            / "addons"
            / "mags_redux"
            / "scripts"
            / "sequential_load_magazine.script",
            SEQLOAD_SOURCE,
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def pack(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            code = packer.main(
                [
                    "--addon-root",
                    str(self.addon_root),
                    "--out",
                    str(self.out_dir),
                ]
            )
        self.assertEqual(code, 0)

    def _repo_root(self) -> Path:
        return self.addon_root.parent

    def test_aio_excludes_skip_and_separate(self):
        self.pack()
        aio = self.out_dir / f"{packer.AIO_NAME}.zip"
        self.assertTrue(aio.is_file())
        names = zip_names(aio)
        self.assertIn("gamedata/scripts/keep_me.script", names)
        self.assertIn("gamedata/configs/items/mod_also.ltx", names)
        self.assertTrue(any(name.startswith("gamedata/") for name in names))
        self.assertFalse(any(name.startswith(packer.AIO_NAME) for name in names))
        self.assertNotIn("gamedata/scripts/cmo_only.script", names)
        self.assertNotIn("gamedata/scripts/quickqk_only.script", names)
        self.assertNotIn("gamedata/scripts/st2_only.script", names)
        self.assertNotIn("gamedata/scripts/skip_loot.script", names)
        self.assertNotIn("gamedata/scripts/skip_bhs.script", names)
        self.assertIn(f"gamedata/scripts/{pack_bhs.MAIN_ZIP}", names)
        self.assertIn("gamedata/scripts/sequential_load_magazine.script", names)
        with zipfile.ZipFile(aio) as zf:
            contents = zf.read("CONTENTS.txt").decode("utf-8")
        self.assertIn("anthology_busyhands_stability_fix", contents)
        self.assertIn("pack_bhs", contents)
        self.assertNotIn("Not included (separate archive, tools/pack_bhs.py)", contents)

    def test_separate_zips_layout_and_version(self):
        self.pack()
        for mod_id, mo2_name in packer.SEPARATE.items():
            archive = self.out_dir / f"{mo2_name}.zip"
            self.assertTrue(archive.is_file(), msg=archive.name)
            names = zip_names(archive)
            self.assertTrue(any(n.startswith("gamedata/") for n in names), msg=names)
            self.assertFalse(any(n.startswith(mo2_name) for n in names), msg=names)
            self.assertIn("meta.ini", names)
            self.assertIn("BUILD_INFO.txt", names)
            with zipfile.ZipFile(archive) as zf:
                meta = zf.read("meta.ini").decode("utf-8")
            self.assertIn("version=3.2.1", meta)

        addons = {p.name for p in packer.aio_addons(self.addon_root)}
        self.assertEqual(addons, {"also_keep", "keep_me"})

    def test_version_from_meta_ini_without_changelog(self):
        write(self.addon_root / "keep_me" / "meta.ini", "version=7.7.7\n")
        (self.addon_root / "keep_me" / "CHANGELOG.md").unlink()
        self.assertEqual(packer.detect_version(self.addon_root / "keep_me"), "7.7.7")
        self.pack()
        aio = self.out_dir / f"{packer.AIO_NAME}.zip"
        with zipfile.ZipFile(aio) as zf:
            contents = zf.read("CONTENTS.txt").decode("utf-8")
        self.assertIn("keep_me", contents)
        self.assertIn("v7.7.7", contents)


if __name__ == "__main__":
    unittest.main()
