# HoC Monolith Icon Fix

## [1.0.1] — 2026-08-28

**Изменено**

- `gamedata/configs/icon_override/ico_fix_hoc_monolith_icon.ltx` — ванильная иконка (90, 3) для `monolith_outfit` и `stalker_monolith_outfit` в канале `icon_override`.
- Удалён `mod_o_sts_fix_hoc_monolith_icon.ltx`: его затирал `mod_system_zzzzzzz_s2armor.ltx`.

**Причина**

1.0.0 патчил `o_sts.ltx`, а HoC пишет те же поля позже через глобальный `mod_system_*`. F7 берёт иконку из `utils_xml.set_icon`, а скрипт HoC сначала читает `icon_override\ico_*.ltx`.

**Как исправлено**

Файл `ico_*` подхватывается `#include "ico_*.ltx"`. Обе секции явно: в этом ini нет наследования от родителя. Поля полные: если секция есть, недостающие не берутся из `ini_sys`.

**Не затронуто**

- Статы, модель, квест Чёрной долины
- `monolith_outfit_wings`
- DDS HoC и остальные костюмы
- Две строки в F7

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции
- В MO2 ниже `HoC Icons Outfit+backpack` и `Icons for Anthology`

**Проверено**

- lint: `python tools/lint_addon.py fix_hoc_monolith_icon`
- В игре: не прогонялось. Нужен полный перезапуск игры. F7 → оба id — ванильная серая иконка, не зелёный «Ветер свободы».

## [1.0.0] — 2026-08-28

DLTX на `o_sts.ltx`. В игре не сработал: HoC `mod_system_zzzzzzz_s2armor.ltx` перезаписывал клетку после патча.
