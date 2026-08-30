#!/usr/bin/env python3
"""Индекс по reference/: проверка, что функция, секция или callback реально существуют.

Инструмент против выдуманного API. Перед использованием незнакомой функции
движка — сначала сюда, потом в код.

    python3 tools/refindex.py build
    python3 tools/refindex.py find actor_on_first_update
    python3 tools/refindex.py section wpn_ak74
    python3 tools/refindex.py callback actor_on_item_use
    python3 tools/refindex.py stats
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, iter_files, read_text, rel  # noqa: E402

DEFAULT_ROOT = REPO_ROOT / "reference"
DEFAULT_INDEX = REPO_ROOT / ".cache" / "refindex.json"

SCRIPT_SUFFIXES = {".script", ".lua"}
LTX_SUFFIXES = {".ltx"}

FUNC_RE = re.compile(r"^\s*function\s+([\w_.:]+)\s*\(([^)]*)\)")
LOCAL_FUNC_RE = re.compile(r"^\s*local\s+function\s+([\w_]+)\s*\(([^)]*)\)")
ASSIGN_FUNC_RE = re.compile(r"^\s*(?:local\s+)?([\w_.]+)\s*=\s*function\s*\(([^)]*)\)")
CLASS_RE = re.compile(r'class\s*"([\w_]+)"')
SECTION_RE = re.compile(r"^\s*(!!|!|@)?\[([^\]\s]+)\]\s*(?::\s*(.*))?$")
CALLBACK_RE = re.compile(
    r"\b(RegisterScriptCallback|UnregisterScriptCallback|SendScriptCallback)\s*\(\s*[\"']([\w_]+)[\"']"
)


class Index:
    def __init__(self, data: dict) -> None:
        self.data = data

    # -- построение --------------------------------------------------

    @classmethod
    def build(cls, root: Path) -> "Index":
        functions: dict[str, list] = {}
        sections: dict[str, list] = {}
        callbacks: dict[str, list] = {}
        counts = {"files": 0, "scripts": 0, "ltx": 0}

        def add(bucket: dict[str, list], key: str, entry: list) -> None:
            bucket.setdefault(key, []).append(entry)

        for path in iter_files(root, SCRIPT_SUFFIXES | LTX_SUFFIXES):
            counts["files"] += 1
            relpath = rel(path)
            suffix = path.suffix.lower()
            try:
                text = read_text(path)
            except OSError:
                continue

            if suffix in SCRIPT_SUFFIXES:
                counts["scripts"] += 1
                stem = path.stem
                for lineno, line in enumerate(text.splitlines(), 1):
                    match = FUNC_RE.match(line)
                    if match:
                        name, params = match.group(1), match.group(2).strip()
                        entry = [relpath, lineno, "function", f"{name}({params})"]
                        add(functions, name, entry)
                        if "." not in name and ":" not in name:
                            add(functions, f"{stem}.{name}", entry)
                        else:
                            add(functions, re.split(r"[.:]", name)[-1], entry)
                        continue

                    match = LOCAL_FUNC_RE.match(line)
                    if match:
                        name, params = match.group(1), match.group(2).strip()
                        entry = [relpath, lineno, "local", f"local {name}({params})"]
                        add(functions, name, entry)
                        add(functions, f"{stem}.{name}", entry)
                        continue

                    match = ASSIGN_FUNC_RE.match(line)
                    if match:
                        name, params = match.group(1), match.group(2).strip()
                        entry = [relpath, lineno, "assigned", f"{name} = function({params})"]
                        add(functions, name, entry)
                        continue

                for match in CLASS_RE.finditer(text):
                    lineno = text[: match.start()].count("\n") + 1
                    add(functions, match.group(1), [relpath, lineno, "class", f'class "{match.group(1)}"'])

                for match in CALLBACK_RE.finditer(text):
                    lineno = text[: match.start()].count("\n") + 1
                    kind = {
                        "RegisterScriptCallback": "register",
                        "UnregisterScriptCallback": "unregister",
                        "SendScriptCallback": "send",
                    }[match.group(1)]
                    add(callbacks, match.group(2), [relpath, lineno, kind])

            elif suffix in LTX_SUFFIXES:
                counts["ltx"] += 1
                for lineno, line in enumerate(text.splitlines(), 1):
                    stripped = line.split(";", 1)[0].strip()
                    if not stripped.startswith(("[", "!", "@")):
                        continue
                    match = SECTION_RE.match(stripped)
                    if not match:
                        continue
                    prefix, name, parents = match.group(1), match.group(2), match.group(3)
                    kind = {None: "base", "!": "override", "!!": "delete", "@": "safe"}[prefix]
                    add(sections, name, [relpath, lineno, kind, (parents or "").strip()])

        data = {
            "version": 1,
            "root": rel(root),
            "built_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "stats": {
                **counts,
                "functions": len(functions),
                "sections": len(sections),
                "callbacks": len(callbacks),
            },
            "functions": functions,
            "sections": sections,
            "callbacks": callbacks,
        }
        return cls(data)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.data, ensure_ascii=False), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Index":
        return cls(json.loads(path.read_text(encoding="utf-8")))

    # -- запросы -----------------------------------------------------

    def lookup(self, bucket: str, name: str) -> list:
        entries = self.data.get(bucket, {})
        if name in entries:
            return entries[name]
        # обращение вида module.func, когда индекс знает только короткое имя
        short = re.split(r"[.:]", name)[-1]
        return entries.get(short, [])

    def suggest(self, bucket: str, name: str, limit: int = 8) -> list[str]:
        keys = list(self.data.get(bucket, {}).keys())
        short = re.split(r"[.:]", name)[-1].lower()
        close = difflib.get_close_matches(name, keys, n=limit, cutoff=0.7)
        if len(close) < limit:
            substr = [k for k in keys if short in k.lower() and k not in close]
            close.extend(sorted(substr, key=len)[: limit - len(close)])
        return close


# Порядок истины внутри reference/: anomaly → anthology → addons → прочее.
# docs/setup.md. На выводе, не в .cache/refindex.json.
_SOURCE_RANK = {
    "anomaly": 0,
    "anthology": 1,
    "addons": 2,
}
_SOURCE_LABEL = {
    "anomaly": "ваниль",
    "anthology": "anthology",
    "addons": "аддон",
    "other": "прочее",
}
_SOURCE_PRINT_ORDER = ("anomaly", "anthology", "addons", "other")


def source_kind(relpath: str) -> str:
    """Ключ источника по пути внутри reference/: anomaly / anthology / addons / other."""
    parts = relpath.replace("\\", "/").split("/")
    known = _SOURCE_RANK
    try:
        idx = parts.index("reference")
    except ValueError:
        idx = -1
    if idx >= 0 and idx + 1 < len(parts) and parts[idx + 1] in known:
        return parts[idx + 1]
    for part in parts:
        if part in known:
            return part
    return "other"


def source_priority(relpath: str) -> int:
    """Чем меньше число, тем раньше строка в find / section / callback."""
    return _SOURCE_RANK.get(source_kind(relpath), 3)


def source_label(relpath: str) -> str:
    return _SOURCE_LABEL[source_kind(relpath)]


def rank_entries(entries: list) -> list:
    """Сортировка для вывода: приоритет источника, затем путь, затем номер строки."""
    return sorted(entries, key=lambda e: (source_priority(e[0]), e[0], e[1]))


def format_omitted(omitted: list) -> str | None:
    """Сводка срезанных лимитом записей: сколько и из каких источников."""
    if not omitted:
        return None
    counts: dict[str, int] = {}
    for entry in omitted:
        kind = source_kind(entry[0])
        counts[kind] = counts.get(kind, 0) + 1
    parts = [
        f"{counts[kind]} [{_SOURCE_LABEL[kind]}]"
        for kind in _SOURCE_PRINT_ORDER
        if counts.get(kind)
    ]
    return f"  ещё {len(omitted)}: {', '.join(parts)}"


def find_usages(root: Path, name: str, limit: int) -> list[tuple[str, int, str]]:
    """Живой grep по reference/: где символ реально вызывается."""
    short = re.split(r"[.:]", name)[-1]
    pattern = re.compile(rf"\b{re.escape(short)}\b")
    found: list[tuple[str, int, str]] = []
    for path in iter_files(root, SCRIPT_SUFFIXES):
        try:
            text = read_text(path)
        except OSError:
            continue
        if short not in text:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if pattern.search(line) and not line.strip().startswith("--"):
                found.append((rel(path), lineno, line.strip()[:160]))
                if len(found) >= limit:
                    return found
    return found


def require_index(path: Path) -> Index:
    if not path.exists():
        print(
            f"Индекс не найден ({rel(path)}). Сначала: python3 tools/refindex.py build",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return Index.load(path)


def cmd_build(args: argparse.Namespace) -> int:
    root: Path = args.root
    if not root.exists():
        print(f"Нет каталога {rel(root)} — положи туда исходники сборки.", file=sys.stderr)
        return 2
    index = Index.build(root)
    index.save(args.index)
    stats = index.data["stats"]
    if stats["files"] == 0:
        print(
            f"{rel(root)} пуст: индекс построен, но проверять нечего. "
            "См. docs/setup.md — что положить в reference/.",
        )
        return 0
    print(
        "Индекс построен: {files} файлов ({scripts} скриптов, {ltx} ltx), "
        "{functions} функций, {sections} секций, {callbacks} callback'ов".format(**stats)
    )
    print(f"Файл: {rel(args.index)}")
    return 0


def cmd_find(args: argparse.Namespace) -> int:
    index = require_index(args.index)
    name = args.name
    entries = index.lookup("functions", name)

    if entries:
        ranked = rank_entries(entries)
        print(f"ОПРЕДЕЛЕНИЯ: {name} — найдено {len(ranked)}")
        for relpath, lineno, kind, signature in ranked[: args.limit]:
            print(f"  [{source_label(relpath)}]  {relpath}:{lineno}  [{kind}]  {signature}")
        omitted = format_omitted(ranked[args.limit :])
        if omitted:
            print(omitted)
    else:
        print(f"ОПРЕДЕЛЕНИЙ НЕТ: {name}")
        suggestions = index.suggest("functions", name)
        if suggestions:
            print("  Похожие имена: " + ", ".join(suggestions))
        print("  Не подтверждено. Не используй как факт — см. docs/api-verification.md")

    if not args.no_usages:
        usages = find_usages(args.root, name, args.usages)
        if usages:
            print(f"\nВЫЗОВЫ (первые {len(usages)}):")
            for relpath, lineno, line in usages:
                print(f"  {relpath}:{lineno}  {line}")
        elif not entries:
            print("\nВЫЗОВОВ ТОЖЕ НЕТ: символ в сборке не встречается.")

    return 0 if entries else 1


def cmd_section(args: argparse.Namespace) -> int:
    index = require_index(args.index)
    entries = index.lookup("sections", args.name)
    if not entries:
        print(f"СЕКЦИИ НЕТ: [{args.name}]")
        suggestions = index.suggest("sections", args.name)
        if suggestions:
            print("  Похожие: " + ", ".join(suggestions))
        print("  DLTX-патч в несуществующую секцию даёт CInifile::r_section при запуске.")
        return 1

    ranked = rank_entries(entries)
    print(f"СЕКЦИЯ [{args.name}] — {len(ranked)} объявлений")
    for relpath, lineno, kind, parents in ranked[: args.limit]:
        suffix = f" : {parents}" if parents else ""
        print(f"  [{source_label(relpath)}]  {relpath}:{lineno}  [{kind}]{suffix}")
    omitted = format_omitted(ranked[args.limit :])
    if omitted:
        print(omitted)
    kinds = {entry[2] for entry in entries}
    if "base" in kinds and len([e for e in entries if e[2] == "base"]) > 1:
        print("  ВНИМАНИЕ: несколько базовых объявлений — движок падает на дубле базовой секции.")
    return 0


def cmd_callback(args: argparse.Namespace) -> int:
    index = require_index(args.index)
    entries = index.lookup("callbacks", args.name)
    if not entries:
        print(f"CALLBACK НЕ НАЙДЕН: {args.name}")
        suggestions = index.suggest("callbacks", args.name)
        if suggestions:
            print("  Похожие: " + ", ".join(suggestions))
        print("  Регистрация несуществующего callback'а не выдаёт ошибку — обработчик просто не вызовется.")
        return 1

    ranked = rank_entries(entries)
    sends = [e for e in ranked if e[2] == "send"]
    print(f"CALLBACK {args.name} — {len(ranked)} упоминаний, из них диспатчей: {len(sends)}")
    for relpath, lineno, kind in ranked[: args.limit]:
        print(f"  [{source_label(relpath)}]  {relpath}:{lineno}  [{kind}]")
    omitted = format_omitted(ranked[args.limit :])
    if omitted:
        print(omitted)
    if not sends:
        print("  ВНИМАНИЕ: нет ни одного SendScriptCallback — callback может быть от модифицированных exe или не существовать.")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    index = require_index(args.index)
    data = index.data
    print(f"Индекс: {rel(args.index)}")
    print(f"Источник: {data['root']}, собран {data['built_at']}")
    for key, value in data["stats"].items():
        print(f"  {key}: {value}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Индекс исходников сборки в reference/")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="корень исходников")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help="файл индекса")
    parser.add_argument("--limit", type=int, default=20, help="сколько результатов показывать")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("build", help="построить индекс").set_defaults(func=cmd_build)

    p_find = sub.add_parser("find", help="найти функцию или класс")
    p_find.add_argument("name")
    p_find.add_argument("--usages", type=int, default=5, help="сколько вызовов показать")
    p_find.add_argument("--no-usages", action="store_true")
    p_find.set_defaults(func=cmd_find)

    p_section = sub.add_parser("section", help="найти LTX-секцию")
    p_section.add_argument("name")
    p_section.set_defaults(func=cmd_section)

    p_callback = sub.add_parser("callback", help="проверить callback")
    p_callback.add_argument("name")
    p_callback.set_defaults(func=cmd_callback)

    sub.add_parser("stats", help="статистика индекса").set_defaults(func=cmd_stats)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
