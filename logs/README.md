# logs/ — логи игры

Сюда кладутся свежие `xray_<user>.log` и тексты крэшей для разбора. В git не попадают: там локальные пути и имя пользователя Windows. Исключение — `logs/samples/`, синтетические примеры для тестов инструментов.

Первым делом лог сжимается в карточку:

```bash
python3 tools/xraylog.py logs/xray_ivan.log --out logs/card.md
```

Дальше работаем по карточке — см. [`../docs/plans/crash.md`](../docs/plans/crash.md).

Полезные режимы:

```bash
python3 tools/xraylog.py logs/xray_ivan.log --warnings-only   # только предупреждения, без вылета
python3 tools/xraylog.py logs/xray_ivan.log --context 80      # больше строк перед падением
python3 tools/xraylog.py logs/xray_ivan.log --json            # машиночитаемо
```
