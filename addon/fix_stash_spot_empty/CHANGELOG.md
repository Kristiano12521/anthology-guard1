# Stash Spot Empty Fix

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT. В MO2 рядом с `fix_stash_id_desync` / Grok Stash Overhaul (порядок не критичен).

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Уже снятые метки остаются снятыми. Без фикса залипшие споты на пустых ящиках могут снова появляться.

## [1.0.0] — 2026-09-25

**Изменено**

- `gamedata/scripts/fix_stash_spot_empty.script` — после забора/открытия ящика (отложенный тик) и одним repair-проходом по загрузке снимает `treasure` / `treasure_searched` / `treasure_unique`, если ящик пуст и `caches[id]` не строка ожидания лута. Офлайн — только при `caches[id] == false`.

**Причина**

`treasure_manager.actor_on_item_take_from_box` снимает метку только при `caches[id] == true`. После полного лута с другим состоянием кэша (или без срабатывания ветки) ящик пустой (`Неизвестный тайник (пусто)`), а спот на карте остаётся (пример: `topi_secret_5`).

**Как исправлено**

Callback на `actor_on_item_take_from_box` и `physic_object_on_use_callback` + отложенный `CreateTimeEvent(0)` (после `try_spawn_treasure`). Неоткрытый тайник не трогается: `caches[id]` — строка. `caches` / `release_stash_by_id` не меняются.

**Не затронуто**

- `treasure_manager.caches`, `caches_count`, `release_stash_by_id`
- `fix_stash_id_desync` (десинк id на не-ящик)
- `all.spawn`, квестовые метки, содержимое тайников
- рюкзаки игрока: при опустошении спот и так снимает `item_backpack`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции; залипшие споты чистятся repair-проходом
- Конфликты: двойное снятие спота с ванилью/Grok безвредно

**Проверено**

- lint: `python tools/lint_addon.py fix_stash_spot_empty`
- в игре: не прогонялось. Ожидание: `loaded v1.0.0`, при залипших — `cleared id=...`, в конце `repair done spots=N`; метки `topi_secret_*` на пустых ящиках исчезают после загрузки/повторного открытия
