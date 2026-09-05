# WTF fetch counter

## [1.0.0] — 2026-09-05

**Изменено**

- `gamedata/scripts/fix_wtf_fetch_counter.script` — monkey-patch `igi_description.get_description`: для Fetch-квестов с MCM `utjan_fetch_thing` сбрасывает `CACHE.description` перед пересборкой текста.

**Причина**

Описание WTF-квеста кэшируется один раз. Счётчик `(У тебя есть N)` из `Fetch.get_description` попадает в кэш при первом показе (часто при N=0) и больше не обновляется. Сдача при этом работает: `ready_to_finish` каждый раз пересчитывает инвентарь.

**Как исправлено**

Callback не подходит: текст PDA/диалога идёт через `get_description` напрямую. Monkey-patch:

- Если у квеста есть сущность с `to_description` и контроллером `igi_target_fetch.Fetch`, и включён `utjan_fetch_thing` — обнулить `CACHE.description`, затем вызвать оригинал.
- Остальные типы целей по-прежнему используют одноразовый кэш.
- Установка в `on_game_start`, повтор в `actor_on_first_update` (MT load). Оригинал возвращается в `on_game_end`.

**Не затронуто**

- файлы WTF (`igi_description.script`, `igi_target_fetch.script`, JSON заданий)
- логику `get_fetched_items` / сдачи / наград
- квесты без Fetch или с выключенным `utjan_fetch_thing`
- `all.spawn`, формат сейва (миграция не нужна; застывший «0» из старого сейва пересчитается при следующем показе)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего своего не пишет
- Зависимость: Weird Tasks Framework (`[QUE] wtf 4_2`). Без него — no-op
- В MO2 ниже WTF

**Проверено**

- lint: `python tools/lint_addon.py fix_wtf_fetch_counter` (0 ошибок)
- cross: `python tools/lint_addon.py --cross fix_wtf_fetch_counter`
- В игре: не прогонялось. Ожидание: у «Еда для новичков» в PDA `(У тебя есть N)` совпадает с инвентарём; у Фаната сдача без изменений
