# Melee Trade Supplies Guard

## [1.0.0] - 2026-09-16

**Изменено**

- `gamedata/scripts/fix_melee_trade_supplies.script` — monkey-patch `melee_trade_inject.vks_spawn_stock`: сообщение `! Trader has no supplies for this supply level` перехватывается, пишется один раз на пару npc|level нашим тегом, геймплей тот же (инжект милишки не делается).

**Причина**

R.A.K `melee_trade_inject` для части торговцев (нет faction в `ini_by_faction`, нет секции `supplies_*` / `supplies_generic` в melee-ini) всегда печатает bang-printf. Обычный trade не ломается.

**Не затронуто**

- `trader_autoinject`, обычные `trade_*.ltx`
- состав melee-стока, когда секция есть

**Совместимость**

- Нужен R.A.K Base с `melee_trade_inject`
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_melee_trade_supplies`
- в игре: не подтверждено. Ожидание: нет `! Trader has no supplies...`; есть разовые `[fix_melee_trade_supplies] skip missing melee supplies`.
