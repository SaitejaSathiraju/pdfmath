# Telugu Diacritics Solution

## Problem
Telugu text is being translated but diacritics (ottulu/vowel marks/dots) are missing in the PDF.

## Root Cause
The original encoding using `has_glyph()` encodes character-by-character, which breaks **combining diacritics** in Telugu.

Telugu uses combining marks like:
- Base: క (U+0C15) ka
- Combining: ో (U+0C4B) oo diacritic  
- Result: కో (ka + oo combined) - should display as one glyph with the oo mark

When encoded character-by-character, the combining relationship is lost.

## Current Status
- ✅ Translation to Telugu works (Google Translate works)
- ✅ PDF rendering works (with Ollama it showed text)  
- ❌ Telugu diacritics/vowel marks are missing or garbled

## Working Solution (Original)

The original code worked for rendering, but with wrong encoding:
```python
return "".join(["%04x" % self.noto.has_glyph(ord(c)) for c in cstk])
```

This uses glyph IDs which work for PDF rendering but lose combining marks.

## Attempted Fixes (Failed)

### Attempt 1: Unicode code points
```python
return "".join(["%04x" % ord(c) for c in cstk])
```
**Result**: Broke encoding completely → Greek characters appeared

### Attempt 2: UTF-16BE encoding  
```python
unicode_str = cstk.encode('utf-16be').hex()
return unicode_str
```
**Result**: Wrong format for PDF font encoding

## Correct Solution Needed

For Telugu with proper diacritics, we need:

1. **Use glyph IDs** for PDF font rendering (current approach)
2. **Preserve combining character sequences** by not splitting them
3. **Ensure font has proper OpenType features** for Telugu shaping

The issue is that Telugu text might need to be encoded as **ligatures** or the font needs **OpenType GSUB tables** for proper combining behavior.

**Next step**: Check if the GoNotoKurrent font supports Telugu properly, or use a font specifically designed for Telugu with proper OpenType features.

