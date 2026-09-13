# Карточка лога — xray_evkor.log.txt

- Файл: `xray_evkor.log.txt` (5.8 МБ, 110542 строк)
- Дата разбора: 2026-09-13
- Класс: **вылета нет, есть повторяющиеся ошибки (2 групп)**
- Среда: xrCore build 10025, anomalydx11avx.exe

## Мои моды

### Не появились в логе (65)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `burnshit_inventory_destroy`
- `campfires_anthology_compat`
- `diag_log_spam`
- `fix_aim_fatigue_visibility`
- `fix_arena_loadout`
- `fix_arti_frames_nil`
- `fix_ashot_aw_travel`
- `fix_attribute_assistent`
- `fix_aver_darkvalley`
- `fix_bhs_fdda_loot`
- `fix_charon_red_forest_travel`
- `fix_crowkiller_hello`
- `fix_dome_quest`
- `fix_dotmarks_dropped_weapon`
- `fix_dynamic_armor_visuals_nil`
- `fix_faction_trade_supply`
- `fix_fdda_mcm_paths`
- `fix_fetch_headlamp`
- `fix_flst_joker_door`
- `fix_g2x_torch_meshes`
- `fix_gigant_space_restriction`
- `fix_gonta_duplicate_dialog`
- `fix_grifon_visibility`
- `fix_hip_quest_text`
- `fix_hoc_monolith_icon`
- `fix_hostage_task_collision`
- `fix_indeikam_breeding`
- `fix_item_combination_magnifiers`
- `fix_kupol_wrong_bone`
- `fix_loot_space`
- `fix_milspec_exo_craft`
- `fix_minigun_dead_parent`
- `fix_misc_script_errors`
- `fix_nimble_order_desc`
- `fix_noosphere_voice_x18`
- `fix_nta_stashes`
- `fix_okrest_texnik_dialog`
- `fix_pda_buyinfo_gui`
- `fix_ph_door_rx_reload`
- `fix_qaw_ammo_nil`
- `fix_quest_stash`
- `fix_quest_story_id`
- `fix_radio`
- `fix_replace_quest_corpse`
- `fix_rogue_hostility`
- `fix_rx_bandage_dead`
- `fix_sim_mechanic_trade`
- `fix_sim_medic_task_dialog`
- `fix_smart_terrain_state_write`
- `fix_soc_nimble_flash`
- `fix_sort_tabs`
- `fix_st2_footstep`
- `fix_stale_fetch_marker`
- `fix_stash_id_desync`
- `fix_talents_pda_respec`
- `fix_trade_craft_stock`
- `fix_trader_restock_callback`
- `fix_vows_ambush_stash`
- `fix_wtf_assault_instacomplete`
- `fix_wtf_fetch_counter`
- `fix_wtf_taskboard_guard`
- `fix_x15_freeplay_gate`
- `fix_x2_gravity_room`
- `fix_xr_effects_sounds`
- `fix_zat_b12_box`

### В логе без отказов (4)

#### `anthology_busyhands_stability_fix` — загрузился

- x13 `[BusyHandsFix v0.4.8] Patched sr_crow_spawner core loaded`
- x13 `[BusyHandsFix v0.4.8] Patched mon_sleep core loaded`
- x13 `* loading script zzzzzz_anthology_busyhands_stability_fix.script`
- x13 `[BusyHandsFix] Anthology Busy Hands Stability Fix 0.4.8-beta-hotfix loaded`
- x13 `[BusyHandsFix v0.4.8] Crow spawner guard mode: loose core replacement`
- x13 `[BusyHandsFix v0.4.8] mon_sleep guard mode: loose core replacement`
- x13 `[BusyHandsFix v0.4.8] Trader/Western Goods guards installed: 8`
- x13 `[BusyHandsFix v0.4.8] Crow spawner guards installed: 1`
- x13 `[BusyHandsFix v0.4.8] mon_sleep guards installed: 1`

#### `context_menu_overhaul_anthology` — загрузился

- x14 `* loading script context_menu_overhaul__ap_mcm.script`
- x14 `* loading script context_menu_overhaul_mcm.script`
- x13 `* loading script context_menu_overhaul.script`
- x13 `* loading script context_menu_overhaul_utils.script`
- x13 `* loading script context_menu_overhaul_wpo.script`
- x13 `* loading script zzzzzzzzzz_context_menu_overhaul_anthology.script`
- x13 `[CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- x13 `[CMO Anthology] installed late | subclasses=1 | mags_redux=false | toxic_air=true | wpo_icons=true`

#### `quickqk_task_complete` — есть строки

- x14 `* loading script zzzzzz_quickqk_task_complete_anthology_mcm.script`
- x13 `* loading script zzzzzz_quickqk_task_complete_anthology.script`

#### `seamless_inventory_sort_anthology` — есть строки

- x18 `path:tooltip_control/hold_key, key:56, old:56`
- x18 `path:tooltip_control/trigger_key, key:56, old:56`
- x14 `* loading script tooltip_control_mcm.script`
- x14 `path:tooltip_control/hold_key, key:56, old:nil`
- x14 `path:tooltip_control/trigger_key, key:56, old:nil`
- x13 `* loading script tooltip_control.script`
- x13 `* loading script tooltip_control_utils.script`
- x13 `* loading script tooltip_fixes.script`

## Нефатальные ошибки

### 1. `axr_main.script` ×13

Триггер: `![axr_main callback_set] trying to set callback actor_on_item_use to nil function!`

```
... axr_main.script (line: 259) in function 'callback_set'
... _g.script (line: 104) in function 'RSC'
... dxml_core.script (line: 27) in function 'RegisterScriptCallback'
... mas_scope_detach.script (line: 106) in function 'on_game_start'
... axr_main.script (line: 333) in function 'on_game_start'
... _g.script (line: 82) in function <... _g.script:73>
```

### 2. `zz_cop_phys_story_id_fix.script` ×1

Триггер: нет строки с `!` / `~` перед блоком

```
... _g.script (line: 2215) in function 'original_alife_release'
... zz_cop_phys_story_id_fix.script (line: 456) in function 'alife_release_id'
... item_weapon.script (line: 391) in function 'ammo_aggregation'
... game_setup.script (line: 537) in function 'func_or_userdata'
... axr_main.script (line: 284) in function 'make_callback'
... _g.script (line: 118) in function 'SendScriptCallback'
... bind_stalker_ext.script (line: 143) in function <... bind_stalker_ext.script:139>
```

## Куда смотреть

- Блок FATAL ERROR не найден, но есть 14 нефатальных Lua-ошибок, 2 уникальных сигнатур.
- Смотри секцию «Нефатальные ошибки»: повторяющиеся traceback'и — основной класс проблем этой сборки.
- Самая частая: `axr_main.script` ×13.

## Предупреждения (топ 15)

- x1162 `~[WG] WARNING | Utils | Trying to set HUD bone 'lid' visibility in third person ! Fallback to 'wpn_body'`
- x1150 `~[WG] WARNING | Utils | Trying to set HUD bone 'flame' visibility in third person ! Fallback to 'wpn_body'`
- x838 `! Failed to render dynamic wallmark`
- x108 `!ERROR get_object_by_id | no game object recieved from id (N)`
- x80 `! [LUA] CSciptEntity [grenade_rgn_impact_explosion]: cannot access class member Alive!`
- x80 `! [LUA]  0 : [C  ] alive`
- x80 `! [LUA]  1 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : register_npc_minigun_bullet`
- x80 `! [LUA]  2 : [Lua] ...pts\weapon_minigun_npc_fire_bullet_driven_v3_lite.script(N) : func_or_userdata`
- x80 `! [LUA]  3 : [Lua] ....3-anthology 2.1/bin/..\gamedata\scripts\axr_main.script(N) : make_callback`
- x80 `! [LUA]  4 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(N) : SendScriptCallback`
- x80 `! [LUA]  5 : [Lua] ... 2.1/bin/..\gamedata\scripts\callbacks_gameobject.script(N) :`
- x60 `!MCM given bad path:EA_settings/enable_animations`
- x60 `!MCM given bad path:EA_settings/take_item_anim`
- x56 `!ERROR item_combination | wrong section names`
- x52 `~ Story Objects | Multiple objects trying to use same story_id jup_b16_oasis_artifact`

## Последние строки лога (40)

```
*        :   2: wpn\wpn_addons\wpn_addon_silencer\wpn_addon_sil_9mm
*        :   2: wpn\wpn_addons\wpn_addon_silencer\wpn_addon_sil_9mm_bump
*        :   1: wpn\wpn_addons\wpn_addon_silencer\wpn_addon_sil_9mm_bump#
*        :   2: wpn\wpn_mag_5x45_30rnd_backelite
*        :   2: wpn\wpn_mag_5x45_30rnd_backelite_bump
*        :   1: wpn\wpn_mag_5x45_30rnd_backelite_bump#
*        :   2: wpn\wpn_toz-194\wpn_toz-194
*        :   2: wpn\wpn_toz-194\wpn_toz-194_bump
*        :   1: wpn\wpn_toz-194\wpn_toz-194_bump#
* RM_Dump: rtargets  : 0
* RM_Dump: vs        : 7
*        :   5: deffer_model_bump
*        :   5: deffer_model_bump-hq
*        :   6: effects_wallmark_blood
*        :  38: particle
*        :  34: particle-clip
*        :   1: shadow_direct_model
*        :  59: stub_notransform_t
* RM_Dump: ps        : 11
*        :   5: deffer_base_bump
*        :   5: deffer_base_bump-hq
*        :   1: dumb
*        :   6: effects_wallmark_blood
*        :  58: hud_default
*        :  34: particle
*        :   4: particle_distort
*        :  15: particle_s-aadd
*        :   5: particle_s-add
*        :  14: particle_s-blend
*        :   1: stub_default
* RM_Dump: dcl       : 2
* RM_Dump: states    : 10
* RM_Dump: tex_list  : 148
* RM_Dump: matrices  : 0
* RM_Dump: lst_constants: 0
* RM_Dump: v_passes  : 148
* RM_Dump: v_elements: 148
* RM_Dump: v_shaders : 108
DeviceREF: 442
[xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
