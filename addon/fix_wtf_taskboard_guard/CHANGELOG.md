# WTF / PDA Taskboard Macro Guard

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_wtf_taskboard_guard.script` — monkey-patch: `igi_text_processor.Macro.resolve`, `igi_task_manager.is_valid_quest`, `igi_generic_task.try_prepare_quest`, `axr_task_manager.generate_available_tasks`, `pda_taskboard.refresh_tasks` / `prepare_task`.

**Причина**

Обновление PDA Taskboard вызывает `generate_available_tasks` по каждому NPC в радиусе. WTF в `is_valid_quest` готовит кандидата через `try_prepare_quest` → `resolve_and_link_cache` → `Macro.resolve` / `eval(loadstring)`. Повреждённый макрос падает с `attempt to index a nil value` на `igi_text_processor.Macro.link_context.<id>.<field>`. Внутренний `igi_helper.pcall` на корутине этот `loadstring`-eval ловит не всегда, исключение доходит до `pda_taskboard.refresh_tasks` и обрывает доску целиком.

ZIP v1.0.0 BETA подменял три файла целиком (`igi_text_processor.script`, `igi_task_manager.script`, `pda_taskboard.script`). Базой Taskboard взята iTheon-версия, а не `[ANTHFIX] Taskboard + Weather`: при победе в MO2 откатывается ленивая `prepare_category` (фриз 1.4–3.9 с). Если тот ZIP влили в `[QUE] wtf 4_2`, у WTF появляется чужой `pda_taskboard.script`, и WTF перекрывает оба таскборда.

**Как исправлено**

Callback не подходит: генерация идёт из прямых вызовов, не из script callback. Monkey-patch:

- `Macro.resolve` — движковый `pcall` вокруг оригинала, в ошибку добавляются `task_id` / макрос / выражение.
- `is_valid_quest` — реальный путь валидации (локальный снимок `Igi.try_prepare_quest` в WTF не видит патч модуля). Глубокая копия `task_data` (у `dup_table` общая вложенность с JSON-шаблоном), движковый `pcall`, при ошибке `false`. Кандидат отбрасывается, `on_task_crashed` / `set_task_failed` не вызываются.
- `try_prepare_quest` — тот же приём для динамических вызовов мимо снимка.
- `generate_available_tasks` — `pcall` на NPC: ванильная генерация и инъекция WTF не валят остальных.
- `refresh_tasks` / `prepare_task` — запасной `pcall`, чтобы UI доски не оставался с пустым списком. Работает и с iTheon, и с ANTHFIX.

Повтор одной `task_id` пишется в лог один раз за сеанс. Сбрасывается на `on_game_load`.

**Не затронуто**

- файлы WTF и PDA Taskboard (нет полной замены)
- выдача, награды, статусы принятых заданий
- `[ANTHFIX] Taskboard + Weather` (`prepare_category`, кэш категорий)
- `igi_finder` memoize patch
- шаблоны JSON / тексты квестов — битый макрос по-прежнему не «додумывается»
- `all.spawn`, сейвы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Зависимость: Weird Tasks Framework. Без него — no-op по WTF-хукам, guard генерации NPC остаётся
- В MO2 ниже WTF, iTheon PDA Taskboard и `[ANTHFIX] Taskboard + Weather`
- ZIP `Anthology_WTF_Taskboard_Macro_Guard_v1.0.0_BETA` выключить. Если его файлы попали внутрь `[QUE] wtf 4_2` — вернуть оригинальные `igi_*.script` и удалить `pda_taskboard.script` из папки WTF

**Проверено**

- lint: `python tools/lint_addon.py fix_wtf_taskboard_guard`
- В игре: не прогонялось. Ожидаемый лог при битом шаблоне: `Rejected generated task task_id=... quest=... macro=...`, доска обновляется, остальные задания на месте
