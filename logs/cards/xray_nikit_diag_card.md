# ╩рЁЄюўър ыюур Ч xray_nikit.log

- ╘рщы: `xray_nikit.log` (729 ╩┴, 9656 ёЄЁюъ)
- ─рЄр ЁрчсюЁр: 2026-09-04
- ╩ырёё: **т√ыхЄр т ыюух эхЄ**
- ╤Ёхфр: xrCore build 10063, anomalydx11avx.exe

## ╠юш ьюф√

### ═х яю тшышё№ т ыюух (2)

╠юф хёЄ№ т `addon/`, эю т ыюух эхЄ эш юфэющ ёЄЁюъш Ч ёъюЁхх тёхую эх єёЄрэютыхэ т MO2 шыш эх яюяры т яръхЄ.

- `fix_bhs_fdda_loot`
- `fix_minigun_dead_parent`

### ╤ юЄърчрьш (1)

#### `fix_aim_fatigue_visibility` Ч хёЄ№ юЄърч√

- `[15:54:09.885] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[15:54:09.885] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:54:11.211] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:54:29.658] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`

### ┬ ыюух схч юЄърчют (59)

#### `anthology_busyhands_stability_fix` Ч чруЁєчшыё 

- `[15:54:09.898] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[15:54:10.207] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[15:54:10.847] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[15:54:10.847] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[15:54:10.847] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[15:54:10.847] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[15:54:10.847] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[15:54:10.848] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[15:54:10.848] [BusyHandsFix v0.6.6] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[15:54:10.848] [BusyHandsFix v0.6.6] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[15:54:10.848] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[15:54:10.848] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- Е х∙╕ 27 єэшъры№э√ї ёЄЁюъ

#### `burnshit_inventory_destroy` Ч чруЁєчшыё 

- `[15:54:10.896] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` Ч чруЁєчшыё 

- `[15:54:09.535] [campfires_anthology_compat] loaded v1.1.0`
- `* [15:54:29.879]  [load-session/lua-callbacks] #07 self=66.61 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`

#### `context_menu_overhaul_anthology` Ч чруЁєчшыё 

- `[15:54:11.206] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[15:54:28.059] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[15:54:28.062] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [15:54:29.879]  [load-session/lua-callbacks] #04 self=81.78 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `[15:54:29.888] [CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=31 current_tab=1 category=manual target_tab=1 route=current_manual`

#### `diag_imotion_death` Ч чруЁєчшыё 

- `[15:54:09.557] [diag_imotion_death] loaded v1.0.0`
- `[15:54:11.206] [diag_imotion_death] diagnostics active v1.0.0`
- `[15:54:24.418] [diag_imotion_death] state reset (game load)`
- `[15:54:29.490] [diag_imotion_death] session level=l10_red_forest actor=id=0 name=actor section=actor`
- `[15:54:54.798] [diag_imotion_death] PREHIT level=l10_red_forest id=47591 name=sim_default_renegade_medic47591 section=sim_default_renegade_medic visual=actors\stalker_renegade\stalker_renegade_1b_face_2 community=renegad`
- `[15:54:54.798] [diag_imotion_death] PREHIT hit power=1.3069140911102 type=8 impulse=32.6728515625 bone_id=0 bone=root_stalker draftsman={id=0 name=actor section=actor} cached_power=1.3069140911102 cached_bone=root_stalke`
- `[15:54:54.798] [diag_imotion_death] PREHIT level=l10_red_forest id=47583 name=sim_default_renegade_trader47583 section=sim_default_renegade_trader visual=actors\stalker_renegade\stalker_renegade_1b_face_1.ogf community=r`
- `[15:54:54.798] [diag_imotion_death] PREHIT hit power=5.6961278915405 type=8 impulse=142.40319824219 bone_id=0 bone=root_stalker draftsman={id=0 name=actor section=actor} cached_power=5.6961278915405 cached_bone=root_stal`
- `[15:54:54.819] [diag_imotion_death] PREHIT level=l10_red_forest id=47596 name=red_bridge_renegade47596 section=red_bridge_renegade visual=actors\stalker_bandit\stalker_bandit_3 community=renegade rank=0 alive=true health`
- `[15:54:54.819] [diag_imotion_death] PREHIT hit power=2.1178586483002 type=8 impulse=52.946464538574 bone_id=0 bone=root_stalker draftsman={id=0 name=actor section=actor} cached_power=2.1178586483002 cached_bone=root_stal`
- `[15:54:54.820] [diag_imotion_death] PREHIT level=l10_red_forest id=47577 name=red_bridge_renegade47577 section=red_bridge_renegade visual=actors\stalker_bandit\stalker_bandit_3 community=renegade rank=0 alive=true health`
- `[15:54:54.820] [diag_imotion_death] PREHIT hit power=3.7337818145752 type=8 impulse=93.344551086426 bone_id=0 bone=root_stalker draftsman={id=0 name=actor section=actor} cached_power=3.7337818145752 cached_bone=root_stal`
- Е х∙╕ 48 єэшъры№э√ї ёЄЁюъ

#### `diag_log_spam` Ч чруЁєчшыё 

- `[15:54:07.959] [diag_log_spam] early printe hook`
- `[15:54:08.698] [diag_log_spam] init v1.2.3`
- `[15:54:10.850] [diag_log_spam] loaded v1.2.3 (wrappers active)`
- `[15:59:07.018] [diag_log_spam] TRACE alife_release | server object is nil`
- `[15:59:07.018] [diag_log_spam]   ... zz_cop_phys_story_id_fix.script (line: 456) in function 'alife_release_id'`
- `[15:59:07.018] [diag_log_spam]   ... item_weapon.script (line: 391) in function 'ammo_aggregation'`
- `[15:59:07.018] [diag_log_spam]   ... game_setup.script (line: 537) in function 'func_or_userdata'`
- `[15:59:07.018] [diag_log_spam]   ... axr_main.script (line: 290) in function 'make_callback'`
- `[15:59:07.018] [diag_log_spam]   ... _g.script (line: 118) in function 'SendScriptCallback'`
- `[15:59:07.018] [diag_log_spam]   ... bind_stalker_ext.script (line: 143) in function <... bind_stalker_ext.script:139>`

#### `fix_arena_loadout` Ч чруЁєчшыё 

- `[15:54:11.211] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` Ч чруЁєчшыё 

- `[15:54:09.885] [fix_ashot_aw_travel] loaded v1.0.1`
- `[15:54:11.212] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` Ч чруЁєчшыё 

- `[15:54:09.885] [fix_attribute_assistent] loaded v1.0.1`
- `[15:54:11.212] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[15:54:16.833] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[15:54:17.250] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[15:54:29.343] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[15:54:29.358] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [15:54:29.879]  [load-session/lua-callbacks] #14 self=31.04 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`

#### `fix_charon_red_forest_travel` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[15:54:11.212] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[15:54:11.212] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_faction_trade_supply` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_faction_trade_supply] loaded v1.0.0`
- `[15:54:11.212] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`

#### `fix_fdda_mcm_paths` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_g2x_torch_meshes] loaded v1.0.0`

#### `fix_gigant_space_restriction` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_gigant_space_restriction] loaded v1.1.1`
- `[15:54:11.212] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[15:54:11.212] [fix_gigant_space_restriction] loaded v1.1.1`
- `[15:54:16.689] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[15:54:16.689] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[15:54:16.750] [fix_gigant_space_restriction] quarantine id=3310 name=gigant_strong3310 section=gigant_strong reason=off_level`
- `[15:54:16.907] [fix_gigant_space_restriction] quarantine id=9852 name=gigant_normal9852 section=gigant_normal reason=off_level`
- `[15:54:16.933] [fix_gigant_space_restriction] quarantine id=10806 name=gigant_normal10806 section=gigant_normal reason=off_level`
- `[15:54:16.974] [fix_gigant_space_restriction] quarantine id=12058 name=gigant_weak12058 section=gigant_weak reason=off_level`
- `[15:54:16.975] [fix_gigant_space_restriction] quarantine id=12084 name=gigant_weak12084 section=gigant_weak reason=off_level`
- `[15:54:17.033] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- `[15:54:17.059] [fix_gigant_space_restriction] quarantine id=15720 name=gigant_weak15720 section=gigant_weak reason=off_level`
- Е х∙╕ 35 єэшъры№э√ї ёЄЁюъ

#### `fix_gonta_duplicate_dialog` Ч чруЁєчшыё 

- `[15:53:01.221] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[15:53:01.221] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[15:53:03.623] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`

#### `fix_grifon_visibility` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_grifon_visibility] loaded v1.0.0`

#### `fix_hip_quest_text` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_indeikam_breeding` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_indeikam_breeding] loaded v1.0.0`

#### `fix_item_combination_magnifiers` Ч чруЁєчшыё 

- `[15:54:09.886] [fix_item_combination_magnifiers] loaded v1.0.0`

#### `fix_kupol_wrong_bone` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[15:54:29.236] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [15:54:29.879]  [load-session/lua-callbacks] #10 self=42.66 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`

#### `fix_loot_space` Ч чруЁєчшыё 

- `[15:54:09.887] [fix_loot_space] loaded v1.0.1`
- `[15:54:11.212] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[15:56:34.817] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`

#### `fix_misc_script_errors` Ч чруЁєчшыё 

- `[15:53:01.221] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[15:53:14.511] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[15:54:09.887] [fix_misc_script_errors] loaded v1.0.2`
- `[15:54:11.212] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` Ч чруЁєчшыё 

- `[15:54:09.887] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` Ч чруЁєчшыё 

- `[15:54:09.887] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[15:54:11.212] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[15:54:11.212] [fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` Ч чруЁєчшыё 

- `[15:54:09.887] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` Ч чруЁєчшыё 

- `[15:54:09.887] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[15:54:11.212] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` Ч чруЁєчшыё 

- `[15:54:09.887] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[15:54:11.212] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[15:54:11.212] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` Ч хёЄ№ ёЄЁюъш

- `[15:54:09.888] [fix_quest_stash] чруЁєцхэ v1.0.4`
- `[15:54:11.212] [fix_quest_stash] v1.0.4 status-ЇєэъЄюЁ юс╕ЁэєЄ`
- `[15:54:11.212] [fix_quest_stash] чруЁєцхэ v1.0.4 section drx_sl_quest_item_1014 exist=yes`

#### `fix_quest_story_id` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_quest_story_id] loaded v1.0.2`
- `[15:54:11.212] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[15:54:11.212] [fix_quest_story_id] loaded v1.0.2`
- `[15:54:17.192] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[15:54:17.782] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[15:54:17.816] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[15:54:29.530] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[15:54:29.569] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[15:54:29.571] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`

#### `fix_radio` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_radio] loaded v1.0.2`
- `[15:54:11.212] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_replace_quest_corpse] loaded v1.0.1`
- `[15:54:09.888] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[15:54:11.212] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_rx_bandage_dead] loaded v1.0.1`
- `[15:54:11.212] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_soc_nimble_flash] loaded v1.0.1`
- `[15:54:11.212] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` Ч чруЁєчшыё 

- `[15:54:09.888] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[15:54:11.212] [fix_stash_id_desync] loaded v1.0.2`
- `[15:54:38.323] [fix_stash_id_desync] cleared id=26404 reason=not_invbox spots=1 cache=false name=gt_package_artifact26404 section=gt_package_artifact`
- `[15:54:38.323] [fix_stash_id_desync] cleared id=26479 reason=not_invbox spots=1 cache=false name=gt_package_artifact26479 section=gt_package_artifact`
- `[15:54:38.402] [fix_stash_id_desync] repair done spots=2 cache_entries=0`

#### `fix_talents_pda_respec` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` Ч чруЁєчшыё 

- `[15:54:08.699] [fix_trader_restock_callback] trader_on_restock exists v1.0.3`
- `[15:54:10.850] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[15:54:10.850] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_vows_ambush_stash] loaded v1.0.1`
- `[15:54:11.212] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[15:54:11.212] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[15:54:11.212] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[15:54:11.212] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_x2_gravity_room] loaded v1.0.1`
- `[15:54:11.212] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` Ч чруЁєчшыё 

- `[15:54:11.212] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` Ч чруЁєчшыё 

- `[15:54:09.889] [fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` Ч чруЁєчшыё 

- `[15:54:10.410] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` Ч чруЁєчшыё 

- `[15:53:26.035] path:tooltip_control/hold_key, key:56, old:nil`
- `[15:53:26.035] path:tooltip_control/trigger_key, key:56, old:nil`
- `[15:54:12.543] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[15:54:12.543] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[15:54:12.564] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[16:01:20.202] path:tooltip_control/hold_key, key:56, old:56`
- `[16:01:20.202] path:tooltip_control/trigger_key, key:56, old:56`
- `[16:01:24.799] path:tooltip_control/hold_key, key:56, old:56`
- `[16:01:24.799] path:tooltip_control/trigger_key, key:56, old:56`

## ╩єфр ёьюЄЁхЄ№

- ┴ыюъ FATAL ERROR эх эрщфхэ: ышсю ыюу юЄ эюЁьры№эюую ёхрэёр, ышсю шуЁр єярыр схч чряшёш (яЁютхЁ№ ъюэхЎ Їрщыр тЁєўэє■).

## ╧ЁхфєяЁхцфхэш  (Єюя 15)

- x4 `! [15:53:25.N] ERROR item_combination | wrong section names`
- x2 `! [15:53:01.N]  Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! [15:53:01.N]  Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_conc_h_04'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_dirt_h_01'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_dirt_h_02'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_dirt_h_03'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_dirt_h_04'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_wood_h_01'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_wood_h_02'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_wood_h_03'`
- x2 `! [15:53:01.N]  Can't find sound 'material\shells\small_shell_wood_h_04'`

## ╧юёыхфэшх ёЄЁюъш ыюур (40)

```
* [16:01:30.058]         :   1: ui_hoc\ui_icon_freshbread
* [16:01:30.058]         :   1: ui_hoc\ui_icon_medkit
* [16:01:30.058]         :   1: ui_hoc\ui_icon_medkitarmy
* [16:01:30.058]         :   1: ui_hoc\ui_icon_psi_block
* [16:01:30.058]         :   1: ui_hoc\ui_icon_spoiledcanned
* [16:01:30.058]         :   1: ui_hoc\ui_icon_vinca
* [16:01:30.058]         :   1: ui_hoc\ui_icon_vodka
* [16:01:30.058]         :   1: ui_hoc\ui_icon_water
* [16:01:30.058]         :   2: unrealengine\electricblast1
* [16:01:30.058]         :   2: unrealengine\puffcolorsplash
* [16:01:30.058]         :   2: unrealengine\puffcolorsplashflicker
* [16:01:30.058]  RM_Dump: rtargets  : 0
* [16:01:30.058]  RM_Dump: vs        : 3
* [16:01:30.058]         :  34: particle
* [16:01:30.058]         :  30: particle-clip
* [16:01:30.058]         :  52: stub_notransform_t
* [16:01:30.058]  RM_Dump: ps        : 7
* [16:01:30.058]         :  51: hud_default
* [16:01:30.058]         :  30: particle
* [16:01:30.058]         :   4: particle_distort
* [16:01:30.058]         :  17: particle_s-aadd
* [16:01:30.058]         :   3: particle_s-add
* [16:01:30.058]         :  10: particle_s-blend
* [16:01:30.058]         :   1: stub_default
* [16:01:30.058]  RM_Dump: dcl       : 1
* [16:01:30.058]  RM_Dump: states    : 7
* [16:01:30.058]  RM_Dump: tex_list  : 114
* [16:01:30.058]  RM_Dump: matrices  : 0
* [16:01:30.058]  RM_Dump: lst_constants: 0
* [16:01:30.058]  RM_Dump: v_passes  : 116
* [16:01:30.058]  RM_Dump: v_elements: 116
* [16:01:30.058]  RM_Dump: v_shaders : 86
[16:01:30.073] refCount:pBaseZB 1
[16:01:30.073] refCount:pBaseRT 1
[16:01:30.073] refCount:m_pSwapChain 1
[16:01:30.079] DeviceREF: 1
[16:01:31.059] refCount:m_pOutput 1
[16:01:31.059] refCount:m_pAdapter 1
[16:01:31.059] refCount:m_pFactory 1
[16:01:31.136] [xrLogger] InternalCloseLog called, terminating thread
```

---

╨рчсюЁ тхф╕ь яю `workflow-crash`: ёэрўрыр ъырёё ш яхЁтюяЁшўшэр, Їшъё Ч Єюы№ъю яюёых яюфЄтхЁцфхэш .
