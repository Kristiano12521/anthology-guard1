"""Общие мелочи для инструментов проекта. Только стандартная библиотека."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, Iterator

REPO_ROOT = Path(__file__).resolve().parent.parent

GAME_TEXT_SUFFIXES = {".script", ".lua", ".ltx", ".xml", ".seq"}

SKIP_DIRS = {".git", ".cache", "__pycache__", "node_modules", ".idea", ".vs"}


def read_text(path: Path) -> str:
    """Читает игровой или лог-файл, не падая на кодировке.

    Игровые файлы в Windows-1251, логи бывают смешанными. Порядок попыток
    подобран так, чтобы cp1251 не молча портил валидный UTF-8.
    """
    data = path.read_bytes()
    return decode_bytes(data)


def decode_bytes(data: bytes) -> str:
    if data.startswith(b"\xef\xbb\xbf"):
        return data[3:].decode("utf-8", errors="replace")
    for encoding in ("utf-8", "cp1251"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("cp1251", errors="replace")


def looks_like_utf8_cyrillic(data: bytes) -> bool:
    """True, если файл похож на UTF-8 с кириллицей (для игровых файлов это ошибка)."""
    if data.startswith(b"\xef\xbb\xbf"):
        return True
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return any("\u0400" <= ch <= "\u04ff" for ch in text)


def iter_files(root: Path, suffixes: Iterable[str] | None = None) -> Iterator[Path]:
    """Обходит дерево, пропуская служебные каталоги."""
    wanted = {s.lower() for s in suffixes} if suffixes else None
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            path = Path(dirpath) / name
            if wanted is None or path.suffix.lower() in wanted:
                yield path


def filename(path: Path | str) -> str:
    """Последний компонент пути. Режет и ``/``, и ``\\``.

    pathlib и ``os.path.basename`` на POSIX не считают обратный слэш
    разделителем: ``C:\\Users\\me\\xray.log`` целиком оказывается в ``.name``.
    """
    text = os.fspath(path).replace("\\", "/")
    return text.rsplit("/", 1)[-1]


def rel(path: Path, base: Path | None = None) -> str:
    """Путь для вывода: относительный от корня репозитория, со слэшами."""
    base = base or REPO_ROOT
    try:
        return path.resolve().relative_to(base.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def path_tail(path: Path) -> str:
    """Путь внутри gamedata: 'scripts/foo.script', 'configs/items/bar.ltx'.

    Нужен, чтобы сопоставлять файлы аддона с файлами reference/ независимо от
    того, как именно распакована сборка.
    """
    parts = [p.lower() for p in path.parts]
    for anchor in ("scripts", "configs", "textures", "meshes", "shaders", "anims", "sounds"):
        if anchor in parts:
            idx = len(parts) - 1 - parts[::-1].index(anchor)
            return "/".join(path.parts[idx:])
    return path.name
