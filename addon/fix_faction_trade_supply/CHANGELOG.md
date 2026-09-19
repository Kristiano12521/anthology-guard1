# Faction Trade UI supply_level crash fix

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; после мода с `faction_trade_ui` / `action_trade_ui` (Faction Based HUD / Kristiano pa.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.1] — 2026-09-17

**Изменено**

- `fix_faction_trade_supply.script` — если `trader_autoinject.supply_level` вернул `nil`, уровень не показывается (раньше подставлялась «1»).

**Причина**

SUPPLIER/MEDIC/MECHANIC без `buy_supplies` получал ложный уровень 1. Ваниль в этом случае ничего не рисует.

**Не затронуто**

- Защита от concatenate function `supply_level`, вызов `trader_autoinject.supply_level(npc, true)`

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_faction_trade_supply`
- в игре: не прогонялось

## [1.0.0] — 2026-09-03

**Изменено**

- `gamedata/scripts/fix_faction_trade_supply.script` — monkey-patch `ui_inventory.UIInventory.UpdateHarukaTradeWindow`: уровень поставок берётся через `trader_autoinject.supply_level` / только `type == "number"`, без конкатенации глобальной функции `supply_level`.

**Причина**

Торговля с барменами Кордона (Тихоныч, Патогеныч) → FATAL в `faction_trade_ui.script:32` (`UpdateHarukaTradeWindow`): `attempt to concatenate global 'supply_level' (a function value)`.

Аддон Faction Based HUD пишет в глобал `supply_level` число или `nil`. У `BARMAN` получается `nil`, ключ пропадает из env скрипта, чтение падает на функцию `supply_level` из `ui_inventory` / `trader_autoinject`. `if supply_level then` для функции истинно → `..` валит Lua.

**Не затронуто**

- `faction_trade_ui.script` / `action_trade_ui.script` файлами не подменяются
- `trader_autoinject`, BusyHands, цены/ресток, XML HUD
- Сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- MO2: после мода с `faction_trade_ui` / `action_trade_ui` (Faction Based HUD / Kristiano pack)

**Проверено**

- lint: `python tools/lint_addon.py fix_faction_trade_supply` — 0 ошибок
- build: `build/fix_faction_trade_supply`
- В игре: не проверено агентом — Кордон, торговля с Тихонычем и Патогенычем; в логе должна быть строка `UpdateHarukaTradeWindow wrapped`, без FATAL на `supply_level`
