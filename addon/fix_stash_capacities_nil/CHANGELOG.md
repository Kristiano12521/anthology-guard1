# Stash Capacities Nil Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; в MO2 рядом с Hideout Furniture (`stash_capacities`). Префикс не нужен: перехват в `on_game_start` / `actor_on_first_update`.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без guard'а снова возможен CTD при Shift-луте стека — исходный баг, не след отключения.

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
