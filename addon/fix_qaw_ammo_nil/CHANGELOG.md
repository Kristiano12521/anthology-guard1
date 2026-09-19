# QAW Ammo Active Item Nil Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 после Quick Action Wheel; скрипт `zzz_*` + `-- load-order: после haru_quick_action_wheel_mcm` после …` в Windows-1251 (редактор без кириллицы; линтер ENC-005).

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.3] — 2026-09-19

**Изменено**

- Monkey-patch re-wrap: больше не обнуляет `orig_*` перед `install()` на `actor_on_first_update`.
- `wraps_ok` требует живой `orig`; вызовы оригинала под nil-guard.
- Снова восстановлено `-- load-order: после …` в Windows-1251 (редактор без кириллицы; линтер ENC-005).

**Причина**

Обнуление всех `orig` при частичном сбое wrap оставляло уже наш патч с `orig == nil` → CTD (как `fix_sim_mechanic_trade` / xray_korisnik).

**Не затронуто**

- Игровая логика патча, сейвы, DLTX

**Проверено**

- lint: `python tools/lint_addon.py fix_qaw_ammo_nil`
- в игре: не прогонялось

## [1.0.2] — 2026-09-17

**Изменено**

- `zzz_fix_qaw_ammo_nil.script` — `wraps_ok` по `QAmmoWheelOption.LoadInActiveWeapon`; retry на `actor_on_first_update` после MT reload; `callbacks_registered`.

**Причина**

1.0.1 при `installed=true` не сверял классы. После reload QAW снова FATAL :1426.

**Не затронуто**

- Отсев `active_item() == nil`; `CanLoadInActiveWeapon`

**Проверено**

- lint: `python tools/lint_addon.py fix_qaw_ammo_nil`
- в игре: не прогонялось

## [1.0.1] — 2026-09-16

**Изменено**

- `gamedata/scripts/zzz_fix_qaw_ammo_nil.script` — в `printf` `batch_total` формат `%d` заменён на `%s` + `tostring`.

**Причина**

`printf` этой сборки подставляет `%s`, не `%d`. При skip лог мог обрезаться, как у travel 1.0.1.

**Не затронуто**

- Отсев `active_item() == nil` в `LoadInActiveWeapon` ammo/mag
- `CanLoadInActiveWeapon` (Update)

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_qaw_ammo_nil`
- в игре: не подтверждено. Ожидание: skip пишет `batch_total=<число>`.

## [1.0.0] — 2026-09-12

**Изменено**

- `gamedata/scripts/zzz_fix_qaw_ammo_nil.script` — monkey-patch `QAmmoWheelOption.LoadInActiveWeapon` и `QMagazineWheelOption.LoadInActiveWeapon`: отсев `active_item() == nil` до вызова оригинала; троттлинг лога отсевов.

**Причина**

Колесо патронов (`QAmmoWheelOption:OnClick`) закрывает GUI и через `CreateTimeEvent(..., 0.1, ...)` вызывает `LoadInActiveWeapon`. Оригинал берёт `db.actor:active_item()` и сразу делает `wpn:unload_magazine(true)` без nil-check. Если за 0.1 с активный предмет пропал (слот/холостер/анимация навески) — FATAL:
`haru_quick_action_wheel_mcm.script:1426 attempt to index local 'wpn' (a nil value)`.
Тот же паттерн у магазинного варианта колеса.

**Как исправлено**

Классы живут в `_G` (как `UIInventory` у BusyHands). Обёртка проверяет `db.actor` и `active_item()`; при nil — лог и return, иначе оригинал. Логика смены патронов/магазина не меняется.

**Не затронуто**

- оригинал `haru_quick_action_wheel_mcm.script`
- `AttachmentWheelOption` / глушак / прицелы (там nil-check уже есть)
- MCM QAW, сейвы, вкладки колеса

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 после Quick Action Wheel; скрипт `zzz_*` + `-- load-order: после haru_quick_action_wheel_mcm`

**Проверено**

- lint: `python tools/lint_addon.py fix_qaw_ammo_nil`
- lint cross: `python tools/lint_addon.py --cross`
- В игре: не прогонялось. Критерий: смена типа патронов с колеса при активном оружии работает; при сбое active item — без FATAL, в логе presence + троттлированный `skip ... no active item`.
