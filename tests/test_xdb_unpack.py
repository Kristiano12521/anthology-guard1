from __future__ import annotations

import contextlib
import io
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


def build_archive(files: dict[str, tuple[bytes, int] | bytes]) -> bytes:
    """Архив: значение — байты (несжатые) или (stored, size_real) для LZO-слота."""
    payload = b""
    toc = b""
    for name, spec in files.items():
        if isinstance(spec, tuple):
            stored, size_real = spec
        else:
            stored, size_real = spec, len(spec)
        ptr = 8 + len(payload)
        payload += stored
        toc += pack_toc_entry(name, ptr, size_real, len(stored))
    chunk0 = struct.pack("<II", 0, len(payload)) + payload
    chunk1 = struct.pack("<II", 1, len(toc)) + toc
    return chunk0 + chunk1


def build_uncompressed_archive(files: dict[str, bytes]) -> bytes:
    """Минимальный архив: chunk 0 = payload, chunk 1 = несжатый TOC."""
    return build_archive(files)


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


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "xdb"
EOS = bytes([0x11, 0x00, 0x00])


class Lzo1xTests(unittest.TestCase):
    def test_archive_fixture_decompresses_to_ltx(self):
        compressed = (FIXTURES / "mod_system_base_hud.lzo").read_bytes()
        expected = (FIXTURES / "mod_system_base_hud.ltx").read_bytes()
        raw = xdb_unpack.lzo1x_decompress(compressed, len(expected))
        self.assertEqual(raw, expected)
        text = raw.decode("cp1251")
        self.assertIn("[hud_base]", text)
        self.assertIn("base_hud_offset_pos", text)

    def test_overlapping_match_is_bytewise(self):
        # литерал 'a' + M2 длина 3, дистанция 1 → «aaaa». Срез dst[-1:2] дал бы 1 байт.
        src = bytes([18, ord("a"), 0x40, 0x00]) + EOS
        self.assertEqual(xdb_unpack.lzo1x_decompress(src, 4), b"aaaa")

    def test_first_literal_state_then_m1(self):
        # первый байт 18: один литерал, state=1; 0x00 — M1 на 2 байта с дистанции 1.
        src = bytes([18, ord("a"), 0x00, 0x00]) + EOS
        self.assertEqual(xdb_unpack.lzo1x_decompress(src, 3), b"aaa")

    def test_m3_length_extended_by_zero_bytes(self):
        # M3 с L=0: один нулевой байт длины + 0x01 → 289 байт с дистанции 1.
        src = bytes([18, ord("a"), 0x20, 0x00, 0x01, 0x00, 0x00]) + EOS
        raw = xdb_unpack.lzo1x_decompress(src, 290)
        self.assertEqual(raw, b"a" * 290)


class SkipSummaryTests(unittest.TestCase):
    def test_format_empty_is_none(self):
        self.assertIsNone(xdb_unpack.format_skip_summary([]))

    def test_groups_by_kind_not_per_file(self):
        kinds = [
            xdb_unpack.skip_kind("lzo bad distance 260 dst=100 inst=111"),
            xdb_unpack.skip_kind("lzo bad distance 877 dst=105 inst=114"),
            xdb_unpack.skip_kind("lzo truncated"),
        ]
        line = xdb_unpack.format_skip_summary(kinds)
        self.assertEqual(line, "пропущено 3: lzo bad distance (2), lzo truncated (1)")

    def test_unpack_prints_summary_and_keeps_per_file_skip(self):
        garbage = bytes([18]) + b"x"  # литерал, дальше обрыв
        blob = build_archive(
            {
                "a.ltx": (garbage, 40),
                "b.ltx": (garbage, 40),
                "ok.ltx": b"[ok]\n",
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "pack.db0"
            dest = root / "out"
            archive.write_bytes(blob)
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                written = xdb_unpack.unpack_archive(archive, dest)
            self.assertEqual(written, 1)
            self.assertTrue((dest / "ok.ltx").exists())
            err = stderr.getvalue()
            self.assertIn("пропуск a.ltx", err)
            self.assertIn("пропуск b.ltx", err)
            self.assertIn("пропущено 2: lzo truncated (2)", stdout.getvalue())

    def test_unpack_omits_summary_when_nothing_skipped(self):
        blob = build_uncompressed_archive({"ok.ltx": b"[ok]\n"})
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "pack.db0"
            dest = root / "out"
            archive.write_bytes(blob)
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
                xdb_unpack.unpack_archive(archive, dest)
            self.assertNotIn("пропущено", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
