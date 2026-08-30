# logs/ — логи игры

Сырые `xray_*.log` — временные: по несколько мегабайт, с локальными путями и именем пользователя Windows. В git и в индекс Cursor не попадают. Исключение — `logs/samples/`, синтетические примеры для тестов инструментов.

Постоянная база — карточки в `logs/cards/`. Одна карточка на разбор, имя `YYYY-MM-DD_<источник>.md` (при совпадении — суффикс `-2`). Их можно коммитить и искать. Одноразовая копия текущего прогона — `logs/card.md`: каждый запуск затирает предыдущий, в индекс Cursor не входит.

```bash
python3 tools/xraylog.py logs/xray_ivan.log --out logs/card.md --archive
```

`--archive` пишет карточку в `logs/cards/` и печатает путь. Без флага поведение прежнее: stdout или `--out`.

Дальше работаем по карточке — см. [`../docs/plans/crash.md`](../docs/plans/crash.md).

Ротация сырых логов оставляет N самых свежих `logs/*.log` (по умолчанию 3), `logs/samples/` не трогает:

```bash
python3 tools/prune_logs.py --dry-run
python3 tools/prune_logs.py --yes
python3 tools/prune_logs.py --yes --keep 5
```

Без `--yes` ничего не удаляется.

Полезные режимы:

```bash
python3 tools/xraylog.py logs/xray_ivan.log --warnings-only   # только предупреждения, без вылета
python3 tools/xraylog.py logs/xray_ivan.log --errors-only     # только нефатальные STACK TRACEBACK
python3 tools/xraylog.py logs/xray_ivan.log --context 80      # больше строк перед падением
python3 tools/xraylog.py logs/xray_ivan.log --json            # машиночитаемо
```
