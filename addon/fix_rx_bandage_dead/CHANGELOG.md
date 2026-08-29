# RX Bandage Dead NPC Guard

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_rx_bandage_dead.script` — monkey-patch `evaluator_bandage:evaluate`, `action_bandage:initialize`, `action_bandage:execute`.

**Причина**

NPC в smart cover начинает действие перевязки, умирает до/в момент `initialize()`, и скрипт вызывает `set_smart_cover_target_idle()`. Движок: `CAI_Stalker: do not call smart_cover_setup_idle_target when stalker is dead` (`rx_bandage.script:175`).

`action_bandage:finalize` уже выходит, если `not npc:alive()`. `xr_smartcover.action_smartcover_activity:target_selector` тоже возвращается до того же вызова. `initialize` / `evaluate` / `execute` — нет. На смерти `rx_ai` подменяет evaluator на `property_evaluator_const(false)`, но `initialize` ещё может успеть отработать в этом кадре.

ZIP v1.0.0 BETA подменял весь `rx_bandage.script` ради одной строки `npc:alive() and npc:in_smart_cover()`. Любой другой мод на этот файл (в том числе Kristiano Fixes) либо затирается, либо затирает патч.

**Как исправлено**

Callback не подходит: вызов идёт из GOAP `action_base.initialize`, не из script callback. Monkey-patch классов `rx_bandage`:

- `evaluate` — мёртвый NPC сразу `false`, действие не стартует и не держится.
- `initialize` — если уже труп, только `action_base.initialize` (учёт планировщика), оригинал не вызывается. Живой — полный оригинал.
- `execute` — на трупе no-op (`play_cycle` / `set_item` / `set_sight` трупу не нужны).

Оригинал `rx_bandage.script` не подменяется.

**Не затронуто**

- сам `rx_bandage.script`, `bandage.ltx`, спавн аптечек/бинтов
- логика лечения живых NPC, анимации, `state_mgr.lock`
- `action_bandage:finalize`, `hit_callback`, `npc_death`
- `xr_smartcover.script`
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 ниже сборки. Если включён Kristiano с его `rx_bandage.script` — этот гард идемпотентен (лишняя проверка `alive()` не мешает)
- ZIP `Anthology_RX_Bandage_Dead_NPC_Guard_Fix_v1.0.0_BETA` выключить: он целиком заменяет `rx_bandage.script`

**Проверено**

- lint: `python tools/lint_addon.py fix_rx_bandage_dead`
- В игре: не прогонялось. Ожидаемый лог: `loaded v1.0.0 wrapped evaluate/initialize/execute`. Убить NPC в момент перевязки в smart cover — без FATAL на `set_smart_cover_target_idle`
