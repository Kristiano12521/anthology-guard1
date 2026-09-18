# fix_matches_campfire_softlock

Снимает soft-lock при разжигании костра спичками (FDDA `zzz_matches_anim`): если анимация не завершилась, через 8 секунд принудительно включает ввод.

## Установка (MO2)

1. Собрать: `python tools/build_addon.py fix_matches_campfire_softlock`
2. Включить мод **после** `[TMA] FDDA Redone`.

## Проверка в логе

```
[fix_matches_campfire_softlock] loaded v1.0.0
[fix_matches_campfire_softlock] guard installed v1.0.0 timeout=8s
```

При срабатывании таймаута:

```
[fix_matches_campfire_softlock] force_unlock reason=timeout
```
