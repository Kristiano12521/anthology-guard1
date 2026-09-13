# Tosox vanish-fail на общем DRX stash-слоте

## [1.0.0] — 2026-09-13

**Изменено**

- `fix_quest_item_shared_fail.script` — обёртка `task_status_functor.drx_sl_quest_item_task_status`: вместо Tosox `"fail"` при мёртвом `var.item_id` сбрасывает `item_id` / `stash_created`, берёт новый `target_id` через `get_random_stash` и оставляет квест на `stage=0` с меткой тайника.

**Причина**

На общих слотах 1/2/3 (`simulation_task_46` + `mar_smart_terrain_base_doctor_task_4` и др.) один `drx_sl_quest_item_N` попадает в `item_id` обоих заданий. Сдача одного делает `alife_release`; Tosox `z_task_marker_delivery_fix` (стр. 55–59) трактует это как потерю предмета и валит соседний заказ.

**Не затронуто**

- Файл Tosox, `tasks_stash.script`, `fix_quest_stash`, LTX-слоты / `remove_item` в `on_complete`, диалоги сдачи.

**Совместимость**

- Сейвы: новая игра не нужна. Поля `save_var` те же; при срабатывании переписываются `item_id`, `stash_created`, `target_id`, `lvl_target`.
- В MO2 ниже сборки и рядом с `fix_quest_stash`; порядок относительно Tosox не критичен (обёртка ставится в `on_game_start` + отложенно).

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_item_shared_fail` — 0 ошибок
- `--cross`: пересечений по этому моду нет
- В игре: не прогонялось. Ожидание: сдача одного document-заказа на слоте 1 не даёт fail второму; в логе `rearm task=...`; метка на новом тайнике.
