#!/usr/bin/env python3
"""Наполняет reference/addons/ из включённых модов MO2.

Аргумент — папка MO2 (не профиля). Профиль по умолчанию берётся из
ModOrganizer.ini (selected_profile, включая @ByteArray с \\xNN).
Копирует из mods/<имя>/gamedata/ только scripts/, configs/, text/,
materials/ в reference/addons/<имя из modlist>/. reference/anthology/
не трогает: ядро Anthology в этой сборке тоже лежит модами MO2.

Свои сборки (BUILD_INFO.txt / meta notes / CONTENTS.txt от packers)
по умолчанию не копируются — иначе lint видит addon/ как «замену себя».
Флаг --include-own включает их.

    python3 tools/fill_reference_addons.py "C:/Games/.../mo2"
    python3 tools/fill_reference_addons.py "C:/Games/.../mo2" --dry-run
    python3 tools/fill_reference_addons.py "C:/Games/.../mo2" --profile "Anthology 2.1 HARD Сложный"
    python3 tools/fill_reference_addons.py "C:/Games/.../mo2" --prune --yes
    python3 tools/fill_reference_addons.py "C:/Games/.../mo2" --include-own
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import xdb_unpack  # noqa: E402
from fill_reference import (  # noqa: E402
    ADDONS_DIR_NAME,
    DEFAULT_REFERENCE,
    KEEP_DIRS,
    dest_relative,
    write_if_changed,
)

BYTEARRAY_PREFIX = "@ByteArray("
NAMED_ESCAPES = {
    "a": "\a",
    "b": "\b",
    "f": "\f",
    "n": "\n",
    "r": "\r",
    "t": "\t",
    "v": "\v",
    '"': '"',
    "?": "?",
    "'": "'",
    "\\": "\\",
}
HEX_DIGITS = "0123456789abcdefABCDEF"
OCT_DIGITS = "01234567"

# Маркеры пакетов из tools/build_addon.py, pack_bhs.py, _pack_kristiano_aio.py.
OWN_NOTES_NEEDLE = "STALKER Anthology Dev"
OWN_CONTENTS_NEEDLES = (
    "Rewritten DLTX",
    "Not included (separate archives)",
    OWN_NOTES_NEEDLE,
)


def _read_text_best_effort(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_bytes().decode("cp1251", errors="replace")
    except OSError:
        return ""


def own_mo2_name_prefixes() -> tuple[str, ...]:
    """Префиксы MO2-имён наших пакетов из упаковщиков (один источник правды)."""
    import _pack_kristiano_aio as kristiano_pack  # noqa: PLC0415
    import pack_bhs  # noqa: PLC0415

    return (kristiano_pack.AIO_NAME, *kristiano_pack.SEPARATE.values(), pack_bhs.OUT_STEM)


def is_own_package_name(name: str) -> bool:
    """Имя начинается с AIO_NAME / SEPARATE / BusyHands OUT_STEM (суффикс NEW и т.п.)."""
    return any(name.startswith(prefix) for prefix in own_mo2_name_prefixes())


def is_own_mo2_package(mod_dir: Path) -> bool:
    """True, если корень мода MO2 — наша сборка, а не чужой эталон.

    Признаки (любой):
    1) имя начинается с префикса из AIO_NAME / SEPARATE / pack_bhs.OUT_STEM
       (MO2 часто добавляет « (NEW)» и другие суффиксы);
    2) BUILD_INFO.txt (build_addon / pack_bhs / kristiano packer);
    3) CONTENTS.txt от Kristiano AIO;
    4) meta.ini notes/comments со «STALKER Anthology Dev»; vendor_fork=1;
       installationFile с путём на .../Anthology/build/.
    """
    if not mod_dir.is_dir():
        return False
    if is_own_package_name(mod_dir.name):
        return True
    if (mod_dir / "BUILD_INFO.txt").is_file():
        return True
    contents = mod_dir / "CONTENTS.txt"
    if contents.is_file():
        text = _read_text_best_effort(contents)
        if any(needle in text for needle in OWN_CONTENTS_NEEDLES):
            return True
    meta = mod_dir / "meta.ini"
    if not meta.is_file():
        return False
    for raw in _read_text_best_effort(meta).splitlines():
        line = raw.strip()
        if not line or line.startswith("[") or line.startswith("#") or line.startswith(";"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key_l = key.strip().lower()
        value = value.strip().strip('"')
        if key_l in ("notes", "comments") and OWN_NOTES_NEEDLE in value:
            return True
        if key_l == "vendor_fork" and value.lower() in ("1", "true", "yes"):
            return True
        if key_l == "installationfile":
            normalized = value.replace("\\", "/").lower()
            if "/anthology/build/" in normalized:
                return True
    return False


def unescape_qt_ini(text: str) -> str:
    """Qt QSettingsPrivate::iniUnescapedStringList без разбора string list.

    \\xNN ест все следующие hex-цифры; неизвестная escape-последовательность
    отбрасывается (символ после \\ пропускается), как в Qt.
    """
    out: list[str] = []
    index = 0
    length = len(text)
    while index < length:
        char = text[index]
        if char != "\\":
            out.append(char)
            index += 1
            continue
        index += 1
        if index >= length:
            break
        esc = text[index]
        index += 1
        named = NAMED_ESCAPES.get(esc)
        if named is not None:
            out.append(named)
            continue
        if esc == "x":
            value = 0
            got = False
            while index < length and text[index] in HEX_DIGITS:
                value = (value << 4) + int(text[index], 16)
                index += 1
                got = True
            if got:
                out.append(chr(value & 0xFF))
            continue
        if esc in OCT_DIGITS:
            value = int(esc, 8)
            digits = 1
            while digits < 3 and index < length and text[index] in OCT_DIGITS:
                value = (value << 3) + int(text[index], 8)
                index += 1
                digits += 1
            out.append(chr(value & 0xFF))
            continue
    return "".join(out)


def decode_qt_ini_value(raw: str) -> str:
    """Значение QSettings: @ByteArray с \\xNN, опциональные кавычки, обычная строка."""
    value = raw.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        value = value[1:-1]
    unescaped = unescape_qt_ini(value)
    if unescaped.startswith(BYTEARRAY_PREFIX) and unescaped.endswith(")"):
        inner = unescaped[len(BYTEARRAY_PREFIX) : -1]
        return inner.encode("latin-1").decode("utf-8")
    if unescaped.startswith("@@"):
        return unescaped[1:]
    return unescaped


def read_selected_profile(ini_path: Path) -> str:
    text = ini_path.read_text(encoding="utf-8-sig")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("selected_profile="):
            continue
        name = decode_qt_ini_value(stripped.split("=", 1)[1])
        if name:
            return name
    raise FileNotFoundError(f"в {ini_path} нет selected_profile")


def is_separator(name: str) -> bool:
    """MO2 ModInfo::isSeparatorName: имя целиком оканчивается на _separator."""
    return name.endswith("_separator")


def parse_modlist(path: Path) -> list[str]:
    """Включённые моды в порядке файла.

    Порядок в modlist.txt обратный порядку загрузки. MO2 Profile::doWriteModlist
    пишет m_ModIndexByPriority с crbegin: первая строка — наибольший приоритет
    (низ левой панели, выигрывает конфликты файлов). При чтении приоритет
    инвертируется обратно. Каждый мод кладётся в свою папку, наложения нет —
    этот порядок только для сводки.

    Источники: ModOrganizer2/modorganizer src/profile.cpp; Nolvus catalog/mo2
    («listed from the bottom up»); STEP forums topic/5082.
    """
    enabled: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        flag = line[0]
        if flag in "+-*":
            name = line[1:].strip()
        else:
            continue
        if not name or is_separator(name):
            continue
        if flag == "-":
            continue
        enabled.append(name)
    return enabled


def iter_files(root: Path):
    """os.walk, не glob: имена модов содержат [, ], (, ), кириллицу, пробелы."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        filenames.sort()
        for name in filenames:
            yield Path(dirpath) / name


def keep_relative(file: Path, gamedata: Path) -> str | None:
    try:
        relative = file.relative_to(gamedata).as_posix()
    except ValueError:
        return None
    return dest_relative(relative)


def extra_addon_dirs(addons_root: Path, keep_names: set[str]) -> list[Path]:
    if not addons_root.is_dir():
        return []
    extra: list[Path] = []
    for child in addons_root.iterdir():
        if child.is_dir() and child.name not in keep_names:
            extra.append(child)
    return sorted(extra, key=lambda path: path.name)


def copy_mod(
    mod_name: str,
    mods_dir: Path,
    addons_root: Path,
    *,
    dry_run: bool,
) -> tuple[int, int, int, list[str]]:
    """(kept, written, unchanged, skip kinds). Целый мод — один kind, иначе по файлам."""
    source = mods_dir / mod_name
    if not source.is_dir():
        return 0, 0, 0, ["нет папки мода"]
    gamedata = source / "gamedata"
    if not gamedata.is_dir():
        return 0, 0, 0, ["нет gamedata"]
    dest_root = addons_root / mod_name
    kept = 0
    written = 0
    unchanged = 0
    skips: list[str] = []
    for file in iter_files(gamedata):
        relative = keep_relative(file, gamedata)
        if relative is None:
            continue
        if dry_run:
            kept += 1
            continue
        try:
            data = file.read_bytes()
        except OSError as exc:
            print(f"  пропуск {mod_name}/{relative}: {exc}", file=sys.stderr)
            skips.append(xdb_unpack.skip_kind(str(exc)))
            continue
        kept += 1
        status = write_if_changed(dest_root.joinpath(*relative.split("/")), data)
        if status == "written":
            written += 1
        else:
            unchanged += 1
    return kept, written, unchanged, skips


def resolve_profile(mo2: Path, profile: str | None) -> str:
    if profile:
        return profile
    ini = mo2 / "ModOrganizer.ini"
    if not ini.is_file():
        raise FileNotFoundError(f"нет {ini}: укажите --profile")
    return read_selected_profile(ini)


def keep_addon_names(
    enabled: list[str],
    mods_dir: Path,
    *,
    include_own: bool,
) -> set[str]:
    """Имена папок reference/addons/, которые prune не трогает."""
    keep = set(enabled)
    if include_own:
        return keep
    for name in enabled:
        if is_own_mo2_package(mods_dir / name):
            keep.discard(name)
    return keep


def fill_addons(
    mo2: Path,
    reference_root: Path,
    *,
    profile: str | None = None,
    dry_run: bool = False,
    prune: bool = False,
    yes: bool = False,
    include_own: bool = False,
) -> tuple[dict[str, int], list[str], list[Path], bool]:
    """Возвращает (counts, skip kinds, extra dirs, aborted).

    aborted=True — --prune без --yes: список напечатан, ничего не писали.
    """
    mods_dir = mo2 / "mods"
    profiles_dir = mo2 / "profiles"
    if not mods_dir.is_dir():
        raise FileNotFoundError(f"нет папки mods/ в {mo2}")
    if not profiles_dir.is_dir():
        raise FileNotFoundError(f"нет папки profiles/ в {mo2}")

    profile_name = resolve_profile(mo2, profile)
    profile_dir = profiles_dir / profile_name
    if not profile_dir.is_dir():
        raise FileNotFoundError(f"нет профиля {profile_name!r} в {profiles_dir}")
    modlist = profile_dir / "modlist.txt"
    if not modlist.is_file():
        raise FileNotFoundError(f"нет {modlist}")

    enabled = parse_modlist(modlist)
    addons_root = reference_root / ADDONS_DIR_NAME
    keep_names = keep_addon_names(enabled, mods_dir, include_own=include_own)
    extra = extra_addon_dirs(addons_root, keep_names)

    counts = {
        "mods": 0,
        "files": 0,
        "written": 0,
        "unchanged": 0,
        "enabled": len(enabled),
        "own_skipped": 0,
    }
    skips: list[str] = []

    if prune and not yes and not dry_run:
        return counts, skips, extra, True

    action = "будет" if dry_run else "взято"
    keep_label = "/".join(KEEP_DIRS)
    for name in enabled:
        source = mods_dir / name
        if not include_own and is_own_mo2_package(source):
            counts["own_skipped"] += 1
            print(f"пропуск {name}: свой пакет", file=sys.stderr)
            continue
        kept, written, unchanged, mod_skips = copy_mod(
            name, mods_dir, addons_root, dry_run=dry_run
        )
        if kept == 0 and mod_skips:
            kind = mod_skips[0]
            print(f"пропуск {name}: {kind}", file=sys.stderr)
            skips.extend(mod_skips)
            continue
        skips.extend(mod_skips)
        counts["mods"] += 1
        counts["files"] += kept
        counts["written"] += written
        counts["unchanged"] += unchanged
        print(
            f"{name}  ->  reference/{ADDONS_DIR_NAME}/{name}/  "
            f"({action} {kept} файлов из {keep_label})"
        )

    if prune and yes and not dry_run:
        for path in extra:
            shutil.rmtree(path)

    return counts, skips, extra, False


def print_prune_preview(extra: list[Path], *, would_delete: bool) -> None:
    if not extra:
        print("удалять нечего: лишних папок в reference/addons/ нет.")
        return
    verb = "удалил бы" if would_delete else "удалён"
    for path in extra:
        print(f"{verb}: {path.name}")
    if would_delete:
        print(
            f"Это preview prune ({len(extra)} папок). "
            "Чтобы удалить, добавьте --yes."
        )
    else:
        print(f"удалено папок: {len(extra)}.")


def print_summary(
    counts: dict[str, int],
    skips: list[str],
    extra: list[Path],
    *,
    dry_run: bool,
    prune: bool,
    aborted: bool,
) -> None:
    if aborted:
        print_prune_preview(extra, would_delete=True)
        return
    verb = "попало бы" if dry_run else "легло"
    print()
    print(
        f"Итого {verb} {counts['files']} файлов из {counts['mods']} модов "
        f"в reference/{ADDONS_DIR_NAME}/ "
        f"(включено в профиле: {counts['enabled']})."
    )
    own_skipped = counts.get("own_skipped", 0)
    if own_skipped:
        print(
            f"пропущено своих пакетов: {own_skipped} "
            "(маркер сборки; см. --include-own)."
        )
    if not dry_run:
        print(
            f"записано новых/изменённых: {counts['written']}, "
            f"без изменений: {counts['unchanged']}."
        )
    summary = xdb_unpack.format_skip_summary(skips)
    if summary:
        print(summary)
    if prune:
        print_prune_preview(extra, would_delete=dry_run)
    print("Дальше: python3 tools/refindex.py build")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Наполнить reference/addons из включённых модов MO2"
    )
    parser.add_argument(
        "mo2",
        type=Path,
        help="папка MO2 (внутри ожидаются mods/ и profiles/), не папка профиля",
    )
    parser.add_argument(
        "--profile",
        help="имя профиля; по умолчанию selected_profile из ModOrganizer.ini",
    )
    parser.add_argument(
        "--reference",
        type=Path,
        default=DEFAULT_REFERENCE,
        help="корень reference/ (по умолчанию в репозитории)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="сводка по модам, ничего не писать и не удалять",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help="убрать из reference/addons/ папки вне включённых модов",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="подтвердить --prune (без этого только список и выход)",
    )
    parser.add_argument(
        "--include-own",
        action="store_true",
        help="копировать и свои сборки (BUILD_INFO / meta notes / CONTENTS)",
    )
    args = parser.parse_args(argv)

    if not args.mo2.is_dir():
        print(f"нет папки MO2: {args.mo2}", file=sys.stderr)
        return 2
    try:
        counts, skips, extra, aborted = fill_addons(
            args.mo2,
            args.reference,
            profile=args.profile,
            dry_run=args.dry_run,
            prune=args.prune,
            yes=args.yes,
            include_own=args.include_own,
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print_summary(
        counts,
        skips,
        extra,
        dry_run=args.dry_run,
        prune=args.prune,
        aborted=aborted,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
