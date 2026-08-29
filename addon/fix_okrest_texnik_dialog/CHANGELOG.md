# Okrest Technician Dialog Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/okrest/mod_okr_a5_main_texnar_fix_okrest_texnik_dialog.ltx` — DLTX на `[meet@stalker_texnik_meet]`: сюжетный `okr_quest_s1_texnik_dialog` стартует только при `+okr_s1_actor_give_instr`.
- `gamedata/configs/text/rus/st_fix_okrest_texnik_dialog.xml` — русский текст трёх динамических заданий на комплекты (в сборке он был только в `eng/`).

**Причина**

После первого разговора (`okr_a5_texnik_dialog_talks`) `meet_dialog` всегда ставит `okr_quest_s1_texnik_dialog` («Ну что, где мои инструменты?»), пока нет `okr_s1_texnik_dialog_talks`. В XML сдача сюжета закрыта `<has_info>okr_s1_actor_give_instr</has_info>`, без предмета остаётся фраза `555555` с `dialogs.break_dialog`. Разговор обрывается — меню механика и `dm_ordered_task_completed_dialog` из `character_desc_attribute.xml` не открываются. Сдать `itm_basickit` / `itm_advancedkit` / `itm_expertkit` нельзя, обычный разговор тоже.

ZIP v1.4.0 подменял весь `okr_a5_main_texnar.ltx`, ставил `use = true` и дублировал сдачу комплектов в `meet_dialog`. `use = true` снимает автостарт кейса (`self` после `okr_a5_texnik_baza_scena_end_ztk`) и открывает разговор до диалога с Шерифом. Ветки `has_task` + `dm_ordered_task_completed_dialog` не нужны: этот диалог уже висит у NPC как `actor_dialog` с precondition `dialogs.actor_has_finished_ordered_task`.

**Как исправлено**

Один DLTX: в condlist сюжетной ветки добавлен `+okr_s1_actor_give_instr` — тот же флаг, что в XML. Без сюжетного предмета стартует `okr_stand_hello_texnik_dialog`, дальше штатное меню. `use` не тронут.

**Не затронуто**

- `use`, `animpoint@a5_stalker_texnik_scena`, `meet = no_meet` на сцене
- `dialogs_attribute.xml`, `character_desc_attribute.xml`
- задания `okr_a5_stalker_texnik_task_1`…`3`, `tm_attribute_mod_dynamic.ltx`
- спавн `okr_s1_instrum`, сцена с кейсом, диалог открытия кейса
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Condlist читается на следующем тике meet-схемы
- Конфликты: ZIP v1.0.0–1.4.0 подменяет тот же `okr_a5_main_texnar.ltx` целиком — выключить. В MO2 ниже сборки

**Проверено**

- lint: `python tools/lint_addon.py fix_okrest_texnik_dialog`
- В игре: не прогонялось. После первого диалога с Технарём без `okr_s1_instrum`: приветствие и меню механика, сдача комплектов через обычную фразу задания. С `okr_s1_actor_give_instr`: сюжетный вопрос об инструментах. После сцены у стола NPC сам начинает диалог про кейс
