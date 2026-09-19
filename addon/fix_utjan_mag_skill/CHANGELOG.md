# Utjan Mag Skill Magazines Guard

**Требования:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; ниже HarukaSkillSystem.

**Совместимость:** перезаписывает `scripts/utjan_mag_skill.script` (HarukaSkillSystem). В MO2 ниже Haruka (и Magazines Redux, если есть). При совпадении путей с другим модом нужен патч или ручное слияние.

**Удаление**

- Отключить слот в MO2; новая игра не нужна. Вернётся файл HarukaSkillSystem из нижележащего мода.
- Сейв не трогает. Без этой замены и без Magazines Redux снова SCRIPT ERROR на загрузке utjan_mag_skill.

## [1.0.0] - 2026-09-16

**Изменено**

- `gamedata/scripts/utjan_mag_skill.script` — **полная замена** файла HarukaSkillSystem. Если модуля `magazines` нет (Magazines Redux не установлен), обёртки не ставятся и нет SCRIPT ERROR на загрузке. Если `magazines` есть — те же `load_magazine` / `unload_magazine` wrappers, что в апстриме.

**Причина**

Без Magazines Redux main chunk оригинала падает на `magazines.load_magazine` (строка 4): `attempt to index global 'magazines' (a nil value)`.

**Почему полная замена**

Ошибка в main chunk до любых callback — monkey-patch после загрузки невозможен. DLTX здесь не применим.

**Не затронуто**

- `haru_skills`, `utjan_traits` (бонусы по-прежнему пишут в `mag_loading_bonus`)
- сам Magazines Redux

**Совместимость**

- HarukaSkillSystem; MO2: этот мод / Kristiano AIO **ниже** Haruka (чтобы заменить `utjan_mag_skill.script`)
- С Magazines Redux: ниже Magazines и Haruka
- Сейвы: без изменений

**Проверено**

- lint: `python tools/lint_addon.py fix_utjan_mag_skill`
- в игре: не подтверждено. Ожидание: нет SCRIPT ERROR `utjan_mag_skill.script:4`; в логе `magazines module missing` или `magazines wrappers installed`.
