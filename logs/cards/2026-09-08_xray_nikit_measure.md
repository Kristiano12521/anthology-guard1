# Карточка лога — xray_nikit_measure.log

- Файл: `xray_nikit_measure.log` (840 КБ, 10063 строк)
- Дата разбора: 2026-09-08
- Класс: **вылета в логе нет**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (3)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_item_combination_magnifiers`
- `fix_minigun_dead_parent`

### С отказами (1)

#### `fix_aim_fatigue_visibility` — есть отказы

- `[11:50:11.771] [fix_aim_fatigue_visibility] loaded v1.0.1`
- `[11:50:11.771] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[11:50:15.113] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`
- `[11:51:03.140] [fix_aim_fatigue_visibility] aim_stamina.on_option_change or aim_stamina.load_state not found - guard NOT installed`

### В логе без отказов (62)

#### `anthology_busyhands_stability_fix` — загрузился

- `[11:50:12.317] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[11:50:12.695] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[11:50:14.623] [BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[11:50:14.623] [BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[11:50:14.623] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[11:50:14.624] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[11:50:14.624] [BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[11:50:14.624] [BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[11:50:14.625] [BusyHandsFix v0.6.10] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[11:50:14.625] [BusyHandsFix v0.6.10] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[11:50:14.625] [BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[11:50:14.625] [BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 27 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[11:50:14.631] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` — загрузился

- `[11:50:11.062] [campfires_anthology_compat] loaded v1.1.0`

#### `context_menu_overhaul_anthology` — загрузился

- `[11:50:15.103] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[11:51:01.136] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[11:51:01.139] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`

#### `diag_log_spam` — загрузился

- `[11:50:01.358] [diag_log_spam] early printe hook`
- `[11:50:02.366] [diag_log_spam] init v1.2.3`
- `[11:50:14.629] [diag_log_spam] loaded v1.2.3 (wrappers active)`

#### `diag_pda_task_hint` — загрузился

- `[11:50:11.104] [diag_pda_task_hint] init v1.0.0 (DIAGNOSTIC ONLY)`
- `[11:50:15.104] [diag_pda_task_hint] wrapped task_functor.anomaly_scanner_task_target`
- `[11:50:15.104] [diag_pda_task_hint] diagnostics active v1.0.0`
- `[11:51:02.944] [diag_pda_task_hint] === task dump reason=actor_on_first_update level=la14_rostok_factory ===`
- `[11:51:02.944] [diag_pda_task_hint] scanner_device story=nil (not in alife / not spawned)`
- `[11:51:02.944] [diag_pda_task_hint] task id=simulation_task_61 stage=3 giver=55082 status_fn=measure_task target_fn=general_measure descr_fn=general_measure_desc`
- `[11:51:02.944] [diag_pda_task_hint] task id=simulation_task_61 current_target=55082 current_title=simulation_task_61_name hint_len=272 bad_ctrl=0 preview="Мне встретился какой-то неизвестный сталкер, который попросил пом`
- `[11:51:02.944] [diag_pda_task_hint] task id=simulation_task_61 saved_anom=table: 0x160a4538`
- `[11:51:02.944] [diag_pda_task_hint] task id=simulation_task_61 anomaly_zone MISSING in db.anomaly_by_name`
- `[11:51:02.944] [diag_pda_task_hint] task id=simulation_task_61 engine_get_task=true`
- `[11:51:03.017] [diag_pda_task_hint] WRAP functor task=simulation_task_61 field=target stage=3 result=55082 id=55082 name=sim_default_isg_medic55082 clsid=35`
- `[11:51:03.089] [diag_pda_task_hint] WRAP functor task=simulation_task_61 field=descr stage=3 result=Доложить об успешной установке оборудования. hint_len=44 bad_ctrl=0 preview="Доложить об успешной установке оборудования`
- … ещё 3 уникальных строк

#### `fix_arena_loadout` — загрузился

- `[11:50:15.113] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_arti_frames_nil` — загрузился

- `[11:50:11.772] [fix_arti_frames_nil] loaded v1.0.0`
- `[11:50:15.113] [fix_arti_frames_nil] guard installed v1.0.0`

#### `fix_ashot_aw_travel` — загрузился

- `[11:50:11.772] [fix_ashot_aw_travel] loaded v1.0.1`
- `[11:50:15.113] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- `[11:50:11.772] [fix_attribute_assistent] loaded v1.0.1`
- `[11:50:15.113] [fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` — загрузился

- `[11:50:15.113] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[11:50:24.410] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[11:50:25.117] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[11:51:03.223] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[11:51:03.247] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`

#### `fix_charon_red_forest_travel` — загрузился

- `[11:50:11.772] [fix_charon_red_forest_travel] loaded v1.0.1`
- `[11:50:15.113] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[11:50:15.113] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` — загрузился

- `[11:50:11.772] [fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[11:50:11.773] [fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[11:50:15.113] [fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_dynamic_armor_visuals_nil` — загрузился

- `[11:50:11.773] [fix_dynamic_armor_visuals_nil] loaded v1.0.0`
- `[11:50:15.113] [fix_dynamic_armor_visuals_nil] guard installed v1.0.0`

#### `fix_faction_trade_supply` — загрузился

- `[11:50:11.773] [fix_faction_trade_supply] loaded v1.0.0`
- `[11:50:15.113] [fix_faction_trade_supply] UpdateHarukaTradeWindow wrapped`

#### `fix_fdda_mcm_paths` — загрузился

- `[11:50:11.773] [fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- `[11:50:11.773] [fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- `[11:50:11.773] [fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- `[11:50:11.773] [fix_g2x_torch_meshes] loaded v1.0.1`

#### `fix_gigant_space_restriction` — загрузился

- `[11:50:11.773] [fix_gigant_space_restriction] loaded v1.1.1`
- `[11:50:15.113] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[11:50:15.113] [fix_gigant_space_restriction] loaded v1.1.1`
- `[11:50:24.399] [fix_gigant_space_restriction] quarantine id=6486 name=gigant_strong6486 section=gigant_strong reason=off_level`
- `[11:50:24.456] [fix_gigant_space_restriction] quarantine id=7886 name=gigant_normal7886 section=gigant_normal reason=off_level`
- `[11:50:24.554] [fix_gigant_space_restriction] quarantine id=10092 name=gigant_strong10092 section=gigant_strong reason=off_level`
- `[11:50:24.601] [fix_gigant_space_restriction] quarantine id=11256 name=gigant_normal11256 section=gigant_normal reason=off_level`
- `[11:50:24.748] [fix_gigant_space_restriction] quarantine id=15184 name=gigant_normal15184 section=gigant_normal reason=off_level`
- `[11:50:24.774] [fix_gigant_space_restriction] quarantine id=15753 name=gigant_strong15753 section=gigant_strong reason=off_level`
- `[11:50:24.797] [fix_gigant_space_restriction] quarantine id=16174 name=gigant_strong16174 section=gigant_strong reason=off_level`
- `[11:50:24.875] [fix_gigant_space_restriction] quarantine id=18388 name=gigant_strong18388 section=gigant_strong reason=off_level`
- `[11:50:24.907] [fix_gigant_space_restriction] quarantine id=19142 name=gigant_normal19142 section=gigant_normal reason=off_level`
- … ещё 34 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[08:59:08.058] [fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[08:59:08.058] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[08:59:14.293] [fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`

#### `fix_grifon_visibility` — загрузился

- `[11:50:11.773] [fix_grifon_visibility] loaded v1.1.0`

#### `fix_hip_quest_text` — загрузился

- `[11:50:11.773] [fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- `[11:50:11.773] [fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_hostage_task_collision` — загрузился

- `[11:50:11.774] [fix_hostage_task_collision] loaded v1.0.0`
- `[11:50:15.114] [fix_hostage_task_collision] v1.0.0 wrapped: give_task, setup_companion_task`

#### `fix_indeikam_breeding` — загрузился

- `[11:50:11.774] [fix_indeikam_breeding] loaded v1.1.0`

#### `fix_kupol_wrong_bone` — загрузился

- `[11:50:15.114] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[11:51:03.319] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`

#### `fix_loot_space` — загрузился

- `[11:50:11.774] [fix_loot_space] loaded v1.0.1`
- `[11:50:15.114] [fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[11:50:15.114] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`
- `[11:52:04.204] [fix_milspec_exo_craft] injected 8 new recipes, exo tab 1 now has 7`

#### `fix_misc_script_errors` — загрузился

- `[08:59:08.058] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[08:59:41.627] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[11:50:11.774] [fix_misc_script_errors] loaded v1.0.2`
- `[11:50:15.114] [fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` — загрузился

- `[11:50:11.774] [fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- `[11:50:11.774] [fix_noosphere_voice_x18] loaded v1.0.1`
- `[11:50:15.114] [fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- `[11:50:15.114] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[11:50:15.114] [fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` — загрузился

- `[11:50:11.774] [fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[11:50:11.775] [fix_pda_buyinfo_gui] loaded v1.0.1`
- `[11:50:15.114] [fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[11:50:11.775] [fix_ph_door_rx_reload] loaded v1.0.1`
- `[11:50:15.114] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[11:50:15.114] [fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — есть строки

- `[11:50:11.775] [fix_quest_stash] загружен v1.0.4`
- `[11:50:15.114] [fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[11:50:15.114] [fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`
- `[11:51:04.512] [fix_quest_stash] задание готово task=ratniy_task_8 section=drx_sl_quest_item_1022 reason=actor_has_canonical`

#### `fix_quest_story_id` — загрузился

- `[11:50:11.775] [fix_quest_story_id] loaded v1.0.2`
- `[11:50:15.114] [fix_quest_story_id] v1.0.2 register() wrapped`
- `[11:50:15.114] [fix_quest_story_id] loaded v1.0.2`
- `[11:50:25.009] [fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- `[11:50:25.279] [fix_quest_story_id] kept first object 17703 for repeated story_id jup_a9_dogs_normal`
- `[11:50:59.670] [fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- `[11:50:59.697] [fix_quest_story_id] kept first object 17703 for repeated story_id jup_a9_dogs_normal`

#### `fix_radio` — загрузился

- `[11:50:11.776] [fix_radio] loaded v1.0.2`
- `[11:50:15.114] [fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` — загрузился

- `[11:50:11.776] [fix_replace_quest_corpse] loaded v1.0.1`
- `[11:50:11.776] [fix_replace_quest_corpse] v1.0.1 installed on _G`
- `[11:50:15.114] [fix_replace_quest_corpse] loaded v1.0.1`

#### `fix_rogue_hostility` — загрузился

- `[11:50:15.114] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[11:50:11.776] [fix_rx_bandage_dead] loaded v1.0.1`
- `[11:50:15.114] [fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- `[11:50:11.776] [fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` — загрузился

- `[11:50:11.776] [fix_soc_nimble_flash] loaded v1.0.1`
- `[11:50:15.114] [fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` — загрузился

- `[11:50:11.776] [fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` — загрузился

- `[11:50:11.776] [fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` — загрузился

- `[11:50:15.114] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[11:50:15.114] [fix_stash_id_desync] loaded v1.0.2`
- `[11:51:06.431] [fix_stash_id_desync] repair done spots=0 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- `[11:50:15.114] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` — загрузился

- `[11:50:11.777] [fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- `[11:50:02.366] [fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[11:50:14.629] [fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` — загрузился

- `[11:50:11.777] [fix_vows_ambush_stash] loaded v1.0.1`
- `[11:50:15.114] [fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`
- `[11:50:15.114] [fix_vows_ambush_stash] loaded v1.0.1`

#### `fix_wtf_assault_instacomplete` — загрузился

- `[11:50:11.777] [fix_wtf_assault_instacomplete] loaded v1.0.1`
- `[11:50:15.114] [fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_fetch_counter` — загрузился

- `[11:50:11.777] [fix_wtf_fetch_counter] loaded v1.0.0`
- `[11:50:15.114] [fix_wtf_fetch_counter] installed v1.0.0`

#### `fix_wtf_taskboard_guard` — загрузился

- `[11:50:11.777] [fix_wtf_taskboard_guard] loaded v1.0.2`
- `[11:50:15.114] [fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` — загрузился

- `[11:50:11.777] [fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- `[11:50:11.777] [fix_x2_gravity_room] loaded v1.0.1`
- `[11:50:15.114] [fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` — загрузился

- `[11:50:15.114] [fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- `[11:50:11.778] [fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- `[11:50:13.982] [quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- `[09:00:07.481] path:tooltip_control/hold_key, key:56, old:nil`
- `[09:00:07.481] path:tooltip_control/trigger_key, key:56, old:nil`
- `[11:50:15.521] [seamless_inventory_sort_anthology] loaded v1.5.8-ux-presets`
- `[11:50:15.524] [Seamless Inventory Sort / Anthology 1.5.8-ux-presets] mode=fps keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[11:50:15.562] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[11:53:44.676] path:tooltip_control/hold_key, key:56, old:56`
- `[11:53:44.676] path:tooltip_control/trigger_key, key:56, old:56`
- `[11:53:56.833] path:tooltip_control/hold_key, key:56, old:56`
- `[11:53:56.833] path:tooltip_control/trigger_key, key:56, old:56`

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
