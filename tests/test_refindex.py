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


class SourceRankTests(unittest.TestCase):
    def test_kind_from_reference_child(self):
        self.assertEqual(refindex.source_kind("reference/anomaly/scripts/axr_main.script"), "anomaly")
        self.assertEqual(refindex.source_kind("reference/anthology/scripts/x.script"), "anthology")
        self.assertEqual(refindex.source_kind("reference/addons/mod/scripts/x.script"), "addons")
        self.assertEqual(refindex.source_kind("reference/docs/readme.md"), "other")

    def test_kind_from_fixture_layout(self):
        self.assertEqual(
            refindex.source_kind("tests/fixtures/reference/addons/ranking_mod/scripts/ranking_mod.script"),
            "addons",
        )

    def test_kind_when_path_is_already_inside_reference_root(self):
        self.assertEqual(refindex.source_kind("anomaly/scripts/axr_main.script"), "anomaly")

    def test_labels(self):
        self.assertEqual(refindex.source_label("reference/anomaly/scripts/x.script"), "ваниль")
        self.assertEqual(refindex.source_label("reference/anthology/scripts/x.script"), "anthology")
        self.assertEqual(refindex.source_label("reference/addons/mod/scripts/x.script"), "аддон")
        self.assertEqual(refindex.source_label("reference/misc/x.script"), "прочее")

    def test_priority_order(self):
        paths = [
            "reference/addons/foo/scripts/a.script",
            "reference/docs/note.md",
            "reference/anthology/scripts/a.script",
            "reference/anomaly/scripts/a.script",
        ]
        ranked = sorted(paths, key=lambda p: (refindex.source_priority(p), p))
        self.assertEqual(
            [refindex.source_kind(p) for p in ranked],
            ["anomaly", "anthology", "addons", "other"],
        )

    def test_rank_entries_sorts_by_path_then_line_within_source(self):
        entries = [
            ["reference/anomaly/scripts/b.script", 10, "function", "f()"],
            ["reference/anomaly/scripts/a.script", 20, "function", "f()"],
            ["reference/anomaly/scripts/a.script", 5, "function", "f()"],
        ]
        ranked = refindex.rank_entries(entries)
        self.assertEqual(
            [f"{e[0]}:{e[1]}" for e in ranked],
            [
                "reference/anomaly/scripts/a.script:5",
                "reference/anomaly/scripts/a.script:20",
                "reference/anomaly/scripts/b.script:10",
            ],
        )

    def test_format_omitted_counts_by_source(self):
        omitted = [
            ["reference/anthology/scripts/a.script", 1, "function", "f()"],
            ["reference/addons/m/scripts/a.script", 1, "function", "f()"],
            ["reference/addons/n/scripts/a.script", 1, "function", "f()"],
        ]
        self.assertEqual(
            refindex.format_omitted(omitted),
            "  ещё 3: 1 [anthology], 2 [аддон]",
        )
        self.assertIsNone(refindex.format_omitted([]))


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

    def test_find_lists_vanilla_definition_before_addon(self):
        # Аддон в индексе может быть раньше из-за обхода addons/ < anomaly/.
        index = refindex.Index.load(self.index_path)
        stored = [entry[0] for entry in index.lookup("functions", "play_item_fx")]
        self.assertTrue(any("/addons/" in path for path in stored))
        self.assertTrue(any("/anomaly/" in path for path in stored))

        code, out = self.run_cli("find", "play_item_fx", "--no-usages")
        self.assertEqual(code, 0)
        def_lines = [line for line in out.splitlines() if "play_item_fx(" in line]
        self.assertGreaterEqual(len(def_lines), 3)
        self.assertIn("[ваниль]", def_lines[0])
        self.assertIn("/anomaly/", def_lines[0])
        self.assertIn("[anthology]", def_lines[1])
        self.assertIn("/anthology/", def_lines[1])
        self.assertIn("[аддон]", def_lines[2])
        self.assertIn("/addons/", def_lines[2])

    def test_find_reports_omitted_sources_after_limit(self):
        code, out = self.run_cli("--limit", "1", "find", "play_item_fx", "--no-usages")
        self.assertEqual(code, 0)
        self.assertIn("[ваниль]", out)
        self.assertIn("/anomaly/", out)
        self.assertIn("ещё 2: 1 [anthology], 1 [аддон]", out)
        def_lines = [line for line in out.splitlines() if "play_item_fx(" in line]
        self.assertEqual(len(def_lines), 1)

    def test_find_unknown_function_fails_loudly(self):
        code, out = self.run_cli("find", "level.add_callback")
        self.assertEqual(code, 1)
        self.assertIn("ОПРЕДЕЛЕНИЙ НЕТ", out)
        self.assertIn("Не подтверждено", out)

    def test_known_section_succeeds(self):
        code, out = self.run_cli("section", "bread")
        self.assertEqual(code, 0)
        self.assertIn("items_food.ltx", out)
        self.assertIn("[ваниль]", out)

    def test_unknown_section_fails(self):
        code, out = self.run_cli("section", "wpn_made_up")
        self.assertEqual(code, 1)
        self.assertIn("СЕКЦИИ НЕТ", out)

    def test_callback_lookup(self):
        code, out = self.run_cli("callback", "actor_on_update")
        self.assertEqual(code, 0)
        self.assertIn("диспатчей: 1", out)
        self.assertIn("[ваниль]", out)

    def test_unknown_callback_warns(self):
        code, out = self.run_cli("callback", "actor_on_teleport_maybe")
        self.assertEqual(code, 1)
        self.assertIn("CALLBACK НЕ НАЙДЕН", out)

    def test_stats(self):
        code, out = self.run_cli("stats")
        self.assertEqual(code, 0)
        self.assertIn("functions:", out)


class IterFilesTests(unittest.TestCase):
    def test_walks_dirnames_in_sorted_order(self):
        from _common import iter_files

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("zeta", "alpha", "mu"):
                (root / name).mkdir()
                (root / name / f"{name}.script").write_text("--\n", encoding="utf-8")
            walked = [path.parent.name for path in iter_files(root, {".script"})]
            self.assertEqual(walked, ["alpha", "mu", "zeta"])


if __name__ == "__main__":
    unittest.main()
