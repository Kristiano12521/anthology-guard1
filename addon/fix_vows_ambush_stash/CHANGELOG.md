# Valley of Whispers Ambush & Ilya Stash Fix

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; `printf` с причиной при раннем выходе из `install()`.

**Не затронуто**

- Обёртка activate_by_section, онлайн-ремонт stash.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/sad/mod_sad_b1_iliya_treasure_fix_vows_ambush_stash.ltx` — DLTX на `[ph_idle@locked]`: лут спавнится один раз в `on_use` с ключом; сломанный `on_info` удалён.
- `gamedata/configs/scripts/sad/mod_sad_sim_3_cs_actor_fix_vows_ambush_stash.ltx` — DLTX на `[animpoint@5]`: запасной `on_timer` ставит `sad_sim_3_rob_snorki`, если функтор прыжка не сработал.
- `gamedata/scripts/fix_vows_ambush_stash.script` — обёртка `xr_logic.activate_by_section` только для `sad_b1_iliya_treasure`: битый/`nil` `active_section` из сейва меняется на `@wait` или `@locked`.

**Причина**

У тайника Ильи `on_info` в `@locked` начинается с `%=spawn_object_in(medkit:...)` без закрывающего `%` на этой строке. `parse_condlist` принимает строку за имя секции, `switch_to_section` уходит в несуществующую схему, ящик остаётся без логики, в сейв пишется мусорный `active_section`. Лут не появляется, ключ не снимается.

У засады братьев дублёр в `@5` ждёт `+sad_sim_3_rob_snorki` из `into` анимации `sad_rob_veranda_jump`. Если wounded проигрывает ролик в обход функтора, братья не выходят из `remark@1_4`, камера заканчивает сцену по `cameff_end`, а не по `sad_sim_3_rob_actor_away`.

ZIP v1.0.0 подменял три LTX целиком, ставил `zzzz_sad_valley_quest_fix.script`, вешал wrap на загрузке файла и не снимал его. `spawn_object` в `sad_sim_3_rob_logic.ltx` менял на `create_cutscene_actor_with_weapon`, хотя дублёр уже забирает ствол через `sad_take_item_from_actor_slot` и возвращает через `sad_relocate_items_npc_slots_to_actor` — клон плюс перенос даёт два оружия.

**Как исправлено**

Логика тайника и флаг прыжка — DLTX, без замены файлов. Состав лута как в стоке, спавн один раз при успешном `on_use`. Спавн дублёра не тронут. Wrap только на активации этого ящика, оригинал снимается в `on_game_end`. Онлайн-сейв чинится ещё раз в `actor_on_first_update`, если объект уже на уровне.

**Не затронуто**

- `sad_sim_3_rob_logic.ltx` (`spawn_object`, камера, `cameff_end`, `sad_sim_3_cutscene_rob_time`)
- `sad_sim_3_mudak_job.ltx`, `state_mgr_scenario_sad.script`, `xr_effects_sad.script`
- `nonscript_usable` у `@wait`, состав лута, ключ `sad_mudak_inventory_key`
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без новой игры. Битый `active_section` тайника чинится при активации объекта. Открытый `@open` не трогается
- Конфликты: нет пересечения файлов с ZIP v1.0.0 (тот заменял оригиналы и `zzzz*.script`). В MO2 ниже сборки; ZIP и копию в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_vows_ambush_stash`
- В игре: не прогонялось. Засада: после прыжка братья смотрят на снорков и стреляют, сцена кончается по `sad_sim_3_rob_actor_away`. Тайник: ключ в инвентаре, использование один раз наполняет ящик и снимает ключ. Сейв с битой секцией: в логе `recovered section [%...] -> [ph_idle@...]`
