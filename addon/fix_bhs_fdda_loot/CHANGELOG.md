# BHS FDDA Loot Window Fix

## [1.0.2] — 2026-08-28

Снят с раздачи. Логика живёт в BHS 0.6.4. В MO2 этот мод не ставить.

**Изменено**

- Повторный `start_body_search` при теге `body_search` больше не открывает лут (вендорский no-op). Иначе параллельно с BHS после Esc инвентарь открывался второй раз.

## [1.0.1] — 2026-08-28

Снят с раздачи: логика влита в `Anthology_BusyHands_Stability_Fix_v0_6_2`. Этот мод в MO2 не ставить параллельно с паком BHS.

**Изменено**

- `fix_bhs_fdda_loot.script` — патч ставится на `liz_fdda_redone_body_search.start_body_search` (таблица модуля), а не только на глобал. В логе `xray_nikit.log` глобал отсутствовал, из-за этого v1.0.0 не устанавливался.

**Причина**

Тот же загрузчик, что у `utils_obj.find_close_cover`: функция живёт на модуле, `_G.start_body_search` пустой.

**Проверено**

- lint: `python tools/lint_addon.py fix_bhs_fdda_loot`
- В игре: после v1.0.1 в логе должно быть `start_body_search wrapped (module liz_fdda_redone_body_search)`, затем лут трупа с включённым BHS.

## [1.0.0] — 2026-08-28

**Изменено**

- `gamedata/scripts/fix_bhs_fdda_loot.script` — monkey-patch глобальной `start_body_search`: если поиск тела уже идёт, открывает ванильное окно лута вместо повторного входа в FDDA.

**Причина**

Busy Hands Stability Fix (`zzzzzz_anthology_bhs_fdda_patch.script`) захватывает `ui_inventory.start` после обёртки FDDA. Когда idle-действие открывает лут, вызов снова попадает в `start_body_search`, а там уже висит тег `body_search` — функция выходит, окно не открывается. Без BHS вендорский FDDA зовёт свой ранний `baseUIS` (ванильный `start`) и окно открывается.

**Как исправлено**

Monkey-patch в `on_game_start` (после file-load патча BHS). Повторный вход во время активного `body_search` открывает лут тем же путём, что `ui_inventory.start` в режиме loot: `LMode_Init` / `ShowDialog`, минуя глобальный `ui_inventory.start`.

**Не затронуто**

- `liz_fdda_redone_body_search.script`
- `zzzzzz_anthology_bhs_fdda_patch.script` и остальные файлы BHS (`find_close_cover`, DotMarks-гард)
- Optimized Storage, Anomalous Stash, Sorting Tabs
- Сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим со старыми сейвами, ничего не пишет
- Конфликты: нужен FDDA Redone (есть `start_body_search`). Ставить вместе с Anthology BusyHands Stability Fix. Порядок MO2 относительно BHS не важен: BHS патчит при загрузке файла, этот мод — в `on_game_start`.

**Проверено**

- lint: `python tools/lint_addon.py fix_bhs_fdda_loot`
- В игре: с включённым BHS открыть инвентарь мёртвого NPC после анимации поиска — должно открыться окно лута, а не оборвать поиск.
