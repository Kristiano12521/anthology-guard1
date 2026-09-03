---
description: Сборка и сверка с MO2. Путь MO2 — аргумент, ANTHOLOGY_MO2 или local.json.
---

Полный цикл сборки и сверки с MO2. Цепочка: [`docs/mo2.md`](../../docs/mo2.md). Код модов не трогай.

## Путь к MO2

Не хардкодь. Возьми из аргумента команды, иначе `$env:ANTHOLOGY_MO2` / `ANTHOLOGY_MO2`, иначе `local.json` → ключ `mo2` (образец `local.json.example`).

Если путь не задан — остановись после сборки, покажи:

```text
Путь к MO2 не задан. Укажи аргументом, ANTHOLOGY_MO2 или local.json.
```

и не выдумывай путь. Шаги 2–4 тогда пропусти с этой пометкой.

## 1. Собрать всё

По порядку, из корня репозитория:

```bash
python3 tools/pack_bhs.py
python3 tools/_pack_kristiano_aio.py
```

AIO забирает все `addon/*/gamedata/` кроме `SKIP`/`SEPARATE` (`_pack_kristiano_aio.py`); BHS внутри AIO через `pack_bhs.stage_gamedata`, отдельный zip BHS — для точечного обновления. SEPARATE (CMO, QuickQK, ST2) — отдельные архивы из того же пакера.

Обычные моды вне этих пакетов: если в `addon/` есть `gamedata/` не из `SKIP`/`SEPARATE` и не из состава AIO — такого сейчас нет; если появится — `python3 tools/build_addon.py <mod_id> --zip` (ошибки линтера — чини или `--force` с пояснением).

В ответе перечисли, что собралось: имя архива/папки в `build/`, версия, краткий итог stdout.

## 2. Сверить с MO2

```bash
python3 tools/check_installed.py "<MO2>"
```

Без явного пути (если заданы env / `local.json`):

```bash
python3 tools/check_installed.py
```

По каждому пакету с `BUILD_INFO.txt`: устарел / актуален / не установлен. Если скрипт пишет «mtime недостоверен… Сравнивать с addon/ нечего» (CI, `--no-mtime`, или узкий разброс mtime после clone) — так и скажи; не помечай всё устаревшим вручную.

## 3. Что переустановить

Возьми блок «переустановить в MO2» из вывода `check_installed` (или `python3 tools/check_installed.py --reinstall`). Для каждого пункта: причина, путь к zip в `build/`.

Напомни: в MO2 — **Install mod from archive → заменить существующий мод**, не создавать второй с тем же именем. Старая папка с устаревшим `BUILD_INFO.txt` — частая причина «в игру уехал старый код».

## 4. После установки

Когда пользователь поставит архивы, проверка:

```bash
python3 tools/check_installed.py
```

Ожидание: пакеты **актуален**, блок переустановки пуст, `built` в `BUILD_INFO.txt` не старше свежей сборки. Если снова «устарел» — в MO2 лежит старая копия.
