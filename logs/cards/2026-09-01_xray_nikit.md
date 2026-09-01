# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (447 КБ, 6997 строк)
- Дата разбора: 2026-09-01
- Класс: **вылета в логе нет**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Мои моды

### Не появились в логе (19)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_aim_fatigue_visibility`
- `fix_bhs_fdda_loot`
- `fix_dome_quest`
- `fix_fetch_headlamp`
- `fix_flst_joker_door`
- `fix_grifon_visibility`
- `fix_hip_quest_text`
- `fix_hoc_monolith_icon`
- `fix_indeikam_breeding`
- `fix_nimble_order_desc`
- `fix_okrest_texnik_dialog`
- `fix_sim_mechanic_trade`
- `fix_sort_tabs`
- `fix_st2_footstep`
- `fix_trade_craft_stock`
- `fix_trader_restock_callback`
- `fix_x15_freeplay_gate`
- `fix_zat_b12_box`
- `quickqk_task_complete`

### С отказами (2)

#### `anthology_busyhands_stability_fix` — есть отказы

- `[15:47:23.627] [BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[15:47:24.071] [BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[15:47:26.307] [BusyHandsFix v0.5.3] RepairOnItemSelect was not found at expected load position - repair chain fix will NOT be able to install correctly`
- `[15:47:26.308] [BusyHandsFix v0.6.0] sr_crow_spawner.crowkiller class was not found - guard NOT installed`
- `[15:47:26.308] [BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[15:47:26.308] [BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[15:47:26.308] [BusyHandsFix v0.5.0] global find_close_cover was not found - guard NOT installed`
- `[15:47:26.308] [BusyHandsFix v0.5.0] utils_obj.find_close_cover patched (module-table path)`
- `[15:47:26.308] [BusyHandsFix v0.5.0] item_repair.UIRepair was not found - guard NOT installed`
- `[15:47:26.309] [BusyHandsFix v0.5.3] vendor base OnItemSelect was not captured (load-order marker missing) - repair chain fix NOT installed, recursion bug remains`
- `[15:47:26.309] [BusyHandsFix v0.5.0] ui_inventory.UIInventory.LMode_Init was not found - guard NOT installed`
- `[15:47:26.309] [BusyHandsFix v0.6.0] trader_autoinject patched: 1 functions (function-level, vendor file untouched)`
- … ещё 27 уникальных строк

#### `fix_dotmarks_dropped_weapon` — есть отказы

- `[15:47:26.837] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`
- `[15:48:16.881] [fix_dotmarks_dropped_weapon] ui_hud_dotmarks not found - guard NOT installed`

### В логе без отказов (33)

#### `burnshit_inventory_destroy` — загрузился

- `[15:47:26.315] [BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `context_menu_overhaul_anthology` — загрузился

- `[15:47:26.824] [CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[15:48:16.550] [CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[15:48:16.556] [CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=false | wpo_icons=true`

#### `fix_arena_loadout` — загрузился

- `[15:47:26.837] [fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` — загрузился

- `[15:47:26.837] [fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- `[15:47:26.837] [fix_attribute_assistent] loaded v1.0.0`

#### `fix_aver_darkvalley` — загрузился

- `[15:47:26.837] [fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[15:47:36.142] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=server_entity_on_register`
- `[15:47:36.792] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=server_entity_on_register`
- `[15:48:16.814] [fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[15:48:16.848] [fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24357 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`

#### `fix_charon_red_forest_travel` — загрузился

- `[15:47:26.837] [fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[15:47:26.837] [fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_gigant_space_restriction` — загрузился

- `[15:47:26.837] [fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[15:47:26.837] [fix_gigant_space_restriction] loaded v1.1.0`
- `[15:47:37.534] [fix_gigant_space_restriction] quarantine id=42185 name=gigant_strong42185 section=gigant_strong reason=off_level`
- `[15:47:37.535] [fix_gigant_space_restriction] quarantine id=42257 name=gigant_normal42257 section=gigant_normal reason=off_level`
- `[15:47:37.535] [fix_gigant_space_restriction] quarantine id=42263 name=gigant_normal42263 section=gigant_normal reason=off_level`
- `[15:47:37.633] [fix_gigant_space_restriction] quarantine id=43503 name=gigant_normal43503 section=gigant_normal reason=off_level`
- `[15:47:37.848] [fix_gigant_space_restriction] quarantine id=46769 name=gigant_strong46769 section=gigant_strong reason=off_level`
- `[15:47:37.892] [fix_gigant_space_restriction] quarantine id=47351 name=gigant_normal47351 section=gigant_normal reason=off_level`
- `[15:47:38.035] [fix_gigant_space_restriction] quarantine id=49560 name=gigant_weak49560 section=gigant_weak reason=off_level`
- `[15:47:38.035] [fix_gigant_space_restriction] quarantine id=49561 name=gigant_weak49561 section=gigant_weak reason=off_level`
- `[15:47:38.057] [fix_gigant_space_restriction] quarantine id=50583 name=gigant_normal50583 section=gigant_normal reason=off_level`
- `[15:47:38.206] [fix_gigant_space_restriction] quarantine id=61359 name=gigant_normal61359 section=gigant_normal reason=off_level`
- … ещё 19 уникальных строк

#### `fix_gonta_duplicate_dialog` — есть строки

- `[15:46:22.790] [Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[15:46:29.593] [fix_gonta_duplicate_dialog] stripped %d LTTZ actor_dialog(s) from 2`

#### `fix_kupol_wrong_bone` — загрузился

- `[15:47:26.837] [fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[15:48:16.956] [fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38437 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`

#### `fix_loot_space` — загрузился

- `[15:47:26.837] [fix_loot_space] loaded v1.0.0 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[15:47:26.838] [fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`

#### `fix_misc_script_errors` — загрузился

- `[15:46:22.790] [Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[15:47:00.858] [fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[15:47:26.838] [fix_misc_script_errors] loaded v1.0.0 wrapped mas_scope_detach.on_game_start`

#### `fix_noosphere_voice_x18` — загрузился

- `[15:47:26.838] [fix_noosphere_voice_x18] loaded v1.0.0`

#### `fix_nta_stashes` — загрузился

- `[15:47:26.838] [fix_nta_stashes] v1.0.0 populate wrapped`
- `[15:47:26.838] [fix_nta_stashes] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[15:47:26.838] [fix_pda_buyinfo_gui] loaded v1.0.0 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[15:47:26.838] [fix_ph_door_rx_reload] loaded v1.0.0 wrapped ph_door.try_to_open/close`
- `[15:47:26.838] [fix_ph_door_rx_reload] loaded v1.0.0 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — загрузился

- `[15:47:26.838] [fix_quest_stash] v1.0.2 status functor wrapped`
- `[15:47:26.838] [fix_quest_stash] loaded v1.0.2 section drx_sl_quest_item_1014 exist=yes`

#### `fix_quest_story_id` — загрузился

- `[15:47:26.838] [fix_quest_story_id] v1.0.1 register() wrapped`
- `[15:47:26.838] [fix_quest_story_id] loaded v1.0.1`
- `[15:47:36.714] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[15:47:38.267] [fix_quest_story_id] kept first object 44931 for repeated story_id jup_a9_dogs_normal`
- `[15:48:15.157] [fix_quest_story_id] ignored duplicate object 21766 for story_id jup_b16_oasis_artifact`
- `[15:48:15.263] [fix_quest_story_id] kept first object 44931 for repeated story_id jup_a9_dogs_normal`

#### `fix_radio` — загрузился

- `[15:47:26.838] [fix_radio] loaded v1.0.1`

#### `fix_replace_quest_corpse` — загрузился

- `[15:47:23.615] [fix_replace_quest_corpse] v1.0.0 installed on _G`
- `[15:47:26.838] [fix_replace_quest_corpse] loaded v1.0.0`

#### `fix_rogue_hostility` — загрузился

- `[15:47:26.838] [fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[15:47:26.838] [fix_rx_bandage_dead] loaded v1.0.0 wrapped evaluate/initialize/execute`

#### `fix_soc_nimble_flash` — загрузился

- `[15:47:26.838] [fix_soc_nimble_flash] loaded v1.0.0`

#### `fix_stash_id_desync` — загрузился

- `[15:47:26.838] [fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[15:47:26.838] [fix_stash_id_desync] loaded v1.0.2`
- `[15:48:27.217] [fix_stash_id_desync] repair done spots=0 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- `[15:47:26.838] [fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_vows_ambush_stash` — загрузился

- `[15:47:26.838] [fix_vows_ambush_stash] v1.0.0 activate_by_section wrapped`
- `[15:47:26.838] [fix_vows_ambush_stash] loaded v1.0.0`

#### `fix_wtf_assault_instacomplete` — загрузился

- `[15:47:26.838] [fix_wtf_assault_instacomplete] loaded v1.0.0`

#### `fix_wtf_taskboard_guard` — загрузился

- `[15:47:26.838] [fix_wtf_taskboard_guard] loaded v1.0.0 wrapped=6 missing=0`

#### `fix_x2_gravity_room` — загрузился

- `[15:47:26.838] [fix_x2_gravity_room] loaded v1.0.0`

#### `fix_xr_effects_sounds` — загрузился

- `[15:47:26.838] [fix_xr_effects_sounds] wrapped %d functions, missing %d`

#### `seamless_inventory_sort_anthology` — есть строки

- `[15:47:03.280] path:tooltip_control/hold_key, key:56, old:nil`
- `[15:47:03.280] path:tooltip_control/trigger_key, key:56, old:nil`
- `[15:47:27.351] [Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[15:47:27.390] [Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[15:49:42.078] path:tooltip_control/hold_key, key:56, old:56`
- `[15:49:42.078] path:tooltip_control/trigger_key, key:56, old:56`
- `[15:49:47.848] path:tooltip_control/hold_key, key:56, old:56`
- `[15:49:47.848] path:tooltip_control/trigger_key, key:56, old:56`

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

## Предупреждения (топ 15)

- x4 `! [15:47:16.N] ERROR item_combination | wrong section names`
- x2 `! [15:46:23.N]  Can't find sound 'material\human\step\n_default_5'`
- x2 `! [15:46:23.N]  Can't find sound 'material\human\step\n_default_6'`
- x2 `! [15:46:23.N]  Can't find sound 'material\human\step\n_gravel_6'`
- x2 `! [15:46:23.N]  Can't find sound 'material\human\step\n_gravel_5'`
- x2 `! [15:46:23.N]  Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! [15:46:23.N]  Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_conc_h_04'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_dirt_h_01'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_dirt_h_02'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_dirt_h_03'`
- x2 `! [15:46:23.N]  Can't find sound 'material\shells\small_shell_dirt_h_04'`

## Последние строки лога (40)

```
* [15:49:56.815]         :   1: semitone\environmental\dandelion_seed_v1
* [15:49:56.815]         :   1: semitone\environmental\dandelion_seed_v2
* [15:49:56.815]         :   1: semitone\environmental\maple_seed_v1
* [15:49:56.815]         :   1: semitone\environmental\pfx_leaves_01
* [15:49:56.815]         :   1: semitone\environmental\seed_a
* [15:49:56.815]         :   1: ui\ui_actor_hint_wnd
* [15:49:56.815]         :   1: ui\ui_actor_sleep_screen
* [15:49:56.815]         :   1: ui\ui_common
* [15:49:56.815]         :   1: unrealengine\electricblast1
* [15:49:56.815]         :   1: unrealengine\electricblast2
* [15:49:56.815]         :   1: unrealengine\puffcolorsplashflicker
* [15:49:56.815]  RM_Dump: rtargets  : 0
* [15:49:56.815]  RM_Dump: vs        : 3
* [15:49:56.815]         :  32: particle
* [15:49:56.815]         :  28: particle-clip
* [15:49:56.815]         :   4: stub_notransform_t
* [15:49:56.815]  RM_Dump: ps        : 7
* [15:49:56.815]         :   3: hud_default
* [15:49:56.815]         :  28: particle
* [15:49:56.815]         :   4: particle_distort
* [15:49:56.815]         :  11: particle_s-aadd
* [15:49:56.815]         :   5: particle_s-add
* [15:49:56.815]         :  12: particle_s-blend
* [15:49:56.815]         :   1: stub_default
* [15:49:56.815]  RM_Dump: dcl       : 1
* [15:49:56.815]  RM_Dump: states    : 7
* [15:49:56.815]  RM_Dump: tex_list  : 36
* [15:49:56.815]  RM_Dump: matrices  : 0
* [15:49:56.815]  RM_Dump: lst_constants: 0
* [15:49:56.815]  RM_Dump: v_passes  : 64
* [15:49:56.815]  RM_Dump: v_elements: 64
* [15:49:56.815]  RM_Dump: v_shaders : 36
[15:49:56.829] refCount:pBaseZB 1
[15:49:56.829] refCount:pBaseRT 1
[15:49:56.934] refCount:m_pSwapChain 1
[15:49:56.934] DeviceREF: 226
[15:49:56.934] refCount:m_pOutput 1
[15:49:56.934] refCount:m_pAdapter 1
[15:49:56.934] refCount:m_pFactory 1
[15:49:57.003] [xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
