# Карточка лога — newxray_nikit.log

- Файл: `newxray_nikit.log` (4.8 МБ, 72366 строк)
- Дата разбора: 2026-09-19
- Класс: **нативный вылет (не Lua)** — physics `UpdateDynamicDamage` / `InitContact`
- mdmp: `xray_nikit_09-19-26_22-19-50.mdmp`
- Среда: xrCore build 10063, anomalydx11avx.exe

## CTD — нативный AV (физика актора, не Lua FATAL)

До фикса `STACK_RE` в `tools/xraylog.py` строка вида `[22:19:50.005] stack trace:` не ловилась — карточка ошибочно шла как «вылета нет».

- **Когда:** 22:19:50, после лута инвентаря (`Register UI: UIInventory` / DotMarks `block_loot_window` на трупах/NPC, Росток).
- **Класс:** native AV без блока FATAL ERROR (`UnhandledFilter` + `stack trace:` + mdmp).
- **Нативный стек:** `UnhandledFilter` → `CPHSimpleCharacter::UpdateDynamicDamage` → `InitContact` → `CPHActorCharacter::InitContact` → `CollideDynamics` → `PHWorld::Step` → `GameThread`.
- **Не** DrawHint / DoRenderDialogs / ScreenResolution — отдельная сигнатура.
- **Lua FATAL:** нет. Lone `! [LUA]` кадры каждый load — известный FDDA `script_anim_part 255` (issues).

### Нефатальное в той же сессии (не CTD)

- `sound_theme` abort ×2 (1-я загрузка): нет коллекции `scenario/black_valley/blck_val_robbery_scene_come_here_pda`.
- `WTF ERROR` / `fix_wtf_taskboard_guard`: отклонён quest `ghentuongsupply46074` (макрос `gt_guard` / faction) — гард сработал, не FATAL.
- `! ERROR: veh_btr… scheme=ph_car stype=nil` ×4 — отдельно.

## Мои моды

### Не появились в логе (3)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_item_combination_magnifiers`
- `fix_minigun_dead_parent`

### С отказами (5)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[21:41:24.013] [fix_aim_fatigue_visibility] loaded v1.0.2`
- `[21:41:24.013] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:41:25.010] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:41:39.839] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:42:30.654] [fix_aim_fatigue_visibility] loaded v1.0.2`
- `[21:42:30.654] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:42:31.531] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:42:38.382] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:50:48.561] [fix_aim_fatigue_visibility] loaded v1.0.2`
- `[21:50:48.561] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:50:49.424] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:50:56.209] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- … ещё 24 уникальных строк

#### `fix_dotmarks_interact_prompt` — есть отказы

- `[21:41:24.015] [fix_dotmarks_interact_prompt] loaded v1.0.0`
- `[21:41:25.011] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:41:38.998] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:42:30.655] [fix_dotmarks_interact_prompt] loaded v1.0.0`
- `[21:42:31.531] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:42:38.688] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:50:48.562] [fix_dotmarks_interact_prompt] loaded v1.0.0`
- `[21:50:49.424] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:50:56.947] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:54:24.131] [fix_dotmarks_interact_prompt] loaded v1.0.0`
- `[21:54:25.088] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- `[21:54:33.528] [fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- … ещё 15 уникальных строк

#### `fix_nil_crash_guards` — есть отказы

- `[21:41:24.017] [fix_nil_crash_guards] loaded v1.1.1`
- `[21:41:24.017] [fix_nil_crash_guards] cover_tilt: demonized_randomizing_functions already present`
- `[21:41:25.011] [fix_nil_crash_guards] wrapped item_knife.get_condition`
- `[21:41:25.011] [fix_nil_crash_guards] wrapped semenov task_functor targets=2`
- `[21:41:25.011] [fix_nil_crash_guards] se_monster.on_unregister not found - guard NOT installed`
- `[21:41:25.011] [fix_nil_crash_guards] se_stalker.on_unregister not found - guard NOT installed`
- `[21:41:25.011] [fix_nil_crash_guards] wrapped smart_terrain.on_death`
- `[21:41:25.011] [fix_nil_crash_guards] wrapped xr_effects.spawn_intercept_artifact_artifact`
- `[21:41:25.011] [fix_nil_crash_guards] wrapped bind_stalker_ext.actor_on_net_spawn`
- `[21:41:25.011] [fix_nil_crash_guards] wrapped reverse_resolution_list_mcm.cont_vid_mode`
- `[21:41:25.011] [fix_nil_crash_guards] retargeted ui_options vid_mode content slots=1`
- `[21:41:39.225] [fix_nil_crash_guards] se_monster.on_unregister not found - guard NOT installed`
- … ещё 105 уникальных строк

#### `fix_qaw_ammo_nil` — есть отказы

- `[21:41:24.743] [fix_qaw_ammo_nil] loaded v1.0.3`
- `[21:41:24.743] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:41:25.378] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:41:39.950] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:42:31.312] [fix_qaw_ammo_nil] loaded v1.0.3`
- `[21:42:31.312] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:42:31.846] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:42:38.553] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:50:49.206] [fix_qaw_ammo_nil] loaded v1.0.3`
- `[21:50:49.206] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:50:49.740] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- `[21:50:56.623] [fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- … ещё 24 уникальных строк

#### `fix_utjan_mag_skill` — есть отказы

- `[21:41:24.697] [fix_utjan_mag_skill] loaded v1.0.0`
- `[21:41:24.697] [fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`
- `[21:42:31.269] [fix_utjan_mag_skill] loaded v1.0.0`
- `[21:42:31.269] [fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`
- `[21:50:49.165] [fix_utjan_mag_skill] loaded v1.0.0`
- `[21:50:49.165] [fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`
- `[21:54:24.797] [fix_utjan_mag_skill] loaded v1.0.0`
- `[21:54:24.797] [fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`
- `[21:57:40.702] [fix_utjan_mag_skill] loaded v1.0.0`
- `[21:57:40.702] [fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`
- `[22:02:56.558] [fix_utjan_mag_skill] loaded v1.0.0`
- `[22:02:56.558] [fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`
- … ещё 6 уникальных строк

### В логе без отказов (74)

#### `anthology_busyhands_stability_fix` — загрузился

- `[21:41:24.034] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[21:41:24.259] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[21:41:24.745] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[21:41:24.745] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[21:41:24.745] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[21:41:24.746] [BusyHandsFix v0.6.14] get_quickhelp_text replaced via ui_hud_dotmarks (fresh get_maingame, no pcall)`
- `[21:41:24.746] [BusyHandsFix v0.6.14] set_quickhelp_text replaced via ui_hud_dotmarks (fresh get_maingame, no pcall)`
- `[21:41:24.746] [BusyHandsFix v0.6.14] get_quickhelp_text replaced via dotmarks_main (fresh get_maingame, no pcall)`
- `[21:41:24.746] [BusyHandsFix v0.6.14] set_quickhelp_text replaced via dotmarks_main (fresh get_maingame, no pcall)`
- `[21:41:24.746] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[21:41:24.746] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[21:41:24.746] [BusyHandsFix v0.6.12] UIInventory.IsInvOwner patched via ui_inventory.UIInventory (method-level, ui_inventory.script untouched)`
- … ещё 465 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[21:41:24.750] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[21:42:31.319] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[21:50:49.213] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[21:54:24.853] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[21:57:40.752] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `- [22:01:57.838] Callback_Tree | tr: 1 - path: burnshit_inventory_destroy - index: 10`
- `[22:02:56.607] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:12:24.619] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:13:32.666] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:16:32.466] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` — загрузился

- `[21:41:23.647] [campfires_anthology_compat] loaded v1.1.2`
- `[21:41:25.006] [campfires_anthology_compat] trader_autoinject.update wrapped v1.1.2`
- `[21:42:30.366] [campfires_anthology_compat] loaded v1.1.2`
- `[21:42:31.530] [campfires_anthology_compat] trader_autoinject.update wrapped v1.1.2`
- `* [21:42:39.459]  [load-session/lua-callbacks] #10 self=38.58 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:109`
- `[21:50:48.275] [campfires_anthology_compat] loaded v1.1.2`
- `[21:50:49.423] [campfires_anthology_compat] trader_autoinject.update wrapped v1.1.2`
- `[21:54:23.824] [campfires_anthology_compat] loaded v1.1.2`
- `[21:54:25.087] [campfires_anthology_compat] trader_autoinject.update wrapped v1.1.2`
- `* [21:54:33.718]  [load-session/lua-callbacks] #09 self=37.77 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:109`
- `[21:57:39.819] [campfires_anthology_compat] loaded v1.1.2`
- `[21:57:40.968] [campfires_anthology_compat] trader_autoinject.update wrapped v1.1.2`
- … ещё 12 уникальных строк

#### `context_menu_overhaul_anthology` — загрузился

- `[21:41:25.006] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[21:41:39.078] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[21:41:39.080] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [21:41:39.973]  [load-session/lua-callbacks] #05 self=90.10 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `* [21:41:39.973]  [load-session/lua-callbacks] #19 self=2.65 ms source=...1/bin/..\gamedata\scripts\cmo_anthology_bootstrap.script:65`
- `[21:41:40.043] [CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=31 current_tab=1 category=manual target_tab=1 route=current_manual`
- `[21:42:31.530] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[21:42:39.150] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[21:42:39.155] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [21:42:39.459]  [load-session/lua-callbacks] #03 self=103.80 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `* [21:42:39.459]  [load-session/lua-callbacks] #19 self=5.13 ms source=...1/bin/..\gamedata\scripts\cmo_anthology_bootstrap.script:65`
- `[21:50:49.423] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- … ещё 30 уникальных строк

#### `diag_log_spam` — загрузился

- x2 `[21:42:29.437] [diag_log_spam]   [C]: in function '__index'`
- x2 `[21:50:47.364] [diag_log_spam]   [C]: in function '__index'`
- x2 `[21:54:22.786] [diag_log_spam]   [C]: in function '__index'`
- x2 `[21:57:38.909] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:02:54.755] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:12:22.781] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:13:30.826] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:16:30.622] [diag_log_spam]   [C]: in function '__index'`
- `[21:41:22.039] [diag_log_spam] early printe hook`
- `[21:41:22.788] [diag_log_spam] init v1.2.3`
- `[21:41:24.748] [diag_log_spam] loaded v1.2.3 (wrappers active)`
- `[21:42:29.059] [diag_log_spam] early printe hook`
- … ещё 70 уникальных строк

#### `fix_aol_sprint_hud` — загрузился

- `[21:41:24.014] [fix_aol_sprint_hud] loaded v1.0.1`
- `[21:41:25.010] [fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- `[21:42:30.654] [fix_aol_sprint_hud] loaded v1.0.1`
- `[21:42:31.531] [fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- `[21:50:48.561] [fix_aol_sprint_hud] loaded v1.0.1`
- `[21:50:49.424] [fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- `[21:54:24.130] [fix_aol_sprint_hud] loaded v1.0.1`
- `[21:54:25.088] [fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- `[21:57:40.099] [fix_aol_sprint_hud] loaded v1.0.1`
- `[21:57:40.969] [fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- `[22:02:55.960] [fix_aol_sprint_hud] loaded v1.0.1`
- `[22:02:56.819] [fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- … ещё 6 уникальных строк

#### `fix_arena_loadout` — загрузился

- `[21:41:24.014] [fix_arena_loadout] loaded v1.1.1`
- `[21:41:25.010] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[21:42:30.654] [fix_arena_loadout] loaded v1.1.1`
- `[21:42:31.531] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[21:50:48.561] [fix_arena_loadout] loaded v1.1.1`
- `[21:50:49.424] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[21:54:24.131] [fix_arena_loadout] loaded v1.1.1`
- `[21:54:25.088] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[21:57:40.099] [fix_arena_loadout] loaded v1.1.1`
- `[21:57:40.969] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:02:55.960] [fix_arena_loadout] loaded v1.1.1`
- `[22:02:56.819] [fix_arena_loadout] bar_arena_teleport wrapped`
- … ещё 6 уникальных строк

#### `fix_arti_frames_nil` — загрузился

- `[21:41:24.014] [fix_arti_frames_nil] loaded v1.0.3`
- `[21:41:25.010] [fix_arti_frames_nil] guard installed v1.0.3`
- `[21:42:30.654] [fix_arti_frames_nil] loaded v1.0.3`
- `[21:42:31.531] [fix_arti_frames_nil] guard installed v1.0.3`
- `[21:50:48.561] [fix_arti_frames_nil] loaded v1.0.3`
- `[21:50:49.424] [fix_arti_frames_nil] guard installed v1.0.3`
- `[21:54:24.131] [fix_arti_frames_nil] loaded v1.0.3`
- `[21:54:25.088] [fix_arti_frames_nil] guard installed v1.0.3`
- `[21:57:40.099] [fix_arti_frames_nil] loaded v1.0.3`
- `[21:57:40.969] [fix_arti_frames_nil] guard installed v1.0.3`
- `[22:02:55.960] [fix_arti_frames_nil] loaded v1.0.3`
- `[22:02:56.819] [fix_arti_frames_nil] guard installed v1.0.3`
- … ещё 6 уникальных строк

#### `fix_ashot_aw_travel` — загрузился

- `[21:41:24.014] [fix_ashot_aw_travel] loaded v1.0.2`
- `[21:41:25.011] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[21:42:30.654] [fix_ashot_aw_travel] loaded v1.0.2`
- `[21:42:31.531] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[21:50:48.561] [fix_ashot_aw_travel] loaded v1.0.2`
- `[21:50:49.424] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[21:54:24.131] [fix_ashot_aw_travel] loaded v1.0.2`
- `[21:54:25.088] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[21:57:40.100] [fix_ashot_aw_travel] loaded v1.0.2`
- `[21:57:40.969] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[22:02:55.960] [fix_ashot_aw_travel] loaded v1.0.2`
- `[22:02:56.819] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- … ещё 6 уникальных строк

#### `fix_attribute_assistent` — загрузился

- `[21:41:24.014] [fix_attribute_assistent] loaded v1.0.3`
- `[21:41:25.011] [fix_attribute_assistent] loaded v1.0.3`
- `[21:42:30.654] [fix_attribute_assistent] loaded v1.0.3`
- `[21:42:31.531] [fix_attribute_assistent] loaded v1.0.3`
- `[21:50:48.561] [fix_attribute_assistent] loaded v1.0.3`
- `[21:50:49.424] [fix_attribute_assistent] loaded v1.0.3`
- `[21:54:24.131] [fix_attribute_assistent] loaded v1.0.3`
- `[21:54:25.088] [fix_attribute_assistent] loaded v1.0.3`
- `[21:57:40.100] [fix_attribute_assistent] loaded v1.0.3`
- `[21:57:40.969] [fix_attribute_assistent] loaded v1.0.3`
- `[22:02:55.960] [fix_attribute_assistent] loaded v1.0.3`
- `[22:02:56.819] [fix_attribute_assistent] loaded v1.0.3`
- … ещё 6 уникальных строк

#### `fix_aver_darkvalley` — загрузился

- `[21:41:25.011] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[21:41:28.452] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[21:41:28.696] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[21:41:39.320] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[21:41:39.347] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [21:41:39.973]  [load-session/lua-callbacks] #08 self=54.98 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`
- `[21:42:31.531] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[21:42:33.529] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[21:42:33.741] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[21:42:38.529] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[21:42:38.542] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [21:42:39.459]  [load-session/lua-callbacks] #14 self=27.58 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`
- … ещё 42 уникальных строк

#### `fix_charon_red_forest_travel` — загрузился

- `[21:41:24.015] [fix_charon_red_forest_travel] loaded v1.0.2`
- `[21:41:25.011] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[21:42:30.654] [fix_charon_red_forest_travel] loaded v1.0.2`
- `[21:42:31.531] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[21:50:48.561] [fix_charon_red_forest_travel] loaded v1.0.2`
- `[21:50:49.424] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[21:54:24.131] [fix_charon_red_forest_travel] loaded v1.0.2`
- `[21:54:25.088] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[21:57:40.100] [fix_charon_red_forest_travel] loaded v1.0.2`
- `[21:57:40.969] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[22:02:55.960] [fix_charon_red_forest_travel] loaded v1.0.2`
- `[22:02:56.819] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- … ещё 6 уникальных строк

#### `fix_crowkiller_hello` — загрузился

- `[21:41:24.015] [fix_crowkiller_hello] loaded v1.0.1`
- `[21:41:25.011] [fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`
- `[21:42:30.654] [fix_crowkiller_hello] loaded v1.0.1`
- `[21:42:31.531] [fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`
- `[21:50:48.562] [fix_crowkiller_hello] loaded v1.0.1`
- `[21:50:49.424] [fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`
- `[21:54:24.131] [fix_crowkiller_hello] loaded v1.0.1`
- `[21:54:25.088] [fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`
- `[21:57:40.100] [fix_crowkiller_hello] loaded v1.0.1`
- `[21:57:40.969] [fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`
- `[22:02:55.960] [fix_crowkiller_hello] loaded v1.0.1`
- `[22:02:56.819] [fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`
- … ещё 6 уникальных строк

#### `fix_dome_quest` — загрузился

- `[21:41:24.015] [fix_dome_quest] loaded v1.0.0`
- `[21:42:30.655] [fix_dome_quest] loaded v1.0.0`
- `[21:50:48.562] [fix_dome_quest] loaded v1.0.0`
- `[21:54:24.131] [fix_dome_quest] loaded v1.0.0`
- `[21:57:40.100] [fix_dome_quest] loaded v1.0.0`
- `[22:02:55.960] [fix_dome_quest] loaded v1.0.0`
- `[22:12:23.973] [fix_dome_quest] loaded v1.0.0`
- `[22:13:32.022] [fix_dome_quest] loaded v1.0.0`
- `[22:16:31.815] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[21:41:24.015] [fix_dotmarks_dropped_weapon] loaded v1.0.3`
- `[21:41:25.011] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[21:42:30.655] [fix_dotmarks_dropped_weapon] loaded v1.0.3`
- `[21:42:31.531] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[21:50:48.562] [fix_dotmarks_dropped_weapon] loaded v1.0.3`
- `[21:50:49.424] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[21:54:24.131] [fix_dotmarks_dropped_weapon] loaded v1.0.3`
- `[21:54:25.088] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[21:57:40.100] [fix_dotmarks_dropped_weapon] loaded v1.0.3`
- `[21:57:40.969] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[22:02:55.960] [fix_dotmarks_dropped_weapon] loaded v1.0.3`
- `[22:02:56.819] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- … ещё 6 уникальных строк

#### `fix_drx_sl_meet_loop` — загрузился

- `[21:41:24.015] [fix_drx_sl_meet_loop] loaded v1.0.2`
- `[21:41:25.011] [fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`
- `[21:42:30.655] [fix_drx_sl_meet_loop] loaded v1.0.2`
- `[21:42:31.531] [fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`
- `[21:50:48.562] [fix_drx_sl_meet_loop] loaded v1.0.2`
- `[21:50:49.424] [fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`
- `[21:54:24.131] [fix_drx_sl_meet_loop] loaded v1.0.2`
- `[21:54:25.088] [fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`
- `[21:57:40.100] [fix_drx_sl_meet_loop] loaded v1.0.2`
- `[21:57:40.969] [fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`
- `[22:02:55.960] [fix_drx_sl_meet_loop] loaded v1.0.2`
- `[22:02:56.819] [fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`
- … ещё 6 уникальных строк

#### `fix_dynamic_armor_visuals_nil` — загрузился

- `[21:41:24.015] [fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- `[21:41:25.011] [fix_dynamic_armor_visuals_nil] guard installed v1.0.4`
- `[21:42:30.655] [fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- `[21:42:31.531] [fix_dynamic_armor_visuals_nil] guard installed v1.0.4`
- `[21:50:48.562] [fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- `[21:50:49.424] [fix_dynamic_armor_visuals_nil] guard installed v1.0.4`
- `[21:54:24.131] [fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- `[21:54:25.088] [fix_dynamic_armor_visuals_nil] guard installed v1.0.4`
- `[21:57:40.100] [fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- `[21:57:40.969] [fix_dynamic_armor_visuals_nil] guard installed v1.0.4`
- `[22:02:55.960] [fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- `[22:02:56.819] [fix_dynamic_armor_visuals_nil] guard installed v1.0.4`
- … ещё 6 уникальных строк

#### `fix_faction_trade_supply` — загрузился

- `[21:41:24.015] [fix_faction_trade_supply] loaded v1.0.1`
- `[21:41:25.011] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[21:42:30.655] [fix_faction_trade_supply] loaded v1.0.1`
- `[21:42:31.531] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[21:50:48.562] [fix_faction_trade_supply] loaded v1.0.1`
- `[21:50:49.424] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[21:54:24.131] [fix_faction_trade_supply] loaded v1.0.1`
- `[21:54:25.088] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[21:57:40.100] [fix_faction_trade_supply] loaded v1.0.1`
- `[21:57:40.969] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[22:02:55.960] [fix_faction_trade_supply] loaded v1.0.1`
- `[22:02:56.819] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- … ещё 6 уникальных строк

#### `fix_fdda_mcm_paths` — загрузился

- `[21:41:24.015] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[21:42:30.655] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[21:50:48.562] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[21:54:24.131] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[21:57:40.100] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:02:55.960] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:12:23.974] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:13:32.022] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:16:31.816] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- `[21:41:24.015] [fix_fetch_headlamp] loaded v1.0.0`
- `[21:42:30.655] [fix_fetch_headlamp] loaded v1.0.0`
- `[21:50:48.562] [fix_fetch_headlamp] loaded v1.0.0`
- `[21:54:24.132] [fix_fetch_headlamp] loaded v1.0.0`
- `[21:57:40.100] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:02:55.960] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:12:23.974] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:13:32.022] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:16:31.816] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- `[21:41:24.015] [fix_flst_joker_door] loaded v1.0.0`
- `[21:42:30.655] [fix_flst_joker_door] loaded v1.0.0`
- `[21:50:48.562] [fix_flst_joker_door] loaded v1.0.0`
- `[21:54:24.132] [fix_flst_joker_door] loaded v1.0.0`
- `[21:57:40.100] [fix_flst_joker_door] loaded v1.0.0`
- `[22:02:55.961] [fix_flst_joker_door] loaded v1.0.0`
- `[22:12:23.974] [fix_flst_joker_door] loaded v1.0.0`
- `[22:13:32.022] [fix_flst_joker_door] loaded v1.0.0`
- `[22:16:31.816] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- `[21:41:24.016] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[21:42:30.655] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[21:50:48.562] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[21:54:24.132] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[21:57:40.100] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[22:02:55.961] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[22:12:23.974] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[22:13:32.022] [fix_g2x_torch_meshes] loaded v1.0.1`
- `[22:16:31.816] [fix_g2x_torch_meshes] loaded v1.0.1`

#### `fix_gigant_space_restriction` — загрузился

- `[21:41:24.016] [fix_gigant_space_restriction] loaded v1.1.2`
- `[21:41:25.011] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[21:41:25.011] [fix_gigant_space_restriction] loaded v1.1.2`
- `[21:41:28.956] [fix_gigant_space_restriction] quarantine id=42275 name=gigant_strong42275 section=gigant_strong reason=off_level`
- `[21:41:28.974] [fix_gigant_space_restriction] quarantine id=43544 name=gigant_normal43544 section=gigant_normal reason=off_level`
- `[21:41:29.028] [fix_gigant_space_restriction] quarantine id=46932 name=gigant_normal46932 section=gigant_normal reason=off_level`
- `[21:41:29.036] [fix_gigant_space_restriction] quarantine id=47503 name=gigant_strong47503 section=gigant_strong reason=off_level`
- `[21:41:29.070] [fix_gigant_space_restriction] quarantine id=50586 name=gigant_weak50586 section=gigant_weak reason=off_level`
- `[21:41:29.070] [fix_gigant_space_restriction] quarantine id=50587 name=gigant_weak50587 section=gigant_weak reason=off_level`
- `[21:41:29.071] [fix_gigant_space_restriction] quarantine id=50759 name=gigant_normal50759 section=gigant_normal reason=off_level`
- `[21:41:29.072] [fix_gigant_space_restriction] quarantine id=50940 name=gigant_normal50940 section=gigant_normal reason=off_level`
- `[21:41:29.073] [fix_gigant_space_restriction] quarantine id=51084 name=gigant_normal51084 section=gigant_normal reason=off_level`
- … ещё 401 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[21:40:12.674] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[21:40:12.674] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[21:40:15.129] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`
- `[21:42:28.920] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[21:42:28.920] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[21:50:46.816] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[21:50:46.816] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[21:54:22.214] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[21:54:22.214] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[21:57:38.402] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[21:57:38.402] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[22:02:54.241] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- … ещё 7 уникальных строк

#### `fix_grifon_visibility` — загрузился

- `[21:41:24.016] [fix_grifon_visibility] loaded v1.1.0`
- `[21:42:30.655] [fix_grifon_visibility] loaded v1.1.0`
- `[21:50:48.562] [fix_grifon_visibility] loaded v1.1.0`
- `[21:54:24.132] [fix_grifon_visibility] loaded v1.1.0`
- `[21:57:40.100] [fix_grifon_visibility] loaded v1.1.0`
- `[22:02:55.961] [fix_grifon_visibility] loaded v1.1.0`
- `[22:12:23.974] [fix_grifon_visibility] loaded v1.1.0`
- `[22:13:32.022] [fix_grifon_visibility] loaded v1.1.0`
- `[22:16:31.816] [fix_grifon_visibility] loaded v1.1.0`

#### `fix_hip_quest_text` — загрузился

- `[21:41:24.016] [fix_hip_quest_text] loaded v1.0.0`
- `[21:42:30.655] [fix_hip_quest_text] loaded v1.0.0`
- `[21:50:48.562] [fix_hip_quest_text] loaded v1.0.0`
- `[21:54:24.132] [fix_hip_quest_text] loaded v1.0.0`
- `[21:57:40.100] [fix_hip_quest_text] loaded v1.0.0`
- `[22:02:55.961] [fix_hip_quest_text] loaded v1.0.0`
- `[22:12:23.974] [fix_hip_quest_text] loaded v1.0.0`
- `[22:13:32.022] [fix_hip_quest_text] loaded v1.0.0`
- `[22:16:31.816] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- `[21:41:24.016] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[21:42:30.655] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[21:50:48.562] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[21:54:24.132] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[21:57:40.101] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:02:55.961] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:12:23.974] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:13:32.022] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:16:31.816] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_hostage_task_collision` — загрузился

- `[21:41:24.016] [fix_hostage_task_collision] loaded v1.0.0`
- `[21:41:25.011] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[21:42:30.655] [fix_hostage_task_collision] loaded v1.0.0`
- `[21:42:31.531] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[21:50:48.562] [fix_hostage_task_collision] loaded v1.0.0`
- `[21:50:49.424] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[21:54:24.132] [fix_hostage_task_collision] loaded v1.0.0`
- `[21:54:25.088] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[21:57:40.101] [fix_hostage_task_collision] loaded v1.0.0`
- `[21:57:40.969] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[22:02:55.961] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:02:56.819] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- … ещё 6 уникальных строк

#### `fix_indeikam_breeding` — загрузился

- `[21:41:24.016] [fix_indeikam_breeding] loaded v1.1.0`
- `[21:42:30.655] [fix_indeikam_breeding] loaded v1.1.0`
- `[21:50:48.562] [fix_indeikam_breeding] loaded v1.1.0`
- `[21:54:24.132] [fix_indeikam_breeding] loaded v1.1.0`
- `[21:57:40.101] [fix_indeikam_breeding] loaded v1.1.0`
- `[22:02:55.961] [fix_indeikam_breeding] loaded v1.1.0`
- `[22:12:23.974] [fix_indeikam_breeding] loaded v1.1.0`
- `[22:13:32.022] [fix_indeikam_breeding] loaded v1.1.0`
- `[22:16:31.816] [fix_indeikam_breeding] loaded v1.1.0`

#### `fix_kupol_wrong_bone` — загрузился

- `[21:41:25.011] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[21:41:39.032] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `* [21:41:39.973]  [load-session/lua-callbacks] #10 self=42.82 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[21:42:31.531] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[21:42:38.515] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `* [21:42:39.459]  [load-session/lua-callbacks] #12 self=34.17 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[21:50:49.424] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[21:50:56.451] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `* [21:50:57.022]  [load-session/lua-callbacks] #07 self=59.38 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[21:54:25.088] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[21:54:33.520] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `* [21:54:33.718]  [load-session/lua-callbacks] #13 self=28.02 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- … ещё 15 уникальных строк

#### `fix_locked_stash_boxes` — загрузился

- `[21:41:24.016] [fix_locked_stash_boxes] loaded v1.0.1`
- `[21:41:25.011] [fix_locked_stash_boxes] v1.0.1 get_random_stash wrapped`
- `[21:41:25.011] [fix_locked_stash_boxes] loaded v1.0.1`
- `[21:41:44.032] [fix_locked_stash_boxes] repair done locked=0 relocated=0 cleared=0 dropped_pending=0`
- `[21:42:30.655] [fix_locked_stash_boxes] loaded v1.0.1`
- `[21:42:31.531] [fix_locked_stash_boxes] v1.0.1 get_random_stash wrapped`
- `[21:42:31.531] [fix_locked_stash_boxes] loaded v1.0.1`
- `[21:42:43.698] [fix_locked_stash_boxes] repair done locked=0 relocated=0 cleared=0 dropped_pending=0`
- `[21:50:48.562] [fix_locked_stash_boxes] loaded v1.0.1`
- `[21:50:49.424] [fix_locked_stash_boxes] v1.0.1 get_random_stash wrapped`
- `[21:50:49.424] [fix_locked_stash_boxes] loaded v1.0.1`
- `[21:50:59.533] [fix_locked_stash_boxes] repair done locked=0 relocated=0 cleared=0 dropped_pending=0`
- … ещё 24 уникальных строк

#### `fix_loot_space` — загрузился

- `[21:41:24.016] [fix_loot_space] loaded v1.0.2`
- `[21:41:25.011] [fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`
- `[21:42:30.655] [fix_loot_space] loaded v1.0.2`
- `[21:42:31.531] [fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`
- `[21:50:48.563] [fix_loot_space] loaded v1.0.2`
- `[21:50:49.424] [fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`
- `[21:54:24.132] [fix_loot_space] loaded v1.0.2`
- `[21:54:25.088] [fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`
- `[21:57:40.101] [fix_loot_space] loaded v1.0.2`
- `[21:57:40.969] [fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`
- `[22:02:55.961] [fix_loot_space] loaded v1.0.2`
- `[22:02:56.819] [fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`
- … ещё 6 уникальных строк

#### `fix_matches_campfire_softlock` — загрузился

- `[21:41:24.017] [fix_matches_campfire_softlock] loaded v1.0.1`
- `[21:41:25.011] [fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`
- `[21:42:30.656] [fix_matches_campfire_softlock] loaded v1.0.1`
- `[21:42:31.531] [fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`
- `[21:50:48.563] [fix_matches_campfire_softlock] loaded v1.0.1`
- `[21:50:49.424] [fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`
- `[21:54:24.132] [fix_matches_campfire_softlock] loaded v1.0.1`
- `[21:54:25.088] [fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`
- `[21:57:40.101] [fix_matches_campfire_softlock] loaded v1.0.1`
- `[21:57:40.969] [fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`
- `[22:02:55.961] [fix_matches_campfire_softlock] loaded v1.0.1`
- `[22:02:56.819] [fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`
- … ещё 6 уникальных строк

#### `fix_melee_trade_supplies` — загрузился

- `[21:41:24.017] [fix_melee_trade_supplies] loaded v1.0.1`
- `[21:41:25.011] [fix_melee_trade_supplies] wrapped melee_trade_inject.vks_spawn_stock`
- `[21:42:30.656] [fix_melee_trade_supplies] loaded v1.0.1`
- `[21:42:31.531] [fix_melee_trade_supplies] wrapped melee_trade_inject.vks_spawn_stock`
- `[21:50:48.563] [fix_melee_trade_supplies] loaded v1.0.1`
- `[21:50:49.424] [fix_melee_trade_supplies] wrapped melee_trade_inject.vks_spawn_stock`
- `[21:54:24.132] [fix_melee_trade_supplies] loaded v1.0.1`
- `[21:54:25.088] [fix_melee_trade_supplies] wrapped melee_trade_inject.vks_spawn_stock`
- `[21:57:40.101] [fix_melee_trade_supplies] loaded v1.0.1`
- `[21:57:40.969] [fix_melee_trade_supplies] wrapped melee_trade_inject.vks_spawn_stock`
- `[22:02:55.961] [fix_melee_trade_supplies] loaded v1.0.1`
- `[22:02:56.819] [fix_melee_trade_supplies] wrapped melee_trade_inject.vks_spawn_stock`
- … ещё 7 уникальных строк

#### `fix_milspec_exo_craft` — загрузился

- `[21:41:24.017] [fix_milspec_exo_craft] loaded v1.0.4`
- `[21:41:25.011] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.4`
- `[21:42:30.656] [fix_milspec_exo_craft] loaded v1.0.4`
- `[21:42:31.531] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.4`
- `[21:45:24.914] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[21:50:48.563] [fix_milspec_exo_craft] loaded v1.0.4`
- `[21:50:49.424] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.4`
- `[21:54:24.132] [fix_milspec_exo_craft] loaded v1.0.4`
- `[21:54:25.089] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.4`
- `[21:55:02.671] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[21:57:40.101] [fix_milspec_exo_craft] loaded v1.0.4`
- `[21:57:40.970] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.4`
- … ещё 12 уникальных строк

#### `fix_misc_script_errors` — загрузился

- `[21:40:12.674] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[21:40:25.739] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[21:41:24.017] [fix_misc_script_errors] loaded v1.0.4`
- `[21:41:25.011] [fix_misc_script_errors] loaded v1.0.4 wrapped mas_scope_detach.on_game_start`
- `[21:41:39.088] [fix_misc_script_errors] wrapped existing mas_scope_detach after_move (late)`
- `[21:42:28.920] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[21:42:30.656] [fix_misc_script_errors] loaded v1.0.4`
- `[21:42:31.531] [fix_misc_script_errors] loaded v1.0.4 wrapped mas_scope_detach.on_game_start`
- `[21:42:38.420] [fix_misc_script_errors] wrapped existing mas_scope_detach after_move (late)`
- `[21:50:46.816] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[21:50:48.563] [fix_misc_script_errors] loaded v1.0.4`
- `[21:50:49.424] [fix_misc_script_errors] loaded v1.0.4 wrapped mas_scope_detach.on_game_start`
- … ещё 25 уникальных строк

#### `fix_nimble_order_desc` — загрузился

- `[21:41:24.017] [fix_nimble_order_desc] loaded v1.0.0`
- `[21:42:30.656] [fix_nimble_order_desc] loaded v1.0.0`
- `[21:50:48.563] [fix_nimble_order_desc] loaded v1.0.0`
- `[21:54:24.133] [fix_nimble_order_desc] loaded v1.0.0`
- `[21:57:40.101] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:02:55.962] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:12:23.975] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:13:32.023] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:16:31.817] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- `[21:41:24.017] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:41:25.011] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:42:30.656] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:42:31.531] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:50:48.563] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:50:49.424] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:54:24.133] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:54:25.089] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:57:40.101] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:57:40.970] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:02:55.962] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:02:56.819] [fix_noosphere_voice_x18] loaded v1.0.1`
- … ещё 6 уникальных строк

#### `fix_nta_stashes` — загрузился

- `[21:41:24.018] [fix_nta_stashes] loaded v1.0.1`
- `[21:41:25.011] [fix_nta_stashes] v1.0.1 populate wrapped`
- `[21:41:25.011] [fix_nta_stashes] callbacks registered v1.0.1`
- `[21:42:30.656] [fix_nta_stashes] loaded v1.0.1`
- `[21:42:31.531] [fix_nta_stashes] v1.0.1 populate wrapped`
- `[21:42:31.531] [fix_nta_stashes] callbacks registered v1.0.1`
- `[21:50:48.563] [fix_nta_stashes] loaded v1.0.1`
- `[21:50:49.424] [fix_nta_stashes] v1.0.1 populate wrapped`
- `[21:50:49.424] [fix_nta_stashes] callbacks registered v1.0.1`
- `[21:54:24.133] [fix_nta_stashes] loaded v1.0.1`
- `[21:54:25.089] [fix_nta_stashes] v1.0.1 populate wrapped`
- `[21:54:25.089] [fix_nta_stashes] callbacks registered v1.0.1`
- … ещё 15 уникальных строк

#### `fix_okrest_texnik_dialog` — загрузился

- `[21:41:24.018] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[21:42:30.656] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[21:50:48.563] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[21:54:24.133] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[21:57:40.101] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:02:55.962] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:12:23.975] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:13:32.023] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:16:31.817] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[21:41:24.018] [fix_pda_buyinfo_gui] loaded v1.1.3`
- `[21:41:25.011] [fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`
- `[21:42:30.656] [fix_pda_buyinfo_gui] loaded v1.1.3`
- `[21:42:31.531] [fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`
- `[21:50:48.563] [fix_pda_buyinfo_gui] loaded v1.1.3`
- `[21:50:49.424] [fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`
- `[21:54:24.133] [fix_pda_buyinfo_gui] loaded v1.1.3`
- `[21:54:25.089] [fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`
- `[21:57:40.102] [fix_pda_buyinfo_gui] loaded v1.1.3`
- `[21:57:40.970] [fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`
- `[22:02:55.962] [fix_pda_buyinfo_gui] loaded v1.1.3`
- `[22:02:56.819] [fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`
- … ещё 6 уникальных строк

#### `fix_ph_door_rx_reload` — загрузился

- `[21:41:24.018] [fix_ph_door_rx_reload] loaded v1.0.2`
- `[21:41:25.011] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped ph_door.try_to_open/close`
- `[21:41:25.011] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped rx_ai.enable_schemes`
- `[21:42:30.656] [fix_ph_door_rx_reload] loaded v1.0.2`
- `[21:42:31.531] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped ph_door.try_to_open/close`
- `[21:42:31.531] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped rx_ai.enable_schemes`
- `[21:50:48.563] [fix_ph_door_rx_reload] loaded v1.0.2`
- `[21:50:49.424] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped ph_door.try_to_open/close`
- `[21:50:49.424] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped rx_ai.enable_schemes`
- `[21:54:24.133] [fix_ph_door_rx_reload] loaded v1.0.2`
- `[21:54:25.089] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped ph_door.try_to_open/close`
- `[21:54:25.089] [fix_ph_door_rx_reload] loaded v1.0.2 wrapped rx_ai.enable_schemes`
- … ещё 15 уникальных строк

#### `fix_quest_item_shared_fail` — загрузился

- `[21:41:24.018] [fix_quest_item_shared_fail] loaded v1.3.2`
- `[21:41:25.011] [fix_quest_item_shared_fail] v1.3.2 status wrapped`
- `[21:41:25.011] [fix_quest_item_shared_fail] loaded ok v1.3.2`
- `[21:42:30.656] [fix_quest_item_shared_fail] loaded v1.3.2`
- `[21:42:31.531] [fix_quest_item_shared_fail] v1.3.2 status wrapped`
- `[21:42:31.532] [fix_quest_item_shared_fail] loaded ok v1.3.2`
- `[21:50:48.564] [fix_quest_item_shared_fail] loaded v1.3.2`
- `[21:50:49.424] [fix_quest_item_shared_fail] v1.3.2 status wrapped`
- `[21:50:49.424] [fix_quest_item_shared_fail] loaded ok v1.3.2`
- `[21:54:24.133] [fix_quest_item_shared_fail] loaded v1.3.2`
- `[21:54:25.089] [fix_quest_item_shared_fail] v1.3.2 status wrapped`
- `[21:54:25.089] [fix_quest_item_shared_fail] loaded ok v1.3.2`
- … ещё 15 уникальных строк

#### `fix_quest_stash` — есть строки

- `[21:41:24.018] [fix_quest_stash] загружен v1.0.6`
- `[21:41:25.011] [fix_quest_stash] v1.0.6 status-функтор обёрнут`
- `[21:41:25.011] [fix_quest_stash] загружен v1.0.6 section drx_sl_quest_item_1014 exist=yes`
- `[21:42:30.657] [fix_quest_stash] загружен v1.0.6`
- `[21:42:31.532] [fix_quest_stash] v1.0.6 status-функтор обёрнут`
- `[21:42:31.532] [fix_quest_stash] загружен v1.0.6 section drx_sl_quest_item_1014 exist=yes`
- `[21:50:48.564] [fix_quest_stash] загружен v1.0.6`
- `[21:50:49.424] [fix_quest_stash] v1.0.6 status-функтор обёрнут`
- `[21:50:49.424] [fix_quest_stash] загружен v1.0.6 section drx_sl_quest_item_1014 exist=yes`
- `[21:54:24.133] [fix_quest_stash] загружен v1.0.6`
- `[21:54:25.089] [fix_quest_stash] v1.0.6 status-функтор обёрнут`
- `[21:54:25.089] [fix_quest_stash] загружен v1.0.6 section drx_sl_quest_item_1014 exist=yes`
- … ещё 15 уникальных строк

#### `fix_quest_story_id` — загрузился

- `[21:41:24.018] [fix_quest_story_id] loaded v1.0.3`
- `[21:41:25.011] [fix_quest_story_id] v1.0.3 register() wrapped`
- `[21:41:25.011] [fix_quest_story_id] loaded v1.0.3`
- `[21:41:28.397] [fix_quest_story_id] ignored duplicate object 2718 for story_id esc_village_zona_quest`
- `[21:41:28.398] [fix_quest_story_id] ignored duplicate object 2750 for story_id esc_zone_atp_all`
- `[21:41:28.639] [fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- `[21:41:29.077] [fix_quest_story_id] kept first object 45078 for repeated story_id jup_a9_dogs_normal`
- `[21:41:38.871] [fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- `[21:41:38.873] [fix_quest_story_id] selected object 24424 for story_id main_story_19_aver_documents (replaced 24425)`
- `[21:41:38.874] [fix_quest_story_id] selected object 24937 for story_id main_story_14_sci_documents (replaced 24938)`
- `[21:41:38.875] [fix_quest_story_id] selected object 26197 for story_id main_story_16_kas_documents (replaced 26198)`
- `[21:41:38.875] [fix_quest_story_id] selected object 26456 for story_id main_story_17_country_documents (replaced 26457)`
- … ещё 114 уникальных строк

#### `fix_radio` — загрузился

- `[21:41:24.019] [fix_radio] loaded v1.0.7`
- `[21:41:25.011] [fix_radio] loaded v1.0.7`
- `[21:42:30.657] [fix_radio] loaded v1.0.7`
- `[21:42:31.532] [fix_radio] loaded v1.0.7`
- `[21:50:48.564] [fix_radio] loaded v1.0.7`
- `[21:50:49.425] [fix_radio] loaded v1.0.7`
- `[21:54:24.134] [fix_radio] loaded v1.0.7`
- `[21:54:25.089] [fix_radio] loaded v1.0.7`
- `[21:57:40.102] [fix_radio] loaded v1.0.7`
- `[21:57:40.970] [fix_radio] loaded v1.0.7`
- `[22:02:55.963] [fix_radio] loaded v1.0.7`
- `[22:02:56.820] [fix_radio] loaded v1.0.7`
- … ещё 6 уникальных строк

#### `fix_replace_quest_corpse` — загрузился

- `[21:41:24.019] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:41:24.019] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[21:41:25.011] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:42:30.657] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:42:30.657] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[21:42:31.532] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:50:48.564] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:50:48.564] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[21:50:49.425] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:54:24.134] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:54:24.134] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[21:54:25.089] [fix_replace_quest_corpse] loaded v1.0.1`
- … ещё 15 уникальных строк

#### `fix_rogue_hostility` — загрузился

- `[21:41:25.011] [fix_rogue_hostility] loaded v1.0.0`
- `[21:42:31.532] [fix_rogue_hostility] loaded v1.0.0`
- `[21:50:49.425] [fix_rogue_hostility] loaded v1.0.0`
- `[21:54:25.089] [fix_rogue_hostility] loaded v1.0.0`
- `[21:57:40.970] [fix_rogue_hostility] loaded v1.0.0`
- `[22:02:56.820] [fix_rogue_hostility] loaded v1.0.0`
- `[22:12:24.829] [fix_rogue_hostility] loaded v1.0.0`
- `[22:13:32.877] [fix_rogue_hostility] loaded v1.0.0`
- `[22:16:32.675] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[21:41:24.019] [fix_rx_bandage_dead] loaded v1.0.2`
- `[21:41:25.011] [fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`
- `[21:42:30.657] [fix_rx_bandage_dead] loaded v1.0.2`
- `[21:42:31.532] [fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`
- `[21:50:48.564] [fix_rx_bandage_dead] loaded v1.0.2`
- `[21:50:49.425] [fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`
- `[21:54:24.134] [fix_rx_bandage_dead] loaded v1.0.2`
- `[21:54:25.089] [fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`
- `[21:57:40.102] [fix_rx_bandage_dead] loaded v1.0.2`
- `[21:57:40.970] [fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`
- `[22:02:55.963] [fix_rx_bandage_dead] loaded v1.0.2`
- `[22:02:56.820] [fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`
- … ещё 6 уникальных строк

#### `fix_sim_mechanic_trade` — загрузился

- `[21:41:24.019] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[21:42:30.657] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[21:50:48.564] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[21:54:24.134] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[21:57:40.102] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[22:02:55.963] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[22:12:23.976] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[22:13:32.024] [fix_sim_mechanic_trade] loaded v1.0.3`
- `[22:16:31.818] [fix_sim_mechanic_trade] loaded v1.0.3`

#### `fix_sim_medic_task_dialog` — загрузился

- `[21:41:24.019] [fix_sim_medic_task_dialog] loaded v1.0.3`
- `[21:41:25.011] [fix_sim_medic_task_dialog] ordered finish fallback -> sim installed`
- `[21:41:25.011] [fix_sim_medic_task_dialog] callback installed`
- `[21:42:30.657] [fix_sim_medic_task_dialog] loaded v1.0.3`
- `[21:42:31.532] [fix_sim_medic_task_dialog] ordered finish fallback -> sim installed`
- `[21:42:31.532] [fix_sim_medic_task_dialog] callback installed`
- `[21:50:48.564] [fix_sim_medic_task_dialog] loaded v1.0.3`
- `[21:50:49.425] [fix_sim_medic_task_dialog] ordered finish fallback -> sim installed`
- `[21:50:49.425] [fix_sim_medic_task_dialog] callback installed`
- `[21:54:24.134] [fix_sim_medic_task_dialog] loaded v1.0.3`
- `[21:54:25.089] [fix_sim_medic_task_dialog] ordered finish fallback -> sim installed`
- `[21:54:25.089] [fix_sim_medic_task_dialog] callback installed`
- … ещё 15 уникальных строк

#### `fix_smart_terrain_state_write` — загрузился

- `[21:41:24.020] [fix_smart_terrain_state_write] loaded v1.0.3`
- `[21:41:25.011] [fix_smart_terrain_state_write] guard installed v1.0.3`
- `[21:42:30.657] [fix_smart_terrain_state_write] loaded v1.0.3`
- `[21:42:31.532] [fix_smart_terrain_state_write] guard installed v1.0.3`
- `[21:50:48.564] [fix_smart_terrain_state_write] loaded v1.0.3`
- `[21:50:49.425] [fix_smart_terrain_state_write] guard installed v1.0.3`
- `[21:54:24.134] [fix_smart_terrain_state_write] loaded v1.0.3`
- `[21:54:25.089] [fix_smart_terrain_state_write] guard installed v1.0.3`
- `[21:57:40.103] [fix_smart_terrain_state_write] loaded v1.0.3`
- `[21:57:40.970] [fix_smart_terrain_state_write] guard installed v1.0.3`
- `[22:02:55.963] [fix_smart_terrain_state_write] loaded v1.0.3`
- `[22:02:56.820] [fix_smart_terrain_state_write] guard installed v1.0.3`
- … ещё 6 уникальных строк

#### `fix_soc_nimble_flash` — загрузился

- `[21:41:24.020] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:41:25.011] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:42:30.657] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:42:31.532] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:50:48.564] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:50:49.425] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:54:24.134] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:54:25.089] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:57:40.103] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:57:40.970] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:02:55.963] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:02:56.820] [fix_soc_nimble_flash] loaded v1.0.1`
- … ещё 6 уникальных строк

#### `fix_sort_tabs` — загрузился

- `[21:41:24.020] [fix_sort_tabs] loaded v1.0.0`
- `[21:42:30.657] [fix_sort_tabs] loaded v1.0.0`
- `[21:50:48.564] [fix_sort_tabs] loaded v1.0.0`
- `[21:54:24.134] [fix_sort_tabs] loaded v1.0.0`
- `[21:57:40.103] [fix_sort_tabs] loaded v1.0.0`
- `[22:02:55.963] [fix_sort_tabs] loaded v1.0.0`
- `[22:12:23.976] [fix_sort_tabs] loaded v1.0.0`
- `[22:13:32.024] [fix_sort_tabs] loaded v1.0.0`
- `[22:16:31.818] [fix_sort_tabs] loaded v1.0.0`

#### `fix_sound_object_missing` — загрузился

- `[21:41:24.020] [fix_sound_object_missing] loaded v1.0.2`
- `[21:41:24.020] [fix_sound_object_missing] sound_object proxy installed v1.0.2`
- `[21:41:25.011] [fix_sound_object_missing] xr_sound.get_safe_sound_object wrapped`
- `[21:42:30.657] [fix_sound_object_missing] loaded v1.0.2`
- `[21:42:30.657] [fix_sound_object_missing] sound_object proxy installed v1.0.2`
- `[21:42:31.532] [fix_sound_object_missing] xr_sound.get_safe_sound_object wrapped`
- `[21:48:27.767] [fix_sound_object_missing] skip missing sound path=tb_growls\tb_growl_5 (unique=1 total_skips=1)`
- `[21:48:31.315] [fix_sound_object_missing] skip missing sound path=tb_growls\tb_growl_1 (unique=2 total_skips=2)`
- `[21:48:34.006] [fix_sound_object_missing] skip missing sound path=tb_growls\tb_growl_6 (unique=3 total_skips=3)`
- `[21:48:38.000] [fix_sound_object_missing] skip missing sound path=tb_growls\tb_growl_3 (unique=4 total_skips=4)`
- `[21:48:42.511] [fix_sound_object_missing] skip missing sound path=tb_growls\tb_growl_4 (unique=5 total_skips=5)`
- `[21:48:56.503] [fix_sound_object_missing] skip missing sound path=tb_growls\tb_growl_8 (unique=6 total_skips=9)`
- … ещё 32 уникальных строк

#### `fix_st2_footstep` — загрузился

- `[21:41:24.020] [fix_st2_footstep] loaded v1.0.0`
- `[21:42:30.657] [fix_st2_footstep] loaded v1.0.0`
- `[21:50:48.564] [fix_st2_footstep] loaded v1.0.0`
- `[21:54:24.134] [fix_st2_footstep] loaded v1.0.0`
- `[21:57:40.103] [fix_st2_footstep] loaded v1.0.0`
- `[22:02:55.963] [fix_st2_footstep] loaded v1.0.0`
- `[22:12:23.976] [fix_st2_footstep] loaded v1.0.0`
- `[22:13:32.025] [fix_st2_footstep] loaded v1.0.0`
- `[22:16:31.818] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stale_fetch_marker` — загрузился

- `[21:41:24.020] [fix_stale_fetch_marker] loaded v1.0.3`
- `[21:41:25.011] [fix_stale_fetch_marker] installed v1.0.3`
- `[21:41:39.789] [fix_stale_fetch_marker] sweep reason=actor_on_first_update pstors=1 probed=0 cleared=0 task_info=true`
- `[21:41:44.036] [fix_stale_fetch_marker] sweep reason=delayed pstors=1 probed=0 cleared=0 task_info=true`
- `[21:42:22.690] [fix_stale_fetch_marker] sweep reason=on_before_level_changing pstors=1 probed=0 cleared=0 task_info=true`
- `[21:42:30.657] [fix_stale_fetch_marker] loaded v1.0.3`
- `[21:42:31.532] [fix_stale_fetch_marker] installed v1.0.3`
- `[21:42:39.457] [fix_stale_fetch_marker] sweep reason=actor_on_first_update pstors=1 probed=0 cleared=0 task_info=true`
- `[21:42:43.698] [fix_stale_fetch_marker] sweep reason=delayed pstors=1 probed=0 cleared=0 task_info=true`
- `[21:50:41.474] [fix_stale_fetch_marker] sweep reason=on_before_level_changing pstors=1 probed=0 cleared=0 task_info=true`
- `[21:50:48.565] [fix_stale_fetch_marker] loaded v1.0.3`
- `[21:50:49.425] [fix_stale_fetch_marker] installed v1.0.3`
- … ещё 31 уникальных строк

#### `fix_stash_id_desync` — загрузился

- `[21:41:25.011] [fix_stash_id_desync] v1.0.3 release_stash_by_id wrapped`
- `[21:41:25.011] [fix_stash_id_desync] loaded v1.0.3`
- `[21:41:46.632] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[21:42:31.532] [fix_stash_id_desync] v1.0.3 release_stash_by_id wrapped`
- `[21:42:31.532] [fix_stash_id_desync] loaded v1.0.3`
- `[21:42:45.300] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[21:50:49.425] [fix_stash_id_desync] v1.0.3 release_stash_by_id wrapped`
- `[21:50:49.425] [fix_stash_id_desync] loaded v1.0.3`
- `[21:50:59.818] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[21:54:25.089] [fix_stash_id_desync] v1.0.3 release_stash_by_id wrapped`
- `[21:54:25.089] [fix_stash_id_desync] loaded v1.0.3`
- `[21:54:40.726] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- … ещё 15 уникальных строк

#### `fix_talents_pda_respec` — загрузился

- `[21:41:24.020] [fix_talents_pda_respec] loaded v1.0.2`
- `[21:41:25.011] [fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`
- `[21:42:30.658] [fix_talents_pda_respec] loaded v1.0.2`
- `[21:42:31.532] [fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`
- `[21:50:48.565] [fix_talents_pda_respec] loaded v1.0.2`
- `[21:50:49.425] [fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`
- `[21:54:24.134] [fix_talents_pda_respec] loaded v1.0.2`
- `[21:54:25.089] [fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`
- `[21:57:40.103] [fix_talents_pda_respec] loaded v1.0.2`
- `[21:57:40.970] [fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`
- `[22:02:55.963] [fix_talents_pda_respec] loaded v1.0.2`
- `[22:02:56.820] [fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`
- … ещё 6 уникальных строк

#### `fix_trade_craft_stock` — загрузился

- `[21:41:24.020] [fix_trade_craft_stock] loaded v1.0.0`
- `[21:42:30.658] [fix_trade_craft_stock] loaded v1.0.0`
- `[21:50:48.565] [fix_trade_craft_stock] loaded v1.0.0`
- `[21:54:24.134] [fix_trade_craft_stock] loaded v1.0.0`
- `[21:57:40.103] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:02:55.963] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:12:23.977] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:13:32.025] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:16:31.819] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- `[21:41:22.789] [fix_trader_restock_callback] trader_on_restock exists v1.0.5`
- `[21:41:24.748] [fix_trader_restock_callback] trader_on_restock added v1.0.5`
- `[21:41:24.748] [fix_trader_restock_callback] Send wrap installed`
- `[21:42:29.446] [fix_trader_restock_callback] trader_on_restock added v1.0.5`
- `[21:42:31.318] [fix_trader_restock_callback] Send wrap installed`
- `[21:50:47.372] [fix_trader_restock_callback] trader_on_restock added v1.0.5`
- `[21:50:49.212] [fix_trader_restock_callback] Send wrap installed`
- `[21:54:22.796] [fix_trader_restock_callback] trader_on_restock added v1.0.5`
- `[21:54:24.851] [fix_trader_restock_callback] Send wrap installed`
- `[21:57:38.918] [fix_trader_restock_callback] trader_on_restock added v1.0.5`
- `[21:57:40.750] [fix_trader_restock_callback] Send wrap installed`
- `[22:02:54.763] [fix_trader_restock_callback] trader_on_restock added v1.0.5`
- … ещё 7 уникальных строк

#### `fix_travel_invalid_id` — загрузился

- `[21:41:24.021] [fix_travel_invalid_id] loaded v1.0.1`
- `[21:41:25.011] [fix_travel_invalid_id] RegisterScriptCallback hook installed v1.0.1`
- `[21:41:39.954] [fix_travel_invalid_id] late-wrapped 4 travel callback(s)`
- `[21:42:30.658] [fix_travel_invalid_id] loaded v1.0.1`
- `[21:42:31.532] [fix_travel_invalid_id] RegisterScriptCallback hook installed v1.0.1`
- `[21:42:38.884] [fix_travel_invalid_id] late-wrapped 4 travel callback(s)`
- `[21:50:48.565] [fix_travel_invalid_id] loaded v1.0.1`
- `[21:50:49.425] [fix_travel_invalid_id] RegisterScriptCallback hook installed v1.0.1`
- `[21:50:56.830] [fix_travel_invalid_id] late-wrapped 4 travel callback(s)`
- `[21:54:24.135] [fix_travel_invalid_id] loaded v1.0.1`
- `[21:54:25.089] [fix_travel_invalid_id] RegisterScriptCallback hook installed v1.0.1`
- `[21:54:32.742] [fix_travel_invalid_id] late-wrapped 4 travel callback(s)`
- … ещё 15 уникальных строк

#### `fix_vows_ambush_stash` — загрузился

- `[21:41:24.021] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:41:25.011] [fix_vows_ambush_stash] v1.0.2 activate_by_section wrapped`
- `[21:41:25.011] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:42:30.658] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:42:31.532] [fix_vows_ambush_stash] v1.0.2 activate_by_section wrapped`
- `[21:42:31.532] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:50:48.565] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:50:49.425] [fix_vows_ambush_stash] v1.0.2 activate_by_section wrapped`
- `[21:50:49.425] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:54:24.135] [fix_vows_ambush_stash] loaded v1.0.2`
- `[21:54:25.089] [fix_vows_ambush_stash] v1.0.2 activate_by_section wrapped`
- `[21:54:25.089] [fix_vows_ambush_stash] loaded v1.0.2`
- … ещё 15 уникальных строк

#### `fix_wtf_assault_instacomplete` — загрузился

- `[21:41:24.021] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:41:25.011] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:42:30.658] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:42:31.532] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:50:48.565] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:50:49.425] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:54:24.135] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:54:25.089] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:57:40.103] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[21:57:40.970] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[22:02:55.964] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- `[22:02:56.820] [fix_wtf_assault_instacomplete] loaded v1.0.3`
- … ещё 6 уникальных строк

#### `fix_wtf_fetch_counter` — загрузился

- `[21:41:24.021] [fix_wtf_fetch_counter] loaded v1.0.1`
- `[21:41:25.011] [fix_wtf_fetch_counter] installed v1.0.1`
- `[21:42:30.658] [fix_wtf_fetch_counter] loaded v1.0.1`
- `[21:42:31.532] [fix_wtf_fetch_counter] installed v1.0.1`
- `[21:50:48.565] [fix_wtf_fetch_counter] loaded v1.0.1`
- `[21:50:49.425] [fix_wtf_fetch_counter] installed v1.0.1`
- `[21:54:24.135] [fix_wtf_fetch_counter] loaded v1.0.1`
- `[21:54:25.089] [fix_wtf_fetch_counter] installed v1.0.1`
- `[21:57:40.103] [fix_wtf_fetch_counter] loaded v1.0.1`
- `[21:57:40.970] [fix_wtf_fetch_counter] installed v1.0.1`
- `[22:02:55.964] [fix_wtf_fetch_counter] loaded v1.0.1`
- `[22:02:56.820] [fix_wtf_fetch_counter] installed v1.0.1`
- … ещё 6 уникальных строк

#### `fix_wtf_taskboard_guard` — загрузился

- x2 `...1/bin/..\gamedata\scripts\fix_wtf_taskboard_guard.script:156: quest=ghentuongsupply46074; entity=enemy; macro=$ igi_helper.db_ini:r_value('gt_guard', |this.faction|); expression= igi_helper.db_ini:r_value('gt_guard', `
- `[21:41:24.021] [fix_wtf_taskboard_guard] loaded v1.0.3`
- `[21:41:25.011] [fix_wtf_taskboard_guard] loaded v1.0.3 wrapped=9 missing=0`
- `[21:42:30.658] [fix_wtf_taskboard_guard] loaded v1.0.3`
- `[21:42:31.532] [fix_wtf_taskboard_guard] loaded v1.0.3 wrapped=9 missing=0`
- `[21:50:48.565] [fix_wtf_taskboard_guard] loaded v1.0.3`
- `[21:50:49.425] [fix_wtf_taskboard_guard] loaded v1.0.3 wrapped=9 missing=0`
- `[21:54:24.135] [fix_wtf_taskboard_guard] loaded v1.0.3`
- `[21:54:25.089] [fix_wtf_taskboard_guard] loaded v1.0.3 wrapped=9 missing=0`
- `[21:57:40.103] [fix_wtf_taskboard_guard] loaded v1.0.3`
- `[21:57:40.970] [fix_wtf_taskboard_guard] loaded v1.0.3 wrapped=9 missing=0`
- `[22:02:55.964] [fix_wtf_taskboard_guard] loaded v1.0.3`
- … ещё 10 уникальных строк

#### `fix_x15_freeplay_gate` — загрузился

- `[21:41:24.021] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[21:42:30.658] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[21:50:48.565] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[21:54:24.135] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[21:57:40.103] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:02:55.964] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:12:23.977] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:13:32.025] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:16:31.819] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- `[21:41:24.022] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:41:25.011] [fix_x2_gravity_room] bas_no_gravity_anomaly bound v1.0.2`
- `[21:41:25.011] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:42:30.658] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:42:31.532] [fix_x2_gravity_room] bas_no_gravity_anomaly bound v1.0.2`
- `[21:42:31.532] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:50:48.565] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:50:49.425] [fix_x2_gravity_room] bas_no_gravity_anomaly bound v1.0.2`
- `[21:50:49.425] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:54:24.135] [fix_x2_gravity_room] loaded v1.0.2`
- `[21:54:25.089] [fix_x2_gravity_room] bas_no_gravity_anomaly bound v1.0.2`
- `[21:54:25.089] [fix_x2_gravity_room] loaded v1.0.2`
- … ещё 15 уникальных строк

#### `fix_xr_effects_sounds` — загрузился

- `[21:41:25.011] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[21:42:31.532] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[21:50:49.425] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[21:54:25.089] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[21:57:40.970] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:02:56.820] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:12:24.829] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:13:32.877] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:16:32.676] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- `[21:41:24.022] [fix_zat_b12_box] loaded v1.0.0`
- `[21:42:30.658] [fix_zat_b12_box] loaded v1.0.0`
- `[21:50:48.565] [fix_zat_b12_box] loaded v1.0.0`
- `[21:54:24.135] [fix_zat_b12_box] loaded v1.0.0`
- `[21:57:40.104] [fix_zat_b12_box] loaded v1.0.0`
- `[22:02:55.964] [fix_zat_b12_box] loaded v1.0.0`
- `[22:12:23.977] [fix_zat_b12_box] loaded v1.0.0`
- `[22:13:32.025] [fix_zat_b12_box] loaded v1.0.0`
- `[22:16:31.819] [fix_zat_b12_box] loaded v1.0.0`

#### `kristiano_kx1_exo` — загрузился

- `[21:41:24.243] [kristiano_kx1_exo] loaded v1.5.5-b`
- `[21:41:24.743] [kristiano_kx1_toxic_air] loaded v1.1.0`
- `[21:41:25.090] [kristiano_kx1_exo] LoadRecipesLTX wrap (re)installed v1.5.5-b`
- `[21:41:25.090] [kristiano_kx1_exo] hooks installed v1.5.5-b`
- `[21:41:25.090] [kristiano_kx1_exo] KX-1 servo preset wrapped (quieter / lower pitch)`
- `[21:41:25.378] [kristiano_kx1_toxic_air] WARN: toxic_air.tank_in_belt missing`
- `[21:41:39.090] [kristiano_kx1_toxic_air] WARN: toxic_air.tank_in_belt missing`
- `[21:42:30.890] [kristiano_kx1_exo] loaded v1.5.5-b`
- `[21:42:31.312] [kristiano_kx1_toxic_air] loaded v1.1.0`
- `[21:42:31.565] [kristiano_kx1_exo] LoadRecipesLTX wrap (re)installed v1.5.5-b`
- `[21:42:31.565] [kristiano_kx1_exo] hooks installed v1.5.5-b`
- `[21:42:31.565] [kristiano_kx1_exo] KX-1 servo preset wrapped (quieter / lower pitch)`
- … ещё 57 уникальных строк

#### `kristiano_welcome` — загрузился

- `[21:41:24.243] [kristiano_welcome] loaded v1.0.0`
- `[21:42:30.890] [kristiano_welcome] loaded v1.0.0`
- `[21:50:48.793] [kristiano_welcome] loaded v1.0.0`
- `[21:54:24.388] [kristiano_welcome] loaded v1.0.0`
- `[21:57:40.334] [kristiano_welcome] loaded v1.0.0`
- `[22:02:56.194] [kristiano_welcome] loaded v1.0.0`
- `[22:12:24.202] [kristiano_welcome] loaded v1.0.0`
- `[22:13:32.251] [kristiano_welcome] loaded v1.0.0`
- `[22:16:32.044] [kristiano_welcome] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- `[21:41:24.402] [quickqk_task_complete] loaded v1.4.2`
- `[21:42:31.040] [quickqk_task_complete] loaded v1.4.2`
- `[21:50:48.939] [quickqk_task_complete] loaded v1.4.2`
- `[21:54:24.545] [quickqk_task_complete] loaded v1.4.2`
- `[21:57:40.477] [quickqk_task_complete] loaded v1.4.2`
- `[22:02:30.901] [QuickQK] action=force_complete | phase=before | task_id=simulation_task_gambling_with_life | title=Азартные игры с жизнью | details=reward_not_guaranteed`
- `[22:02:30.901] [QuickQK] action=force_complete | phase=success | task_id=simulation_task_gambling_with_life | title=Азартные игры с жизнью | details=none`
- `[22:02:56.336] [quickqk_task_complete] loaded v1.4.2`
- `[22:12:24.344] [quickqk_task_complete] loaded v1.4.2`
- `[22:13:32.395] [quickqk_task_complete] loaded v1.4.2`
- `[22:16:32.194] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- `[21:40:36.305] path:tooltip_control/hold_key, key:56, old:nil`
- `[21:40:36.305] path:tooltip_control/trigger_key, key:56, old:nil`
- `[21:41:25.212] [seamless_inventory_sort_anthology] loaded v1.5.8-ux-presets`
- `[21:41:25.212] [Seamless Inventory Sort / Anthology 1.5.8-ux-presets] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[21:41:25.232] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[21:42:30.218] path:tooltip_control/hold_key, key:56, old:nil`
- `[21:42:30.218] path:tooltip_control/trigger_key, key:56, old:nil`
- `[21:42:31.691] [seamless_inventory_sort_anthology] loaded v1.5.8-ux-presets`
- `[21:42:31.691] [Seamless Inventory Sort / Anthology 1.5.8-ux-presets] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[21:42:31.705] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[21:50:48.129] path:tooltip_control/hold_key, key:56, old:nil`
- `[21:50:48.129] path:tooltip_control/trigger_key, key:56, old:nil`
- … ещё 47 уникальных строк

## Стек

Верхние кадры: `UnhandledFilter` → `CPHSimpleCharacter::UpdateDynamicDamage` → `CPHSimpleCharacter::InitContact` → `CPHActorCharacter::InitContact` → `CPHObject::CollideDynamics` → `CPHObject::Collide`

```
[22:19:50.459] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (816): UnhandledFilter
[22:19:50.466] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHSimpleCharacterInline.h (135): CPHSimpleCharacter::UpdateDynamicDamage
[22:19:50.469] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHSimpleCharacter.cpp (1636): CPHSimpleCharacter::InitContact
[22:19:50.474] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHActorCharacter.cpp (352): CPHActorCharacter::InitContact
[22:19:50.494] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHObject.cpp (142): CPHObject::CollideDynamics
[22:19:50.494] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHObject.cpp (130): CPHObject::Collide
[22:19:50.495] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHSimpleCharacter.cpp (2142): CPHSimpleCharacter::Collide
[22:19:50.497] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHWorld.cpp (346): CPHWorld::Step
[22:19:50.498] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrPhysics\PHWorld.cpp (294): CPHWorld::OnFrame
[22:19:50.501] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\EngineThreading.cpp (305): XRay::Engine::GameThread
[22:19:50.509] at address 0x0000001C53C00160
```

## Нефатальные ошибки

### 1. `igi_text_processor.script` x1

Триггер: нет строки с `!` / `~` перед блоком

```
[C]: in function 'error'
...gy 2.1/bin/..\gamedata\scripts\igi_text_processor.script:260: in function 'resolve_and_link_cache'
...logy 2.1/bin/..\gamedata\scripts\igi_generic_task.script:123: in function <...logy 2.1/bin/..\gamedata\scripts\igi_generic_task.script:118>
... igi_task_manager.script (line: 644) in function 'on_task_crashed'
... igi_task_manager.script (line: 104) in function <... igi_task_manager.script:84>
[C]: in function 'pcall'
... fix_wtf_taskboard_guard.script (line: 182) in function 'is_valid_quest'
... igi_task_manager.script (line: 129) in function 'validate_task'
... igi_task_manager.script (line: 117) in function 'get_valid_quests_for_npc'
... igi_task_manager.script (line: 155) in function 'inject_tasks'
... igi_task_manager.script (line: 137) in function <... igi_task_manager.script:135>
[C]: in function 'pcall'
... fix_wtf_taskboard_guard.script (line: 191) in function 'generate_available_tasks'
... pda_taskboard.script (line: 189) in function 'trigger_generate_available_tasks'
... pda_taskboard.script (line: 67) in function <... pda_taskboard.script:60>
```

## Куда смотреть

- Класс: нативный вылет без блока FATAL ERROR (`UnhandledFilter` + `stack trace:`).
- Не Lua: ACCESS_VIOLATION / unhandled exception в C++ (UI, рендер, шедулер, устройство).
- Верх стека: UnhandledFilter → CPHSimpleCharacter::UpdateDynamicDamage → CPHSimpleCharacter::InitContact → CPHActorCharacter::InitContact → CPHObject::CollideDynamics.
- Штатный выход пишет `* Quitting...` и не оставляет UnhandledFilter.

## Предупреждения (топ 15)

- x4 `! [21:40:36.N] ERROR item_combination | wrong section names`
- x4 `~ [21:41:35.N]  ------------------------------------------------------------------------`
- x4 `! [21:42:29.N] ERROR item_combination | wrong section names`
- x4 `! [21:50:47.N] ERROR item_combination | wrong section names`
- x4 `! [21:54:22.N] ERROR item_combination | wrong section names`
- x4 `! [21:57:38.N] ERROR item_combination | wrong section names`
- x4 `! [22:02:54.N] ERROR item_combination | wrong section names`
- x4 `! [22:12:22.N] ERROR item_combination | wrong section names`
- x4 `! [22:13:30.N] ERROR item_combination | wrong section names`
- x4 `! [22:16:30.N] ERROR item_combination | wrong section names`
- x2 `! [21:40:12.N]  Can't find sound 'material\human\step\n_default_5'`
- x2 `! [21:40:12.N]  Can't find sound 'material\human\step\n_default_6'`
- x2 `! [21:40:12.N]  Can't find sound 'material\human\step\n_gravel_6'`
- x2 `! [21:40:12.N]  Can't find sound 'material\human\step\n_gravel_5'`
- x2 `! [21:40:12.N]  Can't find sound 'material\actor\step\n_gravel_5'`

## Строки перед падением (40)

```
* [22:19:22.829]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.78/0.25/1.01 ms max=5.02/12.70/6.02 ms gc(calls/busy/postload)=1883/37/0
[22:19:28.439] Time continual is:2296724
* [22:19:28.439]  Unregister UI: UIInventory
* [22:19:31.335]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=28.29/11.02/16.75/0.13 ms workers(pre/post/bones/game/lua-gc/vision)=1.14/0.65/1.39/9.11/1.04/0.50 ms max(total/frame/render/wait)=131.15/119.63/24.87/7.47 ms
* [22:19:31.335]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=2.28/0.90/1.73/19.10/11.35/4.52 ms
* [22:19:31.335]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.89/0.16/1.11 ms max=9.24/6.04/10.76 ms gc(calls/busy/postload)=1812/36/0
[22:19:31.890] Time continual is:2300173
[22:19:31.890] [2141706] Trying to start inventory in loot mode for container sim_default_duty_258829 (58829)
[22:19:31.890] [2141706][z_ui_inventory_dotmarks] cfg.block_loot_window is true, blocking access to container sim_default_duty_258829 (58829)
[22:19:31.890] [2141706] Trying to start inventory in loot mode for container sim_default_duty_258829 (58829)
[22:19:31.890] [2141706][z_ui_inventory_dotmarks] cfg.block_loot_window is true, blocking access to container sim_default_duty_258829 (58829)
[22:19:31.988] [2141806] Trying to start inventory in loot mode for container sim_default_duty_258829 (58829)
[22:19:31.988] monkey patching ui_inventory.start
[22:19:31.988] [2141806] Trying to start inventory in loot mode for container sim_default_duty_258829 (58829)
[22:19:31.988] monkey patching ui_inventory.start
[22:19:32.990] Time continual is:2301273
* [22:19:32.990]  Register UI: UIInventory
[22:19:36.223] Time continual is:2304505
[22:19:36.223] Name: collect_recipes || new stage: 3 || give points: 550
* [22:19:40.832]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=31.63/15.48/15.51/0.24 ms workers(pre/post/bones/game/lua-gc/vision)=1.16/0.25/1.37/10.65/0.87/0.57 ms max(total/frame/render/wait)=190.13/177.72/28.73/8.42 ms
* [22:19:40.832]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=2.62/0.36/1.75/31.39/9.96/6.07 ms
* [22:19:40.832]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.84/0.12/1.08 ms max=12.46/2.02/5.68 ms gc(calls/busy/postload)=1684/69/0
[22:19:41.009] Time continual is:2309294
* [22:19:41.009]  Unregister UI: UIInventory
[22:19:45.133] Time continual is:2313419
[22:19:45.133] [2154952] Trying to start inventory in loot mode for container bar_bar_drunk_dolg42759 (42759)
[22:19:45.133] [2154952][z_ui_inventory_dotmarks] cfg.block_loot_window is true, blocking access to container bar_bar_drunk_dolg42759 (42759)
[22:19:45.133] [2154952] Trying to start inventory in loot mode for container bar_bar_drunk_dolg42759 (42759)
[22:19:45.133] [2154952][z_ui_inventory_dotmarks] cfg.block_loot_window is true, blocking access to container bar_bar_drunk_dolg42759 (42759)
[22:19:45.210] [2155026] Trying to start inventory in loot mode for container bar_bar_drunk_dolg42759 (42759)
[22:19:45.210] monkey patching ui_inventory.start
[22:19:45.210] [2155026] Trying to start inventory in loot mode for container bar_bar_drunk_dolg42759 (42759)
[22:19:45.210] monkey patching ui_inventory.start
[22:19:46.211] Time continual is:2314493
* [22:19:46.211]  Register UI: UIInventory
[22:19:48.281] Time continual is:2316567
* [22:19:48.281]  Unregister UI: UIInventory
* [22:19:48.919]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=26.87/7.43/18.95/0.10 ms workers(pre/post/bones/game/lua-gc/vision)=1.06/0.23/1.32/6.97/1.08/0.49 ms max(total/frame/render/wait)=191.05/179.26/41.80/4.57 ms
* [22:19:48.919]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=1.90/0.73/1.86/29.50/10.39/4.16 ms
* [22:19:48.919]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.79/0.13/1.29 ms max=5.30/2.14/4.04 ms gc(calls/busy/postload)=1990/33/0
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
