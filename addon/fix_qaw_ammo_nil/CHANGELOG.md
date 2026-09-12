# QAW Ammo Active Item Nil Guard

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
