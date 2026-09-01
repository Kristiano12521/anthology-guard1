# Anthology Busy Hands Stability Fix

## [0.6.8] — 2026-09-01

**Изменено**

- `zzzzzz_anthology_bhs_trader_autoinject_patch.script` — `timed_update` резолвится через bare `_G` и `trader_autoinject.*` до обёртки `trade_manager.update`; `CreateTimeEvent` вызывается только с локальной `patched_timed_update`, иначе — лог и пропуск.

**Причина**

Голое `timed_update` в env патча было `nil` (функция локальна в `trader_autoinject.script` Campfires). Патч передавал `nil` в `CreateTimeEvent` до проверки `type(timed_update) == "function"` — 71× `attempt to push nil instead of function` в логе.

**Как исправлено**

Восстановлена логика v0.6.5: резолв и патч `timed_update` на таблице модуля, затем обёртка `trade_manager.update` с `patched_timed_update` в замыкании. Без резолва — `CreateTimeEvent` не вызывается.

**Не затронуто**

- Вендорский `trader_autoinject.script`, `verified_*`, остальные патчи BHS.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции

**Проверено**

- `lint_addon.py` и `--cross`: 0 ошибок
- В игре: не прогонялось (ожидается: 0 CTE nil, `trader_autoinject guards installed` ненулевой)

## [0.6.7] — 2026-08-31

**Изменено**

- `zzzzzz_anthology_bhs_find_close_cover_patch.script` — одна строка `patched via <путь>` вместо пары «global was not found - guard NOT installed» + «module-table path». Оба пути по-прежнему патчатся, если найдены.

**Причина**

Голый `find_close_cover` в `_G` пустой, цель живёт на `utils_obj`. Первая строка всегда промахивалась и выглядела как отказ, хотя гард вставал вторым путём.

**Как исправлено**

Тот же формат, что у crow / UIRepair / UIInventory после 0.6.5. Менялся только вывод в лог, не поведение.

**Не затронуто**

- Логика `pcall` вокруг `best_cover`, остальные патчи, сохраняемое состояние.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить предыдущий overlay BHS 0.6.6.

**Проверено**

- lint overlay и `--cross`: см. прогон после правки
- В игре: сессия 31.08.2026, 0.6.6 — девять патчей, все guards ненулевые, capture и repair chain встали, 0 traceback. 0.6.7 меняет только текст лога find_close_cover.

## [0.6.6] — 2026-08-31

**Изменено**

- `zzzz_zzz_anthology_bhs_repair_capture_vendor_base.script` — маркер `ANTHOLOGY_BHS_REPAIR_VENDOR_BASE_ON_ITEM_SELECT` пишется и в env файла, и в `_G`.
- `zzzzzz_anthology_bhs_repair_recursion_fix.script` — читает маркер как сводка гардов: `_G`, затем таблица модуля capture.

**Причина**

Захват писал голым присвоением в env `zzzz_zzz_*`. Recursion-fix читал голое имя и через `__index` попадал только в `_G`. В логе подряд: `Captured OnItemSelect via ...` и `vendor base OnItemSelect was not captured`. Та же дыра env vs `_G`, что у маркеров версии в 0.6.2.

**Как исправлено**

Тот же `read_marker`, что в главном скрипте. Имя файла `zzzz_zzz_` не трогали.

**Не затронуто**

- Реконструкция OnItemSelect, слот load-order, остальные гарды.
- Сохраняемое состояние.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить предыдущий overlay BHS 0.6.5.

**Проверено**

- lint overlay и `--cross`: см. прогон после правки
- В игре: не прогонялось. Не должно быть пары `Captured` + `was not captured`; должна быть `repair chain UIRepair.OnItemSelect set via`.

## [0.6.5] — 2026-08-31

**Изменено**

- Четыре патча ищут цель другим путём. Поведение гардов то же.
- `zzzzzz_anthology_bhs_crow_spawner_patch.script` — `sr_crow_spawner.crowkiller` это userdata (`class "crowkiller"`), не table. Условие как у рабочего `zzzz_anthology_crow_spawner_fix`: `_G.crowkiller`, затем модуль; принимаются table и userdata.
- `zzzzzz_anthology_bhs_item_repair_patch.script` и `zzzzzz_anthology_bhs_sortingplus_patch.script` — `class "X" (CUIScriptWnd)` кладёт класс в `_G`, на таблице модуля его нет. Ищутся оба пути, как у `find_close_cover`: голый `UIRepair`/`UIInventory`, `_G.*`, `item_repair.UIRepair` / `ui_inventory.UIInventory`.
- `zzzz_zzz_anthology_bhs_repair_capture_vendor_base.script` — env `zzzz_arti_jamming_repairs` снаружи есть (`_G[filename]`), поле `RepairOnItemSelect` на нём nil. Имя файла не трогали. Если модуля/глобала нет, захватывается текущий `UIRepair.OnItemSelect`.
- `zzzzzz_anthology_bhs_repair_recursion_fix.script` — тот же dual-path к `UIRepair`, иначе цепочка не встанет после смены поиска.

**Причина**

`run_string` 31.08.2026, Anthology 2.1 / Modded Exes MT: `sr_crow_spawner.crowkiller` = userdata; `item_repair.UIRepair` / `ui_inventory.UIInventory` / `zzzz_arti_jamming_repairs.RepairOnItemSelect` = nil. Проверка `type(...) == "table"` и поиск только на модуле цель не находили.

**Как исправлено**

Разный резолв под каждый замер. Каждый патч пишет в лог, каким путём нашёл цель.

**Не затронуто**

- Логика гардов (pcall вокруг vertex, rebind ремкомплекта, LMode_Init, реконструкция OnItemSelect).
- Имена файлов и слот `zzzz_zzz_`.
- FDDA / mon_sleep / sequential_load / traders / DotMarks.
- Сохраняемое состояние.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить предыдущий overlay BHS 0.6.4.

**Проверено**

- lint overlay и `--cross`: см. прогон после правки
- В игре: не прогонялось. В логе у crow/UIRepair/UIInventory/capture должна быть строка `via ...`, не `was not found`.


## [0.6.4] — 2026-08-31

**Изменено**

- В overlay возвращены восемь патчей 0.6.4 и `zzzz_zzz_anthology_bhs_repair_capture_vendor_base.script`. Без них главный скрипт писал `marker was not found` и `guards installed: 0`.
- FDDA-патч снова `zzzzzz_anthology_bhs_fdda_patch.script`. С префиксом `install()` на загрузке файла выполняется после `liz_fdda_redone_body_search`, а не до. В логе сначала `patched (module-table`, потом `Anthology Busy Hands Stability Fix 0.6.4 loaded`; строки `were not found - guard NOT installed` перед `patched` быть не должно.
- У всех `zzzzzz_` / `zzzz_zzz_` скриптов в шапке `-- load-order: после <вендор>`.

**Причина**

`build_addon.py` пакует только `addon/`. Там лежали главный скрипт и FDDA; остальные восемь модулей, которые сводка ищет по имени `zzzzzz_anthology_bhs_*`, в overlay не входили.

**Как исправлено**

Файлы скопированы из эталона `Anthology_BusyHands_Stability_Fix_v0_6_4`. Префиксы как в оригинале: DotMarks / SortingPlus / item_repair / repair chain должны грузиться после вендорских `z_`/`zz_`/`zzz_`/`zzzzz_` скриптов. Capture встаёт между `zzzz_arti_jamming_repairs` и `zzzzz_arti_outfit_repair`.

**Не затронуто**

- Логика FDDA 0.6.4 и текст главного скрипта.
- `mon_sleep` / `guaranteed_loot` / `sequential_load_magazine` / `aes_crow_spawner.ltx`.
- Сохраняемое состояние.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить предыдущий overlay BHS 0.6.4.

**Проверено**

- lint overlay и `--cross`: см. прогон после правки
- В игре: не прогонялось. В логе не должно остаться `marker was not found`; `guards installed` у девяти патчей ненулевые.

## [0.6.4] — 2026-08-28

**Изменено**

- `zzzzzz_anthology_bhs_fdda_patch.script` — повторный `start_body_search` при теге `body_search` снова no-op (как вендор). Idle, если GUI уже показан, ставит `is_ui_enabled`.

**Причина**

Use по трупу дважды зовёт `start("loot")`: движок `CUIActorMenu_OnMode_DeadBodySearch` и `UIInventory:npc_on_use`. В 0.6.2 второй вход открывал лут через `LMode_Init` без флага idle. Esc прятал GUI, idle считал окно ещё не открытым и поднимал лут снова — в том числе после своего инвентаря.

**Как исправлено**

Повторный вход не открывает UI. Открывает только idle через `LMode_Init`. Если окно уже видно (свой инвентарь на задержке), idle помечает UI открытым и по Esc завершает поиск, а не открывает лут.

**Не затронуто**

- Вендорский `liz_fdda_redone_body_search.script`.
- sequential_load 0.6.3 и остальные гарды.
- Префиксы `zzzzzz_` (load order).
- Сохраняемое состояние.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить BHS 0.6.3. Отдельный `fix_bhs_fdda_loot` снять: его повторный open на теге снова даст второй инвентарь.

**Проверено**

- lint overlay: `python tools/lint_addon.py anthology_busyhands_stability_fix`
- В логе после старта: `Anthology Busy Hands Stability Fix 0.6.4 loaded`, `patched (module-table`, `FDDA body search guards installed: 1`.

## [0.6.3] — 2026-08-28

**Изменено**

- `sequential_load_magazine.script` — полная замена файла MAG Redux (как `mon_sleep`): один постепенный заряд за раз (`perform_gradual_load`, `perform_sequential_load`, `menu_check`); `pcall` вокруг `ammo_get_count` на мёртвом ammo-box.
- `zzzzzz_anthology_busyhands_stability_fix.script` — версия 0.6.3; сводка проверяет маркер `ANTHOLOGY_BUSYHANDS_SEQLOAD_FIX_VERSION`.

**Причина**

ПКМ «Зарядить последовательно» на двух магазинах сразу. Каждый job держит один и тот же ammo-box userdata. Когда первый `alife_release_id` последний патрон, второй зовёт `box:ammo_get_count()` → Busy Hands на `take_one_round:227`. `in_progress` ключился по id магазина, поэтому два магазина не блокировали друг друга. Локали не патчатся снаружи.

**Как исправлено**

`if next(in_progress) then return end` в `perform_gradual_load`, `perform_sequential_load` и `menu_check`. В `take_one_round` — `pcall` и выкидывание мёртвого бокса из пула. Файл кладётся в zip пакером из `reference/` MAG, правки применяются при сборке.

**Не затронуто**

- Instant load, пресеты, `magazine_binder` / `magazines` API.
- FDDA-лут 0.6.2 и остальные гарды.
- Префиксы `zzzzzz_` (load order).

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить BHS 0.6.2. BHS должен быть ниже MAG Redux (перекрывает `sequential_load_magazine.script`).

**Проверено**

- lint overlay: `python tools/lint_addon.py anthology_busyhands_stability_fix`
- Сборка: `python tools/pack_bhs.py` → zip содержит `gamedata/scripts/sequential_load_magazine.script`.
- В логе после старта: `Anthology Busy Hands Stability Fix 0.6.3 loaded`, `sequential_load_magazine guard mode: full-file override`.

## [0.6.2] — 2026-08-28

**Изменено**

- `zzzzzz_anthology_bhs_fdda_patch.script` — функции FDDA патчатся на таблице модуля `liz_fdda_redone_body_search`; окно лута открывается через ванильный `LMode_Init`, без вызова обёрнутого `ui_inventory.start`.
- `zzzzzz_anthology_busyhands_stability_fix.script` — версия 0.6.2; сводка гардов читает маркеры с модуля патч-скрипта и из `_G`.

**Причина**

1. `_G.start_body_search` в сборке пустой — FDDA-гард 0.6.1 не вставал.
2. Поздний `ui_inventory.start` снова входил в FDDA и глотал окно лута.
3. Сводка `patch marker was not found` врала: маркер жил в env файла, не в `_G`.

**Как исправлено**

Тот же приём, что у `utils_obj.find_close_cover`. Отдельный `fix_bhs_fdda_loot.script` в пак не входит.

**Не затронуто**

- Остальные гарды 0.6.1 (cover, DotMarks, mon_sleep, guaranteed_loot, traders, repair).
- Вендорский `liz_fdda_redone_body_search.script`.
- Префиксы `zzzzzz_` (load order).

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 заменить BHS 0.6.1 и снять отдельный `fix_bhs_fdda_loot`.

**Проверено**

- lint overlay: `python tools/lint_addon.py anthology_busyhands_stability_fix`
- В логе после старта: `Anthology Busy Hands Stability Fix 0.6.2 loaded`, `patched (module-table`, `FDDA body search guards installed: 1`.
