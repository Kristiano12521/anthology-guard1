#!/usr/bin/env python3
"""Распаковка архивов X-Ray / Anomaly (.db / .dbN / .xdb).

TOC — chunk id 1, при флаге CFS_COMPRESS сжат LZHUF. Полезные данные файлов
лежат по абсолютному смещению `ptr` в файле архива: без сжатия, если
size_real == size_compr, иначе LZO1X без фрейма (как rtc_decompress).

Anomaly на диске почти всегда `name.db0`, `name.db1`, … — суффикс `.dbN`,
не `.db`. Реже встречаются `.db` и `.xdb`. Формат один.

    python3 tools/xdb_unpack.py path/to/scripts.db0 --list
    python3 tools/xdb_unpack.py path/to/scripts.db0 --out unpacked/
    python3 tools/xdb_unpack.py path/to/scripts.db0 --out unpacked/ --filter scripts/
"""

from __future__ import annotations

import argparse
import struct
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import rel  # noqa: E402

N = 4096
F = 60
THRESHOLD = 2
N_CHAR = 256 - THRESHOLD + F
T = N_CHAR * 2 - 1
R = T - 1
MAX_FREQ = 0x4000
CFS_COMPRESS = 1 << 31

D_CODE = bytes([
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
    0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02,
    0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,
    0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09,
    0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B,
    0x0C, 0x0C, 0x0C, 0x0C, 0x0D, 0x0D, 0x0D, 0x0D, 0x0E, 0x0E, 0x0E, 0x0E, 0x0F, 0x0F, 0x0F, 0x0F,
    0x10, 0x10, 0x10, 0x10, 0x11, 0x11, 0x11, 0x11, 0x12, 0x12, 0x12, 0x12, 0x13, 0x13, 0x13, 0x13,
    0x14, 0x14, 0x14, 0x14, 0x15, 0x15, 0x15, 0x15, 0x16, 0x16, 0x16, 0x16, 0x17, 0x17, 0x17, 0x17,
    0x18, 0x18, 0x19, 0x19, 0x1A, 0x1A, 0x1B, 0x1B, 0x1C, 0x1C, 0x1D, 0x1D, 0x1E, 0x1E, 0x1F, 0x1F,
    0x20, 0x20, 0x21, 0x21, 0x22, 0x22, 0x23, 0x23, 0x24, 0x24, 0x25, 0x25, 0x26, 0x26, 0x27, 0x27,
    0x28, 0x28, 0x29, 0x29, 0x2A, 0x2A, 0x2B, 0x2B, 0x2C, 0x2C, 0x2D, 0x2D, 0x2E, 0x2E, 0x2F, 0x2F,
    0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F,
])
D_LEN = bytes([
    0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,
    0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,
    0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04,
    0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04,
    0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04,
    0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
    0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
    0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
    0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08,
])


class LzHufDecoder:
    def __init__(self, src: bytes):
        self.src = src
        self.ip = 0
        self.getbuf = 0
        self.getlen = 0
        self.freq = [0] * (T + 1)
        self.prnt = [0] * (T + N_CHAR + 1)
        self.son = [0] * T
        self.text_buf = bytearray(N + F)

    def _getb(self) -> int:
        if self.ip >= len(self.src):
            return -1
        b = self.src[self.ip]
        self.ip += 1
        return b

    def get_bit(self) -> int:
        while self.getlen <= 8:
            i = self._getb()
            if i < 0:
                i = 0
            self.getbuf |= i << (8 - self.getlen)
            self.getlen += 8
        i = self.getbuf
        self.getbuf = (self.getbuf << 1) & 0xFFFFFFFF
        self.getlen -= 1
        return (i & 0x8000) >> 15

    def get_byte(self) -> int:
        while self.getlen <= 8:
            i = self._getb()
            if i < 0:
                i = 0
            self.getbuf |= i << (8 - self.getlen)
            self.getlen += 8
        i = self.getbuf
        self.getbuf = (self.getbuf << 8) & 0xFFFFFFFF
        self.getlen -= 8
        return (i & 0xFF00) >> 8

    def start_huff(self) -> None:
        for i in range(N_CHAR):
            self.freq[i] = 1
            self.son[i] = i + T
            self.prnt[i + T] = i
        i = 0
        j = N_CHAR
        while j <= R:
            self.freq[j] = self.freq[i] + self.freq[i + 1]
            self.son[j] = i
            self.prnt[i] = j
            self.prnt[i + 1] = j
            i += 2
            j += 1
        self.freq[T] = 0xFFFF
        self.prnt[R] = 0

    def reconst(self) -> None:
        j = 0
        for i in range(T):
            if self.son[i] >= T:
                self.freq[j] = (self.freq[i] + 1) // 2
                self.son[j] = self.son[i]
                j += 1
        i = 0
        j = N_CHAR
        while j < T:
            k = i + 1
            f = self.freq[i] + self.freq[k]
            self.freq[j] = f
            k = j - 1
            while f < self.freq[k]:
                k -= 1
            k += 1
            l = j - k
            self.freq[k + 1 : k + 1 + l] = self.freq[k : k + l]
            self.freq[k] = f
            self.son[k + 1 : k + 1 + l] = self.son[k : k + l]
            self.son[k] = i
            i += 2
            j += 1
        for i in range(T):
            k = self.son[i]
            if k >= T:
                self.prnt[k] = i
            else:
                self.prnt[k] = i
                self.prnt[k + 1] = i

    def update(self, c: int) -> None:
        if self.freq[R] == MAX_FREQ:
            self.reconst()
        c = self.prnt[c + T]
        while True:
            k = self.freq[c] + 1
            self.freq[c] = k
            l = c + 1
            if k > self.freq[l]:
                while k > self.freq[l + 1]:
                    l += 1
                # C does ++l in the while then l-- after; equivalent: advance while next is still < k
                # Original:
                # if (k > freq[l = c + 1]) {
                #   while (k > freq[++l]);
                #   l--;
                # }
                # So l starts at c+1, if k > freq[c+1], do ++l until k <= freq[l], then l--.
                l = c + 1
                if k > self.freq[l]:
                    l += 1
                    while k > self.freq[l]:
                        l += 1
                    l -= 1
                    self.freq[c] = self.freq[l]
                    self.freq[l] = k
                    i = self.son[c]
                    self.prnt[i] = l
                    if i < T:
                        self.prnt[i + 1] = l
                    jn = self.son[l]
                    self.son[l] = i
                    self.prnt[jn] = c
                    if jn < T:
                        self.prnt[jn + 1] = c
                    self.son[c] = jn
                    c = l
            c = self.prnt[c]
            if c == 0:
                break

    def decode_char(self) -> int:
        c = self.son[R]
        while c < T:
            c += self.get_bit()
            c = self.son[c]
        c -= T
        self.update(c)
        return c

    def decode_position(self) -> int:
        i = self.get_byte()
        c = D_CODE[i] << 6
        j = D_LEN[i] - 2
        while j > 0:
            i = (i << 1) + self.get_bit()
            j -= 1
        return c | (i & 0x3F)

    def decode(self) -> bytes:
        textsize = self._getb()
        textsize |= self._getb() << 8
        textsize |= self._getb() << 16
        textsize |= self._getb() << 24
        if textsize <= 0:
            raise ValueError("lzhuf empty")
        out = bytearray(textsize)
        self.start_huff()
        for i in range(N - F):
            self.text_buf[i] = 0x20
        r = N - F
        count = 0
        while count < textsize:
            c = self.decode_char()
            if c < 256:
                out[count] = c
                self.text_buf[r] = c
                r = (r + 1) & (N - 1)
                count += 1
            else:
                i = (r - self.decode_position() - 1) & (N - 1)
                j = c - 255 + THRESHOLD
                for k in range(j):
                    ch = self.text_buf[(i + k) & (N - 1)]
                    out[count] = ch
                    self.text_buf[r] = ch
                    r = (r + 1) & (N - 1)
                    count += 1
                    if count >= textsize:
                        break
        return bytes(out)


def skip_kind(message: str) -> str:
    """Класс ошибки для сводки: без пофайловых чисел и имён."""
    if message.startswith("lzo bad distance"):
        return "lzo bad distance"
    if message.startswith("короткое чтение"):
        return "короткое чтение"
    return message


def format_skip_summary(kinds: list[str]) -> str | None:
    """Одна строка «пропущено N: причина (k), …» или None, если пропусков нет."""
    if not kinds:
        return None
    counts = Counter(kinds)
    parts = [f"{kind} ({n})" for kind, n in counts.most_common()]
    return f"пропущено {len(kinds)}: {', '.join(parts)}"


def lzo1x_decompress(src: bytes, dst_len: int) -> bytes:
    """Сырой LZO1X без фрейма, как minilzo ``lzo1x_decompress`` / X-Ray ``rtc_decompress``.

    Кодирование сверено с:
    - Linux ``Documentation/lzo.txt`` (stream format as understood by the kernel);
    - ``lib/lzo/lzo1x_decompress_safe.c`` (в т.ч. ``m_pos -= 0x4000`` у M4);
    - minilzo Oberhumer (``first_literal_run``, ``match_next``, copy_match побайтно);
    - lzokay (тот же текст Documentation/lzo.txt, читаемый state-machine).
    """
    ip = 0
    n = len(src)
    dst = bytearray()

    def u8() -> int:
        nonlocal ip
        if ip >= n:
            raise ValueError("lzo truncated")
        b = src[ip]
        ip += 1
        return b

    def copy_literal(cnt: int) -> None:
        nonlocal ip
        if cnt < 0 or ip + cnt > n:
            raise ValueError("lzo truncated")
        dst.extend(src[ip : ip + cnt])
        ip += cnt

    def extra_when_zero(add: int) -> int:
        extra = 0
        while True:
            b = u8()
            if b:
                return extra + b + add
            extra += 255

    def copy_match(distance: int, length: int) -> None:
        # Перекрытие (dist < length) — только побайтно, не срезом: каждый
        # новый байт может ссылаться на только что записанный.
        if distance <= 0 or distance > len(dst):
            raise ValueError(f"lzo bad distance {distance} dst={len(dst)}")
        for _ in range(length):
            dst.append(dst[-distance])

    if n < 3:
        raise ValueError("lzo truncated")

    state = 0
    first = src[0]
    if first > 17:
        ip = 1
        taken = first - 17
        copy_literal(taken)
        state = 4 if taken >= 4 else taken

    while True:
        inst = u8()
        if inst >= 64:
            # M2: 01L DDDSS (64..127) длина 3–4; 1LL DDDSS (128..255) длина 5–8.
            # Один байт H, не два: прежний декодер читал H дважды и срывал поток.
            length = (inst >> 5) + 1
            h = u8()
            distance = (h << 3) + ((inst >> 2) & 7) + 1
            state = inst & 3
            copy_match(distance, length)
        elif inst >= 32:
            # M3: 001LLLLL, длина 2+(L ?: 31 + 255*нулей + байт), dist = D+1.
            length = (inst & 31) + 2
            if length == 2:
                length += extra_when_zero(31)
            le16 = u8() | (u8() << 8)
            state = le16 & 3
            copy_match((le16 >> 2) + 1, length)
        elif inst >= 16:
            # M4: 0001HLLL. Компрессор пишет m_off -= 0x4000; декодер возвращает
            # bias: distance = 16384 + (H<<14) + D. EOS, если (H<<14)+D == 0.
            length = (inst & 7) + 2
            if length == 2:
                length += extra_when_zero(7)
            le16 = u8() | (u8() << 8)
            state = le16 & 3
            d = le16 >> 2
            high = (inst & 8) << 11
            if high + d == 0:
                if length != 3:
                    raise ValueError("lzo bad eos")
                break
            copy_match(16384 + high + d, length)
        elif state == 0:
            length = inst + 3
            if length == 3:
                length += extra_when_zero(15)
            copy_literal(length)
            state = 4
            if len(dst) > dst_len:
                raise ValueError("lzo overflow")
            continue
        elif state != 4:
            # M1, после 1–3 литералов: 2 байта с дистанции 1..1k.
            h = u8()
            distance = (h << 2) + (inst >> 2) + 1
            state = inst & 3
            copy_match(distance, 2)
        else:
            # M1 после 4+ литералов (first_literal_run): 3 байта с 2049..3072.
            h = u8()
            distance = (h << 2) + (inst >> 2) + 2049
            state = inst & 3
            copy_match(distance, 3)

        if state:
            copy_literal(state)
        if len(dst) > dst_len:
            raise ValueError("lzo overflow")

    if len(dst) != dst_len:
        raise ValueError(f"lzo size {len(dst)} != {dst_len}")
    return bytes(dst)


@dataclass(frozen=True)
class TocEntry:
    name: str
    ptr: int
    size_real: int
    size_compr: int
    crc: int

    @property
    def is_dir(self) -> bool:
        return self.size_real == 0 and self.size_compr == 0

    @property
    def posix_name(self) -> str:
        return self.name.replace("\\", "/")


def iter_chunks(data: bytes):
    """Режет буфер на чанки. Для маленьких архивов и тестов; большие лучше читать с диска."""
    off = 0
    while off + 8 <= len(data):
        cid, size = struct.unpack_from("<II", data, off)
        off += 8
        payload = data[off : off + size]
        off += size
        yield cid, payload


def parse_toc(toc: bytes) -> list[TocEntry]:
    entries: list[TocEntry] = []
    pos = 0
    while pos + 2 <= len(toc):
        (entry_size,) = struct.unpack_from("<H", toc, pos)
        pos += 2
        if entry_size < 16 or pos + entry_size > len(toc):
            break
        blob = toc[pos : pos + entry_size]
        pos += entry_size
        size_real, size_compr, crc = struct.unpack_from("<III", blob, 0)
        name_len = entry_size - 16
        name = blob[12 : 12 + name_len].split(b"\x00", 1)[0].decode("latin1")
        ptr = struct.unpack_from("<I", blob, 12 + name_len)[0]
        entries.append(TocEntry(name, ptr, size_real, size_compr, crc))
    return entries


def is_db_archive(path: Path) -> bool:
    """Anomaly: `.db0`/`.db1`/… ; реже `.db` и `.xdb`."""
    if not path.is_file():
        return False
    suffix = path.suffix.lower()
    if suffix in {".db", ".xdb"}:
        return True
    return suffix.startswith(".db") and suffix[3:].isdigit()


def find_archives(root: Path) -> list[Path]:
    """Все .db/.dbN/.xdb под root, стабильный порядок."""
    found = [path for path in root.rglob("*") if is_db_archive(path)]
    return sorted(found)


def _decode_toc_payload(payload: bytes, compressed: bool) -> bytes:
    if compressed:
        return LzHufDecoder(payload).decode()
    return payload


def read_toc_bytes(data: bytes) -> list[TocEntry]:
    """TOC из уже прочитанного архива. Chunk id 1, опционально LZHUF."""
    toc_payload = None
    compressed = False
    for cid, payload in iter_chunks(data):
        if (cid & ~CFS_COMPRESS) == 1:
            toc_payload = payload
            compressed = bool(cid & CFS_COMPRESS)
            break
    if toc_payload is None:
        raise ValueError("нет chunk 1 (TOC)")
    return parse_toc(_decode_toc_payload(toc_payload, compressed))


def read_toc(path: Path) -> list[TocEntry]:
    """Читает только заголовки чанков и payload TOC — не грузит весь архив в память."""
    with path.open("rb") as handle:
        handle.seek(0, 2)
        end = handle.tell()
        off = 0
        toc_payload = None
        compressed = False
        while off + 8 <= end:
            handle.seek(off)
            header = handle.read(8)
            if len(header) < 8:
                break
            cid, size = struct.unpack("<II", header)
            if (cid & ~CFS_COMPRESS) == 1:
                toc_payload = handle.read(size)
                compressed = bool(cid & CFS_COMPRESS)
                break
            off += 8 + size
    if toc_payload is None:
        raise ValueError(f"нет chunk 1 (TOC): {path}")
    return parse_toc(_decode_toc_payload(toc_payload, compressed))


def read_entry(path: Path, entry: TocEntry) -> bytes:
    """Читает один файл по ptr. Каталоги (size 0) дают b''."""
    if entry.is_dir or entry.size_compr <= 0:
        return b""
    with path.open("rb") as handle:
        handle.seek(entry.ptr)
        blob = handle.read(entry.size_compr)
    if len(blob) != entry.size_compr:
        raise ValueError(
            f"короткое чтение {entry.name}: {len(blob)} из {entry.size_compr}"
        )
    if entry.size_real == entry.size_compr:
        raw = blob
    else:
        raw = lzo1x_decompress(blob, entry.size_real)
    if len(raw) >= entry.size_real:
        return raw[: entry.size_real]
    return raw


def _entry_matches(entry: TocEntry, needle: str | None) -> bool:
    if entry.is_dir:
        return False
    if not needle:
        return True
    return needle.lower() in entry.posix_name.lower()


def unpack_archive(
    archive: Path,
    dest: Path | None = None,
    needle: str | None = None,
    *,
    list_only: bool = False,
) -> int:
    """Распаковать архив или только перечислить. Возвращает число файлов (записей)."""
    entries = read_toc(archive)
    chosen = [entry for entry in entries if _entry_matches(entry, needle)]
    if list_only or dest is None:
        for entry in chosen:
            print(f"{entry.size_real:8}  {entry.posix_name}")
        print(f"записей: {len(chosen)} (всего в TOC: {len(entries)})")
        return len(chosen)

    dest.mkdir(parents=True, exist_ok=True)
    written = 0
    skips: list[str] = []
    for entry in chosen:
        try:
            raw = read_entry(archive, entry)
        except (ValueError, OSError) as exc:
            print(f"пропуск {entry.posix_name}: {exc}", file=sys.stderr)
            skips.append(skip_kind(str(exc)))
            continue
        out = dest / entry.posix_name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(raw)
        written += 1
    print(f"записано {written} -> {rel(dest)}")
    summary = format_skip_summary(skips)
    if summary:
        print(summary)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Распаковка .db/.dbN/.xdb архивов Anomaly (LZHUF TOC, LZO1X payload)"
    )
    parser.add_argument("archive", type=Path, help="файл архива")
    parser.add_argument("--out", type=Path, help="куда писать файлы")
    parser.add_argument("--list", action="store_true", help="только TOC, ничего не писать")
    parser.add_argument(
        "--filter",
        dest="needle",
        help="подстрока пути (без учёта регистра), иначе все файлы",
    )
    args = parser.parse_args(argv)

    archive = args.archive
    if not archive.is_file():
        print(f"нет файла: {archive}", file=sys.stderr)
        return 2
    try:
        unpack_archive(
            archive,
            dest=None if args.list else args.out,
            needle=args.needle,
            list_only=args.list or args.out is None,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
