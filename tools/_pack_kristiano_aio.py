#!/usr/bin/env python3
"""One-off packer: Kristiano ALL IN ONE + three standalone mods."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pack_bhs  # noqa: E402

from _common import REPO_ROOT, decode_bytes, detect_version  # noqa: E402

ADDON_ROOT = REPO_ROOT / "addon"
OUT_DIR = REPO_ROOT / "build"

SEPARATE = {
    "context_menu_overhaul_anthology": "[HUD] Context Menu_Overhaul_Anthology",
    "quickqk_task_complete": (
        "[GFX] QuickQK Task Status Tool Anthology "
        "— Принудительное завершение заданий от Kristiano"
    ),
    "fix_st2_footstep": "[SND] Anthology ST2 Mutant Footstep Sound",
}

# Raw addon/ copy is wrong for BHS — merged via pack_bhs.stage_gamedata in pack_aio.
# fix_bhs_fdda_loot withdrawn: logic lives in BusyHands 0.6.4+.
SKIP = {"anthology_busyhands_stability_fix", "fix_bhs_fdda_loot"}
BHS_MOD_ID = "anthology_busyhands_stability_fix"

AIO_NAME = "[DBG] Kristiano Fixes ALL IN ONE"


def copy_gamedata(source: Path, destination: Path) -> int:
    count = 0
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        count += 1
    return count


def copy_docs(addon_dir: Path, dest: Path) -> None:
    for name in (
        "README.md",
        "README_RU.txt",
        "README_EN.txt",
        "CHANGELOG.md",
        "CHANGELOG.txt",
        "CREDITS.txt",
        "MANIFEST_SHA256.txt",
        "UNIVERSAL_RETOOL_COVERAGE.txt",
    ):
        src = addon_dir / name
        if src.is_file():
            shutil.copy2(src, dest / name)


def write_zip(folder: Path, archive: Path) -> None:
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(folder).as_posix())


def write_meta(dest: Path, *, version: str, comments: str, install_name: str) -> None:
    dest.write_text(
        "\n".join(
            [
                "[General]",
                "modid=0",
                f"version={version}",
                "newestVersion=",
                'category="Anomaly Anthology"',
                f"installationFile={install_name}.zip",
                "repository=",
                f"comments={comments}",
                "notes=Rewritten pack from STALKER Anthology Dev / addon/",
                "",
            ]
        ),
        encoding="utf-8",
    )


def aio_addons(addon_root: Path) -> list[Path]:
    return sorted(
        p
        for p in addon_root.iterdir()
        if p.is_dir()
        and (p / "gamedata").is_dir()
        and p.name not in SEPARATE
        and p.name not in SKIP
    )


def pack_separate(
    mod_id: str,
    mo2_name: str,
    *,
    addon_root: Path | None = None,
    out_dir: Path | None = None,
) -> Path:
    addon_root = addon_root or ADDON_ROOT
    out_dir = out_dir or OUT_DIR
    addon_dir = addon_root / mod_id
    version = detect_version(addon_dir)
    staging = out_dir / "_staging" / mo2_name
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    files = copy_gamedata(addon_dir / "gamedata", staging / "gamedata")
    copy_docs(addon_dir, staging)
    meta_src = addon_dir / "meta.ini"
    if meta_src.exists():
        text = decode_bytes(meta_src.read_bytes())
        text = re.sub(r"^version\s*=.*$", f"version={version}", text, flags=re.M)
        text = re.sub(
            r"^installationFile\s*=.*$",
            f"installationFile={mo2_name}.zip",
            text,
            flags=re.M,
        )
        (staging / "meta.ini").write_text(text, encoding="utf-8")
    (staging / "BUILD_INFO.txt").write_text(
        "\n".join(
            [
                f"mod_id: {mod_id}",
                f"version: {version}",
                f"built: {datetime.now().isoformat(timespec='seconds')}",
                f"source: addon/{mod_id}",
                f"gamedata_files: {files}",
                "target: Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    archive = out_dir / f"{mo2_name}.zip"
    write_zip(staging, archive)
    print(f"{mo2_name}: {files} files, v{version} -> {archive.name}")
    return archive


def pack_aio(
    addons: list[Path],
    *,
    repo: Path | None = None,
    out_dir: Path | None = None,
) -> Path:
    repo = repo or REPO_ROOT
    out_dir = out_dir or OUT_DIR
    staging = out_dir / "_staging" / AIO_NAME
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    gamedata = staging / "gamedata"
    gamedata.mkdir()

    rows = []
    total = 0
    for addon_dir in addons:
        version = detect_version(addon_dir)
        n = copy_gamedata(addon_dir / "gamedata", gamedata)
        total += n
        rows.append(f"{addon_dir.name:<42} v{version:<10} {n:>3} files")

    bhs_version, bhs_files, _, _ = pack_bhs.stage_gamedata(repo, gamedata)
    total += bhs_files
    rows.append(f"{BHS_MOD_ID:<42} v{bhs_version:<10} {bhs_files:>3} files (pack_bhs)")

    contents = (
        "\n".join(
            [
                AIO_NAME,
                "Rewritten DLTX / callback pack for Anomaly 1.5.3 / Anthology 2.1",
                f"Built: {datetime.now().isoformat(timespec='seconds')}",
                f"Addons: {len(addons) + 1}",
                f"gamedata files: {total}",
                "",
                "Included:",
                *rows,
                "",
                "Not included (separate archives):",
                "  context_menu_overhaul_anthology",
                "  quickqk_task_complete",
                "  fix_st2_footstep",
                "",
                "Not included (withdrawn, lives in BusyHands 0.6.4):",
                "  fix_bhs_fdda_loot",
                "",
            ]
        )
        + "\n"
    )
    (staging / "CONTENTS.txt").write_text(contents, encoding="utf-8")
    (staging / "README_RU.txt").write_text(
        "\n".join(
            [
                AIO_NAME,
                "",
                "Это переписанный пак старых Kristiano-фиксов: DLTX и callback'и,",
                "без полной подмены чужих файлов и без правок all.spawn.",
                "",
                "Установка:",
                "1. Удалить старый [DBG] Kristiano Fixes ALL IN ONE.",
                "2. Удалить отдельные тестовые ZIP тех же фиксов (см. CONTENTS.txt",
                "   и список в чате).",
                "3. Поставить этот архив через Install mod from archive.",
                "4. Поставить его НИЖЕ сборки и модов, которые он патчит:",
                "   MAG Redux (важно для sequential_load_magazine), R.A.K, Catspaw,",
                "   Exo System, Aim Fatigue, Interactive PDA, Classes & Talents,",
                "   Hideout Furniture, WTF / iTheon, Western Goods, SYS_Balance,",
                "   Burn Shit, Sorting Plus, DotMarks, Tosox, Grok Stash, HoC Icons, FDDA.",
                "   BusyHands внутри этого архива — отдельный zip BHS не нужен.",
                "5. Context Menu, QuickQK и ST2 Footstep ставятся отдельными модами.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    write_meta(
        staging / "meta.ini",
        version=datetime.now().strftime("%Y.%m.%d"),
        comments=(
            "Rewritten Kristiano Fixes ALL IN ONE: DLTX/callback pack "
            "for Anomaly 1.5.3 / Anthology 2.1"
        ),
        install_name=AIO_NAME,
    )
    (staging / "BUILD_INFO.txt").write_text(
        "\n".join(
            [
                f"mod_id: {AIO_NAME}",
                f"built: {datetime.now().isoformat(timespec='seconds')}",
                f"addons: {len(addons) + 1}",
                f"gamedata_files: {total}",
                "target: Anomaly 1.5.3 / Anthology 2.1 / Modded Exes MT",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    archive = out_dir / f"{AIO_NAME}.zip"
    write_zip(staging, archive)
    print(f"{AIO_NAME}: {total} files from {len(addons)} addons -> {archive.name}")
    return archive


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Pack Kristiano AIO + separate mods")
    parser.add_argument("--addon-root", type=Path, default=ADDON_ROOT)
    parser.add_argument("--out", type=Path, default=OUT_DIR)
    parser.add_argument(
        "--aio-only",
        action="store_true",
        help="Pack only [DBG] Kristiano Fixes ALL IN ONE, skip CMO/QuickQK/ST2 zips",
    )
    args = parser.parse_args(argv)

    addon_root = args.addon_root
    out_dir = args.out
    repo = addon_root.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    addons = aio_addons(addon_root)
    pack_aio(addons, repo=repo, out_dir=out_dir)
    if not args.aio_only:
        for mod_id, mo2_name in SEPARATE.items():
            pack_separate(mod_id, mo2_name, addon_root=addon_root, out_dir=out_dir)
    staging = out_dir / "_staging"
    if staging.exists():
        shutil.rmtree(staging)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
