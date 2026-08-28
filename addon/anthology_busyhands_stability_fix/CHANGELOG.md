# Anthology Busy Hands Stability Fix

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
