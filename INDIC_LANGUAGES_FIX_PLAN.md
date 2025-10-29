# Fix Plan for All Indic Languages

## Current Status

✅ **Hindi (Devanagari)**: Renders correctly with glyph ID encoding  
❌ **Telugu**: Garbled text (Greek characters appear)  
❌ **Other Dravidian languages**: Likely same issue

## Root Cause

The `GoNotoKurrent-Regular.ttf` font supports Telugu glyphs, but:
1. **Font embedding** might not be preserving Telugu characters correctly
2. **CID encoding** may be needed for proper Indic script shaping  
3. **Glyph ID mapping** works for Hindi but may not match for Telugu

## Solution Options

### Option 1: Use CID Font Encoding for Indic Scripts
Convert Indic scripts to use CID font encoding (like Chinese/Japanese):
- Modify `raw_string()` to detect Indic scripts
- Use Unicode code points with CID font encoding
- Requires font to support CID mapping

### Option 2: Ensure Proper Font Embedding
- Use `--skip-subset-fonts` (already implemented)
- Verify font is fully embedded with all Telugu glyphs
- Check if font subsetting is removing necessary glyphs

### Option 3: Use Different Font Encoding Method
- PDF fonts can use different encoding methods:
  - **Identity-H** encoding for CID fonts (works for Indic)
  - **Unicode** encoding (works but may need proper font setup)
  - **Glyph IDs** (current - works for Hindi, not Telugu)

## Immediate Action

Since Hindi works, the pipeline is correct. The issue is **Telugu-specific encoding**.

**Next step**: Check if we can force CID font encoding for Indic scripts, similar to how Chinese/Japanese are handled.

## Test Commands

```bash
# Test Telugu with current setup
pdf2zh sample-local-pdf.pdf -li en -lo te -s google --ignore-cache --skip-subset-fonts

# Test Hindi (should work)
pdf2zh sample-local-pdf.pdf -li en -lo hi -s google --ignore-cache

# Test IndicTrans2 (may handle Telugu differently)
pdf2zh sample-local-pdf.pdf -li en -lo te -s indictrans2 --ignore-cache -p 1 -t 1
```

