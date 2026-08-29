# Gonta Duplicate Dialog Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/modxml_fix_gonta_duplicate_dialog.script` — DXML: из `zat_b106_stalker_gonta` в `character_desc_cop_zaton.xml` убираются `<actor_dialog>gonta_about_himself</actor_dialog>` и `gonta_about_mutants`, если рядом уже есть CoP-пара `zat_b106_stalker_gonta_about_*`.

**Причина**

У Гонты на Скадовске в меню два одинаковых пункта «Расскажи о себе» и два «Расскажи об охоте на мутантов». В `character_desc_cop_zaton.xml` у `zat_b106_stalker_gonta` висят и оригиналы CoP (`zat_b106_stalker_gonta_about_himself` / `_about_mutants`), и копии LTTZ (`gonta_about_himself` / `gonta_about_mutants`, помечены `<!-- LTTZ -->`). Тексты почти слово в слово. Юпитерный клон `jup_b6_stalker_gonta` дублей не имеет.

ZIP v0.1.0 BETA срезал копии в `on_specific_character_dialog_list` анонимным callback и файлом `zzzz_*.script`. Список реплик чистился при разговоре, XML не трогался, обработчик нельзя снять.

**Как исправлено**

DXML на разборе `gameplay\character_desc_cop_zaton.xml`: именованный `on_xml_read`, `query` + `removeElement`. Это тот же слой, что DLTX для LTX. Копии снимаются только если CoP-пара на месте — профиль, где LTTZ-ветки единственные, не трогается.

**Не затронуто**

- `dialogs_zaton.xml`, `dialogs_cop_zaton.xml`, строковые таблицы
- сюжетные реплики Гонты (Сорока, химера, вампир, Шутник, наём охотников)
- `jup_b6_stalker_gonta`, задания `zat_b106_stalker_gonta_task_*`
- `all.spawn`, сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Список реплик читается из XML при инициализации персонажа
- Конфликты: ZIP v0.1.0 выключить — тот же эффект более грубым способом. В MO2 ниже сборки
- `on_xml_read` намеренно не снимается: иначе после выхода в меню патч опоздает к разбору character_desc

**Проверено**

- lint: `python tools/lint_addon.py fix_gonta_duplicate_dialog`
- В игре: не прогонялось. Затон, Скадовск, Гонта: по одному «о себе» и «об охоте». В логе: `stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`
