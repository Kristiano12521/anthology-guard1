# STALKER Anthology Dev

Рабочее место для разработки фиксов и аддонов к сборке **S.T.A.L.K.E.R. Anomaly 1.5.3 / Anthology 2.1** (Modded Exes MT) вместе с Cursor.

Репозиторий решает три задачи: **фиксы багов**, **новые аддоны**, **разбор вылетов**. Под каждую есть правило-плейбук для агента, набор промптов и инструменты.

## Что внутри

```
.cursor/rules/          правила Cursor (.mdc)
  anomaly-core.mdc          always-apply, короткое: стек, границы, запреты
  no-hallucinated-api.mdc   always-apply, короткое: протокол проверки API
  anomaly-lua.mdc           auto-attached: addon/**/*.script
  anomaly-ltx.mdc           auto-attached: addon/**/*.ltx
  anomaly-mcm.mdc           auto-attached: addon/**/*_mcm.script
  anomaly-xml.mdc           auto-attached: addon/**/*.xml
  workflow-fix.mdc          agent-requested: фикс бага
  workflow-addon.mdc        agent-requested: новый аддон
  workflow-crash.mdc        agent-requested: разбор вылета

AGENTS.md               тот же контекст в портируемом виде
addon/<mod_id>/         мои моды — единственное место для правок
reference/              исходники сборки, только чтение (в git не хранятся)
build/                  собранные моды для MO2
logs/                   логи игры для разбора вылетов
docs/                   плейбуки, справочники, готовые промпты
templates/              скелет аддона
tools/                  инструменты анализа и сборки
```

## Быстрый старт

1. **Наполнить `reference/`.** `python3 tools/fill_reference.py <папка игры>`, затем аддоны из MO2 в `reference/addons/`. Подробно: [`docs/setup.md`](docs/setup.md).

2. **Построить индекс** — он нужен правилу «не выдумывай API»:

```bash
python3 tools/refindex.py build
```

3. **Проверить, что индекс живой:**

```bash
python3 tools/refindex.py find actor_on_first_update
python3 tools/refindex.py section wpn_ak74
```

4. **Создать первый мод:**

```bash
python3 tools/new_addon.py my_fix_weapon_jam --title "Weapon Jam Fix"
```

5. **Собрать и поставить в MO2:**

```bash
python3 tools/lint_addon.py my_fix_weapon_jam
python3 tools/build_addon.py my_fix_weapon_jam --zip
```

## Инструменты

| Команда | Зачем |
| --- | --- |
| `tools/xraylog.py <log>` | сжимает многомегабайтный лог игры в карточку вылета: класс ошибки, стек, warning'и перед падением |
| `tools/xdb_unpack.py <archive> [--list\|--out]` | распаковка `.db`/`.dbN`/`.xdb`: TOC через LZHUF, файлы через LZO1X |
| `tools/fill_reference.py <игра> [--dry-run]` | наполняет `reference/anomaly/` и `reference/anthology/` из `<игра>/db`: только `scripts/`, `configs/`, `text/` |
| `tools/refindex.py build\|find\|section\|callback\|stats` | индекс по `reference/`: проверка, что функция/секция/callback реально существуют |
| `tools/lint_addon.py [mod_id] [--cross]` | проверяет мод на правила: замена файлов сборки, дубли DLTX-секций, кодировка, анонимные callback'и. `ORDER-001` — ошибка на `zzz`/`aaa` у `.ltx`; `ORDER-002` — предупреждение у `.script`, снимается комментарием `-- load-order: после <что>` в первых 10 строках. `--cross` — предупреждения `CROSS-001`, если два мода патчат одну секцию в одном пути внутри gamedata. `vendor_fork=1` в `meta.ini` глушит `LUA-001`, `LTX-001` и `STRUCT-005` на форках чужих модов |
| `tools/new_addon.py <mod_id>` | создаёт скелет мода из `templates/addon-skeleton` |
| `tools/build_addon.py <mod_id>` | собирает мод в `build/`, опционально в zip или сразу в папку модов MO2 |
| `tools/to_cp1251.ps1 <file>…` | UTF-8 → Windows-1251 для игровых файлов; отказывается писать, если символ не входит в cp1251 |
| `tools/check_encoding.ps1 <folder>` | отчёт по кодировке `.script`/`.ltx`/`.xml`/`.txt`/`.ini`/`.seq` в папке: ascii, cp1251 или utf-8, плюс BOM |
| `tools/dds_tool.ps1 decode\|encode` | DDS ↔ PNG для UI-иконок: DXT1/DXT5 и несжатый A8R8G8B8; encode пишет DXT5 без мипов |
| `tools/draw_cmo_unique_icons.ps1` | рисует уникальные 64×64 силуэты CMO и кодирует их в DXT5 DDS через `dds_tool.ps1` |
| `tools/check_changelog_tools.py` | падает, если в диффе `CHANGELOG.md` есть путь `tools/`, а файлы в `tools/` не менялись |
| `tools/pack_bhs.py` | собирает zip Anthology Busy Hands Stability Fix из `reference/` + оверлеи `addon/anthology_busyhands_stability_fix` |
| `tools/_pack_kristiano_aio.py` | одноразовый пакер: zip `[DBG] Kristiano Fixes ALL IN ONE` из всех модов в `addon/` с `gamedata/` (кроме трёх отдельных и снятого `fix_bhs_fdda_loot`) плюс три отдельных архива — Context Menu Overhaul, QuickQK Task Complete, ST2 Footstep — в `build/` |

Python-инструменты — 3.9+, без зависимостей. Кодировка и DDS — PowerShell (`*.ps1`). На Windows — `py -3` вместо `python3`.

## Как работать с агентом

Три плейбука с готовыми промптами:

- [`docs/plans/fix.md`](docs/plans/fix.md) — фикс бага
- [`docs/plans/addon.md`](docs/plans/addon.md) — новый аддон
- [`docs/plans/crash.md`](docs/plans/crash.md) — разбор вылета

Короткая версия: в первом сообщении явно называй workflow.

```
Это разбор вылета, веди по workflow-crash.
Лог: @logs/xray_ivan.log
Этапы 0–3, ничего не исправляй.
```

Правила `workflow-*` подключаются агентом по описанию, но явное упоминание надёжнее автодетекта.

## Справочники

- [`docs/setup.md`](docs/setup.md) — наполнение `reference/`, связка с MO2, кодировки
- [`docs/rules.md`](docs/rules.md) — как устроены правила, режимы активации, токен-бюджет
- [`docs/dltx.md`](docs/dltx.md) — DLTX: операторы, именование, типовые ошибки
- [`docs/mcm.md`](docs/mcm.md) — MCM: контракт `on_mcm_load`, чтение значений
- [`docs/api-verification.md`](docs/api-verification.md) — протокол проверки движкового API
- [`docs/pitfalls.md`](docs/pitfalls.md) — на чём агент чаще всего врёт про Anomaly
- [`docs/mo2.md`](docs/mo2.md) — цепочка исходники → build → MO2 → игра
- [`docs/prompts.md`](docs/prompts.md) — готовые промпты
- [`docs/references.md`](docs/references.md) — внешние источники

## Правила самого репозитория

- `reference/` не редактируется никогда — это эталон.
- Игровые файлы правятся только внутри `addon/<mod_id>/`.
- Каждый мод ведёт свой `CHANGELOG.md`: что изменено, причина, что не затронуто, на какой версии сборки проверено.
- Диагностический скрипт и фикс-скрипт — разные файлы.

## Лицензия

Оригинальные инструменты, правила, документация и собственные фиксы — MIT, см. [`LICENSE`](LICENSE). Форки чужих модов в `addon/` и игровые исходники в `reference/` (в git нет) под эту лицензию не падают — [`NOTICE`](NOTICE).
