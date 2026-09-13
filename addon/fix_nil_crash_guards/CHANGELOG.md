# Nil Crash Guards

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
