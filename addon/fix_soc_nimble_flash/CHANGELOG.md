# SoC Nimble Flash Dialog Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/escape/space_restrictor_soc/mod_trader_zone_task_fix_soc_nimble_flash.ltx` — DLTX на `[sr_idle]`: после интро restrictor снова доходит до `@has_item` и выдаёт `actor_has_item_flash`.
- `gamedata/scripts/fix_soc_nimble_flash.script` — одноразовый `CreateTimeEvent` чинит сейв, где флешка уже есть, а инфопорции нет.

**Причина**

Задание `esc_flash_task` смотрит на предмет `esc_wounded_flash`, стартовый диалог Сидоровича — на `+actor_has_item_flash`. Флаг выдаёт только `trader_zone_task.ltx` в состоянии `[sr_idle@has_item]`. Переход туда требует `-esc_kill_gunslinger`; после интро флаг уже стоит, и если схема откатилась на `[sr_idle]` или restrictor поднялся поздно, переход больше не срабатывает. PDA пишет «вернуть флешку», Сидорович продолжает требовать найти Шустрого.

ZIP v1.0.1 крутил `actor_on_update` и ставил `zzzzzz_*.script`. Сам диалог и награду не трогал — это верно, но причину в автомате restrictor не чинил.

**Как исправлено**

DLTX добавляет запасной переход: при `+esc_kill_gunslinger` схема идёт в `@has_item`, а если флешка уже в инвентаре — сразу выдаёт инфопорцию. Штатный диалог Сидоровича забирает флешку, платит 3500 и закрывает квест. Сейв, где restrictor уже в `nil` или оффлайн, чинится одним `CreateTimeEvent` после загрузки. `actor_on_update` нет.

**Не затронуто**

- `dialogs_soc_escape.script`, XML диалогов, `tm_soc_escape.ltx`
- выдача флешки Шустрым, сумма награды, `esc_serious_talk` / `tutorial_end`
- интро `intro_kill` / `esc_kill_gunslinger`
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Повреждённый сейв чинится при загрузке за 1–8 с
- Конфликты: нет пересечения файлов с ZIP v1.0.x (тот ставил `zzzzzz_anthology_soc_nimble_flash_dialog_fix.script`). В MO2 ниже сборки; ZIP v1.0.x выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_soc_nimble_flash`
- В игре: не прогонялось. Повреждённый сейв: в логе `RECOVERY -> +actor_has_item_flash`, у Сидоровича появляется сдача флешки. Новое прохождение SoC: после получения флешки диалог сдачи доступен без зависания на «найди Шустрого».
