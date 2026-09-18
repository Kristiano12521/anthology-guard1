# FDDA Matches Campfire Softlock Guard

## [1.0.1] — 2026-09-19

**Изменено**

- Monkey-patch re-wrap: больше не обнуляет `orig_*` перед `install()` на `actor_on_first_update`.
- `wraps_ok` требует живой `orig`; вызовы оригинала под nil-guard.

**Причина**

Обнуление всех `orig` при частичном сбое wrap оставляло уже наш патч с `orig == nil` → CTD (как `fix_sim_mechanic_trade` / xray_korisnik).

**Не затронуто**

- Игровая логика патча, сейвы, DLTX

**Проверено**

- lint: `python tools/lint_addon.py fix_matches_campfire_softlock`
- в игре: не прогонялось

## [1.0.0] - 2026-09-19

**Изменено**

- `gamedata/scripts/fix_matches_campfire_softlock.script` — monkey-patch `zzz_matches_anim.ignit` и `actor_on_hud_animation_end`: nil-check binder до `disable_input`, watchdog 8 с с `force_unlock` (stop tutorial, remove cam 9665, restore FOV/slot/detector, `enable_input` без `campfire_go_on`).

**Причина**

FDDA `zzz_matches_anim.ignit` глушит ввод и ждёт только cam-effector callback. Если `level.add_call` не дожидается слота 0 / снятия детектора или callback не срабатывает — soft-lock. Лог `xray_nikit`: `tutorial-xml` ×3 → выход в меню.

**Не затронуто**

- Оригинал `zzz_matches_anim.script`, WG lighter path, `bind_campfire`, placeable campfires
- Успешное разжигание (watchdog снимается в `actor_on_hud_animation_end`)

**Совместимость**

- Нужен FDDA Redone с `zzz_matches_anim`
- Сейвы: без изменений
- MO2: после `[TMA] FDDA Redone`

**Проверено**

- lint: `python tools/lint_addon.py fix_matches_campfire_softlock`
- в игре: не подтверждено. Ожидание: presence + `guard installed`; при зависании через ~8 с — `force_unlock reason=timeout` и управление возвращается.
