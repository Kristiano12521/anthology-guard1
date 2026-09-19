# Sound Object Missing Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 после Anthology base; порядок относительно sound-модов не важен (патч на API) после `aaa_sound_object_patch`: проверка `getFS():exist("$game_sounds$", path.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.2] - 2026-09-16

**Изменено**

- `gamedata/scripts/fix_sound_object_missing.script` — stub с полным no-op API (`play_no_feedback`, `stop_deffered`, `attach_tail`, `get_position`, `frequency` / `min_distance` / `max_distance` + `__index` на неизвестные методы). `get_safe_sound_object` на missing тоже возвращает stub, не `nil`. Stub кэшируется по path. Второй аргумент конструктора (`s2d`/`s3d`) пробрасывается в реальный ctor.

**Причина**

v1.0.1 закрыл CTD ambient, но `get_safe` + `:play_no_feedback` (как в `xr_effects`) падал бы на missing file: ваниль отдаёт объект, мы отдавали `nil`. Неполный stub и новый table на каждый skip — лишний риск и GC в `sound_ambient` (`playing()` всегда false).

**Не затронуто**

- `aaa_sound_object_patch.script`
- сами `.ogg` / sound-моды
- пустые слоты в `sounds=` каналов (корневой конфиг не чистим)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим, состояние не пишется

**Проверено**

- lint: `python tools/lint_addon.py fix_sound_object_missing`
- в игре: не подтверждено. Ожидание: нет CTD ambient; нет SCRIPT ERROR на `get_safe`+`play_no_feedback` для missing path; разовые `skip missing sound path=...`.

## [1.0.1] - 2026-09-16

**Изменено**

- `gamedata/scripts/fix_sound_object_missing.script` - при отсутствии `.ogg` proxy `sound_object(path)` возвращает no-op stub (`play` / `play_at_pos` / `stop` / `playing` / `volume`), а не `nil`. `xr_sound.get_safe_sound_object` по-прежнему возвращает `nil`. Счётчики в логе через `%s` (printf сборки не подставлял `%d`).

**Причина**

v1.0.0 возвращал `nil` из конструктора. Ванильный `sound_ambient.script:146` делает `ch.snd:play_at_pos` без проверки ? CTD (`attempt to index field 'snd'`). В логе перед падением: `skip missing sound path=` (пустой слот в канале).

**Как исправлено**

Конструктор снова всегда даёт объект; тихий stub вместо C++ `super` на битый путь. Safe-API без изменений.

**Не затронуто**

- `aaa_sound_object_patch.script`, кэш `soundCache`
- сами `.ogg` / sound-моды
- `get_safe_sound_object` (nil при отсутствии файла)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим, состояние не пишется

**Проверено**

- lint: `python tools/lint_addon.py fix_sound_object_missing`
- в игре: не подтверждено. Ожидание: нет CTD в `sound_ambient` на missing/empty path; в логе разовые `skip missing sound path=...` с числами unique/total.

## [1.0.0] - 2026-09-15

**Изменено**

- `gamedata/scripts/fix_sound_object_missing.script` - proxy на `_G.sound_object` и обёртка `xr_sound.get_safe_sound_object`: если `.ogg` нет в `$game_sounds$`, конструктор не вызывается, возвращается `nil`. Каждый отсутствующий путь логируется один раз.

**Причина**

Недостающие файлы (`sound_revamp\fireflies\*.ogg`, `tb_growls\tb_lurk_*.ogg` и т.п.) дают спам `File not found` + `aaa_sound_object_patch.script(18) : super` (x17 в логе mg9000). Это шум, не CTD.

**Как исправлено**

Monkey-patch после `aaa_sound_object_patch`: проверка `getFS():exist("$game_sounds$", path .. ".ogg")` до `super`/`sound_object(path)`. Ассеты не восстанавливаются - только заглушка спама.

**Не затронуто**

- `aaa_sound_object_patch.script`, кэш `soundCache`
- сами `.ogg` / sound-моды
- `stop_hud_motion` / FDDA
- travel / `alife_object`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: совместим, состояние не пишется
- В MO2 после Anthology base; порядок относительно sound-модов не важен (патч на API)

**Проверено**

- lint: `python tools/lint_addon.py fix_sound_object_missing`
- в игре: не подтверждено. Ожидание: нет кадров `aaa_sound_object_patch.script(18) : super`; в логе разовые `skip missing sound path=...`.
