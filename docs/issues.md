# Журнал разобранных проблем

Короткий указатель: «мы это уже разбирали?». Одна строка на случай.
Подробности — в CHANGELOG мода / корневом CHANGELOG, в `docs/pitfalls.md`, в карточке `logs/cards/`.
Сюда не копируем разборы.

Формат: **дата** · сигнатура в логе · чей мод · итог · карточка · pitfalls

---

- **2026-08-31** · `![axr_main callback_set] callback trader_on_restock doesn't exist!` · `[FIX] Campfires Anthology Compat` (вырезает `AddScriptCallback`); жертвы `barter_core` / `exo_loot` · починено: `fix_trader_restock_callback` объявляет имя до их `on_game_start` · [2026-08-31_xray_mg9000.md](../logs/cards/2026-08-31_xray_mg9000.md), также `…_nikit_diag`, `…_mg9000_after` · pitfalls — нет · подробности: `addon/fix_trader_restock_callback/CHANGELOG.md`

- **2026-09-01** · `CreateTimeEvent … attempt to push nil instead of function` · BHS `zzzzzz_anthology_bhs_trader_autoinject_patch` + Campfires (`timed_update` локальна в модуле) · починено в BHS **0.6.8**: резолв `timed_update`, в CTE только локальная `patched_timed_update` (ожидание **71 → 0**) · карточки с этой сигнатурой в `logs/cards/` **нет** · pitfalls — нет · подробности: `addon/anthology_busyhands_stability_fix/CHANGELOG.md` [0.6.8] (строка про CTE nil в «Проверено»; число 71 в закоммиченном тексте не расписано)

- **2026-09-01** · `cannot access class member Alive!` (`grenade_rgn_impact_explosion` / `…_rgo_…`) · R.A.K minigun (`weapon_minigun_npc_fire_bullet_driven_V3_lite`) · **не чинится** с нашей стороны: три подхода в `fix_minigun_dead_parent` (pcall → хуже; registry → как без мода; WITHDRAWN) · [2026-09-01_xray_nikit_fresh.md](../logs/cards/2026-09-01_xray_nikit_fresh.md) · [pitfalls §16](pitfalls.md) (`pcall` / `gameobjects_registry`) · подробности: `addon/fix_minigun_dead_parent/CHANGELOG.md`

- **2026-09-01** · `!ERROR get_object_by_id (2119)` · WTF / `igi_actions.is_low_condition` (макрос на уничтоженный предмет) · починено: `fix_wtf_taskboard_guard` **1.0.2** (тихий `level.object_by_id`; ожидание **382 → 0**) · карточки с этой ERROR-сигнатурой в `logs/cards/` **нет** (след — `diag_log_spam` TRACE) · pitfalls — нет · подробности: `addon/fix_wtf_taskboard_guard/CHANGELOG.md`, `addon/diag_log_spam/CHANGELOG.md`

- **2026-09-02** · `!MCM given bad path:EA_settings/…` · Interaction Dot Marks (`mcm_paths` → мёртвые `EA_settings/*`) · DotMarks починен: `fix_fdda_mcm_paths` → `fddar/…`; **три других читателя** (INERTIA Expanded, Glowsticks, BHS Injuries) остались · [2026-09-01_xray_nikit-2.md](../logs/cards/2026-09-01_xray_nikit-2.md) (до фикса) · pitfalls — нет · подробности: `addon/fix_fdda_mcm_paths/CHANGELOG.md`

- **2026-09-04** · `!ERROR item_combination | wrong section names` · R.A.K 3DSS `mod_craft_magnifiers` (ключи `magnifier:e0t2` и зеркала; `[magnifier]` нет, `e0t2`/`uh2`/`*_magd` есть как scope-addon) · **не чинится** с нашей стороны: DLTX `!` не снимает ключи с `:` (`ic_keys=10`, `mag_e0t2=true`); VFS-override чужого файла отказались; `fix_item_combination_magnifiers` **1.1.0 WITHDRAWN** · [2026-09-01_xray_nikit-2.md](../logs/cards/2026-09-01_xray_nikit-2.md) · [pitfalls §16](pitfalls.md) (DLTX `!` + `:`) · подробности: `addon/fix_item_combination_magnifiers/CHANGELOG.md`

- **2026-09-02** · `aa_load_recipes_Banjaji_CSI.check_id() | section […] not found!` (в логе «Ѕ_…») · источник порчи — LTX **`[GAM] R.A.K Balance`** (байты `EF BF BD` вместо лат. `S`), читает Banjaji CSI · разобрано, **нашего фикса нет** (чинить апстрим / перекодировку Balance) · карточки / CHANGELOG / pitfalls в репозитории **нет** · подробности: только переписка разбора 02.09.2026

- **2026-09-01** · `! ui_hud_dotmarks requires script dotmarks_main, which does not exist or failed to load!` · Interaction Dot Marks · **битая установка** в MO2; в следующей сессии **ушло само** (0 строк, DotMarks грузится) · [2026-09-01_xray_nikit-2.md](../logs/cards/2026-09-01_xray_nikit-2.md) · pitfalls — нет · отдельного CHANGELOG/фикса нет

- **?** · `action_name CONTACTS/MAP` (ожидание **500 → 4**, раскладка) · **в репозитории данных нет**: ни в `logs/cards/`, ни в CHANGELOG, ни в pitfalls · итог из запроса («раскладка») здесь не подтверждён источниками

- **2026-08-31** · `![axr_main callback_set] callback on_game_end doesn't exist!` · `RegisterScriptCallback("on_game_end")` — такого callback нет; `on_game_end` — точка входа скрипта · у **нашего** Seamless убрано в **1.5.6**; остаток в логах — **чужие** моды · [2026-08-31_xray_mg9000.md](../logs/cards/2026-08-31_xray_mg9000.md) (ещё наши скрипты до фикса) · [pitfalls §16](pitfalls.md) · подробности: `addon/seamless_inventory_sort_anthology/CHANGELOG.md` [1.5.6]
