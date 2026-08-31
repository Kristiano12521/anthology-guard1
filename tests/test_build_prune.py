from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import build_prune  # noqa: E402
import pack_bhs  # noqa: E402


class BuildPruneTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.build = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _touch(self, name: str, mtime: int) -> Path:
        path = self.build / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if name.endswith(".zip") or "/" not in name and not name.endswith(".zip"):
            if not name.endswith(".zip") and not path.exists():
                path.mkdir(exist_ok=True)
                (path / "BUILD_INFO.txt").write_text("x\n", encoding="utf-8")
            elif name.endswith(".zip"):
                path.write_text("zip\n", encoding="utf-8")
        os.utime(path, (mtime, mtime))
        return path

    def test_classify_bhs_patterns(self) -> None:
        self.assertEqual(
            build_prune.classify_build_name("Anthology_BusyHands_Stability_Fix_v0_6_7"),
            f"mod:{build_prune.BHS_MOD_ID}",
        )
        self.assertEqual(
            build_prune.classify_build_name("Anthology_BusyHands_Stability_Fix_v0_6_7.zip"),
            f"mod:{build_prune.BHS_MOD_ID}",
        )
        self.assertEqual(
            build_prune.classify_build_name("anthology_busyhands_stability_fix-0.6.4.zip"),
            f"mod:{build_prune.BHS_MOD_ID}",
        )

    def test_cleanup_before_build_removes_all_group_artifacts(self) -> None:
        old_dir = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2", 10)
        old_zip = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_3.zip", 20)
        other_zip = self._touch("anthology_busyhands_stability_fix-0.6.4.zip", 30)
        keep = self._touch("keep_me", 40)

        deleted = build_prune.cleanup_before_build(
            self.build,
            f"mod:{build_prune.BHS_MOD_ID}",
            keep_old=False,
        )

        self.assertEqual(
            {p.name for p in deleted},
            {
                "Anthology_BusyHands_Stability_Fix_v0_6_2",
                "Anthology_BusyHands_Stability_Fix_v0_6_3.zip",
                "anthology_busyhands_stability_fix-0.6.4.zip",
            },
        )
        self.assertFalse(old_dir.exists())
        self.assertFalse(old_zip.exists())
        self.assertFalse(other_zip.exists())
        self.assertTrue(keep.exists())

    def test_cleanup_before_build_keep_old(self) -> None:
        old_zip = self._touch("Anthology_BusyHands_Stability_Fix_v0_6_2.zip", 10)
        deleted = build_prune.cleanup_before_build(
            self.build,
            f"mod:{build_prune.BHS_MOD_ID}",
            keep_old=True,
        )
        self.assertEqual(deleted, [])
        self.assertTrue(old_zip.exists())

    def test_pack_bhs_cleans_old_versions(self) -> None:
        repo = REPO_ROOT
        overlay = repo / "addon" / "anthology_busyhands_stability_fix"
        if not overlay.is_dir():
            self.skipTest("overlay fixture missing in repo")

        vendor = repo / "reference" / "addons"
        if not any("BusyHands" in p.name for p in vendor.iterdir() if p.is_dir()):
            self.skipTest("BusyHands vendor missing in reference/")

        import contextlib
        import io
        import shutil

        tmp_repo = self.build / "repo"
        shutil.copytree(repo / "addon", tmp_repo / "addon")
        shutil.copytree(repo / "reference", tmp_repo / "reference")
        (tmp_repo / "build").mkdir()

        stale = tmp_repo / "build" / "Anthology_BusyHands_Stability_Fix_v0_6_2.zip"
        stale.write_text("old\n", encoding="utf-8")
        stale2 = tmp_repo / "build" / "anthology_busyhands_stability_fix-0.6.1.zip"
        stale2.write_text("old\n", encoding="utf-8")

        with contextlib.redirect_stdout(io.StringIO()):
            archive = pack_bhs.pack(tmp_repo, keep_old=False)

        self.assertTrue(archive.is_file())
        self.assertFalse(stale.exists())
        self.assertFalse(stale2.exists())


if __name__ == "__main__":
    unittest.main()
