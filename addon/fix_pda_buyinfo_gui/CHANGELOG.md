# PDA Buy Info GUI Fix

## [1.1.3] — 2026-09-19

**Изменено**

- Monkey-patch re-wrap: больше не обнуляет `orig_*` перед `install()` на `actor_on_first_update`.
- `wraps_ok` требует живой `orig`; вызовы оригинала под nil-guard.

**Причина**

Обнуление всех `orig` при частичном сбое wrap оставляло уже наш патч с `orig == nil` → CTD (как `fix_sim_mechanic_trade` / xray_korisnik).

**Не затронуто**

- Игровая логика патча, сейвы, DLTX

**Проверено**

- lint: `python tools/lint_addon.py fix_pda_buyinfo_gui`
- в игре: не прогонялось

## [1.1.2] — 2026-09-17

**Изменено**

- `fix_pda_buyinfo_gui.script` — `wraps_ok` по слотам buyinfo/trade/banter; на `actor_on_first_update` переустанавливает wrap после MT reload; uninstall только если указатель ещё наш; always re-capture orig.

**Причина**

1.1.1 при `installed=true` не сверял указатели. После MT reload снова FATAL `GUI` на trade/banter.

**Не затронуто**

- with_live_gui / CTE unpack / noop

**Проверено**

- lint: `python tools/lint_addon.py fix_pda_buyinfo_gui`
- в игре: не прогонялось

## [1.1.1] — 2026-09-13

**Изменено**

- `with_cte_gui_guard`: аргументы CTE-колбэка пакуются в `{...}` / `unpack` перед входом во вложенную `function()` — иначе LuaJIT: `cannot use '...' outside a vararg function` на строке обёртки, скрипт не грузится.

**Причина**

Лог `xray_nikit`: `Failed to load script fix_pda_buyinfo_gui` (оба захода сессии).

**Не затронуто**

- Логика banter / buyinfo / trade; сейвы.

**Проверено**

- `lint_addon.py`
- В игре: не прогонялось (ожидание: presence `loaded v1.1.1`, без `Failed to load script`)

## [1.1.0] — 2026-09-13

**Изменено**

- Обёртки `pda_inter_x_banter.send_sos` / `ask_surge` / `ask_psi_storm` / `ask_status`: на время вызова `GUI` → живое окно (`PDA_GUI` / noop); колбэки `CreateTimeEvent` (сброс кулдауна кнопок) тоже идут через тот же bind.
- `noop_gui.UpdBanterButtons`; `with_live_gui` возвращает результаты `pcall` (нужно для CTE `return true`).

**Причина**

`pda_inter_x_banter.script:170` (и соседние `UpdBanterButtons`): `attempt to index field 'GUI' (a nil value)` на встроенной вкладке Interactive PDA — тот же класс, что buyinfo/trade. Срабатывает и сразу в `ask_*`, и из отложенного `reset_cd`.

**Не затронуто**

- `pda_inter_x_raid`; файлы Interactive PDA без полной замены
- Логика SOS / выброс / пси / статус

**Совместимость**

- Как 1.0.x; в MO2 ниже `[GAM] Interactive PDA`

**Проверено**

- lint: `python tools/lint_addon.py fix_pda_buyinfo_gui`
- В игре: не прогонялось. Ожидание: banter-кнопка → закрыть КПК до конца кулдауна → без FATAL на `GUI`

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке.

**Не затронуто**

- Обёртки Interactive PDA, `install()`.

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
