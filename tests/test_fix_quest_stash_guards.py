"""Regression guards for fix_quest_stash item-loss / duplicate-PDA bugs."""

from __future__ import annotations

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = (
    REPO_ROOT
    / "addon"
    / "fix_quest_stash"
    / "gamedata"
    / "scripts"
    / "fix_quest_stash.script"
)


class FixQuestStashGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = SCRIPT.read_text(encoding="utf-8")

    def test_no_blind_shared_type_scan(self) -> None:
        self.assertNotIn("SHARED_TYPES", self.text)
        self.assertIn("leftover_legacy_type", self.text)
        self.assertIn("stash_type_legacy", self.text)

    def test_recover_skips_opened_cache_and_existing_story_item(self) -> None:
        self.assertIn("cache_opened", self.text)
        self.assertIn("story_item_exists", self.text)
        self.assertIn("get_story_se_item", self.text)
        self.assertIn("skip recover", self.text)


if __name__ == "__main__":
    unittest.main()
