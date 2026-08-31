#!/usr/bin/env python3
"""Проверяет мод в addon/ на нарушения правил проекта.

Делает правила проверяемыми, а не декларативными: полная замена файлов сборки,
zzz-префиксы у .ltx, анонимные callback'и, дубли DLTX-секций, кодировка, контракт MCM.

    python3 tools/lint_addon.py                 # все моды
    python3 tools/lint_addon.py my_fix_weapon_jam
    python3 tools/lint_addon.py --cross         # плюс конфликты секций между модами
    python3 tools/lint_addon.py --unverified    # только непроверенные в игре / устаревшие
    python3 tools/lint_addon.py --no-verify     # без VERIFY-001 (CI, clone)
    python3 tools/lint_addon.py my_fix --json

Дополнительно предупреждает LUA-006/007 (контракт CreateTimeEvent в _g.script),
LUA-008 (полный проход id 1..65534) и FORK-001 (у форка нет файлов оригинала
из reference/addons/<vendor_source>/).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    GAME_TEXT_SUFFIXES,
    REPO_ROOT,
    decode_bytes,
    iter_files,
    looks_like_utf8_cyrillic,
    path_tail,
    rel,
)
from refindex import DEFAULT_ROOT  # noqa: E402

ADDON_ROOT = REPO_ROOT / "addon"
ALLOWED_TOP_LEVEL = {"meta.ini", "changelog.md", "readme.md", ".gitignore"}

LOAD_ORDER_HACK_RE = re.compile(r"^(z{3,}|a{3,})", re.I)
LOAD_ORDER_JUSTIFICATION_RE = re.compile(r"--\s*load-order:\s*после\s+\S+", re.I)
VENDOR_FORK_RE = re.compile(r"^vendor_fork\s*=\s*1$", re.I)
VENDOR_SOURCE_RE = re.compile(r"^vendor_source\s*=\s*(.+)$", re.I)
VERIFIED_DATE_RE = re.compile(r"^verified_date\s*=\s*(\S+)$", re.I)
VERIFY_SKIP_NAMES = frozenset({"meta.ini", "changelog.md", "readme.md"})
FORK_SILENCED_CODES = frozenset({"LUA-001", "LTX-001", "STRUCT-005"})
ANON_CALLBACK_RE = re.compile(
    r"RegisterScriptCallback\s*\(\s*[\"'][\w_]+[\"']\s*,\s*function", re.M
)
REGISTER_RE = re.compile(r"\bRegisterScriptCallback\s*\(\s*[\"']([\w_]+)[\"']")
UNREGISTER_RE = re.compile(r"\bUnregisterScriptCallback\s*\(\s*[\"']([\w_]+)[\"']")
# on_xml_read живёт в таблице dxml_core на жизнь процесса; снимать в on_game_end нельзя.
LUA003_UNREGISTER_EXCEPTIONS = frozenset({"on_xml_read"})
MCM_LOAD_RE = re.compile(r"^\s*function\s+on_mcm_load\s*\(", re.M)
SECTION_RE = re.compile(r"^\s*(!!|!|@)?\[([^\]\s]+)\]")
DLTX_NAME_RE = re.compile(r"^mod_(.+)_([^_]+)$")
# 4th arg is a named functor (not `function`). Extra params after it are allowed.
CREATE_NAMED_RE = re.compile(
    r"\b(?:CreateTimeEvent|(?:\w+\s*\.\s*)?create_time_event)\s*\(\s*"
    r"[^,]+,\s*[^,]+,\s*[^,]+,\s*([A-Za-z_]\w*)\s*[,\)]",
    re.S,
)
ALIFE_SCAN_RE = re.compile(r"for\s+\w+\s*=\s*1\s*,\s*(MAX_ALIFE_ID|65534|65535)\b")
ALIFE_SCAN_JUSTIFICATION_RE = re.compile(r"--\s*alife-scan:\s*запасной путь,\s*\S+", re.I)
LUA_STRING_OR_COMMENT_RE = re.compile(
    r"--\[\[[\s\S]*?\]\]|--[^\n]*|\[\[.*?\]\]|"
    r"\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'",
    re.S,
)
LUA_KW_RE = re.compile(r"\b(function|if|for|while|repeat|end|until)\b")
RETURN_TRUE_RE = re.compile(r"\breturn\s+true\b")

VAL_REQUIRED_TYPES = {"check", "track", "list", "radio_h", "radio_v", "input", "key_bind", "combo"}


@dataclass
class Finding:
    code: str
    severity: str  # "error" | "warn"
    message: str
    path: str = ""
    line: int = 0

    def format(self) -> str:
        mark = "ОШИБКА " if self.severity == "error" else "warning"
        where = f"{self.path}:{self.line}" if self.line else self.path
        where = f" {where}" if where else ""
        return f"  [{mark}] {self.code}{where}\n      {self.message}"


@dataclass
class ReferenceView:
    """Что известно про исходники сборки. Может быть пустым — тогда часть проверок пропускается.

    Читается напрямую из reference/, а не из кэша refindex: устаревший индекс
    давал бы ложные срабатывания там, где проверяется существование секций.
    """

    tails: dict = field(default_factory=dict)
    ltx_stems: set = field(default_factory=set)
    sections: dict = field(default_factory=dict)

    @property
    def populated(self) -> bool:
        return bool(self.tails)

    @classmethod
    def load(cls, root: Path) -> "ReferenceView":
        view = cls()
        if not root.exists():
            return view
        for path in iter_files(root, GAME_TEXT_SUFFIXES):
            view.tails.setdefault(path_tail(path).lower(), []).append(rel(path))
            if path.suffix.lower() != ".ltx":
                continue
            if not path.stem.lower().startswith("mod_"):
                view.ltx_stems.add(path.stem.lower())
            try:
                text = decode_bytes(path.read_bytes())
            except OSError:
                continue
            for line in text.splitlines():
                match = SECTION_RE.match(line.split(";", 1)[0].strip())
                if not match:
                    continue
                prefix, section = match.group(1), match.group(2)
                kind = {None: "base", "!": "override", "!!": "delete", "@": "safe"}[prefix]
                view.sections.setdefault(section, set()).add(kind)
        return view

    def has_file(self, path: Path) -> list:
        return self.tails.get(path_tail(path).lower(), [])

    def section_kinds(self, name: str) -> set:
        return self.sections.get(name, set())


def _meta_active_lines(addon_dir: Path) -> list[str]:
    """Строки meta.ini без комментариев `;` / `#` и без заголовков секций."""
    meta = addon_dir / "meta.ini"
    if not meta.is_file():
        return []
    try:
        text = decode_bytes(meta.read_bytes())
    except OSError:
        return []
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.split(";", 1)[0].split("#", 1)[0].strip()
        if not line or line.startswith("["):
            continue
        lines.append(line)
    return lines


def is_vendor_fork(addon_dir: Path) -> bool:
    """True, если в meta.ini стоит необязательный ключ vendor_fork=1."""
    return any(VENDOR_FORK_RE.match(line) for line in _meta_active_lines(addon_dir))


def read_vendor_source(addon_dir: Path) -> str | None:
    """Имя папки оригинала в reference/addons/ из vendor_source, или None."""
    for line in _meta_active_lines(addon_dir):
        match = VENDOR_SOURCE_RE.match(line)
        if not match:
            continue
        value = match.group(1).strip().strip("\"'")
        return value or None
    return None


def strip_load_order_prefixes(name: str) -> str:
    """Имя файла без ведущих z{3,}/a{3,} и следующего подчёркивания."""
    while True:
        match = LOAD_ORDER_HACK_RE.match(name)
        if not match:
            return name
        rest = name[match.end() :]
        if rest.startswith("_"):
            rest = rest[1:]
        if rest == name:
            return name
        name = rest


def fork_match_key(relpath: str) -> str:
    """Путь внутри gamedata для сверки форка: имя без load-order префикса."""
    posix = relpath.replace("\\", "/").lower()
    parent, _, name = posix.rpartition("/")
    key_name = strip_load_order_prefixes(name)
    if parent:
        return f"{parent}/{key_name}"
    return key_name


def vendor_source_folder(addons_root: Path, name: str) -> Path | None:
    """Папка оригинала, или None если имя не однокомпонентное."""
    if not name or Path(name).name != name:
        return None
    return addons_root / name


def read_verified_date(addon_dir: Path) -> date | None:
    """Дата проверки в игре из verified_date. Закомментированные ключи не считаются."""
    for line in _meta_active_lines(addon_dir):
        match = VERIFIED_DATE_RE.match(line)
        if not match:
            continue
        try:
            return date.fromisoformat(match.group(1).strip().strip("\"'"))
        except ValueError:
            return None
    return None


def newest_gamedata_date(addon_dir: Path) -> date | None:
    """Самая свежая дата файлов внутри gamedata/. Служебные имена пропускаются."""
    gamedata = addon_dir / "gamedata"
    if not gamedata.is_dir():
        return None
    newest: date | None = None
    for path in iter_files(gamedata):
        if path.name.lower() in VERIFY_SKIP_NAMES:
            continue
        try:
            stamp = datetime.fromtimestamp(path.stat().st_mtime).date()
        except OSError:
            continue
        if newest is None or stamp > newest:
            newest = stamp
    return newest


def verify_finding(addon_dir: Path) -> Finding | None:
    """VERIFY-001, если мод не проверялся в игре или изменён после verified_date."""
    verified = read_verified_date(addon_dir)
    if verified is None:
        return Finding("VERIFY-001", "warn", "в игре не проверялся", rel(addon_dir))
    newest = newest_gamedata_date(addon_dir)
    if newest is not None and newest > verified:
        return Finding(
            "VERIFY-001",
            "warn",
            f"изменён после последней проверки в игре: {verified.isoformat()}",
            rel(addon_dir),
        )
    return None


def mtime_untrusted_reason() -> str | None:
    """Почему mtime нельзя доверять (CI/clone), или None."""
    if os.environ.get("GITHUB_ACTIONS"):
        return "переменная GITHUB_ACTIONS — mtime после clone недостоверен"
    if os.environ.get("CI"):
        return "переменная CI — mtime после clone недостоверен"
    return None


def has_load_order_justification(text: str) -> bool:
    """Комментарий `-- load-order: после <что>` в первых 10 строках снимает ORDER-002."""
    for line in text.splitlines()[:10]:
        if LOAD_ORDER_JUSTIFICATION_RE.search(line):
            return True
    return False


def has_alife_scan_justification(text: str, match_start: int) -> bool:
    """Комментарий `-- alife-scan: запасной путь, <причина>` в трёх строках перед циклом снимает LUA-008."""
    line_no = text[:match_start].count("\n")
    lines = text.splitlines()
    window = lines[max(0, line_no - 3) : line_no]
    return any(ALIFE_SCAN_JUSTIFICATION_RE.search(line) for line in window)


def gamedata_relpath(path: Path) -> str:
    """Путь внутри gamedata/: 'configs/plugins/foo/menu.ltx'."""
    parts = path.parts
    lower = [p.lower() for p in parts]
    try:
        idx = lower.index("gamedata")
    except ValueError:
        return path_tail(path)
    rest = parts[idx + 1 :]
    if not rest:
        return ""
    return "/".join(rest).replace("\\", "/")


def ltx_sections(path: Path) -> set[str]:
    try:
        text = decode_bytes(path.read_bytes())
    except OSError:
        return set()
    names: set[str] = set()
    for line in text.splitlines():
        stripped = line.split(";", 1)[0].strip()
        match = SECTION_RE.match(stripped)
        if match:
            names.add(match.group(2))
    return names


def resolve_dltx_target(
    relpath: str,
    stems_by_dir: dict[str, set[str]],
    global_stems: set[str],
) -> str:
    """mod_<оригинал>_<суффикс>.ltx → <dir>/<оригинал>.ltx, иначе путь как есть."""
    posix = relpath.replace("\\", "/").lower()
    path = Path(posix)
    stem = path.stem
    suffix = path.suffix
    parent = path.parent.as_posix()
    if parent == ".":
        parent = ""
    if not stem.startswith("mod_"):
        return posix
    rest = stem[4:]
    parts = rest.split("_")
    if len(parts) < 2:
        return posix
    dir_stems = stems_by_dir.get(parent, set()) | global_stems
    for i in range(len(parts) - 1, 0, -1):
        original = "_".join(parts[:i])
        if original in dir_stems:
            if parent:
                return f"{parent}/{original}{suffix}"
            return f"{original}{suffix}"
    return posix


def collect_mod_ltx(addon_dir: Path) -> dict[str, set[str]]:
    """Путь внутри gamedata → имена секций в этом файле."""
    gamedata = addon_dir / "gamedata"
    found: dict[str, set[str]] = {}
    if not gamedata.is_dir():
        return found
    for path in iter_files(gamedata, {".ltx"}):
        relpath = gamedata_relpath(path)
        if not relpath:
            continue
        sections = ltx_sections(path)
        if sections:
            found[relpath.replace("\\", "/")] = sections
    return found


def cross_conflicts(addon_dirs: list[Path], reference: ReferenceView | None = None) -> list[Finding]:
    """Два мода патчат одну секцию в одном пути внутри gamedata."""
    if len(addon_dirs) < 2:
        return []

    per_mod: dict[str, dict[str, set[str]]] = {}
    stems_by_dir: dict[str, set[str]] = {}
    for addon_dir in addon_dirs:
        files = collect_mod_ltx(addon_dir)
        per_mod[addon_dir.name] = files
        for relpath in files:
            posix = relpath.replace("\\", "/").lower()
            path = Path(posix)
            parent = path.parent.as_posix()
            if parent == ".":
                parent = ""
            if not path.stem.startswith("mod_"):
                stems_by_dir.setdefault(parent, set()).add(path.stem)

    global_stems = set(reference.ltx_stems) if reference else set()

    owners: dict[tuple[str, str], set[str]] = {}
    for mod_id, files in per_mod.items():
        seen: set[tuple[str, str]] = set()
        for relpath, sections in files.items():
            target = resolve_dltx_target(relpath, stems_by_dir, global_stems)
            for section in sections:
                key = (target, section)
                if key in seen:
                    continue
                seen.add(key)
                owners.setdefault(key, set()).add(mod_id)

    grouped: dict[tuple[str, str, str], set[str]] = {}
    for (target, section), mods in owners.items():
        if len(mods) < 2:
            continue
        names = sorted(mods)
        for i, left in enumerate(names):
            for right in names[i + 1 :]:
                grouped.setdefault((left, right, target), set()).add(section)

    findings: list[Finding] = []
    for left, right, target in sorted(grouped):
        listed = ", ".join(f"[{name}]" for name in sorted(grouped[(left, right, target)]))
        findings.append(
            Finding(
                "CROSS-001",
                "warn",
                f"{left} и {right}: {listed}. Исход решает порядок в MO2.",
                target,
            )
        )
    return findings


def iter_innermost_tables(text: str):
    """Отдаёт содержимое самых вложенных {...} — это элементы дерева опций MCM."""
    stack: list[int] = []
    for i, ch in enumerate(text):
        if ch == "{":
            stack.append(i)
        elif ch == "}" and stack:
            start = stack.pop()
            inner = text[start + 1 : i]
            if "{" not in inner:
                yield start, inner


def mask_lua_literals(text: str) -> str:
    """Replace strings and comments with spaces so keyword scans ignore them.

    Length and newlines stay, so match offsets still map to line numbers.
    """

    def repl(match: re.Match) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))

    return LUA_STRING_OR_COMMENT_RE.sub(repl, text)


def lua_named_function_span(masked: str, name: str) -> tuple[int, int] | None:
    """Start/end offsets of `function name(...) ... end` in already-masked text."""
    header = re.search(
        rf"(?:^|\n)\s*(?:local\s+)?function\s+{re.escape(name)}\s*\(",
        masked,
    )
    if not header:
        return None
    start = masked.rfind("function", 0, header.end())
    if start < 0:
        return None
    depth = 0
    for kw in LUA_KW_RE.finditer(masked, start):
        word = kw.group(1)
        if word in {"function", "if", "for", "while", "repeat"}:
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return start, kw.end()
    return None


RETURN_CALL_RE = re.compile(r"\breturn\s+([A-Za-z_]\w*)\s*\(")


def function_returns_true(masked: str, name: str, seen: set[str] | None = None) -> bool:
    """True if the named function can return true, including `return other()`."""
    if seen is None:
        seen = set()
    if name in seen:
        return False
    seen.add(name)
    span = lua_named_function_span(masked, name)
    if not span:
        return False
    body = masked[span[0] : span[1]]
    if RETURN_TRUE_RE.search(body):
        return True
    for match in RETURN_CALL_RE.finditer(body):
        if function_returns_true(masked, match.group(1), seen):
            return True
    return False


class AddonLinter:
    def __init__(
        self,
        addon_dir: Path,
        reference: ReferenceView,
        *,
        verify: bool = True,
        reference_root: Path | None = None,
    ) -> None:
        self.dir = addon_dir
        self.reference = reference
        self.reference_root = reference_root if reference_root is not None else DEFAULT_ROOT
        self.vendor_fork = is_vendor_fork(addon_dir)
        self.verify = verify
        self.findings: list[Finding] = []

    def add(self, code: str, severity: str, message: str, path: Path | None = None, line: int = 0) -> None:
        if self.vendor_fork and code in FORK_SILENCED_CODES:
            return
        self.findings.append(
            Finding(code, severity, message, rel(path) if path else rel(self.dir), line)
        )

    # -- проверки уровня мода -----------------------------------------

    def check_structure(self) -> None:
        gamedata = self.dir / "gamedata"
        if not gamedata.is_dir():
            self.add("STRUCT-001", "error", "Нет каталога gamedata/ — MO2 такой мод не увидит.")
        if not (self.dir / "meta.ini").exists():
            self.add("STRUCT-002", "warn", "Нет meta.ini — мод будет безымянным в MO2.")
        if not (self.dir / "CHANGELOG.md").exists():
            self.add(
                "STRUCT-003",
                "warn",
                "Нет CHANGELOG.md — через месяц будет непонятно, что и зачем менялось.",
            )
        for entry in sorted(self.dir.iterdir()):
            if entry.is_dir() and entry.name != "gamedata":
                self.add("STRUCT-004", "warn", f"Каталог {entry.name}/ вне gamedata/ в мод не попадёт.", entry)
            if entry.is_file() and entry.name.lower() not in ALLOWED_TOP_LEVEL:
                self.add("STRUCT-005", "warn", f"Файл {entry.name} вне gamedata/ в мод не попадёт.", entry)

    def check_verified(self) -> None:
        finding = verify_finding(self.dir)
        if finding:
            self.findings.append(finding)

    def check_vendor_fork(self) -> None:
        """FORK-001: у форка нет файлов, которые есть в оригинале reference/addons/."""
        if not self.vendor_fork:
            return
        meta = self.dir / "meta.ini"
        meta_path = meta if meta.is_file() else None
        source_name = read_vendor_source(self.dir)
        if not source_name:
            self.add(
                "FORK-001",
                "warn",
                "vendor_fork=1 без vendor_source: сверка с оригиналом пропущена",
                meta_path,
            )
            return
        addons_root = self.reference_root / "addons"
        if not addons_root.is_dir():
            return
        source_dir = vendor_source_folder(addons_root, source_name)
        if source_dir is None or not source_dir.is_dir():
            self.add(
                "FORK-001",
                "warn",
                f"vendor_source={source_name}: нет папки reference/addons/{source_name}",
                meta_path,
            )
            return
        origin_relpaths = [
            path.relative_to(source_dir).as_posix() for path in iter_files(source_dir)
        ]
        gamedata = self.dir / "gamedata"
        our_keys: set[str] = set()
        if gamedata.is_dir():
            for path in iter_files(gamedata):
                our_keys.add(fork_match_key(gamedata_relpath(path)))
        for relpath in origin_relpaths:
            if fork_match_key(relpath) in our_keys:
                continue
            self.add(
                "FORK-001",
                "warn",
                f"нет {relpath} — есть в оригинале ({source_name})",
                self.dir / "gamedata" / Path(*relpath.split("/")),
            )

    # -- проверки уровня файла ----------------------------------------

    def check_file(self, path: Path) -> None:
        name = path.name.lower()
        suffix = path.suffix.lower()
        if name == "all.spawn":
            self.add("SPAWN-001", "error", "all.spawn в моде запрещён правилами проекта.", path)
        if suffix == ".ltx" and LOAD_ORDER_HACK_RE.match(name):
            self.add(
                "ORDER-001",
                "error",
                "Префикс ради порядка загрузки. Порядок .ltx задаётся списком модов MO2, а не именем файла.",
                path,
            )

        if path.suffix.lower() not in GAME_TEXT_SUFFIXES:
            return

        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            self.add("ENC-001", "error", "BOM в игровом файле: движок читает такой файл неправильно.", path)
        elif looks_like_utf8_cyrillic(data):
            self.add(
                "ENC-002",
                "warn",
                "Похоже на UTF-8 с кириллицей. Игровые файлы — Windows-1251, иначе в игре будет мусор.",
                path,
            )

        text = decode_bytes(data)
        suffix = path.suffix.lower()
        if suffix == ".ltx":
            self.check_ltx(path, text)
        elif suffix in {".script", ".lua"}:
            self.check_script(path, text)

    def check_ltx(self, path: Path, text: str) -> None:
        stem = path.stem
        is_patch = stem.lower().startswith("mod_")
        existing = self.reference.has_file(path)

        if not is_patch and existing:
            self.add(
                "LTX-001",
                "error",
                f"Полная замена файла сборки ({existing[0]}). Нужен DLTX-патч mod_{stem}_<мод>.ltx.",
                path,
            )

        if is_patch and self.reference.ltx_stems:
            match = DLTX_NAME_RE.match(stem.lower())
            base_known = False
            if match:
                candidate = match.group(1)
                while candidate and not base_known:
                    if candidate in self.reference.ltx_stems:
                        base_known = True
                        break
                    if "_" not in candidate:
                        break
                    candidate = candidate.rsplit("_", 1)[0]
            if not base_known:
                self.add(
                    "LTX-002",
                    "warn",
                    "Не удалось сопоставить патч с оригиналом. Имя должно быть "
                    "mod_<имя_оригинала>_<суффикс мода>.ltx, файл лежит рядом с оригиналом.",
                    path,
                )

        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.split(";", 1)[0].strip()
            match = SECTION_RE.match(stripped)
            if not match:
                continue
            prefix, section = match.group(1), match.group(2)
            kinds = self.reference.section_kinds(section)
            if not kinds:
                if prefix in {"!", "!!"} and self.reference.populated:
                    self.add(
                        "LTX-004",
                        "warn",
                        f"Патч секции [{section}], которой нет в reference/. "
                        f"Проверь: python3 tools/refindex.py section {section}",
                        path,
                        lineno,
                    )
                continue
            if prefix is None and "base" in kinds and is_patch:
                self.add(
                    "LTX-003",
                    "error",
                    f"Секция [{section}] уже объявлена в сборке. Дубль базовой секции "
                    f"роняет движок — используй ![{section}].",
                    path,
                    lineno,
                )

    def check_script(self, path: Path, text: str) -> None:
        if LOAD_ORDER_HACK_RE.match(path.name.lower()) and not has_load_order_justification(text):
            self.add(
                "ORDER-002",
                "warn",
                "Префикс задаёт порядок выполнения скриптов. Если гонка загрузки намеренная, "
                "добавь в первые 10 строк комментарий `-- load-order: после <что>`.",
                path,
            )

        existing = self.reference.has_file(path)
        if existing:
            self.add(
                "LUA-001",
                "warn",
                f"Файл повторяет скрипт сборки ({existing[0]}) и заменит его целиком. "
                "Обычно нужен monkey-patch из отдельного файла.",
                path,
            )

        for match in ANON_CALLBACK_RE.finditer(text):
            self.add(
                "LUA-002",
                "error",
                "Анонимная функция в RegisterScriptCallback: снять такой обработчик невозможно, "
                "он переживёт выход в меню.",
                path,
                text[: match.start()].count("\n") + 1,
            )

        registered = set(REGISTER_RE.findall(text))
        unregistered = set(UNREGISTER_RE.findall(text))
        leaked = registered - unregistered - LUA003_UNREGISTER_EXCEPTIONS
        if leaked:
            self.add(
                "LUA-003",
                "warn",
                "Нет UnregisterScriptCallback для: " + ", ".join(sorted(leaked)) +
                ". Снимай обработчики в on_game_end.",
                path,
            )

        if "actor_on_update" in registered and not re.search(r"time_global|CreateTimeEvent", text):
            self.add(
                "LUA-004",
                "warn",
                "actor_on_update без троттлинга: обработчик выполняется каждый тик. "
                "Тяжёлое — в CreateTimeEvent или по таймеру через time_global().",
                path,
            )

        if path.stem.endswith("_diag") and "DIAGNOSTIC ONLY" not in text:
            self.add(
                "LUA-005",
                "warn",
                "Диагностический скрипт без шапки '-- DIAGNOSTIC ONLY': такое легко случайно отправить в релиз.",
                path,
            )

        self.check_time_events(path, text)
        self.check_alife_id_scan(path, text)

        if MCM_LOAD_RE.search(text) and not path.stem.lower().endswith("mcm"):
            self.add(
                "MCM-001",
                "error",
                "on_mcm_load в файле, имя которого не заканчивается на mcm.script — MCM его не найдёт.",
                path,
            )

        if "ui_mcm.get" in text and not re.search(r"ui_mcm\s+(?:and|~=)|if\s+ui_mcm", text):
            self.add(
                "MCM-002",
                "warn",
                "ui_mcm.get без проверки наличия ui_mcm: мод упадёт у игрока без MCM.",
                path,
            )

        if path.stem.lower().endswith("mcm"):
            self.check_mcm_options(path, text)

    def check_time_events(self, path: Path, text: str) -> None:
        """LUA-006 / LUA-007: контракт CreateTimeEvent из _g.script."""
        masked = mask_lua_literals(text)
        seen_never_true: set[str] = set()
        for match in CREATE_NAMED_RE.finditer(masked):
            name = match.group(1)
            if name in seen_never_true:
                continue
            if function_returns_true(masked, name):
                continue
            if not lua_named_function_span(masked, name):
                continue
            seen_never_true.add(name)
            self.add(
                "LUA-006",
                "warn",
                f"{name} передана в CreateTimeEvent и нигде не возвращает true: "
                "слот останется в очереди (_g.script ProcessEventQueue).",
                path,
                text[: match.start()].count("\n") + 1,
            )

        seen_self_retry: set[str] = set()
        for match in CREATE_NAMED_RE.finditer(masked):
            name = match.group(1)
            if name in seen_self_retry:
                continue
            span = lua_named_function_span(masked, name)
            if not span:
                continue
            start, end = span
            body = masked[start:end]
            self_create = None
            for inner in CREATE_NAMED_RE.finditer(body):
                if inner.group(1) == name:
                    self_create = inner
                    break
            if not self_create:
                continue
            after = body[self_create.end() :]
            if "RemoveTimeEvent" in after:
                continue
            if not RETURN_TRUE_RE.search(after):
                continue
            seen_self_retry.add(name)
            self.add(
                "LUA-007",
                "warn",
                f"{name} заново CreateTimeEvent с теми же id и возвращает true: "
                "пока слот жив, Create — no-op, return true его снимает, retry не будет.",
                path,
                text[: start + self_create.start()].count("\n") + 1,
            )

    def check_alife_id_scan(self, path: Path, text: str) -> None:
        """LUA-008: полный проход 1..65534 через alife():object."""
        masked = mask_lua_literals(text)
        for match in ALIFE_SCAN_RE.finditer(masked):
            if has_alife_scan_justification(text, match.start()):
                continue
            self.add(
                "LUA-008",
                "warn",
                "Полный проход id 1..65534: каждый шаг — alife():object. "
                "На загрузке/смене уровня это хитч. Нужен iterate_objects или чанк. "
                "Запасной путь: `-- alife-scan: запасной путь, <причина>` в трёх строках перед циклом.",
                path,
                text[: match.start()].count("\n") + 1,
            )

    def check_mcm_options(self, path: Path, text: str) -> None:
        for start, inner in iter_innermost_tables(text):
            type_match = re.search(r"type\s*=\s*[\"'](\w+)[\"']", inner)
            if not type_match or type_match.group(1) not in VAL_REQUIRED_TYPES:
                continue
            lineno = text[:start].count("\n") + 1
            option_id = re.search(r"id\s*=\s*[\"']([\w_]+)[\"']", inner)
            label = option_id.group(1) if option_id else type_match.group(1)
            if not re.search(r"\bval\s*=", inner):
                self.add(
                    "MCM-003",
                    "error",
                    f"Опция '{label}' без поля val. ui_mcm.script падает при открытии меню "
                    "(val is manditory).",
                    path,
                    lineno,
                )
            if not re.search(r"\bdef\s*=", inner):
                self.add(
                    "MCM-004",
                    "warn",
                    f"Опция '{label}' без def: дефолт в меню и фолбэк в коде разойдутся.",
                    path,
                    lineno,
                )

    # -- запуск --------------------------------------------------------

    def run(self) -> list[Finding]:
        self.check_structure()
        self.check_vendor_fork()
        if self.verify:
            self.check_verified()
        for path in iter_files(self.dir):
            self.check_file(path)
        return self.findings


def lint(
    addon_dir: Path,
    reference: ReferenceView,
    *,
    verify: bool = True,
    reference_root: Path | None = None,
) -> list[Finding]:
    return AddonLinter(
        addon_dir, reference, verify=verify, reference_root=reference_root
    ).run()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Проверка мода на правила проекта")
    parser.add_argument("mod_id", nargs="*", help="имена модов в addon/ (по умолчанию все)")
    parser.add_argument("--addon-root", type=Path, default=ADDON_ROOT)
    parser.add_argument("--reference", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--strict", action="store_true", help="считать warning'и ошибками")
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--cross",
        action="store_true",
        help="искать конфликты секций между модами (один путь внутри gamedata + одно имя)",
    )
    parser.add_argument(
        "--unverified",
        action="store_true",
        help="только моды без проверки в игре или изменённые после verified_date",
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="не проверять verified_* (mtime после git clone недостоверен)",
    )
    args = parser.parse_args(argv)

    if args.mod_id:
        targets = [args.addon_root / name for name in args.mod_id]
    else:
        targets = [p for p in sorted(args.addon_root.glob("*")) if p.is_dir()]

    missing = [t for t in targets if not t.is_dir()]
    for target in missing:
        print(f"Нет такого мода: {rel(target)}", file=sys.stderr)
    targets = [t for t in targets if t.is_dir()]

    if not targets:
        if not missing:
            print("В addon/ пока нет модов. Создать: python3 tools/new_addon.py <mod_id>")
        return 2 if missing else 0

    if args.unverified:
        untrusted = mtime_untrusted_reason()
        if untrusted:
            print(f"mtime в этом окружении недостоверен ({untrusted}). --unverified всё равно выполняется.")
        listed = 0
        for target in targets:
            finding = verify_finding(target)
            if finding:
                print(f"{target.name}: {finding.message}")
                listed += 1
        if not listed:
            print("Все выбранные моды проверены в игре.")
        return 0

    skip_verify = bool(args.no_verify or mtime_untrusted_reason())
    skip_reason = None
    if args.no_verify:
        skip_reason = "--no-verify"
    elif skip_verify:
        skip_reason = mtime_untrusted_reason()

    reference = ReferenceView.load(args.reference)
    results: dict[str, list[Finding]] = {}
    fork_profile: dict[str, bool] = {}
    for target in targets:
        results[target.name] = lint(
            target, reference, verify=not skip_verify, reference_root=args.reference
        )
        fork_profile[target.name] = is_vendor_fork(target)

    cross_findings: list[Finding] = []
    if args.cross:
        cross_findings = cross_conflicts(targets, reference)

    if args.json:
        payload = {
            "reference_populated": reference.populated,
            "mods": {
                name: [finding.__dict__ for finding in findings] for name, findings in results.items()
            },
        }
        if args.cross:
            payload["cross"] = [finding.__dict__ for finding in cross_findings]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if not reference.populated:
            print(
                "reference/ пуст — проверки на замену файлов сборки и существование секций пропущены.\n"
                "См. docs/setup.md.\n"
            )
        if skip_reason:
            print(f"Проверка в игре пропущена: {skip_reason}.")
            print()
        for name, findings in results.items():
            errors = [f for f in findings if f.severity == "error"]
            warns = [f for f in findings if f.severity == "warn"]
            status = "OK" if not findings else f"{len(errors)} ошибок, {len(warns)} предупреждений"
            if fork_profile.get(name):
                status = f"{status} — проверен в профиле форка"
            print(f"{name}: {status}")
            for finding in findings:
                print(finding.format())
            print()
        if args.cross:
            if cross_findings:
                print(f"Перекрёстные конфликты: {len(cross_findings)} предупреждений")
                for finding in cross_findings:
                    print(finding.format())
            else:
                print("Перекрёстные конфликты: нет")
            print()

    total_errors = sum(1 for fs in results.values() for f in fs if f.severity == "error")
    total_warns = sum(1 for fs in results.values() for f in fs if f.severity == "warn")
    total_warns += len(cross_findings)
    if total_errors or (args.strict and total_warns):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
