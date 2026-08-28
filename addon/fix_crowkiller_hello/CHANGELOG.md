# Crowkiller Hello Dialog Fix

## [1.0.0] — 2026-08-28

**Изменено**

- `gamedata/scripts/fix_crowkiller_hello.script` — monkey-patch `minigame_dialogs.crowkiller_is_valiable`: если текущая мини-игра «ворон» ещё не привязана, считает её доступной и при необходимости регистрирует `gar_bandit_crowkiller`.

**Причина**

Новая игра за бандитов, Свалка, депо, разговор с Живодером. Движок: `CPhraseDialog::SayPhrase` / `No available phrase to say, dialog[gar_bandit_bookmaker_hello]`.

Приветствие в `dialogs_cs_garbadge.xml` после пустой фразы `0` ведёт только на фразы `1`–`6`. Все они закрыты `minigame_dialogs.crowkiller_is_*`. Текущая мини-игра в менеджере стартует как `""` и заполняется только в `sr_crowkiller.set_scheme`. Пока restrictor не отработал (типично спавн сразу у стола Живодера), ни одна фраза не проходит — `m_PhraseVector` пустой — FATAL. Запасной ветки в XML нет.

**Как исправлено**

Monkey-patch, не DXML: тот же гард закрывает чёрную долину (`blck_val_bandit_bookmaker_*`) и не плодит вторую NPC-фразу, если мини-игра уже в состоянии `valiable`. Оригинал сохраняется и вызывается, если состояние уже не «доступна».

**Не затронуто**

- `dialogs_cs_garbadge.xml`, `character_desc_garbage.xml`
- `sr_crowkiller.script`, `minigames_manager.script`, спавн ворон
- Ставки / рекорд / тренировка после того, как мини-игра уже привязана
- Сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- Конфликты: нет пересечения файлов; в MO2 ниже сборки

**Проверено**

- lint: `python tools/lint_addon.py fix_crowkiller_hello`
- В игре: новая игра за бандитов, Свалка, депо, поговорить с Живодером. В логе: `crowkiller_is_valiable wrapped`. Диалог должен открыться, а не закрыть игру.
