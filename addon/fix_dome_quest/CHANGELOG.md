# Dome Quest Marker Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/misc/task/task_manager_anthology/mod_tm_az_radar_mod_fix_dome_quest.ltx` — DLTX на `target` у `cit_a2_quest_sich_to_ecolog_posilka` и `atr_quest_ecolog_art_oazis_and_compass`: `sad_atr_trader` → `az_radar_atr_trader`.
- `gamedata/configs/scripts/az_radar/kupol/mod_kup_b38_door_secret_fix_dome_quest.ltx` — DLTX на `on_info` у `sr_idle@spawn_keys`: труп в «Луче» спавнится как `kup_b38_local_ecolog_corpse`.
- `gamedata/configs/creatures/mod_spawn_sections_az_radar_city_fix_dome_quest.ltx` — локальная секция трупа без `story_id`, профиль `sim_default_ecolog_1` (`@`, чтобы не дублировать базу, если старый ZIP ещё включён).

**Причина**

Квесты Куплинова («Посылка Щербана», возврат «Сердца Оазиса» и «Компаса») копипастой смотрят на `sad_atr_trader` — Стаховского в Долине Шорохов. Нужный NPC — `az_radar_atr_trader` на Куполе.

В «Луче» `kup_b38_door_secret.ltx` вызывает `spawn_corpse(pri_b306_envoy:...)`. Секция из `spawn_sections_pripyat.ltx` несёт `story_id = pri_b306_envoy`; `xr_effects.spawn_corpse` делает `alife_create` и регистрирует уникальный объект Припяти. Профиль ещё и кладёт в труп `pri_b306_envoy_pda`.

ZIP v1.0.0 подменял целиком `tm_az_radar_mod.ltx` (~790 строк) и логику рестриктора. Профиль посланника оставили — КПК CoP на трупе в «Луче» оставался.

**Как исправлено**

Только DLTX. Маркеры — два поля `target`, как `fix_fetch_headlamp`. Труп — override одной строки `on_info` плюс новая секция рядом с остальными spawn_sections Купола. Профиль общий экологовский, без `story_id` и без квестового КПК.

**Не затронуто**

- Сами файлы `tm_az_radar_mod.ltx` и `kup_b38_door_secret.ltx`
- Условия квестов, награды, вход в X-15 / «Метро-15»
- Маркер «Метро-15» до получения артефактов (`cit_kpl_4_spot`)
- Спавн `pri_b306_envoy` в Припяти (`pri_b306_sr_control.ltx`)
- Второй и третий трупы в «Луче» (`jup_b202_bandit`, `sim_default_ecolog_1_sector`)
- Диалоги и апгрейд артефактов у Куплинова / Стаховского

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Уже взятые задания подхватывают новый `target` после перезагрузки. Если `+kup_b38_trups_and_key_spawn` уже выставлен, трупы в «Луче» не пересоздаются
- Конфликты: нет пересечения файлов с ZIP v1.0.0 (тот заменял оригиналы). В MO2 ниже сборки; ZIP и `[DBG] Kristiano Fixes ALL IN ONE` с теми же путями выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_dome_quest`
- В игре: не прогонялось. Посылка Щербана и возврат артефактов — маркер на Куплинове, не на Стаховском. В «Луче» до флага `kup_b38_trups_and_key_spawn` труп секции `kup_b38_local_ecolog_corpse`, без `pri_b306_envoy_pda`
