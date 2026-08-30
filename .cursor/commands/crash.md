---
description: Разбор лога X-Ray. Аргумент — путь к логу. Не чинить.
---

Разбор вылета. Аргумент после `/crash` — путь к логу. Нет пути — спроси и остановись.

Собери карточку: `python3 tools/xraylog.py <лог> --out logs/card.md`. Если FATAL ERROR нет — `python3 tools/xraylog.py <лог> --errors-only`. Дальше — по карточке, не по сырому логу.

Веди по [`docs/plans/crash.md`](../../docs/plans/crash.md), этапы 1–3 (правило [`.cursor/rules/workflow-crash.mdc`](../rules/workflow-crash.mdc)). Плейбук не переписывай. Ничего не исправляй. Закончи тем, чего не хватает для подтверждения причины.
