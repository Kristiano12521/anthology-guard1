from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import modcheck  # noqa: E402

EXPECTED_IDS = [
    "1.1",
    "1.2",
    "1.3",
    "1.4",
    "1.5",
    "1.6",
    "1.note",
    "2.1",
    "2.2",
    "2.3",
    "2.4",
    "2.5",
    "2.6",
    "2.7",
    "3.1",
    "3.2",
    "3.3",
    "3.4",
    "3.5",
    "4.1",
    "4.2",
    "4.3",
    "4.4",
    "4.5",
    "4.6",
    "4.7",
    "5.1",
    "5.2",
    "5.3",
    "5.4",
    "6.1",
    "6.2",
    "6.3",
    "7.1",
    "7.2",
    "7.3",
    "7.4",
    "7.5",
    "7.6",
    "8.1",
    "8.2",
    "8.3",
    "8.4",
    "8.5",
    "8.6",
    "8.7",
    "8.8",
    "8.9",
    "8.10",
    "8.11",
    "8.12",
    "8.13",
    "9.1",
    "9.2",
    "9.3",
    "9.4",
    "9.5",
    "9.6",
    "9.7",
    "9.8",
    "9.9",
    "9.10",
    "9.11",
    "9.12",
    "10.1.1",
    "10.1.2",
    "10.2.1",
    "10.2.2",
    "10.2.3",
    "10.3.1",
    "10.3.2",
    "10.3.3a",
    "10.3.3b",
    "10.3.3c",
]


class DiscordRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = modcheck.load_rules()
        cls.index = modcheck.articles_by_id(cls.data)

    def test_ids_cover_full_code(self):
        self.assertEqual(sorted(self.index), sorted(EXPECTED_IDS))

    def test_articles_have_punishment_and_text(self):
        for aid, article in self.index.items():
            self.assertTrue(article.get("text"), aid)
            self.assertTrue(article.get("punishment"), aid)
            self.assertTrue(article.get("title"), aid)
            self.assertIn(article.get("severity"), modcheck.SEVERITY_ORDER, aid)

    def test_lookup_gamma(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = modcheck.main(["lookup", "5.1"])
        self.assertEqual(code, 0)
        out = buf.getvalue()
        self.assertIn("5.1", out)
        self.assertIn("Гамма", out)
        self.assertIn("мут на 1 час", out)

    def test_scan_gamma_joke(self):
        hits = modcheck.scan_text(self.data, "а вот в гамме это лучше, я просто пошутил")
        ids = [row["id"] for row in hits]
        self.assertIn("5.1", ids)
        self.assertIn("1.note", ids)

    def test_scan_weapon_whine(self):
        hits = modcheck.scan_text(
            self.data,
            "оружейка говно, Шура неправильно настроил отдачу",
        )
        ids = [row["id"] for row in hits]
        self.assertIn("7.3", ids)
        self.assertIn("7.6", ids)
        self.assertIn("8.6", ids)

    def test_scan_leave_threat(self):
        hits = modcheck.scan_text(
            self.data,
            "если вы не исправите оружейку, я удаляю мод",
        )
        ids = [row["id"] for row in hits]
        self.assertIn("8.9", ids)

    def test_scan_empty_has_no_hits(self):
        self.assertEqual(modcheck.scan_text(self.data, "когда патч по багу двери?"), [])

    def test_human_rules_file_exists(self):
        text = (REPO_ROOT / "community" / "RULES.md").read_text(encoding="utf-8")
        self.assertIn("5.1", text)
        self.assertIn("G.A.M.M.A", text)
        self.assertIn("10.3.3", text)


if __name__ == "__main__":
    unittest.main()
