# Stash Capacities Nil Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; в MO2 рядом с Hideout Furniture (`stash_capacities`). Префикс не нужен: перехват в `on_game_start` / `actor_on_first_update`.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без guard'а снова возможен CTD при Shift-луте стека — исходный баг, не след отключения.

## [1.0.4] — 2026-09-26

**Изменено**

- `disarm_register_hook` больше не обнуляет `saved_register`. С `_G` хук снимается, только если мы всё ещё верхний слой. `hooked_register` не зовёт nil.

**Причина**

Сессия nikit 2026-09-26 16:39, скрипт 1.0.3: после `guard installed` FATAL `attempt to call upvalue 'saved_register' (a nil value)` на строке 186. `fix_travel_invalid_id` на своём `on_game_start` сохранил наш `hooked_register` как `orig_register`, а наш `actor_on_first_update` раньше обнулил `saved_register`. Дальше travel → `orig_register` → наш хук → nil.

**Не затронуто**

- Nil-check `obj:weight()`, логика steal, сейвы

**Проверено**

- `tools/lint_addon.py fix_stash_capacities_nil`
- В игре ещё нет

## [1.0.3] — 2026-09-26

**Изменено**

- `module_of` больше не читает `_G[name]`. Только `rawget`. Если таблицы модуля нет, хук `RegisterScriptCallback` остаётся включённым до `actor_on_first_update`.

**Причина**

Сессия mg9000 2026-09-26 16:18, AIO 1.0.9 / скрипт 1.0.2: загрузка файла прошла (`loaded v1.0.2`), вылет тот же `invalid parameter` уже из `on_game_start`. Стек: `module_of:82` `_G["stash_capacities"]` ← `install:211` ← `on_game_start:268` ← `axr_main`. Перенос вызова с загрузки файла на `on_game_start` не убрал C `__index`.

**Не затронуто**

- Nil-check `obj:weight()`, хук регистрации, сейвы

**Проверено**

- `tools/lint_addon.py fix_stash_capacities_nil`
- В игре ещё нет

## [1.0.2] — 2026-09-26

**Изменено**

- `install()` больше не вызывается при загрузке файла. На загрузке остаётся только подмена `RegisterScriptCallback`. Поиск модуля `stash_capacities` — из `on_game_start`, когда этот файл уже выполнен.

**Причина**

Сессия mg9000 2026-09-26 15:43, AIO 1.0.8: сразу после `loaded v1.0.1` вылет `invalid_parameter_handler` (`xrDebugNew.cpp:1120`). Стек: `module_of` строка 78 `_G["stash_capacities"]` ← `install` ← тело файла строка 262. Скрипт грузится раньше `stash_capacities.script`; C `__index` у `_G` догружает ещё не открытый файл и рвёт CRT.

**Не затронуто**

- Сам nil-check `obj:weight()`, перехват регистрации callback, сейвы

**Проверено**

- `tools/lint_addon.py fix_stash_capacities_nil`
- В игре ещё нет

## [1.0.1] — 2026-09-26

**Изменено**

- `gamedata/scripts/fix_stash_capacities_nil.script` — перехват `RegisterScriptCallback` с загрузки файла, до `on_game_start` Hideout Furniture. В обёртку попадает только функция, у которой `debug.getinfo` source/short_src содержит `stash_capacities`. Поиск модуля через `_G[name]`, не только `rawget`. Поздний steal из `intercepts` смотрит полный `source`, не только урезанный `short_src`.

**Причина**

Сессия mg9000 2026-09-26: `loaded v1.0.0`, затем `stash_capacities.on_game_start not found` и `after_move nil-guard NOT installed`. Обработчик `actor_on_item_after_move` локальный (`stash_capacities.script:90`); одного `rawget` по `on_game_start` не хватило, callback к `actor_on_first_update` уже был зарегистрирован мимо гарда.

**Не затронуто**

- Сам `stash_capacities.script`, `ui_inventory`, остальные подписчики `ActorMenu_on_item_after_move`
- Сейвы

**Проверено**

- `tools/lint_addon.py fix_stash_capacities_nil`
- В игре ещё нет

## [1.0.0] — 2026-09-25

**Изменено**

- `gamedata/scripts/fix_stash_capacities_nil.script` — nil-guard на локальный `stash_capacities` callback `ActorMenu_on_item_after_move`. При `obj == nil` выход без `obj:weight()`.

**Причина**

Shift-лут трупа (`ish_fast_transfer` → HF `Action_Move_All`) ставит `weight_add` и шлёт `ActorMenu_on_item_after_move` с уже мёртвым child id. `Action_Move` печатает `Can't get item game object!`, но callback всё равно уходит. `actor_on_item_after_move` на строке 92 делает `obj:weight()` → FATAL `lua_pcall_failed` (лог `xray_mg9000.log`, сейв `fatal_ctd_save_1`). У `before_move` nil-check есть, у `after_move` нет. Тот же корень, что `fix_arti_frames_nil`.

**Как исправлено**

Обработчик локальный, слот модуля не патчится. `stash_capacities.on_game_start` подменяется: на время вызова `_G.RegisterScriptCallback` подменяет функцию из `stash_capacities.script` на guard. Если callback уже зарегистрирован — снятие через `UnregisterScriptCallback` после поиска в `intercepts` (`debug.getupvalue` на `axr_main.callback_set`). Повтор на `actor_on_first_update`, если MT подменил модуль. Оригинал вызывается, когда `obj` не nil.

**Не затронуто**

- Оригинал `stash_capacities.script`, `ui_inventory.script`, `ish_fast_transfer.script`
- `ActorMenu_on_item_before_move` (там nil-check уже есть)
- Лимит `capacity` и `weight_add` для живых предметов
- Сейвы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 рядом с Hideout Furniture; префикс не нужен (`-- load-order`)

**Проверено**

- lint: `python tools/lint_addon.py fix_stash_capacities_nil`
- lint cross: `python tools/lint_addon.py --cross`
- в игре: не прогонялось. Репро: Shift-лут стека с трупа — без FATAL на `stash_capacities.script:92`; при срабатывании в логе `skip nil obj`.
