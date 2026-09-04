# Changelog: weapon_loc_kit

Комплект: `weapon_loc_rework` + `fix_localization_reload` в одном MO2-моде.

## 1.0.0 — 2026-09-04

- `configs/text/{eng,rus}/zzz_st_weapon_loc_*.xml` — переводы оружия без оружейных LTX; `zzz_` перекрывает Eng Update и не конфликтует путём с RAK SPL / FIX.
- `zz_fix_localization_reload.script` — смена языка в меню шлёт `on_localization_change`; сброс кэшей `ui_item` / `ui_inventory.st_perc`; `item_name`/`item_description` без stale `last_*_id`.

Не затронуто: балансы оружия, сейвы. Исходный архив с полными LTX ставить нельзя рядом.
