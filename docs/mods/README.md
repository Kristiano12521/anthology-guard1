# Рабочие материалы модов

ТЗ, лор-черновики, наброски иконок и прочие файлы, которые **не едут в MO2-пакет**.

## Куда класть

```
docs/mods/<mod_id>/          # один каталог на мод
docs/mods/<mod_id>/lore/     # черновики лора / энциклопедии
docs/mods/<mod_id>/*.txt     # ТЗ, заметки художнику, чек-листы
```

В `addon/<mod_id>/` остаются только то, что ставится в игру: `gamedata/`, `meta.ini`, `CHANGELOG.md` (и опционально `README.md`). Всё остальное на верхнем уровне мода ловит линтер (`STRUCT-004` / `STRUCT-005`) — в zip оно и так не попадёт, но путает структуру.

## Пример

`docs/mods/kristiano_kx1_exo/ICON_TZ.txt` — ТЗ иконки;  
`docs/mods/kristiano_kx1_exo/lore/kx1_encyclopedia.txt` — черновик статьи PDA (в игру уходит уже через `gamedata/configs/text/...`).
