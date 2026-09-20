# Changelog

Изменения самого рабочего места. Изменения модов ведутся в `addon/<mod_id>/CHANGELOG.md`.
Записи старше месяца — в [`CHANGELOG-archive.md`](CHANGELOG-archive.md).

## [0.1.72] — список сигнатур, ожидающих подтверждения

`docs/awaiting-confirmation.md` — 9 позиций из CHANGELOG модов с пометкой «чужой лог» / Discord-скрины без наших cards: 8 гардов `fix_nil_crash_guards` + `fix_create_squad_nil_smart`. По каждой: что искать в логе, мод, источник, смысл отсутствия/появления. Команда `/logfull` (файл не было — создан) и шаг в `/crash`: при разборе чужого лога сверяться со списком. `docs/prompts.md` — ссылка на `/logfull`.

## [0.1.71] — xraylog: stack trace с таймстемпом; журнал CTD на Баре

`tools/xraylog.py`: `STACK_RE` ловит `[HH:MM:SS.mmm] stack trace:` (Modded Exes) — иначе native AV без FATAL терялся. Тест. Журнал: UnhandledFilter `UpdateDynamicDamage` / `InitContact` на `l05_bar`, sound abort PA black_valley, BTR `ph_car` при `stype=nil`, WTF `gt_guard`. Карточка `logs/cards/2026-09-19_newxray_nikit.md`. Changelog бандла: AIO 1.0.0 и gigant 1.1.2.

## [0.1.70] — версия пакета AIO для бета-отчётов

`tools/_pack_kristiano_aio.py`: константа `AIO_VERSION` (сейчас `1.0.0`, semver) пишется в `BUILD_INFO.txt` (`version:`), `meta.ini` (поле Version в MO2), `CONTENTS.txt` / `README_RU.txt`. Раньше в meta была дата дня сборки, в BUILD_INFO версии не было. Дата остаётся в `built:`. Separate (CMO / QuickQK / ST2 / Campfires) уже берут version из мода в meta и BUILD_INFO — без правок. `community/BUG_REPORT.md` — поле «версия пакета» и где взять. Тест на строки version в AIO zip.

## [0.1.69] — gigant: снятие сессионного карантина на on_game_end

`fix_gigant_space_restriction` 1.1.2: перед `reset_state` на `on_game_end` сессионные reason в `quarantined` получают `set_switch_online(true)`; unsafe оставляем; одна строка лога `exit quarantine freed=…`. Персист `false` — побочный эффект сериализации API, не замысел. `community/UNINSTALL.md` обновлён (шаг load→меню и оставшаяся дыра без запуска).

## [0.1.68] — UNINSTALL.md: снятие AIO одним чек-листом

`community/UNINSTALL.md` — процедура снятия `[DBG] Kristiano Fixes ALL IN ONE` (выборочно нельзя): необратимое (`fix_gigant_space_restriction` / карантин без restore), три шага до выключения, что остаётся в сейве плюсом и какие баги вернутся. Сгруппировано по действию; вердикт — длинный чек-лист по 82 модам не публиковать, для гигантов нужен `allow_online` на `on_game_end`, а не инструкция. Ссылка в `community/README.md`.

## [0.1.67] — публикация модов: Удаление, Требования, совместимость, категории

Во всех 82 `addon/*/CHANGELOG.md`: блок **Удаление** (как снять в MO2 + влияние на сейв); строка **Требования** в шапке (сборка / движок / MO2 / что выключить). У шести форков / full-replace **Совместимость** — список конкретных перезаписываемых путей + фраза про патч/слияние при совпадении.

`meta.ini`: `category` разделён на `чинит вылет` / `чинит логику` / `косметика` по CHANGELOG; починены `category=0` у CMO и разнобой `\r`.

## [0.1.66] — подготовка к бете: отчёт, совместимость, DLTX, архив CHANGELOG

`community/BUG_REPORT.md` — шаблон отчёта тестера (шаги, сейв, ожидание/факт, версии сборки и движка, `modlist.txt`, порядок, полный `xray_*.log`); абзацы про полный лог vs скриншот и про modlist (кейс двух `fix_indeikam_breeding`). Ссылка в `community/README.md`.

Одна строка **Совместимость** у форков без явной строки: `context_menu_overhaul_anthology`, `anthology_busyhands_stability_fix`. Остальные форки / full-replace (`campfires_anthology_compat`, `burnshit_inventory_destroy`, `seamless_inventory_sort_anthology`, `fix_utjan_mag_skill`) уже имели секцию — не трогались.

`docs/pitfalls.md` §8a: вид FATAL `[DLTX] Duplicate section`, смысл, решение (`!` / уникальное имя / выключить дубль в modlist).

`CHANGELOG-archive.md`: перенесены `0.1.0`–`0.1.45` (август); в основном файле — с `0.1.46`. `tools/check_changelog_tools.py` смотрит только `CHANGELOG.md` — архив в сверку не входит, правки кода не требуются. (tools-ref)

## [0.1.65] — xraylog: нативный вылет без FATAL

`tools/xraylog.py` больше не помечает AV с `UnhandledFilter` + `stack trace:` как «вылета в логе нет». Новый класс **`нативный вылет (не Lua)`**: в карточке — верхние кадры стека (`DoRenderDialogs` / `rp_ScreenResolutionChanged` и т.п.), без пустой секции FATAL. Штатный выход (`* Quitting...`, фикстура `clean_session.log`) по-прежнему clean.

FATAL `[DLTX] Duplicate section` / `CInifile::StashCurrentSection` — класс **`конфиг: DLTX`** вместо «не классифицировано». Фикстуры `logs/samples/crash_native_av.log`, `crash_dltx_duplicate.log`; тесты; отпечаток архива `("native", …)`. На логах mg9000 19.09: два UnhandledFilter → нативный класс, DLTX → конфиг: DLTX, Lua pcall без регрессии.

## [0.1.64] — ENC-005 и docs/mods/

`tools/lint_addon.py`: ошибка ENC-005 на подряд идущие `?` (≥2) в комментарии `-- load-order:` — порча кириллицы «после» редактором без cp1251; ENC-004 (EF BF BD) этот случай не ловит. Детектор `tools/_common.py::has_load_order_question_marks`. Тесты на порчу, одиночный `?` и целый cp1251. В `addon/fix_qaw_ammo_nil` снова восстановлено `-- load-order: после …` в Windows-1251.

Рабочие материалы мода (ТЗ, лор-черновики) — в `docs/mods/<mod_id>/`, не в корень `addon/` (STRUCT-004/005). Правило: `docs/mods/README.md`; зеркала в README, AGENTS.md, `anomaly-core.mdc`, `docs/plans/addon.md`. У `kristiano_kx1_exo` перенесены `ICON_TZ.txt` и `lore/`.

Риск ложного срабатывания ENC-005: намеренные `??` / `???` в тексте `-- load-order:` (плейсхолдер или имя мода с вопросами). В проекте комментарий фиксирован как `-- load-order: после <что>` — такие `?` не встречаются; риск приемлем.

## [0.1.63] — критерий архивации карточек

`logs/README.md`: когда класть карточку в `logs/cards/` (новая сигнатура / значимая динамика / точка отсчёта) и когда нет (повтор без изменений, чужая сборка, дубль сессии). `/crash` перед `--archive` сверяет с этим критерием и называет причину. `xraylog --archive` предупреждает в stderr при полном совпадении сигнатуры с уже лежащей карточкой, но не блокирует запись. Чужой путь к exe/gamedata в логе — только глазами: единого маркера «наша папка» нет. Тесты на отпечаток и предупреждение о дубле.

## [0.1.62] — LUA-001: свои пакеты `addon/<id>-версия` в эталоне

`fill_reference_addons`: имя папки == id из `addon/` или id + суффикс версии (`-1.0.0`) считается своим пакетом (раньше ловились только AIO/SEPARATE/BusyHands и BUILD_INFO). `lint_addon.ReferenceView` не индексирует такие папки в `reference/addons/` — иначе LUA-001/LTX-001 видят нашу же сборку. Риск: чужой мод, буквально названный `<наш_id>-1.2.3`, попадёт под фильтр; `fix_foo_extra` / `fix_foo-extra` — нет. В эталоне совпадений было два (`fix_crowkiller_hello-1.0.0`, `fix_xr_effects_sounds-1.0.0`); сирота `fix_rak_lsw_crash-1.1.0` без `addon/`. FORK-001 не затронут (читает `vendor_source` с диска). После правки `--cross --no-verify`: LUA-001/LTX-001 = 0. Тесты на версию и на похожий чужой префикс.

## [0.1.61] — xraylog: консоль cp1251 и карточки без Out-File

Удалены пять битых файлов в `logs/cards/` (три `xray_nikit_*`, `nizrim_card.txt`, дамп `nizrim_card_errors.txt`) — порча от `>`/`Out-File` и падения печати. `xraylog` / `_common.configure_stdio`: stdout/stderr с `errors=replace`, чтобы `UnicodeEncodeError` на ×/→ не валил запуск на cp1251; в карточке счётчики `xN` вместо `×N`. В `docs/setup.md` (у chcp): карточки только через `--archive`/`--out`. `docs/prompts.md`, `docs/mo2.md` — то же. Тесты на печать в cp1251.

## [0.1.60] — чистка логов: clean-карточки и журнал issues

`logs/cards/`: удалены 12 из 14 карточек класса «вылета в логе нет» (оставлены `2026-09-08_xray_nikit_measure`, `2026-09-03_xray_mg9000-5` как точка отсчёта). `docs/issues.md` — блоки `## [issue] \`сигнатура\`` с полями дата/мод/итог/карточка (grep по классу ошибки). `xraylog.py --archive` больше не кладёт чистые сессии в архив без `--archive-clean`. `.cursorignore` уже исключал `logs/cards/` — без изменений. Тесты на отказ/разрешение архивации clean.

## [0.1.59] — ENC-004: UTF-8 replacement (EF BF BD)

`tools/lint_addon.py`: ошибка ENC-004 на байты `EF BF BD` (U+FFFD) в игровых текстовых файлах — порча после перекодировки, которую ENC-003 не ловит. Детектор в `tools/_common.py::has_utf8_replacement`. Тесты на порчу и корректный cp1251. В `addon/fix_qaw_ammo_nil` восстановлено `-- load-order: после …` в Windows-1251 (ORDER-002).

## [0.1.58] — правила Discord и проверка нарушений

`community/RULES.md` — полный свод сервера Anomaly Anthology; `community/discord-rules.json` — индекс пунктов (id, наказание, сигналы). `tools/modcheck.py`: `lookup`, `scan`, `list`. Команда `/modcheck`, правило `workflow-discord-mod.mdc`. `scan` — кандидаты по словам, вердикт по тексту пункта.

## [0.1.57] — пробелы crash/Lua: pcall, модель, OOM, отложенный тик

`workflow-crash.mdc` и `docs/plans/crash.md`: в таблице классификации — `lua_pcall_failed`, `Can't find model file` / `CModelPool`, OOM/`VirtualAlloc`; несколько Lua-ошибок — первая по времени; вылет на сейве — более ранний сейв и смена списка модов; «удали мод и начни новую игру» — не диагностика. `anomaly-lua.mdc`: тяжёлую очистку в callback со сносом объекта/UI откладывать через `CreateTimeEvent(..., 0, named_fn)`. Самопроверка `workflow-addon` / `docs/plans/addon.md`: конфликт с другим модом и nil вне онлайна. `tools/xraylog.py`: те же три FATAL-класса; синтетические `logs/samples/crash_{lua_pcall,missing_model,oom}.log` и тесты. pitfalls §13: первая Lua-ошибка и `.bkp`.

## [0.1.56] — check_changelog_tools: ссылка ≠ правка

`tools/check_changelog_tools.py`: путь `tools/` в добавленной строке CHANGELOG без изменений под `tools/` больше не валит сборку, если в конце строки стоит `(tools-ref)` — явная пометка «ссылка на инструмент, не правка» (как `-- load-order:` для ORDER-002). Без пометки прежнее поведение. Ложное срабатывание на [0.1.55] (упоминание `tools/refindex.py` как маршрута поиска) — причина правки. Тесты на оба случая и на формулировку df81d5f; README.

## [0.1.55] — reference/ и logs/cards/ вне индекса Cursor

`.cursorignore`: каталог `reference/` (~14k файлов) исключён целиком — поиск по эталону через `tools/refindex.py`, не через семантический индекс Cursor; `logs/cards/` тоже вне индекса (чтение адресно при `/crash`). Убраны `!reference/**` и бинарные исключения внутри `reference/`. Правила и команды: `anomaly-core`, `no-hallucinated-api`, `workflow-fix`/`workflow-addon`, `/crash`, зеркало в `AGENTS.md` — явно `refindex.py` / адресный Read, без семантического обхода `reference/`. (tools-ref)

## [0.1.54] — pack_separate: отказ без gamedata/

`pack_separate` больше не собирает zip из одного `BUILD_INFO.txt`: нет `gamedata/` или она пуста → `SystemExit` с именем мода. Фикстура `test_pack_kristiano_aio` создаёт `campfires_anthology_compat` (добавлен в `SEPARATE`, структура как у остальных separate). Тест на отказ без/с пустой `gamedata/`.

## [0.1.53] — карточки без « (N)», удаление MEMORIES.md

`xraylog.py --archive`: из stem источника срезается Windows-суффикс ` (N)` (`xray_mg9000 (1).log` → `…_xray_mg9000.md`, коллизии по-прежнему `-2`, `-3`). Три сессии `logs/cards/2026-09-03_xray_mg9000*.md` переименованы с `(1)`/`(2)` на `-2`/`-3`. Тест на имя с таким суффиксом. Удалён пустой `MEMORIES.md` (шаблон учёта PR — у нас нет PR, учёт разборов уже в `docs/issues.md`).

## [0.1.52] — check_installed: stdout на cp1251 и кавычки у путей с [DBG]

Заголовок блока переустановки: ASCII `->` вместо Unicode `→` — на Windows stdout часто cp1251, иначе `UnicodeEncodeError` на всём отчёте. Пути к zip со скобками (`[DBG]`, …) в кавычках. `reinstall_items` / `format_reinstall` и раньше давали один блок на пакет; тест фиксирует: устаревший AIO с несколькими `sources` — ровно один раз в «переустановить» и в «устарел».

## [0.1.51] — журнал разобранных проблем

[`docs/issues.md`](docs/issues.md) — указатель разобранных случаев (сигнатура в логе → чей мод → итог → карточка / pitfalls). Заполнен по CHANGELOG, pitfalls и `logs/cards/` (десять известных классов). Строка в README; в `.cursor/commands/crash.md` — сначала смотреть журнал, потом карточки.

## [0.1.50] — /deploy: полный цикл сборка → сверка MO2

`.cursor/commands/deploy.md`: сборка пакетов, `check_installed.py`, список переустановки с путями к zip, команда повторной проверки после установки. `check_installed`: путь MO2 из аргумента / `ANTHOLOGY_MO2` / `local.json`; `--reinstall`; эвристика clone (узкий разброс mtime в `addon/*/gamedata/` — «сравнивать не с чем», не «всё устарело»). Образец `local.json.example`, `local.json` в `.gitignore`. Тесты в `tests/test_check_installed.py`.

## [0.1.49] — check_installed: сверка MO2 с addon/

`tools/check_installed.py <MO2>`: находит в `mods/` пакеты с `BUILD_INFO.txt`, сравнивает `built` с mtime `addon/*/gamedata/`, печатает устарел / актуален / не установлен. SKIP и SEPARATE из `_pack_kristiano_aio` в «не установлен» не входят. В CI / при `--no-mtime` — как VERIFY-001: mtime после clone недостоверен, сравнение пропускается. Тесты `tests/test_check_installed.py`.

## [0.1.48] — BHS vendor_source → v0_6_1

`addon/anthology_busyhands_stability_fix/meta.ini`: `vendor_source=Anthology_BusyHands_Stability_Fix_v0_6_1` вместо `…_v0_6_4`. Папки `v0_6_3`/`v0_6_4`/`v0_6_5` удалены из `reference/addons/` 31.08 (`[0.1.33]`); единственный внешний BusyHands в эталоне — `v0_6_1`. Запись в CHANGELOG мода — не откат версии фикса, а привязка packer'а к фактическому источнику full-file.

## [0.1.47] — pack_bhs: vendor_source из meta.ini

`tools/pack_bhs.py` берёт вендорскую папку только из `vendor_source` в `addon/anthology_busyhands_stability_fix/meta.ini`; без ключа или без папки в `reference/addons/` — явный `SystemExit`. Убран fallback по `*BusyHands*` и константа `VENDOR_SOURCE_VERSION`. `BUILD_INFO.txt` фиксирует `vendor_source`, размеры full-file (`mon_sleep`, `guaranteed_loot`, `aes_crow_spawner.ltx`) и источник `sequential_load_magazine`. Тесты в `tests/test_pack_bhs.py`.

## [0.1.46] — ENC-002: порча окончаний строк

`tools/lint_addon.py`: ошибка ENC-002 на `\r\r\n` и одиночный `\r` (не CRLF) в игровых файлах мода. Бывший ENC-002 (UTF-8 с кириллицей) переименован в ENC-003. Детектор в `tools/_common.py::has_bad_line_endings`. Тесты на обе формы порчи и корректный CRLF.
