#!/usr/bin/env python3
"""
HTML -> PDF using Playwright (Chromium).
This approach uses Chromium's text shaping (Harfbuzz) and will render Telugu correctly
provided you embed a proper Telugu font.

Usage:
  pip install -r requirements.txt
  python -m playwright install
  python examples/html_to_pdf_playwright.py --font path/to/NotoSansTelugu-Regular.ttf --out out.pdf
"""

import base64
import argparse
import unicodedata
from pathlib import Path
from playwright.sync_api import sync_playwright

SAMPLE_TEXT = "సాయంత్రం శాంతంగా ఉంది. గుణింతాలు మరియు దీర్ఘాలు సరిగా ఉండాలి."

def embed_font_base64(font_path: Path) -> str:
    b = font_path.read_bytes()
    return base64.b64encode(b).decode('ascii')

def make_html(text: str, font_name: str, font_b64: str) -> str:
    # normalize to NFC
    text = unicodedata.normalize("NFC", text)
    css = f"""
    @font-face {{
      font-family: '{font_name}';
      src: url(data:font/ttf;base64,{font_b64}) format('truetype');
      font-display: swap;
    }}
    html, body {{
      margin: 0;
      padding: 24px;
      font-family: '{font_name}', serif;
      font-size: 20px;
    }}
    """
    html = f"""
    <!doctype html>
    <html lang="te">
    <head><meta charset="utf-8"><style>{css}</style></head>
    <body><div>{text}</div></body>
    </html>"""
    return html

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--font", required=True, help="Path to a Telugu-capable TTF (e.g. NotoSansTelugu-Regular.ttf)")
    parser.add_argument("--out", default="out.pdf")
    parser.add_argument("--text", default=SAMPLE_TEXT)
    args = parser.parse_args()

    font_path = Path(args.font)
    assert font_path.exists(), "Font file not found"

    font_b64 = embed_font_base64(font_path)
    font_name = font_path.stem

    html = make_html(args.text, font_name, font_b64)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="networkidle")
        page.pdf(path=args.out, print_background=True)
        browser.close()
    print("Saved PDF to", args.out)

if __name__ == "__main__":
    main()
