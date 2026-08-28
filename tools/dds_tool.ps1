# DDS <-> PNG helper for UI icons (DXT1/DXT5 and uncompressed A8R8G8B8).
#
# Usage:
#   powershell -File tools/dds_tool.ps1 decode <in.dds> <out.png> [-Background 0xFF202020]
#   powershell -File tools/dds_tool.ps1 encode <in.png> <out.dds>   # writes 4x4-block DXT5, no mips
#
# Written for this repo because no Python interpreter is available on the
# machine; the game's UI icons are DXT5 64x64 with a single mip level.

param(
  [Parameter(Mandatory = $true)][ValidateSet('decode', 'encode')][string]$Mode,
  [Parameter(Mandatory = $true)][string]$InPath,
  [Parameter(Mandatory = $true)][string]$OutPath,
  [string]$Background = '0xFF141414'
)

Add-Type -AssemblyName System.Drawing

Add-Type -TypeDefinition @'
using System;
using System.IO;

public static class Dds {
  const int HEADER = 128;

  static void Color565(ushort c, out int r, out int g, out int b) {
    r = ((c >> 11) & 0x1F) * 255 / 31;
    g = ((c >> 5)  & 0x3F) * 255 / 63;
    b = ( c        & 0x1F) * 255 / 31;
  }

  public static int[] Decode(byte[] dds, out int width, out int height) {
    height = BitConverter.ToInt32(dds, 12);
    width  = BitConverter.ToInt32(dds, 16);
    int pfFlags = BitConverter.ToInt32(dds, 80);
    string fourcc = System.Text.Encoding.ASCII.GetString(dds, 84, 4);
    int[] px = new int[width * height];

    if ((pfFlags & 0x4) == 0) {
      int rgbBits = BitConverter.ToInt32(dds, 88);
      if (rgbBits != 32) throw new Exception("only 32bpp uncompressed supported, got " + rgbBits);
      for (int i = 0; i < width * height; i++) px[i] = BitConverter.ToInt32(dds, HEADER + i * 4);
      return px;
    }

    bool dxt5 = fourcc == "DXT5";
    bool dxt1 = fourcc == "DXT1";
    if (!dxt5 && !dxt1) throw new Exception("unsupported fourcc " + fourcc);

    int blockBytes = dxt5 ? 16 : 8;
    int off = HEADER;
    for (int by = 0; by < height; by += 4) {
      for (int bx = 0; bx < width; bx += 4) {
        byte[] alpha = new byte[16];
        int cOff = off;
        if (dxt5) {
          int a0 = dds[off], a1 = dds[off + 1];
          ulong bits = 0;
          for (int i = 0; i < 6; i++) bits |= (ulong)dds[off + 2 + i] << (8 * i);
          int[] tbl = new int[8];
          tbl[0] = a0; tbl[1] = a1;
          if (a0 > a1) { for (int i = 1; i <= 5; i++) tbl[i + 1] = ((6 - i) * a0 + i * a1) / 7; }
          else { for (int i = 1; i <= 3; i++) tbl[i + 1] = ((4 - i) * a0 + i * a1) / 5; tbl[6] = 0; tbl[7] = 255; }
          for (int i = 0; i < 16; i++) alpha[i] = (byte)tbl[(int)((bits >> (3 * i)) & 0x7)];
          cOff = off + 8;
        } else {
          for (int i = 0; i < 16; i++) alpha[i] = 255;
        }

        ushort c0 = BitConverter.ToUInt16(dds, cOff);
        ushort c1 = BitConverter.ToUInt16(dds, cOff + 2);
        uint idx = BitConverter.ToUInt32(dds, cOff + 4);
        int[] r = new int[4], g = new int[4], b = new int[4];
        Color565(c0, out r[0], out g[0], out b[0]);
        Color565(c1, out r[1], out g[1], out b[1]);
        if (c0 > c1 || dxt5) {
          r[2] = (2 * r[0] + r[1]) / 3; g[2] = (2 * g[0] + g[1]) / 3; b[2] = (2 * b[0] + b[1]) / 3;
          r[3] = (r[0] + 2 * r[1]) / 3; g[3] = (g[0] + 2 * g[1]) / 3; b[3] = (b[0] + 2 * b[1]) / 3;
        } else {
          r[2] = (r[0] + r[1]) / 2; g[2] = (g[0] + g[1]) / 2; b[2] = (b[0] + b[1]) / 2;
          r[3] = 0; g[3] = 0; b[3] = 0;
        }

        for (int py = 0; py < 4; py++) {
          for (int pxi = 0; pxi < 4; pxi++) {
            int x = bx + pxi, y = by + py;
            if (x >= width || y >= height) continue;
            int i = py * 4 + pxi;
            int ci = (int)((idx >> (2 * i)) & 0x3);
            px[y * width + x] = (alpha[i] << 24) | (r[ci] << 16) | (g[ci] << 8) | b[ci];
          }
        }
        off += blockBytes;
      }
    }
    return px;
  }

  static void WriteHeader(BinaryWriter w, int width, int height, int dataSize) {
    w.Write(new byte[] { 0x44, 0x44, 0x53, 0x20 });      // "DDS "
    w.Write(124);                                         // dwSize
    w.Write(0x1 | 0x2 | 0x4 | 0x1000 | 0x80000);          // CAPS|HEIGHT|WIDTH|PIXELFORMAT|LINEARSIZE
    w.Write(height);
    w.Write(width);
    w.Write(dataSize);                                    // dwPitchOrLinearSize
    w.Write(0);                                           // depth
    w.Write(1);                                           // mipMapCount
    for (int i = 0; i < 11; i++) w.Write(0);              // reserved
    w.Write(32);                                          // pf size
    w.Write(0x4);                                         // DDPF_FOURCC
    w.Write(new byte[] { 0x44, 0x58, 0x54, 0x35 });        // "DXT5"
    for (int i = 0; i < 5; i++) w.Write(0);               // bit counts/masks
    w.Write(0x1000);                                      // caps: TEXTURE
    w.Write(0); w.Write(0); w.Write(0); w.Write(0);
  }

  static ushort To565(int r, int g, int b) {
    return (ushort)(((r * 31 / 255) << 11) | ((g * 63 / 255) << 5) | (b * 31 / 255));
  }

  public static void Encode(int[] px, int width, int height, string path) {
    using (var fs = File.Create(path))
    using (var w = new BinaryWriter(fs)) {
      int blocks = (width / 4) * (height / 4);
      WriteHeader(w, width, height, blocks * 16);

      for (int by = 0; by < height; by += 4) {
        for (int bx = 0; bx < width; bx += 4) {
          byte[] a = new byte[16];
          int[] rr = new int[16], gg = new int[16], bb = new int[16];
          for (int py = 0; py < 4; py++) {
            for (int pxi = 0; pxi < 4; pxi++) {
              int i = py * 4 + pxi;
              int p = px[(by + py) * width + bx + pxi];
              a[i] = (byte)((p >> 24) & 0xFF);
              rr[i] = (p >> 16) & 0xFF; gg[i] = (p >> 8) & 0xFF; bb[i] = p & 0xFF;
            }
          }

          // BC3 alpha: two endpoints plus six interpolated steps.
          byte amax = 0, amin = 255;
          foreach (byte v in a) { if (v > amax) amax = v; if (v < amin) amin = v; }
          byte a0 = amax, a1 = amin;
          int[] tbl = new int[8];
          tbl[0] = a0; tbl[1] = a1;
          if (a0 > a1) { for (int i = 1; i <= 5; i++) tbl[i + 1] = ((6 - i) * a0 + i * a1) / 7; }
          else { for (int i = 1; i <= 3; i++) tbl[i + 1] = ((4 - i) * a0 + i * a1) / 5; tbl[6] = 0; tbl[7] = 255; }
          ulong abits = 0;
          for (int i = 0; i < 16; i++) {
            int best = 0, bestd = int.MaxValue;
            int limit = (a0 > a1) ? 8 : 6;
            for (int k = 0; k < limit; k++) {
              int d = Math.Abs(tbl[k] - a[i]);
              if (d < bestd) { bestd = d; best = k; }
            }
            abits |= (ulong)best << (3 * i);
          }
          w.Write(a0); w.Write(a1);
          for (int i = 0; i < 6; i++) w.Write((byte)((abits >> (8 * i)) & 0xFF));

          // BC1 colour: endpoints from the luminance extremes of the block.
          int lo = int.MaxValue, hi = int.MinValue, loI = 0, hiI = 0;
          for (int i = 0; i < 16; i++) {
            int lum = rr[i] * 299 + gg[i] * 587 + bb[i] * 114;
            if (lum < lo) { lo = lum; loI = i; }
            if (lum > hi) { hi = lum; hiI = i; }
          }
          ushort c0 = To565(rr[hiI], gg[hiI], bb[hiI]);
          ushort c1 = To565(rr[loI], gg[loI], bb[loI]);
          if (c0 < c1) { ushort t = c0; c0 = c1; c1 = t; }
          if (c0 == c1) { if (c1 > 0) c1--; else c0++; }
          int[] pr = new int[4], pg = new int[4], pb = new int[4];
          Color565(c0, out pr[0], out pg[0], out pb[0]);
          Color565(c1, out pr[1], out pg[1], out pb[1]);
          pr[2] = (2 * pr[0] + pr[1]) / 3; pg[2] = (2 * pg[0] + pg[1]) / 3; pb[2] = (2 * pb[0] + pb[1]) / 3;
          pr[3] = (pr[0] + 2 * pr[1]) / 3; pg[3] = (pg[0] + 2 * pg[1]) / 3; pb[3] = (pb[0] + 2 * pb[1]) / 3;
          uint cbits = 0;
          for (int i = 0; i < 16; i++) {
            int best = 0, bestd = int.MaxValue;
            for (int k = 0; k < 4; k++) {
              int dr = pr[k] - rr[i], dg = pg[k] - gg[i], db = pb[k] - bb[i];
              int d = dr * dr + dg * dg + db * db;
              if (d < bestd) { bestd = d; best = k; }
            }
            cbits |= (uint)best << (2 * i);
          }
          w.Write(c0); w.Write(c1); w.Write(cbits);
        }
      }
    }
  }
}
'@ -ReferencedAssemblies System.Drawing

function ConvertTo-Png {
  param([string]$src, [string]$dst, [uint32]$bg)
  $bytes = [System.IO.File]::ReadAllBytes($src)
  $w = 0; $h = 0
  $px = [Dds]::Decode($bytes, [ref]$w, [ref]$h)
  $bmp = New-Object System.Drawing.Bitmap($w, $h, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
  $bgR = ($bg -shr 16) -band 0xFF; $bgG = ($bg -shr 8) -band 0xFF; $bgB = $bg -band 0xFF
  for ($y = 0; $y -lt $h; $y++) {
    for ($x = 0; $x -lt $w; $x++) {
      $p = $px[$y * $w + $x]
      $a = ($p -shr 24) -band 0xFF
      $r = ($p -shr 16) -band 0xFF; $g = ($p -shr 8) -band 0xFF; $b = $p -band 0xFF
      $r = [int](($r * $a + $bgR * (255 - $a)) / 255)
      $g = [int](($g * $a + $bgG * (255 - $a)) / 255)
      $b = [int](($b * $a + $bgB * (255 - $a)) / 255)
      $bmp.SetPixel($x, $y, [System.Drawing.Color]::FromArgb(255, $r, $g, $b))
    }
  }
  $bmp.Save($dst, [System.Drawing.Imaging.ImageFormat]::Png)
  $bmp.Dispose()
  "decoded $src -> $dst (${w}x${h})"
}

function ConvertTo-Dds {
  param([string]$src, [string]$dst)
  $bmp = New-Object System.Drawing.Bitmap($src)
  $w = $bmp.Width; $h = $bmp.Height
  if (($w % 4) -ne 0 -or ($h % 4) -ne 0) { throw "size must be a multiple of 4, got ${w}x${h}" }
  $px = New-Object 'int[]' ($w * $h)
  for ($y = 0; $y -lt $h; $y++) {
    for ($x = 0; $x -lt $w; $x++) {
      $px[$y * $w + $x] = $bmp.GetPixel($x, $y).ToArgb()
    }
  }
  $bmp.Dispose()
  [Dds]::Encode($px, $w, $h, $dst)
  "encoded $src -> $dst (${w}x${h}, DXT5)"
}

if ($Mode -eq 'decode') {
  ConvertTo-Png -src (Resolve-Path $InPath) -dst $OutPath -bg ([Convert]::ToUInt32($Background, 16))
}
else {
  ConvertTo-Dds -src (Resolve-Path $InPath) -dst $OutPath
}
