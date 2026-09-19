# Travel Invalid Alife ID Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 после Anthology base.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.1] - 2026-09-16

**Изменено**

- `gamedata/scripts/fix_travel_invalid_id.script` — в `printf` `batch_total` и `late-wrapped` формат `%d` заменён на `%s` + `tostring`.

**Причина**

`printf` этой сборки подставляет `%s`, не `%d`. При skip / late-wrap лог мог обрезаться или врать, как у sound 1.0.1.

**Не затронуто**

- Логика валидации `id` (nil / `<= 0` / `>= 65535`)
- Hook `RegisterScriptCallback` и late-wrap через `axr_main` `intercepts`

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_travel_invalid_id`
- в игре: не подтверждено. Ожидание: skip пишет `batch_total=<число>` без сломанного формата.

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
