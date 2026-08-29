# Attribute Assistant Crash and Hostility Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_attribute_assistent.script` — ставит `xr_effects.mod_sms_error_task` и CP1251-алиас: `give_game_news` + `pda_tips`, как в блоке attribute-mod.
- `gamedata/configs/scripts/secret_forest/mod_scf_sr_quest_assistent_timer_fix_attribute_assistent.ltx` — DLTX: вызов эффекта переведён на ASCII-имя.
- `mod_scf_n1_assistent_*.ltx`, `mod_scf_d2_assistent_*.ltx` — DLTX: живой `on_infoN` с `actor_neutral` на дочерних схемах.
- `mod_scf_n1_main_logic_*.ltx`, `mod_scf_n1_kosters_logic_*.ltx` — DLTX: безусловный `combat_ignore` на `@def` (наследуют Бес, Лютик, Лёха, костёр) + `actor_neutral` на их активных схемах.
- `cerkov/mod_scf_cerkov_stalker_1..7_*.ltx` — DLTX: `combat_ignore` на `walker@ohrannik`, `actor_neutral` на посте и укрытии от выброса.

**Причина**

После разговора с Ассистентом `scf_sr_quest_assistent_timer` вызывает `mod_sms_error_task_а`. В `xr_effects.script` функтор записан как `this["mod_sms_error_task_à"]` — байт суффикса не совпадает с ключом из LTX. `xr_logic.script:492` вызывает `nil`.

Сталкеры в церкви били Ассистента, потому что:

1. `on_info65` / `on_info6` с `%=actor_neutral%` стояли на родительской секции. `cfg_get_switch_conditions` перечисляет только строки самой секции (`ini:line_count` / `r_line_ex`), унаследованный `on_info` не попадает в список.
2. `combat_ignore_cond = {=fighting_dist_ge(30)} true, {=check_enemy_name(actor)} true, false` игнорирует только игрока. Ассистент — другой NPC, в церкви ближе 30 м, фракции враждебны.

ZIP DreamCatcher_AllFixes подменял 12 LTX целиком и слал SMS через `news_manager.send_tip`.

**Как исправлено**

Не файлы целиком: функтор как в оригинале, вызов — ASCII. Вражда — DLTX на `@def` / `walker@ohrannik`, чтобы наследовалось. `actor_neutral` перенесён на дочерние схемы, которые реально перечисляются. Схемы укрытия от выброса свой `combat_ignore` не теряют.

**Не затронуто**

- `xr_effects.script`, `xr_logic.script`, `all.spawn`
- диалоги Ассистента, спавн, таймер 6199, `scf_assistent_quest_info_time`
- `nikita_to_heli` и hide-схемы костра (свой условный `combat_ignore`)
- локализация `mod_sms_error_task_text` / `st_mod_warning_name`
- остальные карты и квесты Атрибута

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Уже дерущиеся NPC успокоятся на следующей смене/проверке схемы
- Конфликты: нет пересечения файлов с ZIP (тот заменял оригиналы). В MO2 ниже сборки; ZIP DreamCatcher_AllFixes выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_attribute_assistent`
- В игре: не прогонялось. Тайный лес, церковь, диалог с Ассистентом до конца: нет CTD, сталкеры / Бес / Лютик не атакуют Ассистента. После обиды на Ассистента — новость с иконкой ошибки и звук PDA. В логе: `loaded v1.0.0`
