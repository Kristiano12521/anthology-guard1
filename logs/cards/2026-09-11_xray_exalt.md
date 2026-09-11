# Карточка лога — xray_exalt.log

- Файл: `xray_exalt.log` (123 КБ, 1804 строк)
- Дата разбора: 2026-09-11
- Класс: **Lua error (pcall)**
- Среда: xrCore build 10057, anomalydx11avx.exe

## Мои моды

### Не появились в логе (64)

Мод есть в `addon/`, но в логе нет ни одной строки — скорее всего не установлен в MO2 или не попал в пакет.

- `anthology_busyhands_stability_fix`
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
- `fix_quest_stash`
- `fix_quest_story_id`
- `fix_radio`
- `fix_replace_quest_corpse`
- `fix_rogue_hostility`
- `fix_rx_bandage_dead`
- `fix_sim_mechanic_trade`
- `fix_sim_medic_task_dialog`
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
- `quickqk_task_complete`

### В логе без отказов (3)

#### `burnshit_inventory_destroy` — загрузился

- `[BurnShitInventoryDestroy] loaded v1.0.4-beta | confirmation=yes_no | equipped=blocked | favorites=protected | quest_default=blocked | untradeable_default=blocked`

#### `context_menu_overhaul_anthology` — загрузился

- `[CMO Anthology] QAW integration | source functor table patched before/alongside QAW startup`
- `[CMO Anthology] patched submenu class: utils_ui_custom.UICellPropertiesCustom`
- `[CMO Anthology] installed late | subclasses=1 | mags_redux=true | toxic_air=true | wpo_icons=true`
- `[CMO Anthology] QAW integration | live override verified | stage=actor_on_update slot=32 current_tab=1 category=manual target_tab=1 route=current_manual`

#### `seamless_inventory_sort_anthology` — загрузился

- `path:tooltip_control/hold_key, key:56, old:nil`
- `path:tooltip_control/trigger_key, key:56, old:nil`
- `[Tooltip Control / Anthology UI Core 1.4.1-hotfix] initialized | hooks=once callbacks=once delay_helper=local`
- `[Seamless Inventory Sort / Anthology 1.5.2-trade-highlight-optimization-rc] mode=balanced keep_gaps=true trade_policy=additions trade_max_items=300 antifreeze=1.1.2-trade-toggle-test`

## FATAL ERROR

```
FATAL ERROR
[error]Expression    : <no expression>
[error]Function      : CScriptEngine::lua_pcall_failed
[error]File          : X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrServerEntities\script_engine.cpp
[error]Line          : 378
[error]Description   : fatal error
[error]Arguments     :
2 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) :
LUA error: ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script:971: bad argument #1 to 'size' (table expected, got nil)
Check log for details
stack trace:
```

## Кадры скриптов

1. `smart_terrain.script:971`
2. `_g.script:750`
3. `igi_mcm.script:157`
4. `_g_patches.script:1570`
5. `_g.script:461`

## Стек

```
! [LUA]  0 : [C] [C](-1) :
! [LUA]  1 : [C  ] size
! [LUA]  2 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) :
! [LUA]  3 : [C] [C](-1) :
! [LUA]  4 : [C  ] size
! [LUA]  5 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) :
! [LUA]  6 : [C  ] execute
! [LUA]  7 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(750) : exec_console_cmd
! [LUA]  8 : [Lua] ...5.3-anthology 2.1/bin/..\gamedata\scripts\igi_mcm.script(157) : f
! [LUA]  9 : [Lua] ...-anthology 2.1/bin/..\gamedata\scripts\_g_patches.script(1570) : functor_a
! [LUA] 10 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(461) :
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (214): xrDebug::gather_info
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (268): xrDebug::backend
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrCore\xrDebugNew.cpp (499): xrDebug::fatal
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\xrServerEntities\script_engine.cpp (380): CScriptEngine::lua_pcall_failed
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (565): lj_err_run
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (674): lj_err_callermsg
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (706): err_argmsg
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (746): lj_err_argtype
X:\S.T.A.L.K.E.R\A.N.T.H.O.L.O.G.Y\ANTHOLOGY\anthology-mt-engine-alex-src\src\3rd party\luajit-2\src\lj_err.c (752): lj_err_argt
```

## Нефатальные ошибки

### 1. `axr_main.script` ×1

Триггер: `![axr_main callback_set] trying to set callback actor_on_item_use to nil function!`

```
... axr_main.script (line: 253) in function 'callback_set'
... _g.script (line: 104) in function 'RSC'
... dxml_core.script (line: 27) in function 'RegisterScriptCallback'
... mas_scope_detach.script (line: 106) in function 'on_game_start'
... axr_main.script (line: 359) in function 'on_game_start'
... _g.script (line: 82) in function <... _g.script:73>
```

## Куда смотреть

- Класс: Lua error из-под pcall (`CScriptEngine::lua_pcall_failed`).
- Это не обычный lua_error: ошибка всплыла из pcall и всё равно стала fatal. Разбирай, какой pcall это был и что дальше по стеку.
- Первый кадр: smart_terrain.script:971 — найди этот файл в reference/ и открой строку.
- Несколько Lua-ошибок подряд — первая по времени, остальные часто каскад.

## Предупреждения (топ 15)

- x7 `! [LUA]  0 : [C] [C](-1) :`
- x7 `! [LUA]  1 : [C  ] size`
- x7 `! [LUA]  2 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(N) :`
- x4 `!ERROR item_combination | wrong section names`
- x4 `!MCM given bad path:EA_settings/enable_animations`
- x4 `!MCM given bad path:EA_settings/take_item_anim`
- x4 `! [LUA]  3 : [C] [C](-1) :`
- x4 `! [LUA]  4 : [C  ] size`
- x4 `! [LUA]  5 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(N) :`
- x4 `! [LUA]  6 : [C  ] execute`
- x4 `! [LUA]  7 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(N) : exec_console_cmd`
- x4 `! [LUA]  8 : [Lua] ...5.3-anthology 2.1/bin/..\gamedata\scripts\igi_mcm.script(N) : f`
- x4 `! [LUA]  9 : [Lua] ...-anthology 2.1/bin/..\gamedata\scripts\_g_patches.script(N) : functor_a`
- x4 `! [LUA] 10 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(N) :`
- x3 `! [LUA]  3 : [C  ] execute`

## Строки перед падением (40)

```
# SAVING: Water deprivation | last_drink: 2840
[id_cleaner_anthology] save_state: initialized=true running=false saved_initialized=true tracked numeric=0 mapped=485 spawn=16142 restore=0 last_released=0 last_spawned=0 retired=0
* Saving spawns...
* Saving objects...
! [LUA]  0 : [C] [C](-1) : 
! [LUA]  1 : [C  ] size
! [LUA]  2 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) : 
! [LUA]  3 : [C] [C](-1) : 
! [LUA]  4 : [C  ] size
! [LUA]  5 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) : 
! [LUA]  6 : [C  ] execute
! [LUA]  7 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(750) : exec_console_cmd
! [LUA]  8 : [Lua] ...5.3-anthology 2.1/bin/..\gamedata\scripts\igi_mcm.script(157) : f
! [LUA]  9 : [Lua] ...-anthology 2.1/bin/..\gamedata\scripts\_g_patches.script(1570) : functor_a
! [LUA] 10 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(461) : 
! [LUA] SCRIPT RUNTIME ERROR
! [LUA]  0 : [C] [C](-1) : 
! [LUA]  1 : [C  ] size
! [LUA]  2 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) : 
! [LUA]  3 : [C] [C](-1) : 
! [LUA]  4 : [C  ] size
! [LUA]  5 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) : 
! [LUA]  6 : [C  ] execute
! [LUA]  7 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(750) : exec_console_cmd
! [LUA]  8 : [Lua] ...5.3-anthology 2.1/bin/..\gamedata\scripts\igi_mcm.script(157) : f
! [LUA]  9 : [Lua] ...-anthology 2.1/bin/..\gamedata\scripts\_g_patches.script(1570) : functor_a
! [LUA] 10 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(461) : 
! [LUA] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script:971: bad argument #1 to 'size' (table expected, got nil)
! [LUA]  0 : [C] [C](-1) : 
! [LUA]  1 : [C  ] size
! [LUA]  2 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) : 
! [LUA]  3 : [C] [C](-1) : 
! [LUA]  4 : [C  ] size
! [LUA]  5 : [Lua] ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script(971) : 
! [LUA]  6 : [C  ] execute
! [LUA]  7 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(750) : exec_console_cmd
! [LUA]  8 : [Lua] ...5.3-anthology 2.1/bin/..\gamedata\scripts\igi_mcm.script(157) : f
! [LUA]  9 : [Lua] ...-anthology 2.1/bin/..\gamedata\scripts\_g_patches.script(1570) : functor_a
! [LUA] 10 : [Lua] ...ly-1.5.3-anthology 2.1/bin/..\gamedata\scripts\_g.script(461) : 
! [SCRIPT ERROR]: ...thology 2.1/bin/..\gamedata\scripts\smart_terrain.script:971: bad argument #1 to 'size' (table expected, got nil)
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
