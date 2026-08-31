from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

from _common import detect_version  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class DetectVersionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addon = Path(self.tmp.name) / "my_mod"
        self.addon.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_changelog_heading(self):
        write(self.addon / "CHANGELOG.md", "# Mod\n\n## [0.6.7] — 2026-08-31\n")
        write(self.addon / "meta.ini", "version=0.0.1\n")
        self.assertEqual(detect_version(self.addon), "0.6.7")

    def test_changelog_txt(self):
        write(self.addon / "CHANGELOG.txt", "## v1.2.3\n")
        self.assertEqual(detect_version(self.addon), "1.2.3")

    def test_meta_ini_when_no_changelog(self):
        write(self.addon / "meta.ini", "[General]\nversion=4.5.6\n")
        self.assertEqual(detect_version(self.addon), "4.5.6")

    def test_default_when_nothing(self):
        self.assertEqual(detect_version(self.addon), "1.0.0")


if __name__ == "__main__":
    unittest.main()
