# Community

- [`BUG_REPORT.md`](BUG_REPORT.md) — шаблон отчёта о проблеме для бета-тестеров (шаги, сейв, версии, `modlist.txt`, полный `xray_*.log`).
- [`UNINSTALL.md`](UNINSTALL.md) — снятие пакета `[DBG] Kristiano Fixes ALL IN ONE` (необратимое, три шага до выключения).
- [`RULES.md`](RULES.md) — канон правил Discord Anomaly Anthology.
- [`discord-rules.json`](discord-rules.json) — машиночитаемый индекс пунктов (id, наказание, сигналы).

Источник правил: Discord-сервер Anomaly Anthology, утверждённый свод администрации. Канон в репозитории обновлён 14.09.2026. Метаданные постов в текст правил не входят.

## Как проверить сообщение

```bash
python tools/modcheck.py scan "текст сообщения или лога чата"
python tools/modcheck.py lookup 5.1 8.5 9.1
python tools/modcheck.py list --section 8
```

`scan` — только кандидаты по ключевым словам, не приговор. Вердикт выносит модератор или агент по полному тексту пункта.

В чате Cursor: `/modcheck` и вставьте сообщения игрока (скрин, цитата, лог).
