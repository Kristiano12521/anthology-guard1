# Gigant Space Restriction Crash Fix

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; в MO2 ниже сборки и `id_cleaner`.

**Удаление**

- Отключить слот в MO2 после выхода в меню с включённым модом (в логе `exit quarantine freed=…`); новая игра не нужна.
- Сессионный карантин (`off_level` / `level_not_ready` / смена уровня) снимается на `on_game_end` — персист `set_switch_online(false)` был побочным эффектом сериализации, не замыслом. Небезопасные (invalid graph / dangling) флаг не трогаем. Сейв на диске с `false` и выключение AIO **без** запуска игры кодом не закрывается. `alife_release` по-прежнему необратим.

## [1.1.3] — 2026-09-26

**Изменено**

- `can_switch_online` вешается на `se_monster.se_monster` (класс из `class_registrator`). Если метод только на таблице скрипта — запасной путь туда.

**Причина**

Прежняя обёртка писала `se_monster.can_switch_online` на таблицу скрипта. Движок зовёт метод вложенного класса `se_monster.se_monster`. Карантин через `set_switch_online` при этом работал; гейт `can_switch_online` — нет.

**Не затронуто**

- Карантин, `set_switch_online`, снятие флагов на `on_game_end`, сейвы

**Проверено**

- `tools/lint_addon.py fix_gigant_space_restriction`
- В игре ещё нет

## [1.1.2] — 2026-09-19

**Изменено**

- `on_game_end`: перед `reset_state` обход `quarantined` — сессионные причины (`off_level`, `level_not_ready`, `on_before_level_changing`, `on_level_changing`, `queued`) получают `set_switch_online(true)`; unsafe (`invalid_game_vertex`, `dangling_*`) оставляем. Одна строка лога: `exit quarantine freed=N kept=M freed_by=… kept_by=…`.
- Версия → 1.1.2.

**Причина**

Карантин задуман как сессионный гейт до `actor_on_first_update` на уровне гиганта; таблица `quarantined` между загрузками пуста, карантин ставится снова на `server_entity_on_register`. `set_switch_online(false)` при этом сериализуется в пакет alife — побочный эффект API, не лечение STATE. На выгрузке флаг не снимался → после снятия AIO гиганты могли навсегда остаться offline.

**Не затронуто**

- Логика `process_one` / `alife_release` unsafe, wrap `can_switch_online`, callback'и входа на уровень
- `uninstall_can_switch_online` — только восстановление указателя метода; CSE не трогает (проход только в `on_game_end`)
- `verified_*`

**Ограничение**

Патч помогает, только если последняя сессия с включённым модом/пакетом дошла до выгрузки (`on_game_end`). Уже лежащий на диске сейв с `false` и выключение слота без запуска — по-прежнему дыра.

**Проверено**

- lint: `python tools/lint_addon.py fix_gigant_space_restriction`
- В игре: не прогонялось агентом. Ожидание: зайти → уйти с уровня гигантов → меню → в логе `exit quarantine freed=…`

## [1.1.1] — 2026-08-31

**Изменено**

- Только логирование: безусловная presence-строка при загрузке; `printf` с причиной при раннем выходе из `install_can_switch_online()`.

**Не затронуто**

- Карантин гигантов, колбэки, таймеры.

## [1.1.0] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_gigant_space_restriction.script` — карантин больше не завязан на чтение CSE-строк рестрикторов. Гигант на чужой локации и offline-гигант на текущей не идут online до `actor_on_first_update` на их уровне. Уход с локации (`on_before_level_changing` и `on_level_changing`) снова сажает текущих гигантов в карантин. Висячие клиентские рестрикторы / битая вершина графа / мёртвый smart — `alife_release`, пока объект offline.

**Причина**

ZIP `Anthology_DeadCity_Gigant_Repair_id24062` удалял ALife id `24062`. Это тот же класс краша, что и Припять/`40604`: повторный вход (МГ → сосед → обратно) валит `CPseudoGigant::reinit` / `CSpaceRestrictionBridge::initialized`. Прямая загрузка сейва уже в МГ проходит. Числовой id после `id_cleaner` бессмысленен.

v1.0.0 промахивался по этому репро: `m_out_space_restrictors` / `m_in_space_restrictors` нет в Lua (`lua_help`), online-гигант помечался `processed` и больше не трогался, `server_entity_on_register` при возврате не стреляет.

**Как исправлено**

Числовые id по-прежнему не используются. Wrap `se_monster.can_switch_online` не перехватывает setter (`can_switch_online(boolean)`). Рестрикторы снимаются только через `alife():remove_all_restrictions(id, 4/5)` и клиентский `game_object:remove_all_restrictions()`, и только если имена из `out/in_restrictions()` не находятся в ALife. CSE STATE не пишется. Тика `actor_on_update` нет.

**Не затронуто**

- остальные мутанты и сталкеры
- здоровые гиганты: после `first_update` на их уровне снова online
- `all.spawn`, LTX секций гиганта, `id_cleaner_anthology`
- сохраняемые таблицы мода (своего `save_state` нет)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции и без новой игры
- В MO2 ниже сборки и `id_cleaner`. Выключить ZIP `Anthology_Central_Pripyat_Gigant_Save_Repair_v1.0.1`, `anthology_pripyat_gigant_repair.script` в `[DBG] Kristiano Fixes ALL IN ONE` и `Anthology_DeadCity_Gigant_Repair_id24062`

**Проверено**

- lint: `python tools/lint_addon.py fix_gigant_space_restriction`
- В игре: не прогонялось. Загрузить сейв в Мёртвом городе или на Центральной Припяти, уйти на соседа и вернуться. Ожидание в логе: `quarantine` на уходе, `safe` или `release` на соседе / по возврату, без FATAL `CPseudoGigant::reinit`

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/scripts/fix_gigant_space_restriction.script` — карантин псевдогиганта до клиентского спавна (`set_switch_online(false)` + wrap `se_monster.can_switch_online`), затем снятие битых space restriction и возврат online, либо `alife_release`.

**Причина**

Повторный вход на локацию с живым псевдогигантом даёт FATAL в `CPseudoGigant::reinit` / `CSpaceRestriction`. Клиентский объект собирается в `CRestrictedObject::net_Spawn`: туда копируются `m_out_space_restrictors` / `m_in_space_restrictors` и вызывается `space_restriction_manager().restrict()`. Lua-биндер гиганта ещё не жив, `actor_on_first_update` опаздывает.

ZIP `Anthology_Central_Pripyat_Gigant_Save_Repair_v1.0.1` удалял ALife id `40604`. Это id конкретного сейва. `id_cleaner_anthology` переназначает номера: в `xray_user.log` на 40604 уже `conserva`, в другом логе — `lights_hanging_lamp`. Скрипт каждый раз писал `safety block` и ничего не чинил. Для Мёртвого города тот же краш требовал другой id (`24062`).

**Как исправлено**

Числовые id не используются. Отбор по секции `gigant*` / `clsid.gigant_s`. На `server_entity_on_register` гигант на текущей локации с непустыми static-restrictor строками, битой `m_game_vertex_id` или мёртвым `m_smart_terrain_id` не допускается online. После регистрации ALife скрипт чистит dynamic restrictions (`remove_all_restrictions` in/out = 4/5) и пытается обнулить static-строки в CSE. Если строки недоступны или вершина графа битая — объект снимается через `alife_release`, пока он ещё offline. Повтор на `on_before_level_changing`. Тика `actor_on_update` нет.

**Не затронуто**

- остальные мутанты и сталкеры
- здоровые гиганты без static-restrictor строк и с живой вершиной графа
- `all.spawn`, LTX секций гиганта, `id_cleaner_anthology`
- сохраняемые таблицы мода (своего `save_state` нет: вылеченная CSE STATE уходит в сейв сама)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции и без новой игры
- В MO2 ниже сборки и `id_cleaner`. ZIP `Anthology_Central_Pripyat_Gigant_Save_Repair_v1.0.1`, `anthology_pripyat_gigant_repair.script` в `[DBG] Kristiano Fixes ALL IN ONE` и `Anthology_DeadCity_Gigant_Repair_id24062` выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_gigant_space_restriction`
- В игре: не прогонялось. Загрузить сейв, который падал на Центральной Припяти или Мёртвом городе. Ожидание в логе: `quarantine` затем `safe` или `release`, без FATAL `CPseudoGigant::reinit`
