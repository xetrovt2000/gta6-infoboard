# Icon und Vorschaubild neu erzeugen

Benötigt: Python mit `fonttools brotli pillow` (z. B. eigene venv: `python -m venv favenv` und `favenv/Scripts/pip install fonttools brotli pillow`).

1. Statische Schriften aus den variablen Webfonts ziehen (schreibt bs900.ttf, bs800.ttf, inter500.ttf nach OUT):
   `python prep_fonts.py <website-ordner> <OUT>`
2. Icon (favicon.svg/.ico, apple-touch-icon.png, icon-32/192/512.png nach OUT):
   `python favicon.py <website-ordner> <OUT>`
3. Vorschaubild zum Teilen (og.jpg, 1200×630, Basis `preview.jpg`):
   `python og.py <website-ordner> <OUT>`

Danach die Dateien aus OUT in den Website-Ordner kopieren und in `index.html` die `?v=N` an den Icon- und og:image-Verweisen hochzählen,
sonst zeigen Browser und Messenger die alten Bilder.
