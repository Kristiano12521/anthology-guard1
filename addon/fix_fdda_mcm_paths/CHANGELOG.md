# fix_fdda_mcm_paths

## 1.0.0 (2026-09-02)

- DLTX-патч `mod_dotmarks_defaults_fix_fdda_mcm_paths.ltx`: в секции `[mcm_paths]` DotMarks перенаправляет `fdda_anims_enabled` и `fdda_pickup_anim` с мёртвых путей `EA_settings/*` на зарегистрированные в `liz_fdda_redone_mcm.script` (`fddar/consumables/enable`, `fddar/pickup/enable`).
- `fix_fdda_mcm_paths_presence.script`: presence-строка `[fix_fdda_mcm_paths] loaded v…` для `xraylog --mine` (DLTX сам по себе в лог не пишет).
- Ожидаемый эффект в логе: исчезают 12 строк `!MCM given bad path:EA_settings/...` от DotMarks за сессию; `cfg.fdda_*` читают реальные значения FDDAR вместо дефолта `false`.

### Проверка в игре (ручная)

- В логе нет `!MCM given bad path:EA_settings/enable_animations` и `.../take_item_anim` от DotMarks.
- Pickup-анимации DotMarks согласованы с MCM FDDA Redone → Pickup → Enable.

### Подтверждено замером — 2026-09-02

Сессия `logs/xray_nikit.log`, 02.09.2026 12:17–13:00. Первый мод, подтверждённый не по строке `loaded`, а по фактическому значению в рантайме.

Команды (`run_string` в консоли):

```lua
printf("[fdda_probe] LTX anims=%s", ini_file_ex("scripts\\dotmarks_defaults.ltx"):r_string_ex("mcm_paths","fdda_anims_enabled") or "nil")
printf("[fdda_probe] LTX pickup=%s", ini_file_ex("scripts\\dotmarks_defaults.ltx"):r_string_ex("mcm_paths","fdda_pickup_anim") or "nil")
printf("[fdda_probe] cfg path anims=%s pickup=%s", tostring(ui_hud_dotmarks.cfg.mcm_paths.fdda_anims_enabled), tostring(ui_hud_dotmarks.cfg.mcm_paths.fdda_pickup_anim))
printf("[fdda_probe] resolved anims=%s pickup=%s", tostring(ui_hud_dotmarks.cfg.fdda_anims_enabled), tostring(ui_hud_dotmarks.cfg.fdda_pickup_anim))
```

Результат:

| Замер | Значение |
| --- | --- |
| LTX `fdda_anims_enabled` | `fddar/consumables/enable` |
| LTX `fdda_pickup_anim` | `fddar/pickup/enable` |
| `cfg.mcm_paths.*` | `fddar/consumables/enable` / `fddar/pickup/enable` |
| `cfg.fdda_*` resolved | `true` / `true` |

DLTX-патч применился, DotMarks читает `mcm_paths`, MCM-пути резолвятся в bool.

Оставшиеся 28 строк `!MCM given bad path:EA_settings/...` в том же окне — не DotMarks: прямые вызовы `ui_mcm.get("EA_settings/...")` из INERTIA Expanded, Glowsticks и BHS Injuries.
