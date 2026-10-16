"""Meldet neue/geänderte Seiten an IndexNow (Bing, Yandex, Seznam, Naver …). Kein Konto nötig.

Aufruf NACH dem Push, wenn die Seite live ist:  py tools/indexnow.py          (neueste 10 Meldungen + Startseite)
                                                py tools/indexnow.py --all    (alle Seiten aus der Sitemap)
Der Schlüssel liegt als 136a170ebd0bc62abf1accd763438466.txt im Wurzelordner und muss online erreichbar bleiben.
"""
import json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = "136a170ebd0bc62abf1accd763438466"
HOST = "leonida-news.de"

urls = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
if "--all" not in sys.argv:
    urls = [urls[0]] + sorted(urls[1:], reverse=True)[:10]
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print(f"IndexNow: {r.status} für {len(urls)} Adressen")
