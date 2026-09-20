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

## [issue] softlock PDA Объявление — клик по заданию (accept)

- дата: 2026-09-20
- мод: `fix_drx_enemy_task_gate` 1.0.2 + `fix_hostage_task_collision` 1.0.1 + `fix_taskboard_sync` 1.0.3; diag `diag_taskboard_accept` 1.0.0–1.0.3
- симптом: клик по заданию в Объявлении → «залипание» (ввод мёртв / мир не отвечает), без FATAL. Примеры: `bar_visitors_barman_stalker_trader_task_4`, `simulation_task_48`.
- классы (триаж по кадрам):
  - **Кадры продолжают идти** после «залипания» → Lua/update живы, завис **ввод**: сток `pda_taskboard.accept_task` держит `currently_processed_npc_id`, `z_taskboard_overrides` делает `is_talking()==true`; если `give_task` не дошёл до сброса id — softlock ввода. Не путать с зависанием `prepare_task` / генерации офферов (там клика ещё нет).
  - **Кадры стоят**, HEARTBEAT/`actor_on_update` молчит → синхронный hang в Lua на пути `accept`→`CRandomTask.give_task` (этот случай).
- диагностика: `diag_taskboard_accept` — `accept begin` без `done`; 1.0.2 `before next-hop` без `after`; 1.0.3 `next-hop src=fix_drx_enemy_task_gate.script:177`. Подтвердило: late `install()` у DRX/hostage переназначал `orig.give_task` на peer → цикл DRX↔hostage (tail-call), `give_task` не возвращается.
- итог: **починено и проверено** — `orig` только при первом захвате; sync accept под `pcall` без окна `currently_processed`. Лог 20:55–20:57: **13×** `accept begin` → ванильный `CRandomTask:give_task()` → `accept done` (fetch + delivery), FATAL нет, diag снят.
- карточка: нет; `logs/xray_nikit_softlock_fixed.log`, локализация `logs/xray_nikit_diag_103.log`
- pitfalls: два monkey-patch на один `give_task` не перезаписывают `orig` при reclaim; diag не должен re-wrap `CRandomTask.give_task` в цикле с peer
- подробности: CHANGELOG `fix_drx_enemy_task_gate` [1.0.2], `fix_hostage_task_collision` [1.0.1], `fix_taskboard_sync` [1.0.3], `diag_taskboard_accept`


## [issue] `rvr_storage_system_engine.script:1835: attempt to index global 'ActiveStorages' (a nil value)`

- дата: 2026-09-20
- мод: [GAM] Optimized Storage System (`rvr_storage_system_engine.og_inventory_start`) + наш `fix_rvr_active_storages_nil` 1.0.0; путь: DotMarks → `hidden_anom_stash` / inventory start
- итог: **починено** — до фикса FATAL `lua_pcall_failed` на `ActiveStorages[obj:id()]` без nil-check (в логе краша `fix_rvr_*` ещё не было). После установки: в сессии nikit 20.09 `guard installed v1.0.0`, FATAL по этой сигнатуре нет. Подтверждение в игре (открыть anomalous stash) — в CHANGELOG ещё «не подтверждено».
- карточка: [2026-09-20_xray_mg9000-14.md](../logs/cards/2026-09-20_xray_mg9000-14.md) (источник `xray_mg9000 (1)4.log`); пост-фикс baseline: [2026-09-20_xray_nikit.md](../logs/cards/2026-09-20_xray_nikit.md)
- pitfalls: нет
- подробности: `addon/fix_rvr_active_storages_nil/CHANGELOG.md` [1.0.0]

## [issue] nikit 2026-09-20: чистая сессия после пакета новых фиксов (динамика)

- дата: 2026-09-20
- мод: пакет фиксов 20.09 (`fix_create_squad_nil_smart`, `fix_rvr_active_storages_nil`, `fix_drx_enemy_task_gate`, `fix_taskboard_sync` 1.0.2, `fix_wtf_taskboard_guard` 1.0.4, `fetch_remote_storage` 1.1.0, …); Бар / ~2 мин; штатный выход
- итог: **динамика / baseline** — класс `вылета в логе нет`; `nonfatal_groups=0`. Новые wrap'ы встали (`create_squad` / `SIMBOARD.create_squad`, RVR guard, DRX hide/block ×6, taskboard reuse). Известные отказы API без динамики (см. guard NOT installed + `aim_stamina` / `fix_utjan_mag_skill` magazines). Чужой `xrs_dyn_music` → `on_game_end` (уже в журнале). `item_combination | wrong section names` ×4 — уже в журнале / WITHDRAWN.
- карточка: [2026-09-20_xray_nikit.md](../logs/cards/2026-09-20_xray_nikit.md) (источник appdata `xray_nikit.log` 19:20–19:24)
- pitfalls: нет
- подробности: нет

## [issue] native `UnhandledFilter` / `CDialogHolder::OnFrame` (меню сразу после load)

- дата: 2026-09-20
- мод: нативный UI (`UIDialogHolder.cpp` / `MainMenu.cpp`); mg9000, Припять (`pri_b306`); падение сразу после успешной загрузки `quicksave_4` (ещё до `actor-spawn-addon`), пока тикает `CMainMenu`
- итог: **не чинится скриптом** — класс **`нативный вылет (не Lua)`**; стек `UnhandledFilter` → `CDialogHolder::OnFrame` → `CMainMenu::OnFrame` → `FrameMove`. FATAL ERROR нет. Соседний класс к `DoRenderDialogs` (19.09, другой кадр того же держателя диалогов). Контекст: 24-я загрузка сейва в одном процессе, третья подряд `quicksave_4` (два предыдущих раза тот же сейв доходил до `actor_on_first_update`); на последней — `static level already active`. Нефатальные `ui_inventory`/`ish_fast_transfer` и `xr_logic.parse_condlist` — далеко по времени, к CTD не ведут. mdmp от этой сессии в `logs/` нет.
- карточка: [2026-09-20_111xray_mg9000.md](../logs/cards/2026-09-20_111xray_mg9000.md) (источник `111xray_mg9000 (1).log`)
- pitfalls: нет
- подробности: повтор — (A) свежий exe + один load `quicksave_4`; (B) после N load в одном процессе. При стабильном повторе — mdmp + PDB в Anthology/Modded Exes. Связанные: `DoRenderDialogs` 19.09, `rp_ScreenResolutionChanged` 19.09.

## [issue] native `UnhandledFilter` / `CPHSimpleCharacter::UpdateDynamicDamage` + `InitContact`

- дата: 2026-09-19
- мод: нативный xrPhysics (актор); падение на `l05_bar` ~1.7 с после закрытия UIInventory (лут `bar_bar_drunk_dolg` / duty-трупов); DotMarks `block_loot_window` в логе есть, но инвентарь всё равно открывался
- итог: **не чинится скриптом** — AV в `UpdateDynamicDamage` на контакте (`InitContact` → `CollideDynamics` → `PHWorld::Step` → `GameThread`). Адрес `0x1C53C00160` вне модулей (`SymGetModuleInfo64` 1114) — типичный битый указатель/UAF в колбэке контакта, не Lua. На уровне в той же сессии: `smart-cover repair … invalid=40`, exclusive job smartcover `[nil]` у `bar_visitors` — возможный фон, связь с CTD **не доказана**. Не DrawHint / DoRenderDialogs / ScreenResolution.
- карточка: [2026-09-19_newxray_nikit.md](../logs/cards/2026-09-19_newxray_nikit.md) (источник `newxray_nikit.log`; 9 загрузок)
- pitfalls: нет
- подробности: mdmp `logs/xray_nikit_09-19-26_22-19-50.mdmp`; детект `stack trace:` с таймстемпом — `tools/xraylog.py` (`STACK_RE`). Следующий шаг: повтор на Баре (A) без лута, (B) с лутом без DotMarks; mdmp в WinDbg; при стабильном повторе — в Anthology/Modded Exes с PDB.

## [issue] `sound_theme` abort: `There are no sound collection with path: scenario\black_valley\blck_val_robbery_scene_come_here_pda`

- дата: 2026-09-19
- мод: PA black_valley — секция `[blck_val_robbery_scene_see_actor]` в `script_sound_pa_black_valley.ltx` (`path = scenario\black_valley\blck_val_robbery_scene_come_here_pda`); загрузка через `sound_theme` `object_sound`/`actor_sound` → `abort` (ваниль)
- итог: **ассет сборки** — в runtime нет `.ogg` по этому path (коллекция пустая → abort). Нефатально (×2 на 1-й загрузке `black_valley`). Нашего фикса нет: чинить пакет звуков PA / Anthology, не monkey-patch `abort`.
- карточка: [2026-09-19_newxray_nikit.md](../logs/cards/2026-09-19_newxray_nikit.md)
- pitfalls: нет
- подробности: эталон LTX `reference/anomaly/configs/misc/sound/script_sound_pa_black_valley.ltx:49–54`; abort `sound_theme.script:459` / `:644`

## [issue] `! ERROR: veh_btr… trying to use a scheme not intended for stype scheme=ph_car stype=nil`

- дата: 2026-09-19
- мод: `ph_car` зарегистрирован на `stype_item` (`modules.script`); ошибка из `xr_logic.activate_by_section` когда `db.storage[id].stype == nil`. Типичный путь: `logic_enforcer.assign` (WG / `tasks_veh_destroy`) → `switch_to_section` на объекте, у которого `st` уже есть (после `bind_car:reinit`), но `initialize_obj` ещё не выставил `stype`
- итог: **игнор / гонка биндера** — ×4 BTR одним кадром на загрузке Escape (`veh_btr56839…41`); схема не ставится (`return`), CTD нет. Нашего фикса нет, пока нет повторяемого геймплейного бага (машина без AI). Опциональный гард: в `logic_enforcer` не вызывать switch, пока `st.stype` nil.
- карточка: [2026-09-19_newxray_nikit.md](../logs/cards/2026-09-19_newxray_nikit.md)
- pitfalls: нет
- подробности: `xr_logic.script:226–228`, `bind_car.script:17–29`, `logic_enforcer.script:56–89`

## [issue] `WTF ERROR: Task crashed` — `ghentuongsupply*` / макрос `gt_guard` + `fix_wtf_taskboard_guard`

- дата: 2026-09-19
- мод: WTF/IGI quest `ghentuongsupply46074` + наш `fix_wtf_taskboard_guard` (`is_valid_quest`); макрос `$ igi_helper.db_ini:r_value('gt_guard', |this.faction|)`
- итог: **гард сработал** (quest rejected during validation) — не CTD; апстрим квеста / faction-ключ `gt_guard`. Соседний класс к уже известному WTF `communitytracking_shot`.
- карточка: [2026-09-19_newxray_nikit.md](../logs/cards/2026-09-19_newxray_nikit.md)
- pitfalls: [§18](pitfalls.md)
- подробности: нет

## [issue] `[DLTX] Duplicate section 'af_indeikam_breeding_1'` (`mod_system_anthology_indeikam_breeding_fix.ltx`)

- дата: 2026-09-19
- мод: старый ZIP / Kristiano AIO (`mod_system_anthology_indeikam_breeding_fix.ltx`), не наш `mod_system_fix_indeikam_breeding.ltx`
- итог: **конфликт установки** — FATAL на старте `CInifile::StashCurrentSection`; секция уже есть (или создана другим патчем), дубликат без `!`/`@`. Наш `fix_indeikam_breeding` **1.1.0** именует файл иначе и использует `@[…]`. В MO2 выключить старый ZIP / копию в Kristiano AIO.
- карточка: [2026-09-19_xray_mg9000.md](../logs/cards/2026-09-19_xray_mg9000.md) (источник `xray_mg9000 (2).log`; класс xraylog: **конфиг: DLTX**)
- pitfalls: нет
- подробности: `addon/fix_indeikam_breeding/CHANGELOG.md` [1.1.0] (явный конфликт имён файлов)

## [issue] `actor_status.script:32: table index is nil` (`scan_boosters_effect` / `BoosterForEach`)

- дата: 2026-09-19
- мод: ваниль `actor_status` — `active_boosters[ boost_name[typ] ]`; `boost_name[typ]` nil (неизвестный `typ` из `BoosterForEach`, таблица из `invert_table(BoosterID)`)
- итог: **не разобрано** — FATAL `lua_pcall_failed` на `actor_on_update` сразу после загрузки сейва. Какой booster/мод отдаёт неизвестный `typ` — не зафиксирован; нужен повтор с инвентарём бустеров / модами на `BoosterID`.
- карточка: [2026-09-19_xray_mg9000-2.md](../logs/cards/2026-09-19_xray_mg9000-2.md) (источник `xray_mg9000 (3).log`)
- pitfalls: нет
- подробности: `reference/anomaly/scripts/actor_status.script:24–32` (`prepare_boosters_effect` / `scan_current_booster_effect`)

## [issue] native `UnhandledFilter` / `rp_ScreenResolutionChanged` (без блока FATAL)

- дата: 2026-09-19
- мод: нативный (не Lua); падение после успешного save `tempsave`
- итог: **не разобрано** — класс **`нативный вылет (не Lua)`** (`UnhandledFilter` → `rp_ScreenResolutionChanged` → `FrameMove`). Отдельно от PDA `CUIMapWnd::DrawHint`.
- карточка: [2026-09-19_xray_mg9000-3.md](../logs/cards/2026-09-19_xray_mg9000-3.md) (источник `xray_mg9000.log`; `(1).log` — байтовый дубль)
- pitfalls: нет
- подробности: нет

## [issue] native `UnhandledFilter` / `CDialogHolder::DoRenderDialogs` (меню после load)

- дата: 2026-09-19
- мод: нативный UI; падение после успешной загрузки `quicksave_5`
- итог: **не разобрано** — класс **`нативный вылет (не Lua)`**; стек `DoRenderDialogs` → `CMainMenu::OnRenderPPUI_main`. Соседний класс к PDA-хинту, но другой кадр.
- карточка: [2026-09-19_xray_mg9000-4.md](../logs/cards/2026-09-19_xray_mg9000-4.md) (источник `xray_mg9000 (4).log`, ~14 сессий в одном файле)
- pitfalls: нет
- подробности: нет

## [issue] guard NOT installed: `se_*on_unregister` / `QAmmoWheelOption.LoadInActiveWeapon` / `InteractPrompt.on_option_change` / `aim_stamina.*`

- дата: 2026-09-19; повтор 2026-09-20 (nikit)
- мод: `fix_nil_crash_guards` 1.1.1, `fix_qaw_ammo_nil` 1.0.3, `fix_dotmarks_interact_prompt` 1.0.0, `fix_aim_fatigue_visibility` 1.0.2; рядом `fix_utjan_mag_skill` — `magazines module missing` (MAG Redux нет → wrappers NOT installed)
- итог: **цель API не найдена** — гарды пишут `… not found - guard NOT installed` (остальные wrap'ы nil-guards встают). Не «install() упал молча»: цель отсутствует или имя/путь другое в пакете. На 20.09 у nikit тот же набор + `aim_stamina.on_option_change`/`load_state`. Следующий шаг — сверить символы через `refindex` / наличие QAW, DotMarks InteractPrompt, Aim Stamina.
- карточка: [2026-09-19_xray_mg9000-3.md](../logs/cards/2026-09-19_xray_mg9000-3.md), [2026-09-19_xray_mg9000-4.md](../logs/cards/2026-09-19_xray_mg9000-4.md), [2026-09-20_xray_nikit.md](../logs/cards/2026-09-20_xray_nikit.md)
- pitfalls: [§9](pitfalls.md) (порядок `.script`); см. также issue про fallback `actor_on_first_update`
- подробности: нет

## [issue] mg9000 2026-09-19: 0 нефатальных Lua-групп (динамика vs baseline)

- дата: 2026-09-19
- мод: пакет mg9000 после nil-guards
- итог: **динамика** — `nonfatal_groups=0` (было 2 в baseline 2026-09-13: `game_backpack_travel` / `game_fast_travel`). Вылеты теперь нативные / DLTX / `actor_status`, не те traceback'и. Baseline 13.09 не отменяем; эта точка — после сдвига.
- карточка: [2026-09-19_xray_mg9000-3.md](../logs/cards/2026-09-19_xray_mg9000-3.md), [2026-09-19_xray_mg9000-4.md](../logs/cards/2026-09-19_xray_mg9000-4.md); baseline 13.09: `## [issue] mg9000 после nil-guards: 2 нефатальные группы`
- pitfalls: нет
- подробности: нет

## [issue] `CUILine::Draw` / `CUIMapWnd::DrawHint` (native ACCESS_VIOLATION, PDA map hint)

- дата: 2026-09-19
- мод: не скриптовый; подозреваемые споты — Milspec PDA / PAW / placeable waypoints / DotMarks (тип спота не зафиксирован)
- итог: **не чинится** без повтора — нет Lua FATAL; AV при отрисовке хинта карты PDA. Lua-кадр `haru_specialized_storage_boxes` в момент падения — смежный снимок VM, не причина. Нужен повтор с типом спота под курсором.
- карточка: нет; mdmp на месте: `logs/xray_nikit_09-19-26_14-16-50.mdmp`
- pitfalls: нет
- подробности: mdmp `logs/xray_nikit_09-19-26_14-16-50.mdmp`

## [issue] `fix_sim_mechanic_trade.script:65: attempt to call upvalue 'orig_trade_init' (a nil value)`

- дата: 2026-09-19
- мод: `fix_sim_mechanic_trade` (обёртка `trade_init` сорвалась — `orig_trade_init` nil)
- итог: **починено в 1.0.3** — re-wrap больше не обнуляет `orig_*`; лог korisnik был до/без этого пакета. Если у тестера снова всплывёт — смотреть, стоит ли 1.0.3.
- карточка: нет (дамп korisnik 2026-09-19 снят вместе с сырым логом)
- pitfalls: нет
- подробности: `addon/fix_sim_mechanic_trade/CHANGELOG.md` [1.0.3]

## [issue] `fix_milspec_exo_craft.script:198` / `kristiano_kx1_exo.script:358` — `LUA error: DebuggerMode` (рекурсия `orig_load`)

- дата: 2026-09-19
- мод: `fix_milspec_exo_craft` + Kristiano KX1 exo (взаимная обёртка `orig_load`)
- итог: **не разобрано** — FATAL `DebuggerMode`, в логе сотни тысяч кадров рекурсии; один и тот же краш у mg900011 и teres
- карточка: нет (дамп mg900011 2026-09-19 снят вместе с сырым логом)
- pitfalls: нет
- подробности: нет

## [issue] `CUIXmlInit::InitFont` / `unknown font` `letterica14`

- дата: 2026-09-15
- мод: UI/шрифты (не наш `fix_*` напрямую); контекст PDA OVCD
- итог: **не разобрано** — нативный FATAL unknown font
- карточка: нет (дамп pda_ovcd 2026-09-19 снят вместе с сырым логом)
- pitfalls: нет
- подробности: нет

## [issue] `pda_inter_x_banter.script:170: attempt to index field 'GUI' (a nil value)`

- дата: 2026-09-13
- мод: `fix_pda_buyinfo_gui` **1.1.0** (раньше только buyinfo/trade)
- итог: починено — обёртка `send_sos` / `ask_surge` / `ask_psi_storm` / `ask_status` + CTE-колбэки через `PDA_GUI` / noop
- карточка: нет (Discord-скрин hicross)
- pitfalls: нет
- подробности: `addon/fix_pda_buyinfo_gui/CHANGELOG.md` [1.1.0]

## [issue] Discord nil-FATAL пакет (crow / Semenov / unregister_npc / clear_dead / intercept / cover_tilt / spawn_fast / vid_mode)

- дата: 2026-09-13
- мод: `fix_nil_crash_guards` **1.1.0** (с 1.0.0 — пакет гардов; тумблеры `GUARD_*` в шапке)
- итог: починено гардами (см. CHANGELOG мода); не покрывает patrol vertex, Not enough IDs, missing anm/xml, armor_ripper без HF; **подтверждение только у авторов Discord-скринов** — в наших cards сигнатур нет
- карточка: нет (пачка Discord-скринов авг 2026)
- pitfalls: нет
- подробности: `addon/fix_nil_crash_guards/CHANGELOG.md` [1.1.0]

## [issue] mg9000 после nil-guards: 2 нефатальные группы (baseline)

- дата: 2026-09-13
- мод: пакет у тестера mg9000 после `fix_nil_crash_guards` / соседних фиксов
- итог: **точка отсчёта** — в fresh-логе класс «вылета нет, 2 группы» против **8** групп в `…_mg9000.log.md` и **Lua error (pcall)** в `…_mg9000-1.log.md` той же даты. Оставшиеся две: (1) `game_backpack_travel.script` x3, триггер `!ALIFE OBJECT ID IS 65535!`; (2) `game_fast_travel.script` x3, триггер без строки `!`/`~` перед блоком. Следующий лог от mg9000 сверять с этим списком — сдвинулось или нет.
- карточка: [2026-09-13_xray_mg9000_fresh.md](../logs/cards/2026-09-13_xray_mg9000_fresh.md); было: [2026-09-13_xray_mg9000.log.md](../logs/cards/2026-09-13_xray_mg9000.log.md), [2026-09-13_xray_mg9000-1.log.md](../logs/cards/2026-09-13_xray_mg9000-1.log.md)
- pitfalls: нет
- подробности: нет

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
