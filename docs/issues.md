# Журнал разобранных проблем

Короткий указатель: «мы это уже разбирали?». Подробности — в CHANGELOG мода / корневом CHANGELOG, в `docs/pitfalls.md`, в карточке `logs/cards/`. Сюда не копируем разборы.

Поиск: `grep -F '## [issue]' docs/issues.md` — все записи; `grep -F '<фрагмент сигнатуры>' docs/issues.md` — по тексту из лога.

Формат блока:

```
## [issue] `<сигнатура как в логе>`

- дата: YYYY-MM-DD
- мод: …
- итог: …
- карточка: [имя](../logs/cards/…) | нет
- pitfalls: … | нет
- подробности: …
```

---

## [issue] `![axr_main callback_set] callback trader_on_restock doesn't exist!`

- дата: 2026-08-31
- мод: `[FIX] Campfires Anthology Compat` (вырезает `AddScriptCallback`); жертвы `barter_core` / `exo_loot`
- итог: починено — `fix_trader_restock_callback` объявляет имя до их `on_game_start`
- карточка: [2026-08-31_xray_mg9000.md](../logs/cards/2026-08-31_xray_mg9000.md); также `…_nikit_diag`, `…_mg9000_after`
- pitfalls: нет
- подробности: `addon/fix_trader_restock_callback/CHANGELOG.md`

## [issue] `CreateTimeEvent … attempt to push nil instead of function`

- дата: 2026-09-01
- мод: BHS `zzzzzz_anthology_bhs_trader_autoinject_patch` + Campfires (`timed_update` локальна в модуле)
- итог: починено в BHS **0.6.8** — резолв `timed_update`, в CTE только локальная `patched_timed_update` (ожидание **71 → 0**)
- карточка: нет
- pitfalls: нет
- подробности: `addon/anthology_busyhands_stability_fix/CHANGELOG.md` [0.6.8] (строка про CTE nil в «Проверено»; число 71 в закоммиченном тексте не расписано)

## [issue] `cannot access class member Alive!` (`grenade_rgn_impact_explosion` / `…_rgo_…`)

- дата: 2026-09-01
- мод: R.A.K minigun (`weapon_minigun_npc_fire_bullet_driven_V3_lite`)
- итог: **не чинится** с нашей стороны — три подхода в `fix_minigun_dead_parent` (pcall → хуже; registry → как без мода; WITHDRAWN)
- карточка: нет (ранее `2026-09-01_xray_nikit_fresh.md`, класс «вылета в логе нет», удалена при чистке 2026-09-13)
- pitfalls: [§16](pitfalls.md) (`pcall` / `gameobjects_registry`)
- подробности: `addon/fix_minigun_dead_parent/CHANGELOG.md`

## [issue] `!ERROR get_object_by_id (2119)`

- дата: 2026-09-01
- мод: WTF / `igi_actions.is_low_condition` (макрос на уничтоженный предмет)
- итог: починено — `fix_wtf_taskboard_guard` **1.0.2** (тихий `level.object_by_id`; ожидание **382 → 0**)
- карточка: нет (след — `diag_log_spam` TRACE)
- pitfalls: нет
- подробности: `addon/fix_wtf_taskboard_guard/CHANGELOG.md`, `addon/diag_log_spam/CHANGELOG.md`

## [issue] `!MCM given bad path:EA_settings/…`

- дата: 2026-09-02
- мод: Interaction Dot Marks (`mcm_paths` → мёртвые `EA_settings/*`)
- итог: DotMarks починен — `fix_fdda_mcm_paths` → `fddar/…`; **три других читателя** (INERTIA Expanded, Glowsticks, BHS Injuries) остались
- карточка: нет (ранее `2026-09-01_xray_nikit-2.md` до фикса, класс «вылета в логе нет», удалена при чистке 2026-09-13)
- pitfalls: нет
- подробности: `addon/fix_fdda_mcm_paths/CHANGELOG.md`

## [issue] `!ERROR item_combination | wrong section names`

- дата: 2026-09-04
- мод: R.A.K 3DSS `mod_craft_magnifiers` (ключи `magnifier:e0t2` и зеркала; `[magnifier]` нет, `e0t2`/`uh2`/`*_magd` есть как scope-addon)
- итог: **не чинится** с нашей стороны — DLTX `!` не снимает ключи с `:` (`ic_keys=10`, `mag_e0t2=true`); VFS-override чужого файла отказались; `fix_item_combination_magnifiers` **1.1.0 WITHDRAWN**
- карточка: нет (ранее `2026-09-01_xray_nikit-2.md`, класс «вылета в логе нет», удалена при чистке 2026-09-13)
- pitfalls: [§16](pitfalls.md) (DLTX `!` + `:`)
- подробности: `addon/fix_item_combination_magnifiers/CHANGELOG.md`

## [issue] `aa_load_recipes_Banjaji_CSI.check_id() | section […] not found!` (в логе «Ѕ_…»)

- дата: 2026-09-02
- мод: источник порчи — LTX **`[GAM] R.A.K Balance`** (байты `EF BF BD` вместо лат. `S`), читает Banjaji CSI
- итог: разобрано, **нашего фикса нет** (чинить апстрим / перекодировку Balance)
- карточка: нет
- pitfalls: нет
- подробности: только переписка разбора 02.09.2026

## [issue] `! ui_hud_dotmarks requires script dotmarks_main, which does not exist or failed to load!`

- дата: 2026-09-01
- мод: Interaction Dot Marks
- итог: **битая установка** в MO2; в следующей сессии **ушло само** (0 строк, DotMarks грузится)
- карточка: нет (ранее `2026-09-01_xray_nikit-2.md`, класс «вылета в логе нет», удалена при чистке 2026-09-13)
- pitfalls: нет
- подробности: отдельного CHANGELOG/фикса нет

## [issue] `action_name CONTACTS/MAP`

- дата: ?
- мод: неизвестен
- итог: ожидание **500 → 4**, «раскладка» — **в репозитории данных нет**; итог из запроса здесь не подтверждён источниками
- карточка: нет
- pitfalls: нет
- подробности: нет

## [issue] `![axr_main callback_set] callback on_game_end doesn't exist!`

- дата: 2026-08-31
- мод: `RegisterScriptCallback("on_game_end")` — такого callback нет; `on_game_end` — точка входа скрипта; у **нашего** Seamless убрано в **1.5.6**; остаток в логах — **чужие** моды
- итог: у нашего Seamless исправлено в **1.5.6**; чужие моды с тем же вызовом остаются
- карточка: [2026-08-31_xray_mg9000.md](../logs/cards/2026-08-31_xray_mg9000.md) (ещё наши скрипты до фикса)
- pitfalls: [§16](pitfalls.md)
- подробности: `addon/seamless_inventory_sort_anthology/CHANGELOG.md` [1.5.6]

## [issue] `ItemProcessor | section [ammo_23_igi_eco] doesn't exist!` + `WTF ERROR: Task crashed` (`communitytracking_shot`)

- дата: 2026-09-05
- мод: WTF Community Task Pack ([Igigog/community-task-pack](https://github.com/Igigog/community-task-pack)), в Anthology влит кусками в `[QUE] wtf 4_2`
- итог: **нашего фикса нет** (вылет и так глотает WTF; `fix_wtf_taskboard_guard` только проясняет причину); обход: MCM `igi_tasks/community/tracking_shot/disabled`
- карточка: [2026-09-05_xray_nikit.md](../logs/cards/2026-09-05_xray_nikit.md)
- pitfalls: [§18](pitfalls.md)
- подробности: нет отдельного фикса

## [issue] `Failed to render dynamic wallmark`

- дата: 2026-09-05
- мод: движок / пул вальмарок
- итог: **игнор / настройка** — снизить `r__wallmark_ttl` (в сессии было 250; ×1047)
- карточка: [2026-09-05_xray_nikit.md](../logs/cards/2026-09-05_xray_nikit.md)
- pitfalls: нет
- подробности: нет

## [issue] `[player_hud::StopScriptAnim()] invalid script_anim_part 255, must be < 3`

- дата: 2026-09-05
- мод: `[TMA] FDDA Redone` `actor_effects` (`stop_hud_motion` на `actor_on_first_update`)
- итог: **к авторам FDDA** / игнор (×32)
- карточка: [2026-09-05_xray_nikit.md](../logs/cards/2026-09-05_xray_nikit.md)
- pitfalls: нет
- подробности: нет

## [issue] `wpo_loot_throttle.script:19: attempt to call global 'IsTimeEventActive' (a nil value)`

- дата: 2026-09-13
- мод: сторонний `wpo_loot_throttle` (в `reference/` файла нет; в `[WPN][2][WPO]…` есть только `wpo_loot.script`); функции **`IsTimeEventActive`** в сборке нет (`refindex` / `lua_help`: 0; семейство только `CreateTimeEvent` / `RemoveTimeEvent` / `ResetTimeEvent`)
- итог: **нашего фикса нет** (не полифиллить чужой API; к автору throttle / снять мод)
- карточка: [2026-09-13_xray_mg9000-1.log.md](../logs/cards/2026-09-13_xray_mg9000-1.log.md)
- pitfalls: нет
- подробности: нет

## [issue] `aaaa_script_fixes_mp.script:936: attempt to call method 'force_set_restrictor_type' (a nil value)`

- дата: 2026-09-13
- мод: ядро Anthology `aaaa_script_fixes_mp` (у тестера xrCore **10037**; в эталоне `reference/anomaly/scripts/aaaa_script_fixes_mp.script` этого вызова нет — строка 936 другая); метода **`force_set_restrictor_type`** нет; похожий — **`set_restrictor_type`** (`bind_anomaly_field.script`; в `lua_help` не описан)
- итог: **нашего фикса нет** (не подменять `force_*` → `set_*` вслепую; обновить `aaaa` / exes до ревизии без вызова)
- карточка: [2026-09-13_xray_Никита.log.md](../logs/cards/2026-09-13_xray_Никита.log.md)
- pitfalls: нет
- подробности: нет

## [issue] `install() fallback via actor_on_first_update` (guards without retry)

- дата: 2026-09-13
- мод: десять без фолбэка — `fix_arena_loadout`, `fix_ashot_aw_travel`, `fix_charon_red_forest_travel`, `fix_crowkiller_hello`, `fix_faction_trade_supply`, `fix_loot_space`, `fix_milspec_exo_craft`, `fix_nta_stashes`, `fix_sim_mechanic_trade`, `fix_wtf_taskboard_guard` (+ два WITHDRAWN не трогали)
- итог: **фолбэк не добавляем**. В `logs/cards/` и `logs/samples/` у этих десяти ни разу не было `guard NOT installed` / `not found` / `ABORT` / `missing` / `partial` от их `install()`. Большинство патчит ванильный модульный API (к `on_game_start` уже на месте) либо цель алфавитно раньше (`aa_*` / `faction_trade_ui`); у `fix_nta_stashes` уже есть повтор на `on_game_load`. Теоретический риск только у `fix_ashot_aw_travel` (`western_goods_utils`) и `fix_wtf_taskboard_guard` (`igi_*` / `pda_taskboard`) — без лог-оснований. У `fix_sim_mechanic_trade` три `printf … not found` только в ветках `else` при провале обёртки; молчание в логе = всё встало.
- карточка: нет (сводка по всем cards/samples)
- pitfalls: [§9](pitfalls.md) (порядок `.script` по имени)
- подробности: разбор 13.09.2026 в чате (фолбэк PR #3 / `fix_dynamic_armor_visuals_nil`)

## [issue] `LUA-001` `fix_crowkiller_hello` / `fix_xr_effects_sounds`

- дата: 2026-09-13
- мод: `fix_crowkiller_hello`, `fix_xr_effects_sounds`
- итог: **ложное срабатывание снято** в инструментах (0.1.62). Линтер матчил хвост `scripts/fix_*.script` на `reference/addons/fix_*-1.0.0/` — **наши же** пакеты без BUILD_INFO. `ReferenceView` больше не индексирует папки `addon/<id>` / `<id>-версия`; fill опознаёт те же имена. Ваниль (`minigame_dialogs` / `xr_effects`) этими аддонами не подменялась — оба уже monkey-patch.
- карточка: нет
- pitfalls: нет
- подробности: `CHANGELOG.md` [0.1.62]
