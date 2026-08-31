# Aim Fatigue Visibility Fix

## [1.0.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; `printf` с причиной при раннем выходе из `install()`.

**Не затронуто**

- Логика патча `on_option_change` / `load_state`, колбэки, MCM.

## [1.0.0] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_aim_fatigue_visibility.script` — monkey-patch `aim_stamina.on_option_change` и `aim_stamina.load_state`: после оригинала три булева флага перечитываются из MCM без сломанного `as_bool`.

**Причина**

В MCM Aim Fatigue чекбоксы «Показывать счётчик усталости прицела» и «Показывать полосу усталости прицела» визуально снимаются, HUD продолжает рисовать оба элемента.

`aim_stamina.script` читает чекбоксы через

`return type(value) == "boolean" and value or fallback`

В Lua `a and b or c` при `b == false` всегда даёт `c`. MCM (`val = 1`) возвращает настоящий boolean, поэтому `false` превращается в fallback `true`. `aim_stamina_hud:Update()` сравнивает флаги верно — ломается только источник значений.

Тот же хелпер стоит на `AS_disable`: debug-режим можно включить, выключить после включения нельзя.

ZIP `Aim Fatigue Visibility Fix` регистрировал те же колбэки, что и оригинал, и надеялся победить по алфавиту имени файла. `as_bool` локальный, снаружи не патчится. Колбэки не снимались, `AS_disable` не трогали.

**Как исправлено**

Оригинал не подменяется. Обёртка вызывает штатные `on_option_change` / `load_state`, затем пишет `show_AS_counter`, `show_AS_bar`, `AS_disable` из `aim_stamina_mcm.get_config`. Если Aim Fatigue уже успел зарегистрировать сырые функции, они снимаются и вместо них ставится обёртка (`RegisterScriptCallback` хранит ссылку, не имя). Повтор на `actor_on_first_update` закрывает top-level init, который тоже идёт через `as_bool`.

**Не затронуто**

- `aim_stamina.script`, `aim_stamina_mcm.script`, HUD XML, текстуры, анимации sway
- дренаж / восстановление стамины, режимы AS, позиции HUD, таймер скрытия
- логика `aim_stamina_hud:Update()`
- MCM-меню Aim Fatigue

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT / [HARD] Aim Fatigue
- Сейвы: без миграции. Ключи те же; `load_state` в конце всё равно зовёт `on_option_change` и читает MCM
- В MO2 ниже `[HARD] Aim Fatigue`. ZIP Visibility Fix выключить — он только дублирует колбэки

**Проверено**

- lint: `python tools/lint_addon.py fix_aim_fatigue_visibility`
- В игре: не прогонялось. Снять оба чекбокса HUD в MCM Aim Fatigue → счётчик и полоса должны пропасть сразу, без перезахода. В логе: `wrapped on_option_change and load_state`.
