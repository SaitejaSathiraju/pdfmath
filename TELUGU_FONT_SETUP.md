# Telugu Font Setup Instructions

## Problem
GoNotoKurrent font doesn't have proper Telugu shaping (gunintaalu and deergalu don't combine correctly).

## Solution: Download and Install Noto Sans Telugu

### Step 1: Download Noto Sans Telugu

1. Visit: https://fonts.google.com/noto/specimen/Noto+Sans+Telugu
2. Click "Download family" (or direct link: https://github.com/google/fonts/raw/main/ofl/notosanstelugu/NotoSansTelugu-Regular.ttf)
3. Save the file as `NotoSansTelugu-Regular.ttf`

### Step 2: Place the Font File

Copy `NotoSansTelugu-Regular.ttf` to one of these locations:

**Option A: Font cache folder (Recommended)**
```
C:\Users\<your-username>\.cache\babeldoc\fonts\NotoSansTelugu-Regular.ttf
```

**Option B: In the pdf2zh folder**
```
PDFMathTranslate\pdf2zh\NotoSansTelugu-Regular.ttf
```

### Step 3: Run Translation Again

The code will automatically detect and use the Telugu font:
```bash
pdf2zh sample-local-pdf.pdf -li en -lo te -s google --ignore-cache --skip-subset-fonts
```

## Quick PowerShell Download Command

Run this in PowerShell:

```powershell
$fontUrl = "https://github.com/google/fonts/raw/main/ofl/notosanstelugu/NotoSansTelugu-Regular.ttf"
$fontDir = "$env:USERPROFILE\.cache\babeldoc\fonts"
if (-not (Test-Path $fontDir)) { New-Item -ItemType Directory -Path $fontDir -Force }
$fontPath = "$fontDir\NotoSansTelugu-Regular.ttf"
Invoke-WebRequest -Uri $fontUrl -OutFile $fontPath
Write-Host "Font downloaded to: $fontPath"
```

Then run the translation again!

