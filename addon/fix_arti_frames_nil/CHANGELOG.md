# Arti Frames Nil Guard

## [1.0.2] — 2026-09-17

**Изменено**

- `fix_arti_frames_nil.script` — `wraps_ok` (current==guarded); на `actor_on_first_update` переустанавливает wrap, если модуль уже не наш; uninstall только если указатель ещё наш; `callbacks_registered`.

**Причина**

1.0.1 при `installed=true` не сверял указатели. После MT reload снова возможен FATAL `obj:id()` на Move_All.

**Не затронуто**

- Отсев `obj == nil`, steal callback

**Проверено**

- lint: `python tools/lint_addon.py fix_arti_frames_nil`
- в игре: не прогонялось

## [1.0.1] — 2026-09-16

**Изменено**

- `gamedata/scripts/fix_arti_frames_nil.script` — в `printf` `batch_total` формат `%d` заменён на `%s` + `tostring`.

**Причина**

`printf` этой сборки подставляет `%s`, не `%d`. При skip лог мог обрезаться, как у DAV 1.0.2.

**Не затронуто**

- Отсев `obj == nil`, steal callback, retry на `actor_on_first_update`

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_arti_frames_nil`
- в игре: не подтверждено. Ожидание: skip пишет `batch_total=<число>`.

## [1.0.0] — 2026-09-08

**Изменено**

- `gamedata/scripts/fix_arti_frames_nil.script` — monkey-patch `arti_frames_control.on_move`: при `obj == nil` выход без вызова оригинала; throttle-лог в xray.

**Причина**

Лут патронов через fast transfer (`ish_fast_transfer` → `Action_Move_All`) после `ammo_aggregation` шлёт `ActorMenu_on_item_after_move` с уже мёртвым child id. `Action_Move` печатает `Can't get item game object!`, но callback всё равно уходит. `arti_frames_control.on_move` на строке 98 делает `obj:id()` → FATAL `lua_pcall_failed` (лог `xray_mg9000 (3).log`, уровень `topi`).

**Как исправлено**

Точечный monkey-patch модуляика (глобальный модуль + перехват callback) — оригинал через `UnregisterScriptCallback`, затем обёртка. Проверка именно на nil, не на destroyed userdata (`fix_minigun_dead_parent`): достаточно `obj == nil`, без `pcall` и без правок в инвентарь. Логика рюкзаков/фреймов не меняется.

**Не затронуто**

- Оригинал `arti_frames_control.script`
- `ui_inventory.script`, `ish_fast_transfer.script`, `item_weapon.ammo_aggregation`
- `fix_dynamic_armor_visuals_nil` (тот же класс бага, другой слушатель)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 после BS Attachments / `arti_frames_control`; префикс не нужен (`-- load-order`)

**Проверка**

- lint: `python tools/lint_addon.py fix_arti_frames_nil`
- lint cross: `python tools/lint_addon.py --cross`
- В игре: не подтверждено. Репро: лутать патроны 5.56 take-all с трупа в топях — без LUA FATAL на `arti_frames_control.script:98`; в логе при срабатывании `skip nil obj`.
