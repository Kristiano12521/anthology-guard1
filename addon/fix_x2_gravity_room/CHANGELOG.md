# Lab X-2 Gravity Room Crash Fix

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; guard-сообщение при отсутствии `xr_effects`.

**Не затронуто**

- Functor `bas_no_gravity_anomaly`, таймер восстановления gravity.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_x2_gravity_room.script` — реализует отсутствующий `xr_effects.bas_no_gravity_anomaly`: короткий импульс `physics_world():set_gravity(0.01)` и возврат прежнего значения.
- `gamedata/configs/misc/mod_postprocess_fix_x2_gravity_room.ltx` — новая секция `[duality_circle]` для `run_postprocess`.
- `gamedata/configs/scripts/labx2/mod_bas_space_restrictor_0016_fix_x2_gravity_room.ltx` — DLTX на `[sr_idle]`: оригинальный condlist, если ZIP/Kristiano его вырезали.

**Причина**

После `+bas_switcher_off` вход в `bas_space_restrictor_0016` вызывает:

1. `run_postprocess(duality_circle)` — секции нет, `abort()` в этой сборке только пишет в лог;
2. `play_snd(affects\hit_fist)` — валидно;
3. `bas_no_gravity_anomaly` — функтора нет, `xr_logic.script:492` вызывает `nil` → CTD.

ZIP v1.0.0 BETA (копия Kristiano) подменяет весь LTX и удаляет оба вызова. Звук и `gravity_blast_final` остаются, сцена невесомости нет.

**Как исправлено**

Не файл целиком: недостающие реализации, вызов как в оригинале. Постпроцесс — `snd_shock.ppe` (в `postprocess.ltx` им уже заменили закомментированный `duality_circle.ppe`), `pp_eff_cyclic = 0`, иначе эффект завис бы: `run_postprocess` не снимает effector. Гравитация — тот же API, что `effect_swiming_true/false`; импульс 6 с, потому что в LTX нет `on_actor_outside` и схема сразу уходит в одноразовый particle. Сброс при смене уровня и загрузке.

**Не затронуто**

- `xr_effects.script`, `xr_logic.script`, `all.spawn`
- остальные restrictor'ы и катсцены X-2 (`bas_release_sc3/4/5` по-прежнему отсутствуют — отдельная тема)
- `bas_space_restrictor_0005` / `radio_blink`
- звук `hit_fist`, particle `anomaly2\gravity_blast_final`, путь `bas_sc7_particle`
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Гравитация в сейв не пишется
- Конфликты: нет пересечения файлов с ZIP v1.0.0 (тот заменял оригинал). В MO2 ниже сборки; ZIP и файл Kristiano `configs/scripts/labx2/bas_space_restrictor_0016.ltx` выключить — DLTX всё равно вернёт condlist, но полная замена того же пути может перебить базу

**Проверено**

- lint: `python tools/lint_addon.py fix_x2_gravity_room`
- В игре: не прогонялось. ЧАЭС-1 / X-2, выключить рубильник, войти в комнату с `bas_space_restrictor_0016`. Ожидание: ударный звук, короткое двоение, импульс невесомости ~6 с, particle blast, без CTD. В логе: `gravity pulse ...` затем `gravity restored`
