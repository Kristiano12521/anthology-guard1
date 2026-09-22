# Campfires Anthology Compat

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; выключить [GAM] Campfires_* и старый Compat.

**Совместимость:** пакет Campfires без полной `dynamic_objects.ltx` — ключевые пути `configs/mod_system_campfires_anthology_compat.ltx`, `configs/items/items/items_campfire.ltx`, `configs/scripts/ph_campfiremod.ltx`, `scripts/campfire_placeable.script`. Взаимоисключающе с `[GAM] Campfires_*` и старым Compat (`dynamic_objects.ltx` / `trader_autoinject.script`). При совпадении путей с другим модом нужен патч или ручное слияние.

**Удаление**

- Отключить слот в MO2. Если костры уже ставили — сначала уберите/сожгите их при включённом моде, затем отключайте.
- Сейв хранит `se_anoms` / `prev_level` и alife-объекты `ph_campfiremod`. Без мода секции пропадут: missing section, «висячие» объекты. Без поставленных костров — безопасно.

## [1.1.3] — 2026-09-22

**Изменено**

- `meta.ini`: `vendor_omit=` для осознанных пропусков относительно placeable-оригинала (FORK-001):
  - `scripts/trader_autoinject.script` (+ `.mohidden`) — полная замена ломала `trader_on_restock`; сток через monkey-patch в `campfire_placeable.script`
  - `configs/models/dynamic_objects.ltx` — форк как раз без ломки Anthology-секций
  - `configs/mod_system_campfires_placeable_anthology.ltx` — заменён на `mod_system_campfires_anthology_compat.ltx` (имя `mod_system_*` + `@[ph_campfiremod]`)

## [1.1.2] — 2026-09-17

**Изменено**

- `campfire_placeable.script` — удаление костров на load / смене уровня через `alife():iterate_objects`; полный `1..65534` только как fallback с `-- alife-scan`; collect-then-release (не `alife_release` внутри iterate).

**Причина**

1.1.1 гонял два полных id-скана через `alife_object` — хитч (LUA-008).

**Не затронуто**

- MT re-wrap `trader_autoinject.update`, DLTX, ray place

**Проверено**

- lint: `python tools/lint_addon.py campfires_anthology_compat` — LUA-008 снят
- в игре: не прогонялось

## [1.1.1] — 2026-09-17

**Изменено**

- `campfire_placeable.script` — `wraps_ok` для `trader_autoinject.update`; на `actor_on_first_update` переустанавливает wrap, если модуль уже не наш; always re-capture; uninstall только если указатель ещё наш.

**Причина**

1.1.0 ставил wrap при загрузке скрипта через глобальный `TraderAuto`. После MT reload сток дров у торговцев мог пропасть.

**Не затронуто**

- DLTX `ph_campfiremod`, механика костров, сейвы

**Проверено**

- lint: `python tools/lint_addon.py campfires_anthology_compat`
- в игре: не прогонялось

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
