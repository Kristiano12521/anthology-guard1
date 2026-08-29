# X-15 Freeplay Gate Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/labx15/mod_lxm15_key_1_door_lock_fix_x15_freeplay_gate.ltx` — DLTX на `[ph_button@quest]`: без контракта картоприёмник переходит в `@press`, как остальные двери лаборатории.

**Причина**

Решётка `lx15m_gate_1` поднимается по `+lx15m_t1_knopka_door_opened`. Флаг выдаёт кнопка `lxm15_key_1_door_lock` после нажатия, но в `@quest` она ждёт `+lx15m_t1_door_mojno_press_go`. Этот флаг ставит только `lx15_m_control_prolog.ltx` при `+az_radar_afina_dialog_to_complate_quest_shmotki_saying` и дешифраторе — то есть сюжет контракта. Во фриплее кнопки нет, tooltip «нет доступа», решётка стоит.

Остальные двери X-15 уже имеют ветку `{-contract_for_a_new_life} ph_door@closed`. У картоприёмника такой ветки не было.

ZIP v1.0.2 крутил `actor_on_update`, через 120 кадров сам ставил `lx15m_t1_knopka_door_opened` и подменял `s11_lxm15_sound_give_xr` / `_xr2` пустышками. Функции звука есть в `xr_effects_contract_new_life.script`; патч их глушил. `zzzz_*.script` запрещён правилами.

**Как исправлено**

Один DLTX: `on_info3` на существующую секцию `@quest`. Игрок жмёт кнопку, штатный `@open` через 5 тиков выдаёт флаг, решётка поднимается, звук играет как в сюжете. Скриптов нет.

**Не затронуто**

- `lx15m_gate_1.ltx`, катсцена `l15_control_gate_sr`, скример, спавн отряда
- `lx15_m_control_prolog.ltx` и выдача `lx15m_t1_door_mojno_press_go`
- `xr_effects_contract_new_life.script` (`s11_lxm15_sound_give_xr` / `_xr2`)
- задания `s11_poisk_otryad_glava_2_to`, `main_22_search_labx15`, `contract_virus_search_quest_info`
- двери `labx15_door_1`…`5` (у них ветка без контракта уже есть)
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Кнопка в `@quest` подхватывает `on_info3` на следующем тике логики
- Конфликты: нет пересечения файлов с ZIP v1.0.2 (тот ставил `zzzz_anthology_x15_freeplay_gate_fix.script`). В MO2 ниже сборки; ZIP v1.0.0–1.0.2 и копию скрипта в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_x15_freeplay_gate`
- В игре: не прогонялось. Фриплей, X-15 (`l15u_pripyat_und`), без `contract_for_a_new_life`: картоприёмник жмётся, решётка поднимается, без F7. Сюжет контракта: кнопка по-прежнему ждёт дешифратор и диалог Афины
