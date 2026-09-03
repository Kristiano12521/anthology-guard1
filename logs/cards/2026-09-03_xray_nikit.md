# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (884 КБ, 10472 строк)
- Дата разбора: 2026-09-03
- Класс: **вылета в логе нет**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (2)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_minigun_dead_parent`

### С отказами (1)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[08:55:13.399] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[08:55:13.399] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[08:55:18.793] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[08:56:27.315] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`

### В логе без отказов (56)

#### `anthology_busyhands_stability_fix` — загрузился

- `[08:55:14.028] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[08:55:14.619] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[08:55:18.234] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[08:55:18.235] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[08:55:18.235] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[08:55:18.235] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[08:55:18.235] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[08:55:18.236] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[08:55:18.236] [BusyHandsFix v0.6.6] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[08:55:18.236] [BusyHandsFix v0.6.6] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[08:55:18.236] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[08:55:18.237] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 27 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[08:55:18.243] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `context_menu_overhaul_anthology` — загрузился

- `[08:55:18.761] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[08:56:25.712] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[08:56:25.715] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`

#### `diag_log_spam` — загрузился

- `[08:55:02.677] [diag_log_spam] early printe hook`
- `[08:55:03.657] [diag_log_spam] init v1.2.3`
- `[08:55:18.241] [diag_log_spam] loaded v1.2.3 (wrappers active)`
- `[09:01:09.510] [diag_log_spam] TRACE alife_release | server object is nil`
- `[09:01:09.511] [diag_log_spam]   ... zz_cop_phys_story_id_fix.script (line: 456) in function 'alife_release_id'`
- `[09:01:09.511] [diag_log_spam]   ... item_weapon.script (line: 391) in function 'ammo_aggregation'`
- `[09:01:09.511] [diag_log_spam]   ... game_setup.script (line: 537) in function 'func_or_userdata'`
- `[09:01:09.511] [diag_log_spam]   ... axr_main.script (line: 284) in function 'make_callback'`
- `[09:01:09.511] [diag_log_spam]   ... _g.script (line: 118) in function 'SendScriptCallback'`
- `[09:01:09.511] [diag_log_spam]   ... bind_stalker_ext.script (line: 143) in function <... bind_stalker_ext.script:139>`

#### `fix_arena_loadout` — загрузился

- `[08:55:18.793] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` — загрузился

- `[08:55:13.400] [fix_ashot_aw_travel] loaded v1.0.1`
- `[08:55:18.793] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- `[08:55:13.400] [fix_attribute_assistent] loaded v1.0.1`
- `[08:55:18.793] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` — загрузился

- `[08:55:18.793] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[08:55:31.110] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[08:55:31.937] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[08:56:27.388] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[08:56:27.413] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`

#### `fix_charon_red_forest_travel` — загрузился

- `[08:55:13.401] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[08:55:18.793] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[08:55:18.793] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` — загрузился

- `[08:55:13.402] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[08:55:13.402] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[08:55:18.793] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_fdda_mcm_paths` — загрузился

- `[08:55:13.402] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- `[08:55:13.402] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- `[08:55:13.402] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- `[08:55:13.402] [fix_g2x_torch_meshes] loaded v1.0.0`

#### `fix_gigant_space_restriction` — загрузился

- `[08:55:13.403] [fix_gigant_space_restriction] loaded v1.1.1`
- `[08:55:18.793] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[08:55:18.793] [fix_gigant_space_restriction] loaded v1.1.1`
- `[08:55:30.822] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[08:55:30.822] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[08:55:30.945] [fix_gigant_space_restriction] quarantine id=3310 name=gigant_strong3310 section=gigant_strong reason=off_level`
- `[08:55:30.946] [fix_gigant_space_restriction] quarantine id=3312 name=gigant_weak3312 section=gigant_weak reason=off_level`
- `[08:55:30.946] [fix_gigant_space_restriction] quarantine id=3313 name=gigant_weak3313 section=gigant_weak reason=off_level`
- `[08:55:31.173] [fix_gigant_space_restriction] quarantine id=8164 name=gigant_normal8164 section=gigant_normal reason=off_level`
- `[08:55:31.439] [fix_gigant_space_restriction] quarantine id=12058 name=gigant_weak12058 section=gigant_weak reason=off_level`
- `[08:55:31.440] [fix_gigant_space_restriction] quarantine id=12084 name=gigant_weak12084 section=gigant_weak reason=off_level`
- `[08:55:31.548] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- … ещё 35 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[08:53:32.998] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[08:53:32.998] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[08:53:39.054] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`

#### `fix_grifon_visibility` — загрузился

- `[08:55:13.403] [fix_grifon_visibility] loaded v1.0.0`

#### `fix_hip_quest_text` — загрузился

- `[08:55:13.403] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- `[08:55:13.403] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_indeikam_breeding` — загрузился

- `[08:55:13.403] [fix_indeikam_breeding] loaded v1.0.0`

#### `fix_item_combination_magnifiers` — загрузился

- `[08:55:13.403] [fix_item_combination_magnifiers] loaded v1.0.0`

#### `fix_kupol_wrong_bone` — загрузился

- `[08:55:18.793] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[08:56:27.475] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`

#### `fix_loot_space` — загрузился

- `[08:55:13.404] [fix_loot_space] loaded v1.0.1`
- `[08:55:18.793] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[08:55:18.794] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[08:58:14.608] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`

#### `fix_misc_script_errors` — загрузился

- `[08:53:32.998] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[08:54:05.967] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[08:55:13.404] [fix_misc_script_errors] loaded v1.0.2`
- `[08:55:18.794] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` — загрузился

- `[08:55:13.404] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- `[08:55:13.404] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:55:18.794] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- `[08:55:18.794] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[08:55:18.794] [fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` — загрузился

- `[08:55:13.405] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[08:55:13.405] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[08:55:18.794] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[08:55:13.405] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[08:55:18.794] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[08:55:18.794] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — загрузился

- `[08:55:13.406] [fix_quest_stash] loaded v1.0.3`
- `[08:55:18.794] [fix_quest_stash] v1.0.3 status functor wrapped`
- `[08:55:18.794] [fix_quest_stash] loaded v1.0.3 section drx_sl_quest_item_1014 exist=yes`

#### `fix_quest_story_id` — загрузился

- `[08:55:13.407] [fix_quest_story_id] loaded v1.0.2`
- `[08:55:18.794] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[08:55:18.794] [fix_quest_story_id] loaded v1.0.2`
- `[08:55:31.852] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[08:55:32.963] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[08:55:33.045] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[08:56:24.335] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[08:56:24.406] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[08:56:24.412] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`

#### `fix_radio` — загрузился

- `[08:55:13.408] [fix_radio] loaded v1.0.2`
- `[08:55:18.794] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` — загрузился

- `[08:55:13.408] [fix_replace_quest_corpse] loaded v1.0.1`
- `[08:55:13.408] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[08:55:18.794] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` — загрузился

- `[08:55:18.794] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[08:55:13.408] [fix_rx_bandage_dead] loaded v1.0.1`
- `[08:55:18.794] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- `[08:55:13.409] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` — загрузился

- `[08:55:13.409] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:55:18.794] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` — загрузился

- `[08:55:13.409] [fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` — загрузился

- `[08:55:13.409] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` — загрузился

- `[08:55:18.794] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[08:55:18.794] [fix_stash_id_desync] loaded v1.0.2`
- `[08:56:35.183] [fix_stash_id_desync] repair done spots=0 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- `[08:55:18.794] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` — загрузился

- `[08:55:13.410] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- `[08:55:03.658] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[08:55:18.241] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` — загрузился

- `[08:55:13.410] [fix_vows_ambush_stash] loaded v1.0.1`
- `[08:55:18.794] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[08:55:18.794] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` — загрузился

- `[08:55:13.411] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:55:18.794] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` — загрузился

- `[08:55:13.411] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[08:55:18.794] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` — загрузился

- `[08:55:13.411] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- `[08:55:13.412] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:55:18.794] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` — загрузился

- `[08:55:18.794] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- `[08:55:13.412] [fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- `[08:55:15.877] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- `[08:54:31.800] path:tooltip_control/hold_key, key:56, old:nil`
- `[08:54:31.800] path:tooltip_control/trigger_key, key:56, old:nil`
- `[08:55:20.518] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[08:55:20.521] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=fps keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[08:55:20.663] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[09:00:09.663] path:tooltip_control/hold_key, key:56, old:56`
- `[09:00:09.663] path:tooltip_control/trigger_key, key:56, old:56`
- `[09:00:11.106] path:tooltip_control/hold_key, key:56, old:56`
- `[09:00:11.106] path:tooltip_control/trigger_key, key:56, old:56`
- `[09:03:50.324] path:tooltip_control/hold_key, key:56, old:56`
- `[09:03:50.324] path:tooltip_control/trigger_key, key:56, old:56`
- `[09:10:55.255] path:tooltip_control/hold_key, key:56, old:56`
- … ещё 5 уникальных строк

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

## Предупреждения (топ 15)

- x6 `~ [08:56:09.N] WARNING : Failed to load 'dynamics\hoc_medical\hoc_bandage\hoc_bandage', falling back to 'dynamics\devices\dev_bandage\dev_bandage.ogf'`
- x5 `~ [08:56:14.N] WARNING : Failed to load 'dynamics\hoc_medical\hoc_bandage\hoc_bandage', falling back to 'dynamics\devices\dev_bandage\dev_bandage.ogf'`
- x4 `! [08:54:31.N] ERROR item_combination | wrong section names`
- x3 `~ [08:55:07.N] [DLTX] WARNING: Attemped to override section 'N', which doesn't exist. Ensure that a base section with the same name is loaded first. Check this file and its DLTX mods: c:/games/antholo`
- x3 `~ [08:56:09.N] WARNING : Failed to load 'dynamics\hoc_medical\hoc_medkit\hoc_medkit', falling back to 'dynamics\devices\dev_aptechka\dev_aptechka_low.ogf'`
- x2 `! [08:53:33.N]  Can't find sound 'material\human\step\n_default_5'`
- x2 `! [08:53:33.N]  Can't find sound 'material\human\step\n_default_6'`
- x2 `! [08:53:33.N]  Can't find sound 'material\human\step\n_gravel_6'`
- x2 `! [08:53:33.N]  Can't find sound 'material\human\step\n_gravel_5'`
- x2 `! [08:53:33.N]  Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! [08:53:33.N]  Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! [08:53:33.N]  Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! [08:53:33.N]  Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! [08:53:33.N]  Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! [08:53:33.N]  Can't find sound 'material\shells\small_shell_conc_h_04'`

## Последние строки лога (40)

```
* [09:47:36.459]         :   1: ui\ui_rak_global_ammo
* [09:47:36.459]         :   1: ui\ui_rak_global_device
* [09:47:36.459]         :   1: ui\ui_rak_global_knife
* [09:47:36.459]         :   1: ui\ui_stalker2_armors
* [09:47:36.459]         :   1: ui\ui_stalker2_mutantparts
* [09:47:36.459]         :   1: ui\ui_upgrade_indicator
* [09:47:36.459]         :   1: ui\weapon_display_icons
* [09:47:36.459]         :   1: ui\xcvb_achievements\icons
* [09:47:36.459]         :   1: unrealengine\electricblast1
* [09:47:36.459]         :   1: unrealengine\electricblast2
* [09:47:36.459]         :   1: unrealengine\puffcolorsplashflicker
* [09:47:36.459]  RM_Dump: rtargets  : 0
* [09:47:36.459]  RM_Dump: vs        : 3
* [09:47:36.460]         :  37: particle
* [09:47:36.460]         :  30: particle-clip
* [09:47:36.460]         :  46: stub_notransform_t
* [09:47:36.460]  RM_Dump: ps        : 7
* [09:47:36.460]         :  45: hud_default
* [09:47:36.460]         :  31: particle
* [09:47:36.460]         :   6: particle_distort
* [09:47:36.460]         :  13: particle_s-aadd
* [09:47:36.460]         :   5: particle_s-add
* [09:47:36.460]         :  12: particle_s-blend
* [09:47:36.460]         :   1: stub_default
* [09:47:36.460]  RM_Dump: dcl       : 1
* [09:47:36.460]  RM_Dump: states    : 8
* [09:47:36.460]  RM_Dump: tex_list  : 82
* [09:47:36.460]  RM_Dump: matrices  : 0
* [09:47:36.460]  RM_Dump: lst_constants: 0
* [09:47:36.460]  RM_Dump: v_passes  : 113
* [09:47:36.460]  RM_Dump: v_elements: 113
* [09:47:36.460]  RM_Dump: v_shaders : 82
[09:47:36.478] refCount:pBaseZB 1
[09:47:36.478] refCount:pBaseRT 1
[09:47:36.545] refCount:m_pSwapChain 1
[09:47:36.545] DeviceREF: 323
[09:47:36.545] refCount:m_pOutput 2
[09:47:36.545] refCount:m_pAdapter 2
[09:47:36.545] refCount:m_pFactory 2
[09:47:36.744] [xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
