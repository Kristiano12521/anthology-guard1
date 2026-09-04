# fix_item_combination_magnifiers

## [1.1.0] — 2026-09-04

**Изменено**

- `gamedata/scripts/fix_item_combination_magnifiers_presence.script` — мод отключён (`WITHDRAWN`): только presence + причина, патч не ставится.
- `gamedata/configs/items/settings/mod_craft_fix_item_combination_magnifiers.ltx` — операторы `!` закомментированы (неактивны).

**Причина**

DLTX-оператор `!` не снимает ключи с двоеточием в имени. VFS-перекрытие чужого `mod_craft_magnifiers.ltx` не делаем: при обновлении R.A.K наша пустышка скрыла бы новую версию. Исправление — только upstream.

**Замер** (04.09.2026, Anthology 2.1 / Modded Exes MT, `-dbg`, мод loaded v1.0.0):

```
run_string printf("ic_keys=%s", tostring(itms_manager.ini_craft:line_count("item_combination")))
→ ic_keys=10

run_string printf("mag_e0t2=%s", tostring(itms_manager.ini_craft:line_exist("item_combination","magnifier:e0t2")))
→ mag_e0t2=true
```

`!ERROR item_combination | wrong section names`: 4 строки на 4 загрузки (как без мода). Ключ `magnifier:e0t2` остался после `![item_combination]` + `!magnifier:e0t2`.

**Не затронуто**

- файл R.A.K `mod_craft_magnifiers.ltx` (нет VFS-override)
- логика `itms_manager` / `item_combine`
- сейвы

**Проверено**

- lint: после правки
- В игре: замер выше (v1.0.0); v1.1.0 — WITHDRAWN в логе

## [1.0.0] — 2026-09-01

**Исправлено**

- 4× `!ERROR item_combination | wrong section names` при старте: `mod_craft_magnifiers.ltx` (R.A.K 3DSS) ссылается на `magnifier`, `e0t2`, `uh2`, `e0t2_magd`, `uh1_magd` как на item-секции; в сборке это имена scope-слотов на оружии, не предметы в `ini_sys`.

**Как**

- DLTX `mod_craft_fix_item_combination_magnifiers.ltx`: `!magnifier:e0t2` и три зеркальные строки.

**Проверено**

- lint: см. прогон после правки
- В игре: не прогонялось (позже опровергнуто замером 04.09.2026 — см. 1.1.0)
