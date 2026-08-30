# Changelog

Изменения самого рабочего места. Изменения модов ведутся в `addon/<mod_id>/CHANGELOG.md`.

## [0.1.10] — распаковка db и наполнение reference/

`tools/xdb_unpack.py` перенесён из `.cache/`: LZHUF для TOC, LZO1X для payload, argparse, чтение TOC без загрузки всего архива. `tools/fill_reference.py` наполняет `reference/anomaly/` и `reference/anthology/` из `<игра>/db` (только `scripts/`, `configs/`, `text/`; `--dry-run`; аддоны не трогает). Раздел в `docs/setup.md`, строки в таблице README.

## [0.1.9] — CHANGELOG только после факта; --cross в процессе аддона

Правило в `anomaly-core.mdc` и `AGENTS.md`: запись в CHANGELOG после применения правки и тестов, только выполненное. README: lint — `ORDER-001`/`ORDER-002`, `--cross`, `vendor_fork=1`; добавлен `_pack_kristiano_aio.py`. В `workflow-addon`, `docs/plans/addon.md` и `docs/mo2.md` `--cross` перед установкой в MO2.

## [0.1.8] — xraylog: заголовок группы не из abort()

`tools/xraylog.py`: заголовок «Нефатальные ошибки» берёт первый Lua-кадр не из инфраструктурных `_g.script` / `axr_main.script`, минуя `[C]: in function`. `abort()` в `_g.script` — обёртка, поэтому стек через `sound_theme` называется `sound_theme.script`. Если отказ в `axr_main.callback_set`, заголовок остаётся `axr_main.script`. Список обёрток — константа `INFRA_SCRIPTS`.

## [0.1.7] — `_tmp_*/` вне индекса и перекрёстный lint

Шаблон `_tmp_*/` в `.gitignore` и `.cursorignore`: распакованные чужие моды для ревью не попадают в git и не конкурируют с `addon/` в поиске Cursor. `tools/lint_addon.py --cross` предупреждает, если два мода патчат одну секцию в одном пути внутри gamedata (пара путь+секция, не имя секции само по себе). DLTX-патч `mod_<оригинал>_<суффикс>.ltx` сравнивается с оригиналом в той же папке. Исход таких пар решает порядок в MO2.

## [0.1.6] — операторы DLTX: сверка с первоисточником

В таблицах `anomaly-ltx.mdc` и `docs/dltx.md` операторы сверены со статьёй DLTX (aqxaromods, 25 Sep 2021) и README Modded Exes. `@`, `>`, `<` помечены: в оригинале их нет, это расширения exe; в корпусе `reference/` почти не встречаются. `!![section]` в оригинале есть, в корпусе — ноль.

## [0.1.5] — инструменты в README и правилах

В таблицу README добавлены `to_cp1251.ps1`, `check_encoding.ps1`, `dds_tool.ps1`, `draw_cmo_unique_icons.ps1`, `pack_bhs.py`. В `anomaly-core.mdc` — одна строка: перекодировку, проверку кодировки и DDS брать из готовых скриптов, не писать одноразовые.

## [0.1.4] — .cursorignore

`.cursorignore` исключает сырые логи, карточку xraylog, `.cache/`, `build/` и бинарники (`*.dds`, `*.png`, `*.ogg`, `*.bin`, `*.seq`) внутри `addon/` и `reference/`. Каталог `reference/` целиком не исключается — это эталон для поиска.

## [0.1.3] — xraylog: нефатальные STACK TRACEBACK

`tools/xraylog.py` больше не считает лог чистым, если FATAL ERROR нет, а Lua-ошибки с `STACK TRACEBACK` есть. Такие блоки группируются по стеку без номеров строк, попадают в секцию «Нефатальные ошибки» и не дублируются в топе предупреждений. Класс: `вылета нет, есть повторяющиеся ошибки (N групп)`. Флаг `--errors-only` — только эта секция, без вылета и warning'ов.

## [0.1.2] — линтер: load-order скриптов и профиль форка

`ORDER-001` — ошибка только для `.ltx`: порядок патчей задаёт список модов в MO2. Для `.script` с префиксом `zzz`/`aaa` — предупреждение `ORDER-002`, снимается комментарием `-- load-order: после <что>` в первых 10 строках. В `meta.ini` необязательный `vendor_fork=1` глушит `LUA-001`, `LTX-001` и `STRUCT-005` на форках чужих модов; сводка помечает такой прогон как проверенный в профиле форка.

## [0.1.1] — приоритет источников в refindex

`tools/refindex.py find|section|callback` больше не показывает попадания в порядке `os.walk`. Сначала anomaly (ваниль), затем anthology, addons, прочее — как в `docs/setup.md`. В каждой строке пометка источника; если `--limit` срезал хвост, печатается сколько записей осталось и из каких источников. Обход `iter_files` сортирует каталоги, чтобы индекс собирался одинаково между запусками. Формат `.cache/refindex.json` не менялся.

## [0.1.0] — первая версия

Добавлено:

- Правила Cursor в `.cursor/rules/`: два коротких always-apply (`anomaly-core`, `no-hallucinated-api`), три auto-attached по типам файлов (`anomaly-lua`, `anomaly-ltx`, `anomaly-mcm`), три agent-requested плейбука (`workflow-fix`, `workflow-addon`, `workflow-crash`).
- `AGENTS.md` — тот же контекст в портируемом формате.
- Структура `reference/` (только чтение) / `addon/` (мои моды) / `build/` / `logs/`.
- Инструменты: `xraylog.py`, `refindex.py`, `lint_addon.py`, `build_addon.py`, `new_addon.py`.
- Скелет аддона в `templates/addon-skeleton`.
- Документация в `docs/`: три плейбука, справочники по DLTX, MCM, проверке API, MO2, типовым ошибкам, готовые промпты.
- Тесты инструментов на фикстурах: `python3 -m unittest discover tests`.
