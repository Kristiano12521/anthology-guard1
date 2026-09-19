# Radio Fix

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 в список попадают лишние файлы, не ` после `@broken` у Сидоровича `scheme` становился `nil`, tip пропадал).

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.7] — 2026-09-18

**Изменено**

- `gamedata/scripts/fix_radio.script` — для `ph_idle` use больше не переключает `music`↔`broken` (после `@broken` у Сидоровича `scheme` становился `nil`, tip пропадал). Мьют: `stop_sounds_by_id` + `bag._fix_radio_muted`; вкл: `xr_effects.play_sound` по теме из `on_info`. Recovery через `activate_by_section` если scheme nil. Toggle в `physic_object_on_use_callback` (и для nil scheme).

**Причина**

Diag: `esc_sidorovich_radio` в игре на `ph_idle@music`, не `ph_sound`. Первый use → `@broken` → через секунду `scheme=nil` → tip/use по схеме мертвы.

**Не затронуто**

- Hit → `@broken` по `hit_on_bone`
- Zone FM (`ph_sound`) volume-mute
- HF placeable

**Проверено**

- lint / деплой
- в игре: ждать `[fix_radio] idle use: esc_sidorovich_radio muted=... scheme=ph_idle`

## [1.0.6] — 2026-09-18

**Изменено**

- `gamedata/scripts/fix_radio.script` — toggle Zone FM (`ph_sound`) через `physic_object_on_use_callback`, а не через добавление `snd_source.use_callback` (у ванили метода нет, lookup ненадёжен). Мьют по-прежнему `volume = 0`. В лог пишется `use: ... muted=...`. На экране краткое `Radio: ON/OFF`.

**Причина**

1.0.5 грузился без Lua-ошибок, но use не давал стабильного эффекта: патч несуществующего `use_callback` на классе мог не вызываться. Binder всегда шлёт `physic_object_on_use_callback`.

**Не затронуто**

- `ph_idle` use (секции music/broken), hit, зона, HF

**Проверено**

- lint / деплой в MO2 pack
- в игре: ждать `[fix_radio] use: esc_sidorovich_radio muted=...` при каждом use

## [1.0.5] — 2026-09-18

**Изменено**

- `gamedata/scripts/fix_radio.script` — use у `ph_sound` больше не трогает `destructed` и не делает `:stop()`; мьют через `_fix_radio_muted` + `volume = 0` (как vasgen_fairy_radio). После orig-update мьют накладывается снова. Старый `destr` от use 1.0.x сбрасывается одним use. Tip снова через `translate_string`.

**Причина**

1.0.4 грузился (лог), но выкл/вкл у Сидоровича всё равно ломал звук и надпись: `stop` по Zone FM `*_out` + `destructed` не давали стабильно включить снова.

**Не затронуто**

- Hit → сломать (`destructed`), зона, HF, `ph_idle`
- Сейвы: миграции таблицы нет; застрявший `destr` от старого use снимается кликом

**Проверено**

- lint: `python tools/lint_addon.py fix_radio`
- в игре: не подтверждено. Ожидание: выкл/вкл много раз, tip на месте, звук возвращается.

## [1.0.4] — 2026-09-18

**Изменено**

- `gamedata/scripts/fix_radio.script` — захват `ph_sound.use_callback` через флаг `snd_use_captured` (повторный `install` больше не кладёт патч в `orig`); tip всегда id `st_fix_radio_use`; tip обновляется и в `use`.

**Причина**

У Сидоровича (`esc_sidorovich_radio`) после выкл/вкл приёмник молчал и пропадала надпись: `on_game_start` + `actor_on_first_update` дважды ставили use-патч, а tip передавался уже переведённой строкой.

**Не затронуто**

- HF placeable, `ph_idle`, LTX, hit→сломать, опция «Радио Зоны»
- Сейвы без миграции (`destr` как в ванили)

**Проверено**

- lint: `python tools/lint_addon.py fix_radio`
- в игре: не подтверждено. Ожидание: у Сидоровича use выкл/вкл много раз подряд, tip «Включить / выключить» не пропадает, Zone FM снова играет.

## [1.0.3] — 2026-09-17

**Изменено**

- `gamedata/scripts/fix_radio.script` — после use «вкл» и после возврата опции «Радио Зоны» снова ставится `st.sound_set = true` (и `pause_time = 0`). То же для уже застрявших `ph_sound` (сейв после выкл/вкл без армa).

**Причина**

`ph_sound` берёт трек только при `sound_set == true`. Use/зона глушили `played_sound`, но `sound_set` оставался `false` — приёмник (Сидорович и др.) молчал до сброса схемы.

**Не затронуто**

- HF placeable, PDA, `ph_idle` (переключение секций)
- LTX, опции, сейвы без миграции (`destr` как раньше)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим

**Проверено**

- lint: `python tools/lint_addon.py fix_radio`
- в игре: не подтверждено. Ожидание: use вкл у Сидоровича снова запускает Zone FM; выкл/вкл «Радио Зоны» тоже.

## [1.0.2] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке.

**Не затронуто**

- HF proxy, world radios, `install()`.

## [1.0.1] — 2026-08-30

**Изменено**

- Больше не подменяет `FS.file_list_open` на весь процесс. Фильтр `*.ogg` ставится только на время `placeable_radio_wrapper.__init` через временный `getFS()`.

**Причина**

Глобальный wrap ловил `getFS():file_list_open` у WTF (`modxml_wtf.get_dialog_xmls`) на `on_game_start`. Повторный вызов сохранённого C++-метода давал `pure virtual function called` и CTD.

**Не затронуто**

- Мировые приёмники: `sound/radio/zone`, hit/use
- Сам `placeable_radio.script`

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
