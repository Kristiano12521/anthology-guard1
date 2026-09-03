# Campfires Anthology Compat

## [1.1.0] — 2026-09-03

**Изменено**

- `gamedata/configs/mod_system_campfires_anthology_compat.ltx` — вместо `1_campfires_anthology_compat.ltx`: имя `mod_system_*`, чтобы DLTX подхватил патч рядом с `system.ltx`; `@[ph_campfiremod]` без ключа `override = false`.
- Удалён `gamedata/scripts/trader_autoinject.script` — полная замена больше не входит в пак.
- `campfire_placeable.script` — presence `printf`, `on_game_end` с `UnregisterScriptCallback`, комментарии `-- alife-scan` на двух полных проходах id.
- Репозиторий: `addon/campfires_anthology_compat/` (`vendor_fork` → `[GAM] Campfires_placeable_ANTHOLOGY_CreditsBVCX`); отдельный мод от Kristiano AIO (`SEPARATE` в `_pack_kristiano_aio.py`).

**Причина**

1. Файл `1_*.ltx` не матчит шаблон DLTX `mod_<root>_<suffix>.ltx` — секция `ph_campfiremod` могла не попасть в ini. `override = false` в README Modded Exes — пример обычного ключа, не директива; связка `@[sec]` + `[sec]` давала риск duplicate base.
2. Сток костров уже вешается monkey-patch’ем в `campfire_placeable.script`. Копия Campfires `trader_autoinject` вырезала `trader_on_restock`, убирала дистанционный guard Сидора/Лесника и содержала `return default` при мёртвом NPC.

**Как исправлено**

DLTX-мост `mod_system_*` с одной новой секцией; ванильный / сборки `trader_autoinject` не перекрывается.

**Не затронуто**

- `items_campfire.ltx`, `campfire_placeable(.mcm).script`, `ph_campfiremod.ltx`, меш/текстуры/звук/PPE/строки
- файлы `fix_trader_restock_callback`, BHS, barter, exo_loot
- сохраняемое состояние (`se_anoms` / `prev_level` как у апстрима)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции; старый сейв с уже поставленными кострами читается тем же `load_state`
- Конфликты: взаимоисключающе с оригинальным `[GAM] Campfires_*` и со старым Compat, где есть `dynamic_objects.ltx` или `trader_autoinject.script`
- Не входит в `[DBG] Kristiano Fixes ALL IN ONE` — отдельный zip / слот MO2

**Проверено**

- lint: прогон после правки
- В игре: не прогонялось агентом (нужны установка костра + переход Кордон / `okr_a5_ph_pda`)
