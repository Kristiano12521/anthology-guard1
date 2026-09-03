"""Очистка артефактов сборки в build/ перед новой упаковкой и ротация старых версий."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from _common import REPO_ROOT, rel  # noqa: E402

BHS_MOD_ID = "anthology_busyhands_stability_fix"
BHS_PACK_STEM = "Anthology_BusyHands_Stability_Fix"
AIO_NAME = "[DBG] Kristiano Fixes ALL IN ONE"
SEPARATE_MO2_NAMES = (
    "[HUD] Context Menu_Overhaul_Anthology",
    "[GFX] QuickQK Task Status Tool Anthology "
    "— Принудительное завершение заданий от Kristiano",
    "[SND] Anthology ST2 Mutant Footstep Sound",
    "[FIX] Campfires Anthology Compat",
)
STAGING_DIR_NAME = "_staging"
MOD_ZIP_RE = re.compile(r"^(?P<mod_id>.+)-(\d+\.\d+(?:\.\d+)?)\.zip$")


def classify_build_name(name: str) -> str | None:
    """Ключ группы артефактов или None, если это не сборка мода."""
    if name == STAGING_DIR_NAME:
        return None
    if name.startswith(BHS_PACK_STEM):
        return f"mod:{BHS_MOD_ID}"
    if name == BHS_MOD_ID or name.startswith(f"{BHS_MOD_ID}-"):
        return f"mod:{BHS_MOD_ID}"
    if name.startswith(AIO_NAME):
        return "pack:kristiano_aio"
    if name in SEPARATE_MO2_NAMES or name in {f"{n}.zip" for n in SEPARATE_MO2_NAMES}:
        return f"pack:separate:{name.removesuffix('.zip')}"
    match = MOD_ZIP_RE.match(name)
    if match:
        return f"mod:{match.group('mod_id')}"
    if "/" not in name and "\\" not in name and not name.endswith(".zip"):
        return f"mod:{name}"
    return None


def list_group_artifacts(build_dir: Path, group: str) -> list[Path]:
    """Все артефакты build/ одной группы, от новых к старым."""
    if not build_dir.is_dir():
        return []
    found: list[Path] = []
    for path in build_dir.iterdir():
        key = classify_build_name(path.name)
        if key == group:
            found.append(path)
    return sorted(found, key=lambda p: (-p.stat().st_mtime, p.name))


def plan_group_prune(build_dir: Path, group: str, keep: int) -> tuple[list[Path], list[Path]]:
    """(оставить, удалить) для одной группы."""
    items = list_group_artifacts(build_dir, group)
    if keep < 0:
        raise ValueError("keep must be >= 0")
    return items[:keep], items[keep:]


def delete_artifacts(paths: list[Path], *, dry_run: bool) -> list[Path]:
    deleted: list[Path] = []
    for path in paths:
        if dry_run:
            deleted.append(path)
            continue
        if path.is_dir():
            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()
        deleted.append(path)
    return deleted


def cleanup_before_build(
    build_dir: Path,
    group: str,
    *,
    keep_old: bool = False,
    dry_run: bool = False,
) -> list[Path]:
    """Удалить все предыдущие артефакты группы перед новой сборкой."""
    if keep_old:
        return []
    _, to_delete = plan_group_prune(build_dir, group, keep=0)
    return delete_artifacts(to_delete, dry_run=dry_run)


def list_all_groups(build_dir: Path) -> dict[str, list[Path]]:
    groups: dict[str, list[Path]] = {}
    if not build_dir.is_dir():
        return groups
    for path in build_dir.iterdir():
        key = classify_build_name(path.name)
        if key is None:
            continue
        groups.setdefault(key, []).append(path)
    for key in groups:
        groups[key] = sorted(groups[key], key=lambda p: (-p.stat().st_mtime, p.name))
    return groups


def plan_build_prune(build_dir: Path, keep: int) -> tuple[list[Path], list[Path]]:
    """(оставить, удалить) по всем группам build/."""
    kept: list[Path] = []
    to_delete: list[Path] = []
    for group in sorted(list_all_groups(build_dir)):
        group_kept, group_delete = plan_group_prune(build_dir, group, keep)
        kept.extend(group_kept)
        to_delete.extend(group_delete)
    return kept, to_delete


def prune_build_dir(
    build_dir: Path,
    keep: int = 1,
    *,
    dry_run: bool = True,
) -> list[Path]:
    _, to_delete = plan_build_prune(build_dir, keep)
    return delete_artifacts(to_delete, dry_run=dry_run)


def default_build_dir() -> Path:
    return REPO_ROOT / "build"
