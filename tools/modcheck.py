#!/usr/bin/env python3
"""Сверка текста с правилами Discord Anomaly Anthology.

Канон: community/discord-rules.json (человекочитаемый текст — community/RULES.md).
scan — только кандидаты по ключевым словам, не приговор.

    python tools/modcheck.py lookup 5.1 7.3
    python tools/modcheck.py scan "а вот в гамме это лучше"
    python tools/modcheck.py list --section 8
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT  # noqa: E402

RULES_PATH = REPO_ROOT / "community" / "discord-rules.json"
SEVERITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "policy": 4,
}
YO_RE = re.compile("ё")
SHORT_TOKEN = 4


def load_rules(path: Path | None = None) -> dict:
    target = path or RULES_PATH
    return json.loads(target.read_text(encoding="utf-8"))


def articles_by_id(data: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for article in data.get("articles", []):
        aid = article.get("id")
        if not aid:
            raise ValueError("статья без id")
        if aid in out:
            raise ValueError("дубликат id: %s" % aid)
        out[aid] = article
    return out


def normalize(text: str) -> str:
    lowered = text.casefold()
    return YO_RE.sub("е", lowered)


def _keyword_hits(blob: str, keyword: str) -> bool:
    needle = normalize(keyword)
    if not needle:
        return False
    if len(needle) < SHORT_TOKEN:
        return re.search(r"(?<!\w)%s(?!\w)" % re.escape(needle), blob) is not None
    return needle in blob


def scan_text(data: dict, text: str) -> list[dict]:
    blob = normalize(text)
    hits: list[dict] = []
    seen: set[str] = set()
    for article in data.get("articles", []):
        aid = article["id"]
        matched: list[str] = []
        for keyword in article.get("keywords") or []:
            if _keyword_hits(blob, keyword):
                matched.append(keyword)
        for example in article.get("examples") or []:
            if _keyword_hits(blob, example) and example not in matched:
                matched.append(example)
        if not matched:
            continue
        if aid in seen:
            continue
        seen.add(aid)
        row = dict(article)
        row["matched"] = matched
        hits.append(row)
    hits.sort(
        key=lambda row: (
            SEVERITY_ORDER.get(row.get("severity") or "policy", 9),
            row["id"],
        )
    )
    return hits


def format_article(article: dict, *, matched: list[str] | None = None) -> str:
    lines = [
        "## %s — %s" % (article["id"], article.get("title") or ""),
        "Раздел: %s" % article.get("section", "?"),
        "Строгость: %s" % article.get("severity", "?"),
        "Наказание: %s" % article.get("punishment", "не указано"),
        "",
        article.get("text") or "",
    ]
    related = article.get("related") or []
    if related:
        lines.append("")
        lines.append("Смежные: %s" % ", ".join(related))
    if matched:
        lines.append("")
        lines.append("Сигналы: %s" % ", ".join(matched))
    return "\n".join(lines).rstrip() + "\n"


def cmd_lookup(data: dict, ids: list[str]) -> int:
    index = articles_by_id(data)
    missing = [aid for aid in ids if aid not in index]
    if missing:
        sys.stderr.write("нет пунктов: %s\n" % ", ".join(missing))
        return 1
    chunks = [format_article(index[aid]) for aid in ids]
    sys.stdout.write("\n".join(chunks))
    return 0


def cmd_list(data: dict, section: str | None) -> int:
    rows = []
    for article in data.get("articles", []):
        if section and str(article.get("section")) != section:
            continue
        rows.append(
            "%s\t%s\t%s\t%s"
            % (
                article["id"],
                article.get("severity") or "",
                article.get("punishment") or "",
                article.get("title") or "",
            )
        )
    if not rows:
        sys.stderr.write("пусто\n")
        return 1
    sys.stdout.write("\n".join(rows) + "\n")
    return 0


def cmd_scan(data: dict, text: str) -> int:
    hits = scan_text(data, text)
    if not hits:
        sys.stdout.write("совпадений по ключевым словам нет — это не оправдание и не приговор\n")
        return 0
    sys.stdout.write(
        "кандидаты (%d), вердикт по полному тексту пункта, не по этому списку:\n\n"
        % len(hits)
    )
    chunks = [
        format_article(article, matched=article.get("matched") or [])
        for article in hits
    ]
    sys.stdout.write("\n".join(chunks))
    conflicts = data.get("meta", {}).get("conflicts") or []
    hit_ids = {article["id"] for article in hits}
    shown = []
    for item in conflicts:
        ids = set(item.get("ids") or [])
        if ids & hit_ids:
            shown.append(item.get("note") or "")
    if shown:
        sys.stdout.write("\nконфликты формулировок:\n")
        for note in shown:
            sys.stdout.write("- %s\n" % note)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rules",
        type=Path,
        default=RULES_PATH,
        help="путь к discord-rules.json",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    lookup = sub.add_parser("lookup", help="показать пункты по id")
    lookup.add_argument("ids", nargs="+")

    listed = sub.add_parser("list", help="таблица пунктов")
    listed.add_argument("--section", help="только раздел, например 8")

    scan = sub.add_parser("scan", help="кандидаты по ключевым словам")
    scan.add_argument("text", nargs="+", help="сообщение игрока")

    args = parser.parse_args(argv)
    data = load_rules(args.rules)
    if args.cmd == "lookup":
        return cmd_lookup(data, args.ids)
    if args.cmd == "list":
        return cmd_list(data, args.section)
    return cmd_scan(data, " ".join(args.text))


if __name__ == "__main__":
    sys.exit(main())
