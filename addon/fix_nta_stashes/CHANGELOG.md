# NTA Stashes Anthology Guard

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_nta_stashes.script` — monkey-patch `z_nta_stashes_utils.populate_stashes_by_levels_table`. Тайник без имени уровня не попадает в `stashes_by_level`; остальные индексируются как в NTA.

**Причина**

NTA при загрузке строит `stashes_by_level` одной строкой: `alife():level_name(game_graph():vertex(gvid):level_id())`, затем `stashes_by_level[lvl] = {}`. На Anthology 2.1 в `treasure_manager.caches` бывает запись с неразрешимой вершиной (подтверждено: id=6253, `game_vertex=65535`, `level_id=168`, `level_name=nil`). Индекс `nil` даёт `table index is nil` в `populate_stashes_by_levels_table` (стек указывает на `actor_on_net_spawn`).

ZIP v1.0.1 подменял `z_nta_stashes_utils.script` целиком. Это конфликт с `[QUE] iTheon Quest Pack`, теряются любые другие функции файла, а база патча могла разъехаться с установленной копией (`on_game_load` vs `actor_on_net_spawn`). Оригинал нельзя обернуть одним `pcall`: первая битая запись обрывает всю таблицу.

**Как исправлено**

Callback не подходит: построение идёт из прямого вызова NTA, не из script callback. Monkey-patch функции на модуле NTA. Оригинал не вызывается — он падает. Цикл тот же (`pairs(treasure_manager.caches)` → `alife_object` → `game_graph():vertex` → `level_name`), плюс проверка имени уровня. Пропуск только этой записи; `treasure_manager` и alife-объект не трогаются. Обёртка стоит до вызова NTA (`on_game_start` / повтор на `on_game_load`), поэтому не важно, `on_game_load` это или `actor_on_net_spawn`.

**Не затронуто**

- `z_nta_stashes_utils.script` и остальные файлы iTheon / NTA
- `treasure_manager.caches`, чёрный список тайников, сюжетные тайники
- `tasks_nta_stash.script` (`dispatch_nta_stash_task_details`, выдача задания)
- `all.spawn`, сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет. Новая игра не нужна
- Зависимость: New Tasks Addon / iTheon Quest Pack. Без него — no-op
- В MO2 ниже `[QUE] iTheon Quest Pack`. ZIP `iTheon_NTA_Stashes_Anthology_Guard_v1.0.0` / `v1.0.1` выключить, чтобы он не перекрывал оригинальный `z_nta_stashes_utils.script`

**Проверено**

- lint: `python tools/lint_addon.py fix_nta_stashes`
- В игре: не прогонялось. Ожидаемый лог: `populate wrapped`, при битой записи `skipped stash id=... game_vertex=65535 level_id=168 reason=no_level_name`, загрузка без `table index is nil`
