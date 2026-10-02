"""Erzeugt das LNN-Icon (SVG + PNG + ICO) aus der lokalen Anton-Schrift."""
import io, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image, ImageDraw, ImageFont

site = sys.argv[1]
out = sys.argv[2]
FG, BG, RED = "#f4f2f7", "#07070c", "#e11d48"

font = TTFont(f"{out}/bs900.ttf")
font.flavor = None
buf = io.BytesIO(); font.save(buf); buf.seek(0)
ttf = TTFont(buf)
gs = ttf.getGlyphSet(); cmap = ttf.getBestCmap()

# Textlayout in Font-Einheiten
text = "LNN"
x = 0; glyphs = []
for ch in text:
    g = cmap[ord(ch)]
    glyphs.append((g, x)); x += gs[g].width
bp = BoundsPen(gs)
for g, gx in glyphs:
    gs[g].draw(TransformPen(bp, (1, 0, 0, 1, gx, 0)))
xmin, ymin, xmax, ymax = bp.bounds

# 64er-Raster: weißes Kästchen, Text dunkel, roter LIVE-Balken unten
S = 64; pad = 6; bar = 11
box_h = S - bar
tw, th = xmax - xmin, ymax - ymin
scale = min((S - 2 * pad) / tw, (box_h - 2 * 9) / th)
ox = (S - tw * scale) / 2 - xmin * scale
oy = (box_h + th * scale) / 2 + ymin * scale  # Grundlinie (y nach unten)

pen = SVGPathPen(gs)
for g, gx in glyphs:
    gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, ox + gx * scale, oy)))
path = pen.getCommands()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<clipPath id="c"><rect width="64" height="64" rx="12"/></clipPath>
<g clip-path="url(#c)"><rect width="64" height="64" fill="{FG}"/><rect y="{box_h}" width="64" height="{bar}" fill="{RED}"/></g>
<path fill="{BG}" d="{path}"/>
</svg>
'''
open(f"{out}/favicon.svg", "w", encoding="utf-8").write(svg)

# PNG per Supersampling über Pillow (Text als Schrift gerendert, gleiche Geometrie)
ttf_path = f"{out}/anton.ttf"; buf.seek(0); open(ttf_path, "wb").write(buf.read())
def render(px, rounded=True):
    k = 8; Z = px * k; f = Z / S
    im = Image.new("RGBA", (Z, Z), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    mask = Image.new("L", (Z, Z), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, Z - 1, Z - 1], radius=int(12 * f) if rounded else 0, fill=255)
    base = Image.new("RGBA", (Z, Z), FG)
    ImageDraw.Draw(base).rectangle([0, int(box_h * f), Z, Z], fill=RED)
    im.paste(base, (0, 0), mask)
    upm = ttf["head"].unitsPerEm
    pf = ImageFont.truetype(ttf_path, int(upm * scale * f))
    d = ImageDraw.Draw(im)
    d.text((ox * f, oy * f), text, font=pf, fill=BG, anchor="ls")
    return im.resize((px, px), Image.LANCZOS)

render(180, rounded=False).convert("RGB").save(f"{out}/apple-touch-icon.png")
for n in (32, 192, 512):
    render(n).save(f"{out}/icon-{n}.png")
render(256).save(f"{out}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("scale", round(scale, 4), "text", round(tw * scale, 1), "x", round(th * scale, 1))
