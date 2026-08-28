# Draw unique 64x64 CMO-style silhouettes (flat off-white, ~48px, centered)
# and encode them as DXT5 DDS next to the rest of the custom icons.

param(
  [string]$PngDir = 'C:\STALKER_DEV\Anthology\.cache\icons',
  [string]$DdsDir = 'C:\STALKER_DEV\Anthology\addon\context_menu_overhaul_anthology\gamedata\textures\ui'
)

Add-Type -AssemblyName System.Drawing

$ink = [System.Drawing.Color]::FromArgb(255, 236, 236, 236)

function New-Canvas {
  $bmp = New-Object System.Drawing.Bitmap 64, 64, ([System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
  $g.Clear([System.Drawing.Color]::Transparent)
  $brush = New-Object System.Drawing.SolidBrush $ink
  ,$bmp, $g, $brush
}

function Save-Icon($name, $bmp) {
  New-Item -ItemType Directory -Force -Path $PngDir | Out-Null
  $png = Join-Path $PngDir "$name.png"
  $bmp.Save($png, [System.Drawing.Imaging.ImageFormat]::Png)
  $dds = Join-Path $DdsDir "$name.dds"
  & powershell -NoProfile -ExecutionPolicy Bypass -File 'C:\STALKER_DEV\Anthology\tools\dds_tool.ps1' encode $png $dds | Out-Host
}

function Draw-And-Save($name, [scriptblock]$draw) {
  $parts = New-Canvas
  $bmp = $parts[0]; $g = $parts[1]; $brush = $parts[2]
  & $draw $g $brush
  $g.Dispose(); $brush.Dispose()
  Save-Icon $name $bmp
  $bmp.Dispose()
}

# Banknote with a vertical split — money exchange.
Draw-And-Save 'ui_cmo_money' {
  param($g, $b)
  $g.FillRectangle($b, 12, 20, 18, 24)
  $g.FillRectangle($b, 34, 20, 18, 24)
  $g.FillEllipse($b, 16, 28, 8, 8)
  $g.FillEllipse($b, 40, 28, 8, 8)
  $g.FillRectangle($b, 30, 18, 4, 6)
  $g.FillRectangle($b, 30, 40, 4, 6)
}

# Round mine with fuse.
Draw-And-Save 'ui_cmo_mine' {
  param($g, $b)
  $g.FillEllipse($b, 14, 16, 36, 36)
  $g.FillRectangle($b, 30, 8, 4, 10)
  $g.FillEllipse($b, 28, 5, 8, 8)
  $g.FillEllipse($b, 29, 28, 6, 6)
}

# Hydration bladder with drinking tube.
Draw-And-Save 'ui_cmo_camelbak' {
  param($g, $b)
  $g.FillEllipse($b, 16, 18, 26, 34)
  $g.FillRectangle($b, 38, 14, 4, 22)
  $g.FillEllipse($b, 36, 10, 8, 8)
  $g.FillEllipse($b, 24, 30, 10, 10)
}

# Autodoc syringe.
Draw-And-Save 'ui_cmo_syringe' {
  param($g, $b)
  $g.FillRectangle($b, 8, 28, 10, 8)
  $g.FillRectangle($b, 18, 26, 26, 12)
  $g.FillRectangle($b, 44, 30, 14, 4)
  $g.FillRectangle($b, 26, 22, 3, 4)
  $g.FillRectangle($b, 32, 22, 3, 4)
}

# Stuck cartridge / unjam.
Draw-And-Save 'ui_cmo_unjam' {
  param($g, $b)
  $g.FillRectangle($b, 10, 26, 28, 14)
  $g.FillRectangle($b, 36, 30, 10, 6)
  $path = New-Object System.Drawing.Drawing2D.GraphicsPath
  $path.AddPolygon([System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(38, 22),
    [System.Drawing.Point]::new(52, 14),
    [System.Drawing.Point]::new(56, 20),
    [System.Drawing.Point]::new(42, 28)
  ))
  $g.FillPath($b, $path)
  $path.Dispose()
}

# Armor plate (not a vest).
Draw-And-Save 'ui_cmo_plate' {
  param($g, $b)
  $g.FillRectangle($b, 16, 12, 32, 40)
  $clear = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::Transparent)
  $g.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceCopy
  $g.FillEllipse($clear, 20, 16, 6, 6)
  $g.FillEllipse($clear, 38, 16, 6, 6)
  $g.FillEllipse($clear, 20, 42, 6, 6)
  $g.FillEllipse($clear, 38, 42, 6, 6)
  $g.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceOver
  $clear.Dispose()
}

# Oil can with spout — SOIP refill.
Draw-And-Save 'ui_cmo_oilcan' {
  param($g, $b)
  $g.FillEllipse($b, 12, 24, 28, 24)
  $g.FillRectangle($b, 16, 20, 20, 12)
  $path = New-Object System.Drawing.Drawing2D.GraphicsPath
  $path.AddPolygon([System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(36, 22),
    [System.Drawing.Point]::new(54, 12),
    [System.Drawing.Point]::new(56, 18),
    [System.Drawing.Point]::new(38, 28)
  ))
  $g.FillPath($b, $path)
  $path.Dispose()
  $g.FillEllipse($b, 50, 8, 6, 6)
}

# Pinup magazine.
Draw-And-Save 'ui_cmo_pinup' {
  param($g, $b)
  $g.FillRectangle($b, 18, 10, 28, 44)
  $g.FillEllipse($b, 26, 16, 12, 12)
  $g.FillEllipse($b, 22, 28, 20, 18)
}

# Cartridge split into parts.
Draw-And-Save 'ui_cmo_ammopart' {
  param($g, $b)
  $g.FillEllipse($b, 10, 26, 14, 12)
  $g.FillRectangle($b, 20, 26, 14, 12)
  $g.FillRectangle($b, 38, 26, 16, 12)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(54, 26),
    [System.Drawing.Point]::new(60, 32),
    [System.Drawing.Point]::new(54, 38)
  ))
}

# Two magazines coupled.
Draw-And-Save 'ui_cmo_maglink' {
  param($g, $b)
  $g.FillRectangle($b, 12, 14, 14, 36)
  $g.FillRectangle($b, 38, 14, 14, 36)
  $g.FillRectangle($b, 24, 28, 16, 8)
}

# Two magazines coming apart.
Draw-And-Save 'ui_cmo_magunlink' {
  param($g, $b)
  $g.FillRectangle($b, 10, 14, 14, 36)
  $g.FillRectangle($b, 40, 14, 14, 36)
  $g.FillRectangle($b, 24, 30, 6, 4)
  $g.FillRectangle($b, 34, 30, 6, 4)
}

# Kettle with steam — boil water.
Draw-And-Save 'ui_cmo_kettle' {
  param($g, $b)
  $g.FillEllipse($b, 14, 24, 32, 24)
  $g.FillRectangle($b, 20, 20, 20, 10)
  $g.FillEllipse($b, 40, 26, 12, 10)
  $g.FillRectangle($b, 12, 30, 6, 10)
  $g.FillEllipse($b, 24, 8, 5, 5)
  $g.FillEllipse($b, 32, 6, 5, 5)
  $g.FillEllipse($b, 40, 8, 5, 5)
}

# Artifact sacrifice (Lucifer) — diamond + downward mark.
Draw-And-Save 'ui_cmo_sacrifice' {
  param($g, $b)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(32, 8),
    [System.Drawing.Point]::new(52, 28),
    [System.Drawing.Point]::new(32, 36),
    [System.Drawing.Point]::new(12, 28)
  ))
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(26, 36),
    [System.Drawing.Point]::new(38, 36),
    [System.Drawing.Point]::new(32, 54)
  ))
}

# Torn page.
Draw-And-Save 'ui_cmo_tearpage' {
  param($g, $b)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(16, 10),
    [System.Drawing.Point]::new(42, 10),
    [System.Drawing.Point]::new(46, 18),
    [System.Drawing.Point]::new(40, 24),
    [System.Drawing.Point]::new(48, 32),
    [System.Drawing.Point]::new(40, 40),
    [System.Drawing.Point]::new(46, 48),
    [System.Drawing.Point]::new(16, 54)
  ))
}

# Folded note (not a book).
Draw-And-Save 'ui_cmo_note' {
  param($g, $b)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(14, 18),
    [System.Drawing.Point]::new(50, 14),
    [System.Drawing.Point]::new(50, 50),
    [System.Drawing.Point]::new(14, 46)
  ))
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(14, 18),
    [System.Drawing.Point]::new(32, 26),
    [System.Drawing.Point]::new(50, 14)
  ))
}

# Anvil — workshop.
Draw-And-Save 'ui_cmo_anvil' {
  param($g, $b)
  $g.FillRectangle($b, 10, 20, 44, 10)
  $g.FillRectangle($b, 24, 30, 16, 10)
  $g.FillRectangle($b, 16, 40, 32, 8)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(10, 20),
    [System.Drawing.Point]::new(4, 28),
    [System.Drawing.Point]::new(10, 30)
  ))
}

# Exo PSU brick with cable.
Draw-And-Save 'ui_cmo_psu' {
  param($g, $b)
  $g.FillRectangle($b, 12, 16, 28, 32)
  $g.FillRectangle($b, 16, 20, 20, 3)
  $g.FillRectangle($b, 16, 26, 20, 3)
  $g.FillRectangle($b, 16, 32, 20, 3)
  $g.FillRectangle($b, 40, 28, 10, 6)
  $g.FillEllipse($b, 48, 24, 8, 14)
}

# Faction patch peeling off.
Draw-And-Save 'ui_cmo_unpatch' {
  param($g, $b)
  $g.FillEllipse($b, 14, 14, 32, 32)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(40, 16),
    [System.Drawing.Point]::new(54, 10),
    [System.Drawing.Point]::new(52, 24)
  ))
}

# Circular arrows — trait respec.
Draw-And-Save 'ui_cmo_respec' {
  param($g, $b)
  $pen = New-Object System.Drawing.Pen $ink, 5
  $pen.StartCap = [System.Drawing.Drawing2D.LineCap]::Round
  $pen.EndCap = [System.Drawing.Drawing2D.LineCap]::Round
  $g.DrawArc($pen, 14, 14, 36, 36, 40, 220)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(44, 12),
    [System.Drawing.Point]::new(56, 22),
    [System.Drawing.Point]::new(40, 26)
  ))
  $pen.Dispose()
}

# Handheld scanner.
Draw-And-Save 'ui_cmo_scanner' {
  param($g, $b)
  $g.FillRectangle($b, 20, 22, 24, 28)
  $g.FillEllipse($b, 18, 10, 28, 16)
  $g.FillEllipse($b, 28, 30, 8, 8)
}

# Map pin — place marker.
Draw-And-Save 'ui_cmo_marker' {
  param($g, $b)
  $g.FillEllipse($b, 18, 8, 28, 28)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(20, 28),
    [System.Drawing.Point]::new(44, 28),
    [System.Drawing.Point]::new(32, 54)
  ))
  $clear = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::Transparent)
  $g.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceCopy
  $g.FillEllipse($clear, 26, 16, 12, 12)
  $g.CompositingMode = [System.Drawing.Drawing2D.CompositingMode]::SourceOver
  $clear.Dispose()
}

# Open booklet — western goods view.
Draw-And-Save 'ui_cmo_readable' {
  param($g, $b)
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(8, 16),
    [System.Drawing.Point]::new(32, 20),
    [System.Drawing.Point]::new(32, 52),
    [System.Drawing.Point]::new(8, 46)
  ))
  $g.FillPolygon($b, [System.Drawing.Point[]]@(
    [System.Drawing.Point]::new(56, 16),
    [System.Drawing.Point]::new(32, 20),
    [System.Drawing.Point]::new(32, 52),
    [System.Drawing.Point]::new(56, 46)
  ))
}

"done"
