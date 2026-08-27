# Changelog

Изменения самого рабочего места. Изменения модов ведутся в `addon/<mod_id>/CHANGELOG.md`.

## [0.1.0] — первая версия

Добавлено:

- Правила Cursor в `.cursor/rules/`: два коротких always-apply (`anomaly-core`, `no-hallucinated-api`), три auto-attached по типам файлов (`anomaly-lua`, `anomaly-ltx`, `anomaly-mcm`), три agent-requested плейбука (`workflow-fix`, `workflow-addon`, `workflow-crash`).
- `AGENTS.md` — тот же контекст в портируемом формате.
- Структура `reference/` (только чтение) / `addon/` (мои моды) / `build/` / `logs/`.
- Инструменты: `xraylog.py`, `refindex.py`, `lint_addon.py`, `build_addon.py`, `new_addon.py`.
- Скелет аддона в `templates/addon-skeleton`.
- Документация в `docs/`: три плейбука, справочники по DLTX, MCM, проверке API, MO2, типовым ошибкам, готовые промпты.
- Тесты инструментов на фикстурах: `python3 -m unittest discover tests`.
