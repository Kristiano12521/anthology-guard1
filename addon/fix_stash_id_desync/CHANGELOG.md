# Stash ID Desync Fix

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
