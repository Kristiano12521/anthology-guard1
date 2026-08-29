# Sim Mechanic Trade Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_sim_mechanic_trade.script` — monkey-patch `trade_manager.trade_init`, узкий `trade_manager.update` и `stalker_generic.reset_show_spot` для `sim_default_*_mechanic`.

**Причина**

Техник на базе сталкеров на Окраинах Припяти (`okr_base_stalker`, `sim_default_stalker_mechanic`) открывал окно торговли с пустыми полками.

`xr_logic.configure_schemes` при отсутствии поля `trade` подставляет `items\trade\trade_generic.ltx`, у которого `buy_supplies` пустой. Exclusive-джоб `logic@okr_base_stalker_mechanic` уже содержит `trade_generic_mechanic.ltx`, но сим сначала может сесть на кемпинг-джоб без `trade`, либо `aaaa_script_fixes_mp` возвращает `resupply_time` с generic-инициализации. Тогда `update()` не вызывает `buy_supplies`, а `dont_keep_items` уже очистил инвентарь.

ZIP `Vasya Trades Fix` хардкодил имя `sim_default_stalker_mechanic11859` и id `11859` (id сейва, не story_id) и форсил ресток всем торговцам без `current_buy_supplies`.

**Как исправлено**

Роль — `xr_conditions.check_npc_mechanic`, не id. Если симу пришёл дефолтный generic cfg, подменяем на `trade_generic_mechanic.ltx`. Ресток с `force_refresh` только этому технику и только пока нет `current_buy_supplies` (в том числе после `dont_keep_items`). Иконка — тот же `ui_pda2_mechanic_location`, что ставит `reset_show_spot` при `level_spot = mechanic`.

**Не затронуто**

- `trade_generic_mechanic.ltx`, `trade_generic.ltx`, пресеты и скидки
- `okr_base_stalker_tech.ltx` и прочие exclusive-джобы (поля `trade` / `level_spot` уже есть)
- `suitable` / prior смарт-террейнов, `meet`, `all.spawn`
- Именные техники (Кардан, Шайба и т.д.)
- Таблица сейва `trade_manager`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Пустой сток нальётся на следующем `trade_init` / `update` этого NPC
- В MO2 ниже сборки (после `aaaa_script_fixes_mp`). ZIP `Vasya Trades Fix` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_sim_mechanic_trade`
- В игре: не прогонялось. Ожидание: сим-техник на `okr_base_stalker` открывает торговлю с supplies_1+ и иконкой техника на карте
