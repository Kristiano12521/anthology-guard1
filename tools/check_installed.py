#!/usr/bin/env python3
"""Сверка установленных в MO2 пакетов с источниками в addon/.

Находит в mods/ пакеты с BUILD_INFO.txt (наши сборки), сравнивает дату
built с mtime файлов в addon/<mod_id>/gamedata/, сообщает: устарел /
актуален / не установлен. При устаревших/отсутствующих — пути к архивам
в build/ для переустановки.

Путь MO2: аргумент, иначе ANTHOLOGY_MO2, иначе local.json {"mo2": "..."}.

mtime после git clone недостоверен (как VERIFY-001): CI / GITHUB_ACTIONS,
--no-mtime, или эвристика «все mtime в addon/*/gamedata/ в узком окне».

    python3 tools/check_installed.py
    python3 tools/check_installed.py "C:/Games/.../mo2"
    python3 tools/check_installed.py --reinstall
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, iter_files, rel  # noqa: E402
from lint_addon import VERIFY_SKIP_NAMES, mtime_untrusted_reason  # noqa: E402

ADDON_ROOT = REPO_ROOT / "addon"
BUILD_ROOT = REPO_ROOT / "build"
LOCAL_CONFIG_NAME = "local.json"
ENV_MO2 = "ANTHOLOGY_MO2"

# pack_bhs пишет mod_id: Anthology_BusyHands_Stability_Fix
BHS_BUILD_MOD_ID = "Anthology_BusyHands_Stability_Fix"

# После clone все файлы получают время чекаута — разброс mtime крошечный.
CLONE_MTIME_SPAN_SEC = 120.0
CLONE_MTIME_MIN_FILES = 20


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
    status: str  # "current" | "outdated" | "no_source" | "no_built" | "skipped"
    source_mtime: datetime | None = None
    source_mods: list[str] = field(default_factory=list)
    detail: str = ""


@dataclass
class ReinstallItem:
    """Что поставить/обновить в MO2 и откуда взять архив."""

    label: str
    reason: str
    archive: Path | None
    mo2_name: str | None = None


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


def collect_gamedata_mtimes(addon_root: Path) -> list[float]:
    """Все mtime файлов в addon/*/gamedata/ (без VERIFY_SKIP_NAMES)."""
    stamps: list[float] = []
    if not addon_root.is_dir():
        return stamps
    for child in sorted(addon_root.iterdir(), key=lambda p: p.name.lower()):
        gamedata = child / "gamedata"
        if not child.is_dir() or not gamedata.is_dir():
            continue
        for path in iter_files(gamedata):
            if path.name.lower() in VERIFY_SKIP_NAMES:
                continue
            try:
                stamps.append(path.stat().st_mtime)
            except OSError:
                continue
    return stamps


def addon_mtime_looks_like_clone(
    addon_root: Path,
    *,
    max_span_sec: float = CLONE_MTIME_SPAN_SEC,
    min_files: int = CLONE_MTIME_MIN_FILES,
) -> bool:
    """True, если разброс mtime похож на единый stamp после git clone."""
    stamps = collect_gamedata_mtimes(addon_root)
    if len(stamps) < min_files:
        return False
    return (max(stamps) - min(stamps)) <= max_span_sec


def resolve_mtime_untrusted(
    addon_root: Path,
    *,
    skip_mtime: bool = False,
) -> str | None:
    """Почему нельзя сравнивать mtime, или None."""
    if skip_mtime:
        return "--no-mtime"
    env_reason = mtime_untrusted_reason()
    if env_reason:
        return env_reason
    if addon_mtime_looks_like_clone(addon_root):
        return (
            f"mtime в addon/*/gamedata/ в окне {int(CLONE_MTIME_SPAN_SEC)}с "
            f"(похоже на git clone)"
        )
    return None


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

    untrusted = resolve_mtime_untrusted(addon_root, skip_mtime=skip_mtime)
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


def read_local_mo2(config_path: Path | None = None) -> Path | None:
    """Читает mo2 из local.json; None если файла/ключа нет."""
    path = config_path or (REPO_ROOT / LOCAL_CONFIG_NAME)
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    value = data.get("mo2")
    if not value or not isinstance(value, str):
        return None
    return Path(value)


def resolve_mo2(
    cli_path: Path | None = None,
    *,
    env: dict[str, str] | None = None,
    config_path: Path | None = None,
) -> tuple[Path | None, str]:
    """Путь MO2 и откуда взяли: cli | env | local.json | "".

    Приоритет: аргумент > ANTHOLOGY_MO2 > local.json.
    """
    if cli_path is not None:
        return cli_path, "cli"
    environ = env if env is not None else os.environ
    env_value = (environ.get(ENV_MO2) or "").strip()
    if env_value:
        return Path(env_value), "env"
    from_config = read_local_mo2(config_path)
    if from_config is not None:
        return from_config, "local.json"
    return None, ""


def mo2_missing_message() -> str:
    return (
        "Путь к MO2 не задан. Укажи аргументом, переменной "
        f"{ENV_MO2}, или ключом mo2 в {LOCAL_CONFIG_NAME} "
        f"(образец: {LOCAL_CONFIG_NAME}.example)."
    )


def _newest_matching(build_root: Path, prefixes: tuple[str, ...], *, suffix: str = ".zip") -> Path | None:
    if not build_root.is_dir():
        return None
    found: list[Path] = []
    for path in build_root.iterdir():
        if not path.is_file() or path.suffix.lower() != suffix:
            continue
        if any(path.name.startswith(prefix) for prefix in prefixes):
            found.append(path)
    if not found:
        return None
    return sorted(found, key=lambda p: (-p.stat().st_mtime, p.name))[0]


def find_archive_for_mod_id(mod_id: str, build_root: Path) -> Path | None:
    """Архив в build/ для mod_id из BUILD_INFO / addon/."""
    k = _kristiano()
    from build_prune import BHS_MOD_ID, BHS_PACK_STEM  # noqa: PLC0415

    if mod_id == k.AIO_NAME:
        exact = build_root / f"{k.AIO_NAME}.zip"
        return exact if exact.is_file() else None
    if mod_id in k.SEPARATE:
        mo2_name = k.SEPARATE[mod_id]
        exact = build_root / f"{mo2_name}.zip"
        return exact if exact.is_file() else None
    if mod_id == BHS_BUILD_MOD_ID or mod_id == BHS_MOD_ID:
        return _newest_matching(build_root, (BHS_PACK_STEM,))
    exact = build_root / f"{mod_id}-{_detect_version_safe(mod_id)}.zip"
    if exact.is_file():
        return exact
    return _newest_matching(build_root, (f"{mod_id}-",))


def _detect_version_safe(mod_id: str) -> str:
    from _common import detect_version  # noqa: PLC0415

    addon_dir = ADDON_ROOT / mod_id
    if addon_dir.is_dir():
        return detect_version(addon_dir)
    return "1.0.0"


def reinstall_items(
    report: CheckReport,
    *,
    build_root: Path | None = None,
    addon_root: Path | None = None,
) -> list[ReinstallItem]:
    """Список пакетов к переустановке с путями к zip в build/."""
    build_root = build_root or BUILD_ROOT
    addon_root = addon_root or ADDON_ROOT
    k = _kristiano()
    items: list[ReinstallItem] = []
    seen_labels: set[str] = set()

    def add(item: ReinstallItem) -> None:
        if item.label in seen_labels:
            return
        seen_labels.add(item.label)
        items.append(item)

    for status in report.packages:
        if status.status not in ("outdated", "no_built"):
            continue
        mod_id = status.package.info.mod_id
        reason = "устарел" if status.status == "outdated" else "нет даты built"
        add(
            ReinstallItem(
                label=status.package.mo2_name,
                reason=reason,
                archive=find_archive_for_mod_id(mod_id, build_root),
                mo2_name=status.package.mo2_name,
            )
        )

    if report.missing:
        aio_members = set(expected_aio_mod_ids(addon_root))
        missing_aio = [m for m in report.missing if m in aio_members]
        missing_other = [m for m in report.missing if m not in aio_members]
        if missing_aio:
            add(
                ReinstallItem(
                    label=k.AIO_NAME,
                    reason=f"не установлен (покрывает {len(missing_aio)} мод.)",
                    archive=find_archive_for_mod_id(k.AIO_NAME, build_root),
                    mo2_name=k.AIO_NAME,
                )
            )
        for mod_id in missing_other:
            mo2_name = k.SEPARATE.get(mod_id, mod_id)
            add(
                ReinstallItem(
                    label=mo2_name,
                    reason="не установлен",
                    archive=find_archive_for_mod_id(mod_id, build_root),
                    mo2_name=mo2_name,
                )
            )

    return items


def _fmt_dt(value: datetime | None) -> str:
    if value is None:
        return "?"
    return value.isoformat(timespec="seconds")


def _fmt_archive_path(archive: Path | None) -> str:
    """Путь к zip для вывода. Скобки в имени (напр. [DBG]) — в кавычках."""
    if archive is None:
        return "архив не найден в build/ — сначала собери"
    text = rel(archive)
    if any(ch in text for ch in "[]{}*?\"'"):
        return f'"{text}"'
    return text


def format_reinstall(items: list[ReinstallItem]) -> str:
    # ASCII "->" — не Unicode →: на Windows stdout часто cp1251.
    lines: list[str] = [
        "переустановить в MO2 (Install mod from archive -> заменить существующий, не создавать новый):",
    ]
    if not items:
        lines.append("  (нечего — всё актуально или сверка пропущена)")
        return "\n".join(lines) + "\n"
    # Один блок на пакет: label / причина / архив. Не печать внутри обхода sources.
    for item in items:
        lines.append(f"  {item.label}")
        lines.append(f"    причина: {item.reason}")
        lines.append(f"    архив: {_fmt_archive_path(item.archive)}")
    lines.append(
        "После установки снова: python3 tools/check_installed.py "
        "(убедись, что built в BUILD_INFO свежий)."
    )
    return "\n".join(lines) + "\n"


def format_report(
    report: CheckReport,
    mo2: Path,
    *,
    build_root: Path | None = None,
    addon_root: Path | None = None,
    include_reinstall: bool = True,
) -> str:
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
                lines.append(
                    f"  {item.package.mo2_name}  mod_id={item.package.info.mod_id}  built={built}"
                )
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
                lines.append(
                    f"  {item.package.mo2_name}  mod_id={item.package.info.mod_id}{detail}"
                )

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

    text = "\n".join(lines) + "\n"
    if include_reinstall:
        items = reinstall_items(report, build_root=build_root, addon_root=addon_root)
        if items:
            text += "\n" + format_reinstall(items)
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Сверить установленные в MO2 пакеты с addon/"
    )
    parser.add_argument(
        "mo2",
        nargs="?",
        type=Path,
        default=None,
        help="папка MO2 (mods/ внутри); иначе ANTHOLOGY_MO2 или local.json",
    )
    parser.add_argument(
        "--addon-root",
        type=Path,
        default=ADDON_ROOT,
        help="корень addon/ (по умолчанию репозиторий)",
    )
    parser.add_argument(
        "--build-root",
        type=Path,
        default=BUILD_ROOT,
        help="корень build/ для путей к архивам",
    )
    parser.add_argument(
        "--no-mtime",
        action="store_true",
        help="не сравнивать mtime (как --no-verify у lint; clone/CI)",
    )
    parser.add_argument(
        "--reinstall",
        action="store_true",
        help="только список переустановки с путями к zip",
    )
    args = parser.parse_args(argv)

    mo2, source = resolve_mo2(args.mo2)
    if mo2 is None:
        print(mo2_missing_message(), file=sys.stderr)
        return 2
    if not mo2.is_dir():
        where = f" ({source})" if source else ""
        print(f"Нет такой папки MO2{where}: {mo2}", file=sys.stderr)
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
    if args.reinstall:
        items = reinstall_items(
            report,
            build_root=args.build_root,
            addon_root=args.addon_root,
        )
        sys.stdout.write(format_reinstall(items))
    else:
        sys.stdout.write(
            format_report(
                report,
                mo2,
                build_root=args.build_root,
                addon_root=args.addon_root,
            )
        )

    if report.mtime_untrusted:
        return 0
    if any(p.status == "outdated" for p in report.packages) or report.missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
