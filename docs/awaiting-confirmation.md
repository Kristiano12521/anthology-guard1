# Сигнатуры, ожидающие подтверждения

Список FATAL/Lua-строк из **чужих** логов (Discord-скрины, чужой paste), по которым собран гард, но у нас в `logs/` / `logs/cards/` этой сигнатуры нет и сами мы её не воспроизводим.

**Зачем:** при разборе присланного лога (`/logfull`, `/crash`) сверить карточку с этим списком. Встретилась ожидаемая сигнатура — этот лог годится, чтобы проверить соответствующий гард/мод.

**Как пользоваться**

| В логе | Смысл |
| --- | --- |
| Есть строка из колонки «Искать» | Этот отчёт — материал для подтверждения указанного мода/гарда |
| Строки нет | Этот лог **не** подтверждает и **не** опровергает гард (сценарий не попал) |
| Мод установлен (`--mine` / presence), FATAL из «Искать» **есть** | Гард не сработал или не та версия — разбирать |
| Мод установлен, FATAL из «Искать» **нет**, есть `skip` / `wrapped` мода | Сценарий, скорее всего, закрыт — отметить подтверждение в CHANGELOG мода и убрать позицию отсюда |

Источник отбора: `addon/*/CHANGELOG.md`, где явно сказано, что сигнатура из чужого лога / Discord-скринов и у нас в cards её нет. Пройден весь `addon/` (2026-09-20): кроме двух модов ниже таких пометок нет.

Сейчас **9** позиций (порог «нужна другая форма» — больше 20).

---

## `fix_nil_crash_guards` — 8 гардов

Общий источник: Discord-скрины, пачка август 2026 (`IMG-20260807…` и соседние кадры). Разбор 2026-09-13 → [issue] Discord nil-FATAL пакет. Авторы скринов в разборе **не зафиксированы**. Карточек в `logs/cards/` нет — только скрины. Presence `wrapped` / `loaded` подтверждает установку обёртки, не отсев FATAL.

Подробности: `addon/fix_nil_crash_guards/CHANGELOG.md` [1.1.0], `docs/issues.md`.

### 1. `GUARD_ITEM_KNIFE` — crow / knife

| | |
| --- | --- |
| **Искать** | `bind_crow` и рядом `item_knife` / `get_condition`; типично сравнение с числом при `nil` (кадр: `bind_crow` ~`:46`) |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, пачка авг 2026; автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять knife-guard на этом логе |

### 2. `GUARD_SEMENOV_TASK` — Semenov / squad nil

| | |
| --- | --- |
| **Искать** | `task_functor` + `yan_ecolog_semenov` / `squad` nil (кадр: `task_functor` ~`:391`) |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка; автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять Semenov-guard (Янтарь) |

### 3. `GUARD_UNREGISTER_NPC` — unregister на смене лока

| | |
| --- | --- |
| **Искать** | `unregister_npc` + `se_monster` и/или `se_stalker` (кадр: `se_monster` ~`:87`) |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка (смена лока / химера); автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять unregister-guard |

### 4. `GUARD_CLEAR_DEAD` — offline combat

| | |
| --- | --- |
| **Искать** | `clear_dead` + контекст offline combat / `zzzz_anthology_offline_combat_nil_fix` / `smart_terrain` |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка (дыра в апстрим offline nil-fix); автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять clear_dead-guard |

### 5. `GUARD_INTERCEPT_ARTIFACT` — iTheon

| | |
| --- | --- |
| **Искать** | `spawn_intercept_artifact_artifact` и/или `tasks_intercept_artifact` (кадр ~`:168`) |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка (iTheon); автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять intercept-guard (нужен iTheon в modlist) |

### 6. `GUARD_COVER_TILT` — Cover Tilt без Ledge Grabbing

| | |
| --- | --- |
| **Искать** | `weapon_cover_tilt` / `random_funcs` / отсутствие `demonized_randomizing_functions` |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка (в т.ч. кадр на Anthology **2.0**); автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять cover-tilt stub |

### 7. `GUARD_SPAWN_FAST` — Performance spawn fast

| | |
| --- | --- |
| **Искать** | `iterate_objects_by_clsid` + `anthology_actor_spawn_fast` / Performance |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка; автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять spawn-fast guard (Performance на exe без API) |

### 8. `GUARD_VID_MODE` — Settings / resolution

| | |
| --- | --- |
| **Искать** | `cont_vid_mode` / `reverse_resolution_list_mcm` / битый `vid_mode` (кадр ~`:65`, `w` nil) |
| **Мод** | `fix_nil_crash_guards` |
| **Откуда** | Discord-скрин, та же пачка (Settings); автор не зафиксирован |
| **Нет строки** | лог не про этот гард |
| **Есть строка** | можно проверять vid_mode-guard |

---

## `fix_create_squad_nil_smart` — 1 сигнатура

### 9. `sim_board` / `spawn_smart` nil

| | |
| --- | --- |
| **Искать** | `sim_board.script:139: attempt to index local 'spawn_smart' (a nil value)` (часто рядом `lua_pcall_failed` и кадр `create_squad`) |
| **Мод** | `fix_create_squad_nil_smart` |
| **Откуда** | чужой FATAL paste (Discord / отчёт), 2026-09-20; автор в CHANGELOG не назван; в наших `logs/` этой FATAL нет |
| **Нет строки** | лог не про этот фикс |
| **Есть строка** | можно проверять мод на этом логе; при сработавшем гарде вместо FATAL ожидать `skip create_squad: spawn_smart=nil …` |

Подробности: `addon/fix_create_squad_nil_smart/CHANGELOG.md` [1.0.0].

---

## Как обновлять

1. Новый фикс по чужому логу без нашей карточки → добавить позицию сюда (и пометку в CHANGELOG мода).
2. Тестер прислал лог, сигнатура встретилась и гард подтверждён → убрать позицию, записать подтверждение в CHANGELOG мода.
3. Стало **больше 20** позиций → не раздувать плоский список; нужна другая форма (группировка / индекс / фильтр).
