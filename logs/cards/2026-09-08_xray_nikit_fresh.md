# Карточка лога — xray_nikit_fresh.log

- Файл: `xray_nikit_fresh.log` (450 КБ, 3511 строк)
- Дата разбора: 2026-09-08
- Класс: **Lua error (pcall)**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (6)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_dynamic_armor_visuals_nil`
- `fix_faction_trade_supply`
- `fix_hostage_task_collision`
- `fix_minigun_dead_parent`
- `fix_wtf_fetch_counter`

### С отказами (1)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[08:48:16.660] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[08:48:16.660] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[08:48:20.440] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[08:49:09.446] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`

### В логе без отказов (59)

#### `anthology_busyhands_stability_fix` — загрузился

- `[08:48:17.235] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[08:48:17.698] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[08:48:19.927] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[08:48:19.928] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[08:48:19.928] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[08:48:19.928] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[08:48:19.928] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[08:48:19.928] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[08:48:19.929] [BusyHandsFix v0.6.10] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[08:48:19.929] [BusyHandsFix v0.6.10] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[08:48:19.929] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[08:48:19.929] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 27 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[08:48:19.935] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` — загрузился

- `[08:48:15.992] [campfires_anthology_compat] loaded v1.1.0`

#### `context_menu_overhaul_anthology` — загрузился

- `[08:48:20.431] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[08:49:07.744] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[08:49:07.748] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`

#### `diag_log_spam` — загрузился

- `[08:48:06.814] [diag_log_spam] early printe hook`
- `[08:48:07.917] [diag_log_spam] init v1.2.3`
- `[08:48:19.933] [diag_log_spam] loaded v1.2.3 (wrappers active)`

#### `diag_pda_task_hint` — загрузился

- `[08:48:16.042] [diag_pda_task_hint] init v1.0.0 (DIAGNOSTIC ONLY)`
- `[08:48:20.431] [diag_pda_task_hint] wrapped task_functor.anomaly_scanner_task_target`
- `[08:48:20.431] [diag_pda_task_hint] diagnostics active v1.0.0`
- `[08:49:09.289] [diag_pda_task_hint] === task dump reason=actor_on_first_update level=la14_rostok_factory ===`
- `[08:49:09.289] [diag_pda_task_hint] scanner_device story=nil (not in alife / not spawned)`
- `[08:49:09.289] [diag_pda_task_hint] task id=simulation_task_61 stage=3 giver=55082 status_fn=measure_task target_fn=general_measure descr_fn=general_measure_desc`
- `[08:49:09.289] [diag_pda_task_hint] task id=simulation_task_61 current_target=55082 current_title=simulation_task_61_name hint_len=272 bad_ctrl=0 preview="Мне встретился какой-то неизвестный сталкер, который попросил пом`
- `[08:49:09.289] [diag_pda_task_hint] task id=simulation_task_61 saved_anom=table: 0x168e4aa8`
- `[08:49:09.289] [diag_pda_task_hint] task id=simulation_task_61 anomaly_zone MISSING in db.anomaly_by_name`
- `[08:49:09.289] [diag_pda_task_hint] task id=simulation_task_61 engine_get_task=true`
- `[08:49:09.366] [diag_pda_task_hint] WRAP functor task=simulation_task_61 field=target stage=3 result=55082 id=55082 name=sim_default_isg_medic55082 clsid=35`
- `[08:49:09.440] [diag_pda_task_hint] WRAP functor task=simulation_task_61 field=descr stage=3 result=Доложить об успешной установке оборудования. hint_len=44 bad_ctrl=0 preview="Доложить об успешной установке оборудования`
- … ещё 3 уникальных строк

#### `fix_arena_loadout` — загрузился

- `[08:48:20.440] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_arti_frames_nil` — загрузился

- `[08:48:16.661] [fix_arti_frames_nil] loaded v1.0.0`
- `[08:48:20.440] [fix_arti_frames_nil] guard installed v1.0.0`

#### `fix_ashot_aw_travel` — загрузился

- `[08:48:16.662] [fix_ashot_aw_travel] loaded v1.0.1`
- `[08:48:20.440] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- `[08:48:16.662] [fix_attribute_assistent] loaded v1.0.1`
- `[08:48:20.440] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` — загрузился

- `[08:48:20.440] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[08:48:28.147] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[08:48:28.838] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[08:49:09.456] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[08:49:09.477] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`

#### `fix_charon_red_forest_travel` — загрузился

- `[08:48:16.663] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[08:48:20.440] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[08:48:20.440] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` — загрузился

- `[08:48:16.664] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[08:48:16.664] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[08:48:20.440] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_fdda_mcm_paths` — загрузился

- `[08:48:16.664] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- `[08:48:16.664] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- `[08:48:16.664] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- `[08:48:16.664] [fix_g2x_torch_meshes] loaded v1.0.0`

#### `fix_gigant_space_restriction` — загрузился

- `[08:48:16.666] [fix_gigant_space_restriction] loaded v1.1.1`
- `[08:48:20.440] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[08:48:20.440] [fix_gigant_space_restriction] loaded v1.1.1`
- `[08:48:28.136] [fix_gigant_space_restriction] quarantine id=6486 name=gigant_strong6486 section=gigant_strong reason=off_level`
- `[08:48:28.191] [fix_gigant_space_restriction] quarantine id=7886 name=gigant_normal7886 section=gigant_normal reason=off_level`
- `[08:48:28.286] [fix_gigant_space_restriction] quarantine id=10092 name=gigant_strong10092 section=gigant_strong reason=off_level`
- `[08:48:28.332] [fix_gigant_space_restriction] quarantine id=11256 name=gigant_normal11256 section=gigant_normal reason=off_level`
- `[08:48:28.478] [fix_gigant_space_restriction] quarantine id=15184 name=gigant_normal15184 section=gigant_normal reason=off_level`
- `[08:48:28.504] [fix_gigant_space_restriction] quarantine id=15753 name=gigant_strong15753 section=gigant_strong reason=off_level`
- `[08:48:28.527] [fix_gigant_space_restriction] quarantine id=16174 name=gigant_strong16174 section=gigant_strong reason=off_level`
- `[08:48:28.606] [fix_gigant_space_restriction] quarantine id=18388 name=gigant_strong18388 section=gigant_strong reason=off_level`
- `[08:48:28.636] [fix_gigant_space_restriction] quarantine id=19142 name=gigant_normal19142 section=gigant_normal reason=off_level`
- … ещё 34 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[08:45:00.600] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[08:45:00.600] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[08:45:06.883] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`

#### `fix_grifon_visibility` — загрузился

- `[08:48:16.666] [fix_grifon_visibility] loaded v1.0.0`

#### `fix_hip_quest_text` — загрузился

- `[08:48:16.666] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- `[08:48:16.666] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_indeikam_breeding` — загрузился

- `[08:48:16.666] [fix_indeikam_breeding] loaded v1.0.0`

#### `fix_item_combination_magnifiers` — загрузился

- `[08:48:16.666] [fix_item_combination_magnifiers] loaded v1.0.0`

#### `fix_kupol_wrong_bone` — загрузился

- `[08:48:20.440] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[08:49:09.541] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`

#### `fix_loot_space` — загрузился

- `[08:48:16.667] [fix_loot_space] loaded v1.0.1`
- `[08:48:20.440] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[08:48:20.440] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`

#### `fix_misc_script_errors` — загрузился

- `[08:45:00.600] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[08:45:33.743] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[08:48:16.668] [fix_misc_script_errors] loaded v1.0.2`
- `[08:48:20.441] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` — загрузился

- `[08:48:16.668] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- `[08:48:16.668] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:48:20.441] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- `[08:48:20.441] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[08:48:20.441] [fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` — загрузился

- `[08:48:16.669] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[08:48:16.669] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[08:48:20.441] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[08:48:16.670] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[08:48:20.441] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[08:48:20.441] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — есть строки

- `[08:48:16.671] [fix_quest_stash] загружен v1.0.4`
- `[08:48:20.441] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[08:48:20.441] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[08:49:10.406] [fix_quest_stash] задание готово task=ratniy_task_8 section=drx_sl_quest_item_1022 reason=actor_has_canonical`

#### `fix_quest_story_id` — загрузился

- `[08:48:16.672] [fix_quest_story_id] loaded v1.0.2`
- `[08:48:20.441] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[08:48:20.441] [fix_quest_story_id] loaded v1.0.2`
- `[08:48:28.734] [fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- `[08:48:28.999] [fix_quest_story_id] kept first object 17703 for repeated story_id jup_a9_dogs_normal`
- `[08:49:06.252] [fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- `[08:49:06.272] [fix_quest_story_id] kept first object 17703 for repeated story_id jup_a9_dogs_normal`

#### `fix_radio` — загрузился

- `[08:48:16.673] [fix_radio] loaded v1.0.2`
- `[08:48:20.441] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` — загрузился

- `[08:48:16.673] [fix_replace_quest_corpse] loaded v1.0.1`
- `[08:48:16.673] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[08:48:20.441] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` — загрузился

- `[08:48:20.441] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[08:48:16.674] [fix_rx_bandage_dead] loaded v1.0.1`
- `[08:48:20.441] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- `[08:48:16.674] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` — загрузился

- `[08:48:16.675] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:48:20.441] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` — загрузился

- `[08:48:16.675] [fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` — загрузился

- `[08:48:16.675] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` — загрузился

- `[08:48:20.441] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[08:48:20.441] [fix_stash_id_desync] loaded v1.0.2`
- `[08:49:12.242] [fix_stash_id_desync] repair done spots=0 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- `[08:48:20.441] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` — загрузился

- `[08:48:16.676] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- `[08:48:07.918] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[08:48:19.933] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` — загрузился

- `[08:48:16.677] [fix_vows_ambush_stash] loaded v1.0.1`
- `[08:48:20.441] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[08:48:20.441] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` — загрузился

- `[08:48:16.678] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:48:20.441] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` — загрузился

- `[08:48:16.679] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[08:48:20.441] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` — загрузился

- `[08:48:16.679] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- `[08:48:16.679] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:48:20.441] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` — загрузился

- `[08:48:20.441] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- `[08:48:16.680] [fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- `[08:48:19.007] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- `[08:45:59.186] path:tooltip_control/hold_key, key:56, old:nil`
- `[08:45:59.186] path:tooltip_control/trigger_key, key:56, old:nil`
- `[08:48:20.851] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[08:48:20.853] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=fps keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[08:48:20.888] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`

## FATAL ERROR

```
FATAL ERROR
[error]Expression    : <no expression>
[error]Function      : CScriptEngine::lua_pcall_failed
[error]File          : X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrServerEntities\script_engine.cpp
[error]Line          : 378
[error]Description   : fatal error
[error]Arguments     :
1 : [Lua] ...logy 2.1/bin/..\gamedata\scripts\faction_trade_ui.script(32) : UpdateHarukaTradeWindow
LUA error: ...logy 2.1/bin/..\gamedata\scripts\faction_trade_ui.script:32: attempt to concatenate global 'supply_level' (a function value)
Check log for details
[08:49:43.634] stack trace:
! [08:49:43.634]  [LUA]  0 : [C  ] __concat
! [08:49:43.634]  [LUA]  1 : [Lua] ...logy 2.1/bin/..\gamedata\scripts\faction_trade_ui.script(32) : UpdateHarukaTradeWindow
! [08:49:43.634]  [LUA]  2 : [Lua] ...logy 2.1/bin/..\gamedata\scripts\faction_trade_ui.script(24) : ResetHaruka
! [08:49:43.634]  [LUA]  3 : [Lua] ...logy 2.1/bin/..\gamedata\scripts\faction_trade_ui.script(47) : func_or_userdata
! [08:49:43.634]  [LUA]  4 : [Lua] ....3-anthology 2.1/bin/..\gamedata\scripts\axr_main.script(284) : make_callback
! [08:49:43.634]  [LUA]  5 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(118) : SendScriptCallback
! [08:49:43.634]  [LUA]  6 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(150) : Register_UI
! [08:49:43.634]  [LUA]  7 : [Lua] ...nthology 2.1/bin/..\gamedata\scripts\ui_inventory.script(486) : baseUIS
! [08:49:43.634]  [LUA]  8 : [Lua] ...n/..\gamedata\scripts\liz_fdda_redone_body_search.script(59) : og_inventory_start
! [08:49:43.634]  [LUA]  9 : [Lua] ...gy 2.1/bin/..\gamedata\scripts\z_new_sorting_tabs.script(5) : base_ui_inventory_start
! [08:49:43.634]  [LUA] 10 : [Lua] ...1/bin/..\gamedata\scripts\z_ui_inventory_dotmarks.script(33) : base_ui_start
! [08:49:43.634]  [LUA] 11 : [Lua] ...ology 2.1/bin/..\gamedata\scripts\anomalous_stash.script(44) : start
! [08:49:43.634]  [LUA] 12 : [Lua] ...nthology 2.1/bin/..\gamedata\scripts\ui_inventory.script(412) : func_or_userdata
! [08:49:43.634]  [LUA] 13 : [Lua] ....3-anthology 2.1/bin/..\gamedata\scripts\axr_main.script(284) : make_callback
! [08:49:43.634]  [LUA] 14 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(118) : SendScriptCallback
! [08:49:43.634]  [LUA] 15 : [Lua] ... 2.1/bin/..\gamedata\scripts\actor_menu_inventory.script(67) :
! [08:49:43.634]  [LUA] 16 : [C  ] start_trade
! [08:49:43.634]  [LUA] 17 : [Lua] ...5.3-anthology 2.1/bin/..\gamedata\scripts\dialogs.script(606) :
[08:49:43.634]
[08:49:43.650] SymInit: Symbol-SearchPath: '.;C:\Games\ANTHOLOGY\Anomaly-1.5.3-Anthology 2.1\bin;C:\Games\ANTHOLOGY\Anomaly-1.5.3-Anthology 2.1\bin;C:\Windows;C:\Windows\system32;', symOptions: 530, UserName: 'nikit'
[08:49:43.650] OS-Version: 6.2.9200 () 0x100-0x1
[08:49:44.599] C:\Games\ANTHOLOGY\Anomaly-1.5.3-Anthology 2.1\bin\AnomalyDX11AVX.exe:AnomalyDX11AVX.exe (0000000140000000), size: 48513024 (result: 0), SymType: 'PDB', PDB: '.\AnomalyDX11AVX.pdb'
[08:49:45.230] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (214): xrDebug::gather_info
[08:49:45.235] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (268): xrDebug::backend
[08:49:45.236] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (499): xrDebug::fatal
[08:49:45.244] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrServerEntities\script_engine.cpp (380): CScriptEngine::lua_pcall_failed
[08:49:45.256] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (565): lj_err_run
[08:49:45.261] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (580): err_msgv
[08:49:45.261] X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (614): lj_err_optype
```

## Куда смотреть

- Класс: Lua error из-под pcall (`CScriptEngine::lua_pcall_failed`).
- Это не обычный lua_error: ошибка всплыла из pcall и всё равно стала fatal. Разбирай, какой pcall это был и что дальше по стеку.
- Несколько Lua-ошибок подряд — первая по времени, остальные часто каскад.

## Предупреждения (топ 15)

- x18 `! [08:48:25.N]  Can't create entity 'stalker_sim_squad_service_trader'`
- x15 `! [08:48:24.N]  Can't create entity 'mag_nato_5.56x45_default'`
- x14 `! [08:48:25.N]  Can't create entity 'stalker_sim_squad_service_tech'`
- x11 `! [08:48:24.N]  Can't create entity 'mag_beretta_9x19_default'`
- x11 `! [08:48:25.N]  Can't create entity 'mag_beretta_9x19_default'`
- x10 `! [08:48:25.N]  Can't create entity 'mag_glock_33_9x19_default'`
- x10 `! [08:48:25.N]  Can't create entity 'mag_glock_33_9x18_alt'`
- x9 `! [08:48:25.N]  Can't create entity 'mag_ak_7.62x39_default'`
- x9 `! [08:48:25.N]  Can't create entity 'mag_beretta_9x18_alt'`
- x9 `! [08:48:25.N]  Can't create entity 'mag_walther_9x19_default'`
- x8 `! [08:48:25.N]  Can't create entity 'mag_ak_5.45x39_default'`
- x8 `! [08:48:25.N]  Can't create entity 'mag_kriss_9x19_default'`
- x8 `! [08:48:25.N]  Can't create entity 'mag_galil_7.62x51_default'`
- x8 `! [08:48:25.N]  Can't create entity 'mag_akalfa_5.56x45_bas'`
- x8 `! [08:48:25.N]  Can't create entity 'mag_glock_9x19_default'`

## Строки перед падением (40)

```
[08:49:43.353] saved condition for af_bloo_af_aac 1
[08:49:43.353] saved condition for af_gold_fish_breeding_2_af_aam 1
[08:49:43.353] saved condition for af_oasis_heart 1
[08:49:43.353] saved condition for af_chertyaico 1
[08:49:43.355] saved condition for af_frames_up 1
[08:49:43.356] saved condition for af_medallion 1
[08:49:43.356] saved condition for af_vyvert_green 1
[08:49:43.356] saved condition for hide_lurker 0.52999997138977
[08:49:43.356] saved condition for hide_flesh 0.69999998807907
[08:49:43.356] saved condition for af_frames 1
[08:49:43.357] saved condition for af_freon 1
[08:49:43.357] saved condition for af_cooler_up 1
[08:49:43.357] saved condition for af_frames 1
[08:49:43.357] saved condition for af_cooler 1
[08:49:43.357] saved condition for af_frames_up 1
[08:49:43.357] saved condition for af_freon_up 1
[08:49:43.357] saved condition for af_grid 1
[08:49:43.357] saved condition for af_grid 1
[08:49:43.357] saved condition for af_grid_up 1
[08:49:43.357] saved condition for hide_bloodsucker 0.75999999046326
[08:49:43.357] saved condition for af_crystal_vyvert 1
[08:49:43.357] saved condition for af_vedsleza3 1
[08:49:43.357] saved condition for hide_bloodsucker 0.68999999761581
[08:49:43.357] saved condition for af_vyvert3 1
# [08:49:43.358]  SAVING: Sleep deprivation | last_sleep: 2451.2
# [08:49:43.358]  SAVING: Water deprivation | last_drink: 3530
[08:49:43.358] [id_cleaner_anthology] save_state: initialized=true running=false saved_initialized=true tracked numeric=0 mapped=485 spawn=14906 restore=0 last_released=0 last_spawned=0 retired=0
# [08:49:43.358]  SAVING: NPC items | number of saved npcs: 0
! [08:49:43.380] -demonized_mugging_squads # SAVING: Mugging Squad | [last_spawn_time]: table: 0x179baaa0
! [08:49:43.380] -demonized_mugging_squads # SAVING: Mugging Squad | [version]: 2
! [08:49:43.380] -demonized_mugging_squads # SAVING: Mugging Squad | [active_squads]: table: 0x16957b68
# [08:49:43.381]  SAVING: Bounty Squad | [last_spawn_time]: table: 0x146f40f8
# [08:49:43.381]  SAVING: Bounty Squad | [active_squads]: table: 0x15fa1898
# [08:49:43.381]  SAVING: level_weather | cycle: rain - preset: w_rain3 - is_underground: false - weather_storage size: 3
[08:49:43.381] WeatherManager.save_state saving fields self.weather_file w_rain3, self.last_weather_file w_preblowout, self.weather_weight 0.93485349416733, self.cycle rain, self.last_cycle cloudy, self.next_weather w_rain3, self.curr_weather w_rain3
* [08:49:43.451]  Saving spawns...
* [08:49:43.457]  Saving objects...
* [08:49:43.586]  48191 objects are successfully saved
* [08:49:43.634]  Game fatal_ctd_save_2.scop is successfully saved to file 'c:/games/anthology/anomaly-1.5.3-anthology 2.1/bin/..\appdata\savedgames\fatal_ctd_save_2.scop'
[08:49:43.634] 
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
