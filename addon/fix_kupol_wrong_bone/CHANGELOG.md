# Kupol Wrong Fixed Bone Fix

## [1.0.1] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_kupol_wrong_bone.script` — `scan_alife` сначала вызывает `alife():iterate_objects` под `pcall` (как `fix_aver_darkvalley`). Полный проход `1..65534` остаётся только если метода нет или вызов упал.

**Причина**

`lint_addon.py` LUA-008: на `actor_on_first_update` / смене уровня цикл `for id = 1, MAX_ALIFE_ID` с `alife():object` на каждом шаге даёт хитч. В этой сборке `iterate_objects` есть: `lua_help_ex.script` (`void iterate_objects(function(se_obj))`) и рабочие вызовы в Hideout Furniture и STORYLINES.

**Не затронуто**

- отбор цели (`cit_physic_object_0014` / `az_radar` / визуал / `fixed_bones = link`)
- `try_fix_object`, callback'и, кэш id, `on_game_load`
- `all.spawn`, LTX, `save_state` / `load_state` (их нет)
- `verified_*` в `meta.ini`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции

**Проверено**

- lint: `python tools/lint_addon.py fix_kupol_wrong_bone` — ошибок нет. LUA-008 остаётся на запасном `for id = 1, MAX_ALIFE_ID` (строка 220), тот же контракт что у `fix_aver_darkvalley`:450: цикл в файле есть, на загрузке не выполняется, если `iterate_objects` отработал.
- VERIFY-001: в игре не прогонялось. `verified_*` не ставились.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_kupol_wrong_bone.script` — один раз за загрузку снимает `fixed_bones = link` у `cit_physic_object_0014` на `az_radar` через `utils_stpk.get_physic_data` / `set_physic_data`.

**Причина**

Вход в Окрестности Купола (`az_radar`) даёт FATAL `P_build_Shell` / `PhysicsShell.cpp:150` / `wrong fixed bone`. После бинарной изоляции объект:

- имя `cit_physic_object_0014`, секция `physic_object` (`class = O_PHYSIC`, не `O_PHYS_S`)
- визуал `dynamics\dead_body\skelet_combine_pose_02`
- `fixed_bones = link`

`link` — кость статичных ящиков. Скелет трупа её не содержит. Значение лежит в STATE-пакете ALife (`all.spawn` / сейв), не в LTX: DLTX на `[physic_object]` заденет все physic-объекты, `all.spawn` править нельзя. Story id нет, `alife():object()` только по числовому id.

ZIP v1.0.0 сканировал 1..65534 на каждый `actor_on_first_update` и каждый переход, ставил `zzzz`-префикс, пропускал патч если игрок уже на `az_radar` (объект ещё может быть offline до `switch_distance`) и не снимал callback'и. В Kristiano есть `v1.1.0-opt1` с чанками по 256 id на кадр — окно до перехода из-за этого только шире.

**Как исправлено**

Пакет пишется один раз за загрузку, пока объект offline. `server_entity_on_register` — быстрый путь, если спавн всё же `se_physic`. Иначе одноразовый поиск по имени на `actor_on_first_update`, плюс синхронный повтор на `on_before_level_changing` / `on_level_changing`, если к переходу ещё не нашли. Найденный id кэшируется. Состояние сбрасывается на `on_game_load`. Патч не пропускается на самой локации: пока объект offline, его ещё можно починить. Пустой `fixed_bones` остаётся в STATE и уходит в сейв сам.

**Не затронуто**

- `all.spawn`, `[physic_object]`, `[skelet_sit_ass_no_hands]`, визуал и сам объект
- остальные physic-объекты Купола и других карт
- `bind_physic_object.script`, `se_item.script`
- сохраняемые таблицы мода (своего `save_state` нет)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции и без новой игры. Патч применяется к уже существующему объекту ALife
- В MO2 ниже сборки. ZIP `Anthology_Kupol_Wrong_Fixed_Bone_Fix_v1.0.0` и копию `zzzz_anthology_kupol_wrong_fixed_bone_fix.script` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_kupol_wrong_bone`
- В игре: не прогонялось. Загрузить сейв до входа в Окрестности Купола, войти обычным переходом. Ожидание: в логе `cleared fixed_bones` или `already clear`, без FATAL `wrong fixed bone`
