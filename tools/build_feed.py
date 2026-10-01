"""Erzeugt feed.xml (RSS 2.0) aus dem Liveticker in index.html.

Aufruf im Repo-Ordner:  python tools/build_feed.py
Nach jedem Ticker-Update ausführen und feed.xml mit committen.
"""
import hashlib, html, re
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leonida-news.de/"
YEAR = 2026
MAX_ITEMS = 40
TZ = timezone(timedelta(hours=2))  # MESZ; Ticker-Zeiten sind MESZ
MONTHS = {m: i for i, m in enumerate(
    "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split(), 1)}

src = (ROOT / "index.html").read_text(encoding="utf-8")
live = src[src.index('id="live"'):src.index('<aside class="side">')]

def text(s):
    s = re.sub(r"<s>.*?</s>", "", s, flags=re.S)  # gestrichene Meldungen nicht in den Feed-Text
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

items, day = [], None
for li in re.finditer(r"<li([^>]*)>(.*?)</li>", live, flags=re.S):
    attrs, body = li.groups()
    if 'class="day"' in attrs:
        m = re.search(r"(\d{1,2})\.\s*(\w+)", text(body))
        day = (int(m.group(1)), MONTHS[m.group(2)])
        continue
    t = re.search(r"<time>(\d{1,2}):(\d{2})</time>", body)
    if not t or not day:
        continue
    div = re.search(r"<div>(.*)</div>", body, flags=re.S).group(1)
    tag = re.search(r'class="tag[^"]*">([^<]+)<', div)
    bold = re.search(r"<b>(.*?)</b>", div, flags=re.S)
    full = text(re.sub(r'<span class="tag[^"]*">[^<]+</span>', "", div))
    full = re.sub(r"\s+(Mehr|Ansehen|Quelle)$", "", full)
    title = text(bold.group(1)).rstrip(":.") if bold else (full[:90] + ("…" if len(full) > 90 else ""))
    if tag:
        title = f"[{tag.group(1)}] {title}"
    when = datetime(YEAR, day[1], day[0], int(t.group(1)), int(t.group(2)), tzinfo=TZ)
    guid = hashlib.sha1(f"{when.isoformat()}|{full}".encode()).hexdigest()[:16]
    items.append((when, title, full, guid))

items = items[:MAX_ITEMS]
esc = lambda s: html.escape(s, quote=False)
out = [
    '<?xml version="1.0" encoding="utf-8"?>',
    '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
    "<channel>",
    "<title>GTA 6 Infoboard – Leonida News Network</title>",
    f"<link>{SITE}</link>",
    f'<atom:link href="{SITE}feed.xml" rel="self" type="application/rss+xml"/>',
    "<description>Liveticker zu GTA 6, jede Meldung mit Quellenstempel: offiziell, berichtet, Gerücht oder Leak.</description>",
    "<language>de-de</language>",
    f"<lastBuildDate>{format_datetime(items[0][0])}</lastBuildDate>",
]
for when, title, full, guid in items:
    out += [
        "<item>",
        f"<title>{esc(title)}</title>",
        f"<link>{SITE}#live</link>",
        f'<guid isPermaLink="false">lnn-{guid}</guid>',
        f"<pubDate>{format_datetime(when)}</pubDate>",
        f"<description>{esc(full)}</description>",
        "</item>",
    ]
out += ["</channel>", "</rss>", ""]
(ROOT / "feed.xml").write_text("\n".join(out), encoding="utf-8", newline="\n")

# Sitemap mitziehen, damit Google das Änderungsdatum kennt
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"  <url><loc>{SITE}</loc><lastmod>{items[0][0]:%Y-%m-%d}</lastmod><changefreq>hourly</changefreq></url>\n"
    "</urlset>\n", encoding="utf-8", newline="\n")
print(f"feed.xml: {len(items)} Meldungen, neueste {items[0][0]:%d.%m. %H:%M}")
