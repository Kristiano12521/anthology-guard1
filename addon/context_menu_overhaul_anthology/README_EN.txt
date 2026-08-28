CONTEXT MENU OVERHAUL 1.4.2 — ANOMALY ANTHOLOGY 2.1 ADAPTATION
Adaptation version: 1.2.2
Date: 2026-08-29

*** This build includes an unofficial local fix layered on top of the
*** original v1.2.1 BETA by its adapter. It is NOT an official update from
*** that adapter. See CHANGELOG.txt for exactly what changed and why.


NEW IN 1.2.2
------------
- Icons for rows that still had none in 1.2.1 (play guitar, split money,
  mines, camelbak, autodoc, unjam, armor plate, oil refill, pinup, boil,
  ammo breakdown, and others).
- Icon keys are string ids / functors, not Russian literals, so EN works.
- Two DLTX patches were named so they never overlaid the original file
  (OPO helmet icons, magazine retool). Filenames now match DLTX rules.
- Label-to-icon lookup is indexed once instead of translating every
  config key for every row.


NEW IN 1.2.1
------------
Quick Action Wheel compatibility is integrated directly into Context Menu Overhaul.

The context menu uses one native action:

Add to wheel

Behaviour:
- on a manual QAW tab, the item is added to the selected tab;
- on a dynamic tab, the item is routed to the configured Manual Tab;
- Second Manual Tab is used when the primary manual tab is unavailable;
- the action is hidden when the destination tab is full;
- the action is hidden when the item is already present;
- item eligibility is determined by Quick Action Wheel.

No separate compatibility addon is required. The temporary startup callback is
removed after registration and does not remain active during normal gameplay.


UNIVERSAL MAGAZINE RETOOL
-------------------------
The Retool action uses a universal resolver instead of a narrow hardcoded list.

The resolver:
- scans all loaded magazine sections;
- preserves native Mags Redux retool_group routes;
- finds additional links through weapon calibre mappings;
- matches physical magazine families by model, variant and capacity;
- supports compatible magazines from other active mods;
- builds the index once and then uses a cache.

Validation against the supplied R.A.K Mags Redux setup found:
- 237 magazine sections;
- 97 native retool routes;
- 37 additional inferred routes;
- 134 magazines with a real alternate result.

The action is hidden when no valid alternate magazine exists. Fake result
sections are not created.


RETOOL REQUIREMENTS
-------------------
- The magazine must be completely empty.
- A leatherman_tool must be present.
- Multi-calibre families cycle through existing variants.
- Native Mags Redux groups take priority.


COMPATIBILITY
-------------
Preserved:
- inventory, loot and player-side trade support;
- OPO and Exo System;
- R.A.K Mags Redux;
- Toxic Air;
- WPO icons;
- Gift enabled by default;
- standard action grouping from menu.ltx.


INSTALLATION
------------
1. Replace the previous adaptation completely. Do not merge version folders.
2. Install through Mod Organizer 2.
3. Place below:
   - Context Menu Overhaul;
   - Quick Action Wheel;
   - R.A.K Mags Redux;
   - OPO and Exo System;
   - Toxic Air;
   - [DBG] Kristiano Fixes ALL IN ONE.
4. Restart the game completely.

No new game is required.
