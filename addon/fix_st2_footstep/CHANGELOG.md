# ST2 Mutant Footstep Fix

## [1.0.0] — 2026-08-29

**Изменено**

- `gamedata/materials/mod_material_pairs_fix_st2_footstep.ltx` — DLTX `![pair]` только на `step_sounds` у сломанных пар ST2-мутантов.

**Причина**

`[SND] S.T.A.L.K.E.R_MUTANTS` задаёт шаги через `mod_material_pairs_ST2_*.ltx`. В девяти файлах пути битые:

- кровосос: в значение попало `step_bloodsucker_sounds =`, между семплами 9 и 10 нет запятой — движок ищет несуществующий файл;
- химера `@default`: путь обрывается на `step_chimera_` вместо `step_chimera_9`;
- химера / контролёр / плоть / псевдогигант / псевдопёс / тушкан / снорк / зомби на поверхностях: шаблон `step_1..5` вместо реальных имён OGG.

Кабан, бюрер, кот и собака в том же паке уже с верными именами.

ZIP v1.0.0 подменял девять файлов пака целиком (те же имена `mod_material_pairs_ST2_*.ltx`), копировал пустые `breaking_sounds` / `collide_*` и объявлял секции как `[section]` без `!`.

**Как исправлено**

Один DLTX на `material_pairs.ltx`: `![creatures\st2_*@...]` и только поле `step_sounds`. Файлы пака не трогаются. Обратные пары (`[earth@creature]:creature@earth`) наследуют значение. Число семплов как у автора: 10 у кровососа везде и у химеры на default; 5 на поверхностях, как у корректно написанной собаки.

**Не затронуто**

- `mod_materials_ST2_footstep.ltx`, `mod_system_ST2_footstep.ltx` (привязка `material = creatures\st2_*`)
- кабан, бюрер, кот, собака; `step_cloth_*` у собаки
- OGG, анимации шага (`mod_system_zzzz_foot_fix.ltx`), radiation/psy sound
- ванильные `material_pairs.ltx` / материалы сталкеров
- `all.spawn`

**Совместимость**

- Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT
- Сейвы: без миграции, новый запуск
- Конфликты: нет пересечения имён с паком. ZIP v1.0.0 выключить — он затирает оригиналы пака. В MO2 ниже `[SND] S.T.A.L.K.E.R_MUTANTS`

**Проверено**

- lint: `python tools/lint_addon.py fix_st2_footstep`
- В игре: не прогонялось. Кровосос на земле: шаги без missing-file в логе. Химера default: играет `step_chimera_9`. Снорк на бетоне: `step_snork_1..5`, не `step_1`
