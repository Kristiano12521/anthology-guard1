# Reports the byte encoding of every game text file under a folder, so a mod
# never ships a rus/eng xml or a .script in anything but Windows-1251.
#
# Usage: powershell -File tools/check_encoding.ps1 <folder>

param([Parameter(Mandatory = $true)][string]$Root)

$root = (Resolve-Path -LiteralPath $Root).ProviderPath
$utf8Strict = New-Object System.Text.UTF8Encoding($false, $true)

Get-ChildItem -LiteralPath $root -Recurse -File -Include *.script, *.ltx, *.xml, *.txt, *.ini, *.seq |
  ForEach-Object {
    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
    $nonAscii = 0
    foreach ($byte in $bytes) { if ($byte -gt 127) { $nonAscii++ } }

    $encoding = 'ascii'
    if ($nonAscii -gt 0) {
      $encoding = 'cp1251'
      try {
        $null = $utf8Strict.GetString($bytes)
        $encoding = 'utf-8'
      }
      catch { }
    }

    $bom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF)
    [pscustomobject]@{
      Encoding = $encoding
      Bom      = $bom
      NonAscii = $nonAscii
      Path     = $_.FullName.Substring($root.Length + 1)
    }
  } | Sort-Object Encoding, Path | Format-Table -AutoSize
