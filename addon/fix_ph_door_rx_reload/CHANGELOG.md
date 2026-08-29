# PH Door Stale Registry and RX Offline Planner Guard

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_ph_door_rx_reload.script` — обёртки `ph_door.try_to_open_door` / `try_to_close_door` и `rx_ai.enable_schemes`; callback `game_object_on_net_destroy` чистит `db.level_doors`.

**Причина**

Два FATAL на ветке «против Пророка», оба — ванильные nil-гонки, не конфиг Атрибута.

1. `ph_door.script:342` — `db.level_doors[id]` пишется в `add_to_binder` и никогда не снимается. `db.del_obj` (`bind_physic_object:98`, `xr_motivator:362`) обнуляет `db.storage[id]`. Сталкер в 3 м от кэшированной позиции мёртвой двери делает `db.storage[id].ph_door`. Та же дыра в `try_to_close_door:356` по списку `opened_doors`.

2. `rx_reload.script:209` — `rx_ai.enable_schemes` зовётся только для `stype_stalker`, дальше `rx_reload` / `rx_facer` / `rx_bandage` / `rx_knife` делают `manager:add_evaluator` без проверки. У объекта из оффлайн-респавна отряда планировщика нет. ZIP глушил только `rx_reload.add_to_binder` — следующий `rx_*` падает так же.

ZIP `[FIX] MTR Attribute Hotfix (slim)` переписывал тела `try_to_open/close` целиком (`_G.__ph_door_patched`, без `on_game_end`) и тащил полную копию `dynamic_objects.ltx` (в slim убрана).

**Как исправлено**

Callback и monkey-patch, оригиналы не подменяются.

- Двери: `game_object_on_net_destroy` снимает запись из `db.level_doors`. Перед оригиналом `try_to_open_door` вычищает уже протухшие id; перед `try_to_close_door` — протухшие id в `opened_doors`. Тела функций сборки не копируются.
- RX: один гард на `rx_ai.enable_schemes` — нет `motivation_action_manager()` → схемы не биндятся. Закрывает все `rx_*` в этой цепочке, не только reload.

`dynamic_objects.ltx` и секции `mtr_e80_bomba_obj_*` сюда не входят: это конфликт полной копии файла у Campfires, лечится `[FIX] Campfires Anthology Compat`.

**Не затронуто**

- `ph_door.script`, `rx_reload.script`, `rx_ai.script`, `rx_bandage.script`
- логика открытия/закрытия живых дверей, `register_door_for_npc`
- схемы reload / bandage / knife / facer у сталкера с планировщиком
- `dynamic_objects.ltx`, квесты Атрибута, `all.spawn`
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- В MO2 ниже сборки. ZIP `[FIX] MTR Attribute Hotfix (slim)` выключить: он подменяет те же функции целиком
- Не конфликтует с `fix_rx_bandage_dead` (тот патчит методы класса, не `enable_schemes`)

**Проверено**

- lint: `python tools/lint_addon.py fix_ph_door_rx_reload`
- В игре: не прогонялось. Ожидаемый лог: `wrapped ph_door.try_to_open/close`, `wrapped rx_ai.enable_schemes`. Штурм Пророка рядом со «старой» дверью — без FATAL на `ph_door.script:342`. Оффлайн-респавн отряда — без FATAL на `rx_reload.script:209`. При пропуске объекта без планировщика: `skip rx schemes, no action planner (...)`.
