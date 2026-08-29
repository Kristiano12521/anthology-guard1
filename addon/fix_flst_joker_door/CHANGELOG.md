# Fallstation Joker Door Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/fallstation/mod_flst_roll_entrance_logic_fix_flst_joker_door.ltx` — DLTX на `[sr_idle@wait]`: тот же переход, что у стокового `[sr_idle@lab_10]`, если уже выдан `flst_j1_dialog_ohr_open_ze_dver`.

**Причина**

Роллетная дверь Fallstation открывается на выход только из `sr_idle@lab_10` по флагу диалога охранника (`flst_j1_ohrannik` / Joker). После выхода контроллер через `@exit_2` уходит в `@init` → `@wait`, если актёр уже не в `flst_j1_sr_ohr` (зона охранника, не вся база). `@init` снова запирает дверь и сбрасывает флаг. Игрок остаётся внутри, возвращается к Джокеру, снова получает флаг — а `@wait` слушает только кнопку снаружи (`+flst_roll_door_call`). То же на сейве, где секция логики сохранена как `@wait`, а инфопоршень уже стоит: `xr_logic.save_obj` пишет `active_section`.

ZIP v1.0.0 BETA подменял весь `flst_roll_entrance_logic.ltx`. Копия лежит в `[DBG] Kristiano Fixes ALL IN ONE`.

**Как исправлено**

Один DLTX: `on_info2` на существующую `[sr_idle@wait]`. Условие и эффекты скопированы с `[sr_idle@lab_10]` — открытие `flst_roll_door`, запирание внутренней двери, `+flst_j1_guard_say_bye`. Вход по кнопке (`on_info`) не тронут. Скриптов нет.

**Не затронуто**

- `flst_roll_door.ltx`, `flst_roll_door_button.ltx`, `flst_roll_enter_door.ltx`
- `flst_j1_main_logic.ltx` и диалог `flst_j1_ohrannik_hello_dialog`
- `@init` / `@pred*` / `@lab_10` / `@exit_*`, в том числе сброс флага в `@init` и `@exit_2`
- переход Окресты ↔ Fallstation, катсцена `flst_start_game_sr_cut`
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Зависший `@wait` с уже выданным флагом подхватывает `on_info2` на следующем тике логики
- Конфликты: нет пересечения файлов с ZIP v1.0.0 (тот заменял оригинал). В MO2 ниже сборки; ZIP и копию `configs/scripts/fallstation/flst_roll_entrance_logic.ltx` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_flst_joker_door`
- В игре: не прогонялось. После диалога с Джокером на выход роллета открывается и из `@wait`. Вход кнопкой снаружи как в стоке.
