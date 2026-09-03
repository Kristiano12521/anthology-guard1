# Bug-finding memories

Tracked critical bugs with open or rejected PRs. Do not re-open a duplicate while status is `open` or `rejected` (unless code materially changed after rejection). Delete merged entries; delete rejected entries older than 30 days.

| Bug (location + root cause) | PR | Status | Recorded |
| --- | --- | --- | --- |
| `fix_quest_stash`: blind SHARED_TYPES 1–7 `alife_release` steals leftover PDAs; `recover_missing` treats `caches[id]==true` as missing and duplicates PDA / skips loot | https://github.com/Kristiano12521/anthology-guard1/pull/2 | open | 2026-09-03 |
