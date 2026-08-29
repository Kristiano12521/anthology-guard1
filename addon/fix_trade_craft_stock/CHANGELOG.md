# Trade Craft Stock Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/items/trade/mod_trade_generic_mechanic_fix_trade_craft_stock.ltx` — DLTX: `steel_wool = 2, 1` в `[supplies_1]` generic-техника.
- `gamedata/configs/items/trade/mod_trade_generic_medic_fix_trade_craft_stock.ltx` — DLTX: `jar = 2, 1` в `[supplies_1]`; `jar = 1, 1` в `[trade_generic_buy]` и `[trade_generic_sell]`.

**Причина**

`steel_wool` (Стальная пряжа) стоит в `[tools]` рядом с `grease` / `duct_tape` и нужен ремкомплектам и крафту. В `[HARD] SYS_Balance` `trade_generic_mechanic.ltx` эти расходники продаёт, пряжу — нет. Профиль `[mechanic]` `tools` не исключает, поэтому достаточно supplies.

ZIP `Anthology_Steel_Wool_Technician_Stock_Fix_v0.1.0_BETA` ставил `steel_wool = 1, 1` во все четыре тира через `@[supplies_*]` «на случай, если наследование уже раскрыто». В этой сборке DLTX на трейд-файлы файловый: `mod_trade_generic_mechanic_*.ltx` патчит только этот ini. `[supplies_2]:supplies_1` (и дальше) живой — так же работают Fillable Canteens и PDA Hacking. Соседи в `[tools]` (`grease`, `duct_tape`) заданы один раз в `supplies_1` с количеством `2, 1`.

`jar` (Пластиковая банка, комментарий в `items_trash.ltx`: Plastic jar) нужен крафту `yadylin` и `drug_booster`. В ванили 1.5.2 и в SYS_Balance его нет ни в одном supplies. Предмет в `[trash]`, профиль `[medic]` наследует trash как NO TRADE (имя без коэффициента). Один supplies без override buy/sell положил бы банку в инвентарь торговца, но не в продажу. Сейчас банка только в луте NPC (`death_items.ltx`, шанс ~0.01–0.03).

**Как исправлено**

Два DLTX, только недостающие поля. Техник: пряжа в базовом стоке, как смазка и скотч; тиры 2–4 берут её наследованием. Медик: банка в стоке и явное разрешение купли/продажи поверх исключения trash — тот же приём, что у `itm_drugkit` в этом файле.

**Не затронуто**

- `trade_presets.ltx`, профили `[mechanic]` / `[medic]` / `[trash]` / `[tools]`
- Именные торговцы (Кардан, Сахаров, Сидорович и т.д.)
- `common_stock`, лут с трупов, рецепты
- Коэффициенты остальных товаров, скидки, `buy_item_exponent`
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. На уже сгенерированном стоке банка и пряжа появятся после обычного рестока торговца
- В MO2 ниже `[HARD] SYS_Balance`. ZIP v0.1.0 BETA и копию `mod_trade_generic_mechanic_steel_wool_fix.ltx` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_trade_craft_stock`
- В игре: не прогонялось. После рестока: generic-техник продаёт Стальную пряжу (2 шт.); generic-медик продаёт Пластиковые банки (2 шт.) и принимает их к скупке
