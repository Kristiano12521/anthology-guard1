# Fetch Remote Storage

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; MCM.
**Soft-deps:** [HF] Hideout Furniture, [GAM] The Anomalous Stash (без них опция просто ничего не делает).

## [1.0.0] — 2026-09-20

**Добавлено**

- Опция MCM (по умолчанию **выкл.**): засчитывать и снимать предметы из `workshop_stash` (Hideout Furniture) и `hidden_anom_stash` (The Anomalous Stash) для цикличных fetch / multifetch.
- Monkey-patch: `actor_has_fetch_item`, `fetch_reward_and_remove`, `remove_fetch_item`, `tasks_multifetch.has_items` / `has_optional_items` / `remove_items_and_pay`.
- TTL-кэш 1 с по online-ящикам; полный обход только при промахе и только если в инвентаре актора не хватает.
- Одна строка лога на сессию (`on_game_end`): `cache_misses`, `items_scanned_max`, `items_scanned_avg`, `boxes_online_max`, `boxes_skipped_offline_sum`.

**Риск (осознанное изменение правил)**

С включённой опцией задание можно сдать, **не имея предмета при себе**. Это не фикс бага Anomaly, а опциональный сдвиг правил.

**set_switch_online**

Не вызывается. У HF `GetStash` ставит `set_switch_online(true)` / `set_switch_offline(false)` без возврата; флаг сериализуется в alife. Offline-ящик в этом тике пропускается (статус и сдача). Снятие флага на `on_game_end` (как в fix_gigant 1.1.2) не требуется — мы CSE не трогаем.

**Не затронуто**

- Глобальный `utils_item.get_amount`
- Обычные `player_created_stashes`, чужие тайники
- `verified_*`

**Совместимость**

- Старый сейв: опция выкл., поведение ванили
- Снятие мода: патчи снимаются; своих таблиц в сейве нет
- Без HF / Anomalous Stash / без ключей в `m_data`: no-op

**Проверено**

- lint: `python tools/lint_addon.py fetch_remote_storage` (+ `--cross`)
- В игре: не прогонялось агентом. Включить опцию, положить fetch-предмет только в верстак / anom, убедиться что статус и сдача работают; в меню — строка `session cache_misses=… items_scanned_max=…`. Если `items_scanned_max` порядка 20–30, TTL можно упростить; если `cache_misses` сотни за короткую сессию — поднять TTL.
