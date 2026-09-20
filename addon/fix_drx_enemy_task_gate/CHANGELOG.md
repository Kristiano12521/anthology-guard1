# fix_drx_enemy_task_gate

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается.

## [1.0.1] — 2026-09-20

**Изменено**

- `drx_sl_is_enemy` смотрит текущую `character_community` (маскировка комбезом), а не `get_actor_true_community` (истинная фракция).
- Оффер/блок и мгновенный fail используют одну и ту же логику.

**Причина**

Ваниль игнорировала маскировку: в комбезе milstalk задания Кирилла всё равно валились по истинному ISG. Нужно: напялил комбез фракции — считаешься ею для этих проверок.

**Не затронуто**

- Разоблачение disguise, default_faction, LTX

## [1.0.0] — 2026-09-20

**Изменено**

- `gamedata/scripts/fix_drx_enemy_task_gate.script` — monkey-patch:
  - `xr_conditions.has_completed_task_prerequisites` — не отдаёт задания с `{=drx_sl_is_enemy(<фракция>)} fail` в `condlist_*`, пока актор враг этой фракции (доска + диалог);
  - `task_manager.CRandomTask.give_task` — отказ принять такое задание (без `on_fail` / штрафа goodwill).

**Причина**

Задания вроде `dmitrov_kirill_task_*` имеют fail при `drx_sl_is_enemy(milstalk)`, но не в `precondition`. ИИГ/ISG брал их с доски → мгновенный провал и минус репутации у milstalk.

**Не затронуто**

- LTX заданий, тексты, награды
- Уже принятые задания
- MCM

**Совместимость**

- Сейвы: без миграции
- Рядом с `fix_hostage_task_collision` / taskboard (оба патчат `give_task` — порядок MO2: этот фикс ниже/позже других give_task-wrap'ов желателен)

**Проверено**

- lint: `python tools/lint_addon.py fix_drx_enemy_task_gate`
- в игре: не прогонялось. Ожидание: за ИИГ нет заданий Кирилла на доске; в логе `hide/block ... (enemy of milstalk ...)`, без `DRX SL task ended` + goodwill− сразу после take
