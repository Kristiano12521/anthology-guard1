# Grifon Visibility Fix

## [1.1.0] — 2026-09-04

**Изменено**

- `mod_ano_smart_terrain_6_2_smart_logic_fix_grifon_visibility.ltx` — `logic@merc_pri_grifon_mlr.active` → `remark@grifon_stand` (`anim = wait`, `target = story | actor`); `animpoint@base` получает `on_info = remark@grifon_stand` для старых сейвов.
- Presence-скрипт / `meta.ini` → v1.1.0.

**Причина**

`avail_animations = wait` (1.0.0) убирал lean `stay_wall`, но `action_animpoint:execute` по-прежнему snap’ил NPC в позицию/направление кавера — лицом в стену без lean. Нужно уйти с animpoint-кавера.

**Не затронуто**

- общий `[meet]`, механик, торговец, kamp_1..7
- visual, story_id, сквад, диалоги
- `pri_a_18_smart_mlr_logic.ltx`, `all.spawn`, `xr_animpoint.script`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без отдельной миграции. Старый `active_section = animpoint@base` переключается на remark через `on_info`
- В MO2 ниже сборки; полную подмену `ano_smart_terrain_6_2_smart_logic.ltx` (ZIP v1.0.4 / копия в `[DBG] Kristiano`) выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_grifon_visibility` (0 ошибок; VERIFY-001 — ждать игры)
- В игре: не прогонялось. На Аномальном лесу Грифон должен стоять с idle `wait`, смотреть на актора, без snap в стену

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/scripts/anomles/mod_ano_smart_terrain_6_2_smart_logic_fix_grifon_visibility.ltx` — DLTX на `[animpoint@base]`: `avail_animations = wait`.

**Причина**

Грифон (`merc_pri_grifon_mlr`) на `ano_smart_terrain_6_2` стоит в dedicated-кавере `anomles_smart_cover_mlr_merc_grifon`. Описание кавера — `animpoint_stay_wall`. В `xr_animpoint` это даёт `state_mgr.set_state(..., animation_position = cover.position)` и `npc:add_animation` с мировым трансформом кавера. Модель периодически пропадает из рендера, метка / имя / диалог остаются. Замена visual на `merc_black` проблему не снимала — это не сломанный меш профиля.

ZIP `Anthology_Grifon_Visibility_Fix_v1.0.4` подменял весь `ano_smart_terrain_6_2_smart_logic.ltx`: схема Грифона уходила в `remark@grifon_visibility_fix` без `cover_name`, а общий `[meet]` этого файла получал `close_victim = actor` / `close_distance = 5`. Remark без точки не ведёт к каверу. `[meet]` общий у механика, торговца и Грифона. Копия той же подмены лежит в `[DBG] Kristiano Fixes ALL IN ONE`.

**Как исправлено**

Одно поле существующей секции. В `xr_animpoint.fill_approved_actions` заданный `avail_animations` игнорирует ассоциации кавера (`animpoint_stay_wall` / eat / weapon). Состояние `wait` в `state_lib`: standing, weapon strapped, animation idle. `cover_name`, `reach_distance`, `logic@merc_pri_grifon_mlr.active = animpoint@base` и `[meet]` не тронуты: Грифон по-прежнему идёт к своей стене, активная секция сейва остаётся `animpoint@base`.

**Не затронуто**

- `logic@merc_pri_a18_mech_mlr`, `logic@pri_special_trader_mlr`, kamp_1..7
- общий `[meet]` / `[meet@bench]`
- visual, story_id, сквад, диалоги
- `pri_a_18_smart_mlr_logic.ltx` (Припять): в отчёте баг на `y05_anomles`
- `all.spawn` (позицию кавера не двигаем)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. `xr_logic` пишет `active_section`; она по-прежнему `animpoint@base`, патч подхватывается на следующем `set_scheme`
- Конфликты: нет пересечения файлов с ZIP v1.0.4 (тот заменял оригинал). В MO2 ниже сборки; ZIP, `Anthology_Grifon_Visual_Test`, `Anthology_Grifon_Animpoint_Bypass_Test` и копию `configs/scripts/anomles/ano_smart_terrain_6_2_smart_logic.ltx` в `[DBG] Kristiano Fixes ALL IN ONE` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_grifon_visibility`
- В игре: не прогонялось. На Аномальном лесу Грифон должен быть виден у своей стены, без lean `stay_wall`. Если модель снова пропадёт — гипотеза «виновата анимация, а не snap кавера» неверна, тогда нужен remark, а не `avail_animations`
