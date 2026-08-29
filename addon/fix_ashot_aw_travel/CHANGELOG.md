# Ashot Army Warehouses Travel Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_ashot_aw_travel.script` — monkey-patch `western_goods_utils.get_named_location` для секции `western_goods_guide_dest_mil_base`. Если её gvid указывает не на Армейские склады, координаты подменяются на `mil_smart_terrain_7_7`.

**Причина**

Western Goods ведёт Ашота на Юпитере маршрутом «Военные склады на базе Свободы». Секция `western_goods_guide_dest_mil_base` в `mod_named_locations_western_goods_guides.ltx` хранит вершины Anomaly 1.5.x: `lvid=281438`, `gvid=2093`, позиция `-11.5322, -8.5719, -21.6517`. В game.graph Anthology 2.1 этот gvid принадлежит `l04u_labx18`. `western_goods_guide.use_guide` читает named location и вызывает `ChangeLevel` — игрок оказывается в X-18.

Бета v1.0.5 оборачивала глобальный `ChangeLevel`, фильтровала вызов по callstack и магическим числам, ставила `zzzz`-префикс и ставила хук трижды. `printf` с `%d` в Anomaly не подставляет числа; перехват по стеку ненадёжен.

**Как исправлено**

Monkey-patch единственного читателя координат. DLTX здесь хуже: захардкоженные вершины снова протухнут при следующем сдвиге графа — ровно так сломался оригинал. Callback `western_goods_guide_on_change_level` получает только имя локации и назначение не меняет. Если секция уже резолвится в `l07_military` / `military`, патч ничего не трогает.

**Не затронуто**

- `western_goods_guide.script`, глобальный `ChangeLevel`
- остальные named locations и маршруты гидов Western Goods
- MLR / Immersive Travel / обычные переходы
- диалоги Ашота, цена маршрута (6000)
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет
- Зависимость: Western Goods. Без него — no-op
- В MO2 ниже Western Goods. Бета v1.0.0–v1.0.5 и диагностический call-trace должны быть выключены

**Проверено**

- lint: `python tools/lint_addon.py fix_ashot_aw_travel`
- В игре: загрузка на Юпитере, разговор с Ашотом, маршрут на Армейские склады. В логе: `get_named_location wrapped`, затем `remapped western_goods_guide_dest_mil_base ... dest=l07_military`. Прибытие — база Свободы, не X-18.
