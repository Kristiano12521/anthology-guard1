---
description: Новый мод. Аргумент — mod_id.
---

Новый аддон. Аргумент после `/newmod` — `mod_id`. Нет id — спроси и остановись.

Веди по [`.cursor/rules/workflow-addon.mdc`](../rules/workflow-addon.mdc); плейбук [`docs/plans/addon.md`](../../docs/plans/addon.md). Текст не копируй. Файлы не создавай до подтверждения плана.

Каркас: `python3 tools/new_addon.py <mod_id>` (читаемое имя — `--title`; `--force` сам не ставь).

В конце, строго по порядку:
1. `python3 tools/lint_addon.py <mod_id>`
2. `python3 tools/lint_addon.py --cross`
3. `python3 tools/build_addon.py <mod_id> --zip`
