# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (13.7 МБ, 203988 строк)
- Дата разбора: 2026-09-06
- Класс: **вылета нет, есть повторяющиеся ошибки (1 групп)**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (3)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_item_combination_magnifiers`
- `fix_minigun_dead_parent`

### С отказами (1)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[22:18:08.791] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[22:18:08.791] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:18:09.832] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:18:27.239] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:21:25.877] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[22:21:25.877] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:21:26.723] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:21:36.021] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:39:43.472] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[22:39:43.472] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:39:44.301] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[22:39:53.959] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- … ещё 56 уникальных строк

### В логе без отказов (60)

#### `anthology_busyhands_stability_fix` — загрузился

- `[22:18:08.805] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[22:18:09.067] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[22:18:09.551] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[22:18:09.551] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[22:18:09.551] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[22:18:09.551] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[22:18:09.551] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[22:18:09.551] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[22:18:09.551] [BusyHandsFix v0.6.10] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[22:18:09.551] [BusyHandsFix v0.6.10] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[22:18:09.551] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[22:18:09.551] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 651 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[22:18:09.594] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:21:26.516] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:39:44.104] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:50:57.296] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:51:58.953] [BurnShitInventoryDestroy] destroy check | section=jup_b32_scanner_device | class=II_ATTCH | blocked_by=quest`
- `[22:52:56.715] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:54:26.860] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[22:57:31.792] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[23:00:38.112] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[23:07:45.400] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[23:15:40.098] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[23:16:26.664] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- … ещё 8 уникальных строк

#### `campfires_anthology_compat` — загрузился

- `[22:18:08.464] [campfires_anthology_compat] loaded v1.1.0`
- `[22:21:25.591] [campfires_anthology_compat] loaded v1.1.0`
- `* [22:21:37.846]  [load-session/lua-callbacks] #08 self=60.09 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`
- `[22:39:43.200] [campfires_anthology_compat] loaded v1.1.0`
- `[22:50:56.391] [campfires_anthology_compat] loaded v1.1.0`
- `* [22:51:08.092]  [load-session/lua-callbacks] #10 self=64.70 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`
- `[22:52:55.810] [campfires_anthology_compat] loaded v1.1.0`
- `* [22:53:07.034]  [load-session/lua-callbacks] #09 self=66.21 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`
- `[22:54:25.955] [campfires_anthology_compat] loaded v1.1.0`
- `* [22:54:38.221]  [load-session/lua-callbacks] #11 self=56.08 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`
- `[22:57:30.890] [campfires_anthology_compat] loaded v1.1.0`
- `* [22:57:42.826]  [load-session/lua-callbacks] #06 self=87.14 ms source=...gy 2.1/bin/..\gamedata\scripts\campfire_placeable.script:37`
- … ещё 22 уникальных строк

#### `context_menu_overhaul_anthology` — загрузился

- `[22:18:09.828] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[22:18:28.943] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[22:18:28.945] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [22:18:28.947]  [load-session/lua-callbacks] #08 self=80.88 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `[22:21:26.722] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[22:21:36.208] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[22:21:36.210] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `* [22:21:37.846]  [load-session/lua-callbacks] #06 self=85.22 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `[22:21:38.499] [CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=31 current_tab=8 category=slots target_tab=1 route=primary_manual`
- `[22:39:44.300] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[22:39:52.682] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[22:39:52.684] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- … ещё 66 уникальных строк

#### `diag_log_spam` — загрузился

- x2 `[22:21:24.663] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:39:42.319] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:50:55.495] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:52:54.923] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:54:25.066] [diag_log_spam]   [C]: in function '__index'`
- x2 `[22:57:30.012] [diag_log_spam]   [C]: in function '__index'`
- x2 `[23:00:36.324] [diag_log_spam]   [C]: in function '__index'`
- x2 `[23:07:43.605] [diag_log_spam]   [C]: in function '__index'`
- x2 `[23:15:38.295] [diag_log_spam]   [C]: in function '__index'`
- x2 `[23:16:24.825] [diag_log_spam]   [C]: in function '__index'`
- x2 `[23:17:36.412] [diag_log_spam]   [C]: in function '__index'`
- x2 `[23:25:35.562] [diag_log_spam]   [C]: in function '__index'`
- … ещё 170 уникальных строк

#### `fix_arena_loadout` — загрузился

- `[22:18:09.832] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:21:26.723] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:39:44.301] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:50:57.495] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:52:56.913] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:54:27.061] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[22:57:31.992] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[23:00:38.313] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[23:07:45.600] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[23:15:40.296] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[23:16:26.866] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[23:17:38.401] [fix_arena_loadout] bar_arena_teleport wrapped`
- … ещё 5 уникальных строк

#### `fix_ashot_aw_travel` — загрузился

- `[22:18:08.791] [fix_ashot_aw_travel] loaded v1.0.1`
- `[22:18:09.832] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[22:21:25.877] [fix_ashot_aw_travel] loaded v1.0.1`
- `[22:21:26.723] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[22:39:43.473] [fix_ashot_aw_travel] loaded v1.0.1`
- `[22:39:44.301] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[22:50:56.667] [fix_ashot_aw_travel] loaded v1.0.1`
- `[22:50:57.495] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[22:52:56.091] [fix_ashot_aw_travel] loaded v1.0.1`
- `[22:52:56.913] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[22:54:26.238] [fix_ashot_aw_travel] loaded v1.0.1`
- `[22:54:27.061] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- … ещё 22 уникальных строк

#### `fix_attribute_assistent` — загрузился

- `[22:18:08.791] [fix_attribute_assistent] loaded v1.0.1`
- `[22:18:09.832] [fix_attribute_assistent] loaded v1.0.1`
- `[22:21:25.877] [fix_attribute_assistent] loaded v1.0.1`
- `[22:21:26.723] [fix_attribute_assistent] loaded v1.0.1`
- `[22:39:43.473] [fix_attribute_assistent] loaded v1.0.1`
- `[22:39:44.301] [fix_attribute_assistent] loaded v1.0.1`
- `[22:50:56.667] [fix_attribute_assistent] loaded v1.0.1`
- `[22:50:57.495] [fix_attribute_assistent] loaded v1.0.1`
- `[22:52:56.091] [fix_attribute_assistent] loaded v1.0.1`
- `[22:52:56.913] [fix_attribute_assistent] loaded v1.0.1`
- `[22:54:26.238] [fix_attribute_assistent] loaded v1.0.1`
- `[22:54:27.061] [fix_attribute_assistent] loaded v1.0.1`
- … ещё 22 уникальных строк

#### `fix_aver_darkvalley` — загрузился

- `[22:18:09.832] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[22:18:14.056] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[22:18:14.343] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[22:18:28.775] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[22:18:28.790] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [22:18:28.947]  [load-session/lua-callbacks] #14 self=32.21 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`
- `[22:21:26.723] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[22:21:29.010] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[22:21:29.346] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[22:21:36.216] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[22:21:36.231] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [22:21:37.846]  [load-session/lua-callbacks] #14 self=31.45 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`
- … ещё 90 уникальных строк

#### `fix_charon_red_forest_travel` — загрузился

- `[22:18:08.792] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[22:18:09.832] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[22:21:25.877] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[22:21:26.723] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[22:39:43.473] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[22:39:44.301] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[22:50:56.667] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[22:50:57.495] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[22:52:56.091] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[22:52:56.913] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[22:54:26.238] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[22:54:27.061] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- … ещё 22 уникальных строк

#### `fix_crowkiller_hello` — загрузился

- `[22:18:09.832] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[22:21:26.723] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[22:39:44.301] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[22:50:57.495] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[22:52:56.913] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[22:54:27.061] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[22:57:31.992] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[23:00:38.313] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[23:07:45.600] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[23:15:40.296] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[23:16:26.866] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[23:17:38.401] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- … ещё 5 уникальных строк

#### `fix_dome_quest` — загрузился

- `[22:18:08.792] [fix_dome_quest] loaded v1.0.0`
- `[22:21:25.877] [fix_dome_quest] loaded v1.0.0`
- `[22:39:43.473] [fix_dome_quest] loaded v1.0.0`
- `[22:50:56.667] [fix_dome_quest] loaded v1.0.0`
- `[22:52:56.091] [fix_dome_quest] loaded v1.0.0`
- `[22:54:26.238] [fix_dome_quest] loaded v1.0.0`
- `[22:57:31.168] [fix_dome_quest] loaded v1.0.0`
- `[23:00:37.487] [fix_dome_quest] loaded v1.0.0`
- `[23:07:44.776] [fix_dome_quest] loaded v1.0.0`
- `[23:15:39.463] [fix_dome_quest] loaded v1.0.0`
- `[23:16:26.021] [fix_dome_quest] loaded v1.0.0`
- `[23:17:37.577] [fix_dome_quest] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[22:18:08.792] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[22:18:09.832] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[22:21:25.877] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[22:21:26.723] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[22:39:43.473] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[22:39:44.301] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[22:50:56.667] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[22:50:57.495] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[22:52:56.091] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[22:52:56.913] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- `[22:54:26.238] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[22:54:27.061] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`
- … ещё 22 уникальных строк

#### `fix_dynamic_armor_visuals_nil` — загрузился

- `[22:18:08.792] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[22:18:09.832] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`
- `[22:21:25.877] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[22:21:26.723] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`
- `[22:39:43.473] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[22:39:44.301] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`
- `[22:50:56.667] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[22:50:57.495] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`
- `[22:52:56.091] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[22:52:56.913] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`
- `[22:54:26.238] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[22:54:27.061] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`
- … ещё 22 уникальных строк

#### `fix_faction_trade_supply` — загрузился

- `[22:18:08.792] [fix_faction_trade_supply] loaded v1.0.0`
- `[22:18:09.832] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[22:21:25.877] [fix_faction_trade_supply] loaded v1.0.0`
- `[22:21:26.723] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[22:39:43.473] [fix_faction_trade_supply] loaded v1.0.0`
- `[22:39:44.301] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[22:50:56.667] [fix_faction_trade_supply] loaded v1.0.0`
- `[22:50:57.495] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[22:52:56.091] [fix_faction_trade_supply] loaded v1.0.0`
- `[22:52:56.913] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- `[22:54:26.238] [fix_faction_trade_supply] loaded v1.0.0`
- `[22:54:27.061] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`
- … ещё 22 уникальных строк

#### `fix_fdda_mcm_paths` — загрузился

- `[22:18:08.792] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:21:25.877] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:39:43.473] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:50:56.667] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:52:56.091] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:54:26.238] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[22:57:31.168] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[23:00:37.487] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[23:07:44.776] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[23:15:39.463] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[23:16:26.021] [fix_fdda_mcm_paths] loaded v1.0.0`
- `[23:17:37.577] [fix_fdda_mcm_paths] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_fetch_headlamp` — загрузился

- `[22:18:08.792] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:21:25.877] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:39:43.473] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:50:56.667] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:52:56.091] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:54:26.238] [fix_fetch_headlamp] loaded v1.0.0`
- `[22:57:31.168] [fix_fetch_headlamp] loaded v1.0.0`
- `[23:00:37.487] [fix_fetch_headlamp] loaded v1.0.0`
- `[23:07:44.776] [fix_fetch_headlamp] loaded v1.0.0`
- `[23:15:39.463] [fix_fetch_headlamp] loaded v1.0.0`
- `[23:16:26.021] [fix_fetch_headlamp] loaded v1.0.0`
- `[23:17:37.577] [fix_fetch_headlamp] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_flst_joker_door` — загрузился

- `[22:18:08.792] [fix_flst_joker_door] loaded v1.0.0`
- `[22:21:25.877] [fix_flst_joker_door] loaded v1.0.0`
- `[22:39:43.473] [fix_flst_joker_door] loaded v1.0.0`
- `[22:50:56.667] [fix_flst_joker_door] loaded v1.0.0`
- `[22:52:56.091] [fix_flst_joker_door] loaded v1.0.0`
- `[22:54:26.238] [fix_flst_joker_door] loaded v1.0.0`
- `[22:57:31.168] [fix_flst_joker_door] loaded v1.0.0`
- `[23:00:37.487] [fix_flst_joker_door] loaded v1.0.0`
- `[23:07:44.776] [fix_flst_joker_door] loaded v1.0.0`
- `[23:15:39.463] [fix_flst_joker_door] loaded v1.0.0`
- `[23:16:26.021] [fix_flst_joker_door] loaded v1.0.0`
- `[23:17:37.577] [fix_flst_joker_door] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_g2x_torch_meshes` — загрузился

- `[22:18:08.792] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[22:21:25.877] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[22:39:43.473] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[22:50:56.667] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[22:52:56.091] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[22:54:26.238] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[22:57:31.168] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[23:00:37.487] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[23:07:44.776] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[23:15:39.463] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[23:16:26.021] [fix_g2x_torch_meshes] loaded v1.0.0`
- `[23:17:37.577] [fix_g2x_torch_meshes] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_gigant_space_restriction` — загрузился

- `[22:18:08.792] [fix_gigant_space_restriction] loaded v1.1.1`
- `[22:18:09.832] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[22:18:09.832] [fix_gigant_space_restriction] loaded v1.1.1`
- `[22:18:13.957] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[22:18:13.957] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[22:18:14.133] [fix_gigant_space_restriction] quarantine id=9852 name=gigant_normal9852 section=gigant_normal reason=off_level`
- `[22:18:14.149] [fix_gigant_space_restriction] quarantine id=10806 name=gigant_normal10806 section=gigant_normal reason=off_level`
- `[22:18:14.167] [fix_gigant_space_restriction] quarantine id=12058 name=gigant_weak12058 section=gigant_weak reason=off_level`
- `[22:18:14.167] [fix_gigant_space_restriction] quarantine id=12084 name=gigant_weak12084 section=gigant_weak reason=off_level`
- `[22:18:14.203] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- `[22:18:14.293] [fix_gigant_space_restriction] quarantine id=20858 name=gigant_normal20858 section=gigant_normal reason=off_level`
- `[22:18:14.296] [fix_gigant_space_restriction] quarantine id=21145 name=gigant_normal21145 section=gigant_normal reason=off_level`
- … ещё 768 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[22:17:14.150] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[22:17:14.150] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[22:17:16.446] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`
- `[22:21:24.170] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[22:21:24.170] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[22:39:41.829] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[22:39:41.829] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[22:50:55.004] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[22:50:55.004] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[22:52:54.433] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[22:52:54.433] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[22:54:24.572] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- … ещё 23 уникальных строк

#### `fix_grifon_visibility` — загрузился

- `[22:18:08.792] [fix_grifon_visibility] loaded v1.1.0`
- `[22:21:25.878] [fix_grifon_visibility] loaded v1.1.0`
- `[22:39:43.473] [fix_grifon_visibility] loaded v1.1.0`
- `[22:50:56.667] [fix_grifon_visibility] loaded v1.1.0`
- `[22:52:56.091] [fix_grifon_visibility] loaded v1.1.0`
- `[22:54:26.238] [fix_grifon_visibility] loaded v1.1.0`
- `[22:57:31.169] [fix_grifon_visibility] loaded v1.1.0`
- `[23:00:37.487] [fix_grifon_visibility] loaded v1.1.0`
- `[23:07:44.776] [fix_grifon_visibility] loaded v1.1.0`
- `[23:15:39.464] [fix_grifon_visibility] loaded v1.1.0`
- `[23:16:26.022] [fix_grifon_visibility] loaded v1.1.0`
- `[23:17:37.577] [fix_grifon_visibility] loaded v1.1.0`
- … ещё 5 уникальных строк

#### `fix_hip_quest_text` — загрузился

- `[22:18:08.792] [fix_hip_quest_text] loaded v1.0.0`
- `[22:21:25.878] [fix_hip_quest_text] loaded v1.0.0`
- `[22:39:43.473] [fix_hip_quest_text] loaded v1.0.0`
- `[22:50:56.667] [fix_hip_quest_text] loaded v1.0.0`
- `[22:52:56.091] [fix_hip_quest_text] loaded v1.0.0`
- `[22:54:26.238] [fix_hip_quest_text] loaded v1.0.0`
- `[22:57:31.169] [fix_hip_quest_text] loaded v1.0.0`
- `[23:00:37.487] [fix_hip_quest_text] loaded v1.0.0`
- `[23:07:44.776] [fix_hip_quest_text] loaded v1.0.0`
- `[23:15:39.464] [fix_hip_quest_text] loaded v1.0.0`
- `[23:16:26.022] [fix_hip_quest_text] loaded v1.0.0`
- `[23:17:37.577] [fix_hip_quest_text] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_hoc_monolith_icon` — загрузился

- `[22:18:08.792] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:21:25.878] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:39:43.473] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:50:56.667] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:52:56.091] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:54:26.238] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[22:57:31.169] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[23:00:37.488] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[23:07:44.776] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[23:15:39.464] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[23:16:26.022] [fix_hoc_monolith_icon] loaded v1.1.0`
- `[23:17:37.577] [fix_hoc_monolith_icon] loaded v1.1.0`
- … ещё 5 уникальных строк

#### `fix_hostage_task_collision` — загрузился

- `[22:18:08.792] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:18:09.832] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[22:21:25.878] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:21:26.723] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[22:39:43.473] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:39:44.301] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[22:50:56.667] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:50:57.495] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[22:52:56.092] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:52:56.913] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- `[22:54:26.238] [fix_hostage_task_collision] loaded v1.0.0`
- `[22:54:27.061] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`
- … ещё 22 уникальных строк

#### `fix_indeikam_breeding` — загрузился

- `[22:18:08.792] [fix_indeikam_breeding] loaded v1.0.0`
- `[22:21:25.878] [fix_indeikam_breeding] loaded v1.0.0`
- `[22:39:43.473] [fix_indeikam_breeding] loaded v1.0.0`
- `[22:50:56.667] [fix_indeikam_breeding] loaded v1.0.0`
- `[22:52:56.092] [fix_indeikam_breeding] loaded v1.0.0`
- `[22:54:26.238] [fix_indeikam_breeding] loaded v1.0.0`
- `[22:57:31.169] [fix_indeikam_breeding] loaded v1.0.0`
- `[23:00:37.488] [fix_indeikam_breeding] loaded v1.0.0`
- `[23:07:44.776] [fix_indeikam_breeding] loaded v1.0.0`
- `[23:15:39.464] [fix_indeikam_breeding] loaded v1.0.0`
- `[23:16:26.022] [fix_indeikam_breeding] loaded v1.0.0`
- `[23:17:37.577] [fix_indeikam_breeding] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_kupol_wrong_bone` — загрузился

- `[22:18:09.832] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[22:18:28.887] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [22:18:28.947]  [load-session/lua-callbacks] #13 self=34.44 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[22:21:26.723] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[22:21:37.581] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [22:21:37.846]  [load-session/lua-callbacks] #12 self=42.31 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[22:39:44.301] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[22:39:53.473] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [22:39:54.380]  [load-session/lua-callbacks] #11 self=42.52 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- `[22:50:57.495] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[22:51:07.631] [fix_kupol_wrong_bone] already clear id=38437 reason=actor_on_first_update`
- `* [22:51:08.092]  [load-session/lua-callbacks] #11 self=61.92 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`
- … ещё 39 уникальных строк

#### `fix_loot_space` — загрузился

- `[22:18:08.793] [fix_loot_space] loaded v1.0.1`
- `[22:18:09.832] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[22:21:25.878] [fix_loot_space] loaded v1.0.1`
- `[22:21:26.724] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[22:39:43.474] [fix_loot_space] loaded v1.0.1`
- `[22:39:44.301] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[22:50:56.667] [fix_loot_space] loaded v1.0.1`
- `[22:50:57.495] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[22:52:56.092] [fix_loot_space] loaded v1.0.1`
- `[22:52:56.913] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[22:54:26.239] [fix_loot_space] loaded v1.0.1`
- `[22:54:27.061] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- … ещё 22 уникальных строк

#### `fix_milspec_exo_craft` — загрузился

- `[22:18:09.832] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[22:18:48.614] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[22:21:26.724] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[22:22:56.201] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[22:39:44.301] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[22:41:05.155] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[22:50:57.496] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[22:51:54.862] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[22:52:56.913] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[22:53:29.480] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[22:54:27.061] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[22:56:51.714] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- … ещё 19 уникальных строк

#### `fix_misc_script_errors` — загрузился

- `[22:17:14.150] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[22:17:26.749] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[22:18:08.793] [fix_misc_script_errors] loaded v1.0.2`
- `[22:18:09.832] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[22:21:24.170] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[22:21:25.878] [fix_misc_script_errors] loaded v1.0.2`
- `[22:21:26.724] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[22:39:41.829] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[22:39:43.474] [fix_misc_script_errors] loaded v1.0.2`
- `[22:39:44.301] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`
- `[22:50:55.004] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[22:50:56.668] [fix_misc_script_errors] loaded v1.0.2`
- … ещё 40 уникальных строк

#### `fix_nimble_order_desc` — загрузился

- `[22:18:08.793] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:21:25.878] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:39:43.474] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:50:56.668] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:52:56.092] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:54:26.239] [fix_nimble_order_desc] loaded v1.0.0`
- `[22:57:31.169] [fix_nimble_order_desc] loaded v1.0.0`
- `[23:00:37.488] [fix_nimble_order_desc] loaded v1.0.0`
- `[23:07:44.776] [fix_nimble_order_desc] loaded v1.0.0`
- `[23:15:39.464] [fix_nimble_order_desc] loaded v1.0.0`
- `[23:16:26.022] [fix_nimble_order_desc] loaded v1.0.0`
- `[23:17:37.578] [fix_nimble_order_desc] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_noosphere_voice_x18` — загрузился

- `[22:18:08.793] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:18:09.832] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:21:25.878] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:21:26.724] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:39:43.474] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:39:44.301] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:50:56.668] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:50:57.496] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:52:56.092] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:52:56.913] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:54:26.239] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[22:54:27.062] [fix_noosphere_voice_x18] loaded v1.0.1`
- … ещё 22 уникальных строк

#### `fix_nta_stashes` — загрузился

- `[22:18:09.832] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[22:18:09.832] [fix_nta_stashes] loaded v1.0.0`
- `[22:21:26.724] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[22:21:26.724] [fix_nta_stashes] loaded v1.0.0`
- `[22:39:44.301] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[22:39:44.301] [fix_nta_stashes] loaded v1.0.0`
- `[22:50:57.496] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[22:50:57.496] [fix_nta_stashes] loaded v1.0.0`
- `[22:52:56.913] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[22:52:56.913] [fix_nta_stashes] loaded v1.0.0`
- `[22:54:27.062] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[22:54:27.062] [fix_nta_stashes] loaded v1.0.0`
- … ещё 22 уникальных строк

#### `fix_okrest_texnik_dialog` — загрузился

- `[22:18:08.794] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:21:25.878] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:39:43.474] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:50:56.668] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:52:56.092] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:54:26.239] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[22:57:31.169] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[23:00:37.488] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[23:07:44.776] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[23:15:39.464] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[23:16:26.022] [fix_okrest_texnik_dialog] loaded v1.0.0`
- `[23:17:37.578] [fix_okrest_texnik_dialog] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_pda_buyinfo_gui` — загрузился

- `[22:18:08.794] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[22:18:09.832] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[22:21:25.878] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[22:21:26.724] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[22:39:43.474] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[22:39:44.301] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[22:50:56.668] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[22:50:57.496] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[22:52:56.092] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[22:52:56.913] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[22:54:26.239] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[22:54:27.062] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- … ещё 22 уникальных строк

#### `fix_ph_door_rx_reload` — загрузился

- `[22:18:08.794] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[22:18:09.832] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[22:18:09.832] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[22:21:25.878] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[22:21:26.724] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[22:21:26.724] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[22:39:43.474] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[22:39:44.301] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[22:39:44.301] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[22:50:56.668] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[22:50:57.496] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[22:50:57.496] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- … ещё 39 уникальных строк

#### `fix_quest_stash` — есть строки

- `[22:18:08.794] [fix_quest_stash] загружен v1.0.4`
- `[22:18:09.832] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[22:18:09.832] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[22:21:25.878] [fix_quest_stash] загружен v1.0.4`
- `[22:21:26.724] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[22:21:26.724] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[22:39:43.474] [fix_quest_stash] загружен v1.0.4`
- `[22:39:44.301] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[22:39:44.301] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[22:50:56.668] [fix_quest_stash] загружен v1.0.4`
- `[22:50:57.496] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[22:50:57.496] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- … ещё 40 уникальных строк

#### `fix_quest_story_id` — загрузился

- `[22:18:08.794] [fix_quest_story_id] loaded v1.0.2`
- `[22:18:09.832] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[22:18:09.832] [fix_quest_story_id] loaded v1.0.2`
- `[22:18:14.306] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[22:18:14.739] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[22:18:14.759] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[22:18:28.097] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[22:18:28.147] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[22:18:28.150] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`
- `[22:21:25.878] [fix_quest_story_id] loaded v1.0.2`
- `[22:21:26.724] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[22:21:26.724] [fix_quest_story_id] loaded v1.0.2`
- … ещё 141 уникальных строк

#### `fix_radio` — загрузился

- `[22:18:08.795] [fix_radio] loaded v1.0.2`
- `[22:18:09.832] [fix_radio] loaded v1.0.2`
- `[22:21:25.879] [fix_radio] loaded v1.0.2`
- `[22:21:26.724] [fix_radio] loaded v1.0.2`
- `[22:39:43.474] [fix_radio] loaded v1.0.2`
- `[22:39:44.301] [fix_radio] loaded v1.0.2`
- `[22:50:56.668] [fix_radio] loaded v1.0.2`
- `[22:50:57.496] [fix_radio] loaded v1.0.2`
- `[22:52:56.092] [fix_radio] loaded v1.0.2`
- `[22:52:56.914] [fix_radio] loaded v1.0.2`
- `[22:54:26.239] [fix_radio] loaded v1.0.2`
- `[22:54:27.062] [fix_radio] loaded v1.0.2`
- … ещё 22 уникальных строк

#### `fix_replace_quest_corpse` — загрузился

- `[22:18:08.795] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:18:08.795] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[22:18:09.832] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:21:25.879] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:21:25.879] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[22:21:26.724] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:39:43.474] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:39:43.474] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[22:39:44.301] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:50:56.668] [fix_replace_quest_corpse] loaded v1.0.1`
- `[22:50:56.668] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[22:50:57.496] [fix_replace_quest_corpse] loaded v1.0.1`
- … ещё 39 уникальных строк

#### `fix_rogue_hostility` — загрузился

- `[22:18:09.832] [fix_rogue_hostility] loaded v1.0.0`
- `[22:21:26.724] [fix_rogue_hostility] loaded v1.0.0`
- `[22:39:44.301] [fix_rogue_hostility] loaded v1.0.0`
- `[22:50:57.496] [fix_rogue_hostility] loaded v1.0.0`
- `[22:52:56.914] [fix_rogue_hostility] loaded v1.0.0`
- `[22:54:27.062] [fix_rogue_hostility] loaded v1.0.0`
- `[22:57:31.992] [fix_rogue_hostility] loaded v1.0.0`
- `[23:00:38.313] [fix_rogue_hostility] loaded v1.0.0`
- `[23:07:45.600] [fix_rogue_hostility] loaded v1.0.0`
- `[23:15:40.296] [fix_rogue_hostility] loaded v1.0.0`
- `[23:16:26.866] [fix_rogue_hostility] loaded v1.0.0`
- `[23:17:38.401] [fix_rogue_hostility] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_rx_bandage_dead` — загрузился

- `[22:18:08.795] [fix_rx_bandage_dead] loaded v1.0.1`
- `[22:18:09.832] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[22:21:25.879] [fix_rx_bandage_dead] loaded v1.0.1`
- `[22:21:26.724] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[22:39:43.474] [fix_rx_bandage_dead] loaded v1.0.1`
- `[22:39:44.301] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[22:50:56.668] [fix_rx_bandage_dead] loaded v1.0.1`
- `[22:50:57.496] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[22:52:56.093] [fix_rx_bandage_dead] loaded v1.0.1`
- `[22:52:56.914] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[22:54:26.239] [fix_rx_bandage_dead] loaded v1.0.1`
- `[22:54:27.062] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- … ещё 22 уникальных строк

#### `fix_sim_mechanic_trade` — загрузился

- `[22:18:08.795] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[22:21:25.879] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[22:39:43.474] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[22:50:56.668] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[22:52:56.093] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[22:54:26.239] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[22:57:31.170] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[23:00:37.489] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[23:07:44.777] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[23:15:39.465] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[23:16:26.023] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[23:17:37.579] [fix_sim_mechanic_trade] loaded v1.0.1`
- … ещё 5 уникальных строк

#### `fix_soc_nimble_flash` — загрузился

- `[22:18:08.795] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:18:09.832] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:21:25.879] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:21:26.724] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:39:43.475] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:39:44.301] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:50:56.668] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:50:57.496] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:52:56.093] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:52:56.914] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:54:26.240] [fix_soc_nimble_flash] loaded v1.0.1`
- `[22:54:27.062] [fix_soc_nimble_flash] loaded v1.0.1`
- … ещё 22 уникальных строк

#### `fix_sort_tabs` — загрузился

- `[22:18:08.795] [fix_sort_tabs] loaded v1.0.0`
- `[22:21:25.879] [fix_sort_tabs] loaded v1.0.0`
- `[22:39:43.475] [fix_sort_tabs] loaded v1.0.0`
- `[22:50:56.668] [fix_sort_tabs] loaded v1.0.0`
- `[22:52:56.093] [fix_sort_tabs] loaded v1.0.0`
- `[22:54:26.240] [fix_sort_tabs] loaded v1.0.0`
- `[22:57:31.170] [fix_sort_tabs] loaded v1.0.0`
- `[23:00:37.489] [fix_sort_tabs] loaded v1.0.0`
- `[23:07:44.777] [fix_sort_tabs] loaded v1.0.0`
- `[23:15:39.465] [fix_sort_tabs] loaded v1.0.0`
- `[23:16:26.023] [fix_sort_tabs] loaded v1.0.0`
- `[23:17:37.579] [fix_sort_tabs] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_st2_footstep` — загрузился

- `[22:18:08.795] [fix_st2_footstep] loaded v1.0.0`
- `[22:21:25.879] [fix_st2_footstep] loaded v1.0.0`
- `[22:39:43.475] [fix_st2_footstep] loaded v1.0.0`
- `[22:50:56.668] [fix_st2_footstep] loaded v1.0.0`
- `[22:52:56.093] [fix_st2_footstep] loaded v1.0.0`
- `[22:54:26.240] [fix_st2_footstep] loaded v1.0.0`
- `[22:57:31.170] [fix_st2_footstep] loaded v1.0.0`
- `[23:00:37.489] [fix_st2_footstep] loaded v1.0.0`
- `[23:07:44.777] [fix_st2_footstep] loaded v1.0.0`
- `[23:15:39.465] [fix_st2_footstep] loaded v1.0.0`
- `[23:16:26.023] [fix_st2_footstep] loaded v1.0.0`
- `[23:17:37.579] [fix_st2_footstep] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_stash_id_desync` — загрузился

- `[22:18:09.832] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[22:18:09.832] [fix_stash_id_desync] loaded v1.0.2`
- `[22:18:31.698] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[22:21:26.724] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[22:21:26.724] [fix_stash_id_desync] loaded v1.0.2`
- `[22:21:42.547] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[22:39:44.301] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[22:39:44.301] [fix_stash_id_desync] loaded v1.0.2`
- `[22:40:00.423] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[22:50:57.496] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[22:50:57.496] [fix_stash_id_desync] loaded v1.0.2`
- `[22:51:12.205] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- … ещё 45 уникальных строк

#### `fix_talents_pda_respec` — загрузился

- `[22:18:09.832] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[22:21:26.724] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[22:39:44.301] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[22:50:57.496] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[22:52:56.914] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[22:54:27.062] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[22:57:31.992] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[23:00:38.313] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[23:07:45.600] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[23:15:40.296] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[23:16:26.866] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[23:17:38.401] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- … ещё 5 уникальных строк

#### `fix_trade_craft_stock` — загрузился

- `[22:18:08.795] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:21:25.879] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:39:43.475] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:50:56.669] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:52:56.093] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:54:26.240] [fix_trade_craft_stock] loaded v1.0.0`
- `[22:57:31.170] [fix_trade_craft_stock] loaded v1.0.0`
- `[23:00:37.489] [fix_trade_craft_stock] loaded v1.0.0`
- `[23:07:44.777] [fix_trade_craft_stock] loaded v1.0.0`
- `[23:15:39.465] [fix_trade_craft_stock] loaded v1.0.0`
- `[23:16:26.023] [fix_trade_craft_stock] loaded v1.0.0`
- `[23:17:37.579] [fix_trade_craft_stock] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_trader_restock_callback` — загрузился

- `[22:18:07.879] [fix_trader_restock_callback] trader_on_restock exists v1.0.3`
- `[22:18:09.553] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[22:18:09.553] [fix_trader_restock_callback] Send wrap installed`
- `[22:21:24.672] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[22:21:26.514] [fix_trader_restock_callback] Send wrap installed`
- `[22:39:42.328] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[22:39:44.102] [fix_trader_restock_callback] Send wrap installed`
- `[22:50:55.503] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[22:50:57.294] [fix_trader_restock_callback] Send wrap installed`
- `[22:52:54.931] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[22:52:56.713] [fix_trader_restock_callback] Send wrap installed`
- `[22:54:25.074] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- … ещё 23 уникальных строк

#### `fix_vows_ambush_stash` — загрузился

- `[22:18:08.795] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:18:09.832] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[22:18:09.832] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:21:25.879] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:21:26.724] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[22:21:26.724] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:39:43.475] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:39:44.301] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[22:39:44.301] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:50:56.669] [fix_vows_ambush_stash] loaded v1.0.1`
- `[22:50:57.496] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[22:50:57.496] [fix_vows_ambush_stash] loaded v1.0.1`
- … ещё 39 уникальных строк

#### `fix_wtf_assault_instacomplete` — загрузился

- `[22:18:08.796] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:18:09.832] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:21:25.879] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:21:26.724] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:39:43.475] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:39:44.301] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:50:56.669] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:50:57.496] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:52:56.093] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:52:56.914] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:54:26.240] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[22:54:27.062] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- … ещё 23 уникальных строк

#### `fix_wtf_fetch_counter` — загрузился

- `[22:18:08.796] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[22:18:09.832] [fix_wtf_fetch_counter] installed v1.0.0`
- `[22:21:25.879] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[22:21:26.724] [fix_wtf_fetch_counter] installed v1.0.0`
- `[22:39:43.475] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[22:39:44.301] [fix_wtf_fetch_counter] installed v1.0.0`
- `[22:50:56.669] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[22:50:57.496] [fix_wtf_fetch_counter] installed v1.0.0`
- `[22:52:56.093] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[22:52:56.914] [fix_wtf_fetch_counter] installed v1.0.0`
- `[22:54:26.240] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[22:54:27.062] [fix_wtf_fetch_counter] installed v1.0.0`
- … ещё 22 уникальных строк

#### `fix_wtf_taskboard_guard` — загрузился

- x2 `...1/bin/..\gamedata\scripts\fix_wtf_taskboard_guard.script:156: quest=communitytracking_shot44869; entity=init$ alife_create_item(|this.section_name|, alife_object(0)).id; macro=init$ alife_create_item(|this.section_nam`
- `[22:18:08.796] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[22:18:09.832] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[22:21:25.879] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[22:21:26.724] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[22:39:43.475] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[22:39:44.302] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[22:50:56.669] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[22:50:57.496] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[22:52:56.093] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[22:52:56.914] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`
- `[22:54:26.240] [fix_wtf_taskboard_guard] loaded v1.0.2`
- … ещё 23 уникальных строк

#### `fix_x15_freeplay_gate` — загрузился

- `[22:18:08.796] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:21:25.879] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:39:43.475] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:50:56.669] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:52:56.093] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:54:26.240] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[22:57:31.170] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[23:00:37.489] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[23:07:44.778] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[23:15:39.465] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[23:16:26.023] [fix_x15_freeplay_gate] loaded v1.0.0`
- `[23:17:37.579] [fix_x15_freeplay_gate] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `fix_x2_gravity_room` — загрузился

- `[22:18:08.796] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:18:09.832] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:21:25.879] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:21:26.724] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:39:43.475] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:39:44.302] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:50:56.669] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:50:57.496] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:52:56.093] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:52:56.914] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:54:26.240] [fix_x2_gravity_room] loaded v1.0.1`
- `[22:54:27.062] [fix_x2_gravity_room] loaded v1.0.1`
- … ещё 22 уникальных строк

#### `fix_xr_effects_sounds` — загрузился

- `[22:18:09.832] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:21:26.724] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:39:44.302] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:50:57.496] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:52:56.914] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:54:27.062] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[22:57:31.993] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[23:00:38.313] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[23:07:45.600] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[23:15:40.296] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[23:16:26.866] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[23:17:38.401] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- … ещё 5 уникальных строк

#### `fix_zat_b12_box` — загрузился

- `[22:18:08.796] [fix_zat_b12_box] loaded v1.0.0`
- `[22:21:25.880] [fix_zat_b12_box] loaded v1.0.0`
- `[22:39:43.475] [fix_zat_b12_box] loaded v1.0.0`
- `[22:50:56.669] [fix_zat_b12_box] loaded v1.0.0`
- `[22:52:56.093] [fix_zat_b12_box] loaded v1.0.0`
- `[22:54:26.240] [fix_zat_b12_box] loaded v1.0.0`
- `[22:57:31.171] [fix_zat_b12_box] loaded v1.0.0`
- `[23:00:37.489] [fix_zat_b12_box] loaded v1.0.0`
- `[23:07:44.778] [fix_zat_b12_box] loaded v1.0.0`
- `[23:15:39.465] [fix_zat_b12_box] loaded v1.0.0`
- `[23:16:26.024] [fix_zat_b12_box] loaded v1.0.0`
- `[23:17:37.579] [fix_zat_b12_box] loaded v1.0.0`
- … ещё 5 уникальных строк

#### `quickqk_task_complete` — загрузился

- `[22:18:09.206] [quickqk_task_complete] loaded v1.4.2`
- `[22:21:26.241] [quickqk_task_complete] loaded v1.4.2`
- `[22:39:43.830] [quickqk_task_complete] loaded v1.4.2`
- `[22:50:57.029] [quickqk_task_complete] loaded v1.4.2`
- `[22:52:56.450] [quickqk_task_complete] loaded v1.4.2`
- `[22:54:26.594] [quickqk_task_complete] loaded v1.4.2`
- `[22:57:31.524] [quickqk_task_complete] loaded v1.4.2`
- `[23:00:37.843] [quickqk_task_complete] loaded v1.4.2`
- `[23:07:45.137] [quickqk_task_complete] loaded v1.4.2`
- `[23:15:39.822] [quickqk_task_complete] loaded v1.4.2`
- `[23:16:26.390] [quickqk_task_complete] loaded v1.4.2`
- `[23:17:37.936] [quickqk_task_complete] loaded v1.4.2`
- … ещё 5 уникальных строк

#### `seamless_inventory_sort_anthology` — загрузился

- `[22:17:36.965] path:tooltip_control/hold_key, key:56, old:nil`
- `[22:17:36.966] path:tooltip_control/trigger_key, key:56, old:nil`
- `[22:18:10.985] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[22:18:10.985] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[22:18:11.003] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[22:21:25.434] path:tooltip_control/hold_key, key:56, old:nil`
- `[22:21:25.434] path:tooltip_control/trigger_key, key:56, old:nil`
- `[22:21:26.884] [seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[22:21:26.884] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[22:21:26.898] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[22:39:43.056] path:tooltip_control/hold_key, key:56, old:nil`
- `[22:39:43.056] path:tooltip_control/trigger_key, key:56, old:nil`
- … ещё 79 уникальных строк

## Нефатальные ошибки

### 1. `igi_text_processor.script` ×1

Триггер: нет строки с `!` / `~` перед блоком

```
[C]: in function 'error'
...gy 2.1/bin/..\gamedata\scripts\igi_text_processor.script:239: in function 'resolve_table_macros'
...anthology 2.1/bin/..\gamedata\scripts\igi_subtask.script:173: in function 'init_entities'
...logy 2.1/bin/..\gamedata\scripts\igi_generic_task.script:160: in function 'initialise_CACHE'
...logy 2.1/bin/..\gamedata\scripts\igi_task_manager.script:237: in function <...logy 2.1/bin/..\gamedata\scripts\igi_task_manager.script:236>
... igi_task_manager.script (line: 644) in function 'on_task_crashed'
... igi_task_manager.script (line: 245) in function 'give_task'
... igi_task_manager.script (line: 570) in function 'give_task'
... pda_taskboard.script (line: 90) in function 'accept_task'
... ui_pda_taskboard_tab.script (line: 140) in function <... ui_pda_taskboard_tab.script:122>
- [22:56:22.350] ------------------------
[22:56:22.350] WTF ERROR: Task crashed! Check PDA Messages or logs for full stack trace. Error:
...1/bin/..\gamedata\scripts\fix_wtf_taskboard_guard.script:156: quest=communitytracking_shot44869; entity=init$ alife_create_item(|this.section_name|, alife_object(0)).id; macro=init$ alife_create_item(|this.section_name|, alife_object(0)).id; expression= alife_create_item(igi_text_processor.Macro.link_context.this.section_name, alife_object(0)).id; error=[WTF Macro Guard v1.0.0] quest=table: 0x17ecbc58; entity=init$ alife_create_item(|this.section_name|, alife_object(0)).id; path=table.id; macro=init$ alife_create_item(|this.section_name|, alife_object(0)).id; expression= alife_create_item(igi_text_processor.Macro.link_context.this.section_name, alife_object(0)).id; error=[string "return  alife_create_item(igi_text_processor...."]:1: attempt to index a nil value\n
- [22:56:22.350] ------------------------
* [22:56:22.466]  [Lua GC/xray-atomic] sequence=90 total=11.69 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.32/8.06/1.87/0.44 ms leaf(marked/unmarked/finalized)=9840526/280/9730858
```

## Куда смотреть

- Блок FATAL ERROR не найден, но есть 1 нефатальных Lua-ошибок, 1 уникальных сигнатур.
- Смотри секцию «Нефатальные ошибки»: повторяющиеся traceback'и — основной класс проблем этой сборки.
- Самая частая: `igi_text_processor.script` ×1.

## Предупреждения (топ 15)

- x54 `! [22:59:13.N]  Failed to render dynamic wallmark`
- x54 `! [23:00:17.N]  Failed to render dynamic wallmark`
- x53 `! [22:59:12.N]  Failed to render dynamic wallmark`
- x53 `! [23:00:18.N]  Failed to render dynamic wallmark`
- x51 `! [23:00:16.N]  Failed to render dynamic wallmark`
- x39 `! [22:58:09.N]  Failed to render dynamic wallmark`
- x38 `! bolt`
- x34 `! [22:59:17.N]  Failed to render dynamic wallmark`
- x30 `! [23:00:20.N]  Failed to render dynamic wallmark`
- x30 `! [23:00:21.N]  Failed to render dynamic wallmark`
- x30 `! [23:00:24.N]  Failed to render dynamic wallmark`
- x29 `! [23:00:22.N]  Failed to render dynamic wallmark`
- x29 `! [23:00:25.N]  Failed to render dynamic wallmark`
- x25 `! [22:59:01.N]  Failed to render dynamic wallmark`
- x23 `! [23:00:26.N]  Failed to render dynamic wallmark`

## Последние строки лога (40)

```
* [23:58:16.295]         :   1: ui_hoc\ui_icon_water
* [23:58:16.295]         :   2: unrealengine\electricblast1
* [23:58:16.295]         :   2: unrealengine\puffcolorsplash
* [23:58:16.295]         :   2: unrealengine\puffcolorsplashflicker
* [23:58:16.295]         :   1: wm\wm_blood_11
* [23:58:16.295]         :   1: wm\wm_blood_1_1
* [23:58:16.295]         :   1: wm\wm_blood_1_3
* [23:58:16.295]         :   1: wm\wm_blood_2
* [23:58:16.295]         :   1: wm\wm_blood_3
* [23:58:16.295]  RM_Dump: rtargets  : 0
* [23:58:16.295]  RM_Dump: vs        : 4
* [23:58:16.295]         :   5: effects_wallmark_blood
* [23:58:16.295]         :  43: particle
* [23:58:16.295]         :  35: particle-clip
* [23:58:16.295]         :  87: stub_notransform_t
* [23:58:16.295]  RM_Dump: ps        : 8
* [23:58:16.295]         :   5: effects_wallmark_blood
* [23:58:16.295]         :  86: hud_default
* [23:58:16.295]         :  36: particle
* [23:58:16.295]         :   7: particle_distort
* [23:58:16.295]         :  17: particle_s-aadd
* [23:58:16.295]         :   3: particle_s-add
* [23:58:16.295]         :  15: particle_s-blend
* [23:58:16.295]         :   1: stub_default
* [23:58:16.295]  RM_Dump: dcl       : 1
* [23:58:16.295]  RM_Dump: states    : 9
* [23:58:16.295]  RM_Dump: tex_list  : 168
* [23:58:16.295]  RM_Dump: matrices  : 0
* [23:58:16.295]  RM_Dump: lst_constants: 0
* [23:58:16.295]  RM_Dump: v_passes  : 170
* [23:58:16.295]  RM_Dump: v_elements: 170
* [23:58:16.295]  RM_Dump: v_shaders : 134
[23:58:16.330] refCount:pBaseZB 1
[23:58:16.330] refCount:pBaseRT 1
[23:58:16.330] refCount:m_pSwapChain 1
[23:58:16.338] DeviceREF: 1
[23:58:17.176] refCount:m_pOutput 1
[23:58:17.177] refCount:m_pAdapter 1
[23:58:17.177] refCount:m_pFactory 1
[23:58:17.359] [xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
