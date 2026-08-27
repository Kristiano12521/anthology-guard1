#!/usr/bin/env python3
"""Создаёт скелет мода в addon/ из templates/addon-skeleton.

    python3 tools/new_addon.py my_fix_weapon_jam --title "Weapon Jam Fix"
    python3 tools/new_addon.py my_diag_squads --diag --no-ltx
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, read_text, rel  # noqa: E402

TEMPLATE_DIR = REPO_ROOT / "templates" / "addon-skeleton"
ADDON_ROOT = REPO_ROOT / "addon"

MOD_ID_RE = re.compile(r"^[a-z][a-z0-9_]{2,39}$")
LOAD_ORDER_HACK_RE = re.compile(r"^(z{3,}|a{3,})", re.I)
CP1251_SUFFIXES = {".script", ".lua", ".ltx", ".xml"}


def substitute(text: str, replacements: dict[str, str]) -> str:
    for token, value in replacements.items():
        text = text.replace(token, value)
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Скелет нового мода")
    parser.add_argument("mod_id", help="идентификатор: латиница, цифры, подчёркивания")
    parser.add_argument("--title", help="читаемое имя (по умолчанию из mod_id)")
    parser.add_argument("--version", default="1.0.0")
    parser.add_argument("--diag", action="store_true", help="добавить диагностический скрипт")
    parser.add_argument("--no-mcm", action="store_true", help="без настроек MCM")
    parser.add_argument("--no-ltx", action="store_true", help="без примера DLTX-патча")
    parser.add_argument("--force", action="store_true", help="перезаписать существующий мод")
    parser.add_argument("--template", type=Path, default=TEMPLATE_DIR)
    parser.add_argument("--addon-root", type=Path, default=ADDON_ROOT)
    args = parser.parse_args(argv)

    mod_id = args.mod_id
    if not MOD_ID_RE.match(mod_id):
        print(
            "Идентификатор должен быть в нижнем регистре, от 3 символов, "
            "только латиница, цифры и подчёркивания.",
            file=sys.stderr,
        )
        return 2
    if LOAD_ORDER_HACK_RE.match(mod_id):
        print(
            "Префиксы вида zzz/aaa запрещены: порядок загрузки задаётся списком модов MO2.",
            file=sys.stderr,
        )
        return 2

    target = args.addon_root / mod_id
    if target.exists() and not args.force:
        print(f"Уже существует: {rel(target)} (перезаписать: --force)", file=sys.stderr)
        return 2

    replacements = {
        "__MOD_ID__": mod_id,
        "__TITLE__": args.title or mod_id.replace("_", " ").title(),
        "__VERSION__": args.version,
        "__DATE__": date.today().isoformat(),
    }

    created: list[Path] = []
    for source in sorted(args.template.rglob("*")):
        if source.is_dir():
            continue
        relative = source.relative_to(args.template)
        name = relative.name

        if name.endswith("_diag.script") and not args.diag:
            continue
        if args.no_mcm and ("mcm" in name):
            continue
        if args.no_ltx and relative.suffix.lower() == ".ltx":
            continue

        destination = target / Path(substitute(relative.as_posix(), replacements))
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = substitute(read_text(source), replacements)
        encoding = "cp1251" if destination.suffix.lower() in CP1251_SUFFIXES else "utf-8"
        destination.write_text(content, encoding=encoding, errors="replace")
        created.append(destination)

    print(f"Создан мод: {rel(target)}")
    for path in created:
        print(f"  {rel(path)}")
    print()
    print("Дальше:")
    print("  1. Убери из скелета лишнее — пустые заготовки только мешают.")
    print(f"  2. python3 tools/lint_addon.py {mod_id}")
    print(f"  3. python3 tools/build_addon.py {mod_id} --zip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
