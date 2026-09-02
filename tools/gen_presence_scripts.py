#!/usr/bin/env python3
"""Write *_presence.script stubs for DLTX/data-only addon mods."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, detect_version

PRESENCE_MODS = (
    "fix_dome_quest",
    "fix_fdda_mcm_paths",
    "fix_fetch_headlamp",
    "fix_flst_joker_door",
    "fix_g2x_torch_meshes",
    "fix_grifon_visibility",
    "fix_hip_quest_text",
    "fix_hoc_monolith_icon",
    "fix_indeikam_breeding",
    "fix_item_combination_magnifiers",
    "fix_nimble_order_desc",
    "fix_okrest_texnik_dialog",
    "fix_sort_tabs",
    "fix_st2_footstep",
    "fix_trade_craft_stock",
    "fix_x15_freeplay_gate",
    "fix_zat_b12_box",
)

TEMPLATE = """-- xraylog presence (dltx/data-only).

local LOG_TAG = "[{mod_id}]"
local VERSION = "{version}"

printf("%s loaded v%s", LOG_TAG, VERSION)
"""


def main() -> int:
    for mod_id in PRESENCE_MODS:
        mod_dir = REPO_ROOT / "addon" / mod_id
        if not mod_dir.is_dir():
            print(f"skip missing {mod_id}", file=sys.stderr)
            continue
        scripts_dir = mod_dir / "gamedata" / "scripts"
        scripts_dir.mkdir(parents=True, exist_ok=True)
        path = scripts_dir / f"{mod_id}_presence.script"
        path.write_text(
            TEMPLATE.format(mod_id=mod_id, version=detect_version(mod_dir)),
            encoding="ascii",
            newline="\n",
        )
        print(path.relative_to(REPO_ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
