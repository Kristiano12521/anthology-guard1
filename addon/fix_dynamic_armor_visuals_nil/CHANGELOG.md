# Dynamic Armor Visuals Nil Guard

## [1.0.0] — 2026-09-04

**Изменено**

- `gamedata/scripts/fix_dynamic_armor_visuals_nil.script` — monkey-patch `dynamic_npc_armor_visuals.actor_on_item_take_from_box`: отсев `item == nil` до вызова оригинала; троттлинг лога отсевов.

**Причина**

При «переложить всё» (`ish_fast_transfer` → `Action_Move_All`) инвентарь шлёт `ActorMenu_on_item_after_move` на каждый child id. К моменту `Action_Move` предмет уже может быть удалён: `CheckItem` возвращает nil, но callback всё равно уходит. Оригинал на строке 166 делает `item:id()` без проверки → LUA error.

**Как исправлено**

Функция экспортирована (глобальная в модуле) и зарегистрирована как callback — снимаем оригинал через `UnregisterScriptCallback`, ставим обёртку. Падение на индексации nil, не на методе destroyed userdata (`fix_minigun_dead_parent`): достаточно `item == nil`, без `pcall` и без обращения к объекту. Логика визуалов не меняется.

**Не затронуто**

- оригинал `dynamic_npc_armor_visuals.script`
- `npc_on_item_take` (там уже есть `not (npc and item)`)
- `npc_armor_visual_update`, `get_visual_prot`, сейв `RAX_default_visuals`
- `ui_inventory.script`, `ish_fast_transfer.script`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 рядом с Dynamic NPC Armor Visuals; скрипт грузится после него (`-- load-order`)

**Проверено**

- lint: `python tools/lint_addon.py fix_dynamic_armor_visuals_nil`
- lint cross: `python tools/lint_addon.py --cross`
- В игре: не прогонялось. Критерий: «переложить всё» на трупе с большим лутом — без LUA error на `dynamic_npc_armor_visuals.script:166`; в логе presence + при отсевах троттлированные `skip nil item`.
