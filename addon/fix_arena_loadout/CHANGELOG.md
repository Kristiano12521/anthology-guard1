# Arena Loadout Fix

## [1.0.0] — 2026-08-28

**Изменено**

- `gamedata/scripts/fix_arena_loadout.script` — monkey-patch `xr_effects.bar_arena_teleport` в `on_game_start`: после выдачи Арни убирает несовместимые магазины MAG, спавнит `weapon_default_magazine` под фактическое оружие и заряжает экзач (БП + энергия).

**Причина**

Mags Redux в `mags_patches.script` выдаёт магазины по таблице ванильной Anomaly 1.5.1 (1911, ОЦ-33, Вал, STANAG). Anthology на арене даёт другое оружие (ПМ, MP5, Гроза, G36) — магазины не встают. Exo System в `exo_loot.free_power` ищет только `exobackpack_exo_outfit` и не ставит модуль питания, поэтому обычный `exo_outfit` остаётся с мощностью 0 и игрок ползает.

**Как исправлено**

Обёртка в `on_game_start` (после файловых патчей MAG/Exo). Через 0.35 с после телепорта: несовместимые магазины снимаются, на каждое MAG-оружие — 2 штатных магазина с патронами из `utils_item.get_ammo`; любой экзач (`item_exo_device.is_exo`) заряжается и получает `exo_power_supply`.

**Не затронуто**

- `mags_patches.script`, `exo_loot.script`, `item_exo_device.script`
- Список боёв и стволы Арни
- Поведение 4 мастеров в финале (это 4 на 1, не FFA)
- Сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- Зависимости: Mags Redux (магазины), Exo System (экзач). Без них соответствующая часть — no-op
- В MO2 ниже MAG Redux и Exo System

**Проверено**

- lint: `python tools/lint_addon.py fix_arena_loadout`
- В игре: после старта в логе `bar_arena_teleport wrapped`. Бой с ПМ/MP5/Грозой/G36 — магазины от этого ствола. 8-й бой — экзач с БП и мощностью > 0, можно бежать.
