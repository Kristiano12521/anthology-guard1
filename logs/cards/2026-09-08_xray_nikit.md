# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (20.8 МБ, 259376 строк)
- Дата разбора: 2026-09-08
- Класс: **вылета нет, есть повторяющиеся ошибки (1 групп)**
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

- `[07:17:29.650] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[07:17:29.650] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:17:33.222] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:18:27.024] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:21:50.914] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[07:21:50.914] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:21:54.348] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:22:24.186] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:23:07.049] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[07:23:07.049] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:23:10.467] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[07:23:44.989] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- … ещё 83 уникальных строк

### В логе без отказов (57)

#### `anthology_busyhands_stability_fix` — загрузился

- `[07:17:30.238] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[07:17:30.723] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[07:17:32.709] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[07:17:32.710] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[07:17:32.710] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[07:17:32.710] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[07:17:32.710] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[07:17:32.710] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[07:17:32.711] [BusyHandsFix v0.6.10] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[07:17:32.711] [BusyHandsFix v0.6.10] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[07:17:32.711] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[07:17:32.711] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 924 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[07:17:32.717] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[07:21:53.897] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[07:23:10.016] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:25:05.803] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:27:22.114] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:37:03.786] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:43:18.585] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:45:17.594] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:46:48.670] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:48:22.579] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:50:13.932] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[08:51:57.347] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- … ещё 12 уникальных строк

#### `campfires_anthology_compat` — загрузился

- `[07:17:29.046] [campfires_anthology_compat] loaded v1.1.0`
- `[07:21:50.219] [campfires_anthology_compat] loaded v1.1.0`
- `[07:23:06.364] [campfires_anthology_compat] loaded v1.1.0`
- `[08:25:01.948] [campfires_anthology_compat] loaded v1.1.0`
- `[08:27:18.407] [campfires_anthology_compat] loaded v1.1.0`
- `[08:37:00.137] [campfires_anthology_compat] loaded v1.1.0`
- `[08:43:14.867] [campfires_anthology_compat] loaded v1.1.0`
- `[08:45:13.879] [campfires_anthology_compat] loaded v1.1.0`
- `[08:46:44.951] [campfires_anthology_compat] loaded v1.1.0`
- `[08:48:18.910] [campfires_anthology_compat] loaded v1.1.0`
- `[08:50:10.267] [campfires_anthology_compat] loaded v1.1.0`
- `[08:51:53.693] [campfires_anthology_compat] loaded v1.1.0`
- … ещё 23 уникальных строк

#### `context_menu_overhaul_anthology` — загрузился

- `[07:17:33.213] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[07:18:25.212] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[07:18:25.217] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `[07:21:54.344] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[07:22:22.767] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[07:22:22.770] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `[07:23:10.463] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[07:23:43.515] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[07:23:43.519] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `[08:25:06.257] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[08:25:38.428] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[08:25:38.434] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- … ещё 58 уникальных строк

#### `diag_log_spam` — загрузился

- x2 `[07:21:40.733] [diag_log_spam]   [C]: in function '__index'`
- x2 `[07:22:57.158] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:24:50.316] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:27:09.084] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:36:50.839] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:43:05.512] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:45:04.519] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:46:35.593] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:48:09.753] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:50:01.079] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:51:44.507] [diag_log_spam]   [C]: in function '__index'`
- x2 `[08:53:18.221] [diag_log_spam]   [C]: in function '__index'`
- … ещё 220 уникальных строк

#### `fix_arena_loadout` — загрузился

- `[07:17:33.222] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[07:21:54.348] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[07:23:10.467] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:25:06.261] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:27:22.569] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:37:04.237] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:43:19.038] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:45:18.048] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:46:49.160] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:48:23.031] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:50:14.384] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[08:51:57.800] [fix_arena_loadout] bar_arena_teleport wrapped`
- … ещё 12 уникальных строк

#### `fix_ashot_aw_travel` — загрузился

- `[07:17:29.651] [fix_ashot_aw_travel] loaded v1.0.1`
- `[07:17:33.222] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[07:21:50.915] [fix_ashot_aw_travel] loaded v1.0.1`
- `[07:21:54.348] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[07:23:07.049] [fix_ashot_aw_travel] loaded v1.0.1`
- `[07:23:10.467] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[08:25:02.665] [fix_ashot_aw_travel] loaded v1.0.1`
- `[08:25:06.261] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[08:27:19.118] [fix_ashot_aw_travel] loaded v1.0.1`
- `[08:27:22.569] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[08:37:00.824] [fix_ashot_aw_travel] loaded v1.0.1`
- `[08:37:04.237] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- … ещё 36 уникальных строк

#### `fix_attribute_assistent` — загрузился

- `[07:17:29.651] [fix_attribute_assistent] loaded v1.0.1`
- `[07:17:33.222] [fix_attribute_assistent] loaded v1.0.1`
- `[07:21:50.915] [fix_attribute_assistent] loaded v1.0.1`
- `[07:21:54.348] [fix_attribute_assistent] loaded v1.0.1`
- `[07:23:07.049] [fix_attribute_assistent] loaded v1.0.1`
- `[07:23:10.467] [fix_attribute_assistent] loaded v1.0.1`
- `[08:25:02.665] [fix_attribute_assistent] loaded v1.0.1`
- `[08:25:06.261] [fix_attribute_assistent] loaded v1.0.1`
- `[08:27:19.118] [fix_attribute_assistent] loaded v1.0.1`
- `[08:27:22.569] [fix_attribute_assistent] loaded v1.0.1`
- `[08:37:00.824] [fix_attribute_assistent] loaded v1.0.1`
- `[08:37:04.237] [fix_attribute_assistent] loaded v1.0.1`
- … ещё 36 уникальных строк

#### `fix_aver_darkvalley` — загрузился

- `[07:17:33.222] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[07:17:40.317] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[07:17:41.141] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[07:18:27.037] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[07:18:27.061] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `[07:21:54.348] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[07:22:00.977] [fix_aver_darkvalley] rewrote dest route=darkvalley_to_aver id=6759 -367.536285, 6.280872, -431.521545 -> 388.674194, -9.332470, -318.518494 gvid=6205 lvid=1490468 dest_level=aver reason=server_entity_on_r`
- `[07:22:01.982] [fix_aver_darkvalley] rewrote dest route=aver_to_darkvalley id=24354 -157.581833, -0.140619, -433.517090 -> -94.382782, -2.695015, -39.998577 gvid=1899 lvid=56202 dest_level=l04_darkvalley reason=server_en`
- `[07:22:24.196] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[07:22:24.231] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24354 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `[07:23:10.467] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[07:23:14.513] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- … ещё 106 уникальных строк

#### `fix_charon_red_forest_travel` — загрузился

- `[07:17:29.651] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[07:17:33.222] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[07:21:50.916] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[07:21:54.348] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[07:23:07.050] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[07:23:10.467] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[08:25:02.666] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[08:25:06.261] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[08:27:19.118] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[08:27:22.569] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[08:37:00.826] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[08:37:04.237] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- … ещё 36 уникальных строк

#### `fix_crowkiller_hello` — загрузился

- `[07:17:33.222] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[07:21:54.348] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[07:23:10.467] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:25:06.261] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:27:22.569] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:37:04.237] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:43:19.038] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:45:18.048] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:46:49.160] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:48:23.032] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:50:14.384] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[08:51:57.800] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- … ещё 12 уникальных строк

#### `fix_dome_quest` — загрузился

- `[07:17:29.651] [fix_dome_quest] loaded v1.0.0`
- `[07:21:50.916] [fix_dome_quest] loaded v1.0.0`
- `[07:23:07.051] [fix_dome_quest] loaded v1.0.0`
- `[08:25:02.667] [fix_dome_quest] loaded v1.0.0`
- `[08:27:19.118] [fix_dome_quest] loaded v1.0.0`
- `[08:37:00.826] [fix_dome_quest] loaded v1.0.0`
- `[08:43:15.585] [fix_dome_quest] loaded v1.0.0`
- `[08:45:14.597] [fix_dome_quest] loaded v1.0.0`
- `[08:46:45.674] [fix_dome_quest] loaded v1.0.0`
- `[08:48:19.596] [fix_dome_quest] loaded v1.0.0`
- `[08:50:10.969] [fix_dome_quest] loaded v1.0.0`
- `[08:51:54.376] [fix_dome_quest] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[07:17:29.652] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[07:17:33.222] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[07:21:50.916] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[07:21:54.348] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[07:23:07.051] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[07:23:10.467] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[08:25:02.667] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[08:25:06.261] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[08:27:19.118] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[08:27:22.569] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[08:37:00.826] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[08:37:04.237] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- … ещё 36 уникальных строк

#### `fix_fdda_mcm_paths` — загрузился

- `[07:17:29.652] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[07:21:50.917] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[07:23:07.051] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:25:02.667] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:27:19.118] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:37:00.826] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:43:15.586] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:45:14.597] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:46:45.675] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:48:19.596] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:50:10.969] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[08:51:54.376] [fix_fdda_mcm_paths] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_fetch_headlamp` — загрузился

- `[07:17:29.652] [fix_fetch_headlamp] loaded v1.0.0`
- `[07:21:50.917] [fix_fetch_headlamp] loaded v1.0.0`
- `[07:23:07.051] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:25:02.667] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:27:19.118] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:37:00.826] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:43:15.586] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:45:14.597] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:46:45.675] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:48:19.596] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:50:10.969] [fix_fetch_headlamp] loaded v1.0.0`
- `[08:51:54.376] [fix_fetch_headlamp] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_flst_joker_door` — загрузился

- `[07:17:29.652] [fix_flst_joker_door] loaded v1.0.0`
- `[07:21:50.917] [fix_flst_joker_door] loaded v1.0.0`
- `[07:23:07.051] [fix_flst_joker_door] loaded v1.0.0`
- `[08:25:02.667] [fix_flst_joker_door] loaded v1.0.0`
- `[08:27:19.118] [fix_flst_joker_door] loaded v1.0.0`
- `[08:37:00.826] [fix_flst_joker_door] loaded v1.0.0`
- `[08:43:15.586] [fix_flst_joker_door] loaded v1.0.0`
- `[08:45:14.597] [fix_flst_joker_door] loaded v1.0.0`
- `[08:46:45.675] [fix_flst_joker_door] loaded v1.0.0`
- `[08:48:19.596] [fix_flst_joker_door] loaded v1.0.0`
- `[08:50:10.969] [fix_flst_joker_door] loaded v1.0.0`
- `[08:51:54.377] [fix_flst_joker_door] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_g2x_torch_meshes` — загрузился

- `[07:17:29.652] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[07:21:50.917] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[07:23:07.051] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:25:02.667] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:27:19.119] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:37:00.826] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:43:15.586] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:45:14.597] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:46:45.675] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:48:19.596] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:50:10.969] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[08:51:54.377] [fix_g2x_torch_meshes] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_gigant_space_restriction` — загрузился

- `[07:17:29.652] [fix_gigant_space_restriction] loaded v1.1.1`
- `[07:17:33.222] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[07:17:33.222] [fix_gigant_space_restriction] loaded v1.1.1`
- `[07:17:40.039] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[07:17:40.039] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[07:17:40.162] [fix_gigant_space_restriction] quarantine id=3310 name=gigant_strong3310 section=gigant_strong reason=off_level`
- `[07:17:40.550] [fix_gigant_space_restriction] quarantine id=10031 name=gigant_weak10031 section=gigant_weak reason=off_level`
- `[07:17:40.557] [fix_gigant_space_restriction] quarantine id=10181 name=gigant_weak10181 section=gigant_weak reason=off_level`
- `[07:17:40.586] [fix_gigant_space_restriction] quarantine id=10806 name=gigant_normal10806 section=gigant_normal reason=off_level`
- `[07:17:40.632] [fix_gigant_space_restriction] quarantine id=12058 name=gigant_weak12058 section=gigant_weak reason=off_level`
- `[07:17:40.633] [fix_gigant_space_restriction] quarantine id=12084 name=gigant_weak12084 section=gigant_weak reason=off_level`
- `[07:17:40.739] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- … ещё 752 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[07:15:36.374] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[07:15:36.374] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[07:15:42.300] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`
- `[07:21:39.581] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[07:21:39.581] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[07:22:56.024] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[07:22:56.024] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[08:24:48.315] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[08:24:48.315] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[08:27:07.939] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[08:27:07.939] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[08:36:49.694] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- … ещё 37 уникальных строк

#### `fix_grifon_visibility` — загрузился

- `[07:17:29.652] [fix_grifon_visibility] loaded v1.0.0`
- `[07:21:50.918] [fix_grifon_visibility] loaded v1.0.0`
- `[07:23:07.052] [fix_grifon_visibility] loaded v1.0.0`
- `[08:25:02.669] [fix_grifon_visibility] loaded v1.0.0`
- `[08:27:19.119] [fix_grifon_visibility] loaded v1.0.0`
- `[08:37:00.828] [fix_grifon_visibility] loaded v1.0.0`
- `[08:43:15.586] [fix_grifon_visibility] loaded v1.0.0`
- `[08:45:14.598] [fix_grifon_visibility] loaded v1.0.0`
- `[08:46:45.675] [fix_grifon_visibility] loaded v1.0.0`
- `[08:48:19.597] [fix_grifon_visibility] loaded v1.0.0`
- `[08:50:10.970] [fix_grifon_visibility] loaded v1.0.0`
- `[08:51:54.377] [fix_grifon_visibility] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_hip_quest_text` — загрузился

- `[07:17:29.652] [fix_hip_quest_text] loaded v1.0.0`
- `[07:21:50.918] [fix_hip_quest_text] loaded v1.0.0`
- `[07:23:07.052] [fix_hip_quest_text] loaded v1.0.0`
- `[08:25:02.669] [fix_hip_quest_text] loaded v1.0.0`
- `[08:27:19.119] [fix_hip_quest_text] loaded v1.0.0`
- `[08:37:00.828] [fix_hip_quest_text] loaded v1.0.0`
- `[08:43:15.587] [fix_hip_quest_text] loaded v1.0.0`
- `[08:45:14.598] [fix_hip_quest_text] loaded v1.0.0`
- `[08:46:45.675] [fix_hip_quest_text] loaded v1.0.0`
- `[08:48:19.597] [fix_hip_quest_text] loaded v1.0.0`
- `[08:50:10.970] [fix_hip_quest_text] loaded v1.0.0`
- `[08:51:54.377] [fix_hip_quest_text] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_hoc_monolith_icon` — загрузился

- `[07:17:29.652] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[07:21:50.918] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[07:23:07.052] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:25:02.669] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:27:19.119] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:37:00.828] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:43:15.587] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:45:14.598] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:46:45.675] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:48:19.597] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:50:10.970] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[08:51:54.377] [fix_hoc_monolith_icon] loaded v1.1.0`
- … ещё 12 уникальных строк

#### `fix_indeikam_breeding` — загрузился

- `[07:17:29.652] [fix_indeikam_breeding] loaded v1.0.0`
- `[07:21:50.918] [fix_indeikam_breeding] loaded v1.0.0`
- `[07:23:07.052] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:25:02.669] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:27:19.119] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:37:00.828] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:43:15.587] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:45:14.598] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:46:45.675] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:48:19.597] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:50:10.970] [fix_indeikam_breeding] loaded v1.0.0`
- `[08:51:54.377] [fix_indeikam_breeding] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_item_combination_magnifiers` — загрузился

- `[07:17:29.652] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[07:21:50.918] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[07:23:07.052] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:25:02.669] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:27:19.119] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:37:00.828] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:43:15.587] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:45:14.598] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:46:45.675] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:48:19.597] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:50:10.970] [fix_item_combination_magnifiers] loaded v1.0.0`
- `[08:51:54.377] [fix_item_combination_magnifiers] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_kupol_wrong_bone` — загрузился

- `[07:17:33.222] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[07:18:27.139] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `[07:21:54.348] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[07:22:24.338] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38434 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[07:23:10.467] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[07:23:45.165] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38434 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[08:25:06.261] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[08:25:38.816] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38434 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[08:27:22.570] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[08:27:54.353] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38434 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[08:37:04.237] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[08:37:33.588] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38434 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- … ещё 35 уникальных строк

#### `fix_loot_space` — загрузился

- `[07:17:29.653] [fix_loot_space] loaded v1.0.1`
- `[07:17:33.222] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[07:21:50.919] [fix_loot_space] loaded v1.0.1`
- `[07:21:54.348] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[07:23:07.053] [fix_loot_space] loaded v1.0.1`
- `[07:23:10.467] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[08:25:02.669] [fix_loot_space] loaded v1.0.1`
- `[08:25:06.261] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[08:27:19.119] [fix_loot_space] loaded v1.0.1`
- `[08:27:22.570] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[08:37:00.828] [fix_loot_space] loaded v1.0.1`
- `[08:37:04.237] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- … ещё 36 уникальных строк

#### `fix_milspec_exo_craft` — загрузился

- `[07:17:33.223] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[07:18:49.047] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[07:21:54.348] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[07:23:10.467] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[07:26:10.403] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[08:25:06.261] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[08:27:22.570] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[08:29:45.745] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[08:37:04.238] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[08:38:52.430] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[08:43:19.038] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[08:45:18.049] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- … ещё 24 уникальных строк

#### `fix_misc_script_errors` — загрузился

- `[07:15:36.375] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[07:16:09.309] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[07:17:29.653] [fix_misc_script_errors] loaded v1.0.2`
- `[07:17:33.223] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[07:21:39.581] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[07:21:50.919] [fix_misc_script_errors] loaded v1.0.2`
- `[07:21:54.348] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[07:22:56.024] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[07:23:07.054] [fix_misc_script_errors] loaded v1.0.2`
- `[07:23:10.467] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[08:24:48.315] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[08:25:02.670] [fix_misc_script_errors] loaded v1.0.2`
- … ещё 61 уникальных строк

#### `fix_nimble_order_desc` — загрузился

- `[07:17:29.653] [fix_nimble_order_desc] loaded v1.0.0`
- `[07:21:50.919] [fix_nimble_order_desc] loaded v1.0.0`
- `[07:23:07.054] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:25:02.670] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:27:19.120] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:37:00.829] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:43:15.588] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:45:14.599] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:46:45.676] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:48:19.598] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:50:10.970] [fix_nimble_order_desc] loaded v1.0.0`
- `[08:51:54.378] [fix_nimble_order_desc] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_noosphere_voice_x18` — загрузился

- `[07:17:29.653] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[07:17:33.223] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[07:21:50.920] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[07:21:54.348] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[07:23:07.054] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[07:23:10.467] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:25:02.670] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:25:06.261] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:27:19.120] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:27:22.570] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:37:00.829] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[08:37:04.238] [fix_noosphere_voice_x18] loaded v1.0.1`
- … ещё 36 уникальных строк

#### `fix_nta_stashes` — загрузился

- `[07:17:33.223] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[07:17:33.223] [fix_nta_stashes] loaded v1.0.0`
- `[07:21:54.348] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[07:21:54.348] [fix_nta_stashes] loaded v1.0.0`
- `[07:23:10.467] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[07:23:10.467] [fix_nta_stashes] loaded v1.0.0`
- `[08:25:06.261] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[08:25:06.261] [fix_nta_stashes] loaded v1.0.0`
- `[08:27:22.570] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[08:27:22.570] [fix_nta_stashes] loaded v1.0.0`
- `[08:37:04.238] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[08:37:04.238] [fix_nta_stashes] loaded v1.0.0`
- … ещё 36 уникальных строк

#### `fix_okrest_texnik_dialog` — загрузился

- `[07:17:29.653] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[07:21:50.920] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[07:23:07.054] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:25:02.671] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:27:19.120] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:37:00.830] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:43:15.589] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:45:14.600] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:46:45.676] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:48:19.599] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:50:10.971] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[08:51:54.379] [fix_okrest_texnik_dialog] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_pda_buyinfo_gui` — загрузился

- `[07:17:29.654] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[07:17:33.223] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[07:21:50.920] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[07:21:54.348] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[07:23:07.055] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[07:23:10.467] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[08:25:02.671] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[08:25:06.261] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[08:27:19.120] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[08:27:22.570] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[08:37:00.830] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[08:37:04.238] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- … ещё 36 уникальных строк

#### `fix_ph_door_rx_reload` — загрузился

- `[07:17:29.654] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[07:17:33.223] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[07:17:33.223] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[07:21:50.921] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[07:21:54.348] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[07:21:54.348] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[07:23:07.055] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[07:23:10.467] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[07:23:10.467] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[08:25:02.671] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[08:25:06.261] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[08:25:06.261] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- … ещё 60 уникальных строк

#### `fix_quest_stash` — есть строки

- `[07:17:29.655] [fix_quest_stash] загружен v1.0.4`
- `[07:17:33.223] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[07:17:33.223] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[07:21:50.922] [fix_quest_stash] загружен v1.0.4`
- `[07:21:54.348] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[07:21:54.348] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[07:23:07.056] [fix_quest_stash] загружен v1.0.4`
- `[07:23:10.467] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[07:23:10.467] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[08:25:02.672] [fix_quest_stash] загружен v1.0.4`
- `[08:25:06.261] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[08:25:06.261] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- … ещё 82 уникальных строк

#### `fix_quest_story_id` — загрузился

- `[07:17:29.656] [fix_quest_story_id] loaded v1.0.2`
- `[07:17:33.223] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[07:17:33.223] [fix_quest_story_id] loaded v1.0.2`
- `[07:17:41.045] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[07:17:42.243] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[07:17:42.327] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[07:18:24.023] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[07:18:24.108] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[07:18:24.115] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`
- `[07:21:50.922] [fix_quest_story_id] loaded v1.0.2`
- `[07:21:54.348] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[07:21:54.348] [fix_quest_story_id] loaded v1.0.2`
- … ещё 312 уникальных строк

#### `fix_radio` — загрузился

- `[07:17:29.657] [fix_radio] loaded v1.0.2`
- `[07:17:33.223] [fix_radio] loaded v1.0.2`
- `[07:21:50.923] [fix_radio] loaded v1.0.2`
- `[07:21:54.348] [fix_radio] loaded v1.0.2`
- `[07:23:07.057] [fix_radio] loaded v1.0.2`
- `[07:23:10.467] [fix_radio] loaded v1.0.2`
- `[08:25:02.674] [fix_radio] loaded v1.0.2`
- `[08:25:06.261] [fix_radio] loaded v1.0.2`
- `[08:27:19.121] [fix_radio] loaded v1.0.2`
- `[08:27:22.570] [fix_radio] loaded v1.0.2`
- `[08:37:00.833] [fix_radio] loaded v1.0.2`
- `[08:37:04.238] [fix_radio] loaded v1.0.2`
- … ещё 36 уникальных строк

#### `fix_replace_quest_corpse` — загрузился

- `[07:17:29.658] [fix_replace_quest_corpse] loaded v1.0.1`
- `[07:17:29.658] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[07:17:33.223] [fix_replace_quest_corpse] loaded v1.0.1`
- `[07:21:50.923] [fix_replace_quest_corpse] loaded v1.0.1`
- `[07:21:50.923] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[07:21:54.348] [fix_replace_quest_corpse] loaded v1.0.1`
- `[07:23:07.058] [fix_replace_quest_corpse] loaded v1.0.1`
- `[07:23:07.058] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[07:23:10.468] [fix_replace_quest_corpse] loaded v1.0.1`
- `[08:25:02.674] [fix_replace_quest_corpse] loaded v1.0.1`
- `[08:25:02.674] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[08:25:06.261] [fix_replace_quest_corpse] loaded v1.0.1`
- … ещё 60 уникальных строк

#### `fix_rogue_hostility` — загрузился

- `[07:17:33.223] [fix_rogue_hostility] loaded v1.0.0`
- `[07:21:54.348] [fix_rogue_hostility] loaded v1.0.0`
- `[07:23:10.468] [fix_rogue_hostility] loaded v1.0.0`
- `[08:25:06.261] [fix_rogue_hostility] loaded v1.0.0`
- `[08:27:22.570] [fix_rogue_hostility] loaded v1.0.0`
- `[08:37:04.238] [fix_rogue_hostility] loaded v1.0.0`
- `[08:43:19.039] [fix_rogue_hostility] loaded v1.0.0`
- `[08:45:18.049] [fix_rogue_hostility] loaded v1.0.0`
- `[08:46:49.160] [fix_rogue_hostility] loaded v1.0.0`
- `[08:48:23.032] [fix_rogue_hostility] loaded v1.0.0`
- `[08:50:14.385] [fix_rogue_hostility] loaded v1.0.0`
- `[08:51:57.801] [fix_rogue_hostility] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_rx_bandage_dead` — загрузился

- `[07:17:29.658] [fix_rx_bandage_dead] loaded v1.0.1`
- `[07:17:33.223] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[07:21:50.924] [fix_rx_bandage_dead] loaded v1.0.1`
- `[07:21:54.348] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[07:23:07.058] [fix_rx_bandage_dead] loaded v1.0.1`
- `[07:23:10.468] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[08:25:02.675] [fix_rx_bandage_dead] loaded v1.0.1`
- `[08:25:06.261] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[08:27:19.122] [fix_rx_bandage_dead] loaded v1.0.1`
- `[08:27:22.570] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[08:37:00.834] [fix_rx_bandage_dead] loaded v1.0.1`
- `[08:37:04.238] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- … ещё 36 уникальных строк

#### `fix_sim_mechanic_trade` — загрузился

- `[07:17:29.659] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[07:21:50.924] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[07:23:07.058] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:25:02.675] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:27:19.122] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:37:00.834] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:43:15.593] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:45:14.604] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:46:45.678] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:48:19.604] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:50:10.972] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[08:51:54.383] [fix_sim_mechanic_trade] loaded v1.0.1`
- … ещё 12 уникальных строк

#### `fix_soc_nimble_flash` — загрузился

- `[07:17:29.659] [fix_soc_nimble_flash] loaded v1.0.1`
- `[07:17:33.223] [fix_soc_nimble_flash] loaded v1.0.1`
- `[07:21:50.925] [fix_soc_nimble_flash] loaded v1.0.1`
- `[07:21:54.348] [fix_soc_nimble_flash] loaded v1.0.1`
- `[07:23:07.059] [fix_soc_nimble_flash] loaded v1.0.1`
- `[07:23:10.468] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:25:02.676] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:25:06.261] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:27:19.122] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:27:22.570] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:37:00.835] [fix_soc_nimble_flash] loaded v1.0.1`
- `[08:37:04.238] [fix_soc_nimble_flash] loaded v1.0.1`
- … ещё 36 уникальных строк

#### `fix_sort_tabs` — загрузился

- `[07:17:29.659] [fix_sort_tabs] loaded v1.0.0`
- `[07:21:50.925] [fix_sort_tabs] loaded v1.0.0`
- `[07:23:07.059] [fix_sort_tabs] loaded v1.0.0`
- `[08:25:02.676] [fix_sort_tabs] loaded v1.0.0`
- `[08:27:19.122] [fix_sort_tabs] loaded v1.0.0`
- `[08:37:00.835] [fix_sort_tabs] loaded v1.0.0`
- `[08:43:15.593] [fix_sort_tabs] loaded v1.0.0`
- `[08:45:14.604] [fix_sort_tabs] loaded v1.0.0`
- `[08:46:45.678] [fix_sort_tabs] loaded v1.0.0`
- `[08:48:19.604] [fix_sort_tabs] loaded v1.0.0`
- `[08:50:10.972] [fix_sort_tabs] loaded v1.0.0`
- `[08:51:54.384] [fix_sort_tabs] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_st2_footstep` — загрузился

- `[07:17:29.659] [fix_st2_footstep] loaded v1.0.0`
- `[07:21:50.925] [fix_st2_footstep] loaded v1.0.0`
- `[07:23:07.059] [fix_st2_footstep] loaded v1.0.0`
- `[08:25:02.676] [fix_st2_footstep] loaded v1.0.0`
- `[08:27:19.122] [fix_st2_footstep] loaded v1.0.0`
- `[08:37:00.835] [fix_st2_footstep] loaded v1.0.0`
- `[08:43:15.593] [fix_st2_footstep] loaded v1.0.0`
- `[08:45:14.604] [fix_st2_footstep] loaded v1.0.0`
- `[08:46:45.678] [fix_st2_footstep] loaded v1.0.0`
- `[08:48:19.604] [fix_st2_footstep] loaded v1.0.0`
- `[08:50:10.972] [fix_st2_footstep] loaded v1.0.0`
- `[08:51:54.384] [fix_st2_footstep] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_stash_id_desync` — загрузился

- `[07:17:33.223] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[07:17:33.223] [fix_stash_id_desync] loaded v1.0.2`
- `[07:18:35.615] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[07:21:54.348] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[07:21:54.348] [fix_stash_id_desync] loaded v1.0.2`
- `[07:23:10.468] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[07:23:10.468] [fix_stash_id_desync] loaded v1.0.2`
- `[07:24:06.487] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[08:25:06.261] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[08:25:06.261] [fix_stash_id_desync] loaded v1.0.2`
- `[08:25:45.297] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[08:27:22.570] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- … ещё 58 уникальных строк

#### `fix_talents_pda_respec` — загрузился

- `[07:17:33.223] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[07:21:54.348] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[07:23:10.468] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:25:06.262] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:27:22.570] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:37:04.238] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:43:19.039] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:45:18.049] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:46:49.161] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:48:23.032] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:50:14.385] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[08:51:57.801] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- … ещё 12 уникальных строк

#### `fix_trade_craft_stock` — загрузился

- `[07:17:29.661] [fix_trade_craft_stock] loaded v1.0.0`
- `[07:21:50.926] [fix_trade_craft_stock] loaded v1.0.0`
- `[07:23:07.060] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:25:02.677] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:27:19.122] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:37:00.836] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:43:15.595] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:45:14.605] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:46:45.678] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:48:19.605] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:50:10.973] [fix_trade_craft_stock] loaded v1.0.0`
- `[08:51:54.385] [fix_trade_craft_stock] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_trader_restock_callback` — загрузился

- `[07:17:20.354] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[07:17:32.715] [fix_trader_restock_callback] Send wrap installed`
- `[07:21:40.757] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[07:21:53.896] [fix_trader_restock_callback] Send wrap installed`
- `[07:22:57.181] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[07:23:10.015] [fix_trader_restock_callback] Send wrap installed`
- `[08:24:50.453] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[08:25:05.802] [fix_trader_restock_callback] Send wrap installed`
- `[08:27:09.108] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[08:27:22.112] [fix_trader_restock_callback] Send wrap installed`
- `[08:36:50.862] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[08:37:03.785] [fix_trader_restock_callback] Send wrap installed`
- … ещё 36 уникальных строк

#### `fix_vows_ambush_stash` — загрузился

- `[07:17:29.661] [fix_vows_ambush_stash] loaded v1.0.1`
- `[07:17:33.223] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[07:17:33.223] [fix_vows_ambush_stash] loaded v1.0.1`
- `[07:21:50.927] [fix_vows_ambush_stash] loaded v1.0.1`
- `[07:21:54.348] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[07:21:54.348] [fix_vows_ambush_stash] loaded v1.0.1`
- `[07:23:07.061] [fix_vows_ambush_stash] loaded v1.0.1`
- `[07:23:10.468] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[07:23:10.468] [fix_vows_ambush_stash] loaded v1.0.1`
- `[08:25:02.678] [fix_vows_ambush_stash] loaded v1.0.1`
- `[08:25:06.262] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[08:25:06.262] [fix_vows_ambush_stash] loaded v1.0.1`
- … ещё 60 уникальных строк

#### `fix_wtf_assault_instacomplete` — загрузился

- `[07:17:29.662] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[07:17:33.223] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[07:21:50.927] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[07:21:54.348] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[07:23:07.061] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[07:23:10.468] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:25:02.678] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:25:06.262] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:27:19.123] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:27:22.570] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:37:00.837] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[08:37:04.238] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- … ещё 36 уникальных строк

#### `fix_wtf_taskboard_guard` — загрузился

- x2 `...1/bin/..\gamedata\scripts\fix_wtf_taskboard_guard.script:156: quest=ghentuongsupply43188; entity=enemy; macro=$ igi_helper.db_ini:r_value('gt_guard', |this.faction|); expression= igi_helper.db_ini:r_value('gt_guard', `
- `[07:17:29.662] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[07:17:33.223] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[07:21:50.928] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[07:21:54.349] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[07:23:07.062] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[07:23:10.468] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[08:25:02.679] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[08:25:06.262] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[08:27:19.123] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[08:27:22.570] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[08:37:00.838] [fix_wtf_taskboard_guard] loaded v1.0.2`
- … ещё 40 уникальных строк

#### `fix_x15_freeplay_gate` — загрузился

- `[07:17:29.663] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[07:21:50.928] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[07:23:07.062] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:25:02.679] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:27:19.123] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:37:00.838] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:43:15.597] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:45:14.607] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:46:45.679] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:48:19.607] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:50:10.973] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[08:51:54.386] [fix_x15_freeplay_gate] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `fix_x2_gravity_room` — загрузился

- `[07:17:29.663] [fix_x2_gravity_room] loaded v1.0.1`
- `[07:17:33.223] [fix_x2_gravity_room] loaded v1.0.1`
- `[07:21:50.929] [fix_x2_gravity_room] loaded v1.0.1`
- `[07:21:54.349] [fix_x2_gravity_room] loaded v1.0.1`
- `[07:23:07.062] [fix_x2_gravity_room] loaded v1.0.1`
- `[07:23:10.468] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:25:02.680] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:25:06.262] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:27:19.123] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:27:22.570] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:37:00.839] [fix_x2_gravity_room] loaded v1.0.1`
- `[08:37:04.238] [fix_x2_gravity_room] loaded v1.0.1`
- … ещё 36 уникальных строк

#### `fix_xr_effects_sounds` — загрузился

- `[07:17:33.223] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[07:21:54.349] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[07:23:10.468] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:25:06.262] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:27:22.570] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:37:04.238] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:43:19.039] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:45:18.049] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:46:49.161] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:48:23.032] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:50:14.385] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[08:51:57.801] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- … ещё 12 уникальных строк

#### `fix_zat_b12_box` — загрузился

- `[07:17:29.664] [fix_zat_b12_box] loaded v1.0.0`
- `[07:21:50.930] [fix_zat_b12_box] loaded v1.0.0`
- `[07:23:07.063] [fix_zat_b12_box] loaded v1.0.0`
- `[08:25:02.680] [fix_zat_b12_box] loaded v1.0.0`
- `[08:27:19.123] [fix_zat_b12_box] loaded v1.0.0`
- `[08:37:00.839] [fix_zat_b12_box] loaded v1.0.0`
- `[08:43:15.598] [fix_zat_b12_box] loaded v1.0.0`
- `[08:45:14.608] [fix_zat_b12_box] loaded v1.0.0`
- `[08:46:45.679] [fix_zat_b12_box] loaded v1.0.0`
- `[08:48:19.608] [fix_zat_b12_box] loaded v1.0.0`
- `[08:50:10.974] [fix_zat_b12_box] loaded v1.0.0`
- `[08:51:54.387] [fix_zat_b12_box] loaded v1.0.0`
- … ещё 12 уникальных строк

#### `quickqk_task_complete` — загрузился

- `[07:17:32.028] [quickqk_task_complete] loaded v1.4.2`
- `[07:21:53.247] [quickqk_task_complete] loaded v1.4.2`
- `[07:23:09.365] [quickqk_task_complete] loaded v1.4.2`
- `[08:25:05.058] [quickqk_task_complete] loaded v1.4.2`
- `[08:27:21.466] [quickqk_task_complete] loaded v1.4.2`
- `[08:37:03.138] [quickqk_task_complete] loaded v1.4.2`
- `[08:43:17.909] [quickqk_task_complete] loaded v1.4.2`
- `[08:45:16.926] [quickqk_task_complete] loaded v1.4.2`
- `[08:46:48.037] [quickqk_task_complete] loaded v1.4.2`
- `[08:48:21.928] [quickqk_task_complete] loaded v1.4.2`
- `[08:50:13.323] [quickqk_task_complete] loaded v1.4.2`
- `[08:51:56.686] [quickqk_task_complete] loaded v1.4.2`
- … ещё 12 уникальных строк

#### `seamless_inventory_sort_anthology` — загрузился

- `[07:16:34.417] path:tooltip_control/hold_key, key:56, old:nil`
- `[07:16:34.417] path:tooltip_control/trigger_key, key:56, old:nil`
- `[07:17:33.627] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[07:17:33.630] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=fps keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[07:17:33.665] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[07:19:08.946] path:tooltip_control/hold_key, key:56, old:56`
- `[07:19:08.946] path:tooltip_control/trigger_key, key:56, old:56`
- `[07:19:18.292] path:tooltip_control/hold_key, key:56, old:56`
- `[07:19:18.292] path:tooltip_control/trigger_key, key:56, old:56`
- `[07:21:43.189] path:tooltip_control/hold_key, key:56, old:nil`
- `[07:21:43.189] path:tooltip_control/trigger_key, key:56, old:nil`
- `[07:21:54.673] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- … ещё 127 уникальных строк

## Нефатальные ошибки

### 1. `igi_text_processor.script` ×1

Триггер: нет строки с `!` / `~` перед блоком

```
[C]: in function 'error'
...gy 2.1/bin/..\gamedata\scripts\igi_text_processor.script:260: in function 'resolve_and_link_cache'
...logy 2.1/bin/..\gamedata\scripts\igi_generic_task.script:92: in function <...logy 2.1/bin/..\gamedata\scripts\igi_generic_task.script:87>
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

- Блок FATAL ERROR не найден, но есть 1 нефатальных Lua-ошибок, 1 уникальных сигнатур.
- Смотри секцию «Нефатальные ошибки»: повторяющиеся traceback'и — основной класс проблем этой сборки.
- Самая частая: `igi_text_processor.script` ×1.

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
