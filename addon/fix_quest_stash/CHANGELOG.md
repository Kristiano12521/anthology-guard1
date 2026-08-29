# Quest Stash Type Migration Fix

## [1.0.1] — 2026-08-30

**Изменено**

- `gamedata/configs/items/items/mod_items_quest_fix_quest_stash.ltx` — DLTX `@[drx_sl_quest_item_1001]`–`1038`: создать секции, если их затёр чужой полный `items_quest.ltx`.

**Причина**

`[QUE] wtf 4_2` кладёт свой `items_quest.ltx` только со слотами 1–3. Сейв хранит `drx_sl_quest_item_1014` / `1023`, движок пишет `Can't create entity`, миграция не может восстановить КПК, `bar_npc_dolg_svayzist_task_4` срывается на загрузке.

**Как исправлено**

Те же поля, что в Anthology `items_quest.ltx`, оператор `@` — не падает, если база уже есть. Скрипт миграции не менялся.

**Не затронуто**

- `fix_quest_stash.script`, `mod_treasure_manager_fix_quest_stash.ltx`
- общие слоты 1–3, `tasks_stash.script`, `get_random_stash`, `all.spawn`

**Совместимость**

- Сейвы: новая игра не нужна. Грузить слот **до** провала, не сейв после `DRX SL task ended`
- В MO2 ниже сборки и `[QUE] wtf 4_2`

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_stash`
- В игре: не прогонялось. Ожидаемый лог: нет `Can't create entity 'drx_sl_quest_item_1014'`, нет `cannot recover ... section missing`

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_quest_stash.script` — одноразовая миграция `save_var.stash_type` активного stash-задания на тип из текущего `on_job_descr`; переписывает pending-строку `treasure_manager.caches`; обёртка `task_status_functor.drx_sl_quest_item_task_status` принимает старый КПК и конвертирует его. Если кэш уже потрачен и предмета нет — спавн актуальной секции игроку.
- `gamedata/configs/items/settings/mod_treasure_manager_fix_quest_stash.ltx` — DLTX: `val_q7_n` в `[blacklist_stashes_names]`.

**Причина**

Anthology развела общие DRX-слоты 1–7 на уникальные `1001–1038` в LTX (`bar_npc_dolg_svayzist_task_4`: было `6`, стало `1014`). Сейв хранит старый `stash_type`. `tasks_stash.script` собирает секцию как `"drx_sl_quest_item_" .. typ`, статус-функтор ищет не тот КПК, `stage` остаётся 0, метка на тайнике, диалог сдачи не появляется.

ZIP v1.4 копировал 38 секций, которые уже есть в `items_quest.ltx`, оборачивал `get_random_stash` (имена уже в чёрном списке, кроме `val_q7_n`), крутил `actor_on_update` 60 с, ставил `zzzz`-скрипт и уничтожал общие предметы 1–3, которые ванильные задания всё ещё используют.

**Как исправлено**

Актуальный тип читается из `task_manager.task_ini` (`drx_sl_create_quest_stash(id:TYPE)`), а не из зашитой карты 37 заданий. Состояние сейва приводится к текущему LTX, чтобы ванильный функтор и Tosox marker-fix работали без подмены. Общие предметы 1–3 не удаляются, если другое активное задание их ещё держит. Плохие ящики — DLTX в штатный blacklist, без monkey-patch селектора.

**Не затронуто**

- `items_quest.ltx`, секции `drx_sl_quest_item_1001`–`1038` (уже в сборке)
- `treasure_manager.get_random_stash`, `tasks_stash.script` целиком
- ванильные stash-задания со слотами 1–3 (Петренко и др.)
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: миграция `stash_type` и инфопорции `*_started` у активных remap-заданий. Поле `stash_type_legacy` добавляется в существующую таблицу `save_var`. Новая игра не нужна
- Конфликты: нет пересечения файлов с ZIP v1.4 (`items_zz_*`, `zzzz_anthology_quest_stash_fix.script`). В MO2 ниже сборки; ZIP и `[DBG] Kristiano Fixes ALL IN ONE` с тем же `zzzz_anthology_quest_stash_fix.script` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_stash`
- В игре: не прогонялось. Связист Ростка `bar_npc_dolg_svayzist_task_4`: лог `migrated task=... stash_type=6->1014`, метка на квестодателе, в диалоге сдача. Предмет `drx_sl_quest_item_1014` в инвентаре
