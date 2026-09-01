# Minigun Dead Parent Guard

## [1.0.0] — 2026-09-01

**Изменено**

- `gamedata/scripts/zzz_fix_minigun_dead_parent.script` — monkey-patch `bullet_on_init`, `npc_on_update`, `monster_on_update` в модуле `weapon_minigun_npc_fire_bullet_driven_V3_lite`.

**Причина**

Мод R.A.K Weapon Pack Adaptation вызывает `parent_obj:alive()` без `pcall` на destroyed userdata в `register_npc_minigun_bullet` (стр. 615) и `maintain_parent_audio` (стр. 660). В логе ~80 сообщений `cannot access class member Alive!` за сессию, CTD нет.

**Как исправлено**

Обёртки отсеивают мёртвый parent до вызова оригинала (`pcall(function() return obj:alive() end)`). Для `bullet_on_init` parent берётся из `bullet.parent_id` через `level.object_by_id`, как в оригинале. Порядок загрузки — префикс `zzz_` (файл грузится после модуля миниганов, патч на top-level до `on_game_start`). Счётчик отсевов печатается раз в 10, не на каждый вызов.

**Не затронуто**

- оригинальный `weapon_minigun_npc_fire_bullet_driven_V3_lite.script`
- звук, спавн пуль, логика стрельбы миниганов
- `game_object_on_net_destroy`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 ниже R.A.K Weapon Pack Adaptation

**Проверено**

- lint: `python tools/lint_addon.py fix_minigun_dead_parent`
- lint cross: `python tools/lint_addon.py --cross`
- build: `python tools/build_addon.py fix_minigun_dead_parent --zip`
- В игре: не прогонялось. Ожидаемый результат: ноль `cannot access class member Alive!` от миниганов; NPC-миниганы стреляют и звучат как раньше.
