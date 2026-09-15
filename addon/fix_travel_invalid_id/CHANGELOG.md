# Travel Invalid Alife ID Guard

## [1.0.0] - 2026-09-15

**Изменено**

- `gamedata/scripts/fix_travel_invalid_id.script` - wrap `map_spot_menu_add_property` / `map_spot_menu_property_clicked` у `game_backpack_travel` и `game_fast_travel`: при `id == nil` / `id <= 0` / `id >= 65535` ранний выход без `alife_object`.

**Причина**

Клики по PDA spot для `task_placeable_waypoint` / пустой карты передают sentinel `65535`. Travel-скрипты зовут `alife_object(id)` без проверки -> `!ALIFE OBJECT ID IS 65535!` и нефатальный traceback (baseline mg9000).

**Как исправлено**

Monkey-patch: hook `RegisterScriptCallback` до регистрации travel (имя `fix_*` грузится раньше `game_*`) + late-wrap через `axr_main` `intercepts` на `actor_on_first_update`.

**Не затронуто**

- `tasks_placeable_waypoints` / PAW логика пинов
- `pda.script`, меню spot кроме travel-опций
- `alife_object` глобально (диагностика для других вызывающих остаётся)
- sound / FDDA

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим, состояние не пишется
- В MO2 после Anthology base

**Проверено**

- lint: `python tools/lint_addon.py fix_travel_invalid_id`
- в игре: не подтверждено. Ожидание: ПКМ по placeable waypoint / пустой карте без `!ALIFE OBJECT ID IS 65535!` от travel; в логе при skip - `skip invalid id=65535`.
