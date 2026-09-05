#!/usr/bin/env python3
"""Bundle: Kristiano AIO + separate MO2 zips + individual/ per-mod zips."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT  # noqa: E402

BUILD = REPO_ROOT / "build"
BUNDLE_NAME = "Kristiano_Fixes_Bundle_2026-09-02.zip"
VANILLA_BUNDLE_NAME = "Kristiano_Vanilla_Anomaly_Fixes_2026-09-02.zip"

ZIP_VER = re.compile(r"^(.+)-(\d+(?:\.\d+)+)\.zip$")

VANILLA_OK = {
    "fix_x2_gravity_room",
    "fix_xr_effects_sounds",
    "fix_rx_bandage_dead",
    "fix_crowkiller_hello",
    "fix_zat_b12_box",
    "fix_grifon_visibility",
    "fix_noosphere_voice_x18",
    "fix_kupol_wrong_bone",
    "fix_gigant_space_restriction",
    "fix_quest_stash",
    "fix_quest_story_id",
    "fix_stash_id_desync",
    "fix_replace_quest_corpse",
    "fix_indeikam_breeding",
    "fix_gonta_duplicate_dialog",
    "fix_soc_nimble_flash",
    "fix_trader_restock_callback",
    "fix_x15_freeplay_gate",
    "fix_rogue_hostility",
    "fix_sim_mechanic_trade",
    "fix_ph_door_rx_reload",
    "fix_vows_ambush_stash",
    "fix_dome_quest",
    "fix_flst_joker_door",
    "fix_nta_stashes",
    "fix_nimble_order_desc",
    "fix_okrest_texnik_dialog",
    "fix_hip_quest_text",
    "fix_radio",
}

# Подмножество VANILLA_OK: нужен только базовый Anomaly 1.5.3, без опциональных сюжетных модов.
VANILLA_STRICT = VANILLA_OK - {
    "fix_vows_ambush_stash",  # SAD / Lost to the Zone
    "fix_dome_quest",  # AZ Radar
    "fix_flst_joker_door",  # Fallstation
    "fix_nta_stashes",  # NTA
    "fix_radio",  # Baer's Radio или аналог
    "fix_okrest_texnik_dialog",  # Okrest
}

TOP_PREFIXES = (
    "[DBG] Kristiano",
    "[HUD] Context",
    "[GFX] QuickQK",
    "[SND] Anthology ST2",
)


def latest_individual_zips(build_dir: Path) -> list[Path]:
    latest: dict[str, Path] = {}
    for path in build_dir.glob("*.zip"):
        match = ZIP_VER.match(path.name)
        if not match:
            continue
        mod_id = match.group(1)
        if mod_id.startswith("["):
            continue
        prev = latest.get(mod_id)
        if prev is None or path.stat().st_mtime >= prev.stat().st_mtime:
            latest[mod_id] = path

    bhs_candidates = sorted(
        build_dir.glob("Anthology_BusyHands_Stability_Fix_v*.zip"),
        key=lambda path: path.stat().st_mtime,
    )
    bhs = bhs_candidates[-1] if bhs_candidates else None
    if bhs is not None and bhs.is_file():
        latest["anthology_busyhands_stability_fix"] = bhs

    return sorted(latest.values(), key=lambda p: p.name.lower())


def mod_id_from_zip(path: Path) -> str:
    if path.name.startswith("Anthology_BusyHands"):
        return "anthology_busyhands_stability_fix"
    match = ZIP_VER.match(path.name)
    return match.group(1) if match else path.stem


def top_level_zips(build_dir: Path, bundle_name: str) -> list[Path]:
    out: list[Path] = []
    for path in sorted(build_dir.glob("*.zip")):
        if path.name == bundle_name:
            continue
        if any(path.name.startswith(prefix) for prefix in TOP_PREFIXES):
            out.append(path)
    return out


def write_index(individual: list[Path]) -> str:
    lines = [
        "individual/ — отдельные zip (MO2: Install mod from archive)",
        f"Собрано: {datetime.now().isoformat(timespec='seconds')}",
        f"Всего: {len(individual)}",
        "",
        "mod_id | zip | vanilla Anomaly",
        "---|---|---",
    ]
    for path in individual:
        mod_id = mod_id_from_zip(path)
        flag = "да" if mod_id in VANILLA_OK else "нет/условно"
        lines.append(f"{mod_id} | {path.name} | {flag}")
    return "\n".join(lines) + "\n"


def write_changelog(count: int) -> str:
    return (
        "# Kristiano Fixes Bundle — 2026-09-02 (v2)\n\n"
        "## Что нового\n\n"
        "### fix_fdda_mcm_paths v1.0.0 (подтверждён 02.09.2026)\n\n"
        "DotMarks: mcm_paths перенаправлен с EA_settings/* на fddar/* (FDDA Redone).\n"
        "Убирает !MCM given bad path от DotMarks; pickup-анимации согласованы с MCM FDDA.\n"
        "Нужны DotMarks + FDDA Redone. Уже внутри AIO.\n\n"
        "### Структура bundle\n\n"
        "- Корень: AIO + 3 отдельных MO2-мода (CMO, QuickQK, ST2)\n"
        f"- individual/: {count} отдельных zip — каждый со своим CHANGELOG.md\n"
        "- README_RU.txt, CHANGELOG.txt, individual/INDEX.txt\n\n"
        "AIO: 54 аддона, 161 файл gamedata, BHS v0.6.10 внутри.\n"
    )


def write_readme() -> str:
    return "\n".join(
        [
            "Kristiano Fixes Bundle — установка",
            "=====================================",
            "",
            "1. Распаковать этот архив.",
            "2. [DBG] Kristiano Fixes ALL IN ONE.zip — для Anthology целиком.",
            "3. individual/ — точечные фиксы; см. INDEX.txt (колонка vanilla Anomaly).",
            "   Каждый zip ставится через Install mod from archive; внутри CHANGELOG.md.",
            "4. Не дублировать: если фикс уже в AIO, отдельный zip не нужен.",
            "",
            "Отдельные MO2-моды в корне (не в AIO):",
            "  [HUD] Context Menu_Overhaul_Anthology.zip",
            "  [GFX] QuickQK Task Status Tool Anthology.zip",
            "  [SND] Anthology ST2 Mutant Footstep Sound.zip",
            "",
            "Для чистой Anomaly без Anthology:",
            "  — не ставить AIO;",
            "  — из individual/ выбрать fix_* где INDEX.txt: vanilla Anomaly = да;",
            "  — fix_fdda_mcm_paths только с DotMarks + FDDA Redone.",
            "",
        ]
    )


def vanilla_zips(build_dir: Path, *, strict: bool = True) -> list[Path]:
    allowed = VANILLA_STRICT if strict else VANILLA_OK
    return sorted(
        (path for path in latest_individual_zips(build_dir) if mod_id_from_zip(path) in allowed),
        key=lambda p: p.name.lower(),
    )


def write_vanilla_index(mods: list[Path], *, strict: bool) -> str:
    lines = [
        "Моды для Anomaly 1.5.3 без Anthology / без тяжёлых сборок",
        f"Собрано: {datetime.now().isoformat(timespec='seconds')}",
        f"Всего: {len(mods)}",
        "",
        "mod_id | zip | примечание",
        "---|---|---",
    ]
    notes = {
        "fix_vows_ambush_stash": "нужен SAD",
        "fix_dome_quest": "нужен AZ Radar",
        "fix_flst_joker_door": "нужен Fallstation",
        "fix_nta_stashes": "нужен NTA mod",
        "fix_radio": "нужен Baer's Radio",
        "fix_okrest_texnik_dialog": "нужен Okrest",
        "fix_rogue_hostility": "LTTZ / Living Legend (в базовой Anomaly)",
        "fix_nimble_order_desc": "COP Zaton (в базовой Anomaly)",
        "fix_hip_quest_text": "Escape (в базовой Anomaly)",
    }
    for path in mods:
        mod_id = mod_id_from_zip(path)
        note = notes.get(mod_id, "базовый Anomaly" if mod_id in VANILLA_STRICT else "опциональный контент")
        lines.append(f"{mod_id} | {path.name} | {note}")
    if strict:
        lines.extend(
            [
                "",
                "Не включены (нужен другой мод или Anthology):",
                "  fix_fdda_mcm_paths — DotMarks + FDDA Redone",
                "  fix_fetch_headlamp — task_manager Anthology",
                "  fix_charon_red_forest_travel — MLR / Hard+ / Anthology smart",
                "  seamless_inventory_sort_anthology, BHS, CMO, QuickQK и пр.",
            ]
        )
    return "\n".join(lines) + "\n"


def write_vanilla_readme(count: int, *, strict: bool) -> str:
    scope = "базовый Anomaly 1.5.3" if strict else "Anomaly без Anthology-сборки"
    return "\n".join(
        [
            "Kristiano — фиксы для обычной Anomaly",
            "========================================",
            "",
            f"Состав: {count} zip. Каждый — отдельный мод для MO2 (Install mod from archive).",
            f"Целевая среда: {scope}.",
            "Внутри каждого zip есть CHANGELOG.md с описанием бага.",
            "",
            "Установка:",
            "1. Распаковать этот архив.",
            "2. Поставить нужные fix_* через MO2 — ниже модов, которые они патчат.",
            "3. Не ставить несколько zip на один и тот же баг.",
            "",
            "INDEX.txt — полный список с примечаниями.",
            "",
            "Не входят сюда (нужна Anthology или другие моды):",
            "  [DBG] Kristiano Fixes ALL IN ONE",
            "  fix_fdda_mcm_paths, seamless_inventory_sort_anthology, BHS, CMO, QuickQK…",
            "",
        ]
    )


def pack_vanilla_bundle(
    *,
    build_dir: Path | None = None,
    bundle_name: str = VANILLA_BUNDLE_NAME,
    strict: bool = True,
) -> Path:
    build_dir = build_dir or BUILD
    bundle_path = build_dir / bundle_name
    mods = vanilla_zips(build_dir, strict=strict)

    if bundle_path.exists():
        bundle_path.unlink()

    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("README_RU.txt", write_vanilla_readme(len(mods), strict=strict))
        zf.writestr("INDEX.txt", write_vanilla_index(mods, strict=strict))
        for path in mods:
            zf.write(path, path.name)

    return bundle_path


def pack_bundle(*, build_dir: Path | None = None, bundle_name: str = BUNDLE_NAME) -> Path:
    build_dir = build_dir or BUILD
    bundle_path = build_dir / bundle_name
    individual = latest_individual_zips(build_dir)
    top = top_level_zips(build_dir, bundle_name)

    if bundle_path.exists():
        bundle_path.unlink()

    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("CHANGELOG.txt", write_changelog(len(individual)))
        zf.writestr("README_RU.txt", write_readme())
        zf.writestr("individual/INDEX.txt", write_index(individual))
        for path in top:
            zf.write(path, path.name)
        for path in individual:
            zf.write(path, f"individual/{path.name}")

    return bundle_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Pack Kristiano bundle with individual zips")
    parser.add_argument("--out", type=Path, default=BUILD)
    parser.add_argument("--name", default=BUNDLE_NAME)
    parser.add_argument(
        "--vanilla-only",
        action="store_true",
        help=f"только zip для обычной Anomaly -> {VANILLA_BUNDLE_NAME}",
    )
    parser.add_argument(
        "--vanilla-with-optional",
        action="store_true",
        help="vanilla bundle + fix_* с опциональным контентом (SAD, Fallstation, …)",
    )
    args = parser.parse_args(argv)

    if args.vanilla_only or args.vanilla_with_optional:
        strict = not args.vanilla_with_optional
        bundle = pack_vanilla_bundle(build_dir=args.out, strict=strict)
        mods = vanilla_zips(args.out, strict=strict)
        size_mb = bundle.stat().st_size / (1024 * 1024)
        label = "strict" if strict else "with optional content"
        print(f"{bundle.name}: {size_mb:.2f} MB ({label}, {len(mods)} mods)")
        return 0

    bundle = pack_bundle(build_dir=args.out, bundle_name=args.name)
    individual = latest_individual_zips(args.out)
    top = top_level_zips(args.out, args.name)
    size_mb = bundle.stat().st_size / (1024 * 1024)
    print(f"{bundle.name}: {size_mb:.2f} MB")
    print(f"  top-level: {len(top)}, individual/: {len(individual)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
