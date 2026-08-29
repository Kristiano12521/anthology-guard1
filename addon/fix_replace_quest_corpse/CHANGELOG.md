# replace_quest_corpse Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_replace_quest_corpse.script` — кладёт на `_G` недостающую `replace_quest_corpse`: спавнит `*_replace_spot` (тот же `story_id`, что у трупа) и квестовый предмет через штатный `create()`.

**Причина**

`sgm_tasks.task_update()` вызывает глобальную `replace_quest_corpse`, которой нет в Anthology 2.1. Когда симуляция снимает квестовый труп (далёкий поход, не обязательно Х-16), ветки «Громобой» / «Касилов» / «Научный доклад» делают `nil()` — FATAL на загрузке сейва, стек `sgm_tasks.script(342)`.

**Как исправлено**

Не замена `sgm_tasks.script` и не обёртка всего `task_update`. Функция ставится в `_G` при загрузке скрипта и в `on_game_start`, чтобы обогнать `bind_stalker` → `task_main`. Если функция уже есть (официальный фикс), патч её не трогает.

**Не затронуто**

- `sgm_tasks.script` и остальные квесты SGM
- координаты и info-поршни `_safe` / `_fail` / `_pda`
- сохраняемое состояние
- MCM

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции; старый сейв должен загрузиться
- Конфликты: нет пересечения файлов. В MO2 ниже сборки. Снять `[FIX] Bagulya Task Corpse Fix FULL` — он подменяет весь `sgm_tasks.script`

**Проверено**

- lint: `python tools/lint_addon.py fix_replace_quest_corpse`
- В игре: загрузить сейв, который раньше падал на `replace_quest_corpse`. В логе: `installed on _G`. Квест не должен закрывать игру.
