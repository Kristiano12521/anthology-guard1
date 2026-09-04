# Changelog: fix_localization_reload

## 1.0.0 — 2026-09-04

- Monkey-patch `ui_options.func_localization`: при смене языка в главном меню (когда `level` ещё нет) вызывается `SendScriptCallback("on_localization_change")`.
- Подписка на `on_localization_change`: `ui_item.refresh_strings`, сброс кэшей `get_sec_*` через sentinel, обновление `ui_inventory.st_perc`.
- Monkey-patch `ui_item.item_name` / `item_description`: сборка через `build_*` без `last_*_id`, чтобы смена языка не отдавала старый перевод.

Не затронуто: string table XML, оружейные LTX, MCM, сохраняемое состояние.
