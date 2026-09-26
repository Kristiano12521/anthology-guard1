# DotMarks InteractPrompt InitStatic Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; после Interaction Dot Marks / Catspaw utils (`-- load-order` в шапке).

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.1] — 2026-09-26

**Изменено**

- `InteractPrompt` берётся с `ui_hud_dotmarks.InteractPrompt`, если там есть `on_option_change`, иначе с глобального `InteractPrompt`.

**Причина**

Лог mg9000 2026-09-26: `setup_pri/sec` находились, а `InteractPrompt.on_option_change not found`. Метод объявлен как `class "InteractPrompt"` в `ui_hud_dotmarks.script:2854` и может лежать на `_G`, а не полем таблицы скрипта.

**Не затронуто**

- Обёртки `get_xml_cache` и `setup_pri/sec_interact_prompt`, сейвы

**Проверено**

- `tools/lint_addon.py fix_dotmarks_interact_prompt`
- В игре ещё нет

## [1.0.0] — 2026-09-18

**Изменено**

- `gamedata/scripts/fix_dotmarks_interact_prompt.script` — monkey-patch:
  - `utils_catspaw_common.get_xml_cache` (свой кэш, можно сбросить);
  - `ui_hud_dotmarks.setup_pri_interact_prompt` / `setup_sec_interact_prompt`;
  - `InteractPrompt.on_option_change`.
  При ошибке InitStatic/BuildUI: log → bust cache → один retry → иначе skip prompt (`destroyed`), без CTD.

**Причина**

Лог `xray_mg9000`: `tutorial_campfire_extinguish` → `InteractPrompt:BuildUI` → `InitStatic("alt_interact")` → BusyHands Runtime Error → tempsave → native crash `ScreenResolutionChanged`. Узел `alt_interact` в стоковом `ui_dotmarks.xml` есть; падение на рантайм-документе/кэше XML.

**Не затронуто**

- `message_box_21` / ultrawide Lua fatal window
- `fix_dotmarks_dropped_weapon`
- Логика маркеров/туториалов Dot Marks кроме soft-fail prompt UI
- Сейвы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- MO2: после Interaction Dot Marks / Catspaw utils (`-- load-order` в шапке)

**Проверено**

- lint: см. ответ агента
- в игре: не прогонялось. Репро: подойти к костру до туториала extinguish — без CTD; при срабатывании guard в логе `bust xml cache` / `skipped`.
