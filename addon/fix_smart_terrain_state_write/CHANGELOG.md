# Smart Terrain STATE_Write Nil Guard

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
