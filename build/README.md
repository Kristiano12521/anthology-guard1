# build/ — собранные моды

Результат `tools/build_addon.py`. Содержимое в git не хранится, руками не правится: любая правка здесь потеряется при следующей сборке.

```bash
python3 tools/build_addon.py my_fix_weapon_jam            # build/my_fix_weapon_jam/
python3 tools/build_addon.py my_fix_weapon_jam --zip      # + zip для установщика MO2
python3 tools/build_addon.py my_fix_weapon_jam --install "D:/MO2/mods"
```

Цепочка целиком описана в [`../docs/mo2.md`](../docs/mo2.md).
