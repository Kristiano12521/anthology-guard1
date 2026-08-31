# Loot Space Take-All Fix

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке.

**Не затронуто**

- Обёртки OnKeyboard, `install()`.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_loot_space.script` — monkey-patch `UIMutantLoot:OnKeyboard` и `UIInventory:OnKeyboard`.
- `gamedata/configs/text/rus|eng/ui_st_inventory_fix_loot_space.xml` — подсказка `ui_st_take_all_hint` упоминает пробел.

**Причина**

ZIP `Anthology_Mutant_Loot_Space_Key_Fix_v1.0.0_BETA` чинил только разделку мутантов: кнопка пишет «Взять всё (ENTER/ПРОБЕЛ)», а `ui_mutant_loot.script` проверяет лишь `DIK_RETURN`. Патч ставил `zzzz`-имя, вешался при разборе файла и не снимал обёртку.

В окне лута трупа/тайника «Взять всё» — `SHIFT + T` на отпускании клавиши (`UIInventory:OnKeyboard`, режим `"loot"`). Пробел там не обрабатывается.

**Как исправлено**

Monkey-patch в `on_game_start`, оригинал возвращается в `on_game_end`. Имя файла без `zzz`: порядок — список MO2.

- Разделка: `DIK_SPACE` передаётся оригиналу как `DIK_RETURN`. Механика добычи не трогается.
- Лут: в `mode == "loot"` на нажатии пробела вызывается текущий `LMode_TakeAll` (включая версию Hideout Furniture, если она подменила метод). Событие съедается, чтобы движок не нажал сфокусированную кнопку. `SHIFT + T` и `SHIFT + P` без изменений. Инвентарь / торговля / ремонт не патчатся.

**Не затронуто**

- `ui_mutant_loot.script`, `ui_inventory.script` как файлы
- состав лута, `FillList` / `Loot`, анимации разделки
- `LMode_PutAll`, сортировочные вкладки (`z_new_sorting_tabs` по-прежнему в цепочке `OnKeyboard`)
- `UICompanionInv` (в Anthology компаньоны идут через `UIInventory` loot)
- сохраняемые таблицы (своего `save_state` нет)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 ниже сборки. ZIP `Anthology_Mutant_Loot_Space_Key_Fix` выключить. Если `zzzzzz_anthology_mutant_loot_space_key_fix.script` лежит внутри другого мода (FDDA / Kristiano) — убрать и его

**Проверено**

- lint: `python tools/lint_addon.py fix_loot_space`
- В игре: не прогонялось. Разделка мутанта: пробел = взять всё, как Enter. Труп/тайник: пробел = взять всё, Shift+T по-прежнему работает. Свой инвентарь: пробел ничего не забирает
