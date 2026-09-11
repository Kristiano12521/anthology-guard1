# Misc Script Error Fixes

## [1.0.3] — 2026-09-11

**Изменено**

- `gamedata/scripts/fix_misc_script_errors.script` — nil-гард на `mas_scope_detach` `ActorMenu_on_item_after_move` (`move`): при `obj == nil` выход без `obj:section()`. Перехват при `RegisterScriptCallback` в обёртке `on_game_start`; late-path через `debug.getupvalue` → `axr_main` `intercepts`, если колбэк уже был зарегистрирован.

**Причина**

Лут больших стаков из тайника (`Action_Move_All`) шлёт `ActorMenu_on_item_after_move` с `obj=nil` (child id уже снят, `CheckItem` падает). Локальный `move` при `mode == "loot"` сразу делает `obj:section()` → FATAL `lua_pcall_failed` на `mas_scope_detach.script:16`. Тот же класс, что `fix_arti_frames_nil` / `fix_dynamic_armor_visuals_nil`.

**Не затронуто**

- Оригинал `mas_scope_detach.script`, drag/drop, `detach()`
- `ui_inventory.script`, `ish_fast_transfer`
- Гард `actor_on_item_use`, tutorial `guard_key`

**Проверка**

- lint: `python tools/lint_addon.py fix_misc_script_errors`
- В игре: не подтверждено. Репро: take-all крупных стаков деталей патронов из тайника — без FATAL на `mas_scope_detach.script:16`; в логе при срабатывании `skip nil obj after_move`.

## [1.0.2] — 2026-09-02

**Изменено**

- `install_mas(true)` на `on_game_start`: ранний «not found» не пишется, если MAS ещё не загрузился; отказ логируется на `actor_on_first_update`, если обёртка так и не встала.

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; `printf` с причиной при раннем выходе из `install_mas()`.

**Не затронуто**

- Патч MAS, modxml tutorial hooks.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_misc_script_errors.script` — monkey-patch `mas_scope_detach.on_game_start`.
- `gamedata/scripts/modxml_fix_tutorial_hooks.script` — DXML-гард `getText` на `ui\game_tutorials.xml`.

**Причина**

ZIP `Anthology_Misc_Script_Error_Fixes_v1.0.0_BETA` подменял три чужих скрипта целиком.

1. `mas_scope_detach.on_game_start` регистрирует `actor_on_item_use`, функции нет. Лог: `trying to set callback actor_on_item_use to nil function` (`mas_scope_detach.script:106`). Отсоединение прицела идёт через drag/drop и after_move.

2. `modxml_tutorial_hooks` зовёт `getText` на пустых `<guard_key/>`. `dxml_core.getText` пишет `element <guard_key doesnt have children`. Автор hooks просит не править его файл.

3. AOL в ZIP заменён на медленный `ini_file("system.ltx")`. В Standard уже побеждает `Anthology_Performance_MO2_merged` (гард + `system_ini` + native filter). Подмена откатила бы этот файл.

**Как исправлено**

- MAS: до вызова оригинала подставляется no-op `actor_on_item_use`, сразу после — `UnregisterScriptCallback`. Глобальный `RegisterScriptCallback` не трогается (`dxml_core` его уже оборачивает).
- Tutorial: `modxml_fix_tutorial_hooks` регистрируется раньше `modxml_tutorial_hooks` и на `ui\game_tutorials.xml` оборачивает `xml_obj.getText`. Узел без текстового ребёнка → `nil`, без parser error. `<guard_key>use</guard_key>` без изменений.
- AOL: не трогаем.

Оригиналы не подменяются.

**Не затронуто**

- `mas_scope_detach.script`, drag/drop, `detach()`
- `aol_anim_transitions.script`, HUD `ts_*`, Performance merged
- `modxml_tutorial_hooks.script`, `monitors`, тексты подсказок
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 ниже RAK 3DSS и Interaction Dot Marks. Не конфликтует с `Anthology_Performance_MO2_merged`
- ZIP `Anthology_Misc_Script_Error_Fixes_v1.0.0_BETA` выключить: он заменяет три файла, в том числе AOL у Performance merged
- `on_xml_read` в `modxml_fix_tutorial_hooks` намеренно не снимается: иначе после выхода в меню гард окажется после hooks

**Проверено**

- lint: `python tools/lint_addon.py fix_misc_script_errors`
- В игре: не прогонялось. Ожидаемый лог: `wrapped mas_scope_detach.on_game_start`; при Dot Marks — `wrapped getText for ui\game_tutorials.xml`. Не должно быть `actor_on_item_use to nil function` и `element <guard_key doesnt have children`. `[AOLTransitionGuard] skipped 6` от Performance merged — норма.
