# LTTZ Rogue Hostility Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/misc/squad_descr/mod_squad_descr_lostzone_ll_fix_rogue_hostility.ltx` — DLTX: `relationship = friend` у `stalker_rogue_squad`.
- `gamedata/scripts/fix_rogue_hostility.script` — одноразовый `CreateTimeEvent`: на старом сейве вызывает штатный `set_squad_relation("friend")` и сбрасывает ложный `death.killer` у живого Бродяги.

**Причина**

`stalker_rogue_squad` спавнится на Скадовске без поля `relationship`. `create_npc` тогда не вызывает `set_squad_relation`, и Бродяга берёт фракционный goodwill. При враждебной/плохой репутации к одиночкам `xr_conditions.actor_enemy` становится true: `use` в `stalker_rogue.ltx` закрывает диалог, в `zat_a2_sr_noweap` он бьёт врукопашную и не стреляет. Тот же персонаж в Припяти / Mortal Sin / Afterglow уже имеет `relationship = friend`.

ZIP v1.0.0 крутил `actor_on_update` до 30 с, сканировал id 1..65534, ставил `zzzzzz`-скрипт и вручную дёргал goodwill/`set_relation`/`enable_talk`.

**Как исправлено**

Поле отряда — DLTX, тот же приём что у `pri_a16_stalker_rogue_squad`. Новый спавн сам ставит friend через `sim_squad_scripted:set_squad_relation`. Уже заспавненный отряд на сейве — один `CreateTimeEvent`, без `actor_on_update`.

**Не затронуто**

- `stalker_rogue.ltx`, диалоги, `tm_lostzone_ll.ltx`
- `pri_a16_stalker_rogue_squad`, `stalker_rogue_ms_squad`, `stalker_rogue_oa_squad`, `stalker_rogue_monolith`
- общие отношения фракций, goodwill игрока
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Враждебный Бродяга на `lttz_ll_meet_rogue` / `lttz_ll_visit_beard` чинится при загрузке за 1–10 с, пока нет `living_legend_rogue_start`
- Конфликты: нет пересечения файлов с ZIP v1.0.0 (тот только `zzzzzz_*.script`). В MO2 ниже сборки; ZIP и `[DBG] Kristiano Fixes ALL IN ONE` с тем же `zzzzzz_anthology_lttz_rogue_hostility_fix.script` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_rogue_hostility`
- В игре: не прогонялось. Скадовск на `lttz_ll_meet_rogue`: Бродяга не красный, диалог открывается, ближняя атака прекращается. Лог: `set stalker_rogue_squad relation=friend`
