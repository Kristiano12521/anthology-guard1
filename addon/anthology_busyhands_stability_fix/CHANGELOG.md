# Anthology Busy Hands Stability Fix

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
