# Память bug-finding

Учёт критических багов с открытыми или отклонёнными PR. Не открывать дубликат, пока статус `open` или `rejected` (кроме случая, когда код заметно изменился после отклонения). Удалять записи после merge; удалять `rejected` старше 30 дней.

| Баг (место + причина) | PR | Статус | Записано |
| --- | --- | --- | --- |
| `fix_quest_stash`: слепой SHARED_TYPES 1–7 через `alife_release` забирает leftover-КПК; `recover_missing` считает `caches[id]==true` пропажей и дублирует КПК / пропускает лут | https://github.com/Kristiano12521/anthology-guard1/pull/2 | open | 2026-09-03 |
