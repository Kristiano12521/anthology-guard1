# Fix DRX SL Meet Loop

## [1.0.1] — 2026-09-14

**Изменено**

- Правка `drx_sl_honchos_table`: второй ряд `cit_killers_merc_mechanic_stalker` (комментарий Vector) → `zat_stancia_trader_merc`.
- Выбор следующего хончо предпочитает ту же фракцию, что у текущего.
- Перед выдачей нового meet снимается залипший meet текущего.

**Причина**

Диалог `default_task` обещает следующего контакта, но ванильная таблица дублирует Кабана вместо Вектора (`zat_stancia_trader_merc`). После Грифона у наёмника часто пустой список кандидатов — 1.0.0 только рвал self-meet без новой метки.

**Не затронуто**

- запрет self-meet при реально пустом списке
- LTX заданий, `fix_grifon_visibility`

**Проверено**

- lint: `python tools/lint_addon.py fix_drx_sl_meet_loop`
- В игре: не прогонялось

## [1.0.0] — 2026-09-14

**Изменено**

- `gamedata/scripts/fix_drx_sl_meet_loop.script` — monkey-patch `xr_effects.drx_sl_meet_random_honcho`.

**Причина**

После исчерпания storyline-заданий хончо (пример: Грифон `merc_pri_grifon_mlr`) диалог выдаёт `*_default_task` с `condlist_0 = {-drx_sl_dummy_info} complete`. Задание мгновенно завершается и зовёт `drx_sl_meet_random_honcho()`. Если других валидных хончо нет, ваниль оставляет `drx_sl_current_honcho` и снова выдаёт `*_meet_task_1` на того же NPC. Meet часто ещё `inprocess` → `TASK ALREADY EXISTS` / `already inprocess`. PDA залипает на «Встретиться с …», диалог мигает «Получить следующее задание» (новая + выполнена).

Логи `xray_mg9000` / `xray_nikit` 14.09.2026: цикл `default_task` → `meet_task_1` → `already inprocess` на `drx_sl_merc_pri_grifon_mlr_*`.

**Как исправлено**

- при пустом списке кандидатов — не выдавать self-meet; снять залипший `drx_sl_meet_honcho_<current>` и `set_task_completed` на активные meet этого хончо;
- перед `give_task` отфильтровать уже активные meet-секции;
- счётчик `drx_sl_current_task_number` увеличивается только при реальной выдаче meet.

**Не затронуто**

- LTX заданий Грифона (`task_1` / `task_2` / тексты)
- `fix_grifon_visibility` (remark / cover)
- таблица `drx_sl_honchos_table` (в т.ч. дубль Vector/Hog)
- `all.spawn`, диалоговые XML

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции; при следующем вызове meet_random_honcho (диалог / сдача) цикл обрывается и meet текущего чистится
- В MO2 после сборки / WTF (wrap на уже загруженный `xr_effects`)

**Проверено**

- lint: `python tools/lint_addon.py fix_drx_sl_meet_loop`
- В игре: не прогонялось. Ожидаемый лог: `wrapped: drx_sl_meet_random_honcho`; при обрыве — `no valid next honcho ... skip self-meet loop`
