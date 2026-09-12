# Arena Loadout Fix

## [1.1.0] — 2026-09-12

**Изменено**

- `gamedata/scripts/fix_arena_loadout.script` — `pcall` вокруг цепочки `bar_arena_teleport` (MAG/Exo/ваниль). При `attempt to index local 'se'` логирует ошибку и, если в инвентаре ещё нет оружия, безопасно доспавнивает loadout текущего `bar_arena_fight_*` с nil-check перед `se_save_var`. Presence-строка `loaded v1.1.0`.

**Причина**

Ванильный `xr_effects.bar_arena_teleport` после `alife_create` сразу делает `se_save_var(se.id, se:name(), ...)` без проверки. Если секция не создаётся — FATAL в обёртке Mags Redux (`mags_patches.script` / диалог `magc_patches`). У игрока стабильно на 4-м бое арены SoC.

**Не затронуто**

- Таблицы боёв Арни и список стволов
- `mags_patches.script` / `exo_loot.script` на диске
- Поведение при успешном телепорте (как в 1.0.0)
- Сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 ниже MAG Redux и Exo System (как раньше)

**Проверено**

- lint: `python tools/lint_addon.py fix_arena_loadout`
- В игре: не прогонялось. Ожидается: нет CTD на 4-м бое; в логе при сбое — `orig bar_arena_teleport error` и при пустом оружии — `recover bar_arena_fight_N`.

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
