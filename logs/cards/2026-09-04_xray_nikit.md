# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (200 КБ, 2231 строк)
- Дата разбора: 2026-09-04
- Класс: **вылета в логе нет**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (3)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_autocomplete_drx_sl`
- `fix_bhs_fdda_loot`
- `fix_minigun_dead_parent`

### С отказами (1)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[21:50:11.915] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[21:50:11.915] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:50:13.221] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[21:50:30.205] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`

### В логе без отказов (58)

#### `anthology_busyhands_stability_fix` — загрузился

- `[21:50:11.932] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[21:50:12.243] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[21:50:12.875] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[21:50:12.876] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[21:50:12.876] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[21:50:12.876] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[21:50:12.876] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[21:50:12.876] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[21:50:12.876] [BusyHandsFix v0.6.6] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[21:50:12.876] [BusyHandsFix v0.6.6] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[21:50:12.876] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[21:50:12.876] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 27 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[21:50:12.919] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` — загрузился

- `[21:50:11.536] [campfires_anthology_compat] loaded v1.1.0`
- `* [21:50:31.247]  [load-session/lua-callbacks] #11 self=50.78 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`

#### `context_menu_overhaul_anthology` — загрузился

- `[21:50:13.216] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[21:50:30.996] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[21:50:30.999] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [21:50:31.247]  [load-session/lua-callbacks] #03 self=119.03 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`

#### `diag_log_spam` — загрузился

- `[21:50:10.195] [diag_log_spam] early printe hook`
- `[21:50:10.807] [diag_log_spam] init v1.2.3`
- `[21:50:12.879] [diag_log_spam] loaded v1.2.3 (wrappers active)`

#### `fix_arena_loadout` — загрузился

- `[21:50:13.221] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` — загрузился

- `[21:50:11.916] [fix_ashot_aw_travel] loaded v1.0.1`
- `[21:50:13.221] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- `[21:50:11.916] [fix_attribute_assistent] loaded v1.0.1`
- `[21:50:13.221] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` — загрузился

- `[21:50:13.221] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[21:50:18.590] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[21:50:18.990] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[21:50:29.411] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[21:50:29.438] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [21:50:31.247]  [load-session/lua-callbacks] #08 self=63.28 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`

#### `fix_charon_red_forest_travel` — загрузился

- `[21:50:11.916] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[21:50:13.221] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[21:50:13.221] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` — загрузился

- `[21:50:11.916] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[21:50:11.916] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[21:50:13.221] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_faction_trade_supply` — загрузился

- `[21:50:11.916] [fix_faction_trade_supply] loaded v1.0.0`
- `[21:50:13.221] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`

#### `fix_fdda_mcm_paths` — загрузился

- `[21:50:11.916] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- `[21:50:11.916] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- `[21:50:11.916] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- `[21:50:11.916] [fix_g2x_torch_meshes] loaded v1.0.0`

#### `fix_gigant_space_restriction` — загрузился

- `[21:50:11.917] [fix_gigant_space_restriction] loaded v1.1.1`
- `[21:50:13.221] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[21:50:13.221] [fix_gigant_space_restriction] loaded v1.1.1`
- `[21:50:18.456] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[21:50:18.457] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[21:50:18.514] [fix_gigant_space_restriction] quarantine id=3310 name=gigant_strong3310 section=gigant_strong reason=off_level`
- `[21:50:18.659] [fix_gigant_space_restriction] quarantine id=9852 name=gigant_normal9852 section=gigant_normal reason=off_level`
- `[21:50:18.683] [fix_gigant_space_restriction] quarantine id=10806 name=gigant_normal10806 section=gigant_normal reason=off_level`
- `[21:50:18.709] [fix_gigant_space_restriction] quarantine id=12058 name=gigant_weak12058 section=gigant_weak reason=off_level`
- `[21:50:18.709] [fix_gigant_space_restriction] quarantine id=12084 name=gigant_weak12084 section=gigant_weak reason=off_level`
- `[21:50:18.760] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- `[21:50:18.783] [fix_gigant_space_restriction] quarantine id=15720 name=gigant_weak15720 section=gigant_weak reason=off_level`
- … ещё 35 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[21:48:47.300] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[21:48:47.300] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[21:48:49.853] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`

#### `fix_grifon_visibility` — загрузился

- `[21:50:11.917] [fix_grifon_visibility] loaded v1.0.0`

#### `fix_hip_quest_text` — загрузился

- `[21:50:11.917] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- `[21:50:11.917] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_indeikam_breeding` — загрузился

- `[21:50:11.917] [fix_indeikam_breeding] loaded v1.0.0`

#### `fix_item_combination_magnifiers` — загрузился

- `[21:50:11.917] [fix_item_combination_magnifiers] loaded v1.0.0`

#### `fix_kupol_wrong_bone` — загрузился

- `[21:50:13.221] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[21:50:29.637] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [21:50:31.247]  [load-session/lua-callbacks] #09 self=60.27 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`

#### `fix_loot_space` — загрузился

- `[21:50:11.917] [fix_loot_space] loaded v1.0.1`
- `[21:50:13.221] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[21:50:13.222] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`

#### `fix_misc_script_errors` — загрузился

- `[21:48:47.301] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[21:49:01.417] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[21:50:11.917] [fix_misc_script_errors] loaded v1.0.2`
- `[21:50:13.222] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` — загрузился

- `[21:50:11.917] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- `[21:50:11.918] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[21:50:13.222] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- `[21:50:13.222] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[21:50:13.222] [fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` — загрузился

- `[21:50:11.918] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[21:50:11.918] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[21:50:13.222] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[21:50:11.918] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[21:50:13.222] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[21:50:13.222] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — есть строки

- `[21:50:11.918] [fix_quest_stash] загружен v1.0.4`
- `[21:50:13.222] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[21:50:13.222] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`

#### `fix_quest_story_id` — загрузился

- `[21:50:11.919] [fix_quest_story_id] loaded v1.0.2`
- `[21:50:13.222] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[21:50:13.222] [fix_quest_story_id] loaded v1.0.2`
- `[21:50:18.922] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[21:50:19.512] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[21:50:19.552] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[21:50:30.161] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[21:50:30.200] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[21:50:30.203] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`

#### `fix_radio` — загрузился

- `[21:50:11.919] [fix_radio] loaded v1.0.2`
- `[21:50:13.222] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` — загрузился

- `[21:50:11.919] [fix_replace_quest_corpse] loaded v1.0.1`
- `[21:50:11.919] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[21:50:13.222] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` — загрузился

- `[21:50:13.222] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[21:50:11.919] [fix_rx_bandage_dead] loaded v1.0.1`
- `[21:50:13.222] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- `[21:50:11.919] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` — загрузился

- `[21:50:11.920] [fix_soc_nimble_flash] loaded v1.0.1`
- `[21:50:13.222] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` — загрузился

- `[21:50:11.920] [fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` — загрузился

- `[21:50:11.920] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` — загрузился

- `[21:50:13.222] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[21:50:13.222] [fix_stash_id_desync] loaded v1.0.2`
- `[21:50:38.883] [fix_stash_id_desync] cleared id=26404 reason=not_invbox spots=1 cache=false name=gt_package_artifact26404 section=gt_package_artifact`
- `[21:50:38.883] [fix_stash_id_desync] cleared id=26479 reason=not_invbox spots=1 cache=false name=gt_package_artifact26479 section=gt_package_artifact`
- `[21:50:39.085] [fix_stash_id_desync] repair done spots=2 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- `[21:50:13.222] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` — загрузился

- `[21:50:11.920] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- `[21:50:10.808] [fix_trader_restock_callback] trader_on_restock exists v1.0.3`
- `[21:50:12.879] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[21:50:12.879] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` — загрузился

- `[21:50:11.920] [fix_vows_ambush_stash] loaded v1.0.1`
- `[21:50:13.222] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[21:50:13.222] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` — загрузился

- `[21:50:11.920] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[21:50:13.222] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` — загрузился

- `[21:50:11.920] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[21:50:13.222] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` — загрузился

- `[21:50:11.920] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- `[21:50:11.921] [fix_x2_gravity_room] loaded v1.0.1`
- `[21:50:13.222] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` — загрузился

- `[21:50:13.222] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- `[21:50:11.921] [fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- `[21:50:12.420] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- `[21:50:03.511] path:tooltip_control/hold_key, key:56, old:nil`
- `[21:50:03.511] path:tooltip_control/trigger_key, key:56, old:nil`
- `[21:50:14.542] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[21:50:14.542] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[21:50:14.566] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

## Предупреждения (топ 15)

- x4 `! [21:50:03.N] ERROR item_combination | wrong section names`
- x3 `~ [21:51:22.N]  ItemProcessor | nothing is passed to process!`
- x2 `! [21:48:47.N]  Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! [21:48:47.N]  Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_conc_h_04'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_dirt_h_01'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_dirt_h_02'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_dirt_h_03'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_dirt_h_04'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_wood_h_01'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_wood_h_02'`
- x2 `! [21:48:47.N]  Can't find sound 'material\shells\small_shell_wood_h_03'`

## Последние строки лога (40)

```
~ [21:51:22.242]  ItemProcessor | nothing is passed to process!
[21:51:22.242] [RAK Rank Knife Drops] using table [default_knife] for community [spectrum] rank [master], entries [1]
[21:51:22.242] [RAK Rank Knife Drops] roll failed [wpn_knife] chance [0.02]
* [21:51:24.827]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=20.43/3.75/16.36/0.01 ms workers(pre/post/bones/game/lua-gc/vision)=0.40/1.07/0.56/5.51/1.34/0.05 ms max(total/frame/render/wait)=26.27/11.62/20.19/1.75 ms
* [21:51:24.827]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=1.25/1.64/0.74/15.91/10.86/0.51 ms
* [21:51:24.827]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.13/0.24/2.40 ms max=13.08/5.23/9.63 ms gc(calls/busy/postload)=2032/2/0
[21:51:26.090] Time continual is:98266
~ [21:51:26.090]  Warfare is not loaded, unregistered warfare callbacks
* [21:51:30.927]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=20.26/3.48/16.48/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.20/1.13/0.53/4.25/1.38/0.05 ms max(total/frame/render/wait)=79.29/13.84/65.18/0.01 ms
* [21:51:30.927]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.60/1.94/0.84/15.68/10.16/0.69 ms
* [21:51:30.927]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.96/0.30/1.22 ms max=3.82/6.56/5.22 ms gc(calls/busy/postload)=2086/0/0
! [21:51:34.852]  Missing ogg-comment, file:  c:/games/anthology/anomaly-1.5.3-anthology 2.1/bin/..\gamedata\sounds\ambient\trx\nature\wind_gust\sound_04.ogg
* [21:51:36.815]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=19.52/3.60/15.62/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.17/1.14/0.56/4.49/1.37/0.06 ms max(total/frame/render/wait)=27.16/12.46/19.62/0.00 ms
* [21:51:36.815]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.50/2.06/0.77/14.52/10.69/0.78 ms
* [21:51:36.815]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.97/0.47/1.32 ms max=3.17/7.67/9.75 ms gc(calls/busy/postload)=2076/1/0
[21:51:36.862] Time continual is:109037
[21:51:36.862] Calculated FOV: 0
[21:51:37.803] [RAK Rank Knife Drops] using table [default_knife] for community [spectrum] rank [veteran], entries [1]
[21:51:37.803] [RAK Rank Knife Drops] roll failed [wpn_knife] chance [0.02]
* [21:51:39.602]  [Lua GC/xray-atomic] sequence=69 total=10.04 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.00/6.45/2.24/0.35 ms leaf(marked/unmarked/finalized)=5955381/295/5882404
[21:51:39.626] Time continual is:111803
[21:51:39.626] [RAK Rank Knife Drops] using table [default_knife] for community [spectrum] rank [legend], entries [1]
[21:51:39.626] [RAK Rank Knife Drops] roll failed [wpn_knife] chance [0.02]
* [21:51:42.698]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=19.51/4.02/15.21/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.40/1.19/0.51/5.66/1.31/0.05 ms max(total/frame/render/wait)=33.24/19.00/19.73/1.17 ms
* [21:51:42.698]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=1.77/1.90/0.74/15.78/10.77/0.91 ms
* [21:51:42.698]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.87/0.35/2.66 ms max=4.05/6.29/10.81 ms gc(calls/busy/postload)=2078/2/0
[21:51:44.128] Time continual is:116306
[21:51:44.128] Calculated FOV: 0
* [21:51:45.179]  [Lua GC/xray-atomic] sequence=75 total=12.76 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/2.68/7.05/2.24/0.79 ms leaf(marked/unmarked/finalized)=6208614/322/6142992
[21:51:46.210] Time continual is:118384
[21:51:46.210] [RAK Rank Knife Drops] using table [bandit_expert_knife] for community [bandit] rank [expert], entries [11]
[21:51:46.211] [RAK Rank Knife Drops] spawned [wpn_bat] on [sim_default_bandit_315214]
[21:51:46.353] [AT] Autocompleting task: simulation_task_31a
/ [21:51:46.381]  Goodwill (main) gained with stalker: 50
/ [21:51:46.381]  Goodwill (side) gained with killer: 14
[21:51:46.381] DRX SL task ended: simulation_task_31a
[21:51:46.381] DRX SL: drx_sl_task_giver_2062 unregistered (0 outstanding)
* [21:51:47.759]  [mt-frame/profile] frames=300 avg(total/frame/render/wait)=16.72/3.91/12.49/0.02 ms workers(pre/post/bones/game/lua-gc/vision)=0.17/1.12/0.49/4.01/1.35/0.04 ms max(total/frame/render/wait)=33.17/21.21/20.15/2.03 ms
* [21:51:47.759]  [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.35/1.99/0.70/16.85/13.81/0.63 ms
* [21:51:47.759]  [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.70/0.23/1.19 ms max=3.34/5.76/12.79 ms gc(calls/busy/postload)=2079/1/0
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
