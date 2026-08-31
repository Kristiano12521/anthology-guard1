#!/usr/bin/env python3
"""Сжимает лог X-Ray / Anomaly в карточку вылета для разбора в Cursor.

Лог игры — это мегабайты, из которых полезны сотни байт. Скрипт вытаскивает
блок FATAL ERROR, нефатальные STACK TRACEBACK, Lua-кадры, осмысленные строки
перед падением и повторяющиеся предупреждения, после чего в чат уходит карточка,
а не весь файл.

    python3 tools/xraylog.py logs/xray_ivan.log --out logs/card.md
    python3 tools/xraylog.py logs/xray_ivan.log --archive
    python3 tools/xraylog.py logs/xray_ivan.log --warnings-only
    python3 tools/xraylog.py logs/xray_ivan.log --errors-only
    python3 tools/xraylog.py logs/xray_ivan.log --mine
    python3 tools/xraylog.py logs/xray_ivan.log --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, deque
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import REPO_ROOT, decode_bytes, filename, rel  # noqa: E402
from mod_mine import (  # noqa: E402
    DEFAULT_ADDON_DIR,
    ModScanResult,
    discover_addon_mods,
    format_mine_markdown,
    scan_log_for_mods,
)

DEFAULT_ARCHIVE_DIR = REPO_ROOT / "logs" / "cards"

FATAL_RE = re.compile(r"^\s*(?:-+\s*)?fatal error\s*(?:-+)?\s*$", re.I)
FIELD_RE = re.compile(
    r"^\s*(?:\[error\])?\s*(Expression|Function|File|Line|Description|Arguments)\s*:\s*(.*)$",
    re.I,
)
STACK_RE = re.compile(r"^\s*stack trace:", re.I)
LUA_TRACEBACK_RE = re.compile(r"^\s*[!~]?\s*STACK TRACEBACK\s*:?\s*$", re.I)
SEPARATOR_RE = re.compile(r"^\s*[!~]?\s*-{5,}\s*$")
SCRIPT_REF_RE = re.compile(r"([\w\-]+\.(?:script|lua))[:(](\d+)")
SCRIPT_NAME_RE = re.compile(r"([\w\-]+\.(?:script|lua))", re.I)
LINE_NUM_RES = [
    re.compile(r"\(line:\s*\d+\)", re.I),
    re.compile(r"(\.(?:script|lua))\(\d+\)", re.I),
    re.compile(r"(\.(?:script|lua)):\d+", re.I),
]
SECTION_RE = re.compile(r"[Cc]an't open section '([^']+)'")
VARIABLE_RE = re.compile(r"[Cc]an't find variable\s+'?([\w\-]+)'?\s+in\s+\[?'?([\w\-]+)'?\]?")
INCLUDE_RE = re.compile(r"[Cc]an't (?:find|open) include file\s*:?\s*'?([^'\s]+)'?")
BUILD_RE = re.compile(r"'xrCore'\s+build\s+(\d+)")
EXE_RE = re.compile(r"([A-Za-z0-9_]*Anomaly[A-Za-z0-9_]*\.exe)", re.I)

NOISE_RES = [
    re.compile(p, re.I)
    for p in (
        r"^\* phase (time|cmem)",
        r"^\* \[x-ray\]",
        r"^\* \[win32\]",
        r"^\* \[ D3D \]",
        r"^\* \[DETAILS\]",
        r"^refCount:",
        r"^SymInit:",
        r"^OS-Version:",
        r"^\* Detected",
        r"^\* CPU ",
        r"^\* Available",
        r"^\* Starting INPUT",
        r"^\* sound",
        r"^\s*$",
        r"^[A-Za-z]:\\.*\.(exe|dll)\s*:",
        r"^\s*\d+\s*:\s*\[C\]",
        r"^-{5,}$",
        r"^Compiling shader",
        r"^compiling shader",
        r"^\* Loading HOM",
        r"^\* t-report",
        r"^~ Duplicate",
    )
]

WARNING_PREFIXES = ("!", "~")
MAX_NONFATAL_GROUPS = 5
MAX_NONFATAL_FRAMES = 40

# Обёртки движка в Lua-стеке: abort() всегда оставляет _g.script сверху,
# axr_main.script бывает следующим диспетчером. Дополнять по мере нужды.
INFRA_SCRIPTS = (
    "_g.script",
    "axr_main.script",
)
C_FRAME_RE = re.compile(r"\[C\]:\s*in function", re.I)

# Нормализация путей и чисел, чтобы одинаковые по смыслу warning'и группировались.
NORMALIZE_RES = [
    (re.compile(r"[A-Za-z]:\\[^\s'\"]+\\"), ""),
    (re.compile(r"\b\d{3,}\b"), "N"),
]


def is_noise(line: str) -> bool:
    return any(rx.search(line) for rx in NOISE_RES)


def normalize_warning(line: str) -> str:
    out = line.strip()
    for rx, repl in NORMALIZE_RES:
        out = rx.sub(repl, out)
    return out


def is_separator(line: str) -> bool:
    return bool(SEPARATOR_RE.match(line.strip()))


def strip_line_numbers(frame: str) -> str:
    """Сигнатура кадра: тот же стек без номеров строк."""
    out = frame.strip()
    out = LINE_NUM_RES[0].sub("", out)
    out = LINE_NUM_RES[1].sub(r"\1", out)
    out = LINE_NUM_RES[2].sub(r"\1", out)
    return re.sub(r"\s+", " ", out).strip()


def _frame_script(frame: str) -> str:
    match = SCRIPT_NAME_RE.search(frame)
    return match.group(1) if match else ""


def culprit_script(frames: list[str]) -> str:
    """Заголовок группы: первый кадр не из инфраструктуры.

    Строки ``[C]: in function`` пропускаются. ``abort()`` кладёт сверху
    ``_g.script`` — это обёртка, не виновник; следующие кадры из
    INFRA_SCRIPTS тоже. Если первый Lua-кадр уже место отказа
    (``axr_main.script`` / ``callback_set``), он остаётся заголовком.
    Если после фильтра ничего не осталось — верхний скриптовый кадр.
    """
    infra = {name.lower() for name in INFRA_SCRIPTS}
    first_script = ""
    skip_infra = False
    for frame in frames:
        if C_FRAME_RE.search(frame):
            continue
        name = _frame_script(frame)
        if not name:
            continue
        key = name.lower()
        if not first_script:
            first_script = name
            if key == "_g.script":
                skip_infra = True
                continue
            return name
        if skip_infra and key in infra:
            continue
        return name
    return first_script


def traceback_trigger(recent: deque[str]) -> str:
    """Предыдущая непустая строка с префиксом ! или ~, минуя разделители."""
    for prev in reversed(recent):
        stripped = prev.strip()
        if not stripped or is_separator(stripped) or LUA_TRACEBACK_RE.match(stripped):
            continue
        if stripped.lstrip()[:1] in WARNING_PREFIXES:
            return stripped
        return ""
    return ""


class NonfatalGroup:
    def __init__(self, trigger: str, frames: list[str]) -> None:
        self.trigger = trigger
        self.frames = frames
        self.count = 1
        self.signature = tuple(strip_line_numbers(f) for f in frames)
        self.culprit = culprit_script(frames)

    def to_dict(self) -> dict:
        return {
            "count": self.count,
            "trigger": self.trigger,
            "frames": self.frames[:15],
            "culprit": self.culprit,
        }


class LogReport:
    def __init__(self, path: Path, addon_dir: Path | None = None) -> None:
        self.path = path
        self.addon_dir = addon_dir or DEFAULT_ADDON_DIR
        self.size = path.stat().st_size
        self.line_count = 0
        self.fatal_lines: list[str] = []
        self.fields: dict[str, str] = {}
        self.stack_lines: list[str] = []
        self.context: list[str] = []
        self.script_refs: list[str] = []
        self.warnings: Counter[str] = Counter()
        self.nonfatal_errors: list[NonfatalGroup] = []
        self.log_lines: list[str] = []
        self.mod_scan: ModScanResult | None = None
        self.engine_build: str | None = None
        self.exe: str | None = None
        self.crashed = False

    # -- разбор ------------------------------------------------------

    def parse(self, context_lines: int) -> None:
        recent: deque[str] = deque(maxlen=context_lines)
        recent_raw: deque[str] = deque(maxlen=30)
        in_fatal = False
        in_stack = False
        in_lua_tb = False
        tb_frames: list[str] = []
        tb_trigger = ""
        groups: dict[tuple[str, ...], NonfatalGroup] = {}
        seen_refs: set[str] = set()

        def close_traceback() -> None:
            nonlocal in_lua_tb, tb_frames, tb_trigger
            if tb_frames:
                group = NonfatalGroup(tb_trigger, tb_frames)
                existing = groups.get(group.signature)
                if existing:
                    existing.count += 1
                else:
                    groups[group.signature] = group
            in_lua_tb = False
            tb_frames = []
            tb_trigger = ""

        def uncount_warning(text: str) -> None:
            key = normalize_warning(text)
            if key in self.warnings:
                self.warnings[key] -= 1
                if self.warnings[key] <= 0:
                    del self.warnings[key]

        with self.path.open("rb") as handle:
            for raw in handle:
                line = decode_bytes(raw).rstrip("\r\n")
                self.line_count += 1
                stripped = line.strip()

                if stripped:
                    recent_raw.append(stripped)
                    self.log_lines.append(stripped)

                if self.engine_build is None:
                    match = BUILD_RE.search(line)
                    if match:
                        self.engine_build = match.group(1)
                if self.exe is None:
                    match = EXE_RE.search(line)
                    if match:
                        self.exe = match.group(1)

                if in_lua_tb and not in_fatal:
                    if LUA_TRACEBACK_RE.match(stripped) or FATAL_RE.match(line):
                        close_traceback()
                    elif is_separator(stripped):
                        close_traceback()
                        if not is_noise(line):
                            recent.append(line)
                        continue
                    else:
                        if stripped:
                            tb_frames.append(stripped)
                        if len(tb_frames) >= MAX_NONFATAL_FRAMES:
                            close_traceback()
                        continue

                if not in_fatal and FATAL_RE.match(line):
                    in_fatal = True
                    self.crashed = True
                    self.context = list(recent)
                    self.fatal_lines.append(line.strip())
                    continue

                if in_fatal:
                    if STACK_RE.match(line):
                        in_stack = True
                        self.fatal_lines.append(line.strip())
                        continue
                    if in_stack:
                        if line.strip() and not is_noise(line):
                            self.stack_lines.append(line.strip())
                        if len(self.stack_lines) > 60:
                            in_fatal = in_stack = False
                    else:
                        match = FIELD_RE.match(line)
                        if match:
                            self.fields[match.group(1).capitalize()] = match.group(2).strip()
                            self.fatal_lines.append(line.strip())
                        elif line.strip():
                            self.fatal_lines.append(line.strip())

                if not in_fatal and LUA_TRACEBACK_RE.match(stripped):
                    tb_trigger = traceback_trigger(recent_raw)
                    if tb_trigger:
                        uncount_warning(tb_trigger)
                    in_lua_tb = True
                    tb_frames = []
                    continue

                for ref_match in SCRIPT_REF_RE.finditer(line):
                    ref = f"{ref_match.group(1)}:{ref_match.group(2)}"
                    if ref not in seen_refs:
                        seen_refs.add(ref)
                        self.script_refs.append(ref)

                lead = stripped.lstrip()[:1] if stripped else ""
                if (
                    lead in WARNING_PREFIXES
                    and len(stripped) > 2
                    and not is_separator(stripped)
                    and not LUA_TRACEBACK_RE.match(stripped)
                ):
                    self.warnings[normalize_warning(stripped)] += 1

                if not is_noise(line):
                    recent.append(line)

        if in_lua_tb:
            close_traceback()

        self.nonfatal_errors = sorted(
            groups.values(),
            key=lambda group: (-group.count, group.culprit),
        )

        if not self.crashed:
            self.context = list(recent)

        catalog = discover_addon_mods(self.addon_dir)
        self.mod_scan = scan_log_for_mods(self.log_lines, catalog)

    # -- выводы ------------------------------------------------------

    @property
    def haystack(self) -> str:
        return " ".join(
            [
                self.fields.get("Function", ""),
                self.fields.get("Description", ""),
                self.fields.get("Arguments", ""),
                self.fields.get("File", ""),
            ]
        )

    def missing_section(self) -> str | None:
        match = SECTION_RE.search(self.haystack)
        return match.group(1) if match else None

    def missing_variable(self) -> tuple[str, str] | None:
        match = VARIABLE_RE.search(self.haystack)
        return (match.group(1), match.group(2)) if match else None

    def missing_include(self) -> str | None:
        match = INCLUDE_RE.search(self.haystack)
        return match.group(1) if match else None

    def lua_refs(self) -> list[str]:
        """Кадры скриптов из блока FATAL ERROR и стека — самые релевантные."""
        text = " ".join([self.haystack] + self.stack_lines)
        refs: list[str] = []
        for match in SCRIPT_REF_RE.finditer(text):
            ref = f"{match.group(1)}:{match.group(2)}"
            if ref not in refs:
                refs.append(ref)
        return refs

    def classify(self) -> tuple[str, list[str]]:
        if not self.crashed:
            if self.nonfatal_errors:
                groups = len(self.nonfatal_errors)
                total = sum(group.count for group in self.nonfatal_errors)
                top = self.nonfatal_errors[0]
                culprit = top.culprit or "неизвестный скрипт"
                return (
                    f"вылета нет, есть повторяющиеся ошибки ({groups} групп)",
                    [
                        f"Блок FATAL ERROR не найден, но есть {total} нефатальных Lua-ошибок, {groups} уникальных сигнатур.",
                        "Смотри секцию «Нефатальные ошибки»: повторяющиеся traceback'и — основной класс проблем этой сборки.",
                        f"Самая частая: `{culprit}` ×{top.count}.",
                    ],
                )
            return (
                "вылета в логе нет",
                [
                    "Блок FATAL ERROR не найден: либо лог от нормального сеанса, "
                    "либо игра упала без записи (проверь конец файла вручную).",
                ],
            )

        text = self.haystack.lower()
        section = self.missing_section()
        variable = self.missing_variable()
        include = self.missing_include()

        if "lua_error" in text or "cscriptengine" in text or self.lua_refs():
            refs = self.lua_refs()
            hints = [
                "Класс: ошибка Lua. Иди по цепочке от кадра к месту, где значение должно было появиться.",
            ]
            if refs:
                hints.append(f"Первый кадр: {refs[0]} — найди этот файл в reference/ и открой строку.")
                hints.append(
                    f"Проверь, не переопределяет ли этот скрипт какой-нибудь мод: "
                    f"tools/refindex.py find {refs[0].split(':')[0].split('.')[0]}"
                )
            hints.append("nil в кадре — это симптом. Причина обычно в другом файле, выше по цепочке.")
            return "Lua error", hints

        if section:
            return (
                "конфиг: нет секции",
                [
                    f"Секция '{section}' не найдена движком.",
                    f"Проверь, существует ли она вообще: python3 tools/refindex.py section {section}",
                    "Если секции нет — её ждёт мод, а объявлявший её мод не установлен или отключён.",
                    "Если есть — смотри, не удалил ли её чей-то DLTX-патч (!![section]) и не опечатка ли в патче.",
                ],
            )

        if variable:
            field, sect = variable
            return (
                "конфиг: нет поля",
                [
                    f"Поле '{field}' отсутствует в секции '{sect}'.",
                    f"python3 tools/refindex.py section {sect} — кто объявляет секцию.",
                    "Частая причина: DLTX-патч удалил поле (!key) или override заменил секцию целиком (![section]).",
                ],
            )

        if include:
            return (
                "конфиг: битый include",
                [
                    f"Не найден включаемый файл: {include}.",
                    "Обычно остаётся после удаления мода, чьи конфиги ещё подключаются через #include.",
                ],
            )

        if any(k in text for k in ("d3d", "render", "shader", "texture", "out of memory", "xrmemory")):
            return (
                "движок/ресурсы",
                [
                    "Это не скрипты: рендер, шейдеры, текстуры или память.",
                    "Проверь недавно поставленные графические моды и настройки Modded Exes.",
                ],
            )

        return (
            "не классифицировано",
            [
                "Сигнатура не распознана. Смотри блок FATAL ERROR целиком и строки перед ним.",
                "Если Lua-кадров нет, а падение в шедулере или потоках — проверь тумблеры MT в опциях Modded Exes.",
            ],
        )

    # -- вывод -------------------------------------------------------

    def to_dict(self, max_warnings: int) -> dict:
        crash_class, hints = self.classify()
        return {
            "file": rel(self.path),
            "size_bytes": self.size,
            "lines": self.line_count,
            "crashed": self.crashed,
            "class": crash_class,
            "engine_build": self.engine_build,
            "exe": self.exe,
            "fields": self.fields,
            "lua_refs": self.lua_refs(),
            "all_script_refs": self.script_refs[:50],
            "missing_section": self.missing_section(),
            "missing_variable": self.missing_variable(),
            "hints": hints,
            "warnings": self.warnings.most_common(max_warnings),
            "nonfatal_groups": len(self.nonfatal_errors),
            "nonfatal_errors": [group.to_dict() for group in self.nonfatal_errors[:MAX_NONFATAL_GROUPS]],
            "mods": self.mod_scan.to_dict() if self.mod_scan else None,
            "context": self.context,
            "stack": self.stack_lines[:30],
        }

    def mine_markdown(self, mine_only: bool = False) -> str:
        if self.mod_scan is None:
            catalog = discover_addon_mods(self.addon_dir)
            self.mod_scan = scan_log_for_mods(self.log_lines, catalog)
        return format_mine_markdown(
            self.mod_scan,
            filename(self.path),
            mine_only=mine_only,
        )

    def to_markdown(
        self,
        max_warnings: int,
        warnings_only: bool,
        errors_only: bool = False,
        analyzed_on: date | None = None,
        mine_only: bool = False,
    ) -> str:
        if mine_only:
            return self.mine_markdown(mine_only=True)

        crash_class, hints = self.classify()
        hide_crash = warnings_only or errors_only
        if self.size >= 1024 * 1024:
            size = f"{self.size / (1024 * 1024):.1f} МБ"
        else:
            size = f"{self.size / 1024:.0f} КБ"
        day = (analyzed_on or date.today()).isoformat()
        log_name = filename(self.path)
        out: list[str] = []
        out.append(f"# Карточка лога — {log_name}")
        out.append("")
        out.append(f"- Файл: `{log_name}` ({size}, {self.line_count} строк)")
        out.append(f"- Дата разбора: {day}")
        out.append(f"- Класс: **{crash_class}**")
        env = []
        if self.engine_build:
            env.append(f"xrCore build {self.engine_build}")
        if self.exe:
            env.append(self.exe)
        if env:
            out.append(f"- Среда: {', '.join(env)}")
        out.append("")

        if self.crashed and not hide_crash:
            out.append("## FATAL ERROR")
            out.append("")
            out.append("```")
            out.extend(self.fatal_lines[:40])
            out.append("```")
            out.append("")

            refs = self.lua_refs()
            if refs:
                out.append("## Кадры скриптов")
                out.append("")
                for i, ref in enumerate(refs[:15], 1):
                    out.append(f"{i}. `{ref}`")
                out.append("")

            if self.stack_lines:
                out.append("## Стек")
                out.append("")
                out.append("```")
                out.extend(self.stack_lines[:20])
                out.append("```")
                out.append("")

        mine_section = self.mine_markdown()
        if mine_section.strip():
            out.append(mine_section.rstrip())
            out.append("")

        shown_errors = self.nonfatal_errors[:MAX_NONFATAL_GROUPS]
        if shown_errors:
            out.append("## Нефатальные ошибки")
            out.append("")
            if len(self.nonfatal_errors) > MAX_NONFATAL_GROUPS:
                out.append(
                    f"Показаны {MAX_NONFATAL_GROUPS} из {len(self.nonfatal_errors)} групп."
                )
                out.append("")
            for i, group in enumerate(shown_errors, 1):
                culprit = group.culprit or "неизвестный скрипт"
                out.append(f"### {i}. `{culprit}` ×{group.count}")
                out.append("")
                if group.trigger:
                    out.append(f"Триггер: `{group.trigger[:200]}`")
                else:
                    out.append("Триггер: нет строки с `!` / `~` перед блоком")
                out.append("")
                if group.frames:
                    out.append("```")
                    out.extend(group.frames[:15])
                    out.append("```")
                    out.append("")

        out.append("## Куда смотреть")
        out.append("")
        for hint in hints:
            out.append(f"- {hint}")
        out.append("")

        if self.warnings and not errors_only:
            out.append(f"## Предупреждения (топ {max_warnings})")
            out.append("")
            for text, count in self.warnings.most_common(max_warnings):
                marker = f"x{count} " if count > 1 else ""
                out.append(f"- {marker}`{text[:200]}`")
            out.append("")

        if self.context:
            title = "Последние строки лога" if not self.crashed else "Строки перед падением"
            out.append(f"## {title} ({len(self.context)})")
            out.append("")
            out.append("```")
            out.extend(self.context)
            out.append("```")
            out.append("")

        out.append("---")
        out.append("")
        out.append(
            "Разбор ведём по `workflow-crash`: сначала класс и первопричина, "
            "фикс — только после подтверждения."
        )
        return "\n".join(out)


def unique_archive_path(
    dest_dir: Path,
    log_path: Path,
    analyzed_on: date | None = None,
) -> Path:
    """Имя карточки: YYYY-MM-DD_<stem>.md, при занятом имени — суффикс -2, -3, …"""
    source = Path(filename(log_path)).stem
    stem = f"{(analyzed_on or date.today()).isoformat()}_{source}"
    candidate = dest_dir / f"{stem}.md"
    if not candidate.exists():
        return candidate
    n = 2
    while True:
        candidate = dest_dir / f"{stem}-{n}.md"
        if not candidate.exists():
            return candidate
        n += 1


def write_archive(
    text: str,
    log_path: Path,
    dest_dir: Path,
    analyzed_on: date | None = None,
) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    path = unique_archive_path(dest_dir, log_path, analyzed_on)
    path.write_text(text + "\n", encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Карточка вылета из лога X-Ray/Anomaly")
    parser.add_argument("log", type=Path, help="путь к xray_*.log или тексту крэша")
    parser.add_argument("--out", type=Path, help="записать карточку в файл")
    parser.add_argument("--archive", action="store_true", help="записать карточку в logs/cards/")
    parser.add_argument(
        "--archive-dir",
        type=Path,
        default=None,
        help="каталог архива (по умолчанию logs/cards/)",
    )
    parser.add_argument("--context", type=int, default=40, help="строк контекста перед падением")
    parser.add_argument("--max-warnings", type=int, default=15, help="сколько предупреждений показать")
    parser.add_argument("--warnings-only", action="store_true", help="без блока вылета")
    parser.add_argument("--errors-only", action="store_true", help="только нефатальные ошибки, без вылета и предупреждений")
    parser.add_argument("--mine", action="store_true", help="только секция «Мои моды»")
    parser.add_argument(
        "--addon-dir",
        type=Path,
        default=None,
        help="каталог addon/ для секции «Мои моды» (по умолчанию addon/)",
    )
    parser.add_argument("--json", action="store_true", help="машиночитаемый вывод")
    args = parser.parse_args(argv)

    if not args.log.exists():
        print(f"Файл не найден: {args.log}", file=sys.stderr)
        return 2

    if args.mine and args.json:
        print("укажите либо --mine, либо --json, не оба", file=sys.stderr)
        return 2

    report = LogReport(args.log, addon_dir=args.addon_dir)
    report.parse(context_lines=max(5, args.context))
    analyzed_on = date.today()

    if args.json:
        text = json.dumps(report.to_dict(args.max_warnings), ensure_ascii=False, indent=2)
    else:
        text = report.to_markdown(
            args.max_warnings,
            args.warnings_only,
            args.errors_only,
            analyzed_on=analyzed_on,
            mine_only=args.mine,
        )

    if args.archive:
        dest_dir = args.archive_dir if args.archive_dir is not None else DEFAULT_ARCHIVE_DIR
        card_md = report.to_markdown(
            args.max_warnings,
            args.warnings_only,
            args.errors_only,
            analyzed_on=analyzed_on,
            mine_only=args.mine,
        )
        archive_path = write_archive(card_md, args.log, dest_dir, analyzed_on)
        sink = sys.stderr if args.json else sys.stdout
        print(rel(archive_path), file=sink)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"Карточка записана: {rel(args.out)}")
    elif not args.archive or args.json:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
