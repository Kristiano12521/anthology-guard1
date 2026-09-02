#!/usr/bin/env python3
"""Audit addon mods for log observability vs a session log."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, read_text
from mod_mine import discover_addon_mods, extract_log_tags, scan_log_for_mods

PRINTF_LOAD = re.compile(
    r"printf\s*\([^)]*(loaded|wrapped|installed|registered|LOG_TAG)",
    re.I,
)
LOG_TAG_DECL = re.compile(r"LOG_TAG\s*=", re.I)


def mod_logging_profile(mod_dir: Path) -> dict:
    scripts_dir = mod_dir / "gamedata" / "scripts"
    scripts = list(scripts_dir.glob("*.script")) if scripts_dir.is_dir() else []
    gamedata = mod_dir / "gamedata"
    ltx = list(gamedata.rglob("*.ltx")) if gamedata.is_dir() else []
    tags: set[str] = set()
    has_load = False
    has_tag = False
    has_guard = False
    for script in scripts:
        text = read_text(script)
        tags |= extract_log_tags(text)
        if PRINTF_LOAD.search(text):
            has_load = True
        if LOG_TAG_DECL.search(text):
            has_tag = True
        if "guard NOT installed" in text or "NOT installed" in text:
            has_guard = True
    dltx_only = not scripts and bool(ltx)
    silent_script = bool(scripts) and not has_load and not has_tag
    return {
        "scripts": len(scripts),
        "ltx": len(ltx),
        "dltx_only": dltx_only,
        "has_load": has_load,
        "has_tag": has_tag,
        "has_guard": has_guard,
        "silent_script": silent_script,
        "tags": sorted(tags)[:3],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit mod log observability")
    parser.add_argument("log", type=Path, nargs="?", default=REPO_ROOT / "logs" / "xray_nikit.log")
    args = parser.parse_args()

    lines = read_text(args.log).splitlines()
    catalog = discover_addon_mods()
    scan = scan_log_for_mods(lines, catalog)

    buckets: dict[str, list[tuple[str, dict, object | None]]] = {
        "ok": [],
        "fail": [],
        "weak": [],
        "absent_has_logging": [],
        "absent_dltx_only": [],
        "absent_silent_script": [],
    }

    for mod_id in sorted(catalog):
        prof = mod_logging_profile(REPO_ROOT / "addon" / mod_id)
        pres = scan.present.get(mod_id)
        if mod_id in scan.absent:
            if prof["dltx_only"] or (not prof["scripts"] and prof["ltx"]):
                buckets["absent_dltx_only"].append((mod_id, prof, None))
            elif prof["silent_script"]:
                buckets["absent_silent_script"].append((mod_id, prof, None))
            elif prof["has_load"] or prof["has_tag"]:
                buckets["absent_has_logging"].append((mod_id, prof, None))
            else:
                buckets["absent_dltx_only"].append((mod_id, prof, None))
        elif pres and pres.has_failures:
            buckets["fail"].append((mod_id, prof, pres))
        elif pres and pres.loaded_hint:
            buckets["ok"].append((mod_id, prof, pres))
        else:
            buckets["weak"].append((mod_id, prof, pres))

    total = len(catalog)
    print(f"log: {args.log.name} ({len(lines)} lines)")
    print(f"mods in addon/: {total}")
    print()
    print(f"OK (in log, loaded/wrapped hint): {len(buckets['ok'])}")
    print(f"FAIL (in log, guard/refusal): {len(buckets['fail'])}")
    print(f"WEAK (in log, no loaded hint): {len(buckets['weak'])}")
    print(f"ABSENT + has logging code: {len(buckets['absent_has_logging'])}")
    print(f"ABSENT + DLTX-only (no script log): {len(buckets['absent_dltx_only'])}")
    print(f"ABSENT + silent script: {len(buckets['absent_silent_script'])}")
    print()

    def dump(title: str, key: str) -> None:
        items = buckets[key]
        if not items:
            return
        print(f"## {title} ({len(items)})")
        for mod_id, prof, pres in items:
            bits = [
                f"scripts={prof['scripts']}",
                f"ltx={prof['ltx']}",
            ]
            if prof["has_load"]:
                bits.append("load_printf=Y")
            if prof["has_tag"]:
                bits.append("LOG_TAG=Y")
            if prof["has_guard"]:
                bits.append("guard_msg=Y")
            if pres is not None:
                bits.append(f"lines={sum(pres.lines.values())}")
            print(f"  {mod_id}: {', '.join(bits)}")
        print()

    dump("OK", "ok")
    dump("FAIL", "fail")
    dump("WEAK (needs better loaded line)", "weak")
    dump("NOT IN LOG but has printf/LOG_TAG (not installed or no trigger)", "absent_has_logging")
    dump("NOT IN LOG, DLTX-only (cannot verify via log)", "absent_dltx_only")
    dump("NOT IN LOG, silent script (no observability)", "absent_silent_script")

    observable = len(buckets["ok"]) + len(buckets["fail"]) + len(buckets["weak"])
    print(f"Observable in this log: {observable}/{total}")
    print(f"Not observable (absent from log): {total - observable}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
