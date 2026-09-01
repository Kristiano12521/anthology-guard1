# G2X Torch Meshes Fix

## [1.0.0] — 2026-09-01

**Изменено**

- `gamedata/meshes/dynamics/devices/dev_torch_light/dev_torch_light.ogf` — стандартная модель налобника для пресетов G2X.
- `gamedata/meshes/dynamics/devices/dev_torch_light/dev_torch_light_red.ogf` — красный вариант для пресета `hl_rd_ref_60_red`.

**Причина**

Мод `[GFX] G2X Tactical Light Presets + MCM` через DLTX подменяет `visual` у `device_torch` на `dev_torch_light*.ogf`. Лаунчер Anthology деплоит конфиги/скрипты/текстуры G2X, но меши в установку игры не попадают: `dev_torch_light.ogf` лежит только в `dev_torch_light.7z`, движок `.7z` не читает. При спавне фонаря (`CTorch::net_Spawn`) — FATAL: `Can't find model file ... dev_torch_light_red.ogf` (или `dev_torch_light.ogf`).

**Как исправлено**

Два `.ogf` в VFS как loose-файлы. Логика G2X и MCM-пресеты не трогаются.

**Не затронуто**

- `g2x_mcm_config_writer.script`, DLTX-пресеты, текстуры `g2x_repository`
- `dev_torch_light3.ogf` (Pinup Collect) — отдельный ресурс, не в этом фиксе
- Ванильный `device_torch` без G2X

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Нужен только если включён G2X Tactical Light Presets + MCM (профиль Standart Anthology)
- Сейвы: без миграции
- В MO2: ниже `[GFX] G2X Tactical Light Presets + MCM` (или в папке Kristiano Fixes — порядок на меши не влияет)

**Проверено**

- lint: `python tools/lint_addon.py fix_g2x_torch_meshes`
- В игре: не прогонялось. После установки: Янтарь / любая локация, включить налобник (`L`) с любым G2X-пресетом, в т.ч. `hl_rd_ref_60_red` — без CTD.
