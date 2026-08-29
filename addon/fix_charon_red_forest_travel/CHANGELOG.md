# Charon Red Forest Travel Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_charon_red_forest_travel.script` — monkey-patch `mlr_utils.change_lvl` для ключа `red_forest_guid_mon`. На время вызова оригинала в `SIMBOARD.smarts_by_names` появляется алиас отсутствующего `red_bridge_bandit_smart_skirmish_mlr` на живой `red_bridge_bandit_smart_skirmish`.

**Причина**

Харон (проводник Монолита) в диалоге вызывает `dialogs_mlr.red_forest_guid_mon` → `mlr_utils.change_lvl("red_forest_guid_mon")`. Локальная таблица `CLT` в `mlr_utils.script:15` указывает на smart `red_bridge_bandit_smart_skirmish_mlr`. В спавне Anthology 2.1 этого smart нет; `change_lvl` на строке 75 делает `se_obj.position` по nil — Lua error.

Живая точка на мосту — `red_bridge_bandit_smart_skirmish` (есть в `simulation_objects_props_l10_red_forest.ltx`). Обычный маршрут `red_forest_guid` сажает на `red_smart_terrain_bridge` и к Харону не относится.

Бета v1.0.1 полностью подменяла `change_lvl` своей телепортацией (время, погода, `ChangeLevel`), ставила `zzzz`-префикс, регистрировала callback'и с верхнего уровня и каждые 60 кадров переустанавливала обёртку через `actor_on_update`. Так она обходила top-level monkey-patch Hard+ (`zzzz_for_level_add.script`), но дублировала штатный travel и оставляла постоянный тик.

**Как исправлено**

`CLT` локальная, DLTX smart не создаст без `all.spawn`. Оборачиваем текущий `mlr_utils.change_lvl` в `on_game_start` — к этому моменту Hard+ уже повесил свой top-level wrap, цепочка сохраняется. Для остальных ключей вызов идёт как есть. Алиас снимается сразу после оригинала, чтобы `pairs(SIMBOARD.smarts_by_names)` не видел второй экземпляр того же smart. Если целевой smart уже есть, патч ничего не трогает. Если нет ни основного, ни `red_smart_terrain_bridge` — travel отменяется без обращения к nil.

**Не затронуто**

- `mlr_utils.script`, `dialogs_mlr.script`, диалоги Харона и цена маршрута
- остальные ключи `CLT` и маршруты MLR / Immersive Travel
- `red_forest_guid` → `red_smart_terrain_bridge`
- Hard+ `zzzz_for_level_add.script` (`NEW_LEVELS` / `ChangeLevel`)
- `SIMBOARD` вне этого вызова, `all.spawn`, сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 ниже сборки и Hard+ (`SYS radioactive_air_toxic_air_rework`). Бета v1.0.0–v1.0.1, диагностический скрипт и копию `zzzzzzzzzzzzzz_anthology_charon_red_forest_travel_fix.script` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_charon_red_forest_travel`
- В игре: не прогонялось. Загрузить сейв у Харона, выбрать «Рыжий лес». В логе: `change_lvl wrapped`, затем `aliased red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish`. Прибытие — бандитский мост Рыжего леса, без `attempt to index local 'se_obj'`
