#!/usr/bin/env python3
"""Падает, если CHANGELOG описывает tools/, а файлы в tools/ не менялись.

    python tools/check_changelog_tools.py
    python tools/check_changelog_tools.py --base origin/main

Смотрит добавленные строки диффа CHANGELOG.md (не весь файл: в истории
tools/ упоминается часто). Нужен git.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT  # noqa: E402

NULL_SHA = "0" * 40
CHANGELOG = "CHANGELOG.md"
# Путь tools/... — не слово «инструменты» и не docs/tools.md без слэша.
TOOLS_PATH = "tools/"


def posix(path: str) -> str:
    return path.replace("\\", "/")


def added_lines(diff: str) -> list[str]:
    """Строки, добавленные в unified diff; заголовки +++ не считаются."""
    out: list[str] = []
    for line in diff.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            out.append(line[1:])
    return out


def changelog_in(changed_files: list[str]) -> bool:
    return any(posix(path) == CHANGELOG for path in changed_files)


def tools_in(changed_files: list[str]) -> bool:
    for path in changed_files:
        rel = posix(path)
        if rel == "tools" or rel.startswith(TOOLS_PATH):
            return True
    return False


def mentions_tools(lines: list[str]) -> bool:
    return any(TOOLS_PATH in line for line in lines)


def check(changed_files: list[str], changelog_diff: str) -> str | None:
    """Сообщение об ошибке или None, если всё согласовано."""
    if not changelog_in(changed_files):
        return None
    if not mentions_tools(added_lines(changelog_diff)):
        return None
    if tools_in(changed_files):
        return None
    return (
        "CHANGELOG.md в этом диапазоне описывает путь tools/, "
        "но ни один файл под tools/ не менялся. "
        "Либо поправь tools/, либо не пиши в CHANGELOG про несделанное."
    )


def _git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def resolve_base(repo: Path, explicit: str | None) -> str | None:
    raw = (explicit or os.environ.get("CHECK_CHANGELOG_BASE") or "").strip()
    if raw and raw != NULL_SHA and set(raw) != {"0"}:
        return raw
    probe = _git(repo, ["rev-parse", "--verify", "HEAD~1"])
    if probe.returncode == 0:
        return "HEAD~1"
    return None


def changed_files(repo: Path, base: str, head: str) -> list[str]:
    result = _git(repo, ["diff", "--name-only", f"{base}...{head}"])
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or result.stdout.strip() or "git diff --name-only failed")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def changelog_diff(repo: Path, base: str, head: str) -> str:
    result = _git(repo, ["diff", f"{base}...{head}", "--", CHANGELOG])
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or result.stdout.strip() or "git diff CHANGELOG.md failed")
    return result.stdout


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="CHANGELOG.md не должен описывать tools/, если tools/ не менялся"
    )
    parser.add_argument("--base", help="git ref левой стороны (иначе CHECK_CHANGELOG_BASE или HEAD~1)")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--repo", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)

    repo = args.repo
    base = resolve_base(repo, args.base)
    if base is None:
        print("Нет базового коммита — пропуск сверки CHANGELOG с tools/.")
        return 0

    files = changed_files(repo, base, args.head)
    diff = changelog_diff(repo, base, args.head)
    message = check(files, diff)
    if message is None:
        return 0
    print(message, file=sys.stderr)
    print("Изменённые файлы:", file=sys.stderr)
    for path in files:
        print(f"  {path}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
