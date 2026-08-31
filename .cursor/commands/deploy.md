---
description: Пересборка модов. Без аргументов.
---

Пересборка. Без аргументов. Цепочка: [`docs/mo2.md`](../../docs/mo2.md).

1. Пакеты: `python3 tools/_pack_kristiano_aio.py` (AIO с BusyHands внутри через `pack_bhs.stage_gamedata` + три отдельных: `context_menu_overhaul_anthology`, `quickqk_task_complete`, `fix_st2_footstep`). Опционально `python3 tools/pack_bhs.py` — отдельный zip BHS для точечного обновления. Состав AIO — `SKIP`/`SEPARATE` в скрипте.
2. Остальные: `python3 tools/build_addon.py` для модов в `addon/`, не входящих в эти пакеты. Ошибки линтера — чини или `--force` с пояснением.

В конце — список архивов и папок в `build/`, что переустановить в MO2. Напомни: открыть папку мода в MO2 и убедиться, что `BUILD_INFO.txt` свежий, а не старая копия. Код не трогай.
