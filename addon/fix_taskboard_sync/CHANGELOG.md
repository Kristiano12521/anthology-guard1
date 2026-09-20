# fix_taskboard_sync

**����������:** Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT; ���� `[ANTHFIX] Taskboard + Weather`.

**��������**

- ��������� ���� � MO2; ����� ���� �� �����.
- �������� `save_var` �������� �� ����� ������ / ����� - ����.

## [1.0.0] - 2026-09-20

**��������**

- `gamedata/scripts/z_fix_taskboard_sync.script` - monkey-patch:
  - reuse `save_var` � `setup_bounty_task`, `drx_sl_create_quest_stash`, fetch-setup, `on_init_delivery_task`, `setup_assault_task` / `validate_assault_task`;
  - ���������� `available_tasks` �� ����� ������ ����� `generate_available_tasks`;
  - ��������� `drx_sl_create_quest_stash` -> `setup_fetch_task` �� �����.

**�������**

����� � ������ �������� setup �������� � ������ ������� ����/������� ����� ������. `pairs(CFG_CACHE)` ����� ������ ���� ������� ������������. Stash-������ �� ����� �������� � bounty ��-�� `normalizer`.

**��� ����������**

��� ������ - ������������ actor `save_var` (���������� MT reload; �������� ��������� `on_before_level_changing`, ���� ������� �� �����). ������ `bounty_cache` / `DIALOG_ID` / `cache_stash` ������ �� �������� ������ ����� ��������.

**�� ���������**

- ��� ������ LTX, `repeat_timeout`, balance level_mode assault (��� B).
- ���������/������ ������� (��� C).
- Dominance->assault remapping �� �����.

**�������������**

- �����: ��� ��������; ������ `save_var` �� �������.
- MO2 ���� Taskboard; ����� MT reload wraps ������������������� �� `actor_on_first_update`.

**���������**

- lint: `python tools/lint_addon.py fix_taskboard_sync`
- � ����: �� �����������. ��������: ������ bounty - ���� ���� �� ����� � � �������; ��������� ������� � "���� ���������".
