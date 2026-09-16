# Nil Crash Guards

## [1.1.1] — 2026-09-16

**Изменено**

- `gamedata/scripts/fix_nil_crash_guards.script` — `GUARD_VID_MODE` после wrap модуля пишет обёртку в `ui_options.options` слот `cmd=vid_mode` / `content`. Повтор на `actor_on_first_update`, даже если wrap уже стоял. Uninstall возвращает orig в content.

**Причина**

`reverse_resolution_list_mcm.patch_ress_list` копирует function value в `content = { cont_vid_mode }`. `on_game_start` идёт по алфавиту: `fix_nil_*` раньше `reverse_*`, поэтому поздний patch перезаписывал слот оригиналом — меню разрешений звало не обёртку.

**Не затронуто**

- Остальные семь гардов, тумблеры `GUARD_*`
- Логика skip битых токенов / fallback-список

**Совместимость**

- Как 1.1.0
- Сейвы: ничего не пишет

**Проверено**

- lint: `python tools/lint_addon.py fix_nil_crash_guards`
- в игре: не прогонялось. Ожидание: `wrapped reverse_resolution_list_mcm.cont_vid_mode` и `retargeted ui_options vid_mode content`; Settings → resolution без FATAL на битом токене.

## [1.1.0] — 2026-09-13

**Изменено**

- В шапке `fix_nil_crash_guards.script` — восемь констант `GUARD_*` (по умолчанию `true`). Выключенный гард в `install()` / при загрузке (cover tilt) пропускается; в лог: `skipped GUARD_… (GUARD_…=false)`. MCM нет.
- Presence-строка `loaded v1.1.0`, затем по строке на гард (`wrapped` / `NOT installed` / `skipped` / stub cover tilt).

**Причина**

Один вредный гард нельзя было отключить без снятия всего мода (как с `fix_minigun_dead_parent`: защита раздула ошибки). Нужны ручные тумблеры для точечной диагностики у тестеров.

**Не затронуто**

- Логика обёрток, callbacks, uninstall, сейвы
- Остальные аддоны

**Источники сигнатур (ни одной нет в наших `logs/cards/`)**

Мод целиком собран по чужим логам: ни одна из восьми сигнатур в наших карточках не встречается. Строка `wrapped` подтверждает только то, что обёртка встала, но не что она отсекает правильно. Настоящее подтверждение придёт от тестера, у которого эта сигнатура была. Это первый мод, который надо отдавать тестерам раньше, чем себе.

| Гард | Константа | Источник | Подтверждение ждать у |
|---|---|---|---|
| `item_knife.get_condition` → nil (`bind_crow`) | `GUARD_ITEM_KNIFE` | Discord-скрин, пачка авг 2026 (`IMG-20260807…`); автор в разборе не зафиксирован | кто прислал crow/knife FATAL |
| Semenov `task_functor` / `squad` nil | `GUARD_SEMENOV_TASK` | Discord-скрин, та же пачка авг 2026; автор не зафиксирован | кто падал на Янтаре / Semenov |
| `unregister_npc` nil (`se_monster` / `se_stalker`) | `GUARD_UNREGISTER_NPC` | Discord-скрин, та же пачка (смена лока / химера); автор не зафиксирован | кто падал при unregister на смене лока |
| `smart_terrain.clear_dead` nil | `GUARD_CLEAR_DEAD` | Discord-скрин, та же пачка (дыра в апстрим `zzzz_anthology_offline_combat_nil_fix`); автор не зафиксирован | кто падал в offline combat на `clear_dead` |
| `spawn_intercept_artifact_artifact` | `GUARD_INTERCEPT_ARTIFACT` | Discord-скрин, та же пачка (iTheon); автор не зафиксирован | у кого iTheon + этот FATAL |
| Cover Tilt / нет `demonized_randomizing_functions` | `GUARD_COVER_TILT` | Discord-скрин, та же пачка (в т.ч. кадр на Anthology **2.0**); автор не зафиксирован | у кого Cover Tilt без Ledge Grabbing |
| `iterate_objects_by_clsid` nil (Performance spawn fast) | `GUARD_SPAWN_FAST` | Discord-скрин, та же пачка; автор не зафиксирован | у кого Performance на exe без API |
| `cont_vid_mode` / битый `vid_mode` | `GUARD_VID_MODE` | Discord-скрин, та же пачка (Settings); автор не зафиксирован | кто падал в меню разрешений |

Пачка разобрана 2026-09-13 ([issue] Discord nil-FATAL пакет); карточек под эти FATAL у нас нет — только скрины.

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: ничего не пишет
- В MO2: как 1.0.0

**Проверено**

- lint: `python tools/lint_addon.py fix_nil_crash_guards`
- В игре: не прогонялось. Ожидаемый лог при всех `true`: `loaded v1.1.0` и строки `wrapped` / stub; при `false` — `skipped GUARD_…`

## [1.0.0] — 2026-09-13

**Изменено**

- `gamedata/scripts/fix_nil_crash_guards.script` — пакет monkey-patch гардов по вылетам из Discord-скринов:
  1. `item_knife.get_condition` — при `nil` возвращает `1` (иначе `bind_crow` / `bind_monster` сравнивают с числом).
  2. `task_functor.yan_ecolog_semenov_task_target` / `_1` — не индексируют `squad`, если `get_story_squad` вернул `nil`.
  3. `se_monster` / `se_stalker` `on_unregister` — вызывают `unregister_npc` только если метод есть.
  4. `smart_terrain.on_death` — вызывают `clear_dead` только если метод есть (путь offline combat / штатный nil-fix Anthology пропускал эту ошибку).
  5. `xr_effects.spawn_intercept_artifact_artifact` — `pcall`, при сбое тихий выход (iTheon).
  6. Стаб `demonized_randomizing_functions` при отсутствии Ledge Grabbing (до загрузки `weapon_cover_tilt`).
  7. `bind_stalker_ext.actor_on_net_spawn` — если нет `iterate_objects_by_clsid`, не даём FATAL от Performance fast-spawn.
  8. `reverse_resolution_list_mcm.cont_vid_mode` — пропускает битые токены разрешений.

**Причина**

Повторяющиеся `lua_pcall_failed` из отчётов игроков (август 2026): crow knife, Semenov, смена лока / химеры, offline `clear_dead`, intercept artifact, Cover Tilt без ease-библиотеки, Performance на exe без API, Settings/`vid_mode`.

**Не затронуто**

- `fix_nta_stashes`, `fix_quest_stash`, `fix_pda_buyinfo_gui` (banter — отдельно в 1.1.0), BusyHands crow patch
- Патруль `bar_zastava_dogs_*`, `Not enough IDs`, отсутствующие `.anm` / `ui_mm_save_dlg_16.xml`, `armor_ripper` без Hideout Furniture
- Оригинальные файлы сборки (полной замены нет)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: ничего не пишет, миграция не нужна
- В MO2 ниже сборки; рядом с Interactive PDA / iTheon / Weapon Cover Tilt / Performance — порядок по имени `.script` достаточный для стаба ease (`fix_*` < `weapon_cover_tilt`)

**Проверено**

- lint: `python tools/lint_addon.py fix_nil_crash_guards`
- В игре: не прогонялось. Ожидаемый лог: `[fix_nil_crash_guards] loaded v1.0.0` и строки `wrapped …` для доступных целей
