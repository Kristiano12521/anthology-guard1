#!/usr/bin/env python3
"""Проверяет мод в addon/ на нарушения правил проекта.

Делает правила проверяемыми, а не декларативными: полная замена файлов сборки,
zzz-префиксы, анонимные callback'и, дубли DLTX-секций, кодировка, контракт MCM.

    python3 tools/lint_addon.py                 # все моды
    python3 tools/lint_addon.py my_fix_weapon_jam
    python3 tools/lint_addon.py my_fix --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
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
ANON_CALLBACK_RE = re.compile(
    r"RegisterScriptCallback\s*\(\s*[\"'][\w_]+[\"']\s*,\s*function", re.M
)
REGISTER_RE = re.compile(r"\bRegisterScriptCallback\s*\(\s*[\"']([\w_]+)[\"']")
UNREGISTER_RE = re.compile(r"\bUnregisterScriptCallback\s*\(\s*[\"']([\w_]+)[\"']")
MCM_LOAD_RE = re.compile(r"^\s*function\s+on_mcm_load\s*\(", re.M)
SECTION_RE = re.compile(r"^\s*(!!|!|@)?\[([^\]\s]+)\]")
DLTX_NAME_RE = re.compile(r"^mod_(.+)_([^_]+)$")

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


class AddonLinter:
    def __init__(self, addon_dir: Path, reference: ReferenceView) -> None:
        self.dir = addon_dir
        self.reference = reference
        self.findings: list[Finding] = []

    def add(self, code: str, severity: str, message: str, path: Path | None = None, line: int = 0) -> None:
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

    # -- проверки уровня файла ----------------------------------------

    def check_file(self, path: Path) -> None:
        name = path.name.lower()
        if name == "all.spawn":
            self.add("SPAWN-001", "error", "all.spawn в моде запрещён правилами проекта.", path)
        if LOAD_ORDER_HACK_RE.match(name):
            self.add(
                "ORDER-001",
                "error",
                "Префикс ради порядка загрузки. Порядок задаётся списком модов MO2, а не именем файла.",
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
        leaked = registered - unregistered
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
        for path in iter_files(self.dir):
            self.check_file(path)
        return self.findings


def lint(addon_dir: Path, reference: ReferenceView) -> list[Finding]:
    return AddonLinter(addon_dir, reference).run()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Проверка мода на правила проекта")
    parser.add_argument("mod_id", nargs="*", help="имена модов в addon/ (по умолчанию все)")
    parser.add_argument("--addon-root", type=Path, default=ADDON_ROOT)
    parser.add_argument("--reference", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--strict", action="store_true", help="считать warning'и ошибками")
    parser.add_argument("--json", action="store_true")
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

    reference = ReferenceView.load(args.reference)
    results: dict[str, list[Finding]] = {}
    for target in targets:
        results[target.name] = lint(target, reference)

    if args.json:
        payload = {
            "reference_populated": reference.populated,
            "mods": {
                name: [finding.__dict__ for finding in findings] for name, findings in results.items()
            },
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if not reference.populated:
            print(
                "reference/ пуст — проверки на замену файлов сборки и существование секций пропущены.\n"
                "См. docs/setup.md.\n"
            )
        for name, findings in results.items():
            errors = [f for f in findings if f.severity == "error"]
            warns = [f for f in findings if f.severity == "warn"]
            status = "OK" if not findings else f"{len(errors)} ошибок, {len(warns)} предупреждений"
            print(f"{name}: {status}")
            for finding in findings:
                print(finding.format())
            print()

    total_errors = sum(1 for fs in results.values() for f in fs if f.severity == "error")
    total_warns = sum(1 for fs in results.values() for f in fs if f.severity == "warn")
    if total_errors or (args.strict and total_warns):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
