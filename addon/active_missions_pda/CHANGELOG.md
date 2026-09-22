# Changelog — Active Missions PDA Tab (Anthology)

## 1.2.0 — 2026-09-22

- Порт Active Missions PDA Tab 1.2 (ModDB) под Anomaly 1.5.3 / Anthology 2.1.
- Русские строки: вычитан перевод UI/MCM (термины Anthology/Taskboard «Объявления», короткие типы заданий).
- Override `zzzz_pda_tabs_pager.script`: `eptActiveMissions` сразу после Area Map в `real_order`, чтобы вкладка попадала в пейджер Anthology.
- DXML-инжектор не rescale'ит полосу вкладок, если загружен `zzzz_pda_tabs_pager` (геометрией владеет пейджер).
- В классификатор типов добавлены story-functor'ы Anthology (`redemption_*`, `hidden_threat_*`, `agr_u_bandit_boss_*`).
- Отдельный zip для MO2; **не** входит в `[DBG] Kristiano Fixes ALL IN ONE`.
