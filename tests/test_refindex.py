import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import refindex  # noqa: E402

FIXTURE_REFERENCE = REPO_ROOT / "tests" / "fixtures" / "reference"


class IndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.index = refindex.Index.build(FIXTURE_REFERENCE)

    def test_indexes_global_functions_under_both_names(self):
        self.assertIn("play_item_fx", self.index.data["functions"])
        self.assertIn("itms_manager.play_item_fx", self.index.data["functions"])

    def test_indexes_local_functions(self):
        entries = self.index.data["functions"]["reset_cache"]
        self.assertEqual(entries[0][2], "local")

    def test_indexes_method_definitions(self):
        self.assertIn("actor_binder:update", self.index.data["functions"])

    def test_indexes_sections_with_kind(self):
        entries = self.index.data["sections"]["bread"]
        self.assertEqual(entries[0][2], "base")
        self.assertIn("identity_immunities", entries[0][3])

    def test_indexes_dispatched_callbacks(self):
        entries = self.index.data["callbacks"]["actor_on_update"]
        self.assertIn("send", {entry[2] for entry in entries})

    def test_suggests_close_names(self):
        self.assertIn("play_item_fx", self.index.suggest("functions", "play_item_fix"))


class CliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.index_path = Path(self.tmp.name) / "index.json"
        self.base_args = ["--root", str(FIXTURE_REFERENCE), "--index", str(self.index_path)]
        with contextlib.redirect_stdout(io.StringIO()):
            refindex.main(self.base_args + ["build"])

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def run_cli(self, *extra: str) -> tuple[int, str]:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = refindex.main(self.base_args + list(extra))
        return code, buffer.getvalue()

    def test_find_known_function_succeeds(self):
        code, out = self.run_cli("find", "play_item_fx")
        self.assertEqual(code, 0)
        self.assertIn("itms_manager.script", out)
        self.assertIn("ВЫЗОВЫ", out)

    def test_find_unknown_function_fails_loudly(self):
        code, out = self.run_cli("find", "level.add_callback")
        self.assertEqual(code, 1)
        self.assertIn("ОПРЕДЕЛЕНИЙ НЕТ", out)
        self.assertIn("Не подтверждено", out)

    def test_known_section_succeeds(self):
        code, out = self.run_cli("section", "bread")
        self.assertEqual(code, 0)
        self.assertIn("items_food.ltx", out)

    def test_unknown_section_fails(self):
        code, out = self.run_cli("section", "wpn_made_up")
        self.assertEqual(code, 1)
        self.assertIn("СЕКЦИИ НЕТ", out)

    def test_callback_lookup(self):
        code, out = self.run_cli("callback", "actor_on_update")
        self.assertEqual(code, 0)
        self.assertIn("диспатчей: 1", out)

    def test_unknown_callback_warns(self):
        code, out = self.run_cli("callback", "actor_on_teleport_maybe")
        self.assertEqual(code, 1)
        self.assertIn("CALLBACK НЕ НАЙДЕН", out)

    def test_stats(self):
        code, out = self.run_cli("stats")
        self.assertEqual(code, 0)
        self.assertIn("functions:", out)


if __name__ == "__main__":
    unittest.main()
