# RVR ActiveStorages Nil Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; в MO2 после [GAM] Optimized Storage System. Имя скрипта без zzz-префикса: wrap ставится в on_game_start / actor_on_first_update.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без guard снова возможен CTD при открытии anomalous stash / inventory с obj, если ActiveStorages не инициализирован.

## [1.0.0] - 2026-09-20

**Изменено**

- gamedata/scripts/fix_rvr_active_storages_nil.script - outer monkey-patch ui_inventory.start: перед вызовом цепочки (включая патч RVR) гарантирует rvr_storage_system_engine.ActiveStorages как таблицу и при необходимости вызывает InitDefaultStorages / InitActiveStorages через pcall. Повторный heal на actor_on_first_update; re-wrap если цепочка сменилась.

**Причина**

rvr_storage_system_engine.script:1835 делает ActiveStorages[obj:id()] без nil-check. Таблица создаётся только в InitActiveStorages() из actor_on_first_update -> init(). После загрузки сейва init может не оставить таблицу (в логе xray_mg9000 (1)4.log нет initialized ActiveStorage, при этом патч жив). Открытие hidden_anom_stash через Dotmarks -> FATAL attempt to index global ActiveStorages (a nil value).

**Не затронуто**

- Оригинал rvr_storage_system_engine.script
- Логика anomalous stash / Dotmarks / sorting tabs
- Сейвы (save_state / load_state RVR не трогаем)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Без установленного Optimized Storage System guard пишет not found и не ставится

**Проверено**

- lint: python tools/lint_addon.py fix_rvr_active_storages_nil
- в игре: не прогонялось. Ожидание: открытие anomalous stash без FATAL; в логе при heal - healed ActiveStorages reason=...
