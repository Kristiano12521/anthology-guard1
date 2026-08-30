#!/usr/bin/env python3
"""One-off packer: Kristiano ALL IN ONE + three standalone mods."""

from __future__ import annotations

import re
import shutil
import sys
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, decode_bytes  # noqa: E402

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

# Withdrawn: logic lives in anthology_busyhands_stability_fix 0.6.4.
SKIP = {"fix_bhs_fdda_loot"}

AIO_NAME = "[DBG] Kristiano Fixes ALL IN ONE"
VERSION_RE = re.compile(r"^##\s*\[?v?(\d+\.\d+(?:\.\d+)?)\]?", re.M)


def detect_version(addon_dir: Path) -> str:
    changelog = addon_dir / "CHANGELOG.md"
    if changelog.exists():
        match = VERSION_RE.search(decode_bytes(changelog.read_bytes()))
        if match:
            return match.group(1)
    changelog_txt = addon_dir / "CHANGELOG.txt"
    if changelog_txt.exists():
        match = VERSION_RE.search(decode_bytes(changelog_txt.read_bytes()))
        if match:
            return match.group(1)
    meta = addon_dir / "meta.ini"
    if meta.exists():
        for line in decode_bytes(meta.read_bytes()).splitlines():
            if line.lower().startswith("version="):
                return line.split("=", 1)[1].strip()
    return "1.0.0"


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


def pack_separate(mod_id: str, mo2_name: str) -> Path:
    addon_dir = ADDON_ROOT / mod_id
    version = detect_version(addon_dir)
    staging = OUT_DIR / "_staging" / mo2_name
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
    archive = OUT_DIR / f"{mo2_name}.zip"
    write_zip(staging, archive)
    print(f"{mo2_name}: {files} files, v{version} -> {archive.name}")
    return archive


def pack_aio(addons: list[Path]) -> Path:
    staging = OUT_DIR / "_staging" / AIO_NAME
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

    contents = (
        "\n".join(
            [
                AIO_NAME,
                "Rewritten DLTX / callback pack for Anomaly 1.5.3 / Anthology 2.1",
                f"Built: {datetime.now().isoformat(timespec='seconds')}",
                f"Addons: {len(addons)}",
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
                "   MAG Redux, R.A.K, Catspaw, Exo System, Aim Fatigue,",
                "   Interactive PDA, Classes & Talents, Hideout Furniture,",
                "   WTF / iTheon, Western Goods, SYS_Balance, Burn Shit,",
                "   Sorting Plus, DotMarks, Tosox, Grok Stash, HoC Icons, FDDA.",
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
    archive = OUT_DIR / f"{AIO_NAME}.zip"
    write_zip(staging, archive)
    print(f"{AIO_NAME}: {total} files from {len(addons)} addons -> {archive.name}")
    return archive


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    addons = sorted(
        p
        for p in ADDON_ROOT.iterdir()
        if p.is_dir()
        and (p / "gamedata").is_dir()
        and p.name not in SEPARATE
        and p.name not in SKIP
    )
    pack_aio(addons)
    for mod_id, mo2_name in SEPARATE.items():
        pack_separate(mod_id, mo2_name)
    staging = OUT_DIR / "_staging"
    if staging.exists():
        shutil.rmtree(staging)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
