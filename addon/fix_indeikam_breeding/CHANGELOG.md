# Indeikam Breeding Fix

## [1.1.0] — 2026-09-06

**Изменено**

- `gamedata/configs/mod_system_fix_indeikam_breeding.ltx` — как в рабочем старом Kristiano AIO: `![af_indeikam]` / `![af_indeikam3]` (+ контейнеры) переназначают `inv_name` на ключи `*_anth_fix`; `@[af_indeikam_breeding_1/2/3]` создают секции селекции Брунько.
- `gamedata/configs/text/rus|eng/st_fix_indeikam_breeding.xml` — только новые ключи `*_anth_fix`: «Индейский камень» / «Узорчатый камень» (eng: Indian / Patterned Stone).
- Удалён `mod_items_artefacts_upgrades_fix_indeikam_breeding.ltx` — файл рядом с `#include`-емым LTX DLTX не подхватывает (`bIsRootFile`, см. `fix_quest_stash`).

**Причина**

В логе: `section [af_indeikam_breeding_1/2/3] doesn't exist` при выдаче у Брунько. В UI имя SGM оставалось `"Индийский камень";` из языкового пака, а Dean показывал чужое «Индейский…». Overlay старых ключей проигрывал паку; `@` в `items/items/` не грузился.

**Не затронуто**

- Статы/иконки/visual базовых `af_indeikam` / `af_indeikam3`
- Описания (`st_af_indeikam*_descr`)
- Селекция остальных артефактов
- Статы breeding — как у `af_oblivion_breeding_*` (−0.00047 / +12 вес / 0.0005 HP + 0.00088 сила), не «выдуманные» −0.00094 из старого ZIP

**Проверено**

- lint / encoding: ниже
- В игре: не прогонялось. Нужно заменить New1 AIO, проверить спавнер и выдачу breeding_1/2/3 у Брунько

## [1.0.1] — 2026-09-06

**Изменено**

- `gamedata/configs/text/rus/st_fix_indeikam_breeding.xml` — восстановлен из `9086c14`: кириллица снова в Windows-1251 (после `5bbf8db` текст был заменён на UTF-8 U+FFFD).
- `gamedata/configs/items/items/mod_items_artefacts_upgrades_fix_indeikam_breeding.ltx` — комментарий с em-dash переведён в CP1251 через `to_cp1251.ps1`.

**Причина**

В игре русские overlay-имена артефактов отображались как кракозябры / пустые квадраты: файл декларировал `windows-1251`, а байты были UTF-8 replacement character.

**Не затронуто**

- Тексты имён (те же, что в 1.0.0): «Индейский камень», «Узорчатый камень», контейнеры СПМ/ПКА/ПМА/СИМК
- Eng XML, DLTX-секции breeding_1/2/3, скрипт presence
- Статы артефактов и `inv_name`

**Проверено**

- `powershell -File tools/check_encoding.ps1 addon/fix_indeikam_breeding` — rus XML и LTX = cp1251
- `python tools/lint_addon.py fix_indeikam_breeding` — 0 ошибок
- В игре: не прогонялось

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/configs/items/items/mod_items_artefacts_upgrades_fix_indeikam_breeding.ltx` — три недостающие секции `af_indeikam_breeding_1/2/3` по шаблону соседей в `items_artefacts_upgrades.ltx` (`af_oblivion` / `af_raibloko` / `af_poipruz`).
- `gamedata/configs/text/rus/st_fix_indeikam_breeding.xml` — overlay существующих ключей: `st_af_indeikam_name`, `st_af_indeikam3_name` и четырёх контейнерных имён.
- `gamedata/configs/text/eng/st_fix_indeikam_breeding.xml` — то же для `st_af_indeikam3_*` (SGM `st_af_indeikam_name` на английском не трогался).

**Причина**

В сборке два разных артефакта с одним отображаемым именем:

- `af_indeikam` — SGM, селекция Брунько (`sgm_dialogs.script`, `breeder_recover_new63_*`).
- `af_indeikam3` — Dean / Need More Artefacts, другая иконка, другой visual, другое описание (узорчатый камень).

Ключи `st_af_indeikam_name` и `st_af_indeikam3_name` уже разные, совпадает текст. Русский пак пишет `"Индийский камень";` с лишней точкой с запятой.

Селекции `af_indeikam_breeding_1/2/3` диалог выдаёт, секций в `items_artefacts_upgrades.ltx` нет. Соседи `af_oblivion` и `af_poipruz` объявлены, `af_venez` и `af_indeikam` — дыры.

ZIP v1.0.2 / Kristiano подменял `inv_name` на новые ключи `*_anth_fix`, клал всё в `mod_system_*.ltx`, оставлял диагностический `zzzzzz_*.script`. Статы селекции были выдуманы (−0.00094 / вес 12 / сила 0.00186), а не взяты с соседей.

**Как исправлено**

Только DLTX и overlay строковой таблицы. `inv_name` секций не переназначается. Новые секции — `@`, как у `fix_dome_quest`: создадутся, если их нет, и перекроют поля старого ZIP, если он ещё включён. Статы селекции — как у `af_oblivion_breeding_*` (радиация −0.00047 / вес +12 / здоровье 0.0005 и сила 0.00088), иконки колонки 31, строки 41–43 (база `af_indeikam` — 31,44).

**Не затронуто**

- Секции `af_indeikam` / `af_indeikam3` (статы, иконка, visual, description, class)
- Контейнеры SGM (`af_indeikam_iam` и т.д.)
- Описания артефактов и контейнеров
- `sgm_dialogs.script`, `sgm_tasks.script`, детекторы, `artefacts.ltx`
- Селекция остальных артефактов, в том числе тоже дырявый `af_venez`
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Новые имена при следующей загрузке. Предметы селекции, которых в сейве ещё нет, появятся при следующем обмене у Брунько
- Конфликты: нет пересечения файлов с ZIP v1.0.2 (тот ставил `mod_system_anthology_indeikam_breeding_fix.ltx` и `zzzzzz_*.script`). В MO2 ниже сборки и языковых паков. ZIP и копию тех же файлов в `[DBG] Kristiano Fixes ALL IN ONE` лучше выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_indeikam_breeding`
- В игре: не прогонялось. Спавнер: `af_indeikam` — «Индейский камень», `af_indeikam3` — «Узорчатый камень». Брунько принимает `af_indeikam` и отдаёт тип 1/2/3 без missing section
