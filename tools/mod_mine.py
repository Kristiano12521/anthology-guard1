"""Сопоставление строк лога X-Ray с модами из addon/."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from _common import REPO_ROOT, read_text

DEFAULT_ADDON_DIR = REPO_ROOT / "addon"

LOG_TAG_RE = re.compile(r'LOG_TAG\s*=\s*"(\[[^\]]+\])"', re.I)
PRINTF_TAG_RE = re.compile(r'printf\s*\(\s*"(\[[^\]]+\])', re.I)

FAILURE_RES = [
    re.compile(p, re.I)
    for p in (
        r"not found",
        r"NOT installed",
        r"was not captured",
        r"was not detected",
        r"patch marker was not found",
        r"guard NOT installed",
        r"\bfailed\b",
    )
]

LOAD_HINT_RE = re.compile(
    r"\b(loaded|installed|wrapped|registered|register\(\) wrapped)\b",
    re.I,
)

MAX_LINES_PER_MOD = 12


@dataclass(frozen=True)
class ModCatalogEntry:
    mod_id: str
    identifiers: tuple[str, ...]


@dataclass
class ModPresence:
    mod_id: str
    lines: Counter[str] = field(default_factory=Counter)
    failure_lines: Counter[str] = field(default_factory=Counter)

    @property
    def appeared(self) -> bool:
        return bool(self.lines)

    @property
    def has_failures(self) -> bool:
        return bool(self.failure_lines)

    @property
    def loaded_hint(self) -> bool:
        return any(LOAD_HINT_RE.search(line) for line in self.lines)


@dataclass
class ModScanResult:
    catalog: dict[str, ModCatalogEntry]
    present: dict[str, ModPresence]
    absent: list[str]

    def to_dict(self) -> dict:
        return {
            "absent": self.absent,
            "present": {
                mod_id: {
                    "appeared": presence.appeared,
                    "loaded_hint": presence.loaded_hint,
                    "has_failures": presence.has_failures,
                    "lines": presence.lines.most_common(MAX_LINES_PER_MOD),
                    "failure_lines": presence.failure_lines.most_common(MAX_LINES_PER_MOD),
                }
                for mod_id, presence in sorted(self.present.items())
            },
        }


def _normalize_tag(raw: str) -> set[str]:
    inner = raw.strip()
    if inner.startswith("[") and inner.endswith("]"):
        inner = inner[1:-1]
    base = re.split(r"\s+v%s", inner)[0].strip()
    out = {base, f"[{base}]"}
    if inner != base:
        out.add(inner)
        out.add(f"[{inner}]")
    return out


def extract_log_tags(text: str) -> set[str]:
    tags: set[str] = set()
    for pattern in (LOG_TAG_RE, PRINTF_TAG_RE):
        for match in pattern.finditer(text):
            tags.update(_normalize_tag(match.group(1)))
    return tags


def discover_addon_mods(addon_dir: Path | None = None) -> dict[str, ModCatalogEntry]:
    root = addon_dir or DEFAULT_ADDON_DIR
    catalog: dict[str, ModCatalogEntry] = {}
    if not root.is_dir():
        return catalog

    for mod_dir in sorted(root.iterdir()):
        if not mod_dir.is_dir() or mod_dir.name.startswith("."):
            continue
        identifiers: set[str] = {mod_dir.name, f"[{mod_dir.name}]"}
        scripts_dir = mod_dir / "gamedata" / "scripts"
        if scripts_dir.is_dir():
            for script in sorted(scripts_dir.glob("*.script")) + sorted(scripts_dir.glob("*.lua")):
                stem = script.stem
                identifiers.add(stem)
                identifiers.add(f"{stem}.script")
                identifiers.update(extract_log_tags(read_text(script)))
        catalog[mod_dir.name] = ModCatalogEntry(
            mod_id=mod_dir.name,
            identifiers=tuple(sorted(identifiers, key=len, reverse=True)),
        )
    return catalog


def _is_failure(line: str) -> bool:
    return any(rx.search(line) for rx in FAILURE_RES)


def _match_mods(line: str, catalog: dict[str, ModCatalogEntry]) -> set[str]:
    matched: set[str] = set()
    for entry in catalog.values():
        for ident in entry.identifiers:
            if ident and ident in line:
                matched.add(entry.mod_id)
                break
    return matched


def scan_log_for_mods(
    lines: list[str],
    catalog: dict[str, ModCatalogEntry] | None = None,
) -> ModScanResult:
    mods = catalog or discover_addon_mods()
    present = {mod_id: ModPresence(mod_id=mod_id) for mod_id in mods}
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        for mod_id in _match_mods(stripped, mods):
            presence = present[mod_id]
            presence.lines[stripped] += 1
            if _is_failure(stripped):
                presence.failure_lines[stripped] += 1
    absent = sorted(mod_id for mod_id, presence in present.items() if not presence.appeared)
    visible = {mod_id: presence for mod_id, presence in present.items() if presence.appeared}
    return ModScanResult(catalog=mods, present=visible, absent=absent)


def _status_label(presence: ModPresence) -> str:
    if presence.has_failures:
        return "есть отказы"
    if presence.loaded_hint:
        return "загрузился"
    return "есть строки"


def _format_line_items(counter: Counter[str], limit: int = MAX_LINES_PER_MOD) -> list[str]:
    out: list[str] = []
    for text, count in counter.most_common(limit):
        marker = f"x{count} " if count > 1 else ""
        out.append(f"- {marker}`{text[:220]}`")
    hidden = len(counter) - limit
    if hidden > 0:
        out.append(f"- … ещё {hidden} уникальных строк")
    return out


def format_mine_markdown(
    scan: ModScanResult,
    log_name: str,
    *,
    mine_only: bool = False,
) -> str:
    out: list[str] = []
    if mine_only:
        out.append(f"# Мои моды — {log_name}")
    else:
        out.append("## Мои моды")
    out.append("")

    if scan.absent:
        out.append(f"### Не появились в логе ({len(scan.absent)})")
        out.append("")
        out.append(
            "Мод есть в `addon/`, но в логе нет ни одной строки — "
            "скорее всего не установлен в MO2 или не попал в пакет."
        )
        out.append("")
        for mod_id in scan.absent:
            out.append(f"- `{mod_id}`")
        out.append("")

    if not scan.present:
        if not scan.absent:
            out.append("Каталог `addon/` пуст или в логе нет строк от своих модов.")
            out.append("")
        return "\n".join(out)

    with_failures = [
        (mod_id, presence)
        for mod_id, presence in sorted(scan.present.items())
        if presence.has_failures
    ]
    okish = [
        (mod_id, presence)
        for mod_id, presence in sorted(scan.present.items())
        if not presence.has_failures
    ]

    if with_failures:
        out.append(f"### С отказами ({len(with_failures)})")
        out.append("")
        for mod_id, presence in with_failures:
            out.append(f"#### `{mod_id}` — {_status_label(presence)}")
            out.append("")
            out.extend(_format_line_items(presence.lines))
            out.append("")

    if okish:
        out.append(f"### В логе без отказов ({len(okish)})")
        out.append("")
        for mod_id, presence in okish:
            out.append(f"#### `{mod_id}` — {_status_label(presence)}")
            out.append("")
            out.extend(_format_line_items(presence.lines))
            out.append("")

    return "\n".join(out)
