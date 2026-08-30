import contextlib
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import prune_logs  # noqa: E402


def run(argv: list[str]) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
        code = prune_logs.main(argv)
    return code, buffer.getvalue()


class PruneLogsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.logs = Path(self.tmp.name)
        self.samples = self.logs / "samples"
        self.samples.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _touch(self, path: Path, mtime: int, text: str = "log\n") -> Path:
        path.write_text(text, encoding="utf-8")
        os.utime(path, (mtime, mtime))
        return path

    def test_does_not_touch_samples(self) -> None:
        sample = self._touch(self.samples / "keep_me.log", 1)
        nested = self._touch(self.samples / "crash_lua_nil.log", 2)
        old = self._touch(self.logs / "xray_old.log", 10)
        self._touch(self.logs / "xray_mid.log", 20)
        self._touch(self.logs / "xray_new.log", 30)

        deleted = prune_logs.prune_logs(self.logs, keep=2, dry_run=False)

        self.assertEqual([p.name for p in deleted], ["xray_old.log"])
        self.assertFalse(old.exists())
        self.assertTrue(sample.exists())
        self.assertTrue(nested.exists())
        self.assertEqual(sample.read_text(encoding="utf-8"), "log\n")

    def test_samples_protected_even_if_logs_dir_is_samples(self) -> None:
        sample = self._touch(self.samples / "keep_me.log", 1)
        extra = self._touch(self.samples / "another.log", 2)
        deleted = prune_logs.prune_logs(self.samples, keep=0, dry_run=False)
        self.assertEqual(deleted, [])
        self.assertTrue(sample.exists())
        self.assertTrue(extra.exists())

    def test_dry_run_does_not_delete(self) -> None:
        old = self._touch(self.logs / "xray_old.log", 10)
        self._touch(self.logs / "xray_new.log", 20)
        deleted = prune_logs.prune_logs(self.logs, keep=1, dry_run=True)
        self.assertEqual([p.name for p in deleted], ["xray_old.log"])
        self.assertTrue(old.exists())

    def test_cli_without_yes_does_not_delete(self) -> None:
        old = self._touch(self.logs / "xray_old.log", 10)
        self._touch(self.logs / "xray_a.log", 20)
        self._touch(self.logs / "xray_b.log", 30)
        self._touch(self.logs / "xray_c.log", 40)
        sample = self._touch(self.samples / "keep_me.log", 1)

        code, out = run(["--logs-dir", str(self.logs), "--dry-run", "--keep", "3"])
        self.assertEqual(code, 0)
        self.assertTrue(old.exists())
        self.assertTrue(sample.exists())
        self.assertIn("dry-run", out)
        self.assertIn("xray_old.log", out)

        code, _ = run(["--logs-dir", str(self.logs), "--keep", "3"])
        self.assertEqual(code, 0)
        self.assertTrue(old.exists())

        code, out = run(["--logs-dir", str(self.logs), "--yes", "--keep", "3"])
        self.assertEqual(code, 0)
        self.assertFalse(old.exists())
        self.assertTrue(sample.exists())
        self.assertTrue((self.logs / "xray_c.log").exists())


if __name__ == "__main__":
    unittest.main()
