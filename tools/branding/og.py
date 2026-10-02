"""Vorschaubild 1200x630 im LNN-Look: Vice-City-Screenshot, Verlauf links, Logo, Titel, Release."""
import io, sys
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

site, out = sys.argv[1], sys.argv[2]
def ttf(name):
    f = TTFont(f"{site}/fonts/{name}.woff2"); f.flavor = None
    p = f"{out}/{name}.ttf"; f.save(p); return p
ANTON, COND, COND5 = f"{out}/bs900.ttf", f"{out}/bs800.ttf", f"{out}/inter500.ttf"
FG, BG, RED, GOLD, MUTED = (244, 242, 247), (7, 7, 12), (225, 29, 72), (251, 191, 36), (215, 210, 228)

W, H = 1200, 630
img = Image.open(f"{site}/preview.jpg").convert("RGB").resize((W, H))

# dunkler Verlauf von links, damit der Text lesbar bleibt; rechts bleibt das Bild (mit Wasserzeichen) frei
grad = Image.new("L", (W, 1))
for x in range(W):
    t = x / W
    grad.putpixel((x, 0), int(235 * max(0.0, 1 - t / 0.72) ** 1.15))
grad = grad.resize((W, H))
img = Image.composite(Image.new("RGB", (W, H), BG), img, grad)
d = ImageDraw.Draw(img)

X = 64
# Logo-Kästchen wie im Header
f_logo = ImageFont.truetype(ANTON, 44)
lb = d.textbbox((0, 0), "LNN", font=f_logo)
bw, bh = lb[2] - lb[0] + 28, 66
d.rounded_rectangle([X, 60, X + bw, 60 + bh], radius=6, fill=FG)
d.text((X + 14 - lb[0], 60 + (bh - (lb[3] - lb[1])) / 2 - lb[1]), "LNN", font=f_logo, fill=BG)
# LIVE-Marke
f_live = ImageFont.truetype(COND, 30)
lx = X + bw + 18
d.rounded_rectangle([lx, 73, lx + 104, 113], radius=4, fill=RED)
d.ellipse([lx + 12, 86, lx + 26, 100], fill=FG)
d.text((lx + 34, 93), "LIVE", font=f_live, fill=FG, anchor="lm")

f_kick = ImageFont.truetype(COND, 30)
d.text((X, 190), "LEONIDA NEWS NETWORK", font=f_kick, fill=GOLD)
f_title = ImageFont.truetype(ANTON, 128)
d.text((X, 228), "GTA 6", font=f_title, fill=FG)
d.text((X, 350), "INFOBOARD", font=f_title, fill=FG)
f_sub = ImageFont.truetype(COND5, 28)
d.text((X, 492), "Liveticker · jede Info mit Quellenstempel", font=f_sub, fill=MUTED)

# Release-Zeile
f_rel = ImageFont.truetype(COND, 32)
y = 552
d.rectangle([X, y, X + 6, y + 36], fill=RED)
d.text((X + 20, y + 18), "RELEASE 19.11.2026", font=f_rel, fill=FG, anchor="lm")
rw = d.textlength("RELEASE 19.11.2026", font=f_rel)
d.text((X + 20 + rw + 26, y + 18), "leonida-news.de", font=f_rel, fill=GOLD, anchor="lm")

img.save(f"{out}/og.jpg", quality=86, optimize=True, progressive=True)
print("ok")
