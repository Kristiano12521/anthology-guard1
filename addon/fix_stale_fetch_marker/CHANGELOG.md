# fix_stale_fetch_marker

## 1.0.2

- v1.0.1: `probed=0` при живом `eloquent_task_8_fetch` у diag — `load_var` + обход только `task_info` не видели ключи.
- Скан pstor напрямую (`AC_ID` / `0` / `actor:id()`), ключи `*_fetch`; очистка в таблице + `save_var`.

## 1.0.1

- v1.0.0 загружался, но не чистил: у призрака `eloquent_task_8` условие только по `status=completed/fail` не сработало.
- Очистка также при `stage=255` и когда есть `*_fetch`, но `actor:get_task` уже nil (нет задания в PDA).
- Лог `probe` / `sweep … probed/cleared`; повторный sweep через 2 с после `actor_on_first_update`.

## 1.0.0

- Причина: после сдачи fetch-таска с `repeat_timeout` запись остаётся в `task_info`, а `*_fetch` в pstor часто не сбрасывается. Utjans `fetch_item_icon` смотрит только `last_check_task` → метка в инвентаре без задания в PDA (кейс: `eloquent_task_8` / `dolg_patch`).
- Скрипт чистит stale `*_fetch` на `actor_on_first_update` / `on_before_level_changing`.
- DLTX: `=pstor_reset(…_fetch)` в `on_complete` для `eloquent_task_3/5/6/7/8`.

Не затронуто: выдача/награды fetch, активные метки, файл Utjans, Tosox keep-items.

Сборка: Anthology 2.1 / Anomaly 1.5.3.
