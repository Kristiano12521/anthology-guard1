# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (3.0 МБ, 46599 строк)
- Дата разбора: 2026-09-01
- Класс: **вылета в логе нет**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (16)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_dome_quest`
- `fix_fetch_headlamp`
- `fix_flst_joker_door`
- `fix_g2x_torch_meshes`
- `fix_grifon_visibility`
- `fix_hip_quest_text`
- `fix_hoc_monolith_icon`
- `fix_indeikam_breeding`
- `fix_nimble_order_desc`
- `fix_okrest_texnik_dialog`
- `fix_sort_tabs`
- `fix_st2_footstep`
- `fix_trade_craft_stock`
- `fix_x15_freeplay_gate`
- `fix_zat_b12_box`

### С отказами (3)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[09:45:10.253] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[09:45:10.253] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[09:45:13.103] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[09:45:52.819] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[09:56:27.806] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[09:56:27.806] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[09:56:30.438] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[09:57:05.168] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[10:17:54.519] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[10:17:54.519] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[10:17:57.320] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[10:18:29.252] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- … ещё 4 уникальных строк

#### `fix_dotmarks_dropped_weapon` — есть отказы

- `[09:45:10.254] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[09:45:13.103] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[09:45:52.865] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[09:56:27.808] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[09:56:30.438] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[09:57:05.217] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[10:17:54.522] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[10:17:57.320] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[10:18:29.293] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[10:19:54.486] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[10:19:57.169] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[10:20:32.401] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`

#### `fix_misc_script_errors` — есть отказы

- `[09:44:11.355] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[09:44:45.425] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[09:45:10.256] [fix_misc_script_errors] loaded v1.0.1`
- `[09:45:10.256] [fix_misc_script_errors] mas_scope_detach.on_game_start not found - guard NOT installed`
- `[09:45:13.104] [fix_misc_script_errors] loaded v1.0.1 wrapped mas_scope_detach.on_game_start`
- `[09:56:18.459] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[09:56:27.809] [fix_misc_script_errors] loaded v1.0.1`
- `[09:56:27.809] [fix_misc_script_errors] mas_scope_detach.on_game_start not found - guard NOT installed`
- `[09:56:30.439] [fix_misc_script_errors] loaded v1.0.1 wrapped mas_scope_detach.on_game_start`
- `[10:17:44.750] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[10:17:54.523] [fix_misc_script_errors] loaded v1.0.1`
- `[10:17:54.523] [fix_misc_script_errors] mas_scope_detach.on_game_start not found - guard NOT installed`
- … ещё 5 уникальных строк

### В логе без отказов (36)

#### `anthology_busyhands_stability_fix` — загрузился

- `[09:45:10.278] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[09:45:10.750] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[09:45:12.640] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[09:45:12.640] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[09:45:12.640] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[09:45:12.640] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[09:45:12.641] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[09:45:12.641] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[09:45:12.641] [BusyHandsFix v0.6.6] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[09:45:12.641] [BusyHandsFix v0.6.6] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[09:45:12.641] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[09:45:12.641] [BusyHandsFix v0.6.0] trader_autoinject patched: 1 functions (function-level, vendor file untouched)`
- … ещё 144 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[09:45:12.646] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[09:48:44.741] [BurnShitInventoryDestroy] destroy check | section=detector_anomaly | class=D_CUSTOM | blocked_by=untradeable`
- `[09:53:07.641] [BurnShitInventoryDestroy] destroy check | section=af_cristall_lead_box | class=II_ATTCH | blocked_by=untradeable`
- `[09:53:09.185] [BurnShitInventoryDestroy] destroy check | section=af_dik_2_lead_box | class=II_ATTCH | blocked_by=untradeable`
- `[09:53:10.438] [BurnShitInventoryDestroy] destroy check | section=af_ledenec_lead_box | class=II_ATTCH | blocked_by=untradeable`
- `[09:53:13.694] [BurnShitInventoryDestroy] destroy check | section=af_vedsleza3_lead_box | class=II_ATTCH | blocked_by=untradeable`
- `[09:56:30.101] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[10:16:55.085] [BurnShitInventoryDestroy] destroy check | section=wpn_sil_geks545 | class=WP_SILEN | blocked_by=favorite`
- `[10:17:56.976] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `[10:19:56.833] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`
- `- [10:24:18.775] Callback_Tree | tr: 1 - path: burnshit_inventory_destroy - index: 2`
- `# [10:24:26.775]  Backup [burnshit_inventory_destroy/allowQuestItems] = false`
- … ещё 14 уникальных строк

#### `context_menu_overhaul_anthology` — загрузился

- `[09:45:13.094] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[09:45:51.328] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[09:45:51.331] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `[09:56:30.436] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[09:57:03.768] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[09:57:03.772] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `[10:17:57.318] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[10:18:27.589] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[10:18:27.594] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`
- `[10:19:57.167] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[10:20:30.888] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[10:20:30.891] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`

#### `fix_arena_loadout` — загрузился

- `[09:45:13.103] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[09:56:30.438] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[10:17:57.320] [fix_arena_loadout] bar_arena_teleport wrapped`
- `[10:19:57.169] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` — загрузился

- `[09:45:10.253] [fix_ashot_aw_travel] loaded v1.0.1`
- `[09:45:13.103] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[09:56:27.807] [fix_ashot_aw_travel] loaded v1.0.1`
- `[09:56:30.438] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[10:17:54.520] [fix_ashot_aw_travel] loaded v1.0.1`
- `[10:17:57.320] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`
- `[10:19:54.485] [fix_ashot_aw_travel] loaded v1.0.1`
- `[10:19:57.169] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- `[09:45:10.253] [fix_attribute_assistent] loaded v1.0.1`
- `[09:45:13.103] [fix_attribute_assistent] loaded v1.0.1`
- `[09:56:27.807] [fix_attribute_assistent] loaded v1.0.1`
- `[09:56:30.438] [fix_attribute_assistent] loaded v1.0.1`
- `[10:17:54.520] [fix_attribute_assistent] loaded v1.0.1`
- `[10:17:57.320] [fix_attribute_assistent] loaded v1.0.1`
- `[10:19:54.485] [fix_attribute_assistent] loaded v1.0.1`
- `[10:19:57.169] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` — загрузился

- `[09:45:13.103] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[09:45:20.257] [fix_aver_darkvalley] rewrote dest route=darkvalley_to_aver id=6759 -367.536285, 6.280872, -431.521545 -> 388.674194, -9.332470, -318.518494 gvid=6205 lvid=1490468 dest_level=aver reason=server_entity_on_r`
- `[09:45:20.964] [fix_aver_darkvalley] rewrote dest route=aver_to_darkvalley id=24357 -157.581833, -0.140619, -433.517090 -> -94.382782, -2.695015, -39.998577 gvid=1899 lvid=56202 dest_level=l04_darkvalley reason=server_en`
- `[09:45:52.830] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[09:45:52.849] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `[09:56:30.438] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[09:56:35.235] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[09:56:35.847] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[09:57:05.181] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[09:57:05.200] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `[10:17:57.320] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[10:18:02.155] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- … ещё 8 уникальных строк

#### `fix_charon_red_forest_travel` — загрузился

- `[09:45:10.254] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[09:45:13.103] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[09:56:27.807] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[09:56:30.438] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[10:17:54.521] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[10:17:57.320] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`
- `[10:19:54.485] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[10:19:57.169] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[09:45:13.103] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[09:56:30.438] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[10:17:57.320] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`
- `[10:19:57.169] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_gigant_space_restriction` — загрузился

- `[09:45:10.255] [fix_gigant_space_restriction] loaded v1.1.1`
- `[09:45:13.103] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[09:45:13.103] [fix_gigant_space_restriction] loaded v1.1.1`
- `[09:45:19.986] [fix_gigant_space_restriction] quarantine id=698 name=gigant_weak0698 section=gigant_weak reason=off_level`
- `[09:45:19.986] [fix_gigant_space_restriction] quarantine id=699 name=gigant_weak0699 section=gigant_weak reason=off_level`
- `[09:45:20.308] [fix_gigant_space_restriction] quarantine id=8164 name=gigant_normal8164 section=gigant_normal reason=off_level`
- `[09:45:20.623] [fix_gigant_space_restriction] quarantine id=14462 name=gigant_strong14462 section=gigant_strong reason=off_level`
- `[09:45:20.696] [fix_gigant_space_restriction] quarantine id=16448 name=gigant_strong16448 section=gigant_strong reason=off_level`
- `[09:45:20.879] [fix_gigant_space_restriction] quarantine id=21856 name=gigant_normal21856 section=gigant_normal reason=off_level`
- `[09:45:20.885] [fix_gigant_space_restriction] quarantine id=22098 name=gigant_weak22098 section=gigant_weak reason=off_level`
- `[09:45:20.885] [fix_gigant_space_restriction] quarantine id=22099 name=gigant_weak22099 section=gigant_weak reason=off_level`
- `[09:45:20.991] [fix_gigant_space_restriction] quarantine id=24976 name=gigant_normal24976 section=gigant_normal reason=off_level`
- … ещё 154 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[09:44:11.355] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[09:44:11.355] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[09:44:17.265] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`
- `[09:56:18.458] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[09:56:18.458] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[10:17:44.750] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[10:17:44.750] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[10:19:46.298] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[10:19:46.298] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`

#### `fix_kupol_wrong_bone` — загрузился

- `[09:45:13.103] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[09:45:52.907] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38437 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[09:56:30.438] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[09:57:05.259] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38437 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[10:17:57.320] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[10:18:29.345] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38437 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `[10:19:57.169] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[10:20:32.464] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38437 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`

#### `fix_loot_space` — загрузился

- `[09:45:10.255] [fix_loot_space] loaded v1.0.1`
- `[09:45:13.103] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[09:56:27.808] [fix_loot_space] loaded v1.0.1`
- `[09:56:30.438] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[10:17:54.522] [fix_loot_space] loaded v1.0.1`
- `[10:17:57.320] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`
- `[10:19:54.487] [fix_loot_space] loaded v1.0.1`
- `[10:19:57.169] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[09:45:13.104] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[09:47:19.700] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[09:56:30.439] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[09:58:37.159] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[10:17:57.320] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[10:18:57.756] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`
- `[10:19:57.169] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[10:23:43.877] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`

#### `fix_noosphere_voice_x18` — загрузился

- `[09:45:10.256] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[09:45:13.104] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[09:56:27.809] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[09:56:30.439] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[10:17:54.523] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[10:17:57.320] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[10:19:54.487] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[10:19:57.169] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- `[09:45:13.104] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[09:45:13.104] [fix_nta_stashes] loaded v1.0.0`
- `[09:56:30.439] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[09:56:30.439] [fix_nta_stashes] loaded v1.0.0`
- `[10:17:57.320] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[10:17:57.320] [fix_nta_stashes] loaded v1.0.0`
- `[10:19:57.169] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[10:19:57.169] [fix_nta_stashes] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[09:45:10.256] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[09:45:13.104] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[09:56:27.809] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[09:56:30.439] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[10:17:54.523] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[10:17:57.320] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`
- `[10:19:54.487] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[10:19:57.169] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[09:45:10.257] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[09:45:13.104] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[09:45:13.104] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[09:56:27.809] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[09:56:30.439] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[09:56:30.439] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[10:17:54.523] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[10:17:57.320] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[10:17:57.320] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`
- `[10:19:54.487] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[10:19:57.169] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[10:19:57.169] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — загрузился

- `[09:45:10.258] [fix_quest_stash] loaded v1.0.3`
- `[09:45:13.104] [fix_quest_stash] v1.0.3 status functor wrapped`
- `[09:45:13.104] [fix_quest_stash] loaded v1.0.3 section drx_sl_quest_item_1014 exist=yes`
- `[09:45:53.473] [fix_quest_stash] task ready task=bar_npc_dolg_svayzist_task_4 section=drx_sl_quest_item_1014 reason=actor_has_canonical`
- `[09:56:27.810] [fix_quest_stash] loaded v1.0.3`
- `[09:56:30.439] [fix_quest_stash] v1.0.3 status functor wrapped`
- `[09:56:30.439] [fix_quest_stash] loaded v1.0.3 section drx_sl_quest_item_1014 exist=yes`
- `[09:57:05.812] [fix_quest_stash] task ready task=bar_npc_dolg_svayzist_task_4 section=drx_sl_quest_item_1014 reason=actor_has_canonical`
- `[10:17:54.524] [fix_quest_stash] loaded v1.0.3`
- `[10:17:57.320] [fix_quest_stash] v1.0.3 status functor wrapped`
- `[10:17:57.321] [fix_quest_stash] loaded v1.0.3 section drx_sl_quest_item_1014 exist=yes`
- `[10:18:30.021] [fix_quest_stash] task ready task=bar_npc_dolg_svayzist_task_4 section=drx_sl_quest_item_1014 reason=actor_has_canonical`
- … ещё 4 уникальных строк

#### `fix_quest_story_id` — загрузился

- `[09:45:10.259] [fix_quest_story_id] loaded v1.0.2`
- `[09:45:13.104] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[09:45:13.104] [fix_quest_story_id] loaded v1.0.2`
- `[09:45:20.877] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[09:45:22.043] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[09:45:22.112] [fix_quest_story_id] selected object 57633 for story_id yan_stalker_levsha (replaced 57632)`
- `[09:45:50.190] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[09:45:50.271] [fix_quest_story_id] kept first object 44881 for repeated story_id jup_a9_dogs_normal`
- `[09:45:50.276] [fix_quest_story_id] ignored duplicate object 57632 for story_id yan_stalker_levsha`
- `[09:56:27.810] [fix_quest_story_id] loaded v1.0.2`
- `[09:56:30.439] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[09:56:30.439] [fix_quest_story_id] loaded v1.0.2`
- … ещё 24 уникальных строк

#### `fix_radio` — загрузился

- `[09:45:10.259] [fix_radio] loaded v1.0.2`
- `[09:45:13.104] [fix_radio] loaded v1.0.2`
- `[09:56:27.810] [fix_radio] loaded v1.0.2`
- `[09:56:30.439] [fix_radio] loaded v1.0.2`
- `[10:17:54.524] [fix_radio] loaded v1.0.2`
- `[10:17:57.321] [fix_radio] loaded v1.0.2`
- `[10:19:54.488] [fix_radio] loaded v1.0.2`
- `[10:19:57.169] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` — загрузился

- `[09:45:10.260] [fix_replace_quest_corpse] loaded v1.0.1`
- `[09:45:10.260] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[09:45:13.104] [fix_replace_quest_corpse] loaded v1.0.1`
- `[09:56:27.810] [fix_replace_quest_corpse] loaded v1.0.1`
- `[09:56:27.810] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[09:56:30.439] [fix_replace_quest_corpse] loaded v1.0.1`
- `[10:17:54.525] [fix_replace_quest_corpse] loaded v1.0.1`
- `[10:17:54.525] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[10:17:57.321] [fix_replace_quest_corpse] loaded v1.0.1`
- `[10:19:54.489] [fix_replace_quest_corpse] loaded v1.0.1`
- `[10:19:54.489] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[10:19:57.169] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` — загрузился

- `[09:45:13.104] [fix_rogue_hostility] loaded v1.0.0`
- `[09:56:30.439] [fix_rogue_hostility] loaded v1.0.0`
- `[10:17:57.321] [fix_rogue_hostility] loaded v1.0.0`
- `[10:19:57.169] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[09:45:10.260] [fix_rx_bandage_dead] loaded v1.0.1`
- `[09:45:13.104] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[09:56:27.811] [fix_rx_bandage_dead] loaded v1.0.1`
- `[09:56:30.439] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[10:17:54.526] [fix_rx_bandage_dead] loaded v1.0.1`
- `[10:17:57.321] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`
- `[10:19:54.489] [fix_rx_bandage_dead] loaded v1.0.1`
- `[10:19:57.169] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- `[09:45:10.260] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[09:56:27.811] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[10:17:54.526] [fix_sim_mechanic_trade] loaded v1.0.1`
- `[10:19:54.490] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` — загрузился

- `[09:45:10.260] [fix_soc_nimble_flash] loaded v1.0.1`
- `[09:45:13.104] [fix_soc_nimble_flash] loaded v1.0.1`
- `[09:56:27.811] [fix_soc_nimble_flash] loaded v1.0.1`
- `[09:56:30.439] [fix_soc_nimble_flash] loaded v1.0.1`
- `[10:17:54.527] [fix_soc_nimble_flash] loaded v1.0.1`
- `[10:17:57.321] [fix_soc_nimble_flash] loaded v1.0.1`
- `[10:19:54.490] [fix_soc_nimble_flash] loaded v1.0.1`
- `[10:19:57.169] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_stash_id_desync` — загрузился

- `[09:45:13.104] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[09:45:13.104] [fix_stash_id_desync] loaded v1.0.2`
- `[09:46:02.241] [fix_stash_id_desync] repair done spots=0 cache_entries=0`
- `[09:56:30.439] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[09:56:30.439] [fix_stash_id_desync] loaded v1.0.2`
- `[09:57:13.143] [fix_stash_id_desync] cleared id=36930 reason=not_invbox spots=1 cache=false name=gt_package_artifact36930 section=gt_package_artifact`
- `[09:57:13.143] [fix_stash_id_desync] cleared id=36931 reason=not_invbox spots=1 cache=false name=gt_package_artifact36931 section=gt_package_artifact`
- `[09:57:13.221] [fix_stash_id_desync] cleared id=60472 reason=not_invbox spots=1 cache=false name=gt_package_ammunition60472 section=gt_package_ammunition`
- `[09:57:13.221] [fix_stash_id_desync] cleared id=60473 reason=not_invbox spots=1 cache=false name=gt_package_ammunition60473 section=gt_package_ammunition`
- `[09:57:13.238] [fix_stash_id_desync] repair done spots=4 cache_entries=0`
- `[10:17:57.321] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[10:17:57.321] [fix_stash_id_desync] loaded v1.0.2`
- … ещё 4 уникальных строк

#### `fix_talents_pda_respec` — загрузился

- `[09:45:13.104] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[09:56:30.439] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[10:17:57.321] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`
- `[10:19:57.169] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trader_restock_callback` — загрузился

- `[09:45:03.420] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[09:45:12.644] [fix_trader_restock_callback] Send wrap installed`
- `[09:56:19.510] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[09:56:30.100] [fix_trader_restock_callback] Send wrap installed`
- `[10:17:45.833] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[10:17:56.974] [fix_trader_restock_callback] Send wrap installed`
- `[10:19:47.435] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[10:19:56.832] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` — загрузился

- `[09:45:10.261] [fix_vows_ambush_stash] loaded v1.0.1`
- `[09:45:13.104] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[09:45:13.104] [fix_vows_ambush_stash] loaded v1.0.1`
- `[09:56:27.811] [fix_vows_ambush_stash] loaded v1.0.1`
- `[09:56:30.439] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[09:56:30.439] [fix_vows_ambush_stash] loaded v1.0.1`
- `[10:17:54.527] [fix_vows_ambush_stash] loaded v1.0.1`
- `[10:17:57.321] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[10:17:57.321] [fix_vows_ambush_stash] loaded v1.0.1`
- `[10:19:54.491] [fix_vows_ambush_stash] loaded v1.0.1`
- `[10:19:57.169] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[10:19:57.169] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` — загрузился

- `[09:45:10.261] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[09:45:13.104] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[09:54:50.083] [fix_wtf_assault_instacomplete] recovered 2 squads for smart 36100 (status)`
- `[09:56:27.812] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[09:56:30.439] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[10:17:54.527] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[10:17:57.321] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[10:19:54.491] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[10:19:57.170] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` — загрузился

- `[09:45:10.262] [fix_wtf_taskboard_guard] loaded v1.0.1`
- `[09:45:13.104] [fix_wtf_taskboard_guard] loaded v1.0.1 wrapped=6 missing=0`
- `[09:56:27.812] [fix_wtf_taskboard_guard] loaded v1.0.1`
- `[09:56:30.439] [fix_wtf_taskboard_guard] loaded v1.0.1 wrapped=6 missing=0`
- `[10:17:54.528] [fix_wtf_taskboard_guard] loaded v1.0.1`
- `[10:17:57.321] [fix_wtf_taskboard_guard] loaded v1.0.1 wrapped=6 missing=0`
- `[10:19:54.491] [fix_wtf_taskboard_guard] loaded v1.0.1`
- `[10:19:57.170] [fix_wtf_taskboard_guard] loaded v1.0.1 wrapped=6 missing=0`

#### `fix_x2_gravity_room` — загрузился

- `[09:45:10.262] [fix_x2_gravity_room] loaded v1.0.1`
- `[09:45:13.104] [fix_x2_gravity_room] loaded v1.0.1`
- `[09:56:27.812] [fix_x2_gravity_room] loaded v1.0.1`
- `[09:56:30.439] [fix_x2_gravity_room] loaded v1.0.1`
- `[10:17:54.528] [fix_x2_gravity_room] loaded v1.0.1`
- `[10:17:57.321] [fix_x2_gravity_room] loaded v1.0.1`
- `[10:19:54.491] [fix_x2_gravity_room] loaded v1.0.1`
- `[10:19:57.170] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` — загрузился

- `[09:45:13.104] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[09:56:30.439] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[10:17:57.321] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`
- `[10:19:57.170] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `quickqk_task_complete` — загрузился

- `[09:45:12.074] [quickqk_task_complete] loaded v1.4.2`
- `[09:56:29.657] [quickqk_task_complete] loaded v1.4.2`
- `[10:17:56.497] [quickqk_task_complete] loaded v1.4.2`
- `[10:19:56.394] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — есть строки

- `[09:44:47.356] path:tooltip_control/hold_key, key:56, old:nil`
- `[09:44:47.356] path:tooltip_control/trigger_key, key:56, old:nil`
- `[09:45:13.508] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[09:45:13.542] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[09:56:21.224] path:tooltip_control/hold_key, key:56, old:nil`
- `[09:56:21.224] path:tooltip_control/trigger_key, key:56, old:nil`
- `[09:56:30.764] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[09:56:30.787] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[10:01:17.580] path:tooltip_control/hold_key, key:56, old:56`
- `[10:01:17.581] path:tooltip_control/trigger_key, key:56, old:56`
- `[10:17:00.492] path:tooltip_control/hold_key, key:56, old:56`
- `[10:17:00.493] path:tooltip_control/trigger_key, key:56, old:56`
- … ещё 20 уникальных строк

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

## Предупреждения (топ 15)

- x80 `! [10:11:12.N]  [LUA] CSciptEntity [grenade_rgn_impact_explosion]: cannot access class member Alive!`
- x80 `! [10:11:12.N]  [LUA]  0 : [C  ] alive`
- x80 `! [10:11:12.N]  [LUA]  1 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : register_npc_minigun_bullet`
- x80 `! [10:11:12.N]  [LUA]  2 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : func_or_userdata`
- x80 `! [10:11:12.N]  [LUA]  3 : [Lua] ....3-anthology 2.1/bin/..\gamedata\scripts\axr_main.script(N) : make_callback`
- x80 `! [10:11:12.N]  [LUA]  4 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(N) : SendScriptCallback`
- x80 `! [10:11:12.N]  [LUA]  5 : [Lua] ... 2.1/bin/..\gamedata\scripts\callbacks_gameobject.script(N) :`
- x80 `! [10:11:17.N]  [LUA] CSciptEntity [grenade_rgn_impact_explosion]: cannot access class member Alive!`
- x80 `! [10:11:17.N]  [LUA]  0 : [C  ] alive`
- x80 `! [10:11:17.N]  [LUA]  1 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : register_npc_minigun_bullet`
- x80 `! [10:11:17.N]  [LUA]  2 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : func_or_userdata`
- x80 `! [10:11:17.N]  [LUA]  3 : [Lua] ....3-anthology 2.1/bin/..\gamedata\scripts\axr_main.script(N) : make_callback`
- x80 `! [10:11:17.N]  [LUA]  4 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(N) : SendScriptCallback`
- x80 `! [10:11:17.N]  [LUA]  5 : [Lua] ... 2.1/bin/..\gamedata\scripts\callbacks_gameobject.script(N) :`
- x14 `! [09:45:17.N]  Can't create entity 'hoc_milk'`

## Последние строки лога (40)

```
* [10:28:45.742]         :   1: ui\ui_rak_global_2
* [10:28:45.742]         :   1: ui\ui_rak_global_ammo
* [10:28:45.742]         :   1: ui\ui_rak_global_device
* [10:28:45.742]         :   1: ui\ui_rak_global_knife
* [10:28:45.742]         :   1: ui\ui_stalker2_armors
* [10:28:45.742]         :   1: ui\ui_stalker2_mutantparts
* [10:28:45.742]         :   1: ui\ui_upgrade_indicator
* [10:28:45.742]         :   1: ui\xcvb_achievements\icons
* [10:28:45.742]         :   1: unrealengine\electricblast1
* [10:28:45.742]         :   1: unrealengine\electricblast2
* [10:28:45.742]         :   1: unrealengine\puffcolorsplashflicker
* [10:28:45.742]  RM_Dump: rtargets  : 0
* [10:28:45.742]  RM_Dump: vs        : 3
* [10:28:45.742]         :  39: particle
* [10:28:45.742]         :  34: particle-clip
* [10:28:45.742]         :  46: stub_notransform_t
* [10:28:45.742]  RM_Dump: ps        : 7
* [10:28:45.742]         :  45: hud_default
* [10:28:45.742]         :  34: particle
* [10:28:45.742]         :   5: particle_distort
* [10:28:45.742]         :  15: particle_s-aadd
* [10:28:45.742]         :   5: particle_s-add
* [10:28:45.742]         :  14: particle_s-blend
* [10:28:45.742]         :   1: stub_default
* [10:28:45.742]  RM_Dump: dcl       : 1
* [10:28:45.742]  RM_Dump: states    : 7
* [10:28:45.742]  RM_Dump: tex_list  : 85
* [10:28:45.742]  RM_Dump: matrices  : 0
* [10:28:45.742]  RM_Dump: lst_constants: 0
* [10:28:45.742]  RM_Dump: v_passes  : 119
* [10:28:45.742]  RM_Dump: v_elements: 119
* [10:28:45.742]  RM_Dump: v_shaders : 85
[10:28:45.776] refCount:pBaseZB 1
[10:28:45.776] refCount:pBaseRT 1
[10:28:45.962] refCount:m_pSwapChain 1
[10:28:45.962] DeviceREF: 324
[10:28:45.962] refCount:m_pOutput 1
[10:28:45.962] refCount:m_pAdapter 1
[10:28:45.963] refCount:m_pFactory 1
[10:28:46.115] [xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
