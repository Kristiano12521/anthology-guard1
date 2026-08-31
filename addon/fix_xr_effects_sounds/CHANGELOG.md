# XR Effects Sound Paths Fix

## [1.0.1] — 2026-08-31

**Изменено**

- `gamedata/scripts/fix_xr_effects_sounds.script` — сводка `wrapped` / `missing` через `%s`: `printf` Anomaly подставляет только `%s`.

**Причина**

В сессии 2026-08-31 в логе было `wrapped %d functions, missing %d` без чисел.

**Не затронуто**

- обёртки `xr_effects`, пути к звукам
- `verified_*` в `meta.ini`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции

**Проверено**

- lint: `python tools/lint_addon.py fix_xr_effects_sounds`
- VERIFY-001: в игре не прогонялось. `verified_*` не ставились.

## [1.0.0] — 2026-08-28

**Изменено**

- `gamedata/scripts/fix_xr_effects_sounds.script` — monkey-patch 19 функций `xr_effects` с битыми путями к звукам. Оригиналы не вызываются.

**Причина**

В Anthology 2.1 в `xr_effects.script` последовательности `\t` и `\n` внутри `[[ ]]` превратились в TAB и перевод строки. Lua long string не экранирует слэш, поэтому путь `okrest\tutorial_women\...` должен содержать слэш и букву `t`. После порчи движок ищет `okrest` + TAB + `utorial_women` — файла нет, голос молчит. Субтитры при этом живые.

Тот же сбой на папках/файлах на `t` и `n`: `taxiboys`, `tesak`, `tinnitus3a`, `t_f1_explosion`, `niichaz`, `n_*_shot`, `nii_intro_back_sound`.

**Как исправлено**

Monkey-patch таблицы `xr_effects` в `on_game_start`. DLTX не применим (это скрипт). Полная замена `xr_effects.script` (~11k строк) дала бы конфликт со всей сборкой. Глобальный `sound_object` нельзя подменить: на классе висят флаги `s2d` / `s3d`.

**Не затронуто**

- сам `xr_effects.script`
- LTX логики катсцен (`okr_sr_c5_perehod.ltx` и остальные)
- субтитры и `st_attribute_subtitres_mod.xml`
- соседние реплики с целыми путями (`okr_a5_tutor_radio_fnc`, монолог актёра)
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Конфликты: нет пересечения файлов; в MO2 ниже сборки

**Проверено**

- lint: `python tools/lint_addon.py fix_xr_effects_sounds`
- В игре: катсцена облёта базы на Окрестностях (`okr_a5_welcome_tutor_*`) — шесть женских реплик должны звучать вместе с субтитрами. В логе: `wrapped 19 functions, missing 0`.
