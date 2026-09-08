# G2X Torch Meshes Fix

## [1.0.1] — 2026-09-08

**Изменено**

- `dev_torch_light.ogf` и `dev_torch_light_red.ogf` — оба заменены на стоковый белый меш Anthology (файлы от ReVo_Onl1ne; `*_red` — тот же белый OGF под именем red).

**Причина**

Движок записывает путь к visual (OGF) в объект при создании. Если в сейве у NPC/фонаря уже прописан `dev_torch_light_red.ogf`, а мод G2X выключен и красного меша нет — CTD `Can't find model file`. Белый меш под обоими именами: при отключённом G2X фонари остаются белыми, сейвы грузятся без вылета.

**Не затронуто**

- Presence-скрипт, логика G2X / MCM-пресеты, текстуры
- Цвет свечения (меняется G2X через MCM независимо от меша)

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции; старые объекты с путём на `*_red` больше не крашат при выключенном G2X
- В MO2: фикс (ALL IN ONE / Kristiano Fixes) выше мода G2X; сам G2X — не в GFX, а ниже этого фикса

**Проверено**

- Хеши обоих OGF совпадают с файлами от ReVo (SHA256 `52123EE3…`)
- lint: `python tools/lint_addon.py fix_g2x_torch_meshes`
- В игре: не прогонялось. После установки: загрузить старый сейв с красным пресетом при выключенном G2X — без CTD, меш белый.

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
