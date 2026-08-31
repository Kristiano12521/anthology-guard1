# Quest Story ID Collision Fix

## [1.0.2] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; `printf` с причиной при раннем выходе из `install()`.

**Не затронуто**

- Обёртка `story_objects.register`, ремонт Levsha.

## [1.0.1] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_quest_story_id.script` — retry ремонта `yan_quest_levsha` через `ResetTimeEvent` + `return false`, а не повторный `CreateTimeEvent` тех же id.

**Причина**

Пока слот жив, `CreateTimeEvent` с той же парой id — no-op (`_g.script`). Следом `return true` снимал действие, поэтому вторая и дальнейшие попытки не запускались, если task manager ещё не был готов.

**Как исправлено**

Тот же приём, что у остальных `fix_*` repair: `ResetTimeEvent(EVENT_ID, REPAIR_ACTION, REPAIR_DELAY)` и `return false`. Слот остаётся, таймер сдвигается на 1 с, до `REPAIR_MAX_ATTEMPTS`.

**Не затронуто**

- DLTX, обёртка `story_objects.register`, предпочтения story_id
- XR-логика Левши, `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_story_id --no-verify`
- В игре: не прогонялось

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/misc/squad_descr/mod_squad_descr_yantar_fix_quest_story_id.ltx` — снят `story_id` у отряда `yan_stalker_levsha_true`.
- `gamedata/configs/misc/squad_descr/mod_squad_descr_cop_jupiter_fix_quest_story_id.ltx` — снят `story_id` у повторяемого `jup_a9_dogs_normal`.
- `gamedata/configs/items/items/mod_items_quest_spectrum_project_fix_quest_story_id.ltx` — снят `story_id` у `bar_a2_spec_juk_item_1` / `_2`.
- `gamedata/scripts/fix_quest_story_id.script` — monkey-patch `story_objects.register`: при коллизии выбирается объект, который ищут квесты. Одноразовый ремонт `current_target` у `yan_quest_levsha` на старом сейве.

**Причина**

`story_objects.register` оставляет первого владельца id и отбрасывает остальных. Отряд Левши регистрировался раньше NPC — маркер `yan_quest_levsha` смотрел на offline-group. Два «Сердца Оазиса», документы сюжета и их spatial-маркеры, зоны Кордона и лампы X-5 делили id в кастомдате спавна. Конвертер Спектрума создаёт пять одинаковых устройств с одним `story_id`.

ZIP v1.0.3 подменял весь `all.spawn`, ставил `zzzzzz`-скрипт и перематывал XR-логику Левши. Это запрещено правилами проекта и смешивает два разных бага.

**Как исправлено**

Конфиг-коллизии — DLTX, поле `!story_id`. Спавн-коллизии без замены `all.spawn`: обёртка `register()` отдаёт id сердцу Юпитера, предмету-документу и NPC Левши. Старый сейв Левши: `CreateTimeEvent` один раз подменяет `current_target`, если он всё ещё указывает на отряд. `check_task` и сам подхватит новый id через `get_story_object_id`.

**Не затронуто**

- `all.spawn`, `story_objects.script` целиком
- XR-логика Левши (`yan_scene_6_stalker_5.ltx`, `remark@yan_give_orders`)
- Предметы, названия, условия сдачи (`actor_has_item`, info portions)
- Респавн собак `jup_a9_dogs_normal` (`squad_exist` / `create_squad`)
- Квест Долины Шорохов (`actor_has_item(af_oasis_heart)`)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Уже выданный `yan_quest_levsha` с целью-отрядом чинится при загрузке
- Конфликты: нет пересечения файлов с ZIP v1.0.x (тот заменял `all.spawn` и `zzzzzz_*.script`). В MO2 ниже сборки; ZIP и `[DBG] Kristiano Fixes ALL IN ONE` с тем же `zzzzzz_anthology_quest_story_id_runtime_fix.script` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_story_id`
- В игре: не прогонялось. Левша: маркер на NPC, не на отряд. Лог: `register() wrapped`, без `Multiple objects trying to use same story_id` для перечисленных id. Диалог Левши, если секция уже `remark@yan_give_orders` без `yan_proriv_k_ystanovke_start` — отдельный баг, этот аддон его не чинит
