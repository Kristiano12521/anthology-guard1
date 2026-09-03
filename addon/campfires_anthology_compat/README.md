# [FIX] Campfires Anthology Compat

Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT.

Совместимый пак **Campfires Placeable** для Anthology: те же костры, без полной подмены `configs\models\dynamic_objects.ltx`.

## Установка

1. **Выключить** оригинал `[GAM] Campfires_placeable_ANTHOLOGY_CreditsBVCX` (и любую старую копию Compat с `1_campfires_*.ltx` / полным `dynamic_objects.ltx`).
2. Поставить этот мод отдельно — **не** входит в `[DBG] Kristiano Fixes ALL IN ONE`.
3. В MO2: после Anthology и после `[GAM] The Anomalous Stash`, до `[QUE]`.
4. Новая игра не обязательна.

## Что внутри

| Файл | Назначение |
| --- | --- |
| `mod_system_campfires_anthology_compat.ltx` | DLTX: `@[ph_campfiremod]` (создать, если нет) |
| `items_campfire.ltx`, скрипты, меш, текстуры, звук, PPE, строки | механика костров как у апстрима |

## Чего нет намеренно

- Полной `dynamic_objects.ltx` (она вырезала `okr_a5_ph_pda` и соседние секции Anthology).
- Замены `trader_autoinject.script` — сток костров уже через monkey-patch в `campfire_placeable.script`; подмена ломала `trader_on_restock` (barter / exo_loot). При активном Campfires-оригинале с вырезанным callback по-прежнему нужен `fix_trader_restock_callback` / BHS; этот пак ванильный `trader_autoinject` не трогает.

## Проверка

1. Старт / загрузка сейва без FATAL по `dynamic_objects`.
2. Рубка дров топором → предмет костра → установка на ровной поверхности.
3. Переход «Кордон»: PDA/ящики Okrest (`okr_a5_ph_*`) на месте, без `Cannot find item with section okr_a5_ph_pda`.
4. В логе нет duplicate section на `ph_campfiremod`.

## Кредиты

Механика и ассеты — community-мод Campfires Placeable (ANTHOLOGY / CreditsBVCX). Совместимость с Anthology DLTX — этот пак.
