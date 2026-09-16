# AOL Sprint HUD Motion Guard

## [1.0.1] - 2026-09-16

**Изменено**

- `gamedata/scripts/fix_aol_sprint_hud.script` — `safe_stop_hud_motion` вызывает сохранённый `orig_stop`, а не `game.stop_hud_motion` (этот слот во время handler — наша обёртка).

**Причина**

v1.0.0 при `hud_motion_allowed() == false` (перезарядка / FDDA / script anim) рекурсил: else-ветка звала уже подменённый `game.stop_hud_motion`. `pcall` глотал ошибку, руки не стопались.

**Не затронуто**

- Условие skip (`allowed() == true`)
- Оригинал `aol_sprint_cancel.script`, прямые `stop_hud_motion` вне этого callback

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_aol_sprint_hud`
- в игре: не подтверждено. Ожидание: нет `script_anim_part 255` на idle sprint; FDDA/reload + спринт стопает руки без `movement handler error`.

## [1.0.0] - 2026-09-16

**Изменено**

- `gamedata/scripts/fix_aol_sprint_hud.script` — monkey-patch `aol_sprint_cancel.actor_on_movement_changed`: `game.stop_hud_motion` вызывается только если `not game.hud_motion_allowed()` (есть активный HUD motion). Иначе skip + редкий лог.

**Причина**

R.A.K `aol_sprint_cancel.script:38/41` зовёт `stop_hud_motion` при обрыве walk↔sprint. Без активной script-анимации движок пишет `player_hud::StopScriptAnim() invalid script_anim_part 255` (×18 за сессию, не CTD).

**Не затронуто**

- Оригинал `aol_sprint_cancel.script`, `aol_anim_transitions`
- FDDA / ledge grabbing и прочие прямые вызовы `stop_hud_motion` вне этого callback

**Совместимость**

- Нужен R.A.K Base с `aol_sprint_cancel`
- Сейвы: без изменений
- MO2: ниже R.A.K Base / внутри Kristiano AIO

**Проверено**

- lint: `python tools/lint_addon.py fix_aol_sprint_hud`
- в игре: не подтверждено. Ожидание: нет спама `script_anim_part 255` от `aol_sprint_cancel`; при skip — `[fix_aol_sprint_hud] skip stop_hud_motion`.
