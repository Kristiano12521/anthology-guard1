#!/usr/bin/env python3
"""Pack Anthology Busy Hands Stability Fix from reference + addon overlays.

    python tools/pack_bhs.py
"""

from __future__ import annotations

import shutil
import zipfile
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VERSION = "0.6.4"
OUT_NAME = "Anthology_BusyHands_Stability_Fix_v0_6_4"

# Overlay files cannot use zzz prefixes (lint). Zip keeps vendor load order.
OVERLAY_MAP = {
    "anthology_bhs_fdda_patch.script": "zzzzzz_anthology_bhs_fdda_patch.script",
    "anthology_busyhands_stability_fix.script": "zzzzzz_anthology_busyhands_stability_fix.script",
}


def bhs_source(repo: Path) -> Path:
    root = repo / "reference" / "addons"
    for path in root.iterdir():
        if path.is_dir() and "BusyHands" in path.name:
            return path
    raise SystemExit("reference/addons/*BusyHands* not found")


def mag_seqload_source(repo: Path) -> Path:
    hits = list((repo / "reference").rglob("sequential_load_magazine.script"))
    if len(hits) != 1:
        raise SystemExit(f"expected 1 sequential_load_magazine.script, got {len(hits)}")
    return hits[0]


def patch_seqload(text: str) -> str:
    """One gradual mag-load job at a time; pcall dead ammo-box userdata.

    Locals take_one_round / in_progress cannot be monkey-patched (same
    reason as mon_sleep). Fail loudly if MAG Redux rewrote the sites.
    """
    text = text.replace("\r\n", "\n")

    bhs_header = """----------------------------------------------------------------
-- Anthology Busy Hands Stability Fix v0.6.3 - DOCUMENTED EXCEPTION
-- Full-file overlay of sequential_load_magazine.script (R.A.K. Mags Redux).
-- Locals take_one_round / in_progress / perform_gradual_load cannot be
-- monkey-patched from outside (same reason as mon_sleep.script).
--
-- Two concurrent gradual loads share ammo-box userdata. When one job
-- alife_release_id the last round, the other job calls ammo_get_count
-- on destroyed userdata -> [BusyHandsDebug] take_one_round:227.
-- Fix: one gradual job at a time; pcall around ammo_get_count.
----------------------------------------------------------------
"""
    old_start = """----------------------------------------------------------------
-- Sequential (alternating) magazine loading.
"""
    if old_start not in text:
        raise SystemExit("seqload: header block not found")
    text = text.replace(old_start, bhs_header + "-- Sequential (alternating) magazine loading.\n", 1)

    old_marker = "local presets = {}\n"
    new_marker = 'ANTHOLOGY_BUSYHANDS_SEQLOAD_FIX_VERSION = "0.6.3"\n\nlocal presets = {}\n'
    if old_marker not in text:
        raise SystemExit("seqload: presets block not found")
    text = text.replace(old_marker, new_marker, 1)

    old_take = """local function take_one_round(pool)
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
end"""

    new_take = """local function take_one_round(pool)
	while #pool.boxes > 0 do
		local box = pool.boxes[1]
		local ok_count, count = pcall(function() return box:ammo_get_count() end)
		if not ok_count or type(count) ~= "number" then
			table.remove(pool.boxes, 1)
		elseif count > 1 then
			box:ammo_set_count(count - 1)
			pool.total = pool.total - 1
			return true
		elseif count == 1 then
			local ok_id, box_id = pcall(function() return box:id() end)
			if ok_id and box_id then
				alife_release_id(box_id)
			end
			table.remove(pool.boxes, 1)
			pool.total = pool.total - 1
			return true
		else
			table.remove(pool.boxes, 1)
		end
	end
	return false
end"""
    if old_take not in text:
        raise SystemExit("seqload: take_one_round block not found")
    text = text.replace(old_take, new_take, 1)

    old_grad = """	-- Don't double-schedule.
	if in_progress[mag_id] then return end
"""
    new_grad = """	-- Don't double-schedule this mag, and don't run two mags at once:
	-- two jobs snapshot the same ammo boxes; take_one_round then hits
	-- a released userdata (Busy Hands at line 227).
	if in_progress[mag_id] then return end
	if next(in_progress) then return end
"""
    if old_grad not in text:
        raise SystemExit("seqload: perform_gradual_load guard not found")
    text = text.replace(old_grad, new_grad, 1)

    old_menu = """	-- Don't show a second time if we're already loading this mag.
	if in_progress[obj:id()] then return false end
	return true
"""
    new_menu = """	-- Don't show if this mag is loading, or any other mag (one job only).
	if in_progress[obj:id()] then return false end
	if next(in_progress) then return false end
	return true
"""
    if old_menu not in text:
        raise SystemExit("seqload: menu_check guard not found")
    text = text.replace(old_menu, new_menu, 1)

    old_entry = """	-- If a gradual load is already running on this mag, ignore further clicks.
	if in_progress[mag_id] then return end
"""
    new_entry = """	-- If a gradual load is already running (this mag or another), ignore.
	-- Context menu can already be open on mag 2 when mag 1 starts loading.
	if in_progress[mag_id] then return end
	if next(in_progress) then return end
"""
    if old_entry not in text:
        raise SystemExit("seqload: perform_sequential_load guard not found")
    text = text.replace(old_entry, new_entry, 1)

    if text.count("if next(in_progress) then return") != 3:
        raise SystemExit("seqload: expected three next(in_progress) guards")
    if "ok_count" not in text:
        raise SystemExit("seqload: pcall ammo_get_count missing")
    return text.replace("\n", "\r\n")


def pack(repo: Path | None = None) -> Path:
    repo = repo or REPO
    overlay = repo / "addon" / "anthology_busyhands_stability_fix"
    src = bhs_source(repo)
    scripts = overlay / "gamedata" / "scripts"
    for name in OVERLAY_MAP:
        if not (scripts / name).is_file():
            raise SystemExit(f"missing overlay {name}")

    seq_src = mag_seqload_source(repo)

    out_dir = repo / "build" / OUT_NAME
    if out_dir.exists():
        shutil.rmtree(out_dir)
    gamedata = out_dir / "gamedata"
    gamedata.mkdir(parents=True)

    copied = 0
    for path in src.rglob("*"):
        if not path.is_file():
            continue
        dst = gamedata / path.relative_to(src)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dst)
        copied += 1

    for overlay_name, zip_name in OVERLAY_MAP.items():
        shutil.copy2(scripts / overlay_name, gamedata / "scripts" / zip_name)

    seq_text = seq_src.read_bytes().decode("cp1251")
    seq_out = gamedata / "scripts" / "sequential_load_magazine.script"
    seq_out.write_bytes(patch_seqload(seq_text).encode("cp1251"))

    loot = gamedata / "scripts" / "fix_bhs_fdda_loot.script"
    if loot.exists():
        loot.unlink()

    shutil.copy2(overlay / "CHANGELOG.md", out_dir / "CHANGELOG.md")
    shutil.copy2(overlay / "meta.ini", out_dir / "meta.ini")
    (out_dir / "BUILD_INFO.txt").write_text(
        "\n".join(
            [
                "mod_id: Anthology_BusyHands_Stability_Fix",
                f"version: {VERSION}",
                f"built: {datetime.now().isoformat(timespec='seconds')}",
                f"source: {src.name} + addon/anthology_busyhands_stability_fix",
                f"seqload: {seq_src.parent.parent.name}",
                f"bhs_files: {copied}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    archive = repo / "build" / f"{OUT_NAME}.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(out_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(out_dir).as_posix())

    names = zipfile.ZipFile(archive).namelist()
    if "gamedata/scripts/fix_bhs_fdda_loot.script" in names:
        raise SystemExit("loot sidecar leaked into zip")
    if "gamedata/scripts/anthology_bhs_fdda_patch.script" in names:
        raise SystemExit("overlay name leaked into zip")
    if "gamedata/scripts/sequential_load_magazine.script" not in names:
        raise SystemExit("seqload overlay missing from zip")

    print(f"source: {src}")
    print(f"seqload: {seq_src}")
    print(f"dir: {out_dir}")
    print(f"zip: {archive} ({archive.stat().st_size} bytes)")
    for name in names:
        print(f"  {name}")
    return archive


def main() -> None:
    pack()


if __name__ == "__main__":
    main()
