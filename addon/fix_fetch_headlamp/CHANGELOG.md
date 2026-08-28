# Fetch Headlamp Fix

## [1.0.0] — 2026-08-28

**Изменено**

- `gamedata/configs/misc/task/task_manager_anthology/mod_tm_anthology_dynamic_fix_fetch_headlamp.ltx` — в пуле fetch Волка (`esc_2_12_stalker_wolf_task_9`) и Фанатика (`esc_2_12_stalker_fanat_task_9`) `device_torch` заменён на `device_torch_dummy`.

**Причина**

Динамический квест «полевое снаряжение» выбирает секцию `device_torch` (служебный фонарь слота 9). В рюкзаке игрока лежит `device_torch_dummy` с тем же `inv_name`. Проверка `actor:object(section)` / `item:section() == section` не находит предмет — в диалоге «x0».

**Как исправлено**

DLTX на два поля `fetch_func`. Скрипты fetch не трогались: достаточно правильной секции в пуле.

**Не затронуто**

- `tasks_fetch.script`, Utjans `z_fetch_shows_count.script`
- `fetch_list.ltx`
- ПНВ-фонари `device_torch_nv_*`, junk `headlamp`
- Остальные fetch-квесты Волка/Фанатика (аптечки, патроны, стволы, нашивки)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Уже выданный запрос на `device_torch` остаётся до отказа и нового разговора (кэш `DIALOG_ID` сбрасывается при смене уровня)
- Конфликты: нет пересечения файлов; в MO2 ниже сборки

**Проверено**

- lint: `python tools/lint_addon.py fix_fetch_headlamp`
- В игре: не прогонялось. Волк / Фанатик, квест полевого снаряжения, налобный фонарик в рюкзаке — счётчик x1, сдача забирает `device_torch_dummy`. Если диалог уже показал фонарик до патча: «Ладно, забудь», сменить локацию, спросить снова.
