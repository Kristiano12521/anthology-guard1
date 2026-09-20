# Create Squad Nil Smart Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный FATAL на `sim_board:139` может вернуться.

## [1.0.0] — 2026-09-20

**Изменено**

- `gamedata/scripts/fix_create_squad_nil_smart.script` — monkey-patch:
  1. `SIMBOARD.create_squad` — при `spawn_smart == nil` возвращает `nil` (как `zz_anthology_safe_offline_spawn`), лог один раз на `squad_section` с `caller` через `debug.getinfo`.
  2. `xr_effects.create_squad` — ранний `return` при неизвестном `smart_name` (в эталоне был только `printf`), лог один раз на имя smart с `squad_id` и `caller`.

**Причина**

`sim_board.script:139` — `attempt to index local 'spawn_smart' (a nil value)`. Condlist `%=create_squad(секция:smart)%` / прямые вызовы с smart, которого нет в `SIMBOARD.smarts_by_names`. В `xr_effects.create_squad` проверка smart без `return`.

**Как исправлено**

Monkey-patch по событию (`on_game_start` / `actor_on_first_update`), префикс имени файла не нужен. Цепочка с `zz_anthology_safe_offline_spawn`: на один объект `SIMBOARD` ставимся один раз и остаёмся их `original`, либо оборачиваем уже их обёртку — `original` у zz не ломаем.

**Не затронуто**

- Успешный спавн при валидном smart
- `utils_obj.create_squad` (там уже есть ранний выход)
- `fix_nil_crash_guards` и прочие nil-гарды
- Сейвы / MCM

**Остаточный риск**

Редкие вызывающие без проверки результата (например `tasks_defense.script` сразу берёт `sq.id`) при `nil` smart раньше падали на `:139`, теперь могут упасть у себя. Перед этим в логе будет наша строка `skip create_squad: spawn_smart=nil squad=… caller=…`.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: ничего не пишет
- Совместим с `zz_anthology_safe_offline_spawn` через цепочку monkey-patch

**Проверено**

- lint: `python tools/lint_addon.py fix_create_squad_nil_smart`
- В игре: не прогонялось. Сигнатура из чужого лога; у нас в `logs/` этой FATAL нет. Ожидание: presence `loaded v1.0.0`, строки `wrapped SIMBOARD.create_squad` / `wrapped xr_effects.create_squad`; при битом smart — `skip …` один раз на ключ, без CTD на `:139`.
