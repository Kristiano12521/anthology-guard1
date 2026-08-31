from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import prune_builds  # noqa: E402


def run(argv: list[str]) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
        code = prune_builds.main(argv)
    return code, buffer.getvalue()


class PruneBuildsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.build = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _touch(self, name: str, mtime: int) -> Path:
        path = self.build / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if name.endswith(".zip"):
            path.write_text("zip\n", encoding="utf-8")
        else:
            path.mkdir(exist_ok=True)
            (path / "BUILD_INFO.txt").write_text("x\n", encoding="utf-8")
        os.utime(path, (mtime, mtime))
        return path

    def test_dry_run_does_not_delete(self) -> None:
        old = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2.zip", 10)
        mid = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_6.zip", 20)
        new = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_7.zip", 30)

        code, out = run(["--build-dir", str(self.build), "--dry-run", "--keep", "1"])
        self.assertEqual(code, 0)
        self.assertTrue(old.exists())
        self.assertTrue(mid.exists())
        self.assertTrue(new.exists())
        self.assertIn("dry-run", out)
        self.assertIn("v0_6_2", out)
        self.assertIn("v0_6_6", out)

    def test_default_without_yes_does_not_delete(self) -> None:
        old = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2.zip", 10)
        self._touch("Anthology_BusyHands_Stability_Fix_v0_6_7.zip", 20)

        code, _ = run(["--build-dir", str(self.build), "--keep", "1"])
        self.assertEqual(code, 0)
        self.assertTrue(old.exists())

    def test_yes_keeps_newest_per_group(self) -> None:
        old = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2.zip", 10)
        mid = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_6.zip", 20)
        new = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_7.zip", 30)
        aio_old = self._touch("[DBG] Kristiano Fixes ALL IN ONE.zip", 15)
        aio_new = self._touch("[DBG] Kristiano Fixes ALL IN ONE NEW1.zip", 25)

        code, out = run(["--build-dir", str(self.build), "--yes", "--keep", "1"])
        self.assertEqual(code, 0)
        self.assertFalse(old.exists())
        self.assertFalse(mid.exists())
        self.assertTrue(new.exists())
        self.assertFalse(aio_old.exists())
        self.assertTrue(aio_new.exists())
        self.assertIn("удалено", out)

    def test_staging_not_listed(self) -> None:
        staging = self.build / "_staging"
        staging.mkdir()
        (staging / "tmp.txt").write_text("x\n", encoding="utf-8")
        code, out = run(["--build-dir", str(self.build), "--yes", "--keep", "0"])
        self.assertEqual(code, 0)
        self.assertIn("удалять нечего", out)
        self.assertTrue(staging.exists())


if __name__ == "__main__":
    unittest.main()
