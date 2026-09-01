# fix_item_combination_magnifiers

## [1.0.0] — 2026-09-01

**Исправлено**

- 4× `!ERROR item_combination | wrong section names` при старте: `mod_craft_magnifiers.ltx` (R.A.K 3DSS) ссылается на `magnifier`, `e0t2`, `uh2`, `e0t2_magd`, `uh1_magd` как на item-секции; в сборке это имена scope-слотов на оружии, не предметы в `ini_sys`.

**Как**

- DLTX `mod_craft_fix_item_combination_magnifiers.ltx`: `!magnifier:e0t2` и три зеркальные строки.

**Проверено**

- lint: см. прогон после правки
- В игре: не прогонялось
