# PDA Buy Info GUI Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_pda_buyinfo_gui.script` — monkey-patch `pda_inter_x_buyinfo.add_sender` и `pda_inter_x_trade.add_trader`: на время вызова `pda_inter_gui.GUI` указывает на живое окно (`PDA_GUI`, иначе `GUI`), затем поле восстанавливается.

**Причина**

`add_sender` крутится из `actor_on_update` (`upd_find_gui`), пока `pda_msg_states[2].state == 5`. Ответ информатора может прийти уже после закрытия КПК. Оригинал в конце делает `pda_inter_gui.GUI:UpdFindLowerMenu()`.

В Anthology вкладка Interactive PDA встроена через `pda_inter_pda_tab` / `get_pda_ui()` и живёт в `PDA_GUI`. Старый `GUI` создаётся только `start_PDAX()` (отдельное окно) и при встроенной вкладке остаётся `nil`. Отсюда:

`pda_inter_x_buyinfo.script:278: attempt to index field 'GUI' (a nil value)`

Отправитель к этому моменту уже записан в `Find_available_messages`, но обращение к `GUI` валит Lua.

ZIP v1.0.0 BETA подменял весь `pda_inter_x_buyinfo.script` (старый синхронный обход 65534 id). Если в `[GAM] Interactive PDA` уже лежит версия с покадровым сканом (OPT1), ZIP её откатывает.

**Как исправлено**

Callback не подходит: обновление GUI — прямой вызов из `add_sender` / `add_trader`, не script callback. Monkey-patch:

- Если `GUI == nil`, на время оригинала подставляется `PDA_GUI` (встроенная вкладка) либо no-op, чтобы последняя строка не индексировала `nil`.
- `pcall` вокруг оригинала: другой сбой не становится FATAL, повтор одной причины в лог один раз за сеанс.
- Тот же приём на `add_trader`: торговые офферы тоже идут из `actor_on_update` и бьют в `GUI:UpdTradeLowerMenu()`.

**Не затронуто**

- файлы `[GAM] Interactive PDA` (нет полной замены)
- логика поиска отправителей, цены, ложь, новости
- покадровый скан ALife, если он уже стоит в Interactive PDA
- `pda_inter_x_banter` / `pda_inter_x_raid` / `pda_inter_x_tasks` (у tasks уже есть `GUI or PDA_GUI`)
- `all.spawn`, сейвы, MCM

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Зависимость: `[GAM] Interactive PDA`. Без него — no-op
- В MO2 ниже `[GAM] Interactive PDA`
- ZIP `Anthology_PDA_Buy_Info_GUI_Fix_v1.0.0_BETA` выключить. Если его файл влили внутрь Interactive PDA — вернуть оригинальный `pda_inter_x_buyinfo.script`

**Проверено**

- lint: `python tools/lint_addon.py fix_pda_buyinfo_gui`
- В игре: не прогонялось. Ожидаемый лог: `[fix_pda_buyinfo_gui] loaded v1.0.0 wrapped=2 missing=0`. Запрос информации → закрыть КПК → дождаться типса → открыть вкладку без `attempt to index field 'GUI'`
