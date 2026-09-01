# Где агент чаще всего ошибается на Anomaly

Список написан под конкретную сборку и пополняется по факту: правило добавляется после второй одинаковой ошибки, а не заранее.

## 1. Выдуманные функции движка

Самый частый и самый дорогой класс ошибок. Отдельный документ: [`api-verification.md`](api-verification.md).

## 2. «Это же Lua 5.1, значит можно всё»

LuaJIT в X-Ray — правда, но бесполезная. Определяет возможности не версия языка, а набор биндингов движка и то, что реально используется в коде сборки. Обучать агента нужно по `reference/`, а не по общей теории Lua. Практическое следствие: перед новой конструкцией смотрим, встречается ли она в существующих скриптах Anomaly.

## 3. Многопоточность Modded Exes MT

Распространённое заблуждение, что MT-сборка выполняет Lua в несколько потоков. Это не так: Lua-VM остаётся однопоточной. Многопоточны загрузка ресурсов, HOM, трава, дождь, частицы, расчёт костей, Feel/Vision у AI, шедулер объектов, логгер. Параллельное выполнение `CreateTimeEvent` и `AddUniqueCall` существует, но **по умолчанию выключено**.

Что из этого следует:

- Объяснение Lua-крэша «гонкой потоков» требует доказательства, что соответствующий тумблер включён.
- Реальные MT-специфичные проблемы обычно выглядят как падения без Lua-кадров в стеке, артефакты моделей (кости), пропажи объектов при батчинге шедулера.
- Тумблеры MT переключаются в опциях Modded Exes; выключение конкретного — легитимный шаг диагностики.

## 4. Анонимные функции в callback'ах

```lua
-- Так нельзя: снять такой обработчик невозможно
RegisterScriptCallback("actor_on_update", function() ... end)
```

Каждый вызов создаёт новый объект функции, `UnregisterScriptCallback` его не найдёт. Обработчик останется висеть между сессиями. Всегда именованная функция, регистрация в `on_game_start`, снятие в `on_game_end`. `tools/lint_addon.py` это ловит.

## 5. Состояние, живущее между сессиями

Модульные локальные переменные и однажды применённый monkey-patch переживают выход в главное меню и загрузку другого сейва. Отсюда баги вида «после перезагрузки сейва мод считает от старых значений». Состояние сбрасываем на `on_game_load`, патч восстанавливаем в `on_game_end`.

## 6. Обращение к db.actor слишком рано

`db.actor` гарантированно доступен начиная с `actor_on_first_update`. Код в `on_game_start` или на верхнем уровне скрипта, трогающий актора, падает или молча ничего не делает.

## 7. Работа в actor_on_update без троттлинга

Каждый тик. Любой перебор объектов, обращение к alife или строковые операции там — просадка FPS, которую потом ищут неделями. Тяжёлое — в `CreateTimeEvent` или чанками с проверкой `time_global()`.

## 8. Полная замена файла вместо наложения

Скопировать `weapons.ltx` из сборки, поменять одну цифру и положить к себе — рабочий способ гарантированно конфликтовать со всеми модами, трогающими этот файл, и потерять правку при обновлении Anthology. Конфиги — DLTX, скрипты — monkey-patch.

## 9. Порядок загрузки через имя файла

Для `.ltx` префикс `zzz_`/`aaa_` ничего не даёт: порядок патчей задаёт список модов в MO2. `tools/lint_addon.py` это ловит как ошибку ORDER-001.

Для `.script` имя файла как раз определяет порядок выполнения: движок грузит все скрипты и сортирует их по имени. Префикс — способ выиграть гонку `install()` на загрузке модуля (как `zzzzzz_anthology_bhs_fdda_patch.script` в сборке). Линтер предупреждает ORDER-002; снимается комментарием в первых 10 строках: `-- load-order: после <что>`. Актуальное правило: [`anomaly-core.mdc`](../.cursor/rules/anomaly-core.mdc) (запрет `zzz`/`aaa` только у `.ltx`; у `.script` префикс допустим с этим комментарием).

Формулировки в старых CHANGELOG модов («префикс — проблема, порядок через MO2») отражают правило до разделения ORDER-001 / ORDER-002. Читать их как действующий запрет префикса для `.script` не нужно.

## 10. Кодировка

Игровые файлы — Windows-1251. Агент, создающий файл с кириллицей в UTF-8, ломает отображение в игре и иногда парсинг. Безопасный подход: в коде латиница, все видимые игроку строки — в `configs/text/`.

## 11. Совместимость сейвов

Добавление поля в сохраняемую таблицу без обработки его отсутствия ломает старые сейвы. Читаем сохранённое состояние оборонительно: любое поле может отсутствовать.

## 12. Советы из соседних движков

Код для Call of Chernobyl, Call of Misery, OGSR, IX-Ray и чистого CoP похож, но не совместим. Совпадение имени функции ничего не доказывает — проверяем по `reference/`.

## 13. Отладочный режим `-dbg` и debug HUD

Запуск с `-dbg` в аргументах MO2. В Modded Exes (`script_storage.cpp` xray-monolith) без этого ключа `printf` в release-сборке молчит: `vscript_log` сразу выходит. Тот же ключ в `console_commands.cpp` регистрирует `run_string`, `run_script`, `g_god` и соседние команды внутри блока `MASTER_GOLD + strstr(Core.Params, "-dbg")` — без `-dbg` консоль ответит unknown command.

Команда `flush` (`CCC_FlushLog` в том же файле) от `-dbg` не зависит. После `printf` из консоли её стоит вызвать сразу: иначе строка часто видна только в `.bkp` следующей сессии.

Гайд по ванильной Anomaly 1.5.3 описывает вкладку Others с оверлеями Debug HUD, Debug map spots, Debug error notifications и Actor Inside Zone Info. Последний — список имён `space_restrictor`, внутри которых сейчас актор. Точные подписи пунктов в русской Anthology по локальному `reference/configs/text` не сверены (`reference/` не наполнен). Проверка: запуск с `-dbg` и осмотр вкладки опций.

Независимо от подписей меню ту же информацию даёт таблица `db.actor_inside_zones` (ключ — имя зоны, значение — `game_object`). Она есть в `db.script` Anomaly 1.5.2 (определения Aoldri). Кто её заполняет, гайд указывает `bind_restrictor.script` — локально не сверено. Проверка в сессии:

```
run_string for name,_ in pairs(db.actor_inside_zones or {}) do printf("inside_zone=%s", name) end
```

У нас со `space_restrictor` работают `fix_gigant_space_restriction`, `fix_soc_nimble_flash`, `fix_x2_gravity_room`.

## 14. Синтаксическая ошибка в `.script`: файл не грузится, попапа нет

Ошибка разбора не даёт загрузиться всему файлу. Игра идёт дальше без него: `on_game_start` не вызывается, callback'и не регистрируются, функциональность просто отсутствует. Попапа нет.

В логе при старте строка вида:

```
[error][     LUA] ...scripts/my_mod.script:42: unexpected symbol near '='
```

Класс: «мод не работает, а лог выглядит чистым». `tools/xraylog.py` собирает FATAL и `STACK TRACEBACK`; ошибка загрузки чанка часто не попадает в карточку. Ищи в сыром логе имя `.script` и `LUA` сразу после старта, не после вылета.

Путь в движке подтверждён: `CScriptStorage::do_file` / `load_buffer` в xray-monolith при `luaL_loadbuffer`/`lua_pcall` ≠ 0 печатает ошибку и возвращает false — скрипт в окружение не попадает. Точный префикс `[error][     LUA]` — форма из гайда по ванильной 1.5.3; сверять по факту в логе этой сборки.

## 15. Коллизия глобальных имён

Каждый `.script` — своё окружение с `__index = _G`. `function foo()` без `local` в двух разных файлах — это `a.foo` и `b.foo`, они не сталкиваются. Реальная коллизия — когда оба пишут в одно и то же место, видимое всем:

- два файла с одним именем: второй модуль в `_G` молча подменяет первый;
- два monkey-patch одной функции на общей таблице модуля (`some_module.fn = ...`): второй побеждает;
- явная запись в `_G` (`rawset(_G, "name", ...)`). В `addon/` так делает `fix_replace_quest_corpse`.

Симптом — неверное значение переменной или подменившаяся функция, без ошибки в логе. Диагностика: `printf("%s", type(имя))` в начале своего callback. В `addon/` десятки `.script`, риск реальный. Новые хелперы — `local`.

## 16. Повторные ошибки из истории модов

Из отчёта по CHANGELOG/`addon/`. Подтверждённое сверено с `reference/` (сверка 2026-08-31); источник наблюдения — мод и версия.

### Подтверждено проверкой

- **`CreateTimeEvent` + `return true` снимает слот, retry не срабатывает; нужен `ResetTimeEvent` + `return false`.** Источники: `fix_quest_story_id` 1.0.1, `seamless_inventory_sort_anthology` 1.5.7.
- **`RegisterScriptCallback("on_game_end")` — такого callback нет; `on_game_end` — точка входа скрипта** (как `on_game_start`). Источник: `seamless_inventory_sort_anthology` 1.5.6; в текущем коде регистрации не осталось.
- **Полный проход id `1..65534` вместо `alife():iterate_objects`.** Источники: `fix_aver_darkvalley` 1.0.1, `fix_kupol_wrong_bone` 1.0.2 (запасной цикл, если `iterate_objects` нет или `pcall` упал). Ловится LUA-008; снимается комментарием `-- alife-scan: запасной путь, <причина>` в трёх строках перед циклом. Проверено в игре 31.08.2026, Anthology 2.1 / Modded Exes MT, ключ `-dbg`: `run_string printf("iter=%s", tostring(type(alife().iterate_objects)))` → `iter=function`.
- **`pcall(obj:id())` не защищает: аргумент вычисляется до вызова `pcall`.** Рабочая форма — `pcall(function() return obj:id() end)`. Образец: `reference/addons/Anthology_BusyHands_Stability_Fix_v0_6_5/scripts/zzzzzz_anthology_busyhands_stability_fix.script:23`. Это разбор Lua, не замер движка. Источник наблюдения: `fix_stash_id_desync` 1.0.2 писал `pcall(db.actor:id())`. Пишет ли движок `STACK TRACEBACK` при пойманной `pcall`-ошибке — см. перепроверку ниже.
- **Патч таблицы модуля, а не `_G`.** `function foo()` без `local` живёт в env файла; снаружи это `имя_скрипта.foo`. `_G` отдаёт свои функции напрямую, чужие — нет: `reference/anomaly/scripts/_g.script:18`. Загрузчик зовёт `_G[file_name].on_game_start()`: `reference/anomaly/scripts/axr_main.script:325`. `start_body_search` объявлен в модуле FDDA (`reference/addons/[TMA] FDDA Redone — Улучшенный FDDA + Разные допы/scripts/liz_fdda_redone_body_search.script:162`), снаружи зовут `liz_fdda_redone_body_search.start_body_search` (`reference/addons/[TMA] FDDA Redone — Улучшенный FDDA + Разные допы/scripts/lam2.script:547`). То же у укрытий: объявление `reference/anomaly/scripts/utils_obj.script:547`, вызов `utils_obj.find_close_cover` (`reference/anomaly/scripts/axr_fight_from_cover.script:139`). Wrap голого глобала не встаёт. Источники наблюдения: `fix_bhs_fdda_loot` 1.0.1, `anthology_busyhands_stability_fix` 0.6.2.
- **`printf` подставляет только `%s`.** Обёртка в `reference/anomaly/scripts/_g.script:612` делает `string_gsub(fmt, "%%s", …)` и отдаёт одну строку в `log(fmt)` без varargs. `%d` / `%f` Lua не подставляет. В ванили `%d` всё ещё встречается (`reference/anomaly/scripts/xr_effects.script:4571`, `reference/anomaly/scripts/utils_obj.script:746`). Число в лог — `printf("%s", n)` или `printf(string.format("…%d…", n))`. Источник наблюдения: `fix_ashot_aw_travel` 1.0.0 (бета v1.0.5). Это Lua-обёртка, не C++ `printf`.
- **`debug.traceback` не печатает в лог — только возвращает строку; стек в xraylog даёт `callstack()` из `_g.script` (форматирует traceback и пишет через `log()`).** Источник: `diag_log_spam` 1.2.2.
- **Поля секции из include-файла может переписать поздний `mod_system_*`; иконки HoC читаются из другого ini.** `[monolith_outfit]` в `reference/anomaly/configs/items/outfits/o_sts.ltx:368`; файл подхватывается `#include "o_*.ltx"` (`reference/anomaly/configs/items/outfits/base_includes.ltx:16`). HoC пишет те же поля через корень: `![monolith_outfit]` в `reference/addons/[MOD] HoC Icons Outfit+backpack/configs/mod_system_zzzzzzz_s2armor.ltx:772`. Канал `icon_override` — отдельный CInifile: `ini_file_ex("icon_override\\icon_override.ltx")` (`reference/addons/[HUD] Icons for Anthology — Иконки для A.N.T.H.O.L.O.G.Y/scripts/aaa_rax_icon_override_mcm.script:18`), внутри `#include "ico_*.ltx"` (`reference/addons/[HUD] Icons for Anthology — Иконки для A.N.T.H.O.L.O.G.Y/configs/icon_override/icon_override.ltx:8`); скрипт берёт поля оттуда раньше `ini_sys` (строки 63, 74–77). `mod_o_sts_*` либо не грузится (см. DLTX-root ниже), либо проигрывает HoC в том же CInifile — в эталоне эти два исхода не различить. Источник наблюдения: `fix_hoc_monolith_icon` 1.0.0 → 1.0.1.
- **Глобальный wrap `ChangeLevel` / `FS:file_list_open` ловит все чужие вызовы.** `ChangeLevel` — глобал `reference/anomaly/scripts/_g.script:406`; его зовут и гид Ашота (`reference/addons/[QUE] Western Goods — Западные товары и квест/scripts/western_goods_guide.script:93`), и ванильный `game_fast_travel` (`reference/anomaly/scripts/game_fast_travel.script:123`), и backpack/MLR/warfare/Azazel. `file_list_open` — C++ метод FS (`reference/anomaly/scripts/lua_help.script:2468`); те же вызовы у WTF (`reference/addons/[QUE] wtf 4_2/scripts/modxml_wtf.script:42`), ванильного радио (`reference/anomaly/scripts/ui_pda_radio_tab.script:60`) и сборщика `modxml_*` (`reference/anomaly/scripts/dxml_core.script:166`). CTD `pure virtual function called` при хранении C++-метода в эталоне Lua не воспроизведён; в шапке `_g.script:8` PVF указан как следствие живых ссылок на userdata. Источники наблюдения: `fix_ashot_aw_travel` 1.0.0, `fix_radio` 1.0.0 → 1.0.1.
- **DLTX-патч к файлу из `#include` требует моста `mod_system_*`.** Сам `mod_items_quest_*.ltx` рядом с подключаемым файлом секций не даёт. Мост — `mod_system_*.ltx` у корня `system.ltx`, внутри только `#include` файла с секциями. В `fix_quest_stash` 1.0.2: `gamedata/configs/mod_system_fix_quest_stash.ltx` содержит `#include "items\items\mod_items_quest_fix_quest_stash.ltx"`; секции — в `mod_items_quest_fix_quest_stash.ltx`. Проверено экспериментом 31.08.2026, Anthology 2.1 / Modded Exes MT, ключ `-dbg`. Замер А, оба файла на месте: `run_string printf("A exist=%s sid=%s", tostring(ini_sys:section_exist("drx_sl_quest_item_1001")), tostring(ini_sys:r_string_ex("drx_sl_quest_item_1001","story_id")))` → `a exist=true sid=drx_sl_quest_item_1001`. Замер Б, из копии мода удалён только мост, та же команда: → `b exist=false sid=nil`. Независимо диагностика мода при старте на другой секции: `test1: section drx_sl_quest_item_1014 exist=yes`; `test2: section drx_sl_quest_item_1014 exist=no`.

### Требует перепроверки по `reference/`

Сверка 2026-08-31. C++ движка в `reference/` нет (только `scripts/`, `configs/`, `text/`, `materials/`).

- **Пишет ли движок `STACK TRACEBACK` при пойманной `pcall`-ошибке.** На решение это не влияет — форма всё равно `pcall(function() return obj:id() end)`. Замер в игре не удался трижды, 31.08.2026, Anthology 2.1 / Modded Exes MT, ключ `-dbg`. Мешало одно и то же: ссылка на объект не доживала до второго ввода. Попытка 1: две команды в одном вводе → синтаксическая ошибка `console_command:2: '=' expected near 'local'`. Попытка 2: глобальная `_tmp` через `run_string` → после смены уровня `attempt to index global '_tmp' (a nil value)`. Попытка 3: `_G.db.__tmp_ref` → `saved=true`, после смены уровня `ref=false`, таблица `db` пересоздаётся. Способ, который может сработать: объект, исчезающий в пределах одного уровня, без смены уровня.

## 17. Молчаливый guard неотличим от отсутствия мода

Секция **«Мои моды»** в `tools/xraylog.py` ищет строки с `LOG_TAG` / именем мода. Если скрипт загрузился, но `install()` вышел без `printf`, мод попадает в **«Не появились в логе»** — как будто его нет в MO2 или пакете.

Пример: `fix_aim_fatigue_visibility` — guard на строках 95–96 возвращает `false`, когда нет `aim_stamina.on_option_change` / `load_state`, без записи в лог. Подтверждено в игре 31.08.2026: `[HARD] Aim Fatigue` отключён в профиле MO2 (`modlist.txt`, строка с минусом), скрипт из `[DBG] Kristiano Fixes ALL IN ONE NEW` на месте, в карточке — ноль строк.

Контракт (`.cursor/rules/anomaly-lua.mdc`): безусловная presence-строка при загрузке файла; каждый ранний `return` из `install()` — `printf` с причиной. Образец: `aaa_fix_trader_restock_callback` (top-level), `fix_charon_red_forest_travel` (`guard NOT installed`).

## Открытые вопросы

Сюда пишем то, что пока не проверено на этой сборке, чтобы не выдавать за факт:

- Насколько полно Anthology 2.1 поддерживает XML-override для UI-файлов и в каком виде — проверить по README Modded Exes конкретной версии.
- Какие именно MT-тумблеры включены в дефолтном конфиге сборки.
- Точные строковые id и русские подписи debug-оверлеев (Actor Inside Zone Info и соседние) в `configs/text` этой сборки.
