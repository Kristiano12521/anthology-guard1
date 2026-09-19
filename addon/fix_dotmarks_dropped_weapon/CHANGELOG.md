# DotMarks Dropped Weapon Marker Fix

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; После MT reload снова возможен prompt «ЗАБРАТЬ» на своём стволе.

**Удаление**

- Отключить слот в MO2; новая игра не нужна.
- Сейв не затрагивается. Без фикса исходный баг или CTD может вернуться.

## [1.0.3] — 2026-09-19

**Изменено**

- Monkey-patch re-wrap: больше не обнуляет `orig_*` перед `install()` на `actor_on_first_update`.
- `wraps_ok` требует живой `orig`; вызовы оригинала под nil-guard.

**Причина**

Обнуление всех `orig` при частичном сбое wrap оставляло уже наш патч с `orig == nil` → CTD (как `fix_sim_mechanic_trade` / xray_korisnik).

**Не затронуто**

- Игровая логика патча, сейвы, DLTX

**Проверено**

- lint: `python tools/lint_addon.py fix_dotmarks_dropped_weapon`
- в игре: не прогонялось

## [1.0.2] — 2026-09-17

**Изменено**

- `fix_dotmarks_dropped_weapon.script` — на `actor_on_first_update` переустанавливает wrap, если слоты DotMarks уже не наши; `callbacks_registered`; uninstall только если указатель ещё наш.

**Причина**

1.0.1 при `installed=true` не сверял указатели. После MT reload снова возможен prompt «ЗАБРАТЬ» на своём стволе.

**Не затронуто**

- Семантика unhide только для оружия

**Проверено**

- lint: `python tools/lint_addon.py fix_dotmarks_dropped_weapon`
- в игре: не прогонялось

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке.

**Не затронуто**

- Патч DotMarks, guard-сообщения в `install()`.

## [1.0.0] — 2026-08-28

**Изменено**

- `gamedata/scripts/fix_dotmarks_dropped_weapon.script` — monkey-patch `ui_hud_dotmarks.setup_marker_for_object` и `main_marker_update_loop`: оружие убирается из `cfg.dropped_items` до ветки `hide_dropped_items`.

**Причина**

Ствол с трупа получает Dot Mark. После «подобрал → выкинул сам» метки нет, но наведение всё ещё даёт «ЗАБРАТЬ ПРЕДМЕТ (F)».

`actor_on_item_drop` пишет любой выброс игрока в `dropped_items`. Дефолт `hide_dropped_items = true` (MCM Advanced, `axr_options.ltx`) прячет маркер. Лут с NPC в эту таблицу не попадает — поэтому светится, пока его не трогать.

**Как исправлено**

Monkey-patch, не DLTX: чекбокс MCM у игрока уже сохранён как `true`, смена дефолта в `dotmarks_defaults.ltx` на текущем профиле ничего не даст. Глобально выключать hide-dropped нельзя — засветятся кучи хлама на базе. Исключение только для `IsWeapon` / `mark.is_weapon`.

**Не затронуто**

- сам `ui_hud_dotmarks.script`, `dotmarks_defaults.ltx`, MCM DotMarks
- прятание выброшенных аптечек, патронов, болтов, еды
- `blacklist_dropped_items`, ванильный quickhelp «ЗАБРАТЬ ПРЕДМЕТ»
- BHS-гард `ui_inventory.start`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT / Interaction Dot Marks 1.7.1
- Сейвы: без миграции. `dropped_items` в сейве DotMarks не ломается: id стволов просто перестают считаться «выброшенными игроком», как только маркер их видит
- Конфликты: нет пересечения файлов; в MO2 ниже сборки и ниже DotMarks / Anthology Performance merged

**Проверено**

- lint: `python tools/lint_addon.py fix_dotmarks_dropped_weapon`
- В игре: не прогонялось. Убить NPC → ствол с меткой → подобрать → выкинуть рядом → метка должна вернуться. В логе: `wrapped setup_marker_for_object and main_marker_update_loop`.
