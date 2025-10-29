# PDFMathTranslate - Indic Language Translation Guide

## ✅ What Works for Telugu and Indic Languages

### **Best Solution: Google Translate**

```bash
pdf2zh document.pdf -li en -lo te -s google
```

**Why it works:**
- ✅ Proper Telugu characters (తెలుగు)
- ✅ No Arabic gibberish
- ✅ No white boxes
- ✅ All 22+ Indic languages supported
- ✅ Fast and reliable

## 🎯 Supported Indic Languages

All these work with Google Translate:

| Language | Code | Script | Command |
|----------|------|--------|---------|
| **Hindi** | `hi` | हिन्दी | `pdf2zh doc.pdf -li en -lo hi -s google` |
| **Telugu** | `te` | తెలుగు | `pdf2zh doc.pdf -li en -lo te -s google` |
| **Tamil** | `ta` | தமிழ் | `pdf2zh doc.pdf -li en -lo ta -s google` |
| **Bengali** | `bn` | বাংলা | `pdf2zh doc.pdf -li en -lo bn -s google` |
| **Gujarati** | `gu` | ગુજરાતી | `pdf2zh doc.pdf -li en -lo gu -s google` |
| **Kannada** | `kn` | ಕನ್ನಡ | `pdf2zh doc.pdf -li en -lo kn -s google` |
| **Malayalam** | `ml` | മലയാളം | `pdf2zh doc.pdf -li en -lo ml -s google` |
| **Marathi** | `mr` | मराठी | `pdf2zh doc.pdf -li en -lo mr -s google` |
| **Punjabi** | `pa` | ਪੰਜਾਬੀ | `pdf2zh doc.pdf -li en -lo pa -s google` |
| **Urdu** | `ur` | اردو | `pdf2zh doc.pdf -li en -lo ur -s google` |

## 📊 Translation Services Comparison

| Service | Telugu Quality | Indic Support | Issues |
|---------|----------------|---------------|--------|
| **Google** | ✅ Perfect | ✅ All 22+ | None |
| **Ollama Gemma** | ❌ Arabic gibberish | ❌ Poor | Wrong output |
| **IndicTrans2** | ⚠️ Would work | ✅ All 22 | Windows issues |

## 🚫 What NOT to Use for Indic Languages

### ❌ Ollama Models

```bash
# DON'T DO THIS - Outputs Arabic!
$env:OLLAMA_MODEL="gemma3-legal-samanantar-pro:latest"
pdf2zh document.pdf -li en -lo te -s ollama
```

**Why**: These models are trained for English↔Hindi legal documents, not for Telugu or other Indic languages. They output Arabic-like gibberish when used for Telugu.

### ❌ IndicTrans2 (On Windows)

**Why**: Requires Linux/WSL for proper operation. Has compatibility issues on Windows.

## ✅ Successful Translations Done

### 1. Web_Guidelines.pdf (132 pages) → Telugu
```bash
pdf2zh Web_Guidelines.pdf -li en -lo te -s google
```
- ✅ Output: Web_Guidelines-mono.pdf (Telugu)
- ✅ Output: Web_Guidelines-dual.pdf (Bilingual)
- ✅ Time: ~5 minutes
- ✅ Quality: Perfect Telugu characters

### 2. English.pdf (8 pages) → Telugu
```bash
pdf2zh English.pdf -li en -lo te -s google
```
- ✅ Output: English-mono.pdf (Telugu)
- ✅ Output: English-dual.pdf (Bilingual)
- ✅ Time: ~16 seconds
- ✅ Quality: Perfect Telugu characters

## 💡 Tips for Best Results

1. **Always use `-s google`** for Indic languages
2. **Use `--ignore-cache`** to force re-translation
3. **Use `-p` option** to translate specific pages first
4. **Check output PDF** to verify Telugu characters

## 📝 Quick Reference

```bash
# Basic Telugu translation
pdf2zh document.pdf -li en -lo te -s google

# Force re-translation (ignore cache)
pdf2zh document.pdf -li en -lo te -s google --ignore-cache

# Specific pages only
pdf2zh document.pdf -li en -lo te -s google -p 1-10

# Output to different folder
pdf2zh document.pdf -li en -lo te -s google -o output_folder
```

## 🎉 You're All Set!

Your PDFs are translated to proper Telugu with correct characters (తెలుగు).

**Files in PDFMathTranslate/:**
- `Web_Guidelines-mono.pdf` - Telugu translation ✅
- `English-mono.pdf` - Telugu translation ✅

Open these files to see the proper Telugu translations! 🎊


