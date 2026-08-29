# Milspec and Exo Craft Fix

## [1.0.1] — 2026-08-30

**Изменено**

- `gamedata/configs/items/settings/mod_craft_device_fix_milspec_exo.ltx` — во вкладке Exo System все семь рецептов из старого архива: кустарный, военный, прототип, щит, двигатель, прыжок, невидимка.

**Причина**

1.0.0 ставил только четыре строки из `exo_loot.add_recipes`. Военный / прыжок / невидимка в крафт не попадали; прыжок и невидимка в оригинале не спавнятся вообще.

**Как исправлено**

Строки и ингредиенты — как в старом архиве. Дроп военного БП в `exo_loot.script` (10% / 3%) не тронут: крафт — дополнительный путь.

**Не затронуто**

- `exo_loot.script` и шансы лута
- `workshop_autoinject.script`, файлы Catspaw / Exo / Banjaji / R.A.K
- Предметы, торговцы, сейвы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 ниже R.A.K, Catspaw All Pack и Exo System. Старый ZIP и скрипт в Kristiano выключить

**Проверено**

- lint: `python tools/lint_addon.py fix_milspec_exo_craft`
- В игре: не прогонялось. Ожидается семь БП во вкладке «Exo System»; военный по-прежнему падает с трупов

## [1.0.0] — 2026-08-30

**Изменено**

- `gamedata/configs/items/settings/mod_craft_device_fix_milspec_exo.ltx` — DLTX: рецепт Milspec PDA в `![craft_-500]` (Устройства); четыре рецепта БП Exo System в `@[craft_-510]`.

**Причина**

Banjaji CSI v4 читает только секции `craft_*` и собирает меню через `aa_load_recipes_Banjaji_CSI.get_recipes()`. Catspaw патчит несуществующий `[1]`. Exo System вызывает `workshop_autoinject.add_new_recipe`, который целится в удалённый `UIWorkshopCraft:LoadRecipes`. Пустая вкладка `craft_-510` из R.A.K удаляется в `check_empty_tabs`. Ошибок в логе нет — оба мода молча ничего не делают.

**Как исправлено**

Один DLTX на живые секции CSI. Строка ПДА — как в `mod_craft_milpda.ltx`. Строки БП — как в `exo_loot.add_recipes`. Ванильный формат CSI переводит сам. Скрипт и хардкод таблиц не нужны.

**Не затронуто**

- Ингредиенты, toolkit и записки оригинальных рецептов
- Крафт `exo_power_supply_military` / `_jump` / `_invisibility` (Exo их не регистрировал)
- `workshop_autoinject.script`, файлы Catspaw / Exo / Banjaji / R.A.K
- Лут, торговцы, предметы, сейвы

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции. Рецепты в `itms_manager.ini_craft`, не в save
- В MO2 ниже `[GAM] R.A.K Balance`, Catspaw All Pack и `[BS] Exo System`. ZIP `Milspec_And_Exo_Craft_Fix` и `workshop_autoinject_banjaji_compat.script` в `[DBG] Kristiano Fixes ALL IN ONE` выключить — иначе дубли

**Проверено**

- lint: `python tools/lint_addon.py fix_milspec_exo_craft`
- В игре: не прогонялось. Ожидается: ПДА в «Устройства» после прочтения `recipe_pda_milspec`; basic/proto/tank/sprint БП во вкладке «Exo System» после соответствующих записок
