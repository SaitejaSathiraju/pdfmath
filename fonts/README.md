# Telugu fonts for examples

This repo does not include font binaries. For the examples, download a Telugu font with proper OpenType support, for example:

- Noto Sans Telugu (Google Fonts): https://github.com/google/fonts/tree/main/ofl/notosanstelugu
  - Download NotoSansTelugu-Regular.ttf and place it in the repo (e.g. fonts/NotoSansTelugu-Regular.ttf)

After downloading, run the Playwright example:
  pip install -r requirements.txt
  python -m playwright install
  python examples/html_to_pdf_playwright.py --font fonts/NotoSansTelugu-Regular.ttf --out examples/telugu_pdf.pdf

Or shape-only:
  python examples/shape_with_harfbuzz.py --font fonts/NotoSansTelugu-Regular.ttf --text "సాయంత్రం" --out shaped.json
