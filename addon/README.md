# addon/ — мои моды

Единственное место, где создаются и меняются игровые файлы.

Один мод — одна папка:

```
addon/
└─ my_fix_weapon_jam/
   ├─ meta.ini
   ├─ CHANGELOG.md
   └─ gamedata/
      ├─ scripts/
      │  ├─ my_fix_weapon_jam.script
      │  └─ my_fix_weapon_jam_mcm.script
      └─ configs/
         └─ weapons/mod_w_ak74_my_fix_weapon_jam.ltx
```

Создать:

```bash
python3 tools/new_addon.py my_fix_weapon_jam --title "Weapon Jam Fix"
```

Проверить и собрать:

```bash
python3 tools/lint_addon.py my_fix_weapon_jam
python3 tools/build_addon.py my_fix_weapon_jam --zip
```

Соглашения:

- Диагностика — отдельный мод или как минимум отдельный файл `*_diag.script` с шапкой `-- DIAGNOSTIC ONLY`.
- Конфиги правятся DLTX-патчами `mod_*.ltx`, скрипты — monkey-patch'ем. Полная копия файла сборки — крайний случай с обоснованием в `CHANGELOG.md`.
- `CHANGELOG.md` заполняется в том же коммите, что и правка.
