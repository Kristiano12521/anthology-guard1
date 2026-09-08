# fix_sim_medic_task_dialog

## [1.0.2] — 2026-09-08

**Сделано**

- Если есть `dm_ordered_task_dialog` / `_dialog2`, **всегда снимаются** `dm_sim_ordered_task_dialog` / `_dialog2` (вторая «Найдётся ли работа…»).
- Раньше при уже существующем sim-completed скрипт выходил сразу и дубль не трогал (типично у механиков/торговцев с `character_dialogs.xml` + ordered).

**Не затронуто**

- Сдача/отмена sim-заданий
- Одна оставшаяся строка выдачи работы (ordered)

## [1.0.1] — 2026-09-08

Не добавлять sim-give, если ordered-give уже есть; только completed/cancel.

## [1.0.0] — 2026-09-08

Первый инжект трёх `dm_sim_ordered_task_*` при наличии ordered-completed.
