# Noosphere Voice X18 Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/labx18/smart/mod_dar_control_poltergeist_fix_noosphere_voice_x18.ltx` — DLTX на `[exclusive]`: подключены job'ы диалоговой сущности, фантомов и финального полтергейста.
- `gamedata/scripts/fix_noosphere_voice_x18.script` — `npc_on_death_callback` для шести фантомов; одноразовый `CreateTimeEvent` чинит сейв, где стадия уже убита без `*_despawn`.

**Причина**

`dar_control_poltergeist.ltx` регистрировал только `com_center_poltergeist`. Логика `x18_dark_presence_apparitions.ltx` в сборке есть, но smart её не назначал. Эйдолон умирал как обычный NPC, `monolith_eidolon_ghost_despawn` не выдавался, `task_status_functor` не спавнил Саваофа, квест оставался на `text5`.

ZIP v1.0.1 подменял весь smart-файл, ставил `zzzz`-скрипт и крутил `actor_on_update`. Финальный полтергейст и так имеет `on_death` в `squad_descr`.

**Как исправлено**

Exclusive-job'ы — DLTX, тот же приём что `mod_yan_smart_terrain_6_4_redemption.ltx`. Штатная схема снова даёт `*_despawn` на пороге HP. One-shot и уже мёртвый фантом в сейве — callback смерти и отложенный recovery. `actor_on_update` нет.

**Не затронуто**

- `task_status_functor.script`, `tm_lostzone_dp.ltx`, `squad_descr_lostzone_dp.ltx`
- файлы логики apparitions / `x18_dark_presence` / `dar_control_poltergeist2_logic`
- ванильный job `com_center_poltergeist`, пороги HP, диалоги, условия сдачи
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Зависший после Эйдолона чинится при загрузке в X-18 за 8–15 с
- Конфликты: нет пересечения файлов с ZIP v1.0.x (тот заменял оригинал и `zzzz*.script`). В MO2 ниже сборки; ZIP и `[DBG] Kristiano Fixes ALL IN ONE` с тем же `zzzzzzzzzzzzzz_anthology_lttz_noosphere_voice_x18_fix.script` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_noosphere_voice_x18`
- В игре: не прогонялось. Новое прохождение X-18: после Эйдолона появляется Саваоф, затем чёрный полтергейст. Зависший сейв в X-18: в логе `RECOVERY story=monolith_eidolon_ghost state=... -> +monolith_eidolon_ghost_despawn`
