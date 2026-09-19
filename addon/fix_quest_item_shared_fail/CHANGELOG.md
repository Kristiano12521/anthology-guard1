# Tosox vanish-fail на общем DRX stash-слоте

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 заменить Kristiano целиком После MT reload Tosox vanish-fail соседа снова проходил без rearm.

**Удаление**

- Отключить слот в MO2; новая игра не нужна. Активный shared DRX stash-квест лучше завершить или дождаться fail-логики с модом.
- Может писать task var через save_var (корректный fail). Сейв не ломается; без фикса vanish-fail на общем слоте вернётся.

## [1.3.2] — 2026-09-17

**Изменено**

- `fix_quest_item_shared_fail.script` — не перезахватывает `orig_status`, если обёртка уже ставилась (другой мод сверху); re-assert только при `current == orig`. Guard `status_busy` против рекурсии status-цепочки с `fix_quest_stash`.

**Причина**

1.3.1 always re-capture + `orig_status = nil` на `actor_on_first_update`/`late install` создавали цикл SF ↔ QS на общем `drx_sl_quest_item_task_status` → Lua stack overflow / CTD при load.

**Не затронуто**

- Логика rearm / vanish-fail

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_item_shared_fail`
- в игре: не прогонялось (ожидание: load без stack overflow)

## [1.3.1] — 2026-09-17

**Изменено**

- `fix_quest_item_shared_fail.script` — убран early-return по `orig_status`; `wraps_ok` / always re-capture; на `actor_on_first_update` переустанавливает wrap, если functor уже не наш.

**Причина**

1.3.0 при записанном `orig_status` не сверял указатель. После MT reload Tosox vanish-fail соседа снова проходил без rearm.

**Не затронуто**

- Rearm через `get_random_stash`, late install 0.5s

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_item_shared_fail`
- в игре: не прогонялось

## [1.3.0] — 2026-09-14

**Изменено**

- Откат к утренней простой схеме (как 1.0.0): только обёртка status — при Tosox `"fail"` из‑за мёртвого `item_id` делается `rearm` с **новым** тайником (`get_random_stash`), квест остаётся на `stage=0`.
- Убраны: ownership / demote / `watched_items` / `loot_claim` / обёртка target / DLTX слотов 1039–1040.

**Причина**

Игрок и тест: утренний фикс удобнее — один КПК, две метки сдачи ок; сдал одному → второй обновился с меткой на тайник, лут на месте. Поздние правки (пустая метка, нет метки второго схрона) хуже UX при той же пользе.

**Не затронуто**

- Tosox; `tasks_stash`; `fix_quest_stash`.

**Совместимость**

- Сейвы: без миграции. Если успели прогнать 1.2.x с типами 1039/1040 — `fix_quest_stash` может оставить уже мигрированный `stash_type`; на поведение vanish→rearm не влияет.
- В MO2 заменить Kristiano целиком.

**Проверено**

- lint/pack: см. прогон
- В игре: не прогонялось (ожидание как у утреннего фикса).

## [1.2.1] — 2026-09-14

Отозвано в 1.3.0 (loot_claim + target=nil while watched).

## [1.2.0] — 2026-09-14

Отозвано в 1.3.0 (DLTX 1039/1040 + ownership).

## [1.1.0] — 2026-09-14

Отозвано в 1.3.0 (demote / claim).

## [1.0.1] — 2026-09-14

Отозвано в 1.3.0 (keep old target_id).

## [1.0.0] — 2026-09-13

**Изменено**

- Обёртка `task_status_functor.drx_sl_quest_item_task_status`: вместо Tosox `"fail"` при мёртвом `var.item_id` — rearm с новым `target_id` через `get_random_stash`.

**Причина**

Общие слоты 1/2/3: сдача одного заказа валила соседний через Tosox vanish-fail.
