# Правила Discord Anomaly Anthology

Канон для проверки игроков на нарушение. Человекочитаемый свод — [`RULES.md`](RULES.md). Машиночитаемый индекс пунктов (id, наказание, сигналы) — [`discord-rules.json`](discord-rules.json).

Источник: Discord-сервер Anomaly Anthology, сообщения администрации (Кирилл [5RP]), 14.06.2026 — 06.07.2026. Метаданные постов в текст правил не входят.

## Как проверить сообщение

```bash
python tools/modcheck.py scan "текст сообщения или лога чата"
python tools/modcheck.py lookup 5.1 7.3 8.4
python tools/modcheck.py list --section 8
```

`scan` — только кандидаты по ключевым словам, не приговор. Вердикт выносит модератор или агент по полному тексту пункта.

В чате Cursor: `/modcheck` и вставьте сообщения игрока (скрин, цитата, лог).
