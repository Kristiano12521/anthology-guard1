# Rewrites UTF-8 game files as Windows-1251, the encoding X-Ray reads .script,
# .ltx and text .xml with. Refuses any file whose characters have no CP1251
# equivalent instead of silently writing "?" in their place.
#
# Usage: powershell -File tools/to_cp1251.ps1 <file> [<file> ...]

param([Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)][string[]]$Paths)

$cp1251 = [System.Text.Encoding]::GetEncoding(1251)
$utf8Strict = New-Object System.Text.UTF8Encoding($false, $true)

foreach ($p in $Paths) {
  $full = (Resolve-Path -LiteralPath $p).ProviderPath
  $bytes = [System.IO.File]::ReadAllBytes($full)

  $text = $null
  try { $text = $utf8Strict.GetString($bytes) }
  catch { "skip (not utf-8): $p"; continue }

  if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    $text = $text.Substring(1)
  }

  $out = $cp1251.GetBytes($text)
  if ($cp1251.GetString($out) -ne $text) {
    "FAIL (characters outside cp1251): $p"
    continue
  }

  if ([System.Linq.Enumerable]::SequenceEqual($bytes, $out)) {
    "unchanged (ascii): $p"
    continue
  }

  [System.IO.File]::WriteAllBytes($full, $out)
  "converted: $p  $($bytes.Length) -> $($out.Length) bytes"
}
