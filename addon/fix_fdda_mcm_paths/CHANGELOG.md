# fix_fdda_mcm_paths

## 1.0.0 (2026-09-02)

- DLTX-патч `mod_dotmarks_defaults_fix_fdda_mcm_paths.ltx`: в секции `[mcm_paths]` DotMarks перенаправляет `fdda_anims_enabled` и `fdda_pickup_anim` с мёртвых путей `EA_settings/*` на зарегистрированные в `liz_fdda_redone_mcm.script` (`fddar/consumables/enable`, `fddar/pickup/enable`).
- `fix_fdda_mcm_paths_presence.script`: presence-строка `[fix_fdda_mcm_paths] loaded v…` для `xraylog --mine` (DLTX сам по себе в лог не пишет).
- Ожидаемый эффект в логе: исчезают 12 строк `!MCM given bad path:EA_settings/...` от DotMarks за сессию; `cfg.fdda_*` читают реальные значения FDDAR вместо дефолта `false`.

### Проверка в игре (ручная)

- В логе нет `!MCM given bad path:EA_settings/enable_animations` и `.../take_item_anim` от DotMarks.
- Pickup-анимации DotMarks согласованы с MCM FDDA Redone → Pickup → Enable.
