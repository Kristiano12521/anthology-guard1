#!/usr/bin/env python3
"""Ротация артефактов в build/: оставляет N самых свежих сборок на мод.

По умолчанию ничего не удаляет — только показывает, что ушло бы.
Чтобы удалить, нужен --yes. _staging/ не трогает.

    python3 tools/prune_builds.py --dry-run
    python3 tools/prune_builds.py --yes
    python3 tools/prune_builds.py --yes --keep 2
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import rel  # noqa: E402
from build_prune import default_build_dir, plan_build_prune, prune_build_dir  # noqa: E402

DEFAULT_KEEP = 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Оставить N самых свежих сборок на мод в build/, остальные удалить"
    )
    parser.add_argument(
        "--keep",
        type=int,
        default=DEFAULT_KEEP,
        metavar="N",
        help=f"сколько самых свежих артефактов оставить на группу (по умолчанию {DEFAULT_KEEP})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="показать, что будет удалено, ничего не трогать (поведение по умолчанию)",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="действительно удалить старые сборки",
    )
    parser.add_argument(
        "--build-dir",
        type=Path,
        default=default_build_dir(),
        help="каталог сборок (по умолчанию build/)",
    )
    args = parser.parse_args(argv)

    if args.keep < 0:
        print("--keep не может быть отрицательным", file=sys.stderr)
        return 2
    if args.dry_run and args.yes:
        print("укажите либо --dry-run, либо --yes, не оба", file=sys.stderr)
        return 2

    build_dir = args.build_dir
    if not build_dir.is_dir():
        print(f"нет каталога сборок: {build_dir}", file=sys.stderr)
        return 2

    dry_run = not args.yes
    kept, to_delete = plan_build_prune(build_dir, args.keep)

    if not to_delete:
        print(f"удалять нечего: {len(kept)} артефактов, keep={args.keep}")
        return 0

    verb = "удалил бы" if dry_run else "удалён"
    for path in to_delete:
        print(f"{verb}: {rel(path)}")
    if dry_run:
        print(
            f"Это dry-run ({len(to_delete)} артефактов). "
            "Чтобы удалить, добавьте --yes."
        )
    else:
        prune_build_dir(build_dir, args.keep, dry_run=False)
        print(f"удалено {len(to_delete)}, осталось {len(kept)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
