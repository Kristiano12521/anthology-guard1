# PH Door Stale Registry and RX Offline Planner Guard

Anomaly 1.5.3 / Anthology 2.1. Monkey-patch + callback. Does not replace `ph_door.script` or any RX script.

## Install

1. Place below Anthology in MO2.
2. Turn **off** `[FIX] MTR Attribute Hotfix (slim)` — it rewrites the same functions wholesale.
3. Restart the game. New game is not required.

## Not in this addon

Missing `mtr_e80_bomba_obj_*` sections come from Campfires shipping a full outdated `dynamic_objects.ltx`. Use `[FIX] Campfires Anthology Compat` instead of the original Campfires pack. Do not restore a full copy of `dynamic_objects.ltx`.
