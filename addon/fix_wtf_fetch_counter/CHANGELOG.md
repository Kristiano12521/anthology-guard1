# WTF fetch counter

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 ниже WTF После замены таблицы WTF счётчик снова залипал на закэшированном N.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.1] — 2026-09-16

**Изменено**

- `gamedata/scripts/fix_wtf_fetch_counter.script` — на `actor_on_first_update` переустанавливает wrap, если `igi_description.get_description` уже не наша обёртка (MT reload). Uninstall возвращает orig только если слот ещё наш.

**Причина**

1.0.0 при `installed=true` не проверял указатель. После замены таблицы WTF счётчик снова залипал на закэшированном N. Тот же паттерн, что у `fix_hostage_task_collision`.

**Не затронуто**

- Логика сброса `CACHE.description` для Fetch + `utjan_fetch_thing`

**Совместимость**

- Как 1.0.0
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_wtf_fetch_counter`
- в игре: не прогонялось. Ожидание: после load счётчик в PDA снова живой.

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
