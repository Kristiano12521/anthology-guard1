# Inventory Sort Tabs Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/mod_system_fix_sort_tabs.ltx` — DLTX на `button_sort_tab_*` в `system.ltx`: вкладки 3, 6, 7, 8 переразложены под 10 кнопок Bart's New Sorting Tabs; секции 9 и 10 создаются, если их нет.

**Причина**

`ui_inventory.script` инициализирует 8 кнопок и читает `button_sort_tab_<n>` через `parse_list(ini_sys, ..., "kinds", true)`. `z_new_sorting_tabs.script` дописывает кнопки 9–10, `modxml_new_sorting_tabs.script` рисует 10 иконок с хинтами `ui_st_tab_*`. В `system.ltx` таблица всё ещё на 8 вкладок: еда+медицина вместе (вкладка 7), «медицина» по иконке получает старое «разное» (вкладка 8), для 9 и 10 секций нет.

`r_string_ex` на отсутствующей секции даёт пустую строку, `parse_list(..., true)` возвращает `{}` (truthy), запасной `{ s_all = true }` не срабатывает — вкладки 9/10 ничего не показывают.

ZIP BETA переписывал все 10 секций через `mod_system_zzzzzz_*.ltx` и ставил **разное на 9, детали/апгрейды на 0**. Это наоборот относительно иконок Bart (`ui_inGame2_btn_sort_upgrades` / `_misc`) и строк `ui_st_tab_upgrades` (9) / `ui_st_tab_misc` (10).

**Как исправлено**

Только поля `kinds` у изменившихся вкладок. 1, 2, 4, 5 не тронуты — они уже совпадают с хинтами. 9 и 10 через `@`, чтобы не дублировать базовую секцию, если BETA уже стояла. Имя файла без `zzz`: порядок — список MO2.

Итоговая раскладка (как в подсказках кнопок):

1. всё
2. оружие и взрывчатка
3. броня, шлемы, рюкзаки, навесное (`i_attach`)
4. патроны
5. артефакты и части мутантов
6. приборы, инструменты, ремонт (`i_device`, `i_tool`, `i_repair`, `i_kit`)
7. еда, напитки, мутантская пища
8. медицина
9. детали и улучшения (`i_part`, `i_upgrade`)
0. разное, документы, квест (`i_misc`, `i_letter`, `i_quest`)

**Не затронуто**

- `ui_inventory.script`, `z_new_sorting_tabs.script`, `modxml_new_sorting_tabs.script`, XML инвентаря
- `button_sort_settings.button_amount` (в скриптах сборки не читается; число кнопок задаёт Lua)
- `plugins/inventory_tabs.ltx` (нигде не подключается)
- SortingPlus `item_kind_order` / MCM — это порядок в сетке, не фильтр вкладок
- тексты `ui_st_tab_*`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим, сохраняемых структур нет
- В MO2 ниже сборки и UI. Выключить `Anthology_Sorting_Plus_Categories_Fix_v1.0.0_BETA` и убрать `mod_system_zzzzzz_anthology_sorting_plus_categories_fix.ltx`, если его клали внутрь Sorting Plus

**Проверено**

- lint: `python tools/lint_addon.py fix_sort_tabs`
- В игре: не прогонялось. Открыть инвентарь, клавиши 7 / 8 / 9 / 0: еда без аптечек, медицина отдельно, 9 — детали и киты улучшения, 0 — письма и хлам. Иконки должны совпадать с содержимым.
