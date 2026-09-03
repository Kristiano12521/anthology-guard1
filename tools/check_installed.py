#!/usr/bin/env python3
"""Сверка установленных в MO2 пакетов с источниками в addon/.

Находит в mods/ пакеты с BUILD_INFO.txt (наши сборки), сравнивает дату
built с mtime файлов в addon/<mod_id>/gamedata/, сообщает: устарел /
актуален / не установлен.

Моды из SKIP и SEPARATE (_pack_kristiano_aio) ставятся отдельно — в списке
«не установлен» не появляются.

mtime после git clone недостоверен (как VERIFY-001): при CI /
GITHUB_ACTIONS сравнение пропускается.

    python3 tools/check_installed.py "C:/Games/.../mo2"
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, iter_files  # noqa: E402
from lint_addon import VERIFY_SKIP_NAMES, mtime_untrusted_reason  # noqa: E402

ADDON_ROOT = REPO_ROOT / "addon"

# pack_bhs пишет mod_id: Anthology_BusyHands_Stability_Fix
BHS_BUILD_MOD_ID = "Anthology_BusyHands_Stability_Fix"


@dataclass
class BuildInfo:
    mod_id: str
    built: datetime | None
    version: str | None = None
    raw: dict[str, str] = field(default_factory=dict)


@dataclass
class InstalledPackage:
    mo2_name: str
    path: Path
    info: BuildInfo


@dataclass
class PackageStatus:
    package: InstalledPackage
    status: str  # "current" | "outdated" | "no_source" | "no_built"
    source_mtime: datetime | None = None
    source_mods: list[str] = field(default_factory=list)
    detail: str = ""


@dataclass
class CheckReport:
    packages: list[PackageStatus] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    mtime_untrusted: str | None = None
    own_count: int = 0


def parse_build_info(text: str) -> BuildInfo:
    """Разбирает BUILD_INFO.txt: ключ: значение (без вложенных блоков)."""
    raw: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.endswith(":") and ":" not in stripped[:-1]:
            # "vendor_full_files:" и подобные заголовки без значения
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if not value:
            continue
        # первая строка ключа побеждает (не перетирать вложенными "  path: size")
        if key not in raw and not line[:1].isspace():
            raw[key] = value

    mod_id = raw.get("mod_id", "")
    version = raw.get("version")
    built: datetime | None = None
    built_raw = raw.get("built")
    if built_raw:
        try:
            built = datetime.fromisoformat(built_raw)
        except ValueError:
            built = None
    return BuildInfo(mod_id=mod_id, built=built, version=version, raw=raw)


def read_build_info(path: Path) -> BuildInfo | None:
    marker = path / "BUILD_INFO.txt"
    if not marker.is_file():
        return None
    try:
        text = marker.read_text(encoding="utf-8")
    except OSError:
        return None
    info = parse_build_info(text)
    if not info.mod_id:
        return None
    return info


def find_own_packages(mods_dir: Path) -> list[InstalledPackage]:
    """Пакеты в mods/ с нашим BUILD_INFO.txt."""
    found: list[InstalledPackage] = []
    if not mods_dir.is_dir():
        return found
    for child in sorted(mods_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        info = read_build_info(child)
        if info is None:
            continue
        found.append(InstalledPackage(mo2_name=child.name, path=child, info=info))
    return found


def _kristiano():
    import _pack_kristiano_aio as kristiano_pack  # noqa: PLC0415

    return kristiano_pack


def source_mod_ids(mod_id: str, addon_root: Path) -> list[str]:
    """Какие addon/<id> покрывает пакет с данным mod_id из BUILD_INFO."""
    k = _kristiano()
    from build_prune import BHS_MOD_ID  # noqa: PLC0415

    if mod_id == k.AIO_NAME:
        ids = [p.name for p in k.aio_addons(addon_root)]
        if (addon_root / BHS_MOD_ID).is_dir():
            ids.append(BHS_MOD_ID)
        return ids
    if mod_id in k.SEPARATE:
        return [mod_id]
    if mod_id == BHS_BUILD_MOD_ID or mod_id == BHS_MOD_ID:
        return [BHS_MOD_ID]
    return [mod_id]


def newest_gamedata_mtime(addon_dir: Path) -> datetime | None:
    """Самый свежий mtime файлов в gamedata/ (как VERIFY-001, но с временем)."""
    gamedata = addon_dir / "gamedata"
    if not gamedata.is_dir():
        return None
    newest: datetime | None = None
    for path in iter_files(gamedata):
        if path.name.lower() in VERIFY_SKIP_NAMES:
            continue
        try:
            stamp = datetime.fromtimestamp(path.stat().st_mtime)
        except OSError:
            continue
        if newest is None or stamp > newest:
            newest = stamp
    return newest


def newest_sources_mtime(mod_ids: list[str], addon_root: Path) -> tuple[datetime | None, list[str]]:
    """Максимальный mtime по списку модов; второй элемент — моды с найденным gamedata."""
    newest: datetime | None = None
    present: list[str] = []
    for mod_id in mod_ids:
        addon_dir = addon_root / mod_id
        stamp = newest_gamedata_mtime(addon_dir)
        if stamp is None:
            continue
        present.append(mod_id)
        if newest is None or stamp > newest:
            newest = stamp
    return newest, present


def expected_aio_mod_ids(addon_root: Path) -> list[str]:
    """Моды, ожидаемые в AIO: есть gamedata, не SKIP и не SEPARATE."""
    k = _kristiano()
    return [
        p.name
        for p in sorted(addon_root.iterdir(), key=lambda p: p.name.lower())
        if p.is_dir()
        and (p / "gamedata").is_dir()
        and p.name not in k.SKIP
        and p.name not in k.SEPARATE
    ]


def check_installed(
    mo2: Path,
    *,
    addon_root: Path | None = None,
    skip_mtime: bool = False,
) -> CheckReport:
    """Сверяет mods/ с addon/. skip_mtime — как --no-verify у lint."""
    addon_root = addon_root or ADDON_ROOT
    mods_dir = mo2 / "mods"
    packages = find_own_packages(mods_dir)
    report = CheckReport(own_count=len(packages))

    untrusted = None if skip_mtime else mtime_untrusted_reason()
    if skip_mtime:
        untrusted = untrusted or "--no-mtime"
    report.mtime_untrusted = untrusted

    covered: set[str] = set()
    for package in packages:
        mod_ids = source_mod_ids(package.info.mod_id, addon_root)
        covered.update(mod_ids)
        if untrusted:
            report.packages.append(
                PackageStatus(
                    package=package,
                    status="skipped",
                    source_mods=mod_ids,
                    detail="mtime недостоверен",
                )
            )
            continue
        if not package.info.built:
            report.packages.append(
                PackageStatus(
                    package=package,
                    status="no_built",
                    source_mods=mod_ids,
                    detail="нет даты built в BUILD_INFO.txt",
                )
            )
            continue
        source_mtime, present = newest_sources_mtime(mod_ids, addon_root)
        if source_mtime is None:
            report.packages.append(
                PackageStatus(
                    package=package,
                    status="no_source",
                    source_mods=mod_ids,
                    detail="нет gamedata в addon/ для этого пакета",
                )
            )
            continue
        if source_mtime > package.info.built:
            report.packages.append(
                PackageStatus(
                    package=package,
                    status="outdated",
                    source_mtime=source_mtime,
                    source_mods=present,
                )
            )
        else:
            report.packages.append(
                PackageStatus(
                    package=package,
                    status="current",
                    source_mtime=source_mtime,
                    source_mods=present,
                )
            )

    if not untrusted:
        for mod_id in expected_aio_mod_ids(addon_root):
            if mod_id not in covered:
                report.missing.append(mod_id)

    return report


def _fmt_dt(value: datetime | None) -> str:
    if value is None:
        return "?"
    return value.isoformat(timespec="seconds")


def format_report(report: CheckReport, mo2: Path) -> str:
    lines: list[str] = [
        f"MO2: {mo2}",
        f"пакетов с BUILD_INFO.txt: {report.own_count}",
    ]
    if report.mtime_untrusted:
        lines.append(
            f"mtime недостоверен ({report.mtime_untrusted}). "
            "Сравнивать с addon/ нечего — пропуск."
        )
        if report.packages:
            lines.append("")
            lines.append("найденные пакеты (без сверки):")
            for item in report.packages:
                built = _fmt_dt(item.package.info.built)
                lines.append(f"  {item.package.mo2_name}  mod_id={item.package.info.mod_id}  built={built}")
        return "\n".join(lines) + "\n"

    by_status: dict[str, list[PackageStatus]] = {
        "outdated": [],
        "current": [],
        "no_built": [],
        "no_source": [],
    }
    for item in report.packages:
        by_status.setdefault(item.status, []).append(item)

    labels = {
        "outdated": "устарел",
        "current": "актуален",
        "no_built": "без даты built",
        "no_source": "нет источника в addon/",
    }
    for key in ("outdated", "current", "no_built", "no_source"):
        items = by_status.get(key) or []
        if not items:
            continue
        lines.append("")
        lines.append(f"{labels[key]}:")
        for item in items:
            built = _fmt_dt(item.package.info.built)
            if key in ("outdated", "current"):
                src = _fmt_dt(item.source_mtime)
                extra = ""
                if len(item.source_mods) > 1:
                    # для AIO показать, откуда свежий mtime
                    extra = f"  sources={len(item.source_mods)}"
                lines.append(
                    f"  {item.package.mo2_name}  built={built}  source={src}{extra}"
                )
            else:
                detail = f"  ({item.detail})" if item.detail else ""
                lines.append(f"  {item.package.mo2_name}  mod_id={item.package.info.mod_id}{detail}")

    lines.append("")
    if report.missing:
        lines.append("не установлен:")
        for mod_id in report.missing:
            lines.append(f"  {mod_id}")
    else:
        lines.append("не установлен: нет")
    lines.append(
        "(SKIP и SEPARATE из _pack_kristiano_aio в «не установлен» не входят.)"
    )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Сверить установленные в MO2 пакеты с addon/"
    )
    parser.add_argument(
        "mo2",
        type=Path,
        help="папка MO2 (внутри ожидается mods/), не папка профиля",
    )
    parser.add_argument(
        "--addon-root",
        type=Path,
        default=ADDON_ROOT,
        help="корень addon/ (по умолчанию репозиторий)",
    )
    parser.add_argument(
        "--no-mtime",
        action="store_true",
        help="не сравнивать mtime (как --no-verify у lint; clone/CI)",
    )
    args = parser.parse_args(argv)

    mo2 = args.mo2
    if not mo2.is_dir():
        print(f"Нет такой папки MO2: {mo2}", file=sys.stderr)
        return 2
    mods_dir = mo2 / "mods"
    if not mods_dir.is_dir():
        print(f"нет папки mods/ в {mo2}", file=sys.stderr)
        return 2

    report = check_installed(
        mo2,
        addon_root=args.addon_root,
        skip_mtime=bool(args.no_mtime),
    )
    sys.stdout.write(format_report(report, mo2))

    if report.mtime_untrusted:
        return 0
    if any(p.status == "outdated" for p in report.packages) or report.missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
