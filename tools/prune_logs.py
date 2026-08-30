#!/usr/bin/env python3
"""Ротация сырых логов X-Ray: оставляет N самых свежих logs/*.log.

По умолчанию ничего не удаляет — только показывает, что ушло бы.
Чтобы удалить, нужен --yes. logs/samples/ не трогает никогда.

    python3 tools/prune_logs.py --dry-run
    python3 tools/prune_logs.py --yes
    python3 tools/prune_logs.py --yes --keep 5
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, rel  # noqa: E402

DEFAULT_LOGS_DIR = REPO_ROOT / "logs"
DEFAULT_KEEP = 3
SAMPLES_DIR_NAME = "samples"


def is_protected(path: Path) -> bool:
    """True, если путь внутри samples/ — такие файлы не удаляем."""
    return SAMPLES_DIR_NAME in path.resolve().parts


def list_raw_logs(logs_dir: Path) -> list[Path]:
    """logs/*.log в корне каталога, без samples/ и без рекурсии."""
    if not logs_dir.is_dir():
        return []
    found: list[Path] = []
    for path in logs_dir.glob("*.log"):
        if not path.is_file():
            continue
        if is_protected(path):
            continue
        found.append(path)
    return sorted(found, key=lambda p: (-p.stat().st_mtime, p.name))


def plan_prune(logs_dir: Path, keep: int) -> tuple[list[Path], list[Path]]:
    """(оставить, удалить). keep — сколько самых свежих сохранить."""
    logs = list_raw_logs(logs_dir)
    return logs[:keep], logs[keep:]


def prune_logs(logs_dir: Path, keep: int = DEFAULT_KEEP, *, dry_run: bool = True) -> list[Path]:
    """Удаляет (или только перечисляет) логи сверх keep. Возвращает список на удаление."""
    _, to_delete = plan_prune(logs_dir, keep)
    if not dry_run:
        for path in to_delete:
            if is_protected(path):
                continue
            path.unlink()
    return to_delete


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Оставить N самых свежих logs/*.log, остальные удалить"
    )
    parser.add_argument(
        "--keep",
        type=int,
        default=DEFAULT_KEEP,
        metavar="N",
        help=f"сколько самых свежих логов оставить (по умолчанию {DEFAULT_KEEP})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="показать, что будет удалено, ничего не трогать (поведение по умолчанию)",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="действительно удалить старые логи",
    )
    parser.add_argument(
        "--logs-dir",
        type=Path,
        default=DEFAULT_LOGS_DIR,
        help="каталог логов (по умолчанию logs/)",
    )
    args = parser.parse_args(argv)

    if args.keep < 0:
        print("--keep не может быть отрицательным", file=sys.stderr)
        return 2
    if args.dry_run and args.yes:
        print("укажите либо --dry-run, либо --yes, не оба", file=sys.stderr)
        return 2

    logs_dir = args.logs_dir
    if not logs_dir.is_dir():
        print(f"нет каталога логов: {logs_dir}", file=sys.stderr)
        return 2

    dry_run = not args.yes
    kept, to_delete = plan_prune(logs_dir, args.keep)

    if not to_delete:
        print(f"удалять нечего: {len(kept)} логов, keep={args.keep}")
        return 0

    verb = "удалил бы" if dry_run else "удалён"
    for path in to_delete:
        print(f"{verb}: {rel(path)}")
    if dry_run:
        print(
            f"Это dry-run ({len(to_delete)} файлов). "
            "Чтобы удалить, добавьте --yes."
        )
    else:
        prune_logs(logs_dir, args.keep, dry_run=False)
        print(f"удалено {len(to_delete)}, осталось {len(kept)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
