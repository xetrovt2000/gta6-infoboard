"""Postet neue Ticker-Meldungen aus feed.xml automatisch an Bluesky und Discord.

Läuft als GitHub-Ablauf (.github/workflows/autopost.yml) nach jedem Push, der feed.xml ändert.
Schon gepostete Meldungen stehen in tools/autopost_posted.json (guid-Liste), damit nichts doppelt kommt.
Fehlt ein Geheimwert (BSKY_HANDLE/BSKY_APP_PASSWORD bzw. DISCORD_WEBHOOK_LEONIDA), wird dieser Kanal übersprungen.
Aufruf lokal ohne Posten: py tools/autopost.py --trocken
"""
import json, os, re, sys, time, html
import urllib.request, urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEED = os.path.join(ROOT, "feed.xml")
STATE = os.path.join(ROOT, "tools", "autopost_posted.json")
SITE = "https://leonida-news.de/"
MAX_PRO_LAUF = 5
UA = {"User-Agent": "LeonidaNewsAutopost/1.0 (+https://leonida-news.de)"}

# Farbe des Discord-Kastens je Stempel
FARBEN = {"Offiziell": 0x2ECC71, "Berichtet": 0x3498DB, "Gerücht": 0xF1C40F, "Leak": 0xE74C3C, "Korrektur": 0x9B59B6}


def http(url, data=None, headers=None, method=None, timeout=30):
    h = dict(UA, **(headers or {}))
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.headers.get("Content-Type", ""), r.read()


def lies_feed():
    root = ET.parse(FEED).getroot()
    items = []
    for it in root.iter("item"):
        items.append({
            "guid": it.findtext("guid"),
            "title": it.findtext("title") or "",
            "link": it.findtext("link") or SITE,
            "desc": it.findtext("description") or "",
            "date": it.findtext("pubDate") or "",
        })
    return items  # neueste zuerst


def zerlege(item):
    """Stempel, Titel ohne Stempel, Text ohne wiederholten Titel."""
    m = re.match(r"\[([^\]]+)\]\s*(.*)", item["title"])
    stempel, titel = (m.group(1), m.group(2)) if m else ("", item["title"])
    text = item["desc"].strip()
    if text.startswith(titel):
        text = text[len(titel):].lstrip(" .:")
    text = re.sub(r"\s*Zum Faktencheck$", "", text)
    return stempel, titel, text


def kuerze(s, n):
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def warte_auf_seite(url):
    """GitHub Pages braucht nach dem Push ein bis zwei Minuten."""
    for _ in range(20):
        try:
            st, _, body = http(url)
            if st == 200:
                return body.decode("utf-8", "replace")
        except urllib.error.HTTPError:
            pass
        except Exception:
            pass
        time.sleep(15)
    return ""


def og_bild(seite):
    m = re.search(r'property="og:image" content="([^"]+)"', seite) or re.search(r'og:image" content="([^"]+)"', seite)
    return html.unescape(m.group(1)) if m else SITE + "og.jpg"


# ---------- Bluesky ----------
class Bluesky:
    def __init__(self, handle, pw):
        st, _, b = http("https://bsky.social/xrpc/com.atproto.server.createSession",
                        json.dumps({"identifier": handle, "password": pw}).encode(),
                        {"Content-Type": "application/json"})
        s = json.loads(b)
        self.did, self.jwt = s["did"], s["accessJwt"]

    def blob(self, url):
        try:
            _, ctype, data = http(url)
            if len(data) > 950_000:
                return None
            _, _, b = http("https://bsky.social/xrpc/com.atproto.repo.uploadBlob", data,
                           {"Content-Type": ctype.split(";")[0] or "image/jpeg", "Authorization": "Bearer " + self.jwt})
            return json.loads(b)["blob"]
        except Exception as e:
            print("  Bild-Upload übersprungen:", e)
            return None

    def post(self, text, link, titel, beschreibung, bild_url):
        facets = []
        for tag in re.finditer(r"#(\w+)", text):
            start = len(text[: tag.start()].encode("utf-8"))
            end = len(text[: tag.end()].encode("utf-8"))
            facets.append({"index": {"byteStart": start, "byteEnd": end},
                           "features": [{"$type": "app.bsky.richtext.facet#tag", "tag": tag.group(1)}]})
        ext = {"uri": link, "title": titel, "description": kuerze(beschreibung, 280)}
        b = self.blob(bild_url) if bild_url else None
        if b:
            ext["thumb"] = b
        rec = {"$type": "app.bsky.feed.post", "text": text, "langs": ["de"],
               "createdAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
               "embed": {"$type": "app.bsky.embed.external", "external": ext}}
        if facets:
            rec["facets"] = facets
        http("https://bsky.social/xrpc/com.atproto.repo.createRecord",
             json.dumps({"repo": self.did, "collection": "app.bsky.feed.post", "record": rec}).encode(),
             {"Content-Type": "application/json", "Authorization": "Bearer " + self.jwt})


def bluesky_text(stempel, titel, text, countdown):
    if countdown:
        return f"⏳ {titel} bis GTA VI (19. November).\n\nAlle News mit Quellenstempel im Liveticker 👇\n\n#GTA6 #GTAVI"
    kopf = f"[{stempel}] {titel}" if stempel else titel
    fuss = "\n\n#GTA6 #GTAVI"
    rest = 295 - len(kopf) - len(fuss) - 2
    return kopf + ("\n\n" + kuerze(text, rest) if rest > 40 and text else "") + fuss


# ---------- Discord ----------
def discord_post(hook, stempel, titel, text, link, bild, countdown):
    if countdown:
        embed = {"title": f"⏳ {titel} bis GTA VI", "url": SITE, "color": 0xC24DFF,
                 "description": "Release am 19. November 2026. Alle Meldungen im Liveticker."}
    else:
        embed = {"title": kuerze((f"[{stempel}] " if stempel else "") + titel, 250), "url": link,
                 "description": kuerze(text, 400), "color": FARBEN.get(stempel, 0xC24DFF)}
        if bild:
            embed["image"] = {"url": bild}
    embed["footer"] = {"text": "Leonida News Network · leonida-news.de"}
    body = {"username": "Leonida News", "avatar_url": SITE + "icon-192.png", "embeds": [embed],
            "allowed_mentions": {"parse": []}}
    http(hook, json.dumps(body).encode(), {"Content-Type": "application/json"})


def main():
    trocken = "--trocken" in sys.argv
    items = lies_feed()
    if not os.path.exists(STATE):
        # Erster Lauf: alles Bestehende als erledigt markieren, nichts posten
        json.dump([i["guid"] for i in items], open(STATE, "w", encoding="utf-8"), indent=0)
        print("Startstand angelegt:", len(items), "Meldungen")
        return
    erledigt = set(json.load(open(STATE, encoding="utf-8")))
    neu = [i for i in items if i["guid"] not in erledigt][:MAX_PRO_LAUF][::-1]  # älteste zuerst
    if not neu:
        print("Nichts Neues.")
        return

    bsky = None
    if not trocken and os.environ.get("BSKY_HANDLE") and os.environ.get("BSKY_APP_PASSWORD"):
        bsky = Bluesky(os.environ["BSKY_HANDLE"], os.environ["BSKY_APP_PASSWORD"])
    hook = os.environ.get("DISCORD_WEBHOOK_LEONIDA") if not trocken else None
    if not trocken and not bsky and not hook:
        print("Keine Zugangsdaten hinterlegt – nichts gepostet, Stand bleibt.")
        return

    for it in neu:
        stempel, titel, text = zerlege(it)
        countdown = bool(re.fullmatch(r"Noch \d+ Tage?", titel))
        link = SITE if countdown else it["link"]
        seite = "" if (countdown or trocken) else warte_auf_seite(link)
        bild = og_bild(seite) if seite else (None if countdown else SITE + "og.jpg")
        btext = bluesky_text(stempel, titel, text, countdown)
        print("→", it["title"], "|", len(btext), "Zeichen")
        if trocken:
            print(btext, "\n")
            continue
        try:
            if bsky:
                bsky.post(btext, link, (f"[{stempel}] " if stempel else "") + titel if not countdown else "GTA 6 Liveticker – Leonida News",
                          text or "Countdown, News und Faktencheck zu GTA VI", bild or SITE + "og.jpg")
            if hook:
                discord_post(hook, stempel, titel, text, link, bild, countdown)
        except Exception as e:
            print("  Fehler:", e)  # trotzdem als erledigt markieren, sonst doppelt im anderen Kanal
        erledigt.add(it["guid"])
        time.sleep(3)

    if not trocken:
        alle = [i["guid"] for i in items if i["guid"] in erledigt]
        json.dump(alle, open(STATE, "w", encoding="utf-8"), indent=0)


if __name__ == "__main__":
    main()
