# Kristiano Welcome

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.0] — 2026-09-14

**Изменено**

- `gamedata/scripts/kristiano_welcome.script` — одноразовое SMS при старте новой игры / первом заходе без info-portion
- `gamedata/configs/text/rus/st_kristiano_welcome.xml` — русский текст приветствия
- `gamedata/configs/text/eng/st_kristiano_welcome.xml` — английский текст приветствия
- `gamedata/textures/ui/ui_icon_news_kristiano.dds` — иконка tip’а 64×64 DXT5
- `gamedata/configs/ui/textures_descr/ui_icon_news_kristiano.xml` — регистрация текстуры
- `gamedata/configs/plugins/mod_news_tips_icons_kristiano_welcome.ltx` — ключ `kristiano` в `news_tips_icons`

**Причина**

Нужно сообщить игрокам, что активен пакет служебных фиксов Kristiano, и куда писать о проблемах.

**Как исправлено**

Callback `on_loading_screen_dismissed` + `dynamic_news_helper.send_tip` по образцу `anthology_sms.script`; повтор блокируется info-portion `dynamic_news_welcome_to_kristiano`; иконка через DLTX к `news_tips_icons`.

**Не затронуто**

- текст и логику SMS самой Anthology
- MCM, сохраняемые таблицы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим; на старом сейве без info-portion сообщение покажется один раз
- Конфликты: нет пересечения файлов с другими модами

**Проверено**

- lint_addon.py — без ошибок
- в игре: не проверено (verified_* ставит человек)
