# Zaton B12 Military Box Spawn Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/zaton/mod_zat_b12_item_spawner_fix_zat_b12_box.ltx` — DLTX на `[sr_idle@spawn_keys]`: `on_info3` ставит `+zat_b12_item_3_spawned` и не стреляет, если уже есть ошибочный `+zat_b12_item_5_spawned`; `on_info4` на затронутых сейвах только выставляет `item_3`, без повторного спавна восьми предметов.

**Причина**

В стоке `zat_b12_item_spawner.ltx` строка `on_info3` проверяет `-zat_b12_item_3_spawned`, а выставляет `+zat_b12_item_5_spawned`. Флаг-страж не защёлкивается. `sr_idle` гоняет `on_info*` каждый апдейт, пока схема в `@spawn_keys`; `on_info3` не переключает секцию, поэтому `xr_effects.spawn_object_in` в `zat_b12_millitary_box` может вызваться снова при реините логики (в логе пачка из восьми `trying to find object zat_b12_millitary_box`). `zat_b12_item_5_spawned` больше нигде не читается.

ZIP v0.1.0 BETA подменял весь файл, включая ключи, баллон и `@end`. Копия лежит в `[DBG] Kristiano Fixes ALL IN ONE`.

**Как исправлено**

Два поля существующей секции. Чистый сейв: нет ни `item_3`, ни `item_5` → один спавн и правильный флаг. Сейв с опечаткой: есть `item_5`, нет `item_3` → только `+item_3`. Условия взаимоисключающие: `pairs()` в `try_switch_to_another_section` не гарантирует порядок `on_info3`/`on_info4`.

**Не затронуто**

- `on_info` / `on_info2` (ключи и документы в `zat_b12_key_*_box`)
- `[sr_idle@spawn_balon]` и спавн `zat_b57_gas` (своего флага в стоке нет)
- `zat_b12_conteiner.ltx`, `zat_b12_quest_line.ltx`
- `xr_effects.spawn_object_in`, состав содержимого ящика
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: миграция через инфопорцию, новая игра не нужна
- Конфликты: нет пересечения файлов с ZIP v0.1.0 (тот заменял оригинал). В MO2 ниже сборки; ZIP и копию `configs/scripts/zaton/zat_b12_item_spawner.ltx` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_zat_b12_box`
- В игре: не прогонялось. На Затоне после загрузки сейва не должно быть новой серии из восьми `xr_effects.spawn_object_in trying to find object zat_b12_millitary_box`. Повторный переход/сейв/загрузка — ящик не обрастает патронами и гранатами
