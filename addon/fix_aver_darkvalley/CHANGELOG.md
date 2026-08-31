# Aver Dark Valley Transition Fix

## [1.0.1] — 2026-08-31

**Изменено**

- `gamedata/scripts/fix_aver_darkvalley.script` — перед запасным `for id = 1, MAX_ALIFE_ID` комментарий `-- alife-scan: запасной путь, …` (LUA-008).

**Причина**

Цикл остаётся: `pcall` вокруг `iterate_objects` ловит любую ошибку обхода, не только отсутствие метода. Без запасного пути мод молча ничего не сделает. Линтер снимает предупреждение комментарием в трёх строках перед циклом.

**Не затронуто**

- отбор целей, `try_fix_object`, callback'и, кэш id
- сам обход: сначала `sim:iterate_objects`, цикл только если метода нет или `pcall` упал
- `all.spawn`, LTX, `save_state` / `load_state`
- `verified_*` в `meta.ini`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции

**Проверено**

- lint: `python tools/lint_addon.py fix_aver_darkvalley` — LUA-008 нет
- VERIFY-001: в игре не прогонялось. `verified_*` не ставились.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_aver_darkvalley.script` — один раз за загрузку переписывает `dest_position` / `dest_game_vertex_id` / `dest_level_vertex_id` у пары нативных level changer’ов `aver` ↔ `l04_darkvalley` через `utils_stpk.get_level_changer_data` / `set_level_changer_data`. Если сейв уже стоит на известной битой точке — один телепорт на `actor_on_first_update`.

**Причина**

Переходы Неизведанные Земли ↔ Тёмная долина приземляют не у своих ворот:

- `aver` → `l04_darkvalley` — dest скопирован с перехода из Забытого Леса (`puzir`): `-157.58, -0.14, -433.52`
- `l04_darkvalley` → `aver` — dest скопирован с перехода со Свалки: `-367.54, 6.28, -431.52`

Значения лежат в STATE-пакете ALife (`all.spawn` / сейв). DLTX на `sr_teleport_sections.ltx` их не меняет: `path` там — патруль текущей карты. `all.spawn` править нельзя.

ZIP v0.5 BETA ловил актора после прибытия: pending-маршрут в `alife_storage_manager`, `actor_on_update` до 45 попыток, `zzz`-имя, гонка с обратным LC, нет `UnregisterScriptCallback` / `on_game_load`. Нативный переход часто не шлёт `on_before_level_changing`, поэтому fallback в v0.5 всё равно опаздывал.

**Как исправлено**

Пакет пишется до `M_CHANGE_LEVEL`. Имена: `aver_level_changer_to_darkvalley_1`, `val_level_changer_to_aver_1`. Запасной отбор: `clsid` level changer на исходной карте с dest в 25 м от известной битой точки — чтобы не задеть `gar_*` / `puzir_*` с теми же координатами. `gvid`/`lvid` берутся с ближайшей вершины `game_graph()` на целевой карте, без хардкода. Целевые точки — существующие walkable патрули (~47 м от обратных ворот, не 11 м как в v0.4). `server_entity_on_register` — быстрый путь; иначе один скан на `actor_on_first_update` и повтор на `on_before_level_changing` / `on_level_changing`. Сброс на `on_game_load`. Новый dest остаётся в STATE и уходит в сейв сам.

**Не затронуто**

- `all.spawn`, `sr_teleport_sections.ltx`, `ChangeLevel`, `ui_sr_teleport.script`
- переходы Свалка ↔ aver, puzir ↔ Dark Valley и все остальные LC
- `val_smart_terrain_7_3` (база бандитов) как точка появления
- сохраняемые таблицы мода (своего `save_state` нет)
- `actor_on_update`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции и без новой игры. Патч применяется к уже существующим объектам ALife
- В MO2 ниже сборки. ZIP `Anthology_Aver_DarkValley_RuntimeFix_v0.5_BETA` и копию `zzz_aver_darkvalley_runtime_fix.script` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_aver_darkvalley`
- В игре: не прогонялось. Загрузить сейв на `aver` перед воротами в долину, пройти `aver` → `l04_darkvalley`, затем обратно. Ожидание: в логе `rewrote dest` или `already fixed`, появление не у puzir-стороны и не у перехода на Свалку, без мгновенного отскока. Отдельно: `l02_garbage` → `aver` не должен измениться.
