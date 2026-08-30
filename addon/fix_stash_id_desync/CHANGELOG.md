# Stash ID Desync Fix

## [1.0.2] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_stash_id_desync.script` — `server_entity_on_unregister` сначала смотрит `typ == "se_invbox"` и выходит. `pcall(db.actor:id())` убран.

**Причина**

Хук висит на всех unregister (предметы, НПС, актор). `actor_present()` звал `db.actor:id()` до фильтра ящика. В X-Ray `pcall` не глушит `cannot access class member CScriptGameObject::ID!` / `destroyed object [0]` — полный traceback на каждый вызов. В логе mg9000 это ~24700 ошибок и десятки МБ. Пока `:id()` падал, хук ещё и не чистил реальные ящики.

**Как исправлено**

Не-ящики отсекаются по строке `typ` без методов `CScriptGameObject`. Живая сессия по-прежнему `session_live` + `db.actor ~= nil`, без `:id()`.

**Не затронуто**

- обёртка `release_stash_by_id`, отложенный repair, `get_random_stash`
- флаги `actor_on_first_update` / `actor_on_net_destroy` / `on_game_load`

**Совместимость**

- Сейвы: без миграции
- В MO2 как раньше

**Проверено**

- lint: `python tools/lint_addon.py fix_stash_id_desync`
- В игре: не прогонялось. В логе не должно быть `fix_stash_id_desync.script` / `actor_present` на unregister предметов

## [1.0.1] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_stash_id_desync.script` — `server_entity_on_unregister` больше не зовёт `release_stash_by_id` после `actor_on_net_destroy` / без `db.actor` (teardown на Disconnect).

**Причина**

На выходе из игры alife снимает все `se_invbox`. Хук принимал это за уничтожение ящика и чистил `treasure_manager.caches` (~1500 записей `mar_treasure_*` и дальше). При «сохранить и выйти» пул тайников можно убить.

**Как исправлено**

Флаг живой сессии: `true` с `actor_on_first_update`, `false` с `actor_on_net_destroy` / `on_game_load` / `on_game_end`. Уничтожение ящика в игре по-прежнему идёт в `release_stash_by_id`.

**Не затронуто**

- обёртка `release_stash_by_id`, отложенный repair после загрузки
- `get_random_stash`, Tosox, `fix_quest_stash`, `all.spawn`

**Совместимость**

- Сейвы: без миграции. Если уже сохранялись после сессии 1.0.0 с wipe на выходе — пул мог похудеть; тогда нужен более ранний сейв
- В MO2 как раньше

**Проверено**

- lint: `python tools/lint_addon.py fix_stash_id_desync`
- В игре: не прогонялось. На выходе не должно быть пачки `cleared id=... reason=unregister`

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_stash_id_desync.script` — обёртка `treasure_manager.release_stash_by_id` снимает `treasure` / `treasure_searched` / `treasure_unique` и отдаёт в оригинал даже `caches[id] == false` (иначе локальный `caches_count` не уменьшается). `server_entity_on_unregister` для `se_invbox` делает то же. После загрузки: вычищает десинхронные ключи `caches` через штатный release, затем чанками 1–65534 снимает висящие споты с id, который уже не ящик.

**Причина**

Метка PDA привязана к alife id. `release_stash_by_id` и ветка «нет объекта» в `get_random_stash` выкидывают кэш и оставляют спот. id забирает другой объект (часто ворона). `actor_on_item_take_from_box` для чужого объекта не срабатывает — метка ходит и зависает.

ZIP v3 обходил все `caches` анонимным callback, писал сырой `tbl[id] = nil` без `caches_count`, не видел спот если кэш уже пуст, и не закрывал дыру на следующем релизе ящика.

**Как исправлено**

Спот снимается в том же месте, где ящик уходит из пула или из alife. Старые сейвы чинятся одним отложенным проходом. Селектор `get_random_stash` не трогается (его уже держит Tosox).

**Не затронуто**

- `treasure_manager.script` целиком, `get_random_stash`, Tosox `treasure_manager_monkey_map_links.script`
- `fix_quest_stash`, `fix_nta_stashes`
- `item_backpack`, радио, файлы Grok Stash Overhaul
- валидные ящики и рюкзаки-invbox со спотом `treasure`
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без новой игры и без новых полей. Из сейва уходят только осиротевшие споты и мёртвые ключи `caches` через `release_stash_by_id`
- В MO2 ниже сборки, Tosox Mini Mods и Grok Stash Overhaul. ZIP `Stash_ID_Desync_Fix` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_stash_id_desync`
- В игре: не прогонялось. Ожидаемый лог: `release_stash_by_id wrapped`, при десинке `cleared id=... reason=not_invbox`, в конце `repair done spots=N cache_entries=M`
