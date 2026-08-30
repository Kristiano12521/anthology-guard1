# Changelog

Изменения самого рабочего места. Изменения модов ведутся в `addon/<mod_id>/CHANGELOG.md`.

## [0.1.18] — VERIFY-001 не в CI: --no-verify и автоотключение

`lint_addon.py --no-verify` отключает проверку в игре. То же само, если выставлена `CI` или `GITHUB_ACTIONS`: после clone mtime у всех файлов равен чекауту и сверка с `verified_date` бесполезна. В сводке одна строка, почему пропущено. `--unverified` в таком окружении всё равно печатает список и предупреждает, что mtime недостоверен. Шаг Lint addons в CI — явно `--cross --no-verify`. Ограничение в `docs/mo2.md`.

## [0.1.17] — verified_* в meta.ini; VERIFY-001 и --unverified

Необязательные ключи `verified_date` / `verified_build` / `verified_note`: человек ставит после проверки в игре, агент не проставляет (`anomaly-core.mdc`). Линтер: предупреждение `VERIFY-001`, если ключей нет или файлы в `gamedata/` новее даты; `vendor_fork=1` не глушит. `python3 tools/lint_addon.py --unverified` — список на сессию. Формат в `docs/mo2.md` и закомментированных строках скелета. Строка в этапах проверки `workflow-fix`, `workflow-addon` и плейбуках.

## [0.1.16] — slash-команды /check, /crash, /newmod

`.cursor/commands/`: `/check` (тесты, `lint_addon.py --cross`, `check_changelog_tools.py`, git status/log), `/crash` (`xraylog.py`, этапы 1–3 crash-плейбука), `/newmod` (`new_addon.py`, дальше workflow-addon, lint и `build_addon.py --zip`). Раздел в README рядом с таблицей инструментов; в `docs/prompts.md` пометка, что промпты, ставшие командами, вызываются через `/`.

## [0.1.15] — MIT + NOTICE; --cross в workflow-fix

Корневой `LICENSE` — MIT только на оригинальное (tools, docs, правила, собственные фиксы). Форки в `addon/` и `reference/` вынесены в `NOTICE`; указатель в README. Этап 6 в `workflow-fix.mdc` и `docs/plans/fix.md`: `lint_addon.py --cross`.

## [0.1.14] — промпты fill_reference / --errors-only / --cross; reference/README

`docs/prompts.md`: секция «Развёртывание на новой машине» с `fill_reference.py` как первым шагом; в разборе вылета — `--errors-only` и промпт, когда FATAL нет, а ошибки есть; в новом аддоне — `lint_addon.py --cross`. `reference/README.md`: `docs/` наполняется руками; `anomaly/` и `anthology/` — `fill_reference.py` (только `scripts/`/`configs/`/`text/`); `addons/` скрипт не трогает.

## [0.1.13] — отладка из гайда Anomaly: `-dbg`, `run_string`, тихие провалы скриптов

`docs/pitfalls.md`: `-dbg` и debug HUD (оверлей зон как зеркало `db.actor_inside_zones`; три мода со `space_restrictor`); синтаксическая ошибка `.script` без попапа; коллизия глобалов. `docs/api-verification.md`: `run_string` — первый способ проверки в сессии, диагностический скрипт — для повторяющихся. Этап 6 в `docs/plans/fix.md` и `workflow-fix.mdc`: повтор фичи, бой/меню/торговля, оборонительный `load_state`. Ссылки на разделы гайда в `docs/references.md`. Сверка с xray-monolith: `-dbg`, `run_string` и `flush` есть; подписи оверлеев в русской сборке не подтверждены.

## [0.1.12] — CI, сверка CHANGELOG с tools/, тесты пакеров

`.github/workflows/ci.yml`: Python 3.9 и 3.12 на push/pull_request — `unittest discover tests`, `lint_addon.py --cross` (предупреждения не валят сборку), `check_changelog_tools.py`. Guard падает, если в добавленных строках CHANGELOG есть путь `tools/`, а файлы под `tools/` в диапазоне не менялись. Тесты `pack_bhs` и `_pack_kristiano_aio` на фикстурах: состав zip, `gamedata/` на верхнем уровне, SKIP/SEPARATE, имя с версией.

## [0.1.11] — нефатальные ошибки в crash-плейбуке; правило XML

`workflow-crash.mdc` и `docs/plans/crash.md`: этап 0 знает секцию «Нефатальные ошибки» и `--errors-only`; в таблице классификации — повторяющийся STACK TRACEBACK без FATAL и `![axr_main callback_set] callback X doesn't exist` / `to nil function`. Новое auto-attached правило `anomaly-xml.mdc` (строковые таблицы, Windows-1251, пара eng/rus, `modxml_*` по двум скриптам в `addon/`). Строки в README и `docs/rules.md`.

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
