"""Erzeugt verkleinerte Vorschaubilder für Galerie, Themenkarten und das Titelbild am Handy.

Aufruf im Repo-Ordner:  python tools/make_thumbs.py
Neue Bilder in shots/ oder official/ ablegen, Skript laufen lassen, thumbs/ mit committen.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SIZES = {"thumbs": 800, "mid": 1280}  # Vorschauen / Titelbild auf kleinen Bildschirmen

for folder in ("shots", "official"):
    for src in sorted((ROOT / folder).glob("*.webp")):
        im = None
        for out_dir, width in SIZES.items():
            if out_dir == "mid" and folder != "shots":
                continue
            dst = ROOT / out_dir / folder / src.name
            if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
                continue
            im = im or Image.open(src)
            h = round(im.height * width / im.width)
            dst.parent.mkdir(parents=True, exist_ok=True)
            im.resize((width, h), Image.LANCZOS).save(dst, "WEBP", quality=76, method=6)
            print(f"{dst.relative_to(ROOT)}  {dst.stat().st_size // 1024} KB")
