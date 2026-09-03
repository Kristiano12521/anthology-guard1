# Карточка лога — xray_aleks.log

- Файл: `xray_aleks.log` (137 КБ, 1952 строк)
- Дата разбора: 2026-09-03
- Класс: **Lua FATAL / CTD** — не про FPS
- Среда: xrCore build 10057 (MT-TEST 2026.08.21), anomalydx11avx.exe; UserName `Aleks`
- Железо: Ryzen 9 5950X, RTX 5070 Ti; cmdline `-smap1536 -prefetch_sounds`
- Не путать с mg9000: другой ПК, другой билд exes, другая жалоба

## Мои моды

### Не появились в логе (3)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `fix_bhs_fdda_loot`
- `fix_faction_trade_supply`
- `fix_minigun_dead_parent`

### В логе без отказов (58)

#### `anthology_busyhands_stability_fix` — загрузился

- `[BusyHandsFix v0.5.1] Patched guaranteed_loot core loaded (documented full-file exception, see header)`
- `[BusyHandsFix v0.5.0] Patched mon_sleep core loaded (documented full-file exception, see header)`
- `[BusyHandsFix v0.6.6] Captured OnItemSelect via zzzz_arti_jamming_repairs.RepairOnItemSelect before outfit_repair overwrites the shared RepairOnItemSelect global`
- `[BusyHandsFix v0.6.5] crowkiller:check_for_spawn_new_crow patched via sr_crow_spawner.crowkiller (method-level, minimal pcall-only diff, sr_crow_spawner.script untouched)`
- `[BusyHandsFix v0.5.0] ui_inventory.start entry guard installed (z_ui_inventory_dotmarks.script untouched)`
- `[BusyHandsFix v0.6.4] start_body_search / get_template_action_looting_idle patched (module-table, liz_fdda_redone_body_search.script untouched)`
- `[BusyHandsFix v0.6.7] find_close_cover patched via utils_obj.find_close_cover (function-level, utils_obj.script untouched)`
- `[BusyHandsFix v0.6.5] UIRepair patched via item_repair.UIRepair: InitControls/Reset/CollectValidItems/UpdateUi/OnRepair/OnCancel (method-level, zz_item_repair_keep_crafting_window_open.script untouched)`
- `[BusyHandsFix v0.6.10] repair chain UIRepair.OnItemSelect set via item_repair.UIRepair`
- `[BusyHandsFix v0.6.10] item_repair.UIRepair.OnItemSelect chain rebuilt: outfit_repair -> jamming_repairs -> vendor base (recursion bug fixed, self.obj nil-safety applied)`
- `[BusyHandsFix v0.6.5] UIInventory.LMode_Init patched via ui_inventory.UIInventory (method-level, zzz_rax_sortingplus_mcm.script untouched)`
- `[BusyHandsFix v0.6.8] trader_autoinject patched: 6 functions (function-level, vendor file untouched)`
- … ещё 27 уникальных строк

#### `burnshit_inventory_destroy` — загрузился

- `[BurnShitInventoryDestroy] loaded v1.0.6 | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked | destroy_all=always`

#### `campfires_anthology_compat` — загрузился

- `[campfires_anthology_compat] loaded v1.1.0`

#### `context_menu_overhaul_anthology` — загрузился

- `[CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[CMO Anthology] installed late | subclasses=1 | mags_redux=true | toxic_air=true | wpo_icons=true`
- `* [load-session/lua-callbacks] #01 self=258.26 ms source=....1/bin/..\gamedata\scripts\cmo_mags_retool_compat.script:801`
- `* [load-session/lua-callbacks] #20 self=4.77 ms source=...1/bin/..\gamedata\scripts\cmo_anthology_bootstrap.script:65`
- `[CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=33 current_tab=1 category=manual target_tab=1 route=current_manual`

#### `diag_log_spam` — загрузился

- `[diag_log_spam] early printe hook`
- `[diag_log_spam] init v1.2.3`
- `[diag_log_spam] loaded v1.2.3 (wrappers active)`

#### `fix_aim_fatigue_visibility` — загрузился

- `[fix_aim_fatigue_visibility] loaded v1.0.1`
- `[fix_aim_fatigue_visibility] loaded v1.0.1 wrapped on_option_change and load_state`

#### `fix_arena_loadout` — загрузился

- `[fix_arena_loadout] bar_arena_teleport wrapped`

#### `fix_ashot_aw_travel` — загрузился

- `[fix_ashot_aw_travel] loaded v1.0.1`
- `[fix_ashot_aw_travel] get_named_location wrapped (western_goods_guide_dest_mil_base -> mil_smart_terrain_7_7)`

#### `fix_attribute_assistent` — загрузился

- x2 `[fix_attribute_assistent] loaded v1.0.1`

#### `fix_aver_darkvalley` — загрузился

- `[fix_aver_darkvalley] loaded v1.0.1 routes=2`
- `[fix_aver_darkvalley] rewrote dest route=darkvalley_to_aver id=6759 -367.536285, 6.280872, -431.521545 -> 388.674194, -9.332470, -318.518494 gvid=6205 lvid=1490468 dest_level=aver reason=server_entity_on_register`
- `[fix_aver_darkvalley] rewrote dest route=aver_to_darkvalley id=24355 -157.581833, -0.140619, -433.517090 -> -94.382782, -2.695015, -39.998577 gvid=1899 lvid=56202 dest_level=l04_darkvalley reason=server_entity_on_registe`
- `[fix_aver_darkvalley] already fixed route=darkvalley_to_aver id=6759 dest=388.674194, -9.332470, -318.518494 dest_level=aver reason=actor_on_first_update`
- `[fix_aver_darkvalley] already fixed route=aver_to_darkvalley id=24355 dest=-94.382782, -2.695015, -39.998577 dest_level=l04_darkvalley reason=actor_on_first_update`
- `* [load-session/lua-callbacks] #08 self=64.94 ms source=...y 2.1/bin/..\gamedata\scripts\fix_aver_darkvalley.script:520`

#### `fix_charon_red_forest_travel` — загрузился

- `[fix_charon_red_forest_travel] loaded v1.0.1`
- `[fix_charon_red_forest_travel] change_lvl wrapped (red_bridge_bandit_smart_skirmish_mlr -> red_bridge_bandit_smart_skirmish)`

#### `fix_crowkiller_hello` — загрузился

- `[fix_crowkiller_hello] crowkiller_is_valiable wrapped`

#### `fix_dome_quest` — загрузился

- `[fix_dome_quest] loaded v1.0.0`

#### `fix_dotmarks_dropped_weapon` — загрузился

- `[fix_dotmarks_dropped_weapon] loaded v1.0.1`
- `[fix_dotmarks_dropped_weapon] wrapped setup_marker_for_object and main_marker_update_loop`

#### `fix_fdda_mcm_paths` — загрузился

- `[fix_fdda_mcm_paths] loaded v1.0.0`

#### `fix_fetch_headlamp` — загрузился

- `[fix_fetch_headlamp] loaded v1.0.0`

#### `fix_flst_joker_door` — загрузился

- `[fix_flst_joker_door] loaded v1.0.0`

#### `fix_g2x_torch_meshes` — загрузился

- `[fix_g2x_torch_meshes] loaded v1.0.0`

#### `fix_gigant_space_restriction` — загрузился

- x2 `[fix_gigant_space_restriction] loaded v1.1.1`
- `[fix_gigant_space_restriction] wrapped se_monster.can_switch_online`
- `[fix_gigant_space_restriction] quarantine id=42264 name=gigant_strong42264 section=gigant_strong reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=43479 name=gigant_normal43479 section=gigant_normal reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=46767 name=gigant_normal46767 section=gigant_normal reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=47341 name=gigant_normal47341 section=gigant_normal reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=51079 name=gigant_strong51079 section=gigant_strong reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=51643 name=gigant_weak51643 section=gigant_weak reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=51644 name=gigant_weak51644 section=gigant_weak reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=51976 name=gigant_normal51976 section=gigant_normal reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=52108 name=gigant_normal52108 section=gigant_normal reason=off_level`
- `[fix_gigant_space_restriction] quarantine id=52257 name=gigant_weak52257 section=gigant_weak reason=off_level`
- … ещё 19 уникальных строк

#### `fix_gonta_duplicate_dialog` — загрузился

- `[fix_gonta_duplicate_dialog] loaded v1.0.2`
- `[Modded Exes] gathering modxml_fix_gonta_duplicate_dialog.script`
- `[fix_gonta_duplicate_dialog] stripped 2 LTTZ actor_dialog(s) from zat_b106_stalker_gonta`

#### `fix_grifon_visibility` — загрузился

- `[fix_grifon_visibility] loaded v1.0.0`

#### `fix_hip_quest_text` — загрузился

- `[fix_hip_quest_text] loaded v1.0.0`

#### `fix_hoc_monolith_icon` — загрузился

- `[fix_hoc_monolith_icon] loaded v1.1.0`

#### `fix_indeikam_breeding` — загрузился

- `[fix_indeikam_breeding] loaded v1.0.0`

#### `fix_item_combination_magnifiers` — загрузился

- `[fix_item_combination_magnifiers] loaded v1.0.0`

#### `fix_kupol_wrong_bone` — загрузился

- `[fix_kupol_wrong_bone] loaded v1.0.2 target=cit_physic_object_0014 level=az_radar`
- `[fix_kupol_wrong_bone] SKIP fixed_bones mismatch id=38435 visual=dynamics\dead_body\skelet_combine_pose_02 fixed_bones=root expected=link`
- `* [load-session/lua-callbacks] #09 self=56.24 ms source=... 2.1/bin/..\gamedata\scripts\fix_kupol_wrong_bone.script:240`

#### `fix_loot_space` — загрузился

- `[fix_loot_space] loaded v1.0.1`
- `[fix_loot_space] loaded v1.0.1 mutant=SPACE->RETURN loot=SPACE take-all`

#### `fix_milspec_exo_craft` — загрузился

- `[fix_milspec_exo_craft] LoadRecipesLTX wrapped v1.0.2`

#### `fix_misc_script_errors` — загрузился

- `[Modded Exes] gathering modxml_fix_tutorial_hooks.script`
- `[fix_misc_script_errors] wrapped getText for ui\game_tutorials.xml`
- `[fix_misc_script_errors] loaded v1.0.2`
- `[fix_misc_script_errors] loaded v1.0.2 wrapped mas_scope_detach.on_game_start`

#### `fix_nimble_order_desc` — загрузился

- `[fix_nimble_order_desc] loaded v1.0.0`

#### `fix_noosphere_voice_x18` — загрузился

- x2 `[fix_noosphere_voice_x18] loaded v1.0.1`

#### `fix_nta_stashes` — загрузился

- `[fix_nta_stashes] v1.0.0 populate wrapped`
- `[fix_nta_stashes] loaded v1.0.0`

#### `fix_okrest_texnik_dialog` — загрузился

- `[fix_okrest_texnik_dialog] loaded v1.0.0`

#### `fix_pda_buyinfo_gui` — загрузился

- `[fix_pda_buyinfo_gui] loaded v1.0.1`
- `[fix_pda_buyinfo_gui] loaded v1.0.1 wrapped=2 missing=0`

#### `fix_ph_door_rx_reload` — загрузился

- `[fix_ph_door_rx_reload] loaded v1.0.1`
- `[fix_ph_door_rx_reload] loaded v1.0.1 wrapped ph_door.try_to_open/close`
- `[fix_ph_door_rx_reload] loaded v1.0.1 wrapped rx_ai.enable_schemes`

#### `fix_quest_stash` — есть строки

- `[fix_quest_stash] загружен v1.0.4`
- `[fix_quest_stash] v1.0.4 status-функтор обёрнут`
- `[fix_quest_stash] загружен v1.0.4 section drx_sl_quest_item_1014 exist=yes`

#### `fix_quest_story_id` — загрузился

- x2 `[fix_quest_story_id] loaded v1.0.2`
- x2 `[fix_quest_story_id] ignored duplicate object 21764 for story_id jup_b16_oasis_artifact`
- x2 `[fix_quest_story_id] kept first object 44928 for repeated story_id jup_a9_dogs_normal`
- `[fix_quest_story_id] v1.0.2 register() wrapped`

#### `fix_radio` — загрузился

- x2 `[fix_radio] loaded v1.0.2`

#### `fix_replace_quest_corpse` — загрузился

- x2 `[fix_replace_quest_corpse] loaded v1.0.1`
- `[fix_replace_quest_corpse] v1.0.1 installed on _G`

#### `fix_rogue_hostility` — загрузился

- `[fix_rogue_hostility] loaded v1.0.0`

#### `fix_rx_bandage_dead` — загрузился

- `[fix_rx_bandage_dead] loaded v1.0.1`
- `[fix_rx_bandage_dead] loaded v1.0.1 wrapped evaluate/initialize/execute`

#### `fix_sim_mechanic_trade` — загрузился

- `[fix_sim_mechanic_trade] loaded v1.0.1`

#### `fix_soc_nimble_flash` — загрузился

- x2 `[fix_soc_nimble_flash] loaded v1.0.1`

#### `fix_sort_tabs` — загрузился

- `[fix_sort_tabs] loaded v1.0.0`

#### `fix_st2_footstep` — загрузился

- `[fix_st2_footstep] loaded v1.0.0`

#### `fix_stash_id_desync` — загрузился

- `[fix_stash_id_desync] v1.0.2 release_stash_by_id wrapped`
- `[fix_stash_id_desync] loaded v1.0.2`
- `[fix_stash_id_desync] repair done spots=0 cache_entries=0`

#### `fix_talents_pda_respec` — загрузился

- `[fix_talents_pda_respec] loaded v1.0.0 wrapped=7 missing=0`

#### `fix_trade_craft_stock` — загрузился

- `[fix_trade_craft_stock] loaded v1.0.0`

#### `fix_trader_restock_callback` — загрузился

- `[fix_trader_restock_callback] trader_on_restock exists v1.0.3`
- `[fix_trader_restock_callback] trader_on_restock added v1.0.3`
- `[fix_trader_restock_callback] Send wrap installed`

#### `fix_vows_ambush_stash` — загрузился

- x2 `[fix_vows_ambush_stash] loaded v1.0.1`
- `[fix_vows_ambush_stash] v1.0.1 activate_by_section wrapped`

#### `fix_wtf_assault_instacomplete` — загрузился

- x2 `[fix_wtf_assault_instacomplete] loaded v1.0.1`

#### `fix_wtf_taskboard_guard` — загрузился

- `[fix_wtf_taskboard_guard] loaded v1.0.2`
- `[fix_wtf_taskboard_guard] loaded v1.0.2 wrapped=9 missing=0`

#### `fix_x15_freeplay_gate` — загрузился

- `[fix_x15_freeplay_gate] loaded v1.0.0`

#### `fix_x2_gravity_room` — загрузился

- x2 `[fix_x2_gravity_room] loaded v1.0.1`

#### `fix_xr_effects_sounds` — загрузился

- `[fix_xr_effects_sounds] wrapped 19 functions, missing 0`

#### `fix_zat_b12_box` — загрузился

- `[fix_zat_b12_box] loaded v1.0.0`

#### `quickqk_task_complete` — загрузился

- `[quickqk_task_complete] loaded v1.4.2`

#### `seamless_inventory_sort_anthology` — загрузился

- `path:tooltip_control/hold_key, key:56, old:nil`
- `path:tooltip_control/trigger_key, key:56, old:nil`
- `[seamless_inventory_sort_anthology] loaded v1.5.6-hook-cleanup`
- `[Seamless Inventory Sort / Anthology 1.5.6-hook-cleanup] mode=balanced keep_gaps=false trade_policy=additions trade_max_items=300 antifreeze=1.1.3-explicit-item-data`
- `[Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`

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
stack trace:
```

## Стек

```
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (214): xrDebug::gather_info
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (268): xrDebug::backend
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (499): xrDebug::fatal
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrServerEntities\script_engine.cpp (380): CScriptEngine::lua_pcall_failed
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (565): lj_err_run
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (580): err_msgv
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (614): lj_err_optype
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_meta.c (254): lj_meta_cat
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_api.c (1123): lua_pcall
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luabind\luabind\src\pcall.cpp (40): luabind::detail::pcall
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\UIGameSP.cpp (176): CUIGameSP::StartTrade
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\script_game_object.cpp (1125): CScriptGameObject::StartTrade
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\include\functional (882): std::_Func_impl_no_alloc<luabind::detail::mem_fn_callback<void (__cdecl CScriptGameObject::*)(CScriptGameObject *),CScriptGameObject>,int,lua_State *>::_Do_call
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luabind\luabind\src\class_rep.cpp (720): luabind::detail::class_rep::function_dispatcher
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_api.c (1123): lua_pcall
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luabind\luabind\src\pcall.cpp (40): luabind::detail::pcall
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luabind\functor.hpp (380): luabind::detail::proxy_functor_void_caller<CScriptGameObject * const *,CScriptGameObject * const *,char const * const *,char const * const *,char const (*)[1],luabind::object const *>::~proxy_functor_void_caller<CScriptGameObject * const *,CScriptGameObject * const *,char const * const *,char const * const *,char const (*)[1],luabind::object const *>
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\PhraseScript.cpp (270): CDialogScriptHelper::Action
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\PhraseDialog.cpp (111): CPhraseDialog::SayPhrase
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrGame\PhraseDialogManager.cpp (80): CPhraseDialogManager::SayPhrase
```

## Куда смотреть

- Падение при `StartTrade` → `faction_trade_ui.UpdateHarukaTradeWindow`: `attempt to concatenate global 'supply_level' (a function value)`.
- В логе **нет** `fix_faction_trade_supply` — а это как раз наш фикс этой сигнатуры (Faction Based HUD / бармен → `supply_level = nil` → подтягивается функция из `_G` → `..` валит Lua).
- Лечение: поставить `fix_faction_trade_supply` в MO2 после мода с `faction_trade_ui` / `action_trade_ui`; в логе должна появиться строка wrap.
- FPS тут не тема: после загрузки окна ~7–15 ms (~70–140 FPS), до краша игра живая.

## Предупреждения (топ 15)

- x4 `!ERROR item_combination | wrong section names`
- x2 `! Can't find sound 'material\human\step\n_default_5'`
- x2 `! Can't find sound 'material\human\step\n_default_6'`
- x2 `! Can't find sound 'material\human\step\n_gravel_6'`
- x2 `! Can't find sound 'material\human\step\n_gravel_5'`
- x2 `! Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! Can't find sound 'material\shells\small_shell_conc_h_04'`
- x2 `! Can't find sound 'material\shells\small_shell_dirt_h_01'`
- x2 `! Can't find sound 'material\shells\small_shell_dirt_h_02'`
- x2 `! Can't find sound 'material\shells\small_shell_dirt_h_03'`
- x2 `! Can't find sound 'material\shells\small_shell_dirt_h_04'`

## Строки перед падением (40)

```
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=2.62/0.76/0.00/0.14 ms workers(pre/post/bones/game/lua-gc/vision)=0.03/0.00/0.00/1.23/1.21/0.00 ms max(total/frame/render/wait)=7.17/1.37/0.00/4.31 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.08/0.00/0.00/6.38/6.35/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.01/0.01 ms max=0.00/0.03/0.03 ms gc(calls/busy/postload)=1929/8/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=2.62/0.73/0.00/0.10 ms workers(pre/post/bones/game/lua-gc/vision)=0.03/0.00/0.00/1.19/1.17/0.00 ms max(total/frame/render/wait)=7.16/1.28/0.00/4.53 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.10/0.00/0.00/6.49/6.47/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.01/0.01 ms max=0.00/0.02/0.05 ms gc(calls/busy/postload)=2079/7/0
* vid_monitor: live-refresh triggered
* vid_monitor: enumerated 1 monitor(s)
* [Lua GC/xray-atomic] sequence=141 total=10.36 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.03/6.28/2.72/0.33 ms leaf(marked/unmarked/finalized)=4552838/259/4466042
* [Lua GC/xray-atomic] sequence=142 total=11.01 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.01/6.88/2.76/0.36 ms leaf(marked/unmarked/finalized)=4609826/259/4528686
* [Lua GC/xray-atomic] sequence=143 total=10.72 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.06/6.82/2.49/0.35 ms leaf(marked/unmarked/finalized)=4666771/269/4585670
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=8.22/3.84/3.56/0.33 ms workers(pre/post/bones/game/lua-gc/vision)=0.38/0.10/1.08/3.44/1.22/0.12 ms max(total/frame/render/wait)=32.60/13.30/5.93/8.97 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=1.28/0.25/2.37/19.24/11.74/1.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.12/0.18/0.92 ms max=4.44/6.14/12.96 ms gc(calls/busy/postload)=1816/32/0
* [Lua GC/xray-atomic] sequence=144 total=10.25 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.11/6.56/2.27/0.31 ms leaf(marked/unmarked/finalized)=4722208/269/4642582
* [Lua GC/xray-atomic] sequence=145 total=10.88 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.10/6.82/2.58/0.37 ms leaf(marked/unmarked/finalized)=4780329/269/4698013
* [Lua GC/xray-atomic] sequence=146 total=12.56 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.06/8.13/3.01/0.36 ms leaf(marked/unmarked/finalized)=4847848/269/4756146
* [Lua GC/xray-atomic] sequence=147 total=10.83 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.15/6.65/2.60/0.43 ms leaf(marked/unmarked/finalized)=4903472/269/4823665
* [Lua GC/xray-atomic] sequence=148 total=10.69 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.12/6.67/2.49/0.41 ms leaf(marked/unmarked/finalized)=4958934/269/4879289
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=8.59/4.06/3.81/0.33 ms workers(pre/post/bones/game/lua-gc/vision)=0.42/0.11/1.17/3.56/1.23/0.13 ms max(total/frame/render/wait)=65.35/61.28/10.64/10.16 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=1.56/0.17/1.95/16.73/12.82/0.97 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=1.16/0.19/0.98 ms max=4.50/5.77/4.55 ms gc(calls/busy/postload)=1815/26/0
* [Lua GC/xray-atomic] sequence=149 total=10.19 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.14/6.48/2.21/0.35 ms leaf(marked/unmarked/finalized)=5012850/269/4934751
* [Lua GC/xray-atomic] sequence=150 total=10.59 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.06/6.68/2.47/0.38 ms leaf(marked/unmarked/finalized)=5068095/269/4988667
* [Lua GC/xray-atomic] sequence=151 total=10.22 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/1.05/6.45/2.36/0.35 ms leaf(marked/unmarked/finalized)=5120689/269/5043911
* [Lua GC/xray-atomic] sequence=152 total=10.64 ms phases(remark-roots/grayagain/separateudata/mmudata/weak-sweep)=0.00/0.97/6.74/2.54/0.39 ms leaf(marked/unmarked/finalized)=5178453/269/5096506
Time continual is:106639
monkey patching ui_inventory.start
xcvb discounts trader sec: [esc_barman_patogen_pa] not found
[Inventory Antifreeze / Anthology 1.1.3-explicit-item-data] trade bypass | container=actor_trade_bag items=145 reason=af_trade_enabled=false
[Inventory Antifreeze / Anthology 1.1.3-explicit-item-data] trade bypass | container=npc_trade_bag items=165 reason=af_trade_enabled=false
! [SCRIPT ERROR]: ...logy 2.1/bin/..\gamedata\scripts\faction_trade_ui.script:32: attempt to concatenate global 'supply_level' (a function value)
saved condition for hide_pseudodog 0.52999997138977
saved condition for af_grid 1
[id_cleaner_anthology] save_state: initialized=true running=false saved_initialized=true tracked numeric=0 mapped=485 spawn=16139 restore=0 last_released=0 last_spawned=0 retired=0
WeatherManager.save_state saving fields self.weather_file w_partly4, self.last_weather_file w_partly4, self.weather_weight 0.74242621660233, self.cycle partly, self.last_cycle cloudy, self.next_weather w_partly4, self.curr_weather w_partly4
* Saving spawns...
* Saving objects...
* 38653 objects are successfully saved
* Game fatal_ctd_save_1.scop is successfully saved to file 'd:/anthology/anomaly-1.5.3-anthology 2.1/bin/..\appdata\savedgames\fatal_ctd_save_1.scop'
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
