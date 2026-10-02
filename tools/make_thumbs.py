"""Erzeugt verkleinerte Vorschaubilder für Galerie, Themenkarten und das Titelbild am Handy.

Aufruf im Repo-Ordner:  python tools/make_thumbs.py
Neue Bilder in shots/, official/ oder press/ ablegen, Skript laufen lassen, thumbs/ mit committen.
press/ = Bilder aus Magazinen, oft Hochformat: die Vorschau wird auf 16:9 zugeschnitten (oberes Drittel,
dort sind meist die Gesichter), das Großbild bleibt ungeschnitten.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SIZES = {"thumbs": 800, "mid": 1280}  # Vorschauen / Titelbild auf kleinen Bildschirmen

for folder in ("shots", "official", "press"):
    if not (ROOT / folder).exists():
        continue
    for src in sorted((ROOT / folder).glob("*.webp")):
        im = None
        for out_dir, width in SIZES.items():
            if out_dir == "mid" and folder != "shots":
                continue
            dst = ROOT / out_dir / folder / src.name
            if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
                continue
            im = im or Image.open(src)
            img = im
            if folder == "press" and im.width / im.height < 16 / 9:
                ch = round(im.width * 9 / 16)
                top = max(0, min(im.height - ch, round(im.height * 0.22 - ch * 0.3)))
                img = im.crop((0, top, im.width, top + ch))
            h = round(img.height * width / img.width)
            dst.parent.mkdir(parents=True, exist_ok=True)
            img.resize((width, h), Image.LANCZOS).save(dst, "WEBP", quality=76, method=6)
            print(f"{dst.relative_to(ROOT)}  {dst.stat().st_size // 1024} KB")
