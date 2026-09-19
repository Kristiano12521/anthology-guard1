# Фикс закрытых ящиков под зелёные тайники

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; В MO2 ниже сборки и Grok's Stash Overhaul (если стоит).

**Удаление**

- Один load с модом (перенос лута с закрытых ящиков), сохранитесь, затем отключайте.
- Перенесённый лут остаётся. Без blacklist зелёные метки снова могут сесть на закрытые сюжетные ящики.

## [1.0.1] — 2026-09-17

**Изменено**

- В blacklist добавлены `esc_inventory_box_quest` и `caz_aeroplan_narkota_box` (скрипт + оба DLTX).
- `meta.ini` -> 1.0.1.

**Причина**

На Кордоне `simulation_task_44` («Было ваше — стало наше») через `get_random_stash(..., inv_box=true)` садился на `esc_inventory_box_quest`: сундук открывается, путь режет запертая дверь. Имени не было в списке (класс «открытый ящик за дверью», без `nonscript_usable=false`). `caz_aeroplan_narkota_box` — скриптово закрытый ящик, пропущенный в 1.0.0.

**Не затронуто**

- Логика дверей/ключей, `all.spawn`, остальные имена blacklist
- Пул свободных ящиков для белых/зелёных/красных меток и заданий

**Проверено**

- lint: `python tools/lint_addon.py fix_locked_stash_boxes` — 0 ошибок
- `--cross`: CROSS-001 с `fix_quest_stash` на `[blacklist_stashes_names]` (как раньше; порядок в MO2)
- в игре: не прогонялось. Ожидаемый лог при проблемном сейве: `relocated pending name=esc_inventory_box_quest ...` или `removed from pool name=esc_inventory_box_quest ...`

## [1.0.0] — 2026-09-14

**Изменено**

- `gamedata/configs/items/settings/mod_treasure_manager_fix_locked_stash_boxes.ltx` — DLTX `![blacklist_stashes_names]`: сюжетные/закрытые ящики.
- `gamedata/configs/items/settings/mod_grok_treasure_manager_fix_locked_stash_boxes.ltx` — то же для Grok's Stash Overhaul (`grok_treasure_manager.ltx`).
- `gamedata/scripts/fix_locked_stash_boxes.script` — обёртка `treasure_manager.get_random_stash` (оригинал проверяет blacklist только при `inv_box=true`); repair сейва: pending-лут переносится на свободный ящик, пустые слоты и метки снимаются.

**Список имён (se_obj:name)**

`esc_kkp_sidr_habar`, `esc_inv_out_quest_fee`, `esc_inventory_box_base_bandits`, `esc_inventory_box_quest_fee`, `okr_s1_inventory_box`, `okr_av_1..5_inv_box`, `kn_b1_av_1_inv_box`, `scf_av_1_inv_box`, `scf_d3_box_code`, `scf_v1_shakal_box`, `sad_b1_iliya_treasure`, `sad_b2_maxim_treasure`, `sad_ran_cowboy_treasure`, `inv_box_strelok_mlr`, `mon_blue_box_mlr`, `zat_b12_conteiner`, `topi_i1_killer_code_tainik`, `cit_a2_secret_box`, `az_box_pidor_case_merger`, `caz_bb_heli_container_pilots`, `okr_texnar_util_box`, `sad_b2_util_box`, `jup_b202_snag_treasure`, `jup_b202_actor_treasure`.

**Причина**

Зелёный тайник (`treasure` spot) сел на закрытый сюжетный ящик Сидора на северном КПП (`esc_kkp_sidr_habar`, «Путь во мгле»). Тот же класс: ящики с `nonscript_usable=false` до ключа/кода/инфопорции не были в `[blacklist_stashes_names]`.

**Не затронуто**

- Сюжетные замки, ключи, логика ящиков, `all.spawn`
- `fix_quest_stash` / `val_q7_n`, уже существующие записи blacklist
- Выдача хабара Сидору / Spectrum

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: repair при `actor_on_first_update`; новая игра не нужна
- В MO2 ниже сборки и Grok's Stash Overhaul (если стоит)

**Проверено**

- lint: ожидается `python tools/lint_addon.py fix_locked_stash_boxes`
- В игре: не прогонялось. Ожидаемый лог: `get_random_stash wrapped`, при проблемном сейве `relocated pending name=esc_kkp_sidr_habar ...`
