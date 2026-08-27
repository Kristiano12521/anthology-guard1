#!/usr/bin/env python3
"""Собирает мод из addon/ в build/ и, по желанию, ставит его в MO2.

Между кодом и игрой стоит явный шаг сборки: сломанный эксперимент откатывается
галочкой в менеджере модов, а не восстановлением файлов сборки.

    python3 tools/build_addon.py my_fix_weapon_jam
    python3 tools/build_addon.py my_fix_weapon_jam --zip
    python3 tools/build_addon.py my_fix_weapon_jam --install "D:/MO2/mods"
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, decode_bytes, rel  # noqa: E402
from lint_addon import ReferenceView, lint  # noqa: E402
from refindex import DEFAULT_ROOT  # noqa: E402

ADDON_ROOT = REPO_ROOT / "addon"
BUILD_ROOT = REPO_ROOT / "build"

VERSION_RE = re.compile(r"^##\s*\[?v?(\d+\.\d+(?:\.\d+)?)\]?", re.M)
META_VERSION_RE = re.compile(r"^version\s*=.*$", re.M)


def detect_version(addon_dir: Path) -> str:
    changelog = addon_dir / "CHANGELOG.md"
    if changelog.exists():
        match = VERSION_RE.search(decode_bytes(changelog.read_bytes()))
        if match:
            return match.group(1)
    return "1.0.0"


def git_revision() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return "unknown"


def copy_tree(source: Path, destination: Path) -> int:
    count = 0
    for path in sorted(source.rglob("*")):
        if path.is_dir():
            continue
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        count += 1
    return count


def build_one(addon_dir: Path, args: argparse.Namespace, reference: ReferenceView) -> int:
    mod_id = addon_dir.name
    version = args.version or detect_version(addon_dir)

    if not args.skip_lint:
        findings = lint(addon_dir, reference)
        errors = [f for f in findings if f.severity == "error"]
        warns = [f for f in findings if f.severity == "warn"]
        if errors and not args.force:
            print(f"{mod_id}: сборка остановлена, {len(errors)} ошибок линтера:")
            for finding in errors:
                print(finding.format())
            print("  Исправь или собери с --force.")
            return 1
        if warns:
            print(f"{mod_id}: предупреждений линтера — {len(warns)} (сборка продолжается)")

    gamedata = addon_dir / "gamedata"
    if not gamedata.is_dir():
        print(f"{mod_id}: нет gamedata/ — нечего собирать.", file=sys.stderr)
        return 1

    out_dir = args.out / mod_id
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    files = copy_tree(gamedata, out_dir / "gamedata")

    meta_source = addon_dir / "meta.ini"
    if meta_source.exists():
        meta_text = decode_bytes(meta_source.read_bytes())
        meta_text = META_VERSION_RE.sub(f"version={version}", meta_text)
        (out_dir / "meta.ini").write_text(meta_text, encoding="utf-8")

    changelog = addon_dir / "CHANGELOG.md"
    if changelog.exists():
        shutil.copy2(changelog, out_dir / "CHANGELOG.md")

    (out_dir / "BUILD_INFO.txt").write_text(
        "\n".join(
            [
                f"mod_id: {mod_id}",
                f"version: {version}",
                f"built: {datetime.now().isoformat(timespec='seconds')}",
                f"source_revision: {git_revision()}",
                f"gamedata_files: {files}",
                "target: Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"{mod_id}: собрано {files} файлов -> {rel(out_dir)} (версия {version})")

    if args.zip:
        archive = args.out / f"{mod_id}-{version}.zip"
        if archive.exists():
            archive.unlink()
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(out_dir.rglob("*")):
                if path.is_file():
                    zf.write(path, path.relative_to(out_dir).as_posix())
        print(f"{mod_id}: архив {rel(archive)} — ставится в MO2 через Install mod from archive")

    if args.install:
        destination = args.install / mod_id
        if destination.exists():
            if not args.force and any(destination.iterdir()):
                print(
                    f"{mod_id}: {destination} уже существует. Перезаписать: --force",
                    file=sys.stderr,
                )
                return 1
            shutil.rmtree(destination)
        copy_tree(out_dir, destination)
        print(f"{mod_id}: установлено в {destination} — включи мод в списке MO2")

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Сборка мода для MO2")
    parser.add_argument("mod_id", nargs="*", help="моды в addon/ (по умолчанию все)")
    parser.add_argument("--out", type=Path, default=BUILD_ROOT)
    parser.add_argument("--addon-root", type=Path, default=ADDON_ROOT)
    parser.add_argument("--reference", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--version", help="переопределить версию (по умолчанию из CHANGELOG.md)")
    parser.add_argument("--zip", action="store_true", help="дополнительно собрать архив")
    parser.add_argument("--install", type=Path, help="папка mods в MO2")
    parser.add_argument("--skip-lint", action="store_true")
    parser.add_argument("--force", action="store_true", help="собрать несмотря на ошибки линтера")
    args = parser.parse_args(argv)

    if args.mod_id:
        targets = [args.addon_root / name for name in args.mod_id]
    else:
        targets = [p for p in sorted(args.addon_root.glob("*")) if p.is_dir()]

    missing = [t for t in targets if not t.is_dir()]
    for target in missing:
        print(f"Нет такого мода: {rel(target)}", file=sys.stderr)
    targets = [t for t in targets if t.is_dir()]
    if not targets:
        print("Нечего собирать.", file=sys.stderr)
        return 2

    reference = ReferenceView.load(args.reference)
    args.out.mkdir(parents=True, exist_ok=True)

    status = 0
    for target in targets:
        status |= build_one(target, args, reference)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
