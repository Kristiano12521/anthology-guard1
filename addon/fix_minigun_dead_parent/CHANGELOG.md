# Minigun Dead Parent Guard

## [1.1.0] — 2026-09-01

**Изменено**

- `gamedata/scripts/zzz_fix_minigun_dead_parent.script` — патч только `bullet_on_init`; отсев по `gameobjects_registry[parent_id]` / `[weapon_id]` без вызовов `:alive()`, `:id()`, `:clsid()`. Счётчик `dead_skip_count` без периодического `printf`; одна строка `session_total` в `on_game_end` при `count > 0`.
- `tools/_pack_kristiano_aio.py` — мод снова в составе AIO (убран из `SKIP`).

**Причина**

v1.0.0 вызывал `:alive()` под `pcall` в трёх callback'ах → 320 `cannot access class member Alive!` при 4200 отсевах. v1.0.1 отключён. Миниган читает `bullet.parent_id` как поле таблицы (`callbacks_gameobject.script:115`), не метод — проверка по числовому id безопасна. Онлайн-объекты — `gameobjects_registry` (`callbacks_gameobject.script:28-35`).

**Как исправлено**

Если `parent_id` (или `weapon_id`) нет в `gameobjects_registry`, оригинальный `register_npc_minigun_bullet` не вызывается — `level.object_by_id` + `:alive()` на протухшем userdata не доходят. `npc_on_update` / `monster_on_update` не трогаем (звук при мёртвом parent — баг оригинала R.A.K, не наш).

**Не затронуто**

- оригинальный `weapon_minigun_npc_fire_bullet_driven_V3_lite.script`
- `npc_on_update`, `monster_on_update`, `maintain_parent_audio`

**Совместимость**

- Сейвы: без миграции
- В MO2 ниже R.A.K Weapon Pack Adaptation

**Проверено**

- lint: `python tools/lint_addon.py fix_minigun_dead_parent`
- В игре: не прогонялось. Критерий: `cannot access class member Alive!` < 80 за сессию (было ~80 от оригинала). Если не ниже — фикс бесполезен, отключить и писать автору R.A.K.

## [1.0.1] — 2026-09-01

**Изменено**

- `gamedata/scripts/zzz_fix_minigun_dead_parent.script` — мод отключён (`WITHDRAWN`): `install()` только пишет причину и не патчит миниганы.
- `tools/_pack_kristiano_aio.py` — `fix_minigun_dead_parent` в `SKIP` (не попадает в новые сборки AIO).

**Причина**

v1.0.0 вызывал `obj:alive()` под `pcall` в `bullet_on_init`, `npc_on_update`, `monster_on_update`. `pcall` ловит исключение, но движок печатает `cannot access class member Alive!` и стек. Сессия 01.09.2026 22:32–23:00: было ~80 таких сообщений от оригинала, стало 320 при 4200 `dead_parent_skip`.

**Не затронуто**

- оригинальный `weapon_minigun_npc_fire_bullet_driven_V3_lite.script`

**Проверено**

- lint: `python tools/lint_addon.py fix_minigun_dead_parent`
- В игре: не прогонялось. Ожидаемый результат: строка `guard NOT installed v1.0.1`; патч не активен; спам от guard отсутствует.

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
