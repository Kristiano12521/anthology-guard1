# Hip Quest Item Text Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/text/rus/st_fix_hip_quest_text.xml` — overlay ключа `devushka_1_start_2`.
- `gamedata/configs/text/eng/st_fix_hip_quest_text.xml` — то же для английского.

**Причина**

Цепочка Хип (`dialogs_devushka.script`) принимает только `wpn_toz34_mark4` (инвентарное имя ТОЗ-34 «Зубр» / TOZ-34 "Bizon") и 20 патронов `ammo_12x70_buck`. Журнал (`toz34_sk2_find` / `toz34_return_descr`) уже называет «Зубр». Оффер в диалоге говорил просто «уникальный ТОЗ с охотничьим прицелом» / "scoped TOZ" — рядом в сборке есть отдельный помповый ТОЗ-194.

ZIP v1.0.0 BETA подменял `st_quests_escape.xml` и `st_dialogs_escape.xml` целиком (~100 КБ). SHA256 совпал с ванильным `configs.xdb0`: 0 изменённых ключей. Полная замена ничего не чинит, конфликтует с любым модом на эти файлы и уже лежит в `[DBG] Kristiano Fixes ALL IN ONE`.

Консервы и артефакты в ванили уже совпадают с логикой: `conserva` = банка тунца, `af_vyvert` / `af_fireball` / `af_electra_moonlight` = «Выверт», «Огненный шар», «Лунный свет».

**Как исправлено**

Отдельный файл строковой таблицы с тем же `id`. Движок грузит все XML из `configs/text/<lang>/`, повтор ключа перезаписывает значение. Имя `st_fix_hip_quest_text.xml` идёт после `st_dialogs_escape.xml`. Скрипт, LTX заданий и предметы не трогались.

**Не затронуто**

- `dialogs_devushka.script`, `tm_escape.ltx`, дерево `dialogs_escape.xml`
- `st_quests_escape.xml` (журнальные строки уже верные)
- названия предметов (`st_wpn_toz34_mark4`, `st_conserva`, артефакты)
- состав сдачи, награды, инфопорции, `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Новый текст при следующем открытии диалога
- Конфликты: нет пересечения файлов с ZIP v1.0.0 (тот ставил полные `st_*_escape.xml`). В MO2 ниже сборки. ZIP и копию тех же XML в `[DBG] Kristiano Fixes ALL IN ONE` лучше выключить — они не меняют строки

**Проверено**

- lint: `python tools/lint_addon.py fix_hip_quest_text`
- Дифф ванильного `configs.xdb0` против ZIP: 0 изменённых ключей
- В игре: не прогонялось. Кордон, Хип, первый заказ — в оффере должны прозвучать «Зубр» / Bizon и 20×12x70, сдача по-прежнему только `wpn_toz34_mark4`
