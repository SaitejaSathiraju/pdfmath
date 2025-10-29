#!/usr/bin/env python3
"""
Shape Telugu (or any script) using HarfBuzz (uharfbuzz) and emit JSON describing
the glyph ids and their positions in PDF units.

This script does shaping only — producing glyph IDs and x/y advances/offsets.
It does not draw a PDF. The JSON can be consumed by a PDF generator that accepts
positioned glyphs (glyph id/name + x,y advances). Example consumers:
- A PDF library that supports direct glyph placement using glyph names/IDs
- A custom rendering pipeline that converts glyph outlines to paths

Usage:
  pip install -r requirements.txt
  python examples/shape_with_harfbuzz.py --font path/to/NotoSansTelugu-Regular.ttf --text "సాయంత్రం"
"""

import json
import argparse
import unicodedata
from pathlib import Path
from fontTools.ttLib import TTFont
import uharfbuzz as hb

def load_font_face(font_path: Path):
    with open(font_path, "rb") as fh:
        data = fh.read()
    face = hb.Face(data)
    font = hb.Font(face)
    # set scale to upem (unitsPerEm)
    tt = TTFont(font_path)
    upem = tt['head'].unitsPerEm
    font.scale = (upem, upem)
    return font, tt

def shape_text(font, text, script="tel", lang="te"):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.set_script(script)
    buf.set_language(lang)
    buf.guess_segment_properties()
    hb.shape(font, buf)
    infos = buf.glyph_infos
    pos = buf.glyph_positions
    result = []
    for info, p in zip(infos, pos):
        result.append({
            "gid": info.codepoint,
            "cluster": info.cluster,
            "x_advance": p.x_advance,
            "y_advance": p.y_advance,
            "x_offset": p.x_offset,
            "y_offset": p.y_offset
        })
    return result

def gid_to_name(ttfont: TTFont, gid: int) -> str:
    # map gid to glyph name (may be .notdef for some)
    try:
        name = ttfont.getGlyphName(gid)
    except Exception:
        name = f"gid{gid}"
    return name

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--font", required=True)
    parser.add_argument("--text", required=True)
    parser.add_argument("--out", default="shaped_output.json")
    args = parser.parse_args()

    text = unicodedata.normalize("NFC", args.text)
    font_path = Path(args.font)
    assert font_path.exists()

    hb_font, tt = load_font_face(font_path)
    shaped = shape_text(hb_font, text)

    # include glyph names
    for item in shaped:
        item["glyph_name"] = gid_to_name(tt, item["gid"])

    output = {
        "text": text,
        "font": str(font_path),
        "shaped": shaped,
        "unitsPerEm": tt['head'].unitsPerEm
    }

    Path(args.out).write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print("Wrote shaped output to", args.out)

if __name__ == "__main__":
    main()
