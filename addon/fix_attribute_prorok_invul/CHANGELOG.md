# Attribute Prophet Invul Clear

## [1.0.0] — 2026-08-30

**Изменено**

- `gamedata/scripts/fix_attribute_prorok_invul.script` — после `cld_bs_run_start` принудительно `npc:invulnerable(false)` у `cd_p30_prorok`; обёртка `stalker_generic.reset_invulnerability` на кадре смены схемы.

**Причина**

Интро Коллайдера ставит `invulnerable = true` на `walker@start`. Смена на `move@fight` должна снять флаг. `reset_invulnerability` читает старый `active_section` (вызов до записи новой секции в `xr_logic.script:235/253`), `disable_invulnerability` пустой. Если геттер уже врёт `false`, `update_invulnerability` сеттер не зовёт. Бой при этом обычный. F5/F9 перебиндивает объект — флаг собирается заново.

**Как исправлено**

Callback + узкий monkey-patch, оригиналы схем не подменяются. После инфопорта интро сеттер `false` зовётся без проверки геттера, только для story id `cd_p30_prorok`.

**Не затронуто**

- `cld_p30_prorok_boss_logic.ltx`, `xr_move`, `combat_ignore`
- `anthology_npc_specific_toughness.script` (множитель 0.05)
- метро e70 / казнь, `all.spawn`
- неуязвимость других сталкеров
- сохраняемое состояние

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, ничего не пишет. На уже начатом бое Коллайдера флаг снимается на следующем кадре
- В MO2 ниже сборки и Атрибута

**Проверено**

- lint: `python tools/lint_addon.py fix_attribute_prorok_invul` — OK
- В игре: не прогонялось. Ожидаемый лог: `wrapped stalker_generic.reset_invulnerability`, `cleared invulnerable on cd_p30_prorok`. После камеры интро урон должен идти без F5/F9
