"""Регрессионные проверки fix_quest_stash: кража предметов / дубль КПК."""

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
        cls.text = SCRIPT.read_text(encoding="utf-8", errors="replace")
        # Игровой .script — Windows-1251; для поиска ASCII-маркеров этого достаточно.
        raw = SCRIPT.read_bytes()
        try:
            cls.text_cp = raw.decode("cp1251")
        except UnicodeDecodeError:
            cls.text_cp = cls.text

    def test_no_blind_shared_type_scan(self) -> None:
        self.assertNotIn("SHARED_TYPES", self.text_cp)
        self.assertIn("leftover_legacy_type", self.text_cp)
        self.assertIn("stash_type_legacy", self.text_cp)

    def test_recover_skips_opened_cache_and_existing_story_item(self) -> None:
        self.assertIn("cache_opened", self.text_cp)
        self.assertIn("story_item_exists", self.text_cp)
        self.assertIn("get_story_se_item", self.text_cp)
        self.assertIn("пропуск recover", self.text_cp)


if __name__ == "__main__":
    unittest.main()
