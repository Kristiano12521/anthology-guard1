# fix_taskboard_sync

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; рядом с `[ANTHFIX] Taskboard + Weather`.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сохранённые `save_var` офферов до сдачи задания / смены уровня - плюс.

## [1.0.3] - 2026-09-20

**Изменено**

- `pda_taskboard.accept_task` — обёртка: `give_task` под `pcall` **без** окна `currently_processed_npc_id`. При ошибке — лог + `level.enable_input()`.

**Причина**

Клик по заданию в Объявлении = `OnTaskClicked` → `accept_task`. Сток выставляет `currently_processed_npc_id` вокруг `give_task`; `z_taskboard_overrides` тогда делает `is_talking() == true`. Если `give_task` падает или не доходит до сброса id — ввод мёртв («нажал на задание — зависло»). В логах nikit 20.09: открытие доски есть, `CRandomTask:give_task()` printf нет (буфер / обрыв до flush или путь без ванильного printf).

**Не затронуто**

- reuse офферов, remap stash→fetch, prepare_category

**Остаточный риск**

Редкий accept без заранее сохранённого `save_var`, где `on_init` жёстко требует живого `get_speaker` — на доске офферы уже подготовлены. Если softlock останется при `accept begin` без `accept done` — висеть внутри `give_task`, не в `is_talking`.

**Проверено**

- lint: `python tools/lint_addon.py fix_taskboard_sync`
- в игре: не прогонялось (`verified_*` не ставились)

## [1.0.2] - 2026-09-20

**Изменено**

- `gamedata/scripts/z_fix_taskboard_sync.script` → `fix_taskboard_sync.script` (префикс `z_` снят); убран `-- load-order`.

**Причина**

Патч ставится в `on_game_start` / `actor_on_first_update` — к событию все скрипты уже загружены, алфавитное место не нужно.

**Не затронуто**

- Логика reuse / сортировки / remap stash→fetch

**Проверено**

- lint / unittest / build_addon: см. прогон после правки
- в игре: не прогонялось (`verified_*` не ставились; переименование меняет момент install)

## [1.0.1] - 2026-09-20

**Изменено**

- schedule_talk: вызывает z_taskboard_overrides.CreateTimeEventOverride, а не глобальный CreateTimeEvent.

**Причина**

При reuse assault/bounty/stash/fetch/delivery CreateTimeEvent шёл из окружения sync-скрипта и не попадал в steal z_taskboard_overrides во время prepare_category. give_talk_message2 не захватывался — на доске «Объявление» пустые иконки (шум) и нет title/локации. Лог: reuse assault ... без ошибок guard.

**Не затронуто**

- Логика reuse save_var, сортировка available_tasks, remap stash→fetch
- fix_wtf_taskboard_guard

**Совместимость**

- Как 1.0.0; нужен iTheon/ANTHFIX Taskboard (z_taskboard_overrides)
- Сейвы: без изменений

**Проверено**

- lint: python tools/lint_addon.py fix_taskboard_sync
- в игре: не прогонялось. Ожидание: категория штурм/мутанты — иконка, title, вид/группировка, местонахождение как без sync

## [1.0.0] - 2026-09-20

**Изменено**

- gamedata/scripts/z_fix_taskboard_sync.script - monkey-patch:
  - reuse save_var в setup_bounty_task, drx_sl_create_quest_stash, fetch-setup, on_init_delivery_task, setup_assault_task / validate_assault_task;
  - сортировка available_tasks по task_id после generate_available_tasks;
  - категория drx_sl_create_quest_stash -> setup_fetch_task на доске.

**Причина**

Доска и диалог вызывают setup независимо и дают разные цели/предметы между оффером. pairs(CFG_CACHE) делает порядок слотов недетерминированным. Stash-задания на доске попадали в bounty из-за normalizer.

**Как исправлено**

Один оффер — переиспользование actor save_var (переживает MT reload; очистка непринятых on_before_level_changing, как ваниль на уровне). Память bounty_cache / DIALOG_ID / cache_stash между двумя вызовами setup не требуется.

**Не затронуто**

- Сами тексты LTX, repeat_timeout, balance level_mode assault (фаза B).
- Принятие/сдача заданий (фаза C).
- Dominance->assault remapping на доске.

**Совместимость**

- Сейвы: без миграции; старые save_var не мешают.
- MO2 ниже Taskboard; после MT reload wraps переустанавливаются на actor_on_first_update.

**Проверено**

- lint: python tools/lint_addon.py fix_taskboard_sync
- в игре: не прогонялось. Ожидание: один bounty — одна цель на доске и в диалоге; stash-категория в «Сбор предметов».
