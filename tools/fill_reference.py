#!/usr/bin/env python3
"""Наполняет reference/anomaly/ и reference/anthology/ из db-архивов игры.

Ищет .db / .dbN / .xdb в <игра>/db (включая вложенные), читает TOC через
xdb_unpack, пишет только scripts/, configs/, text/. Текстуры, модели, звуки,
шейдеры и уровни пропускаются. reference/addons/ не трогает — аддоны ставятся
из MO2 отдельно.

Куда класть архив: если в относительном пути от db/ есть «anthology» —
в reference/anthology/, иначе в reference/anomaly/. Это имя файла/папки,
не содержимое архива: ваниль и Anthology в одном инстансе различаются
архивами вроде scripts.db0 vs scripts_anthology.db0.

    python3 tools/fill_reference.py "C:/games/Anomaly"
    python3 tools/fill_reference.py "C:/games/Anomaly" --dry-run
    python3 tools/fill_reference.py "C:/games/Anomaly" --reference reference/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import xdb_unpack  # noqa: E402
from _common import REPO_ROOT  # noqa: E402

KEEP_DIRS = ("scripts", "configs", "text")
ADDONS_DIR_NAME = "addons"
DEFAULT_REFERENCE = REPO_ROOT / "reference"


def classify_archive(archive: Path, db_root: Path) -> str:
    """'anthology' если в пути от db/ есть anthology, иначе 'anomaly'."""
    try:
        relative = archive.resolve().relative_to(db_root.resolve())
    except ValueError:
        relative = Path(archive.name)
    parts = [archive.stem.lower(), *[p.lower() for p in relative.parts]]
    if any("anthology" in part for part in parts):
        return "anthology"
    return "anomaly"


def dest_relative(entry_name: str) -> str | None:
    """Путь внутри anomaly/ или anthology/, либо None — файл не для reference/.

    Берётся первый каталог scripts|configs|text в пути. Префикс gamedata/
    отбрасывается вместе со всем, что левее. Каталоги (хвост \\ или /) — None.
    """
    if entry_name.endswith(("\\", "/")):
        return None
    parts = [p for p in entry_name.replace("\\", "/").split("/") if p]
    if not parts:
        return None
    lower = [p.lower() for p in parts]
    for index, part in enumerate(lower):
        if part in KEEP_DIRS:
            return "/".join(parts[index:])
    return None


def should_keep(entry_name: str, size_real: int = 1) -> bool:
    if size_real <= 0:
        return False
    return dest_relative(entry_name) is not None


def resolve_db_dir(game: Path) -> Path:
    db_dir = game / "db"
    if not db_dir.is_dir():
        raise FileNotFoundError(f"нет папки db/ в {game}")
    return db_dir


def write_if_changed(dest: Path, data: bytes) -> str:
    """'written' | 'unchanged'. Не удаляет лишние файлы."""
    if dest.exists() and dest.is_file() and dest.read_bytes() == data:
        return "unchanged"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return "written"


def process_archive(
    archive: Path,
    db_root: Path,
    reference_root: Path,
    *,
    dry_run: bool,
) -> tuple[str, list[str], int, int]:
    """Возвращает (bucket, dest_rel paths kept, written, unchanged)."""
    bucket = classify_archive(archive, db_root)
    dest_root = reference_root / bucket
    entries = xdb_unpack.read_toc(archive)
    kept: list[str] = []
    written = 0
    unchanged = 0
    for entry in entries:
        relative = dest_relative(entry.name)
        if relative is None or entry.is_dir or entry.size_real <= 0:
            continue
        kept.append(relative)
        if dry_run:
            continue
        try:
            data = xdb_unpack.read_entry(archive, entry)
        except (ValueError, OSError) as exc:
            print(f"  пропуск {relative}: {exc}", file=sys.stderr)
            continue
        status = write_if_changed(dest_root.joinpath(*relative.split("/")), data)
        if status == "written":
            written += 1
        else:
            unchanged += 1
    return bucket, kept, written, unchanged


def fill_reference(
    game: Path,
    reference_root: Path,
    *,
    dry_run: bool = False,
) -> dict[str, int]:
    db_root = resolve_db_dir(game)
    archives = xdb_unpack.find_archives(db_root)
    counts = {"anomaly": 0, "anthology": 0, "written": 0, "unchanged": 0, "archives": 0}

    if not archives:
        print(f"в {db_root} архивов .db/.xdb не найдено")
        return counts

    addons_root = (reference_root / ADDONS_DIR_NAME).resolve()

    for archive in archives:
        try:
            bucket, kept, written, unchanged = process_archive(
                archive, db_root, reference_root, dry_run=dry_run
            )
        except ValueError as exc:
            print(f"не архив X-Ray, пропуск {archive}: {exc}", file=sys.stderr)
            continue

        dest_root = (reference_root / bucket).resolve()
        if addons_root == dest_root or addons_root in dest_root.parents:
            print(f"отказ писать в {ADDONS_DIR_NAME}/: {archive}", file=sys.stderr)
            continue

        counts["archives"] += 1
        counts[bucket] += len(kept)
        counts["written"] += written
        counts["unchanged"] += unchanged

        try:
            shown = archive.resolve().relative_to(db_root.resolve()).as_posix()
        except ValueError:
            shown = archive.name
        action = "будет" if dry_run else "взято"
        print(
            f"{shown}  →  reference/{bucket}/  "
            f"({action} {len(kept)} файлов из {'/'.join(KEEP_DIRS)})"
        )
        if dry_run:
            for relative in kept:
                print(f"  {relative}")

    return counts


def print_summary(counts: dict[str, int], *, dry_run: bool) -> None:
    total = counts["anomaly"] + counts["anthology"]
    verb = "попало бы" if dry_run else "легло"
    print()
    print(
        f"Итого {verb} {total} файлов: "
        f"reference/anomaly/ {counts['anomaly']}, "
        f"reference/anthology/ {counts['anthology']} "
        f"(архивов просмотрено: {counts['archives']})."
    )
    if not dry_run:
        print(
            f"записано новых/изменённых: {counts['written']}, "
            f"без изменений: {counts['unchanged']}."
        )
    print("Аддоны в reference/addons/ этот скрипт не трогает — их кладут из MO2 отдельно.")
    print("Дальше: python3 tools/refindex.py build")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Наполнить reference/anomaly и reference/anthology из db/ игры"
    )
    parser.add_argument("game", type=Path, help="папка установленной игры (внутри ожидается db/)")
    parser.add_argument(
        "--reference",
        type=Path,
        default=DEFAULT_REFERENCE,
        help="корень reference/ (по умолчанию в репозитории)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="показать архивы и файлы, ничего не писать",
    )
    args = parser.parse_args(argv)

    game = args.game
    if not game.is_dir():
        print(f"нет папки игры: {game}", file=sys.stderr)
        return 2
    try:
        counts = fill_reference(game, args.reference, dry_run=args.dry_run)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print_summary(counts, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
