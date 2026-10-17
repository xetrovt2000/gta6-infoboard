"""Erzeugt für jede Ticker-Meldung eine eigene Seite unter n/<id>.html und die Sitemap.

Wird von build_feed.py aufgerufen (nach dem Vergeben der IDs). Eigene Seiten pro Meldung
bringen Google-Treffer für einzelne Themen und schöne Vorschauen beim Teilen (Discord, WhatsApp, X).
Countdown-Einträge („Noch 34 Tage“) bekommen keine Seite.
"""
import html, json, re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leonida-news.de/"
YEAR = 2026
TZ = timezone(timedelta(hours=2))
MONTHS = {m: i for i, m in enumerate(
    "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split(), 1)}
WD = "Montag Dienstag Mittwoch Donnerstag Freitag Samstag Sonntag".split()
MN = "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split()


def text(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def parse(src):
    a = src.index('id="live"')
    b = src.index('<aside class="side">')
    live = src[a:b]
    items, day = [], None
    for li in re.finditer(r"<li([^>]*)>(.*?)</li>", live, flags=re.S):
        attrs, body = li.groups()
        if 'class="day"' in attrs:
            m = re.search(r"(\d{1,2})\.\s*(\w+)", text(body))
            day = (int(m.group(1)), MONTHS[m.group(2)])
            continue
        t = re.search(r"<time>(\d{1,2}):(\d{2})</time>", body)
        lid = re.search(r'\bid="(m-[^"]+)"', attrs)
        if not t or not day or not lid:
            continue
        div = re.search(r"<div>(.*)</div>", body, flags=re.S).group(1)
        bold = re.search(r"<b>(.*?)</b>", div, flags=re.S)
        plain = text(div)
        if re.match(r"Noch \d+ Tag(e)? bis", plain):
            continue  # Countdown
        tag = re.search(r'<span class="tag ([^"]+)">([^<]+)</span>', div)
        srcs = re.search(r'<span class="srcs">(.*?)</span>(?=\s*(?:<a class="tpic"|$))', div, flags=re.S)
        pic = re.search(r'<a class="tpic"[^>]*>\s*<img src="([^"]+)" alt="([^"]*)"', div)
        bodyhtml = re.sub(r'<span class="srcs">.*?</span>(?=\s*(?:<a class="tpic"|$))|<a class="tpic".*?</a>', "", div, flags=re.S)
        bodyhtml = re.sub(r'<span class="tag [^"]+">[^<]+</span>\s*', "", bodyhtml)
        if bold:
            bodyhtml = re.sub(r"<b>.*?</b>\s*", "", bodyhtml, count=1, flags=re.S)
            title = text(bold.group(1)).rstrip(":.")
        else:  # ältere Meldungen ohne fette Schlagzeile: erster Satz als Titel
            first = re.match(r"(.{20,120}?[.!?])(\s|$)", text(bodyhtml))
            title = (first.group(1) if first else text(bodyhtml)[:90]).rstrip(":.")
        bodyhtml = re.sub(r'href="#', 'href="../#', bodyhtml).strip()
        desc = text(bodyhtml)
        items.append(dict(
            id=lid.group(1), when=datetime(YEAR, day[1], day[0], int(t.group(1)), int(t.group(2)), tzinfo=TZ),
            title=title, tag=(tag.group(1), tag.group(2)) if tag else None, body=bodyhtml, desc=desc,
            srcs=srcs.group(1).strip() if srcs else "", pic=(pic.group(1), pic.group(2)) if pic else None,
            struck="<s>" in div))
    return items


CSS = """
:root{--bg:#07070c;--panel:#10101a;--line:#262636;--fg:#f4f2f7;--muted:#a7a3b8;--red:#e11d48;--gold:#fbbf24;
--ok:#4ade80;--warn:#fbbf24;--bad:#f87171;--leak:#c4b5fd;--display:"Big Shoulders Display","Arial Narrow",Impact,sans-serif;
--body:"Inter",system-ui,sans-serif}
*{box-sizing:border-box}html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 var(--body)}
a{color:var(--gold)}
.top{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--line);background:#0b0b12}
.logo{display:inline-flex;align-items:center;gap:8px;color:var(--fg);text-decoration:none;font:900 22px/1 var(--display);letter-spacing:.04em}
.logo i{background:var(--red);color:#fff;font-style:normal;padding:4px 7px;border-radius:3px}
.top .live{margin-left:auto;font:800 14px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:#fff;
background:var(--red);padding:9px 12px;border-radius:4px;text-decoration:none}
main{max-width:760px;margin:0 auto;padding:28px 16px 40px}
.meta{color:var(--muted);font-size:14px;display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.tag{display:inline-block;font:800 12px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;padding:4px 7px 3px;
border:2px solid currentColor;border-radius:3px;rotate:-3deg}
.t-ok{color:var(--ok)}.t-warn{color:var(--warn)}.t-bad{color:var(--bad)}.t-leak{color:var(--leak)}
h1{font:900 clamp(32px,6vw,52px)/1.02 var(--display);letter-spacing:.01em;margin:14px 0 18px;text-wrap:balance}
.body{font-size:17px}.body p{margin:0 0 1em}
figure{margin:22px 0}figure img{width:100%;height:auto;border-radius:6px;display:block}
.src{margin-top:22px;padding-top:14px;border-top:1px solid var(--line);color:var(--muted);font-size:14px}
.dc{display:block;width:max-content;max-width:100%;margin:6px 0 0;padding:10px 14px;border:1px solid var(--line);border-radius:6px;color:var(--muted);text-decoration:none;font-size:14px}.dc b{color:var(--fg)}.dc:hover{border-color:var(--gold);color:var(--fg)}
.cta{display:inline-block;margin:26px 0 8px;font:800 16px/1 var(--display);letter-spacing:.1em;text-transform:uppercase;
color:#111;background:var(--gold);padding:13px 16px;border-radius:4px;text-decoration:none}
.more{margin-top:34px;border-top:1px solid var(--line);padding-top:18px}
.more h2{font:900 22px/1 var(--display);letter-spacing:.04em;text-transform:uppercase;margin:0 0 12px}
.more ul{list-style:none;margin:0;padding:0}.more li{padding:9px 0;border-bottom:1px solid var(--line)}
.more a{color:var(--fg);text-decoration:none}.more a:hover{color:var(--gold)}.more time{color:var(--muted);font-size:13px;margin-right:8px}
.nav{display:flex;justify-content:space-between;gap:12px;margin-top:22px;font-size:14px}
footer{color:var(--muted);font-size:13px;text-align:center;padding:24px 16px;border-top:1px solid var(--line)}
.xc{display:flex;width:max-content;margin:14px auto 0;align-items:center;gap:8px;color:var(--muted);text-decoration:none;font-size:12px;letter-spacing:.04em;opacity:.8;transition:opacity .2s}.xc:hover{opacity:1}.xc img{display:block;height:22px;width:auto}
"""


def fmt(d):
    return f"{WD[d.weekday()]}, {d.day}. {MN[d.month-1]} {d.year}, {d:%H:%M} Uhr"


def page(it, prev, nxt, latest):
    e = lambda s: html.escape(s, quote=True)
    url = f"{SITE}n/{it['id']}.html"
    img = SITE + it["pic"][0] if it["pic"] else SITE + "og.jpg?v=2"
    desc = it["desc"] if len(it["desc"]) <= 158 else it["desc"][:155].rsplit(" ", 1)[0] + " …"
    stamp = f'<span class="tag {it["tag"][0]}">{e(it["tag"][1])}</span>' if it["tag"] else ""
    ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": it["title"][:110],
          "datePublished": it["when"].isoformat(), "dateModified": it["when"].isoformat(),
          "image": [img], "inLanguage": "de-DE", "mainEntityOfPage": url, "description": desc,
          "author": {"@type": "Organization", "name": "Leonida News Network", "url": SITE},
          "publisher": {"@type": "Organization", "name": "Leonida News Network", "url": SITE,
                        "logo": {"@type": "ImageObject", "url": SITE + "icon-512.png"}}}
    fig = (f'<figure><img src="../{it["pic"][0]}" alt="{e(it["pic"][1])}" width="800" height="450"></figure>'
           if it["pic"] else "")
    more = "".join(f'<li><time>{o["when"]:%d.%m.}</time><a href="{o["id"]}.html">{e(o["title"])}</a></li>'
                   for o in latest if o is not it)[:6000]
    nav = ""
    if nxt or prev:
        nav = '<div class="nav">' + (f'<a href="{nxt["id"]}.html">← Neuere: {e(nxt["title"][:60])}</a>' if nxt else "<span></span>") \
            + (f'<a href="{prev["id"]}.html">Ältere: {e(prev["title"][:60])} →</a>' if prev else "") + "</div>"
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(it['title'])} | GTA 6 News | LNN</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Leonida News Network">
<meta property="og:title" content="{e(it['title'])}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:locale" content="de_DE">
<meta property="article:published_time" content="{it['when'].isoformat()}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#07070c">
<link rel="icon" href="../favicon.ico?v=2" sizes="48x48">
<link rel="icon" href="../favicon.svg?v=2" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png?v=2">
<link rel="alternate" type="application/rss+xml" title="LNN Liveticker" href="{SITE}feed.xml">
<link rel="stylesheet" href="../fonts/fonts.css?v=2">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<header class="top"><a class="logo" href="../"><i>LNN</i> Leonida News Network</a><a class="live" href="../#{it['id']}">Zum Liveticker</a></header>
<main>
<article>
<div class="meta">{stamp}<time datetime="{it['when'].isoformat()}">{fmt(it['when'])}</time></div>
<h1>{e(it['title'])}</h1>
<div class="body"><p>{it['body']}</p></div>
{fig}
{f'<p class="src">{it["srcs"]}</p>' if it['srcs'] else ''}
</article>
<a class="cta" href="../#{it['id']}">Alle GTA-6-News im Liveticker</a>
<a class="dc" href="https://discord.gg/5anXePGCPg" rel="noopener">💬 Diskutier mit: <b>#leonida-news</b> auf dem Xetcraft-Discord</a>
{nav}
<section class="more"><h2>Neueste Meldungen</h2><ul>{more}</ul></section>
</main>
<footer>Leonida News Network · GTA 6 News auf Deutsch, jede Meldung mit Quellenstempel · Inoffizielle Fanseite, nicht verbunden mit Rockstar Games oder Take-Two<br><a href="../impressum.html">Impressum</a> · <a href="../datenschutz.html">Datenschutz</a><a class="xc" href="https://xetcraft.de" title="Xetcraft – die Werkstatt von XetrovT2000"><span>Ein Projekt von</span><img src="../xetcraft-logo.png" width="95" height="22" alt="Xetcraft"></a></footer>
<script data-goatcounter="https://gta6-infoboard.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
"""


def build():
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    items = parse(src)
    out = ROOT / "n"
    out.mkdir(exist_ok=True)
    keep = set()
    latest = items[:8]
    for i, it in enumerate(items):
        nxt = items[i - 1] if i > 0 else None
        prev = items[i + 1] if i + 1 < len(items) else None
        f = out / f"{it['id']}.html"
        keep.add(f.name)
        new = page(it, prev, nxt, latest)
        if not f.exists() or f.read_text(encoding="utf-8") != new:
            f.write_text(new, encoding="utf-8", newline="\n")
    for f in out.glob("m-*.html"):
        if f.name not in keep:
            f.unlink()
    urls = [f"  <url><loc>{SITE}</loc><lastmod>{items[0]['when']:%Y-%m-%d}</lastmod><changefreq>hourly</changefreq></url>"]
    urls += [f"  <url><loc>{SITE}n/{it['id']}.html</loc><lastmod>{it['when']:%Y-%m-%d}</lastmod></url>" for it in items]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8", newline="\n")
    return items


if __name__ == "__main__":
    print(f"{len(build())} Meldungsseiten")
