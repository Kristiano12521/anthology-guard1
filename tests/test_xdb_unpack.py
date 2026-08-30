import struct
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import xdb_unpack  # noqa: E402


def pack_toc_entry(name: str, ptr: int, size_real: int, size_compr: int, crc: int = 0) -> bytes:
    name_bytes = name.encode("latin1") + b"\x00"
    blob = struct.pack("<III", size_real, size_compr, crc) + name_bytes + struct.pack("<I", ptr)
    return struct.pack("<H", len(blob)) + blob


def build_uncompressed_archive(files: dict[str, bytes]) -> bytes:
    """Минимальный архив: chunk 0 = payload, chunk 1 = несжатый TOC."""
    payload = b""
    toc = b""
    for name, content in files.items():
        ptr = 8 + len(payload)
        payload += content
        toc += pack_toc_entry(name, ptr, len(content), len(content))
    chunk0 = struct.pack("<II", 0, len(payload)) + payload
    chunk1 = struct.pack("<II", 1, len(toc)) + toc
    return chunk0 + chunk1


class ParseTocTests(unittest.TestCase):
    def test_parses_name_ptr_and_sizes(self):
        toc = pack_toc_entry("scripts\\foo.script", ptr=171, size_real=12, size_compr=12, crc=9)
        entries = xdb_unpack.parse_toc(toc)
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry.name, "scripts\\foo.script")
        self.assertEqual(entry.posix_name, "scripts/foo.script")
        self.assertEqual(entry.ptr, 171)
        self.assertEqual(entry.size_real, 12)
        self.assertEqual(entry.size_compr, 12)
        self.assertEqual(entry.crc, 9)
        self.assertFalse(entry.is_dir)

    def test_directory_entry_is_dir(self):
        toc = pack_toc_entry("scripts\\", ptr=0, size_real=0, size_compr=0)
        entry = xdb_unpack.parse_toc(toc)[0]
        self.assertTrue(entry.is_dir)

    def test_multiple_entries(self):
        toc = pack_toc_entry("a.ltx", 1, 2, 2) + pack_toc_entry("b.ltx", 3, 4, 4)
        names = [e.name for e in xdb_unpack.parse_toc(toc)]
        self.assertEqual(names, ["a.ltx", "b.ltx"])


class ArchiveKindTests(unittest.TestCase):
    def test_db_suffixes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db0 = root / "scripts.db0"
            xdb = root / "pack.xdb"
            plain = root / "pack.db"
            txt = root / "readme.txt"
            db0.write_bytes(b"x")
            xdb.write_bytes(b"x")
            plain.write_bytes(b"x")
            txt.write_bytes(b"x")
            self.assertTrue(xdb_unpack.is_db_archive(db0))
            self.assertTrue(xdb_unpack.is_db_archive(xdb))
            self.assertTrue(xdb_unpack.is_db_archive(plain))
            self.assertFalse(xdb_unpack.is_db_archive(txt))
            self.assertFalse(xdb_unpack.is_db_archive(root / "missing.db0"))

    def test_find_archives_nested_sorted(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "db"
            (db / "configs").mkdir(parents=True)
            (db / "textures").mkdir()
            first = db / "configs" / "ai.db0"
            second = db / "textures" / "textures.db1"
            extra = db / "note.txt"
            first.write_bytes(b"a")
            second.write_bytes(b"b")
            extra.write_bytes(b"c")
            found = [p.relative_to(db).as_posix() for p in xdb_unpack.find_archives(db)]
            self.assertEqual(found, ["configs/ai.db0", "textures/textures.db1"])


class RoundTripTests(unittest.TestCase):
    def test_read_toc_and_payload_without_lzo(self):
        body = b"hello script"
        blob = build_uncompressed_archive({"scripts\\foo.script": body})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scripts.db0"
            path.write_bytes(blob)
            entries = xdb_unpack.read_toc(path)
            self.assertEqual(len(entries), 1)
            self.assertEqual(xdb_unpack.read_entry(path, entries[0]), body)


if __name__ == "__main__":
    unittest.main()
