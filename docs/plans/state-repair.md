# План: правка STATE alife-объекта

Для случая «битые данные уже лежат в пакете alife-объекта (сейв / spawn), а не в LTX». Правило: [`.cursor/rules/workflow-state.mdc`](../../.cursor/rules/workflow-state.mdc).

Эталон каркаса — три аддона: `fix_kupol_wrong_bone`, `fix_aver_darkvalley`, `fix_gigant_space_restriction`. В `addon/` callback `server_entity_on_register` встречается только в них. Ниже — то, что видно в этих трёх скриптах; утверждений про движок вне их кода нет. Если каркас расходится — расхождение названо явно, без усреднения.

## Когда этот плейбук НЕ нужен

- Значение есть в LTX и правится секцией — обычный [`fix.md`](fix.md) через DLTX.
- Объект уже online, чинить нужно клиентскую логику/схему при активации — другой приём: см. `fix_vows_ambush_stash` (monkey-patch `xr_logic.activate_by_section` + разовый `try_repair_online_stash` на `actor_on_first_update`; `server_entity_on_register` там нет).
- Новый контент / новая механика — [`addon.md`](addon.md). Вылет без понятного alife-объекта — сначала [`crash.md`](crash.md).

## Общий каркас (все три)

Одинаковый набор callback'ов: регистрация в `on_game_start`, снятие в `on_game_end` (именованные функции):

| Callback | Роль в каркасе |
| --- | --- |
| `server_entity_on_register` | ранняя точка на se-объекте (фильтр по типу/виду) |
| `actor_on_first_update` | полный проход / «уровень готов» |
| `on_before_level_changing` | действие до смены уровня |
| `on_level_changing` | то же (или повтор) при смене |
| `on_game_load` | сброс флагов/кэшей на загрузку сейва |

Идентификация цели — по имени / секции / clsid, не по «магическому» числовому id как единственному ключу (у gigant явный запрет опираться на id из-за remapper'а; kupol/aver кэшируют id только после нахождения объекта).

## Расхождения (не усреднять)

### A. Перепись пакета (`kupol`, `aver`)

1. Найти se-объект (`server_entity_on_register` и/или `scan_alife` через `alife():iterate_objects` / перебор id).
2. Проверки до записи: имя/маршрут, уровень источника, наличие `utils_stpk.get_*` / `set_*`, сигнатура данных (visual+fixed_bones у kupol; dest рядом с «плохими» координатами у aver).
3. Запись: `utils_stpk.set_physic_data` / `set_level_changer_data`, затем повторный get и проверка.
4. «Уже не нужно»: флаг на этот load — `patched_this_load` (kupol) или `done[route.key]` / `all_done()` (aver). Ставится и при успехе, и при «уже исправлено», и при несовпадении сигнатуры (SKIP).
5. Смена уровня: оба вызывают `scan_alife` в `on_before_level_changing` и `on_level_changing` (попытка дописать пакет до/во время перехода).
6. Только aver: на `actor_on_first_update` дополнительно `rescue_actor` — если актёр уже стоит у «плохого» dest, `db.actor:set_actor_position` на fix-координаты (один раз за load: `rescued_this_load`).

### B. Карантин / release (`gigant`)

Скрипт пишет: поля CSE space restrictors в Lua не экспортированы, запись — no-op; binder'ы после client spawn гонку не выигрывают. Поэтому пакета через `utils_stpk` нет.

1. `server_entity_on_register`: запомнить имя/id; для гиганта — проверка graph vertex / smart terrain; если offline и уровень не готов или объект не на текущем уровне — `set_switch_online(false)` (quarantine) + отложенный `process` через `CreateTimeEvent`.
2. Monkey-patch `se_monster.can_switch_online`: пока id в `quarantined`, возвращает `false`.
3. `actor_on_first_update`: `level_ready = true`, `process_all` — безопасным разрешить online (`allow_online`), небезопасным offline — `alife_release` / `sim:release`.
4. Смена уровня: `quarantine_current_level` (сброс `level_ready`, снова держать offline гигантов текущего уровня) — не scan/rewrite.
5. «Уже не нужно» в смысле one-shot флага нет: объект снимается из учёта через `released[id]` либо снова проходит process; карантин временный до готовности уровня.

## Этап 1. Локализация объекта и поля

```
Это правка STATE, веди по workflow-state. Этап 1, ничего не редактируй.

Симптом: <что ломается, на каком уровне / объекте>
Кандидат: <имя se-объекта / секция / clsid, если известны>

Покажи по коду трёх эталонов, какой путь ближе: A (utils_stpk) или B (quarantine/release).
Не предлагай DLTX и не трогай all.spawn.
```

Признак провала: сразу патч LTX или правка `all.spawn`.

## Этап 2. Доказуемость «не в LTX»

```
Этап 2. Откуда видно, что значение не из конфига секции?
Что именно читается/пишется в эталонном моде того же класса объекта
(get_physic_data / get_level_changer_data / либо почему записи нет, как у gigant).
Догадки помечай как догадки. reference/ пуст — не выдумывай API.
```

## Этап 3. Точки хука и идемпотентность

```
Этап 3. Перечисли:
- какие callback'и регистрируются (сверь со списком выше);
- фильтр в server_entity_on_register (type_name и/или is_*);
- что делается на on_before/on_level_changing (scan vs quarantine);
- чем мод помечает «чинить больше не нужно» на этот load
  (patched_this_load / done[] / released[] — как в ближайшем эталоне);
- что сбрасывается в on_game_load.
Кода не пиши.
```

## Этап 4. Предложение

```
Этап 4. В 2-3 предложениях: путь A или B, список файлов в addon/<mod_id>/,
явный список проверок до мутации, что НЕ меняется (LTX, all.spawn, online-объекты без карантина).
Кода пока не пиши.
```

## Этап 5. Патч

```
Этап 5. Реализуй в addon/<mod_id>/ по выбранному эталону.
Сигнатуры callback'ов не меняй. Не сканируй alife в actor_on_update.
```

## Этап 6. Проверка

```bash
python3 tools/lint_addon.py <mod_id>
python3 tools/lint_addon.py --cross
```

```
Этап 6. Проверь:
- загрузку сейва, где баг ещё есть, и сейва, где уже починен (флаг done / already fixed);
- переход на уровень с объектом и уход с него (ветки level_changing);
- что после успешной правки повторные callback'и no-op;
- порядок в MO2 относительно зависимостей (utils_stpk / связанные моды);
- после подтверждения в игре — verified_* в meta.ini (только человек);
- CHANGELOG.md мода.
```

## Если не сработало

Не меняй приём вслепую. Вернись к этапу 2: путь A vs B мог быть выбран неверно (у gigant запись пакета сознательно отсутствует). Сравни логи тегов `[fix_*]` эталона с своим `reason=` в callback'ах.
