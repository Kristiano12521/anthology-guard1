# WTF Assault instacomplete

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; `printf` с причиной при раннем выходе из `install()`.

**Не затронуто**

- Обёртки Assault.on_init / status.

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_wtf_assault_instacomplete.script` — monkey-patch `igi_target_assault.Assault.on_init` и `Assault.status`.

**Причина**

Квест «Приказ! Зов Долга» (`orders_duty.json`) выдаётся по `has_dogs`: у смарта есть любой назначенный отряд. Контроллер `Assault` при старте собирает цели через `add_target_squads` → `is_squad_at_smart`, где без `get_script_target` нужен `current_action == 1` (отряд уже занял смарт). После загрузки Бара стая часто ещё в пути: `entity.squads` пустой, `is_completed()` считает пустой список зачисткой, первый `status()` ставит COMPLETED и выдаёт награду.

Тот же пустой снапшот возможен у других Assault-квестов (GhenTuong supply/mutant/transaction), если отряды создаются после `Assault.on_init` в той же группе сущностей.

Сырой ZIP `Fix instacomplete Duty assault` ждал один тик `status()` и копировал в цели всех с `smart.squads` без фильтра враг/легит, не пересобирал список, если на `on_init` смарт ещё пуст, крутил `CreateTimeEvent` до 50 раз и не снимал патч.

**Как исправлено**

Callback не подходит: `on_init` / `status` вызываются из WTF напрямую. Monkey-patch:

- Сбор целей = отряды из `SIMBOARD.smarts[id].squads` (как `has_dogs`) + исходные фильтры «враг актёра» и не крыса/тушкан. `current_action == 1` не требуется.
- `on_init`: после оригинала в снапшот дописываются назначенные вражеские отряды, которых строгий сбор пропустил.
- `status`: тот же сбор только пока снапшот пуст — ловит отряды, появившиеся после `on_init`. Новые назначения симуляции после непустого снапшота не подмешиваются.
- Установка в `on_game_start`, повтор в `actor_on_first_update` (MT load). Оригинал возвращается в `on_game_end`.

**Не затронуто**

- файлы WTF (`igi_target_assault.script`, `orders_duty.json` и остальные шаблоны)
- награды, тексты, выдачу квеста, `has_dogs`
- квесты без контроллера Assault
- уже непустой строгий снапшот — только дополняется назначенными врагами
- `all.spawn`, сейвы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет. Уже мгновенно закрытый квест в старом сейве не откатывается
- Зависимость: Weird Tasks Framework (`[QUE] wtf 4_2`). Без него — no-op
- В MO2 ниже WTF
- ZIP `[QUE] wtf 4_2 - Fix instacomplete Duty assault` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_wtf_assault_instacomplete`
- В игре: не прогонялось. Ожидаемый лог при срабатывании: `recovered N squads for smart <id> (on_init|status)`. Квест «Зов Долга» остаётся RUNNING, пока назначенная стая жива
