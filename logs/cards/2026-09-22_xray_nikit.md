# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (1.0 МБ, 20040 строк)
- Дата разбора: 2026-09-22
- Класс: **вылета в логе нет**
- Среда: xrCore build 10087, anomalydx11avx.exe

## Мои моды

### Не появились в логе (3)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_item_combination_magnifiers`
- `fix_minigun_dead_parent`

### С отказами (6)

#### `fix_aim_fatigue_visibility` — есть отказы

- x6 `[fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- x2 `[fix_aim_fatigue_visibility] loaded v1.0.2`

#### `fix_dotmarks_interact_prompt` — есть отказы

- x4 `[fix_dotmarks_interact_prompt] InteractPrompt.on_option_change not found - guard NOT installed`
- x2 `[fix_dotmarks_interact_prompt] loaded v1.0.0`

#### `fix_melee_trade_supplies` — есть отказы

- x4 `[fix_melee_trade_supplies] melee_trade_inject.vks_spawn_stock not found - guard NOT installed`
- x2 `[fix_melee_trade_supplies] loaded v1.0.1`

#### `fix_nil_crash_guards` — есть отказы

- x4 `[fix_nil_crash_guards] se_monster.on_unregister not found - guard NOT installed`
- x4 `[fix_nil_crash_guards] se_stalker.on_unregister not found - guard NOT installed`
- x2 `[fix_nil_crash_guards] loaded v1.1.1`
- x2 `[fix_nil_crash_guards] cover_tilt: demonized_randomizing_functions already present`
- x2 `[fix_nil_crash_guards] wrapped item_knife.get_condition`
- x2 `[fix_nil_crash_guards] wrapped semenov task_functor targets=2`
- x2 `[fix_nil_crash_guards] wrapped smart_terrain.on_death`
- x2 `[fix_nil_crash_guards] wrapped xr_effects.spawn_intercept_artifact_artifact`
- x2 `[fix_nil_crash_guards] wrapped bind_stalker_ext.actor_on_net_spawn`
- x2 `[fix_nil_crash_guards] wrapped reverse_resolution_list_mcm.cont_vid_mode`
- x2 `[fix_nil_crash_guards] retargeted ui_options vid_mode content slots=1`

#### `fix_qaw_ammo_nil` — есть отказы

- x6 `[fix_qaw_ammo_nil] QAmmoWheelOption.LoadInActiveWeapon not found - guard NOT installed`
- x2 `[fix_qaw_ammo_nil] loaded v1.0.3`

#### `fix_utjan_mag_skill` — есть отказы

- x2 `[fix_utjan_mag_skill] loaded v1.0.0`
- x2 `[fix_utjan_mag_skill] magazines module missing - mag skill wrappers NOT installed`

### В логе без отказов (79)

#### `anthology_busyhands_stability_fix` — загрузился

- x2 `[BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- x2 `[BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- x2 `[BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- x2 `[BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- x2 `[BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- x2 `[BusyHandsFix v0.6.14] get_quickhelp_text replaced via ui_hud_dotmarks (fresh get_maingame, no pcall)`
- x2 `[BusyHandsFix v0.6.14] set_quickhelp_text replaced via ui_hud_dotmarks (fresh get_maingame, no pcall)`
- x2 `[BusyHandsFix v0.6.14] get_quickhelp_text replaced via dotmarks_main (fresh get_maingame, no pcall)`
- x2 `[BusyHandsFix v0.6.14] set_quickhelp_text replaced via dotmarks_main (fresh get_maingame, no pcall)`
- x2 `[BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- x2 `[BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- x2 `[BusyHandsFix v0.6.12] UIInventory.IsInvOwner patched via ui_inventory.UIInventory (method-level, ui_inventory.script untouched)`
- … ещё 44 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- x2 `[BurnShitInventoryDestroy] loaded v1.0.4-beta | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked`
- x2 `[BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` — загрузился

- x2 `[campfires_anthology_compat] loaded v1.1.2`
- x2 `[campfires_anthology_compat] trader_autoinject.update wrapped v1.1.2`
- x2 `* 64.1 : [   1] ui\ui_campfire_placeable`

#### `context_menu_overhaul_anthology` — загрузился

- x2 `[CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- x2 `[CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- x2 `[CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`

#### `diag_log_spam` — загрузился

- x2 `[diag_log_spam] early printe hook`
- x2 `[diag_log_spam] init v1.2.3`
- x2 `[diag_log_spam] loaded v1.2.3 (wrappers active)`
- x2 `[diag_log_spam]   [C]: in function '__index'`
- `[diag_log_spam] TRACE printe:item_combination | !ERROR item_combination | wrong section names`
- `[diag_log_spam]   ... itms_manager.script (line: 78) in main chunk`
- `[diag_log_spam]   ... a_wpo_parts.script (line: 2) in main chunk`
- `[diag_log_spam]   ... axr_main.script (line: 325) in function 'on_game_start'`
- `[diag_log_spam]   ... _g.script (line: 82) in function <... _g.script:73>`

#### `fetch_remote_storage` — загрузился

- x2 `[fetch_remote_storage] loaded v1.1.0`
- x2 `[fetch_remote_storage] installed v1.1.0 (PDA stash markers)`

#### `fix_aol_sprint_hud` — загрузился

- x2 `[fix_aol_sprint_hud] loaded v1.0.1`
- x2 `[fix_aol_sprint_hud] wrapped aol_sprint_cancel.actor_on_movement_changed`
- `[fix_aol_sprint_hud] skip stop_hud_motion (no active hud motion, total=1)`
- `[fix_aol_sprint_hud] skip stop_hud_motion (no active hud motion, total=2)`
- `[fix_aol_sprint_hud] skip stop_hud_motion (no active hud motion, total=4)`

#### `fix_arena_loadout` — загрузился

- x2 `[fix_arena_loadout] loaded v1.1.1`
- x2 `[fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_arti_frames_nil` — загрузился

- x2 `[fix_arti_frames_nil] loaded v1.0.3`
- x2 `[fix_arti_frames_nil] guard installed v1.0.3`

#### `fix_ashot_aw_travel` — загрузился

- x2 `[fix_ashot_aw_travel] loaded v1.0.2`
- x2 `[fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- x4 `[fix_attribute_assistent] loaded v1.0.3`

#### `fix_aver_darkvalley` — загрузился

- x2 `[fix_aver_darkvalley] loaded v1.0.1 routes=2`
- x2 `[fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- x2 `[fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- x2 `[fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- x2 `[fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`

#### `fix_charon_red_forest_travel` — загрузился

- x2 `[fix_charon_red_forest_travel] loaded v1.0.2`
- x2 `[fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_create_squad_nil_smart` — загрузился

- x2 `[fix_create_squad_nil_smart] loaded v1.0.0`
- x2 `[fix_create_squad_nil_smart] wrapped xr_effects.create_squad`
- x2 `[fix_create_squad_nil_smart] wrapped SIMBOARD.create_squad`

#### `fix_crowkiller_hello` — загрузился

- x2 `[fix_crowkiller_hello] loaded v1.0.1`
- x2 `[fix_crowkiller_hello] crowkiller_is_valiable wrapped v1.0.1`

#### `fix_dome_quest` — загрузился

- x2 `[fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- x2 `[fix_dotmarks_dropped_weapon] loaded v1.0.3`
- x2 `[fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_drx_enemy_task_gate` — загрузился

- x2 `[fix_drx_enemy_task_gate] loaded v1.0.2`
- x2 `[fix_drx_enemy_task_gate] v1.0.2 wrapped: drx_sl_is_enemy, has_completed_task_prerequisites, CRandomTask.give_task`
- x2 `[fix_drx_enemy_task_gate] v1.0.2 reclaim: CRandomTask.give_task`

#### `fix_drx_sl_meet_loop` — загрузился

- x2 `[fix_drx_sl_meet_loop] loaded v1.0.2`
- x2 `[fix_drx_sl_meet_loop] v1.0.2 wrapped: drx_sl_meet_random_honcho`

#### `fix_dynamic_armor_visuals_nil` — загрузился

- x2 `[fix_dynamic_armor_visuals_nil] loaded v1.0.4`
- x2 `[fix_dynamic_armor_visuals_nil] guard installed v1.0.4`

#### `fix_faction_trade_supply` — загрузился

- x2 `[fix_faction_trade_supply] loaded v1.0.1`
- x2 `[fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`

#### `fix_fdda_mcm_paths` — загрузился

- x2 `[fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- x2 `[fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- x2 `[fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- x2 `[fix_g2x_torch_meshes] loaded v1.0.1`

#### `fix_gigant_space_restriction` — загрузился

- x4 `[fix_gigant_space_restriction] loaded v1.1.2`
- x2 `[fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- x2 `[fix_gigant_space_restriction] quarantine id=42237 name=gigant_normal42237 section=gigant_normal reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=42244 name=gigant_normal42244 section=gigant_normal reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=43472 name=gigant_normal43472 section=gigant_normal reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=46862 name=gigant_normal46862 section=gigant_normal reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=47464 name=gigant_normal47464 section=gigant_normal reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=50525 name=gigant_strong50525 section=gigant_strong reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=60826 name=gigant_strong60826 section=gigant_strong reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=61490 name=gigant_weak61490 section=gigant_weak reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=61491 name=gigant_weak61491 section=gigant_weak reason=off_level`
- x2 `[fix_gigant_space_restriction] quarantine id=62227 name=gigant_weak62227 section=gigant_weak reason=off_level`
- … ещё 19 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- x2 `[fix_gonta_duplicate_dialog] loaded v1.0.2`
- x2 `[Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`

#### `fix_grifon_visibility` — загрузился

- x2 `[fix_grifon_visibility] loaded v1.1.0`

#### `fix_hip_quest_text` — загрузился

- x2 `[fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- x2 `[fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_hostage_task_collision` — загрузился

- x2 `[fix_hostage_task_collision] loaded v1.0.1`
- x2 `[fix_hostage_task_collision] v1.0.1 wrapped: give_task, setup_companion_task`
- x2 `[fix_hostage_task_collision] v1.0.1 reclaim: give_task`

#### `fix_indeikam_breeding` — загрузился

- x2 `[fix_indeikam_breeding] loaded v1.1.0`

#### `fix_kupol_wrong_bone` — загрузился

- x2 `[fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- x2 `[fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`

#### `fix_locked_stash_boxes` — загрузился

- x4 `[fix_locked_stash_boxes] loaded v1.0.1`
- x2 `[fix_locked_stash_boxes] v1.0.1 get_random_stash wrapped`
- x2 `[fix_locked_stash_boxes] repair done locked=0 relocated=0 cleared=0 dropped_pending=0`

#### `fix_loot_space` — загрузился

- x2 `[fix_loot_space] loaded v1.0.2`
- x2 `[fix_loot_space] loaded v1.0.2 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_matches_campfire_softlock` — загрузился

- x2 `[fix_matches_campfire_softlock] loaded v1.0.1`
- x2 `[fix_matches_campfire_softlock] guard installed v1.0.1 timeout=8s`

#### `fix_milspec_exo_craft` — загрузился

- x2 `[fix_milspec_exo_craft] loaded v1.0.4`
- x2 `[fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.4`
- x2 `[fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`

#### `fix_misc_script_errors` — загрузился

- x2 `[Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- x2 `[fix_misc_script_errors] loaded v1.0.4`
- x2 `[fix_misc_script_errors] loaded v1.0.4 wrapped mas_scope_detach.on_game_start`
- x2 `[fix_misc_script_errors] wrapped existing mas_scope_detach after_move (late)`
- `[fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`

#### `fix_nimble_order_desc` — загрузился

- x2 `[fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- x4 `[fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- x2 `[fix_nta_stashes] loaded v1.0.1`
- x2 `[fix_nta_stashes] v1.0.1 populate wrapped`
- x2 `[fix_nta_stashes] callbacks registered v1.0.1`

#### `fix_okrest_texnik_dialog` — загрузился

- x2 `[fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- x2 `[fix_pda_buyinfo_gui] loaded v1.1.3`
- x2 `[fix_pda_buyinfo_gui] loaded v1.1.3 wrapped=6 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- x2 `[fix_ph_door_rx_reload] loaded v1.0.2`
- x2 `[fix_ph_door_rx_reload] loaded v1.0.2 wrapped ph_door.try_to_open/close`
- x2 `[fix_ph_door_rx_reload] loaded v1.0.2 wrapped rx_ai.enable_schemes`

#### `fix_quest_item_shared_fail` — загрузился

- x2 `[fix_quest_item_shared_fail] loaded v1.3.2`
- x2 `[fix_quest_item_shared_fail] v1.3.2 status wrapped`
- x2 `[fix_quest_item_shared_fail] loaded ok v1.3.2`

#### `fix_quest_stash` — загрузился

- x2 `[fix_quest_stash] загружен v1.0.6`
- x2 `[fix_quest_stash_hint] loaded v1.0.2`
- x2 `[fix_quest_stash] v1.0.6 status-функтор обёрнут`
- x2 `[fix_quest_stash] загружен v1.0.6 section drx_sl_quest_item_1014 exist=yes`
- x2 `[fix_quest_stash_hint] v1.0.2 wrapped: get_random_stash, set_random_stash`

#### `fix_quest_stash_hint` — загрузился

- x2 `[fix_quest_stash_hint] loaded v1.0.2`
- x2 `[fix_quest_stash_hint] v1.0.2 wrapped: get_random_stash, set_random_stash`

#### `fix_quest_story_id` — загрузился

- x4 `[fix_quest_story_id] loaded v1.0.3`
- x4 `[fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- x4 `[fix_quest_story_id] kept first object 44964 for repeated story_id jup_a9_dogs_normal`
- x2 `[fix_quest_story_id] v1.0.3 register() wrapped`
- x2 `[fix_quest_story_id] ignored duplicate object 2718 for story_id esc_village_zona_quest`
- x2 `[fix_quest_story_id] ignored duplicate object 2750 for story_id esc_zone_atp_all`
- x2 `[fix_quest_story_id] selected object 24424 for story_id main_story_19_aver_documents (replaced 24425)`
- x2 `[fix_quest_story_id] selected object 24937 for story_id main_story_14_sci_documents (replaced 24938)`
- x2 `[fix_quest_story_id] selected object 26197 for story_id main_story_16_kas_documents (replaced 26198)`
- x2 `[fix_quest_story_id] selected object 26456 for story_id main_story_17_country_documents (replaced 26457)`
- x2 `[fix_quest_story_id] selected object 27561 for story_id main_story_18_los_documents (replaced 27562)`

#### `fix_radio` — загрузился

- x4 `[fix_radio] loaded v1.0.7`

#### `fix_replace_quest_corpse` — загрузился

- x6 `[fix_replace_quest_corpse] replace_quest_corpse already defined, skip`
- x4 `[fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` — загрузился

- x2 `[fix_rogue_hostility] loaded v1.0.0`

#### `fix_rvr_active_storages_nil` — загрузился

- x2 `[fix_rvr_active_storages_nil] loaded v1.0.0`
- x2 `[fix_rvr_active_storages_nil] guard installed v1.0.0`
- x2 `[fix_rvr_active_storages_nil] healed ActiveStorages reason=actor_on_first_update (batch_total=1)`

#### `fix_rx_bandage_dead` — загрузился

- x2 `[fix_rx_bandage_dead] loaded v1.0.2`
- x2 `[fix_rx_bandage_dead] loaded v1.0.2 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- x2 `[fix_sim_mechanic_trade] loaded v1.0.3`

#### `fix_sim_medic_task_dialog` — загрузился

- x2 `[fix_sim_medic_task_dialog] loaded v1.0.3`
- x2 `[fix_sim_medic_task_dialog] ordered finish fallback -> sim installed`
- x2 `[fix_sim_medic_task_dialog] callback installed`

#### `fix_smart_terrain_state_write` — загрузился

- x2 `[fix_smart_terrain_state_write] loaded v1.0.3`
- x2 `[fix_smart_terrain_state_write] guard installed v1.0.3`

#### `fix_soc_nimble_flash` — загрузился

- x4 `[fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` — загрузился

- x2 `[fix_sort_tabs] loaded v1.0.0`

#### `fix_sound_object_missing` — загрузился

- x2 `[fix_sound_object_missing] loaded v1.0.2`
- x2 `[fix_sound_object_missing] sound_object proxy installed v1.0.2`
- x2 `[fix_sound_object_missing] xr_sound.get_safe_sound_object wrapped`
- `[fix_sound_object_missing] skip missing sound path=tb_growls\tb_lurk_5 (unique=1 total_skips=1)`
- `[fix_sound_object_missing] skip missing sound path=tb_growls\tb_lurk_2 (unique=2 total_skips=2)`
- `[fix_sound_object_missing] skip missing sound path=tb_growls\tb_lurk_3 (unique=3 total_skips=3)`

#### `fix_st2_footstep` — загрузился

- x2 `[fix_st2_footstep] loaded v1.0.0`

#### `fix_stale_fetch_marker` — загрузился

- x2 `[fix_stale_fetch_marker] loaded v1.0.3`
- x2 `[fix_stale_fetch_marker] installed v1.0.3`
- x2 `[fix_stale_fetch_marker] sweep reason=delayed pstors=1 probed=0 cleared=0 task_info=true`
- `[fix_stale_fetch_marker] cleared fetch pstor task=rosf_isg_trader_task_2 why=orphan_no_engine sec=ammo_12x70_buck stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=simulation_task_57 why=orphan_no_engine sec=vodka stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=rosf_isg_medic_task_1 why=orphan_no_engine sec=itm_drugkit stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=rosf_isg_trader_task_4 why=orphan_no_engine sec=itm_pda_common stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=rosf_isg_tech_task_1 why=orphan_no_engine sec=itm_basickit stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=rosf_isg_trader_task_3 why=orphan_no_engine sec=medkit_army stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=eloquent_task_7 why=orphan_no_engine sec=ammo_11.43x23_fmj stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=eloquent_task_5 why=orphan_no_engine sec=radio stor=AC_ID`
- `[fix_stale_fetch_marker] cleared fetch pstor task=rosf_isg_trader_task_6 why=orphan_no_engine sec=af_blood stor=AC_ID`
- … ещё 11 уникальных строк

#### `fix_stash_id_desync` — загрузился

- x2 `[fix_stash_id_desync] v1.0.3 release_stash_by_id wrapped`
- x2 `[fix_stash_id_desync] loaded v1.0.3`
- x2 `[fix_stash_id_desync] repair done spots=0 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- x2 `[fix_talents_pda_respec] loaded v1.0.2`
- x2 `[fix_talents_pda_respec] loaded v1.0.2 wrapped=7 missing=0`

#### `fix_taskboard_sync` — загрузился

- x4 `[fix_taskboard_sync] v1.0.3 wrapped: xr_effects.setup_bounty_task, xr_effects.drx_sl_create_quest_stash, xr_effects.setup_fetch_task, xr_effects.setup_generic_fetch_task, xr_effects.setup_supplies_fetch_task_lostzone_pat`
- x2 `[fix_taskboard_sync] loaded v1.0.3`

#### `fix_trade_craft_stock` — загрузился

- x2 `[fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- x2 `[fix_trader_restock_callback] trader_on_restock added v1.0.5`
- x2 `[fix_trader_restock_callback] Send wrap installed`

#### `fix_travel_invalid_id` — загрузился

- x2 `[fix_travel_invalid_id] loaded v1.0.1`
- x2 `[fix_travel_invalid_id] RegisterScriptCallback hook installed v1.0.1`
- x2 `[fix_travel_invalid_id] late-wrapped 4 travel callback(s)`

#### `fix_vows_ambush_stash` — загрузился

- x4 `[fix_vows_ambush_stash] loaded v1.0.2`
- x2 `[fix_vows_ambush_stash] v1.0.2 activate_by_section wrapped`

#### `fix_wtf_assault_instacomplete` — загрузился

- x4 `[fix_wtf_assault_instacomplete] loaded v1.0.3`

#### `fix_wtf_fetch_counter` — загрузился

- x2 `[fix_wtf_fetch_counter] loaded v1.0.1`
- x2 `[fix_wtf_fetch_counter] installed v1.0.1`

#### `fix_wtf_taskboard_guard` — загрузился

- x4 `[fix_wtf_taskboard_guard] loaded v1.0.4 wrapped=9 missing=0`
- x2 `[fix_wtf_taskboard_guard] loaded v1.0.4`

#### `fix_x15_freeplay_gate` — загрузился

- x2 `[fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- x4 `[fix_x2_gravity_room] loaded v1.0.2`
- x2 `[fix_x2_gravity_room] bas_no_gravity_anomaly bound v1.0.2`

#### `fix_xr_effects_sounds` — загрузился

- x2 `[fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- x2 `[fix_zat_b12_box] loaded v1.0.0`

#### `kristiano_kx1_exo` — загрузился

- x4 `[kristiano_kx1_toxic_air] WARN: toxic_air.tank_in_belt missing`
- x2 `[kristiano_kx1_exo] loaded v1.5.5-b`
- x2 `[kristiano_kx1_toxic_air] loaded v1.1.1`
- x2 `[kristiano_kx1_exo] LoadRecipesLTX wrap (re)installed v1.5.5-b`
- x2 `[kristiano_kx1_exo] hooks installed v1.5.5-b`
- x2 `[kristiano_kx1_exo] KX-1 servo preset wrapped (quieter / lower pitch)`
- x2 `[kristiano_kx1_exo] injected 3 new recipes`
- `[kristiano_kx1_exo] lore article unlocked: encyclopedia_items_kristiano_kx1`
- `[kristiano_kx1_exo] ensured encyclopedia unlock for existing blueprint`

#### `kristiano_welcome` — загрузился

- x2 `[kristiano_welcome] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- x2 `[quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- x8 `path:tooltip_control/hold_key, key:56, old:56`
- x8 `path:tooltip_control/trigger_key, key:56, old:56`
- x2 `path:tooltip_control/hold_key, key:56, old:nil`
- x2 `path:tooltip_control/trigger_key, key:56, old:nil`
- x2 `[seamless_inventory_sort_anthology] loaded v1.5.8-ux-presets`
- x2 `[Seamless Inventory Sort / Anthology 1.5.8-ux-presets] mode=balanced keep_gaps=false trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- x2 `[Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[seamless_inventory_sort_anthology] applied ux_preset=comfort`
- `path:tooltip_control/hold_key, key:number, k:number`
- `path:tooltip_control/trigger_key, key:number, k:number`

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

## Предупреждения (топ 15)

- x80 `! [LUA] CSciptEntity [grenade_rgo_impact_explosion]: cannot access class member Alive!`
- x80 `! [LUA]  0 : [C  ] alive`
- x80 `! [LUA]  1 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : register_npc_minigun_bullet`
- x80 `! [LUA]  2 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : func_or_userdata`
- x80 `! [LUA]  3 : [Lua] ....5.3 — anthology/bin/..\gamedata\scripts\axr_main.script(N) : make_callback`
- x80 `! [LUA]  4 : [Lua] ...maly 1.5.3 — anthology/bin/..\gamedata\scripts\_g.script(N) : SendScriptCallback`
- x80 `! [LUA]  5 : [Lua] ...logy/bin/..\gamedata\scripts\callbacks_gameobject.script(N) :`
- x8 `!ERROR item_combination | wrong section names`
- x8 `!MCM given bad path:EA_settings/take_item_anim`
- x8 `!MCM given bad path:EA_settings/enable_animations`
- x7 `!-demonized_mugging_squads # SAVING: Mugging Squad | [version]: 2`
- x6 `!MCM given bad path:milpda/milpdagen/kiltrak`
- x6 `!MCM given bad path:milpda/cfg_device_pda_0/enabled`
- x6 `!MCM given bad path:milpda/cfg_device_pda_4/enabled`
- x6 `!MCM given bad path:milpda/cfg_device_pda_actor/enabled`

## Последние строки лога (40)

```
*        :   1: ui\ui_icons_new_icons_outfits_trenchcoat_gfy_a_pack
*        :   1: ui\ui_ingame2_common
*        :   1: ui\ui_maid_efp_props
*        :   1: ui\ui_mcm
*        :   1: ui\ui_options
*        :   1: ui\ui_rak_global_1
*        :   1: ui\ui_rak_global_2
*        :   1: ui\ui_rak_global_ammo
*        :   1: ui\ui_rak_global_device
*        :   1: ui\ui_rak_global_knife
*        :   1: ui\ui_stalker2_armors
*        :   1: ui\ui_stalker2_mutantparts
*        :   1: ui\xcvb_achievements\icons
*        :   1: ui\xcvb_pda\xcvb_pda_main
*        :   2: unrealengine\electricblast1
*        :   2: unrealengine\electricblast2
*        :   2: unrealengine\puffcolorsplashflicker
* RM_Dump: rtargets  : 0
* RM_Dump: vs        : 3
*        :  39: particle
*        :  35: particle-clip
*        :  69: stub_notransform_t
* RM_Dump: ps        : 7
*        :  68: hud_default
*        :  35: particle
*        :   4: particle_distort
*        :  16: particle_s-aadd
*        :   5: particle_s-add
*        :  14: particle_s-blend
*        :   1: stub_default
* RM_Dump: dcl       : 1
* RM_Dump: states    : 7
* RM_Dump: tex_list  : 143
* RM_Dump: matrices  : 0
* RM_Dump: lst_constants: 0
* RM_Dump: v_passes  : 143
* RM_Dump: v_elements: 143
* RM_Dump: v_shaders : 108
DeviceREF: 388
[xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
