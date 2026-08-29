# Burn Shit Inventory Destroy

## [1.0.6] — 2026-08-29

**Изменено**

- `gamedata/scripts/anthology_burnshit_inventory_destroy.script` — видимость «Уничтожить всё», проверка экипировки, обход рюкзака, регистрация functor'ов, сброс диалога.
- `gamedata/scripts/burnshit_inventory_destroy_mcm.script` — дефолт `destroyAll = always`.
- `gamedata/configs/text/rus|eng/burnshit_inventory_destroy.xml` — строка «нечего уничтожать», уточнены описания MCM.

**Причина**

v1.0.4 прятала оба пункта на квестовых / неторгуемых / избранных / экипированных предметах, если в рюкзаке не было двух разрешённых объектов (`destroyAll = multiple`). Снимок экипировки ходил по слоту 14 (script animation). Файл `zzzzzz_*.script` зависел от алфавитного порядка загрузки. Диалог подтверждения не сбрасывался при загрузке сейва. `can_destroy_all` на каждый ПКМ обходил весь инвентарь.

**Как исправлено**

- Дефолт «Уничтожить всё» = Всегда: пункт на каждом предмете инвентаря без обхода рюкзака. Режим «несколько» скрывает его только если одиночное «Уничтожить» уже покрывает единственный доступный объект.
- Экипировка: `SCANNED_SLOTS` (1–13) + пояс (`iterate_belt` / `belt_count`). Слот 14 не трогается.
- Сбор кандидатов: `iterate_ruck`, запасной путь — `iterate_inventory` без экипированных.
- Регистрация в `on_game_start` / `on_game_load`, снятие в `on_game_end`. Имя файла без `zzz`.
- Подпись пунктов — строковый id, не заранее переведённый текст.
- Кэш снимка экипировки и полного сбора на один `time_global()` (один ПКМ). Перед `alife_release_id` снимок берётся заново.
- `confirm_control` обнуляется на `on_game_load` / `on_game_end`.

**Не затронуто**

- Костёр оригинального Burn Shit (`burnshit.script`)
- Подтверждение Да/Нет и `alife_release_id`
- Дефолтный запрет удалять квест / `can_trade = false` / избранное / экипировку
- `all.spawn`, сохраняемые таблицы (своего `save_state` нет)
- MCM id `burnshit_inventory_destroy` (старые галочки игрока остаются)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 ниже Burn Shit и Context Menu Overhaul. ZIP v1.0.0–v1.0.5 выключить

**Проверено**

- lint: `python tools/lint_addon.py burnshit_inventory_destroy`
- В игре: не прогонялось. Ожидаемый лог: `[BurnShitInventoryDestroy] loaded v1.0.6`. ПКМ по экипировке/избранному даёт «Уничтожить всё»; по хламу в рюкзаке — «Уничтожить».
