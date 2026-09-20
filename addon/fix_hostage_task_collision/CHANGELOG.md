# Fix Hostage Task Collision

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 после WTF / Taskboard (wrap ставится на уже подменённый `give_task`).

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.1] — 2026-09-20

**Изменено**

- Late-reinstall `give_task` / `setup_companion_task`: `orig` захватывается один раз; reclaim outer без `orig = {}` (цикл с `fix_drx_enemy_task_gate` → softlock Объявления).
- `printf wrapped:` только при первом захвате или реальном reclaim (не на каждом `actor_on_first_update`).

**Причина**

Diag 1.0.3: next-hop `fix_drx_enemy_task_gate:177`, hang без `after`. DRX после hostage делал `orig = hostage`, hostage.orig оставался DRX → взаимный tail-call.

**Не затронуто**

- Логика блокировки второго hostage

## [1.0.0] — 2026-09-05

**Изменено**

- `gamedata/scripts/fix_hostage_task_collision.script` — monkey-patch `CRandomTask.give_task` и `xr_effects.setup_companion_task`.

**Причина**

Все hostage-квесты (сим `simulation_task_26+`, Волк `esc_2_12_stalker_wolf_task_2`, JTDR `*b` и др.) делят один слот `hostage_companion_task_1`. Precondition уже запрещает второй активный hostage, но `give_task` его не перепроверяет. С таскборда можно принять два задания подряд на одну точку: второй `setup_companion_task` спавнит отряд с тем же story_id; сдача одного валит второе (−репутация) и оставляет сироту-компаньона.

Лог `xray_nikit` 04.09.2026: `give_task` wolf_task_2 и simulation_task_26 за 316 мс → `Multiple objects trying to use same story_id hostage_companion_task_1` → оба closed в одну секунду.

**Как исправлено**

Monkey-patch (DLTX не закрывает дыру на accept):

- `give_task`: для заданий со слотом `hostage_companion_task_1` повторно вызывает `has_completed_task_prerequisites`; при `false` — отказ и запись в лог.
- `setup_companion_task`: если hostage-слот уже занят (info / story squad / squad_exist) — не спавнить второй отряд.
- Установка в `on_game_start`, повтор в `actor_on_first_update` (MT). Снятие в `on_game_end`.

**Не затронуто**

- LTX наград, текстов, story_id, JTDR-секции
- одиночный hostage-квест (взял → спас → сдал)
- не-hostage задания
- уже залипший компаньон в старом сейве (отпустить вручную)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 после WTF / Taskboard (wrap ставится на уже подменённый `give_task`)

**Проверено**

- lint: `python tools/lint_addon.py fix_hostage_task_collision`
- в игре 2026-09-20 (cycle-fix 1.0.1 + sync): 13× accept begin → give_task → accept done; FATAL нет → `verified_*` в `meta.ini`
