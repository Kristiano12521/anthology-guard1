# Log Spam Diagnostic

## [1.2.0] — 2026-09-01

**Изменено**

- `_diag_log_spam_printe.script`: ранний хук `printe` сразу после `_g.script` — ловит `item_combination` при инициализации `itms_manager` (до `aaa_diag_log_spam`).
- Общее состояние трассировки в `_G.__diag_log_spam` (early + main wrappers).

**Проверено**

- lint: см. прогон после правки

## [1.1.0] — 2026-09-01

**Изменено**

- `on_game_end`: сводка через `function on_game_end()`, без `RegisterScriptCallback` (убраны ложные STACK TRACEBACK при загрузке).
- Обёртка `printe`: первый hit по паттернам `item_combination`, `wrong section names`, `callback doesn't exist`, `no game object`, `no server object` — TRACE + callstack.
- MCM: `trace_printe_patterns` (eng/rus).

**Проверено**

- lint: 0 ошибок

## [1.0.0] — 2026-09-01

**Добавлено**

- `aaa_diag_log_spam.script` — обёртки `get_object_by_id`, `alife_release`, `alife_release_id`.
- Первый промах `get_object_by_id` на каждый id: `callstack` в лог (`[diag_log_spam] TRACE`).
- Повторные промахи: без `!ERROR get_object_by_id` (MCM `suppress_get_object_by_id_noise`, по умолчанию вкл).
- `alife_release` без server object: один стек + тихий выход (MCM `fix_alife_release_nil`).
- Сводка по id при `on_game_end`.
- MCM: `diag_log_spam_mcm.script`, строки eng/rus.

**Причина**

В сессии 01.09.2026 после BHS 0.6.8: 382× `get_object_by_id (2119)` и 1× `alife_release | no server object` из цепочки `item_weapon.ammo_aggregation` / `zz_cop_phys_story_id_fix`.

**Как использовать**

1. Поставить мод, загрузить сейв.
2. В xraylog найти `[diag_log_spam] TRACE get_object_by_id` — там стек виновника.
3. **Найдено 01.09.2026:** `igi_actions.is_low_condition(2119)` из WTF `quest_status` — фикс в `fix_wtf_taskboard_guard` v1.0.2.
4. После точечного фикса `diag_log_spam` можно снять или оставить как гард на `alife_release`.

**Не затронуто**

- Игровая логика торговли, агрегации патронов, story_id.
- `verified_*` не ставились.

**Проверено**

- lint: см. прогон после правки
- В игре: не прогонялось
