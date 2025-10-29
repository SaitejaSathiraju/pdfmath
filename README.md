# Telugu (and other Indic) PDF rendering — fixes and examples

This branch contains examples and helper scripts to ensure correct shaping of Telugu text (and other Indic scripts) when creating PDFs.

Why the problem happens
- Telugu uses combining marks, vowel signs, and conjunct formation. Correct visual glyphs are produced by an OpenType shaping engine (Harfbuzz/Pango) using the font's GSUB/GPOS tables.
- Many PDF toolkits draw Unicode code points one-by-one without shaping, producing separate characters for gunintaalu (గుణింతాలు) and deergalu (దీర్ఘాలు).

What this branch contains
- examples/html_to_pdf_playwright.py — recommended, easy, reliable: render HTML (with embedded font) in headless Chromium (Playwright) so glyph shaping is performed correctly and the PDF embeds the font.
- examples/shape_with_harfbuzz.py — a helper that uses HarfBuzz (uharfbuzz) and fontTools to produce a JSON describing glyph IDs and positioned advances. Use this when you must render glyphs yourself in a low-level PDF library.
- requirements.txt — Python package requirements.
- examples/sample_telugu.txt — short sample text to test.
- fonts/ README explains where to obtain Noto Sans Telugu (not checked in due to binary size).

Recommended quick route (works in most setups)
1. Install requirements and Playwright, then run the Playwright example. Playwright/Chromium performs shaping and will embed the font in the produced PDF.
2. If you must use a low-level PDF renderer without shaping, run shape_with_harfbuzz.py, then use its output with a PDF library capable of drawing positioned glyphs (glyph id/name + x,y advances). The code and notes explain what to do next.

Notes
- Always normalize Telugu text to NFC before shaping/embedding. The examples do this.
- Use a proper Telugu font (Noto Sans Telugu, etc.) that includes GSUB/GPOS OpenType data.
- Installing Playwright requires `playwright install` after pip install to get the browsers.

If you want, I will push the prepared files to the telugu-fix branch now and then:
- run the Playwright example with a bundled font to produce a working, shaped PDF example, and
- add CI examples or tests demonstrating correct glyph composition.
