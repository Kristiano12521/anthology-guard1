# Наполнение reference/ и настройка окружения

## Зачем нужен reference/

Это эталонная копия исходников сборки, доступная агенту только на чтение. Она решает две задачи: даёт возможность проверить, что функция или секция существуют, и снимает соблазн править файлы сборки напрямую. В git она не хранится — объём и лицензия.

## Что положить

```
reference/
├─ anomaly/          распакованные gamedata ванильной Anomaly 1.5.3
│  ├─ scripts/
│  ├─ configs/
│  ├─ text/
│  └─ materials/
├─ anthology/        gamedata Anthology 2.1 (то, чем сборка отличается от ваниллы)
├─ addons/           gamedata ключевых аддонов сборки, по папке на аддон
└─ docs/             README Modded Exes, заметки, распечатки вики
```

Порядок именно такой: при конфликте одного и того же файла инструменты и агент должны понимать, что `anthology/` перекрывает `anomaly/`, а `addons/` — обоих (реальный порядок задаётся MO2, здесь это только соглашение).

Текстуры, модели, звуки в `reference/` класть не нужно — они не помогают анализу и раздувают папку. Минимум: `scripts/`, `configs/`, `text/`, `materials/`.

## Наполнение reference/

Из установленной игры (папка, внутри которой есть `db/`):

```bash
python3 tools/fill_reference.py "C:/games/anomaly-1.5.3-anthology 2.1" --dry-run
python3 tools/fill_reference.py "C:/games/anomaly-1.5.3-anthology 2.1"
python3 tools/refindex.py build
```

`--dry-run` печатает архивы и пути, ничего не пишет. Повторный запуск не дублирует файлы: совпавший байт в байт пропускается, лишние уже лежащие файлы не удаляются.

Что делает скрипт:

- Ищет архивы `.db`, `.xdb` и `.db0`/`.db1`/… (так Anomaly именует тома) в `<игра>/db` и вложенных папках.
- Читает TOC (chunk 1, LZHUF) и достаёт payload (LZO1X) через `tools/xdb_unpack.py`. Целый архив в память не грузится.
- Пишет только пути с каталогом `scripts/`, `configs/`, `text/` или `materials/`. Текстуры, модели, звуки, шейдеры, уровни — нет.
- Архив, в чьём относительном пути от `db/` есть `anthology`, идёт в `reference/anthology/`, остальные — в `reference/anomaly/`.

Чего скрипт **не** делает:

- Не копирует распакованную `gamedata/` с диска — это `fill_reference_addons.py` (см. ниже). В Anthology 2.1 основная масса исходников лежит модами MO2, не в `.db0`.
- Не трогает `reference/addons/`.
- Не распаковывает форматы, кроме X-Ray с chunk 1 в TOC. Неопознанный файл печатается и пропускается.

Из модов MO2 (папка самого менеджера, не профиля):

```bash
python3 tools/fill_reference_addons.py "C:/Games/ANTHOLOGY/SYS_A.N.T.H.O.L.O.G.Y_mo2_CBT" --dry-run
python3 tools/fill_reference_addons.py "C:/Games/ANTHOLOGY/SYS_A.N.T.H.O.L.O.G.Y_mo2_CBT"
python3 tools/refindex.py build
```

Профиль по умолчанию — `selected_profile` из `ModOrganizer.ini`. Кириллица там часто в `@ByteArray` с `\xNN` (UTF-8 байты); скрипт это разворачивает, иначе папка профиля не найдётся. `--profile` перекрывает имя из ini.

Что делает скрипт:

- Читает `<MO2>/profiles/<профиль>/modlist.txt`: `+` включён, `-` выключен, `*` — unmanaged MO2 (тоже включён). Имена с суффиксом `_separator` — разделители, не моды.
- Порядок строк в файле **обратный** порядку загрузки: MO2 пишет список с конца приоритета (`Profile::doWriteModlist`, `crbegin`), первая строка — низ левой панели и выигрывает конфликты файлов. В `reference/addons/` каждый мод идёт в свою папку, наложения нет.
- Копирует из `<MO2>/mods/<имя>/gamedata/` только `scripts/`, `configs/`, `text/`, `materials/` в `reference/addons/<имя из modlist>/`. Имена со скобками и кириллицей берутся буквально, не через glob.
- Свои сборки по умолчанию пропускаются: имя начинается с префикса из `AIO_NAME` / `SEPARATE` (`_pack_kristiano_aio.py`) или `OUT_STEM` (`pack_bhs.py`) — так ловятся и старые копии без `BUILD_INFO` и варианты с суффиксом `(NEW)`; либо есть `BUILD_INFO.txt`, `CONTENTS.txt` от Kristiano AIO, или в `meta.ini` notes/comments со `STALKER Anthology Dev` / `vendor_fork=1` / `installationFile` с путём на `Anthology/build`. `--include-own` копирует и их.
- Повторный запуск идемпотентен (`write_if_changed`). `--dry-run` — сводка по модам и итог, без списка файлов.
- `--prune` удаляет папки в `addons/`, которых нет среди включённых чужих модов (свои включённые тоже считаются лишними, если нет `--include-own`). По умолчанию выключено; без `--yes` печатает список к удалению и выходит, ничего не копируя и не удаляя.

Всё включённое идёт в `addons/`, не в `anthology/`: среди модов MO2 нет надёжного признака «ядро сборки vs аддон».

Один архив вручную:

```bash
python3 tools/xdb_unpack.py path/to/scripts.db0 --list
python3 tools/xdb_unpack.py path/to/scripts.db0 --out unpacked/ --filter scripts/
```

## Что не класть

- `all.spawn` и прочие бинарники — их всё равно не прочитать.
- Сейвы и `appdata` — там нет ничего для анализа кода.
- Свои моды — они живут в `addon/`.

## Индекс

После каждого обновления сборки:

```bash
python3 tools/refindex.py build
```

Индекс кладётся в `.cache/refindex.json` и в git не попадает. Проверка:

```bash
python3 tools/refindex.py stats
python3 tools/refindex.py find actor_on_first_update
```

## Кодировка

Игровые `.script` и `.ltx` — Windows-1251. Практические следствия:

- В редакторе для этих файлов выставь cp1251, иначе кириллица в комментариях и строках превратится в мусор при сохранении.
- BOM не ставим никогда.
- `.gitattributes` помечает игровые файлы как `-text`, чтобы git не переписывал переводы строк.
- `tools/lint_addon.py` предупреждает, если файл похож на UTF-8.

Простое правило, снимающее большую часть проблем: в новых файлах комментарии и строковые константы пиши латиницей, кириллицу держи в строковых таблицах `configs/text/`.

## Пути на Windows

Репозиторий не обязан лежать внутри MO2. Рабочая раскладка:

```
D:\STALKER_DEV\Anthology\      этот репозиторий
D:\STALKER_DEV\Anthology\build\  результат сборки
<MO2>\mods\                     сюда ставятся собранные моды
```

Копирование логов из MO2 в `logs/` удобно делать разово перед разбором: логи лежат в профиле MO2 (`<MO2>/profiles/<profile>/`) либо в `appdata/logs` внутри инстанса.

## Python

Нужен Python 3.9+. Внешних зависимостей нет. На Windows команды из документации выглядят как `py -3 tools\refindex.py build`.

**Кодировка консоли (Windows).** Инструменты печатают по-русски в UTF-8, PowerShell по умолчанию читает вывод в OEM — получаются кракозябры. В текущей сессии: `chcp 65001` и `$env:PYTHONIOENCODING = "utf-8"`; постоянно — те же строки в `$PROFILE`. Отдельно: не-ASCII в разметке вывода самих инструментов (например стрелка `→` в `print`) роняет запуск на консоли cp1251 — в `tools/` для разметки только ASCII, кириллица в тексте допустима.

Тесты инструментов:

```bash
python3 -m unittest discover tests
```

На `push` и `pull_request` то же гоняет GitHub Actions (Python 3.9 и 3.12), плюс `python tools/lint_addon.py --cross --no-verify` (предупреждения не валят сборку; `VERIFY-001` в CI пропускается — mtime после clone недостоверен) и `python tools/check_changelog_tools.py`.
