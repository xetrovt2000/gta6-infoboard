"""Erzeugt die Ratgeber-Seiten unter ratgeber/<slug>.html (feste Seiten zu Fragen, die Leute googeln).

Inhalt steht unten in GUIDES. Bei neuen Fakten: Text anpassen, STAND setzen, `py tools/build_guides.py`
(läuft auch automatisch über build_pages.py), dann IndexNow. Keine Gedankenstriche in den Texten.
"""
import html, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leonida-news.de/"
STAND = ("2026-11-24", "24. November 2026")

PSD = "https://store.playstation.com/de-de/product/EP1004-PPSA01547_00-GTAVIULTIMATE001"
R_PRE = "https://www.rockstargames.com/newswire/article/5171972o3ak5oa/pre-order-grand-theft-auto-vi-on-june-25"
R_LOAD = "https://www.rockstargames.com/newswire/article/k4ak9okk485712/grand-theft-auto-vi-pre-load-begins-on-november-10"
PS_LOAD = "https://blog.playstation.com/2026/11/03/grand-theft-auto-vi-pre-download-begins-november-10/"
VGC_LOAD = "https://www.videogameschronicle.com/news/rockstar-details-grand-theft-auto-6-pre-load-date-and-time-and-file-size/"
USK = "https://usk.de/digitaler-elternabend-gta-vi-ist-ab-18-was-eltern-wissen-mussen/"
PEGI = "https://store.playstation.com/en-gb/product/EP1004-PPSA01547_00-GTAVISTANDARD001"
R_VI = "https://www.rockstargames.com/VI"
SUP = "https://support.rockstargames.com/articles/29jV3Cv2cCgvwM1XgtMO5o/grand-theft-auto-vi-regional-pre-load-and-release-times-on-playstation-5-and-xbox-series-x-or-s"
GB = "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"
XCLOUD = "https://www.gosugamers.net/entertainment/news/79311-xbox-denies-claims-that-gta-vi-will-stream-exclusively-through-xbox-cloud-gaming"
POLY = "https://www.polygon.com/gta-6-preorders-sales-8-million-copies-before-release-date/"
R_NOW = "https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available"
XBOX_CLOUD = "https://news.xbox.com/en-us/2026/11/10/grand-theft-auto-6-comes-to-xbox-cloud-gaming-november-19/"
PS_STD = "https://store.playstation.com/de-de/product/EP1004-PPSA01547_00-GTAVISTANDARD001"


def q(url, name):
    return f'<a class="q" href="{url}" target="_blank" rel="noopener">{name}</a>'


T_OK = '<span class="tag t-ok">Offiziell</span>'
T_W = '<span class="tag t-warn">Berichtet</span>'
T_O = '<span class="tag t-bad">Offen</span>'

GUIDES = [
    {
        "slug": "gta-6-release-deutschland",
        "title": "GTA 6 Release in Deutschland: Datum, Uhrzeit, Preis",
        "h1": "GTA 6 Release in Deutschland: alles Wichtige",
        "desc": "GTA 6 ist am 19. November 2026 erschienen. Uhrzeit in Deutschland, Preise, Editionen, Download, USK und PC-Version, jede Angabe mit Quelle.",
        "lead": "GTA VI ist am <b>Donnerstag, 19. November 2026</b> um 0:00 Uhr Ortszeit für PlayStation 5 und Xbox Series X|S erschienen. Hier steht kompakt, was für Spieler in Deutschland wichtig ist. Jede Zeile trägt einen Stempel: <b>Offiziell</b> heißt von Rockstar, Sony, Microsoft oder der USK bestätigt, <b>Berichtet</b> heißt von seriösen Medien gemeldet, <b>Offen</b> heißt noch nicht bekannt.",
        "facts": [
            ("Release", f"{T_OK} Erschienen am Donnerstag, 19. November 2026 {q(R_NOW, 'Rockstar')}"),
            ("Plattformen", f"{T_OK} PlayStation 5 und Xbox Series X|S, PS5 Pro Enhanced {q(PSD, 'PS Store')}. Xbox One nur per Xbox Cloud Gaming {q(XBOX_CLOUD, 'Xbox')}"),
            ("Uhrzeit", f"{T_OK} 19. November, Mitternacht Ortszeit auf PS5 und Xbox, in Deutschland also 0:00 Uhr {q(SUP, 'Rockstar')}. Xbox Cloud Gaming ab 7:00 Uhr MEZ {q(XBOX_CLOUD, 'Xbox')}"),
            ("Download", f"{T_OK} Bis zu 212 GB. Der Vorab-Download für digitale Vorbestellungen lief ab 10. November {q(R_LOAD, 'Rockstar')} {q(PS_LOAD, 'PlayStation')}"),
            ("Preis", f"{T_OK} Standard 79,99 €, Ultimate Edition 99,99 € {q(PSD, 'PS Store')}"),
            ("Altersfreigabe", f"{T_OK} USK: keine Jugendfreigabe (ab 18) {q(USK, 'USK')}"),
            ("Wertungen", f"{T_W} Metacritic 99 (PS5, 151 Tests, alle positiv), OpenCritic 99 (90 Tests, 99 % Empfehlung), Stand 20. November {q('https://www.metacritic.com/game/grand-theft-auto-vi/', 'Metacritic')} {q('https://opencritic.com/game/15398/grand-theft-auto-vi', 'OpenCritic')}"),
            ("PC-Version", f"{T_O} Nicht angekündigt, Bericht über Anfang 2027 {q(GB, 'GamesBeat')}"),
        ],
        "sections": [
            ("Wann ging es los?",
             f"<p>Rockstar hat GTA VI am <b>19. November um Mitternacht Ortszeit</b> freigeschaltet, in allen Regionen und auf PS5 und Xbox gleichermaßen {q(SUP, 'Rockstar')} {q(R_NOW, 'Rockstar')}. In Deutschland war das in der Nacht von Mittwoch auf Donnerstag um <b>0:00 Uhr</b>.</p>"
             f"<p>Über Xbox Cloud Gaming läuft das Spiel seit dem 19. November, 7:00 Uhr MEZ. Das ist auch der einzige Weg für Xbox One {q(XBOX_CLOUD, 'Xbox')}.</p>"),
            ("Was kostet GTA 6?",
             f"<p>Die <b>Standard Edition kostet 79,99 €</b>, die <b>Ultimate Edition 99,99 €</b> {q(PSD, 'PS Store')} {q('https://store.rockstargames.com/de/game/buy-gta-vi', 'Rockstar Store')}. Die Ultimate Edition bringt zusätzliche Autos, Waffen, Kleidung und Läden. Ein Upgrade ist auch später möglich.</p>"
             f"<p>Die Box-Version im Handel enthält <b>keine Disc</b>, nur einen Download-Code. Sie kam am 12. November in die Läden {q(VGC_LOAD, 'VGC')}.</p>"
             f"<p>Die Vorbesteller-Aktion (Vintage Vice City Pack, bei digitalem Kauf zusätzlich ein Monat GTA+) ist <b>vorbei</b>: Sie lief nur bis zum 19. November {q(R_NOW, 'Rockstar')}. Das Vintage Vice City Pack wird jetzt einzeln für 4,99 € verkauft {q(PS_STD, 'PS Store')}.</p>"
             f"<p>Die Sammlerbox „The Goodtime State: Vice City Collection“ für 399,99 € enthält Figur, Brille, Cap und mehr, aber <b>nicht das Spiel</b>.</p>"),
            ("Wie groß ist der Download?",
             f"<p>Das Spiel braucht <b>bis zu 212 GB</b> {q(PS_LOAD, 'PlayStation')} {q(VGC_LOAD, 'VGC')}. Der Vorab-Download lief seit dem 10. November: auf der PS5 ab Mitternacht Ortszeit, auf der Xbox ab 1 Uhr deutscher Zeit. Alle Details stehen im <a href=\"gta-6-vorab-download.html\">Ratgeber zum Download</a>.</p>"),
            ("Ab welchem Alter ist GTA 6?",
             f"<p>Die USK hat GTA VI mit <b>keine Jugendfreigabe</b> gekennzeichnet, das Spiel ist also ab 18 {q(USK, 'USK')}. In Europa gilt PEGI 18, in den USA „Mature 17+“. Mehr dazu im <a href=\"gta-6-usk-ab-18.html\">Ratgeber zur Altersfreigabe</a>.</p>"),
            ("Kommt GTA 6 für den PC?",
             f"<p>Bisher <b>nicht angekündigt</b>. GamesBeat berichtet mit Berufung auf anonyme Quellen von einem PC-Start im ersten Quartal 2027 {q(GB, 'GamesBeat')}. Den <a href=\"gta-6-pc-version.html\">Stand zur PC-Version</a> halten wir aktuell.</p>"),
            ("Wie lang ist die Story, gibt es Online?",
             "<p>Rob Nelson von Rockstar North brauchte nach eigener Aussage rund <b>80 Stunden</b> für einen Story-Durchgang mit Nebenzielen. GTA VI ist ein Einzelspieler-Spiel und offline spielbar. Einen Online-Modus für GTA VI hat Rockstar nicht angekündigt, der PS Store nennt es ein Single-Player-Erlebnis {q(PSD, 'PS Store')}.</p>"
             f"<p>Vor dem Start schätzte Sensor Tower rund 7,7 Millionen digitale Vorbestellungen {q(POLY, 'Polygon')}. Rockstar selbst nennt keine Zahlen. Die Wertungen sind bisher sehr gut: Metacritic 99 (PS5, 151 Tests), OpenCritic 99 (90 Tests, 99 % Empfehlung).</p>"),
        ],
        "faq": [
            ("Wann ist GTA 6 erschienen?", "Am Donnerstag, 19. November 2026, für PlayStation 5 und Xbox Series X|S. Seit 7:00 Uhr MEZ läuft es auch über Xbox Cloud Gaming."),
            ("Um wie viel Uhr konnte man GTA 6 spielen?", "Ab dem 19. November um Mitternacht Ortszeit, auf PS5 und Xbox. In Deutschland also ab 0:00 Uhr."),
            ("Was kostet GTA 6?", "Die Standard Edition kostet 79,99 Euro, die Ultimate Edition 99,99 Euro."),
            ("Hat die GTA 6 Box-Version eine Disc?", "Nein. Die Box-Version enthält nur einen Download-Code und kam am 12. November in den Handel."),
            ("Kommt GTA 6 für den PC?", "Eine PC-Version ist nicht angekündigt. Berichte nennen das erste Quartal 2027, bestätigt ist das nicht."),
        ],
    },
    {
        "slug": "gta-6-vorab-download",
        "title": "GTA 6 Download: Größe (212 GB) und Speicherplatz",
        "h1": "GTA 6 laden: wie groß, wie viel Platz",
        "desc": "GTA 6 Download: bis zu 212 GB, so machst du Platz. Der Vorab-Download lief seit 10. November, PS5 ab Mitternacht, Xbox ab 1 Uhr deutscher Zeit. Mit Quellen.",
        "lead": "GTA VI ist seit dem 19. November erschienen und braucht <b>bis zu 212 GB</b> Speicher. Wer digital vorbestellt hatte, konnte schon <b>ab dem 10. November</b> vorab laden, neun Tage vor dem Start.",
        "facts": [
            ("Vorab-Download PS5", f"{T_OK} Lief ab 10. November, 0:00 Uhr Ortszeit {q(PS_LOAD, 'PlayStation')}"),
            ("Vorab-Download Xbox", f"{T_OK} Lief ab 10. November, 0:00 Uhr britische Zeit, also 1:00 Uhr in Deutschland {q(VGC_LOAD, 'VGC')}"),
            ("Größe", f"{T_OK} Bis zu 212 GB, je nach Gerät {q(R_LOAD, 'Rockstar')}"),
            ("Freier Speicher", f"{T_OK} Sony rät zu mindestens 212 GB freiem Platz {q(PS_LOAD, 'PlayStation')}"),
            ("Wer durfte vorladen", f"{T_OK} Digitale Vorbestellungen {q(PS_LOAD, 'PlayStation')}"),
            ("Box-Version", f"{T_OK} Nur Download-Code, im Handel seit 12. November {q(VGC_LOAD, 'VGC')}"),
            ("Spielbar seit", f"{T_OK} 19. November, 0:00 Uhr auf PS5 und Xbox {q(SUP, 'Rockstar')}"),
        ],
        "sections": [
            ("So funktioniert der Download",
             "<p>Auf der <b>PS5</b> startet der Download nach dem Kauf im PlayStation Store automatisch, wenn die Konsole im Ruhemodus mit dem Internet verbunden ist und automatische Downloads eingeschaltet sind. Sonst findest du GTA VI in der Spielebibliothek unter „Gekauft“ und startest den Download dort.</p>"
             "<p>Auf der <b>Xbox Series X|S</b> erscheint das Spiel nach dem Kauf unter „Meine Spiele und Apps“ in der Warteschlange. Läuft der Download nicht von selbst an, dort auf Installieren gehen.</p>"
             "<p>Spielen lässt sich GTA VI seit dem 19. November. Auch wer vorgeladen hat, kann noch ein Update brauchen, plane dafür etwas Zeit ein.</p>"),
            ("Reicht mein Speicher?",
             "<p>212 GB sind viel. Auf einer PS5 mit 825 GB bleiben nach dem System nur gut 660 GB frei, auf der Xbox Series S mit 512 GB rund 360 GB. Mach also vorher Platz:</p>"
             "<ul class=\"pts\"><li>Große Spiele, die du gerade nicht spielst, löschen. Spielstände liegen in der Cloud oder bleiben auf der Konsole.</li>"
             "<li>PS4-Spiele und ältere Xbox-Spiele auf eine externe USB-Festplatte verschieben.</li>"
             "<li>Eine M.2-SSD in der PS5 oder eine Speichererweiterungskarte für die Xbox schafft dauerhaft Platz.</li></ul>"),
            ("Was ist mit der Box-Version?",
             f"<p>Die Box im Handel enthält <b>keine Disc</b>, nur einen Code. Sie kam am 12. November in die Läden {q(VGC_LOAD, 'VGC')}. Laut Rockstar erschien sie so früh, damit auch Box-Käufer vorab laden konnten: Code einlösen, dann startete der Download wie bei der digitalen Fassung {q(R_PRE, 'Rockstar')}. Vorladen ging damit ab dem 12. November, digital schon ab dem 10.</p>"
             "<p>Alles andere zum Start, also Preis, Editionen und Uhrzeit, steht im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>.</p>"),
        ],
        "faq": [
            ("Wann konnte man GTA 6 vorladen?", "Ab dem 10. November 2026. Auf der PS5 ab Mitternacht Ortszeit, auf der Xbox ab 1 Uhr deutscher Zeit. Seit dem Release am 19. November lädst du es ganz normal."),
            ("Wie groß ist GTA 6?", "Rockstar nennt bis zu 212 GB, je nach Gerät. Sony rät, mindestens 212 GB freizumachen."),
            ("Kann man mit der Box-Version vorladen?", "Ja. Die Box enthält einen Download-Code und kam am 12. November in den Handel, laut Rockstar extra so früh, damit man vorladen konnte. Digital ging es schon ab dem 10. November."),
            ("Kann man GTA 6 nach dem Download spielen?", "Ja. Seit dem Release am 19. November um 0 Uhr Ortszeit ist es spielbar. Nach dem Vorab-Download kann noch ein Update nötig sein."),
        ],
    },
    {
        "slug": "gta-6-usk-ab-18",
        "title": "GTA 6 USK: ab 18, keine Jugendfreigabe",
        "h1": "GTA 6 und die USK: ab 18",
        "desc": "GTA 6 hat in Deutschland keine Jugendfreigabe (USK ab 18). Was das beim Kauf bedeutet, PEGI und ESRB im Vergleich, deutsche Sprache. Mit Quellen.",
        "lead": "Die Unterhaltungssoftware Selbstkontrolle hat GTA VI mit <b>keine Jugendfreigabe</b> gekennzeichnet. Das Spiel ist in Deutschland also <b>ab 18</b>.",
        "facts": [
            ("Deutschland (USK)", f"{T_OK} Keine Jugendfreigabe, ab 18 {q(USK, 'USK')}"),
            ("Europa (PEGI)", f"{T_OK} PEGI 18 {q(PEGI, 'PS Store')}"),
            ("USA (ESRB)", f"{T_OK} Mature 17+, mit Hinweis „In-Game Purchases“ {q(R_VI, 'Rockstar')}"),
            ("Deutsche Texte", f"{T_OK} Deutsch steht bei den unterstützten Sprachen {q(PSD, 'PS Store')}"),
            ("Deutsche Sprachausgabe", f"{T_O} Von Rockstar nicht bestätigt"),
        ],
        "sections": [
            ("Was heißt „keine Jugendfreigabe“?",
             f"<p>Das ist das höchste Alterskennzeichen der USK. Händler dürfen das Spiel nur an Volljährige verkaufen, im Laden wird nach dem Ausweis gefragt. Bei Online-Händlern und im Store der Konsole greift die Altersprüfung des Kontos.</p>"
             f"<p>Warum GTA VI keine Jugendfreigabe hat, erklärt die USK bei einem digitalen Elternabend am 2. Dezember {q(USK, 'USK')}. Weltweit liegt das Spiel überall in der höchsten Stufe: PEGI 18 in Europa, Mature 17+ in den USA, R 18+ in Australien.</p>"),
            ("Ist GTA 6 in Deutschland geschnitten?",
             "<p>Dazu gibt es keine Aussage von Rockstar oder der USK. GTA V erschien in Deutschland ungeschnitten. Nutzer haben aus Store-Daten gelesen, dass die Xbox-Fassung für die EU dieselbe wie für die USA sein soll. Das ist nicht bestätigt, sobald es belastbare Angaben gibt, tragen wir sie hier ein.</p>"),
            ("Gibt es GTA 6 auf Deutsch?",
             f"<p>Deutsch steht im PlayStation Store bei den unterstützten Sprachen {q(PSD, 'PS Store')}. Ob das auch eine deutsche Sprachausgabe meint oder wie bei früheren Teilen nur Texte und Untertitel, hat Rockstar nicht gesagt.</p>"
             "<p>Release, Uhrzeit und Preise stehen im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>.</p>"),
        ],
        "faq": [
            ("Ab wie viel Jahren ist GTA 6?", "In Deutschland hat GTA 6 von der USK keine Jugendfreigabe bekommen, es ist also ab 18. In Europa gilt PEGI 18."),
            ("Ist GTA 6 in Deutschland uncut?", "Dazu gibt es noch keine Angabe von Rockstar oder der USK. GTA V erschien in Deutschland ungeschnitten."),
            ("Hat GTA 6 eine deutsche Sprachausgabe?", "Deutsch wird als Sprache unterstützt. Ob es eine deutsche Sprachausgabe gibt oder nur deutsche Texte, hat Rockstar nicht bestätigt."),
        ],
    },
    {
        "slug": "gta-6-pc-version",
        "title": "GTA 6 PC-Version: Release und aktueller Stand",
        "h1": "Kommt GTA 6 für den PC?",
        "desc": "GTA 6 PC: Rockstar hat noch keine PC-Version angekündigt. Was Berichte sagen (Anfang 2027), was es mit Xbox Cloud Gaming auf sich hat und was du jetzt tun kannst.",
        "lead": "GTA VI ist am 19. November <b>nur für PlayStation 5 und Xbox Series X|S</b> erschienen, dazu per Xbox Cloud Gaming. Eine PC-Version hat Rockstar bisher nicht angekündigt.",
        "facts": [
            ("PC-Version", f"{T_O} Von Rockstar nicht angekündigt"),
            ("Bericht", f"{T_W} PC-Start im ersten Quartal 2027, laut vier anonymen Quellen {q(GB, 'GamesBeat')}"),
            ("Xbox Cloud Gaming", f"{T_OK} Seit 19. November, 7:00 Uhr MEZ, auch für Xbox One. Eine PC-Version ist das nicht {q(XBOX_CLOUD, 'Xbox')}"),
            ("Konsolen", f"{T_OK} PS5 und Xbox Series X|S seit 19. November {q(R_NOW, 'Rockstar')}"),
        ],
        "sections": [
            ("Was ist bekannt?",
             f"<p>Rockstar spricht offiziell nur von PS5 und Xbox Series X|S. GamesBeat berichtete am 13. Oktober, der PC-Start sei für Januar bis März 2027 geplant, die PC-Fassung müsse vorher dieselbe Qualitätsprüfung bestehen wie die Konsolenversion {q(GB, 'GamesBeat')}. Bestätigt hat Rockstar das nicht.</p>"
             "<p>Bei früheren Teilen kam der PC deutlich später: GTA V erschien gut anderthalb Jahre nach der Konsolenfassung, Red Dead Redemption 2 rund ein Jahr danach.</p>"),
            ("Gibt es GTA 6 per Cloud?",
             f"<p>Ja, aber nicht als PC-Version: Xbox Cloud Gaming bietet GTA VI seit dem 19. November, 7:00 Uhr MEZ, an. Xbox One kann es nur so spielen {q(XBOX_CLOUD, 'Xbox')}. Welche Geräte unterstützt werden, nennt Microsoft in der Ankündigung. Ein Bericht über exklusive Streaming-Rechte war am 7. Oktober von Xbox zurückgewiesen worden {q(XCLOUD, 'GosuGamers')}.</p>"),
            ("Was heißt das für PC-Spieler?",
             "<p>Wer jetzt spielen will, braucht eine PS5, eine Xbox Series X|S oder Xbox Cloud Gaming. Wer warten kann, sollte nichts für den PC vorbestellen, solange es keine offizielle Ankündigung gibt: Angebote für „GTA 6 PC Keys“ sind derzeit unseriös.</p>"
             "<p>Alles zum Konsolen-Release steht im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>. Neue Infos zur PC-Version landen zuerst in unserem <a href=\"../\">Liveticker</a>.</p>"),
        ],
        "faq": [
            ("Kommt GTA 6 für den PC?", "Rockstar hat noch keine PC-Version angekündigt. GamesBeat berichtet von einem PC-Start im ersten Quartal 2027."),
            ("Kann man GTA 6 am PC streamen?", "Seit dem 19. November gibt es GTA 6 bei Xbox Cloud Gaming. Welche Geräte das unterstützt, nennt Microsoft in der Ankündigung. Eine PC-Version ist es nicht."),
            ("Kann man GTA 6 für den PC schon kaufen?", "Nein. Es gibt keine offizielle PC-Version, Angebote für PC-Keys sind unseriös."),
        ],
    },
]

R_SITE = "https://www.rockstargames.com/VI"
R_MUSIC = "https://www.rockstargames.com/VI/music"
R_RADIO = "https://www.rockstargames.com/newswire/article/o3982oa93a23k4/the-music-of-grand-theft-auto-vi-in-game-radio-stations"
R_ALBUM = "https://www.rockstargames.com/newswire/article/7599a881942544/announcing-grand-theft-auto-vi-the-album-coming-november-19"
SCORE = "https://www.musicweek.com/labels/read/rockstar-games-and-justice-unveil-grand-theft-auto-vi-original-score/095363"
EDGE = "https://www.vice.com/en/article/gta-6-edge-magazine-new-screenshots-features/"
WELT = "../#welt"
GAL = "../#galerie"
CHAR = "../#charaktere"
IGN = "../#ign"
R_MEDIA = "https://www.rockstargames.com/VI/media/screenshots"
TGA = "https://www.cbc.ca/news/entertainment/game-of-the-year-9.7425430"

GUIDES += [
    {
        "slug": "gta-6-charaktere",
        "title": "GTA 6 Charaktere: Jason, Lucia und alle Nebenfiguren",
        "h1": "GTA 6 Charaktere: wer ist wer?",
        "desc": "Alle bekannten GTA 6 Charaktere: Jason Duval, Lucia Caminos und sechs Nebenfiguren mit Steckbrief, dazu was über Beziehung und Story bekannt ist. Mit Quellen.",
        "lead": "In GTA VI spielt man zum ersten Mal ein Paar: <b>Jason Duval</b> und <b>Lucia Caminos</b>. Rockstar hat dazu bisher <b>sechs Nebenfiguren</b> vorgestellt. Hier stehen alle mit kurzem Steckbrief.",
        "facts": [
            ("Hauptfiguren", f"{T_OK} Jason Duval und Lucia Caminos, man wechselt zwischen beiden {q(R_SITE, 'Rockstar')}"),
            ("Nebenfiguren", f"{T_OK} Cal Hampton, Brian Heder, Raul Bautista, Boobie Ike, Dre’Quan Priest, Real Dimez {q(R_MEDIA, 'Rockstar')}"),
            ("Bilder", f"{T_OK} 19 offizielle Bilder von Jason, 14 von Lucia, 20 vom Paar, je 4 pro Nebenfigur <a class=\"q\" href=\"{GAL}\">Galerie</a>"),
            ("Sprecher", f"{T_OK} Lucia: Manni L. Perez, bestätigt durch ihre Nominierung bei den Game Awards {q(TGA, 'CBC')}. Weitere Besetzung hat Rockstar nicht veröffentlicht"),
        ],
        "sections": [
            ("Jason Duval",
             "<p>Armeeveteran, der sein Leben lang von Kriminellen umgeben war. Zu Beginn arbeitet er für Drogenschmuggler in den Leonida Keys.</p>"),
            ("Lucia Caminos",
             "<p>Stammt aus Liberty City und wurde von ihrem Vater im Kampfsport trainiert. Sie saß im Leonida Penitentiary und will nach der Entlassung endlich das gute Leben. Ihre <b>Fußfessel</b> spielt laut Rockstar in der Geschichte eine wichtige Rolle.</p>"
             f"<p>Gespielt wird Lucia von <b>Manni L. Perez</b>. Das ist seit dem 17. November offiziell: Die Game Awards haben sie für GTA VI in der Kategorie beste Darstellung nominiert {q(TGA, 'CBC')}. Fans hatten das lange vermutet.</p>"),
            ("Die Nebenfiguren",
             "<ul class=\"pts\">"
             "<li><b>Cal Hampton:</b> Jasons verpeilter, etwas paranoider Kumpel mit Hang zu Verschwörungstheorien.</li>"
             "<li><b>Brian Heder:</b> alter Drogenschmuggler und einer der wichtigsten Auftraggeber. Jason wohnt mietfrei in einem seiner Häuser.</li>"
             "<li><b>Raul Bautista:</b> charmanter, erfahrener Bankräuber, der Jason und Lucia als Fluchtfahrer anheuert.</li>"
             "<li><b>Boobie Ike:</b> Unternehmer aus Vice City mit Immobilien, Musik und krummen Geschäften.</li>"
             "<li><b>Dre’Quan Priest:</b> ehrgeiziger Macher beim Musiklabel Only Raw Records.</li>"
             "<li><b>Real Dimez:</b> Bae-Luxe und Roxy, ein Rap-Duo mit einem einzigen Hit, das seinen Ruhm zurückwill. Unter Vertrag bei Only Raw Records.</li>"
             f"</ul><p>Brian Heder wird laut Game Informer von Schauspieler <b>Stephen Root</b> gesprochen, das hat er dort selbst gesagt. Rockstar bestätigt die Besetzung nicht. Ausführlich mit allen Bildern in unserem Bereich <a href=\"{CHAR}\">Charaktere</a>.</p>"),
            ("Was über das Paar bekannt ist",
             f"<p>Aus einem Interview mit IGN {q(IGN, 'IGN')}:</p><ul class=\"pts\">"
             "<li>Der Partner kann das Steuer übernehmen, man fährt dann mit oder schießt vom Beifahrersitz.</li>"
             "<li>Die beiden schreiben und telefonieren miteinander, auch über Alltägliches. Ignorierte Nachrichten schaden der Beziehung ein wenig.</li>"
             "<li>Wer die Figur wechselt, platzt mitten in den Alltag des anderen.</li>"
             "<li>Die Beziehung hat ein eigenes System, getrennt davon, was für ein Verbrecher man ist.</li>"
             "<li>Wird ein Partner verhaftet, während der andere flieht, ist er festgenommen.</li>"
             "<li>Kleine Entscheidungen in der Story wirken lange nach.</li></ul>"
             "<p>Wie groß die Welt ist, in der die beiden unterwegs sind, steht im <a href=\"gta-6-karte-leonida.html\">Ratgeber zur Karte</a>.</p>"),
        ],
        "faq": [
            ("Wer sind die Hauptfiguren in GTA 6?", "Jason Duval und Lucia Caminos. Man spielt beide und kann zwischen ihnen wechseln."),
            ("Wer ist Lucia in GTA 6?", "Lucia Caminos stammt aus Liberty City, wurde von ihrem Vater im Kampfsport trainiert und saß im Leonida Penitentiary. Ihre Fußfessel spielt in der Story eine wichtige Rolle."),
            ("Wer spielt Lucia in GTA 6?", "Manni L. Perez. Bestätigt ist das seit ihrer Nominierung für die beste Darstellung bei den Game Awards 2026 am 17. November."),
            ("Wer ist Jason in GTA 6?", "Jason Duval ist ein Armeeveteran, der zu Beginn für Drogenschmuggler in den Leonida Keys arbeitet."),
            ("Welche Nebenfiguren gibt es in GTA 6?", "Bisher vorgestellt: Cal Hampton, Brian Heder, Raul Bautista, Boobie Ike, Dre’Quan Priest und das Rap-Duo Real Dimez."),
        ],
    },
]

GUIDES += [
    {
        "slug": "gta-6-editionen",
        "title": "GTA 6 Editionen: Standard oder Ultimate Edition?",
        "h1": "GTA 6 Editionen im Vergleich",
        "desc": "GTA 6 Standard für 79,99 € oder Ultimate Edition für 99,99 €? Alle Inhalte der Ultimate Edition, das Vintage Vice City Pack und GTA+, mit Quellen.",
        "lead": "GTA VI gibt es in zwei Editionen: <b>Standard für 79,99 €</b> und <b>Ultimate für 99,99 €</b>. Das <b>Vintage Vice City Pack</b> gab es nur als Vorbesteller-Bonus bis 19. November und es kostet jetzt einzeln 4,99 €. Hier steht, was genau drin ist.",
        "facts": [
            ("Standard Edition", f"{T_OK} 79,99 €, das komplette Spiel {q(PSD, 'PS Store')}"),
            ("Ultimate Edition", f"{T_OK} 99,99 €, Spiel plus Zusatzinhalte, Upgrade auch später möglich {q(PSD, 'PS Store')}"),
            ("Vorbesteller-Bonus", f"{T_OK} Vorbei: Das Vintage Vice City Pack gab es bis 19. November, jetzt einzeln für 4,99 € {q(R_NOW, 'Rockstar')} {q(PS_STD, 'PS Store')}"),
            ("GTA+", f"{T_OK} Der Gratismonat bei digitaler Vorbestellung ist mit dem 19. November ausgelaufen {q(R_NOW, 'Rockstar')}"),
            ("Box-Version", f"{T_OK} Download-Code statt Disc, seit 12. November im Handel {q(R_PRE, 'Rockstar')}"),
            ("Sammlerbox", f"{T_OK} 399,99 €, ohne Spiel"),
        ],
        "sections": [
            ("Was steckt in der Ultimate Edition?",
             f"<p>Laut Rockstar sind die Inhalte über die ganze Geschichte von Jason und Lucia verteilt, mit jedem Kapitel kommt etwas Neues dazu {q(R_SITE, 'Rockstar')}. Einige Läden öffnen <b>nur</b> mit der Ultimate Edition.</p>"
             "<ul class=\"pts\">"
             "<li><b>’95 Grotti Cheetah:</b> Sportwagen im Retro-Look der 90er.</li>"
             "<li><b>Revolver Hawk und Little Morgan:</b> je einer für Jason und Lucia, im Vice-City-Stil mit Palmengriff und Zielfernrohr.</li>"
             "<li><b>Persönliche Pistolen:</b> gravierte Fassungen von Jasons Girardi ES9 und Lucias Klose K17.</li>"
             "<li><b>Vice City Style:</b> eigene Outfits, Tattoos und mehr für beide.</li>"
             "<li><b>Fahrzeuge fürs Versteck:</b> Motorrad Dinka Enduro in Tarnfarben und ein Crest-Kajak.</li>"
             "<li><b>Ganado Retro Build:</b> Umbauten für Jasons Pick-up Vapid Ganado.</li>"
             "<li><b>Rideout Customs:</b> Tuning-Werkstatt mit Felgen und Innenausstattung, nur mit Ultimate.</li>"
             "<li><b>Sara’s Unisex Salon:</b> Frisuren, Bärte, Make-up und Nägel, nur mit Ultimate.</li>"
             "<li><b>Shitzu Squalo:</b> Boot in Pink und Blau mit einer Kiste Sprengstoff an Bord.</li>"
             "<li><b>Stock 305:</b> Streetwear-Laden in Stockyard, nur mit Ultimate.</li>"
             "<li><b>’67 Vapid Dominator Buggy</b> samt Paradise Garage in Watson Bay mit Waffenschrank und Hehlerlager.</li>"
             "<li><b>Electric Fang Tattoo:</b> über 50 Motive des Künstlerkollektivs FAILE, nur mit Ultimate.</li>"
             "<li><b>One-Eyed Willie’s:</b> Offroad-Werkstatt am Lake Leonida, nur mit Ultimate.</li>"
             "<li><b>Goodtime Gear:</b> Kleidung rund um das TV-Maskottchen Macca the Gator.</li>"
             "<li><b>PTT Youngin$:</b> ein Gang-Gelände in Southside Vice City zum Ausrauben.</li>"
             "<li><b>Classic Car Collection:</b> Auftrag vom Sammler Wyman, verlassene Oldtimer aufspüren und herrichten.</li>"
             f"</ul><p>Alle 47 offiziellen Bilder dazu stehen in unserer <a href=\"{GAL}\">Galerie</a> unter „Ultimate Edition“.</p>"),
            ("Was ist im Vintage Vice City Pack?",
             f"<p>Das Paket war bis 19. November bei allen Käufen und Vorbestellungen dabei, egal welche Edition {q(R_PRE, 'Rockstar')}. Jetzt wird es einzeln für <b>4,99 €</b> verkauft {q(PS_STD, 'PS Store')}. Der Inhalt:</p>"
             "<ul class=\"pts\"><li><b>’55 Vapid Stanier:</b> Oldtimer-Limousine samt Garage Shore Court an Ocean Beach, mit Waffenschrank und Hehlerlager.</li>"
             "<li><b>Outfits und Frisuren:</b> Jason im Leinenanzug in Pastell, Lucia im roten Paillettenkleid.</li>"
             "<li><b>Waffenmuster:</b> Palmen-Muster nach Tommy Vercettis Hemd aus GTA Vice City.</li></ul>"),
            ("Lohnt sich die Ultimate Edition?",
             "<p>Für 20 € mehr gibt es kein zusätzliches Story-Kapitel, aber spürbar mehr Spielwelt: ein Salon, ein Klamottenladen, ein Tattoo-Studio und zwei Werkstätten öffnen nur damit, dazu Fahrzeuge, ein Bandengelände und ein Sammelauftrag. Wer viel Zeit in Leonida verbringen will, bekommt also mehr zu tun. Wer nur die Geschichte spielen will, verpasst nichts Wesentliches.</p>"
             "<p>Gut zu wissen: Das Upgrade lässt sich auch später kaufen. Man kann also mit der Standard Edition starten und erst danach entscheiden. Das gilt laut Rockstar auch für die Box: Die Ultimate Edition gibt es nicht als Box, das Upgrade lässt sich aber nach dem Einlösen des Codes im PlayStation Store oder bei Xbox nachkaufen.</p>"
             "<p>Uhrzeit, Download und Altersfreigabe stehen im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>.</p>"),
        ],
        "faq": [
            ("Was kostet die GTA 6 Ultimate Edition?", "99,99 Euro. Die Standard Edition kostet 79,99 Euro."),
            ("Was ist in der GTA 6 Ultimate Edition enthalten?", "Unter anderem ein Grotti Cheetah, zwei Revolver, ein Boot, ein Buggy mit Garage, eigene Outfits und Tattoos sowie mehrere Läden und Werkstätten, die nur mit der Ultimate Edition öffnen."),
            ("Kann man später auf die Ultimate Edition upgraden?", "Ja, laut PlayStation Store ist ein Upgrade auch später möglich."),
            ("Wie bekomme ich das Vintage Vice City Pack?", "Die Vorbesteller-Aktion lief bis 19. November 2026 und ist vorbei. Seitdem wird das Pack einzeln für 4,99 Euro verkauft."),
        ],
    },
    {
        "slug": "gta-6-karte-leonida",
        "title": "GTA 6 Karte: Leonida, Vice City und alle Regionen",
        "h1": "GTA 6 Karte: Leonida und seine Regionen",
        "desc": "Wie groß ist die GTA 6 Karte? Leonida, Vice City und alle sechs Regionen, Tiere, Wetter und Hurrikane. Nur Bestätigtes, mit Quellen.",
        "lead": "GTA VI spielt im Bundesstaat <b>Leonida</b>, Rockstars Version von Florida, mit der Großstadt <b>Vice City</b>. Laut Rockstar ist es die <b>größte Karte, die das Studio je gebaut hat</b>.",
        "facts": [
            ("Schauplatz", f"{T_OK} Bundesstaat Leonida nach dem Vorbild Floridas {q(R_SITE, 'Rockstar')}"),
            ("Größe", f"{T_OK} Doppelt so groß wie GTA V (Aaron Garbut) <a class=\"q\" href=\"{WELT}\">Game Informer</a>"),
            ("Vergleich", f"{T_W} Fast so groß wie die Karten von GTA IV, GTA V und Red Dead Redemption 2 zusammen {q(EDGE, 'Edge via VICE')}"),
            ("Regionen", f"{T_OK} Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia, Mount Kalaga <a class=\"q\" href=\"{WELT}\">Game Informer</a>"),
            ("Tiere", f"{T_OK} Über 170 Arten <a class=\"q\" href=\"../#tiere\">Game Informer</a>"),
            ("Wetter", f"{T_OK} Örtlich begrenzt, mit Tropenstürmen und Hurrikanen <a class=\"q\" href=\"../#wetter\">Game Informer</a>"),
        ],
        "sections": [
            ("Die sechs Regionen",
             "<ul class=\"pts\">"
             "<li><b>Vice City:</b> Art déco, Strände, Kreuzfahrthafen und Staus, die Verfolgungsjagden schwerer machen.</li>"
             "<li><b>Leonida Keys:</b> die Inselkette im Süden, Vorbild sind die Florida Keys.</li>"
             "<li><b>Grassrivers:</b> Sumpfland nach Art der Everglades, voller Raubtiere und bewaffneter Einheimischer.</li>"
             "<li><b>Port Gellhorn:</b> verlassene Attraktionen, billige Motels und Einkaufszeilen.</li>"
             "<li><b>Ambrosia:</b> das Industrieherz mit Fabriken und Raffinerien, eine Rockergang hat das Sagen.</li>"
             "<li><b>Mount Kalaga National Park:</b> im Norden an der Grenze zum Nachbarstaat Leonida-Gloriana.</li>"
             f"</ul><p>Quelle sind die Rockstar-Interviews im Game Informer, ausführlich in unserem <a href=\"{WELT}\">Magazin-Teil</a>. Zu jeder Region gibt es offizielle Bilder in der <a href=\"{GAL}\">Galerie</a>.</p>"),
            ("Was gibt es auf dem Land zu tun?",
             "<p>Rockstar nennt Quad-Strecken, Schlammpartys, Demolition Derbys bei Flutlicht, Mountainbike-Trails, Farmen und Ranches, einen Golfplatz, Motocross in den Dünen und Barschangeln. Vorbilder für die Gegenden waren unter anderem Panama City, Jacksonville und Ocala.</p>"
             "<p>Laut Rockstar gibt es außerdem deutlich mehr begehbare Innenräume als in früheren Teilen.</p>"),
            ("Tiere und Wetter",
             "<p>Leonida hat <b>über 170 Tierarten</b>, darunter Alligatoren, Seekühe, Flamingos, Haie, Wale und eingeschleppte Arten wie Leguane und Rhesusaffen. Wie in Red Dead Redemption lassen sich Tiere aufspüren, eingeteilt in selten, entdeckbar und legendär.</p>"
             "<p>Das Wetter ist <b>örtlich begrenzt</b>: Man kann in der Sonne stehen, während nebenan ein Schauer niedergeht. Es gibt Tropenstürme und <b>Hurrikane</b>, Pfützen bleiben nach dem Regen liegen.</p>"
             f"<p>Seit dem Release am 19. November gibt es die offizielle Karte: Rockstar bietet auf der offiziellen Seite ein druckfertiges Poster mit der Karte von Leonida und dem Cover zum kostenlosen Download an <a class=\"q\" href=\"https://www.rockstargames.com/VI/media\" target=\"_blank\" rel=\"noopener\">Rockstar</a>. Eine gedruckte Fassung soll bald im Rockstar Store folgen.</p>"),
        ],
        "faq": [
            ("Wie groß ist die GTA 6 Karte?", "Laut Rockstar ist Leonida die größte Karte des Studios, doppelt so groß wie die von GTA V. Das Magazin Edge schreibt, sie sei fast so groß wie die Karten von GTA IV, GTA V und Red Dead Redemption 2 zusammen."),
            ("Wo spielt GTA 6?", "Im fiktiven Bundesstaat Leonida nach dem Vorbild Floridas, mit der Großstadt Vice City nach dem Vorbild Miamis."),
            ("Welche Regionen gibt es in GTA 6?", "Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia und den Mount Kalaga National Park."),
            ("Gibt es in GTA 6 Hurrikane?", "Ja. Rockstar bestätigt Tropenstürme und Hurrikane mit Sturm, Starkregen, Donner und Blitz."),
        ],
    },
    {
        "slug": "gta-6-soundtrack-radio",
        "title": "GTA 6 Soundtrack: Album, Radiosender und Score",
        "h1": "GTA 6 Musik: Album, Radio und Filmmusik",
        "desc": "GTA 6 Soundtrack: The Album mit 34 Songs seit 19. November, Filmmusik von Justice am 11. Dezember, alle bekannten Singles und Radiosender. Mit Quellen.",
        "lead": "Zu GTA VI gibt es zwei Alben: <b>„Grand Theft Auto VI: The Album“</b> mit 34 neuen Songs, erschienen am 19. November, und die <b>Filmmusik von Justice</b>, die am 11. Dezember folgt. Im Spiel kommt die größte Radioauswahl der Reihe dazu.",
        "facts": [
            ("The Album", f"{T_OK} 34 neue Songs, erschienen am 19. November {q(R_ALBUM, 'Rockstar')}"),
            ("Original Score", f"{T_OK} Justice, 30 Stücke plus Bonus-Tracks, erscheint am 11. Dezember {q(R_MUSIC, 'Rockstar')}"),
            ("Radio", f"{T_OK} Größte Radioauswahl der Reihe, erstmals mit Podcasts {q(R_RADIO, 'Rockstar')}"),
            ("Vinyl und CD", f"{T_OK} Beide Alben gibt es laut Rockstars Musikseite auch auf Vinyl und CD {q(R_MUSIC, 'Rockstar')}"),
        ],
        "sections": [
            ("Die Singles von „The Album“",
             f"<p>Diese Songs gab es schon vorab {q(R_MUSIC, 'Rockstar')}:</p><ul class=\"pts\">"
             "<li>Yung Lean: „That’s It“ (feat. Future und Metro Boomin)</li>"
             "<li>Travis Scott: „RHYNO“</li>"
             "<li>CA7RIEL und Paco Amoroso, PinkPantheress, Fred again.. und Etienne de Crécy: „Sexy Magic“</li>"
             "<li>Justice: „Flower in a Hurricane“ (feat. Tame Impala, SZA, King Gizzard und The Lizard Wizard), der Song aus dem Launch-Trailer</li>"
             "<li>Morgan Wallen: „Last Thing You Need“</li>"
             "<li>Fuerza Regida: „Suzuki“</li>"
             "<li>Rauw Alejandro: „Macacoa 2000“</li>"
             "<li>Cardi B: „Don’t Chart“</li>"
             "<li>Keith Richards: „Bright Lights, Big City“</li></ul>"),
            ("Die Filmmusik von Justice",
             f"<p>Das französische Duo Justice hat die Musik zum Spiel komponiert. Sie passt sich im Spiel dynamisch an das an, was man gerade tut. Das Album „Grand Theft Auto VI: Original Score“ erscheint am <b>11. Dezember</b> mit 30 Stücken, als Download, auf CD und Vinyl {q(R_MUSIC, 'Rockstar')} {q(SCORE, 'Music Week')}. Schon zu hören: „Flower in a Hurricane“ und „Pusher“ mit Gesaffelstein.</p>"),
            ("Die Radiosender",
             f"<p>Rockstar hat bisher sechs Sender vorgestellt {q(R_RADIO, 'Rockstar')}:</p><ul class=\"pts\">"
             "<li><b>Cocoteo FM:</b> moderner Latin-Sound mit El Martillo und La Gata.</li>"
             "<li><b>Back Country Radio:</b> Country mit MW und Delta Dawne.</li>"
             "<li><b>AfroBank FM:</b> Amapiano, afrikanische Klassiker und mehr mit Burna und Palmsy.</li>"
             "<li><b>The Chamber 106.6:</b> Metal mit DJ Kerry und DJ Tom.</li>"
             "<li><b>Flash FM:</b> Pop mit Robyn und Alex.</li>"
             "<li><b>Dirty South Classics:</b> Südstaaten-Rap mit Trick und Trina.</li></ul>"
             "<p>Neu sind Podcasts, und Radio lässt sich auch zu Fuß über Kopfhörer hören. Hörproben gibt es auf Rockstars Musikseite.</p>"
             "<p>Alles zum Start steht im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>.</p>"),
        ],
        "faq": [
            ("Wann ist der GTA 6 Soundtrack erschienen?", "„Grand Theft Auto VI: The Album“ ist am 19. November 2026 zusammen mit dem Spiel erschienen. Die Filmmusik von Justice folgt am 11. Dezember."),
            ("Wer macht die Musik zu GTA 6?", "Die Filmmusik stammt vom französischen Duo Justice. Auf dem Album sind unter anderem Travis Scott, Cardi B, Morgan Wallen, Rauw Alejandro, Yung Lean und Keith Richards."),
            ("Welcher Song läuft im GTA 6 Launch-Trailer?", "„Flower in a Hurricane“ von Justice mit Tame Impala, SZA und King Gizzard and The Lizard Wizard."),
            ("Welche Radiosender gibt es in GTA 6?", "Bisher vorgestellt: Cocoteo FM, Back Country Radio, AfroBank FM, The Chamber 106.6, Flash FM und Dirty South Classics."),
        ],
    },
]

CSS = """:root{--bg:#07070c;--panel:#10101a;--line:#262636;--fg:#f4f2f7;--muted:#a7a3b8;--red:#e11d48;--gold:#fbbf24;
--ok:#4ade80;--warn:#fbbf24;--bad:#f87171;--display:"Big Shoulders Display","Arial Narrow",Impact,sans-serif;--body:"Inter",system-ui,sans-serif}
*{box-sizing:border-box}html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 var(--body)}
a{color:var(--gold)}
.top{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--line);background:#0b0b12}
.logo{display:inline-flex;align-items:center;gap:8px;color:var(--fg);text-decoration:none;font:900 22px/1 var(--display);letter-spacing:.04em}
.logo i{background:var(--red);color:#fff;font-style:normal;padding:4px 7px;border-radius:3px}
.top .live{margin-left:auto;font:800 14px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--red);padding:9px 12px;border-radius:4px;text-decoration:none}
main{max-width:760px;margin:0 auto;padding:22px 16px 40px;font-size:17px}
.crumb{font-size:13px;color:var(--muted)}.crumb a{color:var(--muted)}
.meta{color:var(--muted);font-size:14px}
h1{font:900 clamp(32px,6vw,52px)/1.02 var(--display);letter-spacing:.01em;margin:12px 0 14px;text-wrap:balance}
h2{font:900 26px/1.1 var(--display);letter-spacing:.02em;margin:30px 0 10px}
p{margin:0 0 1em}
.tag{display:inline-block;font:800 11px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;padding:3px 6px 2px;border:2px solid currentColor;border-radius:3px;margin-right:6px;vertical-align:1px}
.t-ok{color:var(--ok)}.t-warn{color:var(--warn)}.t-bad{color:var(--bad)}
.facts{background:var(--panel);border:1px solid var(--line);border-radius:8px;margin:20px 0;padding:4px 16px}
.facts div{display:grid;grid-template-columns:150px 1fr;gap:12px;padding:10px 0;border-bottom:1px solid var(--line);font-size:15px}
.facts div:last-child{border-bottom:0}.facts dt{color:var(--muted);font-weight:600}.facts dd{margin:0}
@media(max-width:520px){.facts div{grid-template-columns:1fr;gap:2px}}
a.q{font-size:12px;color:var(--muted);text-decoration:none;border:1px solid var(--line);border-radius:3px;padding:1px 5px;margin-left:2px;white-space:nowrap}a.q:hover{color:var(--gold);border-color:var(--gold)}
ul.pts{padding-left:20px}ul.pts li{margin:4px 0}
details{border-bottom:1px solid var(--line);padding:10px 0}summary{cursor:pointer;font-weight:700}details p{margin:8px 0 0;color:#dcd8e6}
.cta{display:inline-block;margin:26px 0 8px;font:800 16px/1 var(--display);letter-spacing:.1em;text-transform:uppercase;color:#111;background:var(--gold);padding:13px 16px;border-radius:4px;text-decoration:none}
.more{margin-top:34px;border-top:1px solid var(--line);padding-top:6px}.more ul{list-style:none;margin:0;padding:0}
.more li{padding:9px 0;border-bottom:1px solid var(--line)}.more li a{color:var(--fg);text-decoration:none}.more li a:hover{color:var(--gold)}
footer{color:var(--muted);font-size:13px;text-align:center;padding:24px 16px;border-top:1px solid var(--line)}
.keys{width:100%;border-collapse:collapse;margin:14px 0;font-size:15px}.keys th,.keys td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}.keys th{font:800 13px/1 var(--display);letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
.xc{display:flex;width:max-content;margin:14px auto 0;align-items:center;gap:8px;color:var(--muted);text-decoration:none;font-size:12px;letter-spacing:.04em;opacity:.8}.xc:hover{opacity:1}.xc img{display:block;height:22px;width:auto}"""


def plain(s):
    import re
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def render(g):
    url = f"{SITE}ratgeber/{g['slug']}.html"
    e = html.escape
    facts = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in g["facts"])
    secs = "".join(f"<h2>{h}</h2>{b}" for h, b in g["sections"])
    faq = "".join(f"<details><summary>{e(a)}</summary><p>{e(b)}</p></details>" for a, b in g["faq"])
    more = "".join(f'<li><a href="{o["slug"]}.html">{e(o["h1"])}</a></li>' for o in GUIDES if o is not g)
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
         "inLanguage": "de-DE", "mainEntityOfPage": url, "image": [SITE + "og.jpg"],
         "datePublished": g.get("published", "2026-11-05"), "dateModified": STAND[0],
         "author": {"@type": "Organization", "name": "Leonida News Network", "url": SITE},
         "publisher": {"@type": "Organization", "name": "Leonida News Network", "url": SITE}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in g["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "GTA 6 News", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Ratgeber", "item": SITE + "ratgeber/"},
            {"@type": "ListItem", "position": 3, "name": g["h1"], "item": url}]},
    ]
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(g['title'])} | LNN</title>
<meta name="description" content="{e(g['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Leonida News Network">
<meta property="og:title" content="{e(g['title'])}">
<meta property="og:description" content="{e(g['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}og.jpg?v=2">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#07070c">
<link rel="icon" href="../favicon.ico?v=2" sizes="48x48">
<link rel="icon" href="../favicon.svg?v=2" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png?v=2">
<link rel="stylesheet" href="../fonts/fonts.css?v=2">
{lds}<style>
{CSS}
</style>
</head>
<body>
<header class="top"><a class="logo" href="../"><i>LNN</i> Leonida News Network</a><a class="live" href="../#live">Zum Liveticker</a></header>
<main>
<nav class="crumb" aria-label="Brotkrümel"><a href="../">GTA 6 News</a> › <a href="./">Ratgeber</a></nav>
<h1>{e(g['h1'])}</h1>
<p class="meta">Stand: {STAND[1]} · wird bei neuen Infos aktualisiert</p>
<p>{g['lead']}</p>
<dl class="facts">{facts}</dl>
{secs}
<h2>Häufige Fragen</h2>
{faq}
<a class="cta" href="../">Alle GTA 6 News mit Quelle</a>
<section class="more"><h2>Mehr Ratgeber</h2><ul>{more}<li><a href="./">Alle Ratgeber auf einen Blick</a></li><li><a href="../countdown.html">GTA 6 Countdown für deine Seite</a></li></ul></section>
</main>
<footer>Leonida News Network · GTA 6 News auf Deutsch, jede Meldung mit Quellenstempel · Inoffizielle Fanseite, nicht verbunden mit Rockstar Games oder Take-Two<br><a href="../impressum.html">Impressum</a> · <a href="../datenschutz.html">Datenschutz</a><a class="xc" href="https://xetcraft.de" title="Xetcraft: die Werkstatt von XetrovT2000"><span>Ein Projekt von</span><img src="../xetcraft-logo.png" width="95" height="22" alt="Xetcraft"></a></footer>
<script data-goatcounter="https://gta6-infoboard.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
"""


T_G = '<span class="tag t-bad">Gerücht</span>'
EG = "https://www.eurogamer.de/gta-6-steuerung-tastenbelegung-aenderungen"
EG_IMG = "https://assetsio.gnwcdn.com/GTA6---Steuerung008.jpg?width=1600&quality=90&format=jpg"
R_SET = "https://support.rockstargames.com/articles/4jUHNdP22SmaKSF8DWqhXC/how-to-change-grand-theft-auto-vi-settings"
GS_MELEE = "https://www.gamestar.de/artikel/gta-6-fortgeschrittene-nahkampf-moves-guide,3463745.html"
IG_CTRL = "https://insider-gaming.com/gta-6-control-settings/"
GTAB = "https://www.gtabase.com/gta-6/articles/gta-6-combat-stealth-guide"
IG_STYLE = "https://insider-gaming.com/gta-6-has-different-fighting-styles-for-both-the-characters/"
KOTAKU_TR = "https://kotaku.com/here-are-some-super-useful-control-shortcuts-gta-6-doesnt-tell-you-about-2000759100"
MP1_TR = "https://mp1st.com/news/gta-6-hidden-controls-you-might-not-know-about"
PSI_TR = "https://www.playstationinfo.de/2026/11/23/gta-6-versteckte-steuerungs-tricks-die-ihr-unbedingt-kennen-solltet/"
GTAB_DRV = "https://www.gtabase.com/gta-6/articles/gta-6-driving-tips"
T_T = '<span class="tag t-ok">Getestet</span>'

GUIDES += [
    {
        "slug": "gta-6-nahkampf-steuerung",
        "published": "2026-11-24",
        "title": "GTA 6 Steuerung: Nahkampf und versteckte Tricks (PS5, Xbox)",
        "h1": "GTA 6 Steuerung: Nahkampf und versteckte Tricks",
        "desc": "GTA 6 Nahkampf und versteckte Tricks: blocken, kontern, packen, Granate schnell werfen, Steuerkreuz richtig nutzen. PS5 und Xbox, mit Quellen.",
        "lead": "Der Nahkampf in GTA VI kann mehr, als das Spiel erklärt. Hämmern auf eine Taste reicht nicht mehr: Wer blind drauflos schlägt, wird gekontert und steht ohne Ausdauer da. Hier steht, welche Taste was macht, was hinter den versteckten Moves steckt und welche kleinen Kniffe dir das Spiel nirgends beibringt, etwa die schnelle Granate. Alle Tasten gelten für das Steuerungsschema <b>Standard</b>. Jede Angabe trägt einen Stempel: <b>Offiziell</b> heißt von Rockstar oder aus dem Spielmenü, <b>Getestet</b> heißt von uns im Spiel ausprobiert, <b>Berichtet</b> heißt von Medien oder Guide-Seiten, <b>Gerücht</b> heißt nicht belegt.",
        "facts": [
            ("Einstellen", f"{T_OK} Pause, Einstellungen, Steuerungsschema, Ansicht „Nahkampf“ {q(R_SET, 'Rockstar')}"),
            ("Schlagen/Treten", f"{T_OK} Quadrat (PS5), X (Xbox), im Spielmenü geprüft {q(EG_IMG, 'Spielmenü')}"),
            ("Blocken/Ausweichen", f"{T_OK} Kreuz (PS5), A (Xbox), im Spielmenü geprüft. Zum Blocken halten {q(EG, 'Eurogamer')}"),
            ("Parieren", f"{T_W} Wird Kreuz eingeblendet, genau im richtigen Moment drücken {q(EG, 'Eurogamer')}"),
            ("Anvisieren", f"{T_OK} L2 (PS5), LT (Xbox) halten, im Spielmenü geprüft {q(EG_IMG, 'Spielmenü')}"),
            ("Packen", f"{T_OK} R2 (PS5), RT (Xbox), im Spielmenü geprüft {q(EG_IMG, 'Spielmenü')}"),
            ("Ducken", f"{T_OK} Kreis (PS5), B (Xbox), zu Fuß und beim Zielen, im Spielmenü geprüft"),
            ("Fokus", f"{T_W} L3 und R3 zusammen drücken {q(EG, 'Eurogamer')}"),
            ("Granate schnell", f"{T_T} Beim Zielen R1 (Xbox: RB) halten wirft den zuletzt gewählten Sprengkörper"),
            ("Schemata", f"{T_W} Standard, Klassisch und Linkshänder {q(IG_CTRL, 'Insider Gaming')}"),
        ],
        "sections": [
            ("Die Tasten auf einen Blick",
             f"<p>So zeigt das Spiel selbst die Nahkampf-Belegung im Schema Standard. Wir haben sie am 24. November im deutschen Einstellungsmenü auf der PS5 selbst geprüft. Dasselbe Menü zeigt auch ein Screenshot bei Eurogamer {q(EG_IMG, 'Screenshot')} {q(EG, 'Eurogamer')}. Die Begriffe in der linken Spalte stehen genau so im Spiel.</p>"
             "<table class=\"keys\"><thead><tr><th>Im Spiel</th><th>PS5</th><th>Xbox</th></tr></thead><tbody>"
             "<tr><td>Anvisieren (halten)</td><td>L2</td><td>LT</td></tr>"
             "<tr><td>Packen</td><td>R2</td><td>RT</td></tr>"
             "<tr><td>Schlagen/Treten</td><td>Quadrat</td><td>X</td></tr>"
             "<tr><td>Blocken/Ausweichen</td><td>Kreuz</td><td>A</td></tr>"
             "<tr><td>Bewegen</td><td>linker Stick</td><td>linker Stick</td></tr>"
             "<tr><td>Umschauen</td><td>rechter Stick</td><td>rechter Stick</td></tr>"
             "</tbody></table>"
             f"<p>Geprüft haben wir auf der PS5. Die Xbox-Tasten liegen an derselben Stelle, so führt sie auch die Guide-Seite GTABase {q(GTAB, 'GTABase')}.</p>"
             "<p>Wichtig: Auch in den Ansichten <b>Zu Fuß</b> und <b>Zielen</b> liegt „Nahkampf“ auf Quadrat (Xbox: X). Du kannst also jederzeit zuschlagen, auch mit gezogener Waffe. Kreis (Xbox: B) ist dort <b>Ducken</b>, so schleichst du dich an.</p>"),
            ("So findest du deine Belegung",
             f"<p>Laut Rockstar erreichst du alle Einstellungen über das <b>Pausenmenü</b> und dann <b>Einstellungen</b>. Unter <b>Steuerungsschema</b> gibt es eine eigene Ansicht für jede Lage: zu Fuß, Zielen, Nahkampf, Land- und Wasserfahrzeuge, Luftfahrzeuge, Fahrrad, Schwimmen und Fallschirm {q(R_SET, 'Rockstar')}. Unten auf dem Bildschirm setzt „Standard wiederherstellen“ alles zurück.</p>"
             f"<p>Es gibt drei Schemata {q(IG_CTRL, 'Insider Gaming')}:</p><ul class=\"pts\">"
             "<li><b>Standard:</b> wie in der Tabelle oben. Rennen liegt hier auf dem gedrückten linken Stick.</li>"
             "<li><b>Klassisch:</b> wie in früheren Rockstar-Spielen. Schlagen liegt auf Kreis (Xbox: B), Blocken und Ausweichen auf Quadrat (Xbox: X). Anvisieren und Packen bleiben auf L2 und R2.</li>"
             "<li><b>Linkshänder:</b> Anvisieren und Packen sind getauscht (Packen auf L2, Anvisieren auf R2), ebenso die beiden Sticks.</li></ul>"
             "<p>Wenn dir ein Guide eine andere Taste nennt, liegt das oft am Schema. Im Zweifel zeigt dir das Spiel unter Steuerungsschema, Nahkampf, was bei dir gilt.</p>"),
            ("Der Grundablauf",
             f"<ul class=\"pts\"><li><b>Anvisieren:</b> L2 halten. So bleibst du auf einen Gegner ausgerichtet und kannst um ihn herum laufen.</li>"
             "<li><b>Schlagen:</b> Quadrat. Ob Jason oder Lucia schlagen oder treten, entscheidet das Spiel je nach Lage.</li>"
             f"<li><b>Blocken:</b> Kreuz <b>gedrückt halten</b>, dann nehmen die beiden die Hände hoch {q(EG, 'Eurogamer')}.</li>"
             f"<li><b>Parieren:</b> Wird während eines Angriffs Kreuz eingeblendet, im richtigen Moment drücken {q(EG, 'Eurogamer')}.</li></ul>"
             f"<p>{T_W} Wildes Hämmern auf die Angriffstaste bestraft das Spiel: Der Gegner kontert und die Ausdauer ist leer {q(GS_MELEE, 'GameStar')}. Besser ist es, auf Lücken zu warten.</p>"
             f"<p>{T_W} Die Guide-Seite GTABase nennt noch zwei Dinge, die wir in keiner zweiten Quelle gefunden haben: Quadrat <b>halten</b> gibt einen schweren Angriff, und nach einem Konter (Kreuz kurz vor dem Treffer) folgt mit Quadrat der Gegenangriff {q(GTAB, 'GTABase')}.</p>"),
            ("Packen und versteckte Moves",
             f"<p>Mit R2 packst du einen Gegner. Laut GameStar stecken dahinter mehrere Moves, die das Spiel nirgends erklärt. Sie laufen alle über dieselben Tasten: R2, Quadrat, Rennen (linker Stick gedrückt) und eine Richtung am linken Stick {q(GS_MELEE, 'GameStar')}. {T_W}</p><ul class=\"pts\">"
             "<li><b>Suplex:</b> von hinten mit R2 packen, Quadrat halten, bis der Griff wechselt. Dann loslassen, linken Stick nach hinten und Quadrat erneut drücken.</li>"
             "<li><b>Würgegriff oder Body Slam:</b> aus kurzer Distanz packen und Quadrat halten. Weiter halten würgt den Gegner bis zur Ohnmacht. Stattdessen loslassen, Stick nach hinten und Quadrat antippen gibt einen Body Slam.</li>"
             "<li><b>Seiten- und Stoßtritt:</b> einen zu nahen Gegner packen, wegschubsen, dann Quadrat halten und den Stick zur Seite neigen. Das schafft Abstand.</li>"
             "<li><b>Tackle:</b> mit Anlauf frontal auf den Gegner zu rennen und beim Aufprall Quadrat drücken. Am Boden kannst du nachschlagen.</li>"
             "<li><b>Dropkick:</b> genauso anrennen, aber Quadrat schon während des Anlaufs drücken.</li>"
             "<li><b>Clothesline:</b> einem heranstürmenden Gegner frontal entgegen rennen und im richtigen Moment Quadrat drücken.</li></ul>"
             f"<p>Zähe Gegner reißen sich laut GameStar oft sofort wieder los. Erst ein paar normale Schläge, dann packen {q(GS_MELEE, 'GameStar')}. Für lautlose Takedowns nennt GTABase: von hinten anschleichen, R2 halten, dann mehrmals Quadrat {q(GTAB, 'GTABase')}.</p>"),
            ("Fokus und Ausdauer",
             f"<p>{T_W} L3 und R3 zusammen starten den <b>Fokus</b>, eine Art Zeitlupe. Im Kampf hebt er die Schwachstellen von Gegnern hervor {q(EG, 'Eurogamer')}. Laut GTABase zeigt er auch, welche Treffer tödlich sind und welche nicht {q(GTAB, 'GTABase')}.</p>"
             f"<p>{T_W} Nahkampf kostet <b>Ausdauer</b> {q(GTAB, 'GTABase')} {q(GS_MELEE, 'GameStar')}. Ausdauer trainierst du zum Beispiel beim Schwimmen und Radfahren {q(EG, 'Eurogamer')}.</p>"
             f"<p>{T_G} Spieler vermuten, dass Jasons Kraft beeinflusst, wie gut schwere Moves wie der Suplex gelingen, und dass sich Kraft an Gewichten trainieren lässt. GameStar gibt das nur als Vermutung aus Reddit wieder {q(GS_MELEE, 'GameStar')}.</p>"),
            ("Kniffe im Kampf, die das Spiel nicht erklärt",
             f"<ul class=\"pts\"><li>{T_T} <b>Granate schnell werfen:</b> Während du mit L2 zielst, R1 (Xbox: RB) <b>halten</b>. Die Figur wirft sofort den Sprengkörper, den du zuletzt im Waffenrad gewählt hast, ohne dass du die Waffe wechseln musst. Das haben wir selbst im Spiel ausprobiert. So beschreiben es auch Guide-Seiten {q(GTAB, 'GTABase')}.</li>"
             f"<li>{T_OK} <b>Wurfbahn anzeigen:</b> Beim Zielen liegt auf R3 „Zoomen/Wurfbahn“ (Spielmenü, Ansicht Zielen). Mit einem Wurfgegenstand in der Hand siehst du so vorher, wo er landet.</li>"
             f"<li>{T_OK} <b>Sprengstoff zünden:</b> Steuerkreuz rechts (Spielmenü, Ansicht Zu Fuß).</li>"
             f"<li>{T_OK} <b>Schneller Waffenwechsel:</b> Beim Zielen auf Dreieck (Xbox: Y), ohne das Waffenrad zu öffnen (Spielmenü, Ansicht Zielen).</li>"
             f"<li>{T_OK} <b>Zuschlagen mit Waffe in der Hand:</b> Quadrat (Xbox: X) ist auch beim Zielen Nahkampf (Spielmenü).</li>"
             f"<li>{T_W} <b>Aus dem Auto heraus:</b> Quadrat (Xbox: X) beim Fahren schlägt Leute mit der Autotür, auf Motorrad oder Roller gibt es einen Tritt {q(MP1_TR, 'MP1st')} {q(GTAB_DRV, 'GTABase')}. Kreis (Xbox: B) halten duckt dich im Auto weg, das hilft gegen die Polizei {q(MP1_TR, 'MP1st')}.</li>"
             f"<li>{T_W} <b>Untersuchen:</b> L2 halten und R3 antippen schaltet eine Ansicht aus der Ich-Perspektive ein, in der du dich umsehen, aber nicht bewegen kannst {q(MP1_TR, 'MP1st')} {q(PSI_TR, 'PlayStationInfo')}.</li></ul>"),
            ("Kämpfen Jason und Lucia unterschiedlich?",
             f"<p>{T_OK} Lucia wurde laut Rockstar von ihrem Vater im <b>Kampfsport</b> trainiert {q(R_SITE, 'Rockstar')}. Jason ist Armeeveteran.</p>"
             f"<p>{T_W} Laut GameStar hat Lucia eigene Moves, eher MMA-Manöver statt Haltegriffe. Sie liegen auf denselben Tasten wie bei Jason {q(GS_MELEE, 'GameStar')}. Die Steuerung musst du also nur einmal lernen.</p>"
             f"<p>{T_G} Schon im September hieß es, Lucia kämpfe technisch mit Kickboxen und MMA und Jason als Straßenschläger mit roher Kraft. Das stammt von einem italienischen YouTuber, der eine Vorführung bei Rockstar gesehen, aber nicht selbst gespielt hat {q(IG_STYLE, 'Insider Gaming')}. Rockstar hat das so nie gesagt.</p>"
             "<p>Mehr zu den beiden steht im <a href=\"gta-6-charaktere.html\">Ratgeber zu den Charakteren</a>.</p>"),
            ("Muss jeder Kampf tödlich enden?",
             "<p>Nein. Laut Rob Nelson von Rockstar North kommt man an vielen Stellen voran, ohne jemanden zu töten. Einfach sei das aber nicht immer. Details stehen in unserem Magazin unter <a href=\"../#vs-gewalt\">Weiterkommen ohne zu töten</a>.</p>"),
            ("Weitere versteckte Tricks: Steuerkreuz und Alltag",
             f"<p>{T_OK} Das <b>Steuerkreuz</b> hat zu Fuß zwei Ebenen. Kurz drücken: oben Handy, links Radiosteuerung, unten Missionsziel und Minikarte, rechts Sprengstoff zünden. Halten: oben die WAiNK-App, links das Radiomenü, unten Schnellnavigation, rechts das Partnermenü. Das zeigt das Spielmenü in der Ansicht Zu Fuß. Auf der Xbox liegt alles an derselben Stelle.</p>"
             f"<ul class=\"pts\"><li>{T_OK} <b>Ausruhen:</b> Kreis (Xbox: B) zu Fuß <b>halten</b>. Je nach Ort setzt sich die Figur hin oder lehnt sich an eine Wand (Spielmenü; Details laut {q(MP1_TR, 'MP1st')}).</li>"
             f"<li>{T_W} <b>Schnell einen Wegpunkt setzen:</b> Steuerkreuz unten halten setzt einen Zielpunkt in der Nähe, ohne die Karte zu öffnen {q(MP1_TR, 'MP1st')}.</li>"
             f"<li>{T_W} <b>Auto prüfen, bevor du es klaust:</b> Steuerkreuz oben halten (WAiNK-App), dann R1 (Xbox: RB) halten scannt das Fahrzeug {q(MP1_TR, 'MP1st')}.</li>"
             "</ul><p>Alle Tricks rund ums Auto, Boot und Flugzeug, etwa Autopilot, Motor laufen lassen und Blinker, stehen jetzt im <a href=\"gta-6-fahren-steuerung.html\">Ratgeber zum Fahren</a>.</p>"
             "<p>Du hast selbst einen Kniff entdeckt? Schreib uns im Discord-Kanal #leonida-news, wir probieren ihn aus und nehmen ihn auf.</p>"),
        ],
        "faq": [
            ("Wie schlägt man in GTA 6?", "Im Steuerungsschema Standard mit Quadrat auf der PS5 und X auf der Xbox. Im Schema Klassisch liegt Schlagen auf Kreis beziehungsweise B."),
            ("Wie blockt man in GTA 6?", "Kreuz auf der PS5 oder A auf der Xbox gedrückt halten. Dieselbe Taste dient auch zum Ausweichen."),
            ("Wie pariert oder kontert man in GTA 6?", "Wenn während eines gegnerischen Angriffs Kreuz (Xbox: A) eingeblendet wird, genau im richtigen Moment drücken. Danach mit Quadrat (Xbox: X) angreifen."),
            ("Wie packt man Gegner in GTA 6?", "Mit R2 auf der PS5 oder RT auf der Xbox. Aus dem Griff heraus gibt es weitere Moves wie Würgegriff, Body Slam oder Suplex."),
            ("Wo ändert man die Steuerung in GTA 6?", "Im Pausenmenü unter Einstellungen und Steuerungsschema. Dort gibt es die Schemata Standard, Klassisch und Linkshänder und eine eigene Ansicht für den Nahkampf."),
            ("Wie wirft man in GTA 6 schnell eine Granate?", "Beim Zielen mit L2 die Taste R1 halten (Xbox: LT und RB). Die Figur wirft dann sofort den zuletzt gewählten Sprengkörper."),
            ("Kämpft Lucia anders als Jason?", "Lucia wurde im Kampfsport trainiert und hat laut GameStar eigene MMA-Moves. Die Tasten sind bei beiden gleich."),
        ],
    },
]

EG_CAR = "https://assetsio.gnwcdn.com/GTA6---Steuerung009.jpg?width=1600&quality=90&format=jpg"
EG_CAR_H = "https://assetsio.gnwcdn.com/GTA6---Steuerung010.jpg?width=1600&quality=90&format=jpg"
EG_AIR = "https://assetsio.gnwcdn.com/GTA6---Steuerung012.jpg?width=1600&quality=90&format=jpg"
PC_TR = "https://www.playcentral.de/gta-6-steuerung-tricks-die-jeder-kennen-sollte/"
BEE_TR = "https://beebom.com/gta-6-secret-controls/"

GUIDES += [
    {
        "slug": "gta-6-fahren-steuerung",
        "published": "2026-11-25",
        "title": "GTA 6 Fahren: Steuerung, Autopilot, Blinker (PS5, Xbox)",
        "h1": "GTA 6 Fahren: Steuerung und versteckte Tricks",
        "desc": "GTA 6 Fahrzeug-Steuerung für PS5 und Xbox: Blinker, Nitro, Handbremse, Autopilot, Motor laufen lassen, Boot und Fliegen. Jede Angabe mit Quelle.",
        "lead": "Im Auto legt GTA VI viele Funktionen auf doppelt gedrückte oder gehaltene Tasten, und kaum etwas davon erklärt das Spiel. Hier steht die Belegung aus dem Spielmenü und dazu die Kniffe, die Spieler und Medien seit dem Start gefunden haben. Alle Tasten gelten für das Steuerungsschema <b>Standard</b>. <b>Offiziell</b> heißt von Rockstar oder aus dem Spielmenü, <b>Berichtet</b> heißt von Medien oder Guide-Seiten.",
        "facts": [
            ("Einstellen", f"{T_OK} Pause, Einstellungen, Steuerungsschema, Ansicht „Land-/Wasserfahrzeug“ {q(R_SET, 'Rockstar')}"),
            ("Gas und Bremse", f"{T_OK} R2 beschleunigen, L2 bremsen und rückwärts (Xbox: RT, LT) {q(EG_CAR, 'Spielmenü')}"),
            ("Handbremse", f"{T_OK} Kreuz (Xbox: A) {q(EG_CAR, 'Spielmenü')}"),
            ("Hupe und Nitro", f"{T_OK} L3, also linken Stick drücken (Xbox: LS) {q(EG_CAR, 'Spielmenü')}"),
            ("Blinker", f"{T_OK} Steuerkreuz links oder rechts {q(EG_CAR, 'Spielmenü')}"),
            ("Licht und Ducken", f"{T_OK} Kreis (Xbox: B) drücken für Scheinwerfer, halten zum Ducken {q(EG_CAR_H, 'Spielmenü')}"),
            ("Autopilot", f"{T_W} Wegpunkt setzen, Steuerkreuz unten halten, Options, dann Kreis halten {q(MP1_TR, 'MP1st')}"),
            ("Motor anlassen", f"{T_W} Beim Aussteigen Dreieck (Xbox: Y) zweimal drücken {q(KOTAKU_TR, 'Kotaku')}"),
        ],
        "sections": [
            ("Die Tasten im Auto auf einen Blick",
             f"<p>So zeigt das Spiel die Belegung für Land- und Wasserfahrzeuge im Schema Standard. Grundlage sind zwei Screenshots des deutschen Einstellungsmenüs, die Eurogamer veröffentlicht hat: einer für kurz gedrückte Tasten {q(EG_CAR, 'Screenshot 1')}, einer für gehaltene {q(EG_CAR_H, 'Screenshot 2')} {q(EG, 'Eurogamer')}. Die Begriffe stehen genau so im Spiel.</p>"
             "<table class=\"keys\"><thead><tr><th>Im Spiel</th><th>PS5</th><th>Xbox</th></tr></thead><tbody>"
             "<tr><td>Beschleunigen</td><td>R2</td><td>RT</td></tr>"
             "<tr><td>Bremsen/Rückwärtsgang</td><td>L2</td><td>LT</td></tr>"
             "<tr><td>Lenken</td><td>linker Stick</td><td>linker Stick</td></tr>"
             "<tr><td>Handbremse</td><td>Kreuz</td><td>A</td></tr>"
             "<tr><td>Hupe/Nitro</td><td>L3</td><td>LS</td></tr>"
             "<tr><td>Scheinwerfer (halten: Ducken)</td><td>Kreis</td><td>B</td></tr>"
             "<tr><td>Fahrzeug verlassen</td><td>Dreieck</td><td>Y</td></tr>"
             "<tr><td>Nahkampf</td><td>Quadrat</td><td>X</td></tr>"
             "<tr><td>Schießen</td><td>R1</td><td>RB</td></tr>"
             "<tr><td>Waffe wegstecken (halten: Ausrüstung)</td><td>L1</td><td>LB</td></tr>"
             "<tr><td>Links blinken / Rechts blinken</td><td>Steuerkreuz links / rechts</td><td>Steuerkreuz links / rechts</td></tr>"
             "<tr><td>Handy</td><td>Steuerkreuz oben</td><td>Steuerkreuz oben</td></tr>"
             "<tr><td>Missionsziel/Minimap</td><td>Steuerkreuz unten</td><td>Steuerkreuz unten</td></tr>"
             "<tr><td>Nach hinten schauen</td><td>R3</td><td>RS</td></tr>"
             "<tr><td>Umschauen</td><td>rechter Stick</td><td>rechter Stick</td></tr>"
             "</tbody></table>"
             f"<p>Hältst du das <b>Steuerkreuz</b> gedrückt, kommt eine zweite Ebene: oben Interagieren, links Fahrzeugmenü, unten Schnellnavigation, rechts Partnermenü. Weil L2 im Auto bremst, liegt das Interagieren hier auf dem Steuerkreuz {q(EG, 'Eurogamer')}. Die Screenshots zeigen den PS5-Controller, die Xbox-Tasten liegen an derselben Stelle.</p>"),
            ("Versteckte Tricks beim Fahren",
             f"<ul class=\"pts\"><li>{T_W} <b>Autopilot:</b> Wegpunkt auf der Karte setzen, Steuerkreuz unten halten, Options (Xbox: Menü) drücken für die Kinokamera, dann Kreis (Xbox: B) halten. Jason oder Lucia fahren dich zum Ziel und halten sich dabei an die Verkehrsregeln {q(MP1_TR, 'MP1st')} {q(PC_TR, 'PlayCentral')} {q(BEE_TR, 'Beebom')}.</li>"
             f"<li>{T_W} <b>Motor laufen lassen:</b> Beim Aussteigen Dreieck (Xbox: Y) zweimal schnell drücken. Motor, Radio und Licht laufen weiter. Wer Dreieck dagegen hält, bremst erst und steigt dann aus {q(KOTAKU_TR, 'Kotaku')} {q(PC_TR, 'PlayCentral')} {q(GTAB_DRV, 'GTABase')}.</li>"
             f"<li>{T_OK} <b>Blinken:</b> Steuerkreuz links oder rechts kurz drücken (Spielmenü). {T_W} Zweimal links schaltet laut Kotaku das Radio aus und wieder an {q(KOTAKU_TR, 'Kotaku')}.</li>"
             f"<li>{T_OK} <b>Licht:</b> Kreis (Xbox: B) schaltet die Scheinwerfer (Spielmenü). {T_W} Zweimal drücken wechselt zwischen aus, Fernlicht und Abblendlicht {q(KOTAKU_TR, 'Kotaku')}.</li>"
             f"<li>{T_OK} <b>Fahrzeugmenü:</b> Steuerkreuz links halten (Spielmenü). {T_W} Mit dem rechten Stick wählst du dort Fenster, Warnblinker, Lichtstärke und beim Cabrio das Verdeck {q(PC_TR, 'PlayCentral')} {q(BEE_TR, 'Beebom')}.</li>"
             f"<li>{T_OK} <b>Wegducken:</b> Kreis (Xbox: B) halten (Spielmenü). {T_W} So wirst du schlechter gesehen, das hilft gegen die Polizei {q(MP1_TR, 'MP1st')}.</li>"
             f"<li>{T_OK} <b>Partner ans Steuer:</b> Rockstar hat bestätigt, dass der Partner das Steuer übernehmen kann und du dann mitfährst oder vom Beifahrersitz schießt (<a href=\"../#ign\">IGN-Interview</a>). {T_W} Dafür Steuerkreuz rechts halten (Partnermenü) und Kreuz (Xbox: A) drücken {q(BEE_TR, 'Beebom')}.</li>"
             f"<li>{T_OK} <b>Aus dem Auto kämpfen:</b> R1 (Xbox: RB) schießt, Quadrat (Xbox: X) ist Nahkampf (Spielmenü). {T_W} Im Auto schlägst du damit Leute mit der Tür, auf Motorrad oder Roller gibt es einen Tritt {q(MP1_TR, 'MP1st')} {q(GTAB_DRV, 'GTABase')}.</li>"
             f"<li>{T_W} <b>Andere Fahrer anschreien:</b> R3 antippen. Halten heißt nach hinten schauen {q(PC_TR, 'PlayCentral')} {q(KOTAKU_TR, 'Kotaku')}.</li>"
             f"<li>{T_W} <b>Auto wieder aufrichten:</b> Aussteigen, neben das umgekippte Auto stellen, L3 drücken und Quadrat (Xbox: X) halten. Bei sehr schweren Autos oder leerer Ausdauer klappt das nicht {q(MP1_TR, 'MP1st')} {q(GTAB_DRV, 'GTABase')}.</li>"
             f"<li>{T_W} <b>Wheelie:</b> Auf dem Motorrad beim Gasgeben den linken Stick nach hinten ziehen. Nach vorn gibt es einen Stoppie {q(BEE_TR, 'Beebom')}.</li>"
             f"<li>{T_W} <b>Auto prüfen, bevor du es klaust:</b> Zu Fuß Steuerkreuz oben halten (WAiNK-App), dann R1 (Xbox: RB) halten scannt das Fahrzeug {q(MP1_TR, 'MP1st')}.</li></ul>"),
            ("Boote und Jetskis",
             f"<p>{T_W} Auf größeren Booten kannst du das Ruder verlassen und an Deck herumlaufen, während das Boot weiter Kurs hält: Dreieck (Xbox: Y) zweimal drücken {q(EG, 'Eurogamer')} {q(KOTAKU_TR, 'Kotaku')}. Einen gestrandeten Jetski schiebst du zurück ins Wasser, indem du dich dahinter stellst und R1 (Xbox: RB) hältst {q(BEE_TR, 'Beebom')}. Sonst gilt im Boot dieselbe Belegung wie im Auto.</p>"),
            ("Fliegen: Hubschrauber und Flugzeuge",
             f"<p>{T_OK} Für Luftfahrzeuge hat das Spiel eine eigene Belegung {q(EG_AIR, 'Spielmenü')}:</p>"
             "<table class=\"keys\"><thead><tr><th>Im Spiel</th><th>PS5</th><th>Xbox</th></tr></thead><tbody>"
             "<tr><td>Schub geben</td><td>R2</td><td>RT</td></tr>"
             "<tr><td>Schub drosseln</td><td>L2</td><td>LT</td></tr>"
             "<tr><td>Nicken/Rollen</td><td>linker Stick</td><td>linker Stick</td></tr>"
             "<tr><td>Nach links drehen</td><td>Quadrat</td><td>X</td></tr>"
             "<tr><td>Nach rechts drehen</td><td>Kreis</td><td>B</td></tr>"
             "<tr><td>Fahrwerk</td><td>L3</td><td>LS</td></tr>"
             "<tr><td>Schießen</td><td>R1</td><td>RB</td></tr>"
             "<tr><td>Fahrzeug verlassen</td><td>Dreieck</td><td>Y</td></tr>"
             "</tbody></table>"
             f"<p>Hubschrauber und Flugzeuge brauchen etwas Übung, bringen dich danach aber schnell über die Karte {q(EG, 'Eurogamer')}. Wohin es geht, zeigt der <a href=\"gta-6-karte-leonida.html\">Ratgeber zur Karte</a>.</p>"
             "<p>Tricks fürs Kämpfen und das Steuerkreuz zu Fuß stehen im <a href=\"gta-6-nahkampf-steuerung.html\">Ratgeber zu Nahkampf und versteckten Tricks</a>. Du hast selbst einen Kniff gefunden? Schreib uns im Discord-Kanal #leonida-news.</p>"),
        ],
        "faq": [
            ("Wie lässt man in GTA 6 das Auto selbst fahren?", "Wegpunkt setzen, Steuerkreuz unten halten, Options (Xbox: Menü) drücken und dann Kreis (Xbox: B) halten. Jason oder Lucia fahren dann zum Ziel."),
            ("Wie blinkt man in GTA 6?", "Steuerkreuz links oder rechts kurz drücken, auf PS5 und Xbox."),
            ("Wie lässt man in GTA 6 beim Aussteigen den Motor laufen?", "Beim Aussteigen Dreieck (Xbox: Y) zweimal schnell drücken. Motor, Radio und Licht laufen weiter."),
            ("Wo ist Nitro und Hupe in GTA 6?", "Beides liegt auf L3, also dem gedrückten linken Stick (Xbox: LS)."),
            ("Wie duckt man sich in GTA 6 im Auto?", "Kreis (Xbox: B) gedrückt halten. Kurz drücken schaltet stattdessen die Scheinwerfer."),
            ("Wie dreht man ein umgekipptes Auto in GTA 6 um?", "Aussteigen, neben das Auto stellen, L3 drücken und Quadrat (Xbox: X) halten. Bei sehr schweren Autos klappt das nicht."),
        ],
    },
]

EG_MONEY = "https://www.eurogamer.de/gta-6-schnell-geld-verdienen"
GP_MONEY = "https://www.gamepro.de/artikel/gta-6-schnell-geld-verdienen,3463617.html"
GIGA_MONEY = "https://www.giga.de/games/gta-6-schnell-geld-verdienen-mit-diesen-methoden-verdient-ihr-bis-zu-205-000-dollar--01M86MKSWHGDCT40NXSQ3122D9"

GUIDES += [
    {
        "slug": "gta-6-geld-verdienen",
        "published": "2026-11-25",
        "title": "GTA 6 Geld verdienen: die besten Methoden je Kapitel",
        "h1": "GTA 6 Geld verdienen: so kommt ihr an Kohle",
        "desc": "GTA 6 schnell Geld verdienen: Läden ausrauben, Tauchen, Autos an Moses verkaufen, Juweliere, Banken und Tresore bis 205.000 Dollar. Mit Quellen.",
        "lead": "Jason und Lucia starten pleite, und die Story-Missionen allein füllen die Kasse kaum. Hier steht, womit ihr in welcher Phase des Spiels am besten Geld verdient und wie ihr dabei möglichst wenig Ärger mit der Polizei bekommt. Missionsnamen und Story-Wendungen lassen wir weg, die Namen der Auftraggeber und Hehler nennen wir, damit ihr sie im Spiel findet. Die Beträge stammen aus Tests der Medien und schwanken im Spiel. <b>Offiziell</b> heißt von Rockstar, <b>Berichtet</b> heißt von Medien oder Guide-Seiten.",
        "facts": [
            ("Läden", f"{T_OK} Fast jeden Laden könnt ihr überfallen, auch wenn er nicht auf der Karte steht (Rob Nelson, Rockstar North, <a class=\"q\" href=\"../#vs-raub\">Magazin</a>)"),
            ("Große Ziele", f"{T_OK} Juweliere, Banken, Pfandleiher und Geldtransporter zeigt die Karte mit geschätzter Beute (<a class=\"q\" href=\"../#vs-raub\">Magazin</a>)"),
            ("Anfang", f"{T_W} Läden ausrauben und Tauchen bringen ein paar Tausend Dollar pro Stunde {q(EG_MONEY, 'Eurogamer')}"),
            ("Autos", f"{T_W} Moses kauft Autos ohne Peilsender für 800 bis 1.200 Dollar {q(GP_MONEY, 'GamePro')}"),
            ("Juweliere", f"{T_W} Etwa 10.000 bis 25.000 Dollar pro Überfall {q(GIGA_MONEY, 'GIGA')}"),
            ("Kleine Banken", f"{T_W} Etwa 5.000 bis 45.000 Dollar {q(GIGA_MONEY, 'GIGA')}"),
            ("Große Tresore", f"{T_W} Bis zu 205.000 Dollar, gegen Ende des vierten Kapitels {q(GIGA_MONEY, 'GIGA')} {q(GP_MONEY, 'GamePro')}"),
        ],
        "sections": [
            ("Die Methoden auf einen Blick",
             f"<p>{T_W} Die Übersicht fasst zusammen, was GIGA, GamePro und Eurogamer berichten {q(GIGA_MONEY, 'GIGA')} {q(GP_MONEY, 'GamePro')} {q(EG_MONEY, 'Eurogamer')}. Kapitel heißen die Story-Abschnitte des Spiels.</p>"
             "<table class=\"keys\"><thead><tr><th>Methode</th><th>Ab wann</th><th>Ertrag</th></tr></thead><tbody>"
             "<tr><td>Läden ausrauben</td><td>sofort</td><td>ein paar Hundert pro Laden</td></tr>"
             "<tr><td>Tauchen nach Schätzen für Kenton</td><td>1. Kapitel</td><td>lohnend, je nach Fund</td></tr>"
             "<tr><td>Andere Verbrecher ausrauben</td><td>jederzeit</td><td>1.000 bis 15.000 $</td></tr>"
             "<tr><td>Autos an Moses verkaufen</td><td>2. Kapitel</td><td>800 bis 1.200 $</td></tr>"
             "<tr><td>Tiere jagen für Bret</td><td>2. Kapitel</td><td>Hunderte bis einige Tausend $</td></tr>"
             "<tr><td>Gang-Verstecke ausrauben</td><td>Ende 2. Kapitel</td><td>Geld, Waffen, Sprengstoff</td></tr>"
             "<tr><td>Juweliere</td><td>3. Kapitel</td><td>10.000 bis 25.000 $</td></tr>"
             "<tr><td>Kleine Banken</td><td>3. Kapitel</td><td>5.000 bis 45.000 $</td></tr>"
             "<tr><td>Autos mit Peilsender, Wunschliste von Randy</td><td>3. Kapitel</td><td>ca. 4.000 $, Sportwagen über 30.000 $</td></tr>"
             "<tr><td>Demolition Derby</td><td>wiederholbar</td><td>3.800 bis 6.300 $ pro Sieg</td></tr>"
             "<tr><td>Lieferflüge für Pilot Pete (nur Jason)</td><td>4. Kapitel</td><td>10.000 bis 20.000 $</td></tr>"
             "<tr><td>Große Banktresore</td><td>Ende 4. Kapitel</td><td>bis 205.000 $</td></tr>"
             "</tbody></table>"),
            ("Am Anfang: Läden, Tauchen, kleine Dinger",
             f"<p>{T_W} In den ersten beiden Kapiteln lohnen sich Banken noch nicht. Viele Scheine sind markiert und bringen bei frühen Hehlern wenig, andere Geldpakete haben Farbbomben, gegen die ihr erst später ein Störgerät bekommt. Die Karte zeigt Banken anfangs nicht einmal an {q(EG_MONEY, 'Eurogamer')}.</p>"
             f"<ul class=\"pts\"><li>{T_W} <b>Läden ausrauben:</b> Am besten spät abends. Parkt ein Fluchtauto mit Wechsel-Outfit im Kofferraum hinter dem Laden, setzt eine Maske auf und geht mit gezogener Waffe hinein. Zielt auf die Angestellten und bedroht sie, dann legen sie das Geld meist von selbst hin. Danach Waffe wegstecken, ums Gebäude zum Auto, Outfit wechseln, Maske ab. Ein Laden bringt nur ein paar Hundert Dollar, nach einer Stunde summiert sich das {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Shirleys Schnapsladen:</b> Eure Nachbarin Shirley schickt euch früh zum Laden Three Sheets Liquor. Im Hinterzimmer läuft illegaler Tierhandel. Nachts durch den Garten anschleichen, Wachen mit Pfeifen (L2 auf eine Wache, dann pfeifen) oder geworfenen Flaschen weglocken und von hinten ausschalten. Geld steckt hinter einem Lüftungsgitter, das ihr mit dem Fokus findet, dazu ein Safe. Eurogamer holte so über 6.000 Dollar, der Überfall lässt sich nach einer Weile wiederholen {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Tauchen für Kenton:</b> Ein Freund von Brian. Ab dem ersten Treffen fahrt ihr zu den Tauch-Spots auf der Karte und sucht an Wracks nach Gold-Dublonen. Die Funde verkauft ihr bei Kenton. Lohnt sich früh und ganz ohne Polizei {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Augen offen halten:</b> Hört ihr Unruhe, zeigt der Fokus (L3 und R3) die Quelle. Oft ist es ein Überfall anderer Gangster, bei dem ihr dazwischengehen könnt {q(EG_MONEY, 'Eurogamer')}. Andere Verbrecher auszurauben bringt laut GIGA 1.000 bis 15.000 Dollar {q(GIGA_MONEY, 'GIGA')}.</li></ul>"),
            ("Mittelteil: Autos, Gangs, Juweliere, kleine Banken",
             f"<ul class=\"pts\"><li>{T_W} <b>Autos an Moses:</b> Im zweiten Kapitel bekommt ihr von Moses Watkins in Port Gellhorn einen Slim Jim, damit knackt ihr Autos mit Alarmanlage leise. Moses kauft unauffällige Autos ohne Peilsender, aber nicht direkt bei ihm um die Ecke geklaut, zwei, drei Blocks weiter reicht. Sitzt ihr im Auto, markiert seine Werkstatt auf der Karte: Dort steht, ob er den Wagen nimmt und was er zahlt {q(EG_MONEY, 'Eurogamer')}. Mit der WAiNK-App seht ihr vorher, ob ein Auto einen Peilsender hat {q(GIGA_MONEY, 'GIGA')}.</li>"
             f"<li>{T_W} <b>Autos mit Peilsender:</b> Ab dem dritten Kapitel werdet ihr auch die los, über Pay 'N' Spray, für etwa 4.000 Dollar. Randy hat eine Wunschliste mit 22 Fahrzeugen, für bestimmte Sportwagen zahlt er über 30.000 Dollar {q(GIGA_MONEY, 'GIGA')} {q(GP_MONEY, 'GamePro')}.</li>"
             f"<li>{T_W} <b>Gang-Verstecke:</b> Gelb auf der Karte markiert, zum Beispiel die der Bande Kolt &amp; Associates. Eine verlassene Bowlingbahn südlich von Moses eignet sich zum Üben. Ihr findet Geld, Waffen und Sprengstoff, die Beute geht an Hehler wie Tyrone. Fast immer gibt es eine Schießerei und Polizei, mit Schalldämpfer geht es auch leise. Die Verstecke füllen sich mit der Zeit wieder {q(EG_MONEY, 'Eurogamer')} {q(GP_MONEY, 'GamePro')} {q(GIGA_MONEY, 'GIGA')}.</li>"
             f"<li>{T_W} <b>Tiere jagen für Bret:</b> Ab dem zweiten Kapitel, bringt einige Hundert bis einige Tausend Dollar {q(GIGA_MONEY, 'GIGA')}.</li>"
             f"<li>{T_W} <b>Juweliere:</b> Ab dem dritten Kapitel, etwa 10.000 bis 25.000 Dollar {q(GIGA_MONEY, 'GIGA')} {q(GP_MONEY, 'GamePro')}.</li>"
             f"<li>{T_W} <b>Kleine Banken:</b> Später im dritten Kapitel, etwa 5.000 bis 45.000 Dollar. Wachleute sind das größte Risiko {q(GIGA_MONEY, 'GIGA')} {q(GP_MONEY, 'GamePro')}.</li></ul>"),
            ("Später: große Tresore, Flüge, Derby",
             f"<ul class=\"pts\"><li>{T_W} <b>Große Banktresore:</b> Gegen Ende des vierten Kapitels schaltet ein optionaler Auftrag von Yasmani acht große Tresore frei, bis zu 205.000 Dollar pro Überfall. Sobald ein Tresor offen ist, habt ihr vier Fahndungssterne, beim fünften rückt das SWAT an. Plant Fluchtauto und Route vorher {q(GIGA_MONEY, 'GIGA')} {q(GP_MONEY, 'GamePro')}.</li>"
             f"<li>{T_W} <b>Lieferflüge für Pilot Pete:</b> Ab dem vierten Kapitel, nur mit Jason, etwa 10.000 bis 20.000 Dollar {q(GIGA_MONEY, 'GIGA')}.</li>"
             f"<li>{T_W} <b>Demolition Derby:</b> Strecke in Ambrosia, wiederholbar, etwa 3.800 bis 6.300 Dollar pro Sieg {q(GIGA_MONEY, 'GIGA')}.</li></ul>"
             f"<p>GamePro rät, zwischendurch auch mal Rennen zu fahren statt nur zu farmen, sonst wird es schnell eintönig {q(GP_MONEY, 'GamePro')}.</p>"),
            ("Weniger Ärger bei Überfällen",
             f"<ul class=\"pts\"><li>{T_W} <b>Nicht schießen, drohen:</b> Je brutaler ihr vorgeht, desto aggressiver reagiert die Polizei. Wenn doch, auf Knie oder Ellbogen zielen {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Kameras:</b> Wer maskiert ist und danach das Outfit wechselt, muss sich um Kameras kaum sorgen. Manchmal steht im Hinterzimmer ein Videorekorder, dessen Aufnahme ihr zerstören könnt {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Wachleute:</b> Von hinten bedrohen, dann ergeben sie sich eher. Sind sie in der Überzahl, erst einen von hinten niederschlagen {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Hinterzimmer:</b> Wer es noch durchsuchen will, schlägt die Angestellten vorher nieder, sonst rufen sie die Polizei {q(EG_MONEY, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Später leiser:</b> Mit der Pickpistole, die ihr im Spielverlauf bekommt, öffnet ihr verschlossene Hintertüren lautlos {q(EG_MONEY, 'Eurogamer')}.</li></ul>"
             "<p>Laut Rockstar kommt man an vielen Stellen auch weiter, ohne jemanden zu töten, mehr dazu im Magazin unter <a href=\"../#vs-gewalt\">Weiterkommen ohne zu töten</a>. Wie ihr nach dem Überfall mit dem Auto entkommt und euch wegduckt, steht im <a href=\"gta-6-fahren-steuerung.html\">Ratgeber zum Fahren</a>, Schleichen und Ausschalten im <a href=\"gta-6-nahkampf-steuerung.html\">Ratgeber zum Nahkampf</a>.</p>"
             "<p>Einen Geld-Glitch, den manche Seiten beschreiben, nehmen wir bewusst nicht auf: Solche Fehler werden meist schnell gepatcht.</p>"),
        ],
        "faq": [
            ("Wie verdient man am Anfang von GTA 6 schnell Geld?", "Läden nachts maskiert ausrauben, nach Schätzen tauchen und bei Shirleys Schnapsladen den illegalen Tierhandel ausnehmen. Banken lohnen sich in den ersten Kapiteln noch nicht."),
            ("Wo verkauft man in GTA 6 gestohlene Autos?", "Ab dem zweiten Kapitel bei Moses Watkins in Port Gellhorn, solange das Auto keinen Peilsender hat. Autos mit Peilsender werdet ihr ab dem dritten Kapitel über Pay 'N' Spray los."),
            ("Was bringt in GTA 6 am meisten Geld?", "Die großen Banktresore gegen Ende des vierten Kapitels, bis zu 205.000 Dollar pro Überfall. Danach gibt es sofort vier Fahndungssterne."),
            ("Wie viel bringt ein Juwelier in GTA 6?", "Laut Medienberichten etwa 10.000 bis 25.000 Dollar pro Überfall, freigeschaltet im dritten Kapitel."),
            ("Kann man in GTA 6 jeden Laden ausrauben?", "Fast jeden. Rockstar hat bestätigt, dass ihr fast jeden Laden überfallen könnt, auch wenn er nicht auf der Karte markiert ist."),
        ],
    },
]

EG_POL = "https://www.eurogamer.de/gta-6-fahndungslevel-aufmerksamkeit-flucht"
PCG_POL = "https://www.pcgames.de/GTA-6-Spiel-55239/Tipps/polizei-entkommen-reden-1560560/"

GUIDES += [
    {
        "slug": "gta-6-polizei-fahndung",
        "published": "2026-11-25",
        "title": "GTA 6 Polizei abhängen: Sterne, Symbole, Fahndung erklärt",
        "h1": "GTA 6 Fahndung: so werdet ihr die Polizei los",
        "desc": "GTA 6 Fahndungssterne und Aufmerksamkeits-Symbole erklärt: was die Farben bedeuten, wie ihr die Polizei abhängt und Sterne loswerdet. Mit Quellen.",
        "lead": "Einfach Vollgas geben reicht in GTA VI nicht mehr. Die Polizei merkt sich, wie ihr ausseht, was ihr tragt und welches Auto ihr fahrt, und das zeigt das Spiel mit kleinen Symbolen unter den Sternen. Hier steht, was die Sterne und Symbole bedeuten und wie ihr sie wieder loswerdet. <b>Offiziell</b> heißt von Rockstar, <b>Berichtet</b> heißt von Medien, die das Spiel gespielt haben.",
        "facts": [
            ("Sterne", f"{T_W} 1 bis 5, in Ausnahmefällen 6. Ab 3 Sternen kommt ein Hubschrauber {q(EG_POL, 'Eurogamer')}"),
            ("Beschreibung", f"{T_OK} Die Sterne zeigen auch, ob die Polizei weiß, wie ihr ausseht (Rob Nelson, <a class=\"q\" href=\"../#ign-polizei\">IGN-Interview</a>)"),
            ("Symbole", f"{T_W} Gesicht, Fahrzeug, Outfit, sichtbare Waffe, Partner, Kamera {q(EG_POL, 'Eurogamer')}"),
            ("Entkommen", f"{T_W} Sichtkontakt brechen, Suchgebiet verlassen, Symbole loswerden {q(EG_POL, 'Eurogamer')}"),
            ("Reden", f"{T_W} Bei 1 Stern lässt sich ein Polizist manchmal beruhigen {q(PCG_POL, 'PC Games')}"),
            ("Verhaftung", f"{T_OK} Wird einer geschnappt, während der andere entkommt, ist er verhaftet (<a class=\"q\" href=\"../#ign-polizei\">IGN-Interview</a>)"),
        ],
        "sections": [
            ("Kurz und knapp: in drei Schritten weg",
             f"<ol class=\"pts\"><li><b>Sichtkontakt brechen:</b> Raus aus dem Blickfeld der Polizei, durch Gassen, Hinterhöfe, unter Brücken oder in ein Parkhaus.</li>"
             "<li><b>Suchgebiet verlassen:</b> Das Gebiet auf der Karte, in dem die Polizei sucht. Sobald die Sterne blinken, seid ihr auf dem richtigen Weg.</li>"
             "<li><b>Symbole loswerden:</b> Outfit wechseln, Maske ab, Auto tauschen. Die Polizei kann euch nur finden, wenn sie weiß, wonach sie sucht.</li></ol>"
             f"<p>{T_W} So beschreibt es Eurogamer nach dem Spielen {q(EG_POL, 'Eurogamer')}.</p>"),
            ("Was die Sterne bedeuten",
             f"<p>{T_W} Je schwerer das Vergehen, desto mehr Sterne und desto härter die Polizei. Neu ist, dass auch die Farbe der Sterne etwas aussagt {q(EG_POL, 'Eurogamer')}:</p>"
             "<table class=\"keys\"><thead><tr><th>Sterne</th><th>Bedeutung</th></tr></thead><tbody>"
             "<tr><td>Grau</td><td>Die Polizei ist auf dem Weg zum Tatort.</td></tr>"
             "<tr><td>Hohl (innen dunkel, Rand weiß)</td><td>Das Verbrechen ist bemerkt, aber die Polizei hat keine Beschreibung von euch.</td></tr>"
             "<tr><td>Weiß</td><td>Die Polizei ist euch direkt auf den Fersen und kennt euer Aussehen.</td></tr>"
             "<tr><td>Wieder grau</td><td>Ihr habt den Sichtkontakt gebrochen. Jetzt das Suchgebiet verlassen.</td></tr>"
             "<tr><td>Blinkend</td><td>Ihr hängt die Verfolger gerade ab.</td></tr>"
             "<tr><td>Rot</td><td>Die Polizei sucht weiter dort, wo ihr zuletzt gesehen wurdet. Kommt ihr zurück und fallt auf, geht die Fahndung neu los.</td></tr>"
             "<tr><td>Rot, innen schwarz</td><td>Wie rot, aber ohne Beschreibung von euch.</td></tr>"
             "</tbody></table>"
             f"<p>{T_W} Ab drei Sternen verfolgt euch ein Hubschrauber, einen sechsten Stern gibt es nur in Ausnahmefällen {q(EG_POL, 'Eurogamer')}. Bei den großen Banktresoren habt ihr sofort vier Sterne, mehr dazu im <a href=\"gta-6-geld-verdienen.html\">Ratgeber zum Geldverdienen</a>.</p>"),
            ("Die sechs Symbole und wie ihr sie loswerdet",
             f"<p>{T_W} Unter den Sternen zeigt das Spiel, was die Polizei über euch weiß. Jedes Symbol lässt sich gezielt löschen {q(EG_POL, 'Eurogamer')}:</p>"
             "<table class=\"keys\"><thead><tr><th>Symbol</th><th>So werdet ihr es los</th></tr></thead><tbody>"
             "<tr><td>Aussehen</td><td>Maske, Brille oder Hut abnehmen, die ihr bei der Tat getragen habt: L1 halten, mit R1 zu den Gegenständen wechseln, Teil auswählen (Xbox: LB, RB).</td></tr>"
             "<tr><td>Fahrzeug</td><td>Ungesehen in ein anderes Auto wechseln.</td></tr>"
             "<tr><td>Outfit</td><td>Am Kofferraum eures eigenen Autos ungesehen umziehen. In Kleidungsläden, die ihr überfallt, könnt ihr auch Outfits mitnehmen.</td></tr>"
             "<tr><td>Sichtbare Waffe</td><td>Langwaffen tragen Jason und Lucia sichtbar auf dem Rücken. In den Kofferraum legen oder fallen lassen. Eigene Waffen holt ihr euch später am Waffenschrank oder Kofferraum zurück.</td></tr>"
             "<tr><td>Partner</td><td>Jason und Lucia zusammen fallen auf. Den Partner über das Partnermenü (Steuerkreuz) mit „Aufteilen“ wegschicken.</td></tr>"
             "<tr><td>Kamera</td><td>Bei Kameras ohne Wolke steht oft im Hinterzimmer ein Rekorder, dort die Aufnahme zerstören. Kameras mit Wolke speichern in der Cloud, dagegen hilft nichts, das gibt es vor allem in Banken.</td></tr>"
             "</tbody></table>"),
            ("Fliehen: Auto, Parkhaus, Hubschrauber, Hunde",
             f"<ul class=\"pts\"><li>{T_W} <b>Beim Einsteigen nicht gesehen werden:</b> Das Fluchtauto hinter einer Mauer parken, die zwischen euch und dem Tatort liegt. Eigene Autos sind am besten, weil im Kofferraum Kleidung liegt. Ein fremdes Auto vorher leise mit dem Slim Jim knacken {q(EG_POL, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Haken schlagen:</b> Durch Hecken, Hinterhöfe und unter hoch gelegenen Autobahnen fahren, Sprünge nutzen, Frontalcrashs meiden, damit der Motor heil bleibt {q(EG_POL, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Parkhaus:</b> Der beste Ort. Der Hubschrauber sieht euch nicht, die Polizei verfährt sich oft und belagert lieber das Gebäude, und drinnen stehen Autos zum Wechseln. Oben gibt es fast immer eine Rampe, über die ihr vom Gebäude springen könnt {q(EG_POL, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Hubschrauber:</b> Unter Brücken seht ihr ihn nicht. Werdet ihr ihn nicht los, auf den Heckrotor schießen {q(EG_POL, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Spürhunde:</b> Zu Fuß setzt die Polizei manchmal Hunde ein. Dann ins Wasser springen und an eine schwer einsehbare Stelle tauchen, oder schnell in ein Auto. Im Gebüsch ducken (Kreis, Xbox: B) bricht die Sicht menschlicher Verfolger {q(EG_POL, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Pay 'n' Spray:</b> Umlackieren geht weiterhin, aber nur, wenn keine Polizei direkt hinter euch ist {q(EG_POL, 'Eurogamer')}.</li></ul>"
             "<p>Ducken im Auto, Motor laufen lassen und weitere Fahr-Tricks stehen im <a href=\"gta-6-fahren-steuerung.html\">Ratgeber zum Fahren</a>.</p>"),
            ("Gar nicht erst gesucht werden",
             f"<ul class=\"pts\"><li>{T_W} <b>Vorbereiten:</b> Maske vor der Tat aufsetzen, Wechsel-Outfit im Kofferraum, Fluchtauto versteckt parken {q(EG_POL, 'Eurogamer')}.</li>"
             f"<li>{T_W} <b>Nicht töten:</b> Wer niemanden umbringt, kommt glimpflicher davon {q(EG_POL, 'Eurogamer')}. {T_OK} Rockstar bestätigt, dass ihr eine Konfrontation mit gezogener Waffe auch ohne Schuss beenden könnt (<a href=\"../#ign-polizei\">IGN-Interview</a>).</li>"
             f"<li>{T_W} <b>Reden statt rennen:</b> Bei <b>einem</b> Stern Waffe wegstecken, mit L2 (Xbox: LT) auf den Polizisten zielen und im Interaktionsmenü „Entschärfen“ wählen. Klappt es, ist der Stern weg. Garantiert ist das nicht, manche greifen trotzdem an. Bei mehreren Sternen hilft es kaum {q(PCG_POL, 'PC Games')}.</li></ul>"
             "<p>Wie ihr bei Überfällen leise bleibt, steht im <a href=\"gta-6-geld-verdienen.html\">Ratgeber zum Geldverdienen</a>, Schleichen und Ausschalten im <a href=\"gta-6-nahkampf-steuerung.html\">Ratgeber zum Nahkampf</a>.</p>"),
            ("Verhaftung und Partner",
             f"<p>{T_OK} Seid ihr getrennt unterwegs und einer von beiden wird geschnappt, während der andere entkommt, gilt er als verhaftet. Das hat Rob Nelson von Rockstar North im IGN-Interview erklärt (<a href=\"../#ign-polizei\">IGN-Interview</a>). Zusammen unterwegs zu sein ist umgekehrt ein Erkennungsmerkmal, deshalb gibt es das Partner-Symbol {q(EG_POL, 'Eurogamer')}.</p>"),
        ],
        "faq": [
            ("Wie wird man in GTA 6 die Polizei los?", "Sichtkontakt brechen, das Suchgebiet auf der Karte verlassen und die Symbole unter den Sternen loswerden, also Outfit wechseln, Maske abnehmen und das Auto tauschen."),
            ("Was bedeuten die Farben der Sterne in GTA 6?", "Grau heißt, die Polizei ist unterwegs. Hohle Sterne heißen, sie hat keine Beschreibung. Weiß heißt, sie ist euch auf den Fersen. Blinkend heißt, ihr hängt sie ab. Rot heißt, im alten Gebiet wird noch gesucht."),
            ("Was bedeuten die Symbole unter den Sternen in GTA 6?", "Sie zeigen, was die Polizei über euch weiß: Aussehen, Fahrzeug, Outfit, sichtbare Waffe, Partner oder Kameraaufnahmen. Jedes lässt sich gezielt loswerden."),
            ("Wie viele Fahndungssterne gibt es in GTA 6?", "Normalerweise bis zu fünf, in Ausnahmefällen sechs. Ab drei Sternen kommt ein Hubschrauber."),
            ("Kann man in GTA 6 mit der Polizei reden?", "Bei einem Stern manchmal ja: Waffe wegstecken, mit L2 auf den Polizisten zielen und im Menü Entschärfen wählen. Erfolg ist nicht garantiert."),
            ("Wie wird man in GTA 6 den Hubschrauber los?", "Unter Brücken oder in ein Parkhaus fahren, dort sieht er euch nicht. Notfalls auf den Heckrotor schießen."),
        ],
    },
]

EG_EASY = "https://www.eurogamer.de/gta-6-spiel-einfacher-machen-versteckter-schwierigkeitsgrad"
PSQ_EASY = "https://www.pushsquare.com/news/2026/11/gta-6-has-an-easy-mode-buried-in-an-impressive-range-of-accessibility-options"
TG_SET = "https://www.thegamer.com/grand-theft-auto-6-best-settings-to-change-streaming-god-mode-guide/"

GUIDES += [
    {
        "slug": "gta-6-einstellungen-schwierigkeit",
        "published": "2026-11-25",
        "title": "GTA 6 Einstellungen: leichter Modus und beste Optionen",
        "h1": "GTA 6 Einstellungen: leichter spielen und besser zielen",
        "desc": "GTA 6 hat keinen Schwierigkeitsgrad, aber zwei versteckte Schalter für leichtere Kämpfe. Dazu die besten Einstellungen für Zielen, Bewegung, Streamer. Mit Quellen.",
        "lead": "GTA VI hat keinen Schwierigkeitsgrad zum Auswählen. In den Einstellungen stecken aber zwei Schalter, die das Spiel spürbar leichter machen, und viele Optionen, die das Spielgefühl verbessern. Hier steht, wo ihr was findet und was sich lohnt. <b>Offiziell</b> heißt von Rockstar, <b>Berichtet</b> heißt von Medien, die das Spiel gespielt haben. Wo wir den deutschen Namen im Menü nicht kennen, steht der englische dabei.",
        "facts": [
            ("Einstellungen", f"{T_OK} Pausenmenü, dann Einstellungen {q(R_SET, 'Rockstar')}"),
            ("Schwierigkeitsgrad", f"{T_W} Gibt es nicht, nur eine Standard-Einstellung {q(EG_EASY, 'Eurogamer')}"),
            ("Leichter Modus", f"{T_W} Reiter Gameplay ganz unten: „Erleichterter Kampf“ und „Reduzierter Fahrzeugschaden“ {q(EG_EASY, 'Eurogamer')}"),
            ("Trophäen", f"{T_W} Bleiben trotz der beiden Schalter erhalten {q(EG_EASY, 'Eurogamer')} {q(PSQ_EASY, 'Push Square')}"),
            ("Streamer", f"{T_W} Unter Audio lässt sich lizenzierte Musik stummschalten {q(TG_SET, 'TheGamer')}"),
        ],
        "sections": [
            ("So findet ihr die Einstellungen",
             f"<p>{T_OK} Pausenmenü öffnen und <b>Einstellungen</b> wählen. Laut Rockstar gibt es diese Reiter {q(R_SET, 'Rockstar')}:</p>"
             "<ul class=\"pts\"><li><b>Steuerungsschema:</b> Belegung für zu Fuß, Zielen, Nahkampf, Fahrzeuge, Fliegen, Fahrrad, Schwimmen, Fallschirm.</li>"
             "<li><b>Controller:</b> Empfindlichkeit beim Zielen und Umschauen, Invertieren, Funktionen des DualSense auf der PS5.</li>"
             "<li><b>Gameplay:</b> Kampf, Bewegung und Barrierefreiheit.</li>"
             "<li><b>Anzeige:</b> Bild, visuelle Effekte und Hochkontrast-Shader.</li>"
             "<li><b>UI:</b> Größe und Lesbarkeit, Untertitel, Navigation, Fadenkreuz, Kampf- und Fortschrittsanzeigen, Maßeinheiten.</li>"
             "<li><b>Kamera:</b> zu Fuß, Fahrzeuge, Komfort, Flugzeuge, unter Wasser, Kino.</li>"
             "<li><b>Audio:</b> Setup, Lautstärke, Sprachausgabe.</li></ul>"
             "<p>Unten auf dem Bildschirm setzt „Standard wiederherstellen“ alles zurück. Welche Taste was macht, steht im <a href=\"gta-6-nahkampf-steuerung.html\">Ratgeber zu Nahkampf und Tricks</a> und im <a href=\"gta-6-fahren-steuerung.html\">Ratgeber zum Fahren</a>.</p>"),
            ("Der versteckte leichte Modus",
             f"<p>{T_W} Ganz unten im Reiter <b>Gameplay</b> stehen zwei Schalter {q(EG_EASY, 'Eurogamer')}:</p>"
             "<ul class=\"pts\"><li><b>Erleichterter Kampf</b> (englisch: Accessible Combat): Gegner halten weniger Treffer aus, Jason und Lucia dafür mehr. Hilft vor allem gegen schwer gepanzerte Einheiten und große Gruppen.</li>"
             "<li><b>Reduzierter Fahrzeugschaden</b> (Reduced Vehicle Damage): Euer Auto geht bei Unfällen und Beschuss nicht so schnell kaputt. Ganz robust wird es trotzdem nicht, aber ihr kommt durch eine oder zwei Straßensperren mehr.</li></ul>"
             f"<p>{T_W} Das Spiel warnt beim Einschalten, dass sich Balance und Spielerlebnis deutlich ändern {q(PSQ_EASY, 'Push Square')}. Trophäen und Erfolge bleiben aber erhalten, euer Profil wird nicht markiert {q(EG_EASY, 'Eurogamer')} {q(PSQ_EASY, 'Push Square')}. Eurogamer hat die Schalter zum Üben schwerer Banküberfälle genutzt, mehr dazu im <a href=\"gta-6-geld-verdienen.html\">Ratgeber zum Geldverdienen</a>.</p>"),
            ("Die besten Einstellungen zum Start",
             f"<p>{T_W} Empfehlungen von TheGamer {q(TG_SET, 'TheGamer')} und Eurogamer {q(EG, 'Eurogamer')}:</p>"
             "<ul class=\"pts\"><li><b>Zielmodus</b> (Gameplay, Kampf): „Teilweise“ (Partial) ist voreingestellt und mit Controller am besten. Wer es leichter will, nimmt die volle Zielerfassung (Lock-On), freies Zielen ist mit Controller mühsam. Die <b>Zielhilfe</b> könnt ihr ruhig hoch stellen.</li>"
             "<li><b>Bewegungstempo</b> (Gameplay, Bewegung): legt fest, wie schnell Jason und Lucia gehen, wenn ihr den Stick ganz nach vorn drückt. Eurogamer empfiehlt „Joggen“, dann ist der Stickdruck nur noch für den Sprint da. Das Tempo im Kampf am besten auf „Rennen“.</li>"
             "<li><b>Stehen und Sprinten</b> (Stand and Sprint): ausschalten, sonst steht ihr beim Schleichen ungewollt auf.</li>"
             "<li><b>Totzone der Sticks</b> (Controller): so einstellen, wie es sich für euch am besten anfühlt.</li>"
             "<li><b>Zielbeschleunigung</b> (Controller, Empfindlichkeit): etwas höher macht das Zielen direkter.</li>"
             "<li><b>Steuerungsschema „Klassisch“:</b> nur, wenn ihr wie früher per Tastenhämmern rennen wollt. Für alle anderen ist „Standard“ besser.</li></ul>"),
            ("Anzeige, Untertitel und Komfort",
             f"<p>{T_W} Ebenfalls nach TheGamer {q(TG_SET, 'TheGamer')}:</p>"
             "<ul class=\"pts\"><li><b>Untertitel und Sprechernamen an:</b> Über Gespräche, die ihr nebenbei hört, entdeckt ihr Nebenaufgaben.</li>"
             "<li><b>Bewegungsunschärfe</b> (Anzeige, visuelle Effekte): senken statt ganz ausschalten. Das Spiel läuft mit 30 Bildern pro Sekunde, ganz ohne Unschärfe wirkt es ruckeliger.</li>"
             "<li><b>Wurfbahn immer anzeigen</b> (Projectile Arc) und <b>Straßennamen</b> an.</li>"
             "<li><b>Minikarte</b> dauerhaft an statt „dynamisch“, dazu der Kompass.</li>"
             "<li><b>Kamerawackeln aus und Kamerawippen niedriger</b> (Kamera, Komfort), wenn euch schnell schwindelig wird.</li>"
             "<li><b>Unfall-Kamera seltener</b> (Kamera, Kino): Dann unterbrechen Zeitlupen-Crashs die Fahrt nicht so oft.</li>"
             "<li><b>Tinnitus-Reduzierung</b> (Audio, Setup) beim Spielen mit Kopfhörern.</li>"
             "<li><b>Musik etwas leiser</b>, damit Dialoge nicht untergehen.</li></ul>"),
            ("Für Streamer und YouTube",
             f"<ul class=\"pts\"><li>{T_W} <b>Lizenzierte Musik stummschalten</b> (Audio, Setup, englisch: Mute Licensed Music): Dann laufen keine Radio-Songs, die zu Urheberrechts-Sperren auf Twitch oder YouTube führen können {q(TG_SET, 'TheGamer')}.</li>"
             f"<li>{T_W} <b>Blut und Gewalt</b> (Anzeige, visuelle Effekte): Intensität senken und abgetrennte Gliedmaßen ausschalten {q(TG_SET, 'TheGamer')}.</li>"
             f"<li>{T_W} <b>Nacktheit</b> lässt sich nicht abschalten, außer in Fassungen, die ab Werk geschnitten sind, etwa in Japan. Im Zweifel schneiden {q(TG_SET, 'TheGamer')}.</li></ul>"),
            ("Barrierefreiheit",
             f"<p>{T_W} Rockstar hat viele Optionen eingebaut, die Medien loben die Auswahl {q(PSQ_EASY, 'Push Square')}:</p>"
             f"<ul class=\"pts\"><li><b>Tippen statt Hämmern</b> (Gameplay, Barrierefreiheit, englisch: Tap Assist): Statt schnell zu drücken, haltet ihr die Taste, oder ein Druck zählt mehrfach {q(TG_SET, 'TheGamer')}.</li>"
             f"<li><b>Vereinfachte Minispiele:</b> Weniger komplizierte Eingaben bei Minispielen {q(PSQ_EASY, 'Push Square')}.</li>"
             f"<li><b>Autopilot ohne Einschränkung</b> (Auto Drive): Dann fährt euch die Figur auf mehr Strecken selbst {q(TG_SET, 'TheGamer')}. Wie der Autopilot geht, steht im <a href=\"gta-6-fahren-steuerung.html\">Ratgeber zum Fahren</a>.</li>"
             f"<li>{T_OK} <b>Hochkontrast-Shader</b> (Anzeige) und Größe und Lesbarkeit der Anzeigen (UI) {q(R_SET, 'Rockstar')}, dazu Optionen für Spieler mit eingeschränktem Sehvermögen {q(PSQ_EASY, 'Push Square')}.</li>"
             f"<li><b>Zielhilfe und Zielerfassung</b> lassen sich ebenfalls anpassen {q(PSQ_EASY, 'Push Square')}.</li></ul>"),
        ],
        "faq": [
            ("Hat GTA 6 einen Schwierigkeitsgrad?", "Nein, nur eine Standard-Einstellung. Im Reiter Gameplay gibt es aber die Schalter Erleichterter Kampf und Reduzierter Fahrzeugschaden, die das Spiel leichter machen."),
            ("Verliert man Trophäen, wenn man den leichten Modus nutzt?", "Nein. Laut Eurogamer und Push Square bleiben Trophäen und Erfolge erhalten, auch mit Erleichtertem Kampf und Reduziertem Fahrzeugschaden."),
            ("Welcher Zielmodus ist in GTA 6 am besten?", "Mit Controller der voreingestellte Modus Teilweise (Partial) mit hoher Zielhilfe. Wer es leichter will, nimmt die volle Zielerfassung."),
            ("Wie stellt man in GTA 6 das Gehtempo ein?", "Im Reiter Gameplay unter Bewegung. Eurogamer empfiehlt Joggen, dann ist der gedrückte Stick nur noch für den Sprint da."),
            ("Kann man in GTA 6 die Radiomusik für Streams abschalten?", "Ja, unter Audio lässt sich lizenzierte Musik stummschalten. Das hilft gegen Urheberrechts-Sperren auf Twitch und YouTube."),
        ],
    },
]

ORDER = ["gta-6-release-deutschland", "gta-6-nahkampf-steuerung", "gta-6-fahren-steuerung", "gta-6-geld-verdienen", "gta-6-polizei-fahndung", "gta-6-einstellungen-schwierigkeit", "gta-6-vorab-download", "gta-6-editionen", "gta-6-usk-ab-18",
         "gta-6-charaktere", "gta-6-karte-leonida", "gta-6-soundtrack-radio", "gta-6-pc-version"]
THUMB = {"gta-6-release-deutschland": "launch_03", "gta-6-vorab-download": "launch_39", "gta-6-editionen": "ue_01",
         "gta-6-usk-ab-18": "launch_02", "gta-6-charaktere": "jason_and_lucia_02", "gta-6-karte-leonida": "vice_city_01",
         "gta-6-soundtrack-radio": "radio_01", "gta-6-pc-version": "launch_35", "gta-6-nahkampf-steuerung": "lucia_caminos_01", "gta-6-fahren-steuerung": "launch_27", "gta-6-geld-verdienen": "jason_and_lucia_02", "gta-6-polizei-fahndung": "jason_and_lucia_09", "gta-6-einstellungen-schwierigkeit": "jason_and_lucia_03"}
GUIDES.sort(key=lambda g: ORDER.index(g["slug"]) if g["slug"] in ORDER else 99)

HUB_CSS = """main{max-width:1040px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin:24px 0}
.card{display:block;background:var(--panel);border:1px solid var(--line);border-radius:8px;overflow:hidden;color:var(--fg);text-decoration:none;transition:border-color .2s,transform .2s}
.card:hover,.card:focus-visible{border-color:var(--gold);transform:translateY(-2px)}
.card img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover}
.card div{padding:12px 14px 14px}.card h2{font:900 21px/1.1 var(--display);letter-spacing:.02em;margin:0 0 6px}
.card p{margin:0;color:var(--muted);font-size:14px;line-height:1.5}
@media(prefers-reduced-motion:reduce){.card:hover{transform:none}}"""


def render_index():
    e = html.escape
    url = SITE + "ratgeber/"
    cards = "".join(
        f'<a class="card" href="{g["slug"]}.html"><img src="../thumbs/official/{THUMB.get(g["slug"], "launch_01")}.webp" alt="" loading="lazy" decoding="async" width="800" height="450">'
        f'<div><h2>{e(g["h1"])}</h2><p>{e(g["desc"])}</p></div></a>' for g in GUIDES)
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "GTA 6 Ratgeber", "url": url, "inLanguage": "de-DE",
           "hasPart": [{"@type": "Article", "headline": g["title"], "url": f"{url}{g['slug']}.html"} for g in GUIDES]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "GTA 6 News", "item": SITE},
              {"@type": "ListItem", "position": 2, "name": "Ratgeber", "item": url}]}]
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    desc = "Alle GTA 6 Ratgeber auf Deutsch: Release-Uhrzeit, Nahkampf-Steuerung, Fahren, Geld verdienen, Polizei, Einstellungen, Download, Editionen, USK, Charaktere, Karte, Musik und PC-Version. Jede Angabe mit Quelle."
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>GTA 6 Ratgeber: alles zum Release | LNN</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Leonida News Network">
<meta property="og:title" content="GTA 6 Ratgeber: alles zum Release">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}og.jpg?v=2">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#07070c">
<link rel="icon" href="../favicon.ico?v=2" sizes="48x48">
<link rel="icon" href="../favicon.svg?v=2" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png?v=2">
<link rel="stylesheet" href="../fonts/fonts.css?v=2">
{lds}<style>
{CSS}
{HUB_CSS}
</style>
</head>
<body>
<header class="top"><a class="logo" href="../"><i>LNN</i> Leonida News Network</a><a class="live" href="../#live">Zum Liveticker</a></header>
<main>
<nav class="crumb" aria-label="Brotkrümel"><a href="../">GTA 6 News</a> › Ratgeber</nav>
<h1>GTA 6 Ratgeber</h1>
<p class="meta">Stand: {STAND[1]} · {len(GUIDES)} Ratgeber · wird bei neuen Infos aktualisiert</p>
<p>Alles, was du zum Start von GTA VI wissen musst, kompakt auf je einer Seite. Wie im Liveticker trägt jede Angabe einen Stempel: Offiziell, Berichtet oder Offen, mit Link zur Quelle.</p>
<div class="grid">{cards}</div>
<a class="cta" href="../">Alle GTA 6 News im Liveticker</a>
</main>
<footer>Leonida News Network · GTA 6 News auf Deutsch, jede Meldung mit Quellenstempel · Inoffizielle Fanseite, nicht verbunden mit Rockstar Games oder Take-Two<br><a href="../impressum.html">Impressum</a> · <a href="../datenschutz.html">Datenschutz</a><a class="xc" href="https://xetcraft.de" title="Xetcraft: die Werkstatt von XetrovT2000"><span>Ein Projekt von</span><img src="../xetcraft-logo.png" width="95" height="22" alt="Xetcraft"></a></footer>
<script data-goatcounter="https://gta6-infoboard.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
"""


def build():
    out = ROOT / "ratgeber"
    out.mkdir(exist_ok=True)
    for g in GUIDES:
        (out / f"{g['slug']}.html").write_text(render(g), encoding="utf-8", newline="\n")
    (out / "index.html").write_text(render_index(), encoding="utf-8", newline="\n")
    return ["ratgeber/"] + [f"ratgeber/{g['slug']}.html" for g in GUIDES]


if __name__ == "__main__":
    for p in build():
        print(p)
