from __future__ import annotations

import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import check_changelog_tools as guard  # noqa: E402

GIT_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "Test",
    "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test",
    "GIT_COMMITTER_EMAIL": "test@example.com",
}


def unified(added: list[str], *, filename: str = "CHANGELOG.md") -> str:
    lines = [
        f"--- a/{filename}",
        f"+++ b/{filename}",
        "@@ -1,0 +1,{} @@".format(len(added)),
    ]
    lines.extend(f"+{line}" for line in added)
    return "\n".join(lines) + "\n"


class CheckLogicTests(unittest.TestCase):
    def test_changelog_claims_tools_but_tools_untouched(self):
        diff = unified(["`tools/xraylog.py` теперь группирует traceback."])
        msg = guard.check(["CHANGELOG.md", "docs/plans/crash.md"], diff)
        self.assertIsNotNone(msg)
        self.assertIn("tools/", msg)
        self.assertIn(guard.TOOLS_REF_MARK, msg)

    def test_ok_when_tools_also_changed(self):
        diff = unified(["`tools/xraylog.py`: заголовок группы не из abort()."])
        msg = guard.check(["CHANGELOG.md", "tools/xraylog.py"], diff)
        self.assertIsNone(msg)

    def test_ok_when_new_entry_does_not_mention_tools(self):
        diff = unified(["Правило XML: строковые таблицы и кодировка."])
        msg = guard.check(["CHANGELOG.md"], diff)
        self.assertIsNone(msg)

    def test_ok_when_changelog_not_in_diff(self):
        diff = unified(["`tools/foo.py` неважно: файл не в списке изменений."])
        msg = guard.check(["tools/foo.py"], diff)
        self.assertIsNone(msg)

    def test_tools_ref_marker_allows_mention_without_tools_change(self):
        """Ссылка на инструмент с (tools-ref) — не заявление о правке."""
        diff = unified(
            [
                "поиск по эталону через `tools/refindex.py`, "
                "не через семантический индекс Cursor. (tools-ref)"
            ]
        )
        files = [
            "CHANGELOG.md",
            ".cursorignore",
            "AGENTS.md",
            ".cursor/rules/anomaly-core.mdc",
        ]
        self.assertIsNone(guard.check(files, diff))

    def test_tools_claim_without_marker_still_fails(self):
        """Правка tools/ в тексте без (tools-ref) и без изменений в tools/ — ошибка."""
        diff = unified(["`tools/check_changelog_tools.py`: подавление ложных срабатываний."])
        msg = guard.check(["CHANGELOG.md", "tests/test_check_changelog_tools.py"], diff)
        self.assertIsNotNone(msg)
        self.assertIn("tools/", msg)

    def test_tools_ref_marker_must_be_at_line_end(self):
        diff = unified(["(tools-ref) см. `tools/refindex.py` в середине."])
        msg = guard.check(["CHANGELOG.md"], diff)
        self.assertIsNotNone(msg)

    def test_df81d5f_wording_with_marker_passes(self):
        """Текст записи 0.1.55 (коммит df81d5f) + (tools-ref) — guard молчит."""
        line = (
            "`.cursorignore`: каталог `reference/` (~14k файлов) исключён целиком — "
            "поиск по эталону через `tools/refindex.py`, не через семантический индекс "
            "Cursor; `logs/cards/` тоже вне индекса (чтение адресно при `/crash`). "
            "Убраны `!reference/**` и бинарные исключения внутри `reference/`. "
            "Правила и команды: `anomaly-core`, `no-hallucinated-api`, "
            "`workflow-fix`/`workflow-addon`, `/crash`, зеркало в `AGENTS.md` — явно "
            "`refindex.py` / адресный Read, без семантического обхода `reference/`. "
            "(tools-ref)"
        )
        files = [
            ".cursor/commands/crash.md",
            ".cursor/rules/anomaly-core.mdc",
            ".cursor/rules/no-hallucinated-api.mdc",
            ".cursor/rules/workflow-addon.mdc",
            ".cursor/rules/workflow-fix.mdc",
            ".cursorignore",
            "AGENTS.md",
            "CHANGELOG.md",
        ]
        self.assertIsNone(guard.check(files, unified([line])))

    def test_plus_plus_plus_header_is_not_an_added_line(self):
        diff = "+++ b/CHANGELOG.md\n--- a/CHANGELOG.md\n@@ -1 +1 @@\n правило XML\n"
        self.assertEqual(guard.added_lines(diff), [])
        self.assertIsNone(guard.check(["CHANGELOG.md"], diff))

    def test_removed_tools_mention_does_not_fail(self):
        diff = (
            "--- a/CHANGELOG.md\n"
            "+++ b/CHANGELOG.md\n"
            "@@ -1 +1 @@\n"
            "-`tools/xraylog.py` старая строка\n"
            "+только документация правил\n"
        )
        self.assertIsNone(guard.check(["CHANGELOG.md"], diff))

    def test_windows_slash_in_changed_files(self):
        diff = unified(["см. tools/pack_bhs.py"])
        msg = guard.check(["CHANGELOG.md", "tools\\pack_bhs.py"], diff)
        self.assertIsNone(msg)


class GitRepoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        self._git("init")
        (self.repo / "README.md").write_text("start\n", encoding="utf-8")
        self._git("add", "README.md")
        self._git("commit", "-m", "init")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _git(self, *args: str) -> None:
        subprocess.run(
            ["git", "-c", "user.name=Test", "-c", "user.email=test@example.com", *args],
            cwd=self.repo,
            check=True,
            capture_output=True,
            env=GIT_ENV,
            text=True,
        )

    def test_cli_fails_on_changelog_only_tools_claim(self):
        (self.repo / "CHANGELOG.md").write_text(
            "## [0.1.99]\n\n`tools/xraylog.py` якобы починен.\n",
            encoding="utf-8",
        )
        self._git("add", "CHANGELOG.md")
        self._git("commit", "-m", "changelog without tools")
        buffer = io.StringIO()
        with contextlib.redirect_stderr(buffer):
            code = guard.main(["--repo", str(self.repo), "--base", "HEAD~1"])
        self.assertEqual(code, 1)
        self.assertIn("tools/", buffer.getvalue())

    def test_cli_passes_when_tools_file_changes(self):
        tools = self.repo / "tools"
        tools.mkdir()
        (tools / "xraylog.py").write_text("print(1)\n", encoding="utf-8")
        (self.repo / "CHANGELOG.md").write_text(
            "## [0.1.99]\n\n`tools/xraylog.py` реально починен.\n",
            encoding="utf-8",
        )
        self._git("add", "CHANGELOG.md", "tools/xraylog.py")
        self._git("commit", "-m", "changelog and tools")
        code = guard.main(["--repo", str(self.repo), "--base", "HEAD~1"])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
