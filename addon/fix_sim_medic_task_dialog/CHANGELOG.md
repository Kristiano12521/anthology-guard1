# fix_sim_medic_task_dialog

## [1.0.1] — 2026-09-08

**Сделано**

- Не добавлять `dm_sim_ordered_task_dialog`, если уже есть `dm_ordered_task_dialog` (одинаковая фраза «Найдётся ли работа…»).
- По-прежнему добавляются только `dm_sim_ordered_task_completed_dialog` и `dm_sim_ordered_task_cancel_dialog`.

**Причина**

После 1.0.0 сдача sim-замера заработала, но в меню появились две одинаковые строки про работу.

**Не затронуто**

- Логика сдачи / `get_first_finished_task`
- Диалоги лечения

## [1.0.0] — 2026-09-08

Callback `on_specific_character_dialog_list`: при наличии `dm_ordered_task_completed_dialog` без sim-варианта добавлялись все три `dm_sim_ordered_task_*`.
