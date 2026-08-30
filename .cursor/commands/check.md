---
description: Проверка перед коммитом. Ничего не чинить.
---

Проверка перед коммитом. Ничего не исправляй — только сводка.

1. `python3 -m unittest discover tests`
2. `python3 tools/lint_addon.py --cross` — без `mod_id`, все моды в `addon/`.
3. `python3 tools/check_changelog_tools.py`
4. `git status --short` и `git log origin/main..HEAD --oneline`

Сведи вывод: что зелёное, что красное, есть ли незапушенные коммиты. Найденное не чини.
