# fix_quest_stash_hint

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; ниже Grok's Stash Overhaul и The Anomalous Stash; рядом с `fix_quest_stash`.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Уже поставленные метки `treasure` остаются - плюс.

## [1.0.1] - 2026-09-20

**Изменено**

- patched_get_random_stash: после 8 попыток фильтра — fallback на orig.get_random_stash без фильтра (не 
eturn nil).
- Лог fallback один раз за сессию; счётчик ilter_fallback_count растёт тихо. Сброс на on_game_load / on_game_end.

**Причина**


eturn nil срывал создание stash-задания. N=8: хватает, чтобы отвести горстку stray anom в caches, без лишних orig-проходов на каждую выдачу.

**Не затронуто**

- Логика спота после set_random_stash, refresh на first_update.

## [1.0.0] - 2026-09-20

**Изменено**

- `gamedata/scripts/z_fix_quest_stash_hint.script` - monkey-patch:
  - после `treasure_manager.set_random_stash` для bonus с `drx_sl_quest_item_*` гарантирует `map_add_object_spot_ser(..., "treasure")`, если спота ещё нет;
  - `get_random_stash(..., inv_box=true)` не отдаёт `anom_inv_stash` / `hidden_anom_stash`;
  - на `actor_on_first_update` обновляет споты активных stash-заданий с `stash_created`.

**Причина**

Ветка B: в диалоге локация уже есть (`give_talk_message2` / `st_location`), после взятия маркер не появляется. В профиле Standart включены Grok (своя `set_random_stash` + `map_add_object_spot_ser`) и Anomalous Stash (`anom_inv_stash` в пуле inv_box).

**Как исправлено**

Не заменяем файлы Grok/Anomalous. Спот ставится тем же API после их `set_random_stash`. Ветка A (текст локации при оффере) не трогалась.

**Не затронуто**

- Тексты оффера / `give_talk_message2`
- `spawn_local`, награды, типы КПК 1001-1038 (это `fix_quest_stash`)
- PDA taskboard sync

**Совместимость**

- Сейвы: без миграции
- MO2 ниже Grok и Anomalous; после `fix_quest_stash` допустимо
- Stash_ID_Desync в профиле Standart не включён

**Проверено**

- lint: `python tools/lint_addon.py fix_quest_stash_hint`
- в игре: не прогонялось. Ожидание: взять documents/stash у НПС - локация в диалоге (как раньше), после принятия метка treasure на ящике, предмет находится.
