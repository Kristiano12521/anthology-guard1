# Trader Restock Callback Fix

## [1.0.1] — 2026-08-31

**Изменено**

- `gamedata/scripts/aaa_fix_trader_restock_callback.script` — в `on_game_start` chain-wrap `trader_autoinject.timed_update` на таблице модуля. После оригинала шлёт `SendScriptCallback("trader_on_restock", npc)`, если оригинал сам это не сделал. `AddScriptCallback` на верхнем уровне — как в 1.0.0.

**Причина**

Campfires вырезает и объявление, и отправку. 1.0.0 чинил только intercept: подписки вставали, событие при активном Campfires уходило только если патч BHS реально подменил `timed_update`. Без отправителя бартер не обновляет пул, `exo_loot.spawn_psus` не кладёт батареи.

**Как исправлено**

Monkey-patch `trader_autoinject.timed_update` (не глобал). Обёртка вызывает оригинал, затем шлёт событие. Предохранитель от двойного Send: на время `orig()` вешается `axr_main.make_callback` — это диспетчер `SendScriptCallback` (`_g.script:112` → `axr_main.script:280`). Ваниль (`trader_autoinject.script:66`) и BHS (`zzzzzz_anthology_bhs_trader_autoinject_patch` ~183) зовут `SendScriptCallback` внутри `timed_update`; Campfires — нет. Если `make_callback("trader_on_restock")` уже прошёл, свой Send не дублируем: иначе `exo_loot.spawn_psus` отработает дважды за тик, `alife_create_item` ещё не в инвентаре, `check_existing` не увидит первую пачку и насыпет лишних батарей.

Диагностика не по стенным часам: один `printf`, если обёртка `timed_update` сработала хотя бы раз за заход, а наш подписчик события ничего не получил. На старте отдельной строкой: встала ли обёртка Send. Если модуля или `timed_update` нет — не падаем, пишем в лог и выходим.

**Вторая дыра (не чиним)**

Патч BHS `zzzzzz_anthology_bhs_trader_autoinject_patch` не загружается вовсе: marker читается с собственного модуля `zzzzzz_anthology_bhs_trader_autoinject_patch`, а не из `trader_autoinject.script`. Это отдельная проблема BHS, этот фикс её не трогает.

**Не затронуто**

- файлы `trader_autoinject.script`, Campfires, BHS, `barter_core.script`, `exo_loot.script`
- ассортимент, цены, крафт Exo System (кроме доставки события рестока)
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Зависимостей нет. В MO2 не требует слота относительно Campfires/BHS: обёртка ставится в `on_game_start` после top-level патча BHS

**Проверено**

- lint: `python tools/lint_addon.py fix_trader_restock_callback` — ошибок нет, VERIFY-001 (в игре не прогонялось)
- `--cross`: CROSS-001 на этот мод нет
- В игре: не прогонялось. Нужно дождаться рестока у торговца и проверить ассортимент (бартер / батареи), не только отсутствие traceback. Ожидаемый лог старта: `Send wrap installed`. Не должно быть `wrap ran but subscriber got nothing` после того, как `timed_update` реально отработал.

## [1.0.0] — 2026-08-31

**Изменено**

- `gamedata/scripts/aaa_fix_trader_restock_callback.script` — на верхнем уровне файла объявляет `trader_on_restock` через `AddScriptCallback`. Имя `aaa_*` грузится раньше `barter_core.script` и `exo_loot.script`. Если intercept уже есть, повторный `Add` не вызывается как ошибка.

**Причина**

`trader_on_restock` — динамический callback: ванильный `trader_autoinject.script:205` объявляет его на верхнем уровне. В сборке файл перекрыт `[FIX] Campfires Anthology Compat v2`, где `AddScriptCallback` вырезан. `barter_core` (`[HARD] Anthology_barter`) и `exo_loot` (`[BS] Exo System`) регистрируются на имя, которого нет: `callback trader_on_restock doesn't exist!`. Подписки не встают.

Патч BHS (`zzzzzz_anthology_bhs_trader_autoinject_patch.script`) тоже делает `AddScriptCallback`, но с префиксом `zzzzzz_` позже `on_game_start` этих двух модов.

**Как исправлено**

`axr_main.on_game_start` обходит `$game_scripts$` через `file_list_open_ex` без своей сортировки — порядок задаёт имя файла. Скрипт `aaa_*` выполняется до `barter_core` / `exo_loot` и создаёт intercept до их `RegisterScriptCallback`.

`callback_add` на уже существующем имени пишет `already exists!` и `callstack()`, таблицу не затирает. Повторный `Add` глотается, чтобы не шуметь, если Campfires снят (ваниль объявила сама) или BHS успел раньше.

`SendScriptCallback` не вызывается.

**Риск**

Campfires вырезает и отправку: в его `trader_autoinject.timed_update` нет `SendScriptCallback("trader_on_restock")`. Тогда intercept есть, подписки встают, а событие шлёт только патч BHS (`zzzzzz_anthology_bhs_trader_autoinject_patch.timed_update`). Других отправителей в сборке нет: ванильный `trader_autoinject.script:66` перекрыт Campfires; Ammo Maker подписку закомментировал. Без BHS ресток бартера и батарей на прилавках по-прежнему не сработает, хотя traceback на старте пропадёт.

**Не затронуто**

- `trader_autoinject.script`, Campfires, BHS, `barter_core.script`, `exo_loot.script`
- ассортимент, цены, крафт Exo System
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Зависимостей нет. BHS по-прежнему нужен, чтобы событие реально ушло при активном Campfires

**Проверено**

- lint: `python tools/lint_addon.py fix_trader_restock_callback` — ошибок нет, ORDER-002 снят комментарием `-- load-order:`
- `--cross`: CROSS-001 на этот мод нет
- В игре: не прогонялось. Ожидаемый лог: `[fix_trader_restock_callback] trader_on_restock added v1.0.0` (или `exists`, если intercept уже был). Не должно быть `callback trader_on_restock doesn't exist!` из `barter_core.script:718` и `exo_loot.script:185`
