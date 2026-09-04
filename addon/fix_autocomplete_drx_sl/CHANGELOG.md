# Autocomplete DRX SL Guard

## [1.0.0] — 2026-09-03

**Изменено**

- `gamedata/scripts/fix_autocomplete_drx_sl.script` — monkey-patch `z_autocomplete_tasks_core.should_autocomplete`: задания с эффектом `drx_sl_` в `on_init` / `on_complete` / `on_fail` не автозакрываются.

**Причина**

На Курчатове (`kurchatov_37`) Autocomplete Tasks закрыл DRX SL-баунти `simulation_task_31a` сразу после убийства цели. В логе: `[AT] Autocompleting task` → `DRX SL task ended` → зависание без FATAL. Без AT задание сдаётся через диалог и зависания нет.

У баунти `task_status_functor.bounty_task` после смерти цели ставит `stage = 1` (вернуться к заказчику), а не `complete`. AT считает `stage == stage_complete` достаточным и вызывает `set_task_completed` в поле. Список `PROTECTED_TASK_EFFECTS` в AT не содержит `drx_sl_`.

**Как исправлено**

Monkey-patch публичного `should_autocomplete` (локальный `is_safe_anthology_combat_task` недоступен). DLTX бесполезен: секции `simulation_task_*` создаются рантаймом. Callback на смерть NPC не отличит «можно закрыть» от «нужен диалог». AT остаётся включённым для обычных assault / bounty / spring-clean / destroy BTR.

**Не затронуто**

- файлы `[GAM] Autocomplete Tasks`
- ванильный баунти без `drx_sl_*` в condlist
- assault, зачистка мутантов, уничтожение БТР
- `set_task_completed`, награды, диалоги DRX SL
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Зависимость: Autocomplete Tasks. Без него — no-op (`guard NOT installed`)
- В MO2 рядом с остальными фиксами; имя скрипта без zzz-префикса, хук в `on_game_start`

**Проверено**

- lint: `python tools/lint_addon.py fix_autocomplete_drx_sl`
- В игре: не прогонялось. Критерий: AT включён, то же DRX SL-задание на устранение — в логе `skip autocomplete tid=simulation_task_* reason=drx_sl_effect`, нет `[AT] Autocompleting task` по нему, игра не зависает; сдать у заказчика как без AT. Обычный не-DRX баунти по-прежнему автозакрывается.
