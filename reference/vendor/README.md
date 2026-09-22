# reference/vendor/

Постоянные слепки оригиналов чужих модов, на которых стоят наши форки
(`vendor_source` в `addon/*/meta.ini`).

Сюда класть вручную, например:

- `Anthology_BusyHands_Stability_Fix_v0_6_1`
- Context Menu Overhaul (базовый пакет с `menu.ltx`)
- Campfires placeable (до Compat)
- Seamless Inventory Sort (до нашей замены)

`fill_reference.py` и `fill_reference_addons.py` (включая `--prune`) эту папку
не трогают. Поиск: `reference/vendor/<имя>`, затем `reference/addons/<имя>`.

**Не в git** — чужие работы / лицензии (см. корневой `NOTICE`). При переезде
скопируй всю `reference/vendor/` на новую машину, иначе `pack_bhs` и FORK-001
не найдут оригиналы. Подробнее: `docs/setup.md`.
