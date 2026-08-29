# Radio Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_radio.script` — monkey-patch `getFS():file_list_open` / `placeable_radio_wrapper.__init`, `ph_idle.action_idle` (hit/use/update), `ph_sound.snd_source` (hit/use/update), `xr_effects.play_sound`.
- `gamedata/configs/text/eng|rus/st_fix_radio.xml` — подсказка use на приёмниках.

**Причина**

ZIP `Hideout_Furniture_Placeable_Radio_Fix` 1.0.3 подменял весь `placeable_radio.script`, оставлял только две ванильные станции и клал свой `track_21.ogg`. Оригинал HF берёт каналы из `plugins/placeable_radio/base.ltx` (включая extended) и перечисляет папку через `file_list_open`. В MO2 в список попадают лишние файлы, не `.ogg` — `sound_object()` на них ломает плейлист.

Мировые приёмники: опция `sound/radio/zone` читается только в `ph_sound` (21 объект, Zone FM). 58 баз/ноутов идут через `ph_idle` + `play_sound` и опцию игнорируют. У `ph_sound` `no_hit` по умолчанию true. У `ph_idle` выстрел срабатывает только на кость 2. `on_use` нет.

**Как исправлено**

- Для путей `$game_sounds$` с `radio` в имени: `file_list_open` отдаёт только `*.ogg`, иначе `track_N` / `session_N` через `getFS():exist`. Оригинал HF не подменяется.
- `play_sound` и апдейт `ph_idle`/`ph_sound` смотрят `sound/radio/zone` (true / 1 / "true").
- Выстрел по radio/notebook/laptop: любой bone, если в LTX есть `hit_on_bone`; у `ph_sound` игнорируется `no_hit`.
- Use переключает `ph_idle@music` ↔ `ph_idle@broken` или флаг `destructed` у Zone FM.

**Не затронуто**

- `placeable_radio.script`, `ui_pda_radio_tab.script`, плейлисты PDA
- LTX логики объектов, `all.spawn`
- Громкость, каналы, `no_hit` у не-радио `ph_sound`
- Сохраняемые таблицы мода (своего `save_state` нет; `destructed` и секция логики — как в ванили)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 ниже [HF] Hideout Furniture. ZIP Placeable Radio Fix выключить и вернуть оригинальный `placeable_radio.script`

**Проверено**

- lint: `python tools/lint_addon.py fix_radio`
- В игре: не прогонялось. Ожидаемый лог: `[fix_radio] loaded v1.0.0`, при удачном wrap ещё `wrapped file_list_open`. Свалка, депо: опция Radio Zone глушит радио и ноут; use и выстрел выключают. HF-радио: станции из `radio_extended.ltx` на месте, без чужих файлов в плейлисте.
