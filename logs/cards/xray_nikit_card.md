# ╩рЁЄюўър ыюур Ч xray_nikit.log

- ╘рщы: `xray_nikit.log` (737 ╩┴, 10524 ёЄЁюъ)
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

- `[15:38:44.536] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[15:38:44.536] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:38:45.727] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:39:02.475] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:40:09.337] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[15:40:09.337] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:40:10.339] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[15:40:19.122] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`

### ┬ ыюух схч юЄърчют (58)

#### `anthology_busyhands_stability_fix` Ч чруЁєчшыё 

- `[15:38:44.547] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[15:38:44.800] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[15:38:45.372] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[15:38:45.372] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[15:38:45.372] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[15:38:45.372] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[15:38:45.372] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[15:38:45.372] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[15:38:45.372] [BusyHandsFix v0.6.6] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[15:38:45.372] [BusyHandsFix v0.6.6] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[15:38:45.373] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[15:38:45.373] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- Е х∙╕ 66 єэшъры№э√ї ёЄЁюъ

#### `burnshit_inventory_destroy` Ч чруЁєчшыё 

- `[15:38:45.418] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[15:40:10.095] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` Ч чруЁєчшыё 

- `[15:38:44.178] [campfires_anthology_compat] loaded v1.1.0`
- `* [15:39:03.403]  [load-session/lua-callbacks] #04 self=106.41 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`
- `[15:40:09.033] [campfires_anthology_compat] loaded v1.1.0`
- `* [15:40:20.156]  [load-session/lua-callbacks] #09 self=55.20 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`

#### `context_menu_overhaul_anthology` Ч чруЁєчшыё 

- `[15:38:45.721] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[15:39:02.332] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[15:39:02.337] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [15:39:03.403]  [load-session/lua-callbacks] #07 self=78.26 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `[15:39:03.414] [CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=31 current_tab=1 category=manual target_tab=1 route=current_manual`
- `[15:40:10.338] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[15:40:19.701] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[15:40:19.703] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [15:40:20.156]  [load-session/lua-callbacks] #04 self=99.59 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `[15:40:20.166] [CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=31 current_tab=1 category=manual target_tab=1 route=current_manual`

#### `diag_log_spam` Ч чруЁєчшыё 

- x2 `[15:40:07.977] [diag_log_spam]   [C]: in function '__index'`
- `[15:38:42.804] [diag_log_spam] early printe hook`
- `[15:38:43.342] [diag_log_spam] init v1.2.3`
- `[15:38:45.375] [diag_log_spam] loaded v1.2.3 (wrappers active)`
- `[15:40:07.568] [diag_log_spam] early printe hook`
- `[15:40:07.976] [diag_log_spam] TRACE printe:item_combination | !ERROR item_combination | wrong section names`
- `[15:40:07.977] [diag_log_spam]   ... itms_manager.script (line: 78) in main chunk`
- `[15:40:07.977] [diag_log_spam]   ... a_wpo_parts.script (line: 2) in main chunk`
- `[15:40:07.977] [diag_log_spam]   ... axr_main.script (line: 351) in function 'on_game_start'`
- `[15:40:07.977] [diag_log_spam]   ... _g.script (line: 82) in function <... _g.script:73>`
- `[15:40:07.986] [diag_log_spam] init v1.2.3`
- `[15:40:10.093] [diag_log_spam] loaded v1.2.3 (wrappers active)`

#### `fix_arena_loadout` Ч чруЁєчшыё 

- `[15:38:45.727] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[15:40:10.339] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` Ч чруЁєчшыё 

- `[15:38:44.536] [fix_ashot_aw_travel] loaded v1.0.1`
- `[15:38:45.727] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[15:40:09.337] [fix_ashot_aw_travel] loaded v1.0.1`
- `[15:40:10.339] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` Ч чруЁєчшыё 

- `[15:38:44.536] [fix_attribute_assistent] loaded v1.0.1`
- `[15:38:45.727] [fix_attribute_assistent] loaded v1.0.1`
- `[15:40:09.337] [fix_attribute_assistent] loaded v1.0.1`
- `[15:40:10.339] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` Ч чруЁєчшыё 

- `[15:38:45.727] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[15:38:50.907] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[15:38:51.295] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[15:39:02.174] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[15:39:02.198] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [15:39:03.403]  [load-session/lua-callbacks] #12 self=59.43 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`
- `[15:40:10.339] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[15:40:12.372] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[15:40:12.666] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[15:40:18.652] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[15:40:18.671] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [15:40:20.156]  [load-session/lua-callbacks] #12 self=37.72 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`

#### `fix_charon_red_forest_travel` Ч чруЁєчшыё 

- `[15:38:44.536] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[15:38:45.727] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[15:40:09.338] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[15:40:10.339] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` Ч чруЁєчшыё 

- `[15:38:45.727] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[15:40:10.339] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_dome_quest] loaded v1.0.0`
- `[15:40:09.338] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[15:38:45.727] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[15:40:09.338] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[15:40:10.339] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_faction_trade_supply` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_faction_trade_supply] loaded v1.0.0`
- `[15:38:45.727] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[15:40:09.338] [fix_faction_trade_supply] loaded v1.0.0`
- `[15:40:10.339] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`

#### `fix_fdda_mcm_paths` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[15:40:09.338] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_fetch_headlamp] loaded v1.0.0`
- `[15:40:09.338] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_flst_joker_door] loaded v1.0.0`
- `[15:40:09.338] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[15:40:09.338] [fix_g2x_torch_meshes] loaded v1.0.0`

#### `fix_gigant_space_restriction` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_gigant_space_restriction] loaded v1.1.1`
- `[15:38:45.727] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[15:38:45.727] [fix_gigant_space_restriction] loaded v1.1.1`
- `[15:38:50.780] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[15:38:50.780] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[15:38:50.835] [fix_gigant_space_restriction] quarantine id=3310 name=gigant_strong3310 section=gigant_strong reason=off_level`
- `[15:38:50.976] [fix_gigant_space_restriction] quarantine id=9852 name=gigant_normal9852 section=gigant_normal reason=off_level`
- `[15:38:50.998] [fix_gigant_space_restriction] quarantine id=10806 name=gigant_normal10806 section=gigant_normal reason=off_level`
- `[15:38:51.023] [fix_gigant_space_restriction] quarantine id=12058 name=gigant_weak12058 section=gigant_weak reason=off_level`
- `[15:38:51.023] [fix_gigant_space_restriction] quarantine id=12084 name=gigant_weak12084 section=gigant_weak reason=off_level`
- `[15:38:51.075] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- `[15:38:51.097] [fix_gigant_space_restriction] quarantine id=15720 name=gigant_weak15720 section=gigant_weak reason=off_level`
- Е х∙╕ 82 єэшъры№э√ї ёЄЁюъ

#### `fix_gonta_duplicate_dialog` Ч чруЁєчшыё 

- `[15:38:07.605] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[15:38:07.605] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[15:38:09.863] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`
- `[15:40:07.427] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[15:40:07.427] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`

#### `fix_grifon_visibility` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_grifon_visibility] loaded v1.0.0`
- `[15:40:09.338] [fix_grifon_visibility] loaded v1.0.0`

#### `fix_hip_quest_text` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_hip_quest_text] loaded v1.0.0`
- `[15:40:09.338] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[15:40:09.338] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_indeikam_breeding` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_indeikam_breeding] loaded v1.0.0`
- `[15:40:09.338] [fix_indeikam_breeding] loaded v1.0.0`

#### `fix_item_combination_magnifiers` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[15:40:09.338] [fix_item_combination_magnifiers] loaded v1.0.0`

#### `fix_kupol_wrong_bone` Ч чруЁєчшыё 

- `[15:38:45.727] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[15:39:02.748] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [15:39:03.403]  [load-session/lua-callbacks] #06 self=82.75 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[15:40:10.339] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[15:40:20.064] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [15:40:20.156]  [load-session/lua-callbacks] #13 self=35.80 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`

#### `fix_loot_space` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_loot_space] loaded v1.0.1`
- `[15:38:45.727] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[15:40:09.338] [fix_loot_space] loaded v1.0.1`
- `[15:40:10.339] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` Ч чруЁєчшыё 

- `[15:38:45.728] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[15:40:10.339] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`

#### `fix_misc_script_errors` Ч чруЁєчшыё 

- `[15:38:07.605] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[15:38:20.950] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[15:38:44.537] [fix_misc_script_errors] loaded v1.0.2`
- `[15:38:45.728] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[15:40:07.427] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[15:40:09.339] [fix_misc_script_errors] loaded v1.0.2`
- `[15:40:10.339] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` Ч чруЁєчшыё 

- `[15:38:44.537] [fix_nimble_order_desc] loaded v1.0.0`
- `[15:40:09.339] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[15:38:45.728] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[15:40:09.339] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[15:40:10.339] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` Ч чруЁєчшыё 

- `[15:38:45.728] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[15:38:45.728] [fix_nta_stashes] loaded v1.0.0`
- `[15:40:10.339] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[15:40:10.339] [fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[15:40:09.339] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[15:38:45.728] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[15:40:09.339] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[15:40:10.339] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[15:38:45.728] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[15:38:45.728] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[15:40:09.339] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[15:40:10.339] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[15:40:10.339] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` Ч хёЄ№ ёЄЁюъш

- `[15:38:44.538] [fix_quest_stash] чруЁєцхэ v1.0.4`
- `[15:38:45.728] [fix_quest_stash] v1.0.4 status-ЇєэъЄюЁ юс╕ЁэєЄ`
- `[15:38:45.728] [fix_quest_stash] чруЁєцхэ v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[15:40:09.339] [fix_quest_stash] чруЁєцхэ v1.0.4`
- `[15:40:10.339] [fix_quest_stash] v1.0.4 status-ЇєэъЄюЁ юс╕ЁэєЄ`
- `[15:40:10.339] [fix_quest_stash] чруЁєцхэ v1.0.4 section drx_sl_quest_item_1014 exist=yes`

#### `fix_quest_story_id` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_quest_story_id] loaded v1.0.2`
- `[15:38:45.728] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[15:38:45.728] [fix_quest_story_id] loaded v1.0.2`
- `[15:38:51.228] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[15:38:51.820] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[15:38:51.854] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[15:39:03.027] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[15:39:03.065] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[15:39:03.067] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`
- `[15:40:09.339] [fix_quest_story_id] loaded v1.0.2`
- `[15:40:10.339] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[15:40:10.339] [fix_quest_story_id] loaded v1.0.2`
- Е х∙╕ 6 єэшъры№э√ї ёЄЁюъ

#### `fix_radio` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_radio] loaded v1.0.2`
- `[15:38:45.728] [fix_radio] loaded v1.0.2`
- `[15:40:09.339] [fix_radio] loaded v1.0.2`
- `[15:40:10.339] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` Ч чруЁєчшыё 

- `[15:38:44.538] [fix_replace_quest_corpse] loaded v1.0.1`
- `[15:38:44.538] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[15:38:45.728] [fix_replace_quest_corpse] loaded v1.0.1`
- `[15:40:09.339] [fix_replace_quest_corpse] loaded v1.0.1`
- `[15:40:09.339] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[15:40:10.339] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` Ч чруЁєчшыё 

- `[15:38:45.728] [fix_rogue_hostility] loaded v1.0.0`
- `[15:40:10.339] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_rx_bandage_dead] loaded v1.0.1`
- `[15:38:45.728] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[15:40:09.340] [fix_rx_bandage_dead] loaded v1.0.1`
- `[15:40:10.339] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[15:40:09.340] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_soc_nimble_flash] loaded v1.0.1`
- `[15:38:45.728] [fix_soc_nimble_flash] loaded v1.0.1`
- `[15:40:09.340] [fix_soc_nimble_flash] loaded v1.0.1`
- `[15:40:10.339] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_sort_tabs] loaded v1.0.0`
- `[15:40:09.340] [fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_st2_footstep] loaded v1.0.0`
- `[15:40:09.340] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` Ч чруЁєчшыё 

- `[15:38:45.728] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[15:38:45.728] [fix_stash_id_desync] loaded v1.0.2`
- `[15:39:10.198] [fix_stash_id_desync] cleared id=26404 reason=not_invbox spots=1 cache=false name=gt_package_artifact26404 section=gt_package_artifact`
- `[15:39:10.198] [fix_stash_id_desync] cleared id=26479 reason=not_invbox spots=1 cache=false name=gt_package_artifact26479 section=gt_package_artifact`
- `[15:39:10.412] [fix_stash_id_desync] repair done spots=2 cache_entries=0`
- `[15:40:10.339] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[15:40:10.339] [fix_stash_id_desync] loaded v1.0.2`
- `[15:40:26.409] [fix_stash_id_desync] cleared id=26404 reason=not_invbox spots=1 cache=false name=gt_package_artifact26404 section=gt_package_artifact`
- `[15:40:26.409] [fix_stash_id_desync] cleared id=26479 reason=not_invbox spots=1 cache=false name=gt_package_artifact26479 section=gt_package_artifact`
- `[15:40:26.478] [fix_stash_id_desync] repair done spots=2 cache_entries=0`

#### `fix_talents_pda_respec` Ч чруЁєчшыё 

- `[15:38:45.728] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[15:40:10.339] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_trade_craft_stock] loaded v1.0.0`
- `[15:40:09.340] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` Ч чруЁєчшыё 

- `[15:38:43.342] [fix_trader_restock_callback] trader_on_restock exists v1.0.3`
- `[15:38:45.375] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[15:38:45.375] [fix_trader_restock_callback] Send wrap installed`
- `[15:40:07.986] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[15:40:10.093] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_vows_ambush_stash] loaded v1.0.1`
- `[15:38:45.728] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[15:38:45.728] [fix_vows_ambush_stash] loaded v1.0.1`
- `[15:40:09.340] [fix_vows_ambush_stash] loaded v1.0.1`
- `[15:40:10.339] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[15:40:10.339] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[15:38:45.728] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[15:40:09.340] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[15:40:10.339] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[15:38:45.728] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[15:40:09.340] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[15:40:10.339] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[15:40:09.340] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` Ч чруЁєчшыё 

- `[15:38:44.539] [fix_x2_gravity_room] loaded v1.0.1`
- `[15:38:45.728] [fix_x2_gravity_room] loaded v1.0.1`
- `[15:40:09.340] [fix_x2_gravity_room] loaded v1.0.1`
- `[15:40:10.339] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` Ч чруЁєчшыё 

- `[15:38:45.728] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[15:40:10.339] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` Ч чруЁєчшыё 

- `[15:38:44.540] [fix_zat_b12_box] loaded v1.0.0`
- `[15:40:09.340] [fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` Ч чруЁєчшыё 

- `[15:38:44.987] [quickqk_task_complete] loaded v1.4.2`
- `[15:39:46.463] [QuickQK] action=force_complete | phase=before | task_id=simulation_task_31a | title=╧ЁхфрЄхы№ | details=reward_not_guaranteed`
- `[15:39:46.463] [QuickQK] action=force_complete | phase=success | task_id=simulation_task_31a | title=╧ЁхфрЄхы№ | details=none`
- `[15:40:09.774] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` Ч чруЁєчшыё 

- `[15:38:32.675] path:tooltip_control/hold_key, key:56, old:nil`
- `[15:38:32.675] path:tooltip_control/trigger_key, key:56, old:nil`
- `[15:38:47.023] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[15:38:47.023] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[15:38:47.049] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[15:39:25.590] path:tooltip_control/hold_key, key:56, old:56`
- `[15:39:25.590] path:tooltip_control/trigger_key, key:56, old:56`
- `[15:40:08.866] path:tooltip_control/hold_key, key:56, old:nil`
- `[15:40:08.866] path:tooltip_control/trigger_key, key:56, old:nil`
- `[15:40:10.517] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[15:40:10.517] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[15:40:10.532] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`

## ╩єфр ёьюЄЁхЄ№

- ┴ыюъ FATAL ERROR эх эрщфхэ: ышсю ыюу юЄ эюЁьры№эюую ёхрэёр, ышсю шуЁр єярыр схч чряшёш (яЁютхЁ№ ъюэхЎ Їрщыр тЁєўэє■).

## ╧ЁхфєяЁхцфхэш  (Єюя 15)

- x4 `! [15:38:32.N] ERROR item_combination | wrong section names`
- x4 `! [15:40:07.N] ERROR item_combination | wrong section names`
- x2 `! [15:38:07.N]  Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! [15:38:07.N]  Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_conc_h_04'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_dirt_h_01'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_dirt_h_02'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_dirt_h_03'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_dirt_h_04'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_wood_h_01'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_wood_h_02'`
- x2 `! [15:38:07.N]  Can't find sound 'material\shells\small_shell_wood_h_03'`

## ╧юёыхфэшх ёЄЁюъш ыюур (40)

```
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\exp_pfx_fog_night
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\effects\fog_stormy_dust
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\effects\fog_stormy_leaves_01
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\exp_pfx_fogdust_00
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\exp_pfx_fogdust_00
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\exp_pfx_fogdust_00
[15:40:33.600] [Wind_Leaves] Loaded OK: nature\fog_foggy_00
[15:40:33.600] [Wind_Leaves] Total unique particles loaded: 19
[15:40:33.600] [Wind_Leaves] play_underground valid particles: 6
[15:40:33.600] [Wind_Leaves] Particles initialized after 300 ticks
[15:40:33.600] [Wind_Leaves] Level changed: 'l10_red_forest', play_leaves=1
* [15:40:34.043]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=13.72/2.77/10.32/0.19 ms workers(pre/post/bones/game/lua-gc/vision)=0.64/1.30/0.89/4.04/1.28/0.08 ms max(total/frame/render/wait)=70.61/63.85/49.93/25.10 ms
* [15:40:34.043]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=1.30/2.23/1.36/31.01/10.08/0.92 ms
* [15:40:34.043]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.94/0.24/1.34 ms max=4.98/14.62/28.31 ms gc(calls/busy/postload)=2126/7/0
[15:40:35.653] Time continual is:149175
[15:40:35.653] [RAK Rank Knife Drops] using table [renegade_trainee_knife] for community [renegade] rank [trainee], entries [11]
[15:40:35.653] [RAK Rank Knife Drops] spawned [wpn_bat] on [sim_default_renegade_trader47583]
[15:40:35.657] stack trace:
[15:40:35.657] 
[15:40:35.660] SymInit: Symbol-SearchPath: '.;C:\Games\ANTHOLOGY\Anomaly-1.5.3-Anthology 2.1\bin;C:\Games\ANTHOLOGY\Anomaly-1.5.3-Anthology 2.1\bin;C:\Windows;C:\Windows\system32;', symOptions: 530, UserName: 'nikit'
[15:40:35.660] OS-Version: 6.2.9200 () 0x100-0x1
[15:40:35.783] C:\Games\ANTHOLOGY\Anomaly-1.5.3-Anthology 2.1\bin\AnomalyDX11AVX.exe:AnomalyDX11AVX.exe (0000000140000000), size: 48513024 (result: 0), SymType: 'PDB', PDB: '.\AnomalyDX11AVX.pdb'
[15:40:36.061] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (816): UnhandledFilter
[15:40:36.068] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\imotion_position.cpp (171): imotion_position::state_start
[15:40:36.075] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\CharacterPhysicsSupport.cpp (506): CCharacterPhysicsSupport::KillHit
[15:40:36.077] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\CharacterPhysicsSupport.cpp (548): CCharacterPhysicsSupport::in_Hit
[15:40:36.082] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\entity_alive.cpp (343): CEntityAlive::Die
[15:40:36.085] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\CustomMonster.cpp (743): CCustomMonster::Die
[15:40:36.087] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\Ai\Stalker\ai_stalker.cpp (613): CAI_Stalker::Die
[15:40:36.091] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\Entity.cpp (69): CEntity::OnEvent
[15:40:36.093] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\Ai\Stalker\ai_stalker_events.cpp (29): CAI_Stalker::OnEvent
[15:40:36.101] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\Level.cpp (1174): CLevel::ProcessGameEvents
[15:40:36.103] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\Level.cpp (1356): CLevel::OnFrame
[15:40:36.107] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\device.cpp (1216): CRenderDevice::FrameMove
[15:40:36.108] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\device.cpp (627): CRenderDevice::on_idle
[15:40:36.109] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\device.cpp (1143): CRenderDevice::Run
[15:40:36.110] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\x_ray.cpp (725): Startup
[15:40:36.111] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\x_ray.cpp (1353): WinMain_impl
[15:40:36.112] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrEngine\x_ray.cpp (1454): WinMain
[15:40:36.122] at address 0x0000000140482CB7
```

---

╨рчсюЁ тхф╕ь яю `workflow-crash`: ёэрўрыр ъырёё ш яхЁтюяЁшўшэр, Їшъё Ч Єюы№ъю яюёых яюфЄтхЁцфхэш .
