# Smart Terrain STATE_Write Nil Guard

## [1.0.3] — 2026-09-19

**Изменено**

- Monkey-patch re-wrap: больше не обнуляет `orig_*` перед `install()` на `actor_on_first_update`.
- `wraps_ok` требует живой `orig`; вызовы оригинала под nil-guard.

**Причина**

Обнуление всех `orig` при частичном сбое wrap оставляло уже наш патч с `orig == nil` → CTD (как `fix_sim_mechanic_trade` / xray_korisnik).

**Не затронуто**

- Игровая логика патча, сейвы, DLTX

**Проверено**

- lint: `python tools/lint_addon.py fix_smart_terrain_state_write`
- в игре: не прогонялось

## [1.0.2] — 2026-09-17

**Изменено**

- `fix_smart_terrain_state_write.script` — `wraps_ok` до early-return; на `actor_on_first_update` переустанавливает wrap STATE_Write/Read после MT reload; `callbacks_registered`.

**Причина**

1.0.1 делал `if installed then return` до сверки указателей. После reload класса снова `table.size(nil)` на :971.

**Не затронуто**

- Heal `npc_info` / `arriving_npc` / `already_spawned`

**Проверено**

- lint: `python tools/lint_addon.py fix_smart_terrain_state_write`
- в игре: не прогонялось

## [1.0.1] — 2026-09-16

**Изменено**

- `gamedata/scripts/fix_smart_terrain_state_write.script` — в `printf` heal `total` формат `%d` заменён на `%s` + `tostring`.

**Причина**

`printf` этой сборки подставляет `%s`, не `%d`. При heal лог мог обрезаться, как у travel 1.0.1.

**Не затронуто**

- Heal `npc_info` / `arriving_npc` / `already_spawned`, wrap `STATE_Write` / `STATE_Read`

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_smart_terrain_state_write`
- в игре: не подтверждено. Ожидание: heal пишет `total=<число>`.

## [1.0.0] — 2026-09-11

**Изменено**

- `gamedata/scripts/fix_smart_terrain_state_write.script` — monkey-patch `smart_terrain.se_smart_terrain:STATE_Write` / `STATE_Read`: перед записью и после чтения гарантирует таблицы `npc_info`, `arriving_npc` (и `already_spawned` при `respawn_point`); throttle-лог имени smart при heal.

**Причина**

Quicksave после боя на Свалке (Депо, кабаны + военные) → FATAL `smart_terrain.script:971` — `table.size(self.npc_info)` при `npc_info == nil` (`xray_exalt.log`). `STATE_Read` пересоздаёт только `arriving_npc`, поэтому возможен объект с валидным `arriving_npc` и nil `npc_info`.

**Как исправлено**

Monkey-patch класса (как Anthology A-Life на `setup_logic`): пустые таблицы вместо nil, оригинал вызывается без изменений сигнатуры. Job/assignment не трогаем.

**Не затронуто**

- Оригинал `smart_terrain.script`
- Логика регистрации NPC, gulag jobs, ассаулты
- `all.spawn`, формат сейва (пустая таблица = «нет NPC на jobs»)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего своего не пишет
- В MO2 после ядра Anthology; префикс не нужен (`-- load-order: after smart_terrain.script`, установка в `on_game_start`)

**Проверка**

- lint: `python tools/lint_addon.py fix_smart_terrain_state_write`
- В игре: не подтверждено. Репро: отбить атаку на Депо → quicksave без FATAL на `:971`; при heal в логе `healed nil tables [npc_info] name=...`.
