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

1. **Наполнить `reference/`.** Распакованные `gamedata` ванильной Anomaly 1.5.3, Anthology 2.1 и ключевых аддонов сборки. Подробно: [`docs/setup.md`](docs/setup.md).

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
| `tools/refindex.py build\|find\|section\|callback\|stats` | индекс по `reference/`: проверка, что функция/секция/callback реально существуют |
| `tools/lint_addon.py <mod_id>` | проверяет мод на нарушения правил проекта: полная замена файлов сборки, `zzz`-префиксы, анонимные callback'и, дубли DLTX-секций, кодировка |
| `tools/new_addon.py <mod_id>` | создаёт скелет мода из `templates/addon-skeleton` |
| `tools/build_addon.py <mod_id>` | собирает мод в `build/`, опционально в zip или сразу в папку модов MO2 |

Всё на чистом Python 3.9+, без зависимостей. На Windows — `py -3` вместо `python3`.

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
