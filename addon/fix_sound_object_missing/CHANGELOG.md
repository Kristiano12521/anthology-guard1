# Sound Object Missing Guard

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
