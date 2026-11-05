"""Erzeugt die Ratgeber-Seiten unter ratgeber/<slug>.html (feste Seiten zu Fragen, die Leute googeln).

Inhalt steht unten in GUIDES. Bei neuen Fakten: Text anpassen, STAND setzen, `py tools/build_guides.py`
(läuft auch automatisch über build_pages.py), dann IndexNow. Keine Gedankenstriche in den Texten.
"""
import html, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://leonida-news.de/"
STAND = ("2026-11-05", "5. November 2026")

PSD = "https://store.playstation.com/de-de/product/EP1004-PPSA01547_00-GTAVIULTIMATE001"
R_PRE = "https://www.rockstargames.com/newswire/article/5171972o3ak5oa/pre-order-grand-theft-auto-vi-on-june-25"
R_LOAD = "https://www.rockstargames.com/newswire/article/k4ak9okk485712/grand-theft-auto-vi-pre-load-begins-on-november-10"
PS_LOAD = "https://blog.playstation.com/2026/11/03/grand-theft-auto-vi-pre-download-begins-november-10/"
VGC_LOAD = "https://www.videogameschronicle.com/news/rockstar-details-grand-theft-auto-6-pre-load-date-and-time-and-file-size/"
USK = "https://usk.de/digitaler-elternabend-gta-vi-ist-ab-18-was-eltern-wissen-mussen/"
PEGI = "https://store.playstation.com/en-gb/product/EP1004-PPSA01547_00-GTAVISTANDARD001"
R_VI = "https://www.rockstargames.com/VI"
GB = "https://gamesbeat.com/grand-theft-auto-vis-pc-release-is-slated-for-q1-2027/"
XCLOUD = "https://www.gosugamers.net/entertainment/news/79311-xbox-denies-claims-that-gta-vi-will-stream-exclusively-through-xbox-cloud-gaming"
POLY = "https://www.polygon.com/gta-6-preorders-sales-8-million-copies-before-release-date/"


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
        "desc": "GTA 6 erscheint am 19. November 2026. Uhrzeit in Deutschland, Preise, Editionen, Vorab-Download, USK und PC-Version, jede Angabe mit Quelle.",
        "lead": "GTA VI erscheint am <b>Donnerstag, 19. November 2026</b> für PlayStation 5 und Xbox Series X|S. Hier steht kompakt, was für Spieler in Deutschland wichtig ist. Jede Zeile trägt einen Stempel: <b>Offiziell</b> heißt von Rockstar, Sony, Microsoft oder der USK bestätigt, <b>Berichtet</b> heißt von seriösen Medien gemeldet, <b>Offen</b> heißt noch nicht bekannt.",
        "facts": [
            ("Release", f"{T_OK} Donnerstag, 19. November 2026 {q(R_PRE, 'Rockstar')}"),
            ("Plattformen", f"{T_OK} PlayStation 5 und Xbox Series X|S, PS5 Pro Enhanced {q(PSD, 'PS Store')}"),
            ("Uhrzeit PS5", f"{T_OK} 19. November, 0:00 Uhr laut deutschem PlayStation Store {q(PSD, 'PS Store')}"),
            ("Uhrzeit Xbox", f"{T_O} Noch nicht bekannt"),
            ("Vorab-Download", f"{T_OK} Ab 10. November für digitale Vorbestellungen, bis zu 212 GB {q(R_LOAD, 'Rockstar')} {q(PS_LOAD, 'PlayStation')}"),
            ("Preis", f"{T_OK} Standard 79,99 €, Ultimate Edition 99,99 € {q(PSD, 'PS Store')}"),
            ("Altersfreigabe", f"{T_OK} USK: keine Jugendfreigabe (ab 18) {q(USK, 'USK')}"),
            ("PC-Version", f"{T_O} Nicht angekündigt, Bericht über Anfang 2027 {q(GB, 'GamesBeat')}"),
        ],
        "sections": [
            ("Um wie viel Uhr geht es los?",
             f"<p>Im deutschen PlayStation Store ist die Freischaltung für den <b>19. November um 0:00 Uhr</b> eingetragen {q(PSD, 'PS Store')}. Wer digital vorbestellt und vorab geladen hat, kann also in der Nacht von Mittwoch auf Donnerstag direkt um Mitternacht starten.</p>"
             "<p>Für die Xbox hat Microsoft noch keine Uhrzeit genannt. Beim Vorab-Download galt auf der Xbox britische Zeit, also 1 Uhr bei uns. Ob das auch für den Start gilt, ist offen. Wir tragen die Uhrzeit nach, sobald sie feststeht.</p>"),
            ("Was kostet GTA 6?",
             f"<p>Die <b>Standard Edition kostet 79,99 €</b>, die <b>Ultimate Edition 99,99 €</b> {q(PSD, 'PS Store')} {q('https://store.rockstargames.com/de/game/buy-gta-vi', 'Rockstar Store')}. Die Ultimate Edition bringt zusätzliche Autos, Waffen, Kleidung und Läden. Ein Upgrade ist auch später möglich.</p>"
             f"<p>Die Box-Version im Handel enthält <b>keine Disc</b>, nur einen Download-Code. Sie liegt ab dem 12. November in den Läden {q(VGC_LOAD, 'VGC')}. Wer vor dem 20. November kauft, bekommt das Vintage Vice City Pack, digitale Vorbesteller zusätzlich einen Monat GTA+ {q(R_PRE, 'Rockstar')}.</p>"
             f"<p>Die Sammlerbox „The Goodtime State: Vice City Collection“ für 399,99 € enthält Figur, Brille, Cap und mehr, aber <b>nicht das Spiel</b>.</p>"),
            ("Ab wann kann ich vorladen?",
             f"<p>Ab <b>10. November</b>: auf der PS5 ab Mitternacht Ortszeit, auf der Xbox ab 1 Uhr deutscher Zeit. Das Spiel braucht <b>bis zu 212 GB</b> {q(PS_LOAD, 'PlayStation')} {q(VGC_LOAD, 'VGC')}. Alle Details stehen im <a href=\"gta-6-vorab-download.html\">Ratgeber zum Vorab-Download</a>.</p>"),
            ("Ab welchem Alter ist GTA 6?",
             f"<p>Die USK hat GTA VI mit <b>keine Jugendfreigabe</b> gekennzeichnet, das Spiel ist also ab 18 {q(USK, 'USK')}. In Europa gilt PEGI 18, in den USA „Mature 17+“. Mehr dazu im <a href=\"gta-6-usk-ab-18.html\">Ratgeber zur Altersfreigabe</a>.</p>"),
            ("Kommt GTA 6 für den PC?",
             f"<p>Bisher <b>nicht angekündigt</b>. GamesBeat berichtet mit Berufung auf anonyme Quellen von einem PC-Start im ersten Quartal 2027 {q(GB, 'GamesBeat')}. Den <a href=\"gta-6-pc-version.html\">Stand zur PC-Version</a> halten wir aktuell.</p>"),
            ("Wie lang ist die Story, gibt es Online?",
             "<p>Rob Nelson von Rockstar North brauchte nach eigener Aussage rund <b>80 Stunden</b> für einen Story-Durchgang mit Nebenzielen. GTA VI ist ein Einzelspieler-Spiel und offline spielbar. Ein neues GTA Online hat Rockstar noch nicht angekündigt, berichtet wird ein Start 2027.</p>"
             f"<p>Wie groß der Andrang ist: Sensor Tower schätzt rund 7,7 Millionen digitale Vorbestellungen {q(POLY, 'Polygon')}. Rockstar selbst nennt keine Zahlen.</p>"),
        ],
        "faq": [
            ("Wann erscheint GTA 6 in Deutschland?", "Am Donnerstag, 19. November 2026, für PlayStation 5 und Xbox Series X|S."),
            ("Um wie viel Uhr kann man GTA 6 spielen?", "Auf der PS5 laut deutschem PlayStation Store ab 19. November, 0:00 Uhr. Für die Xbox ist die Uhrzeit noch nicht bekannt."),
            ("Was kostet GTA 6?", "Die Standard Edition kostet 79,99 Euro, die Ultimate Edition 99,99 Euro."),
            ("Hat die GTA 6 Box-Version eine Disc?", "Nein. Die Box-Version enthält nur einen Download-Code und liegt ab dem 12. November im Handel."),
            ("Kommt GTA 6 für den PC?", "Eine PC-Version ist nicht angekündigt. Berichte nennen das erste Quartal 2027, bestätigt ist das nicht."),
        ],
    },
    {
        "slug": "gta-6-vorab-download",
        "title": "GTA 6 Vorab-Download: Uhrzeit und Größe (212 GB)",
        "h1": "GTA 6 vorab laden: wann, wie groß, wie",
        "desc": "GTA 6 Vorab-Download ab 10. November: PS5 ab Mitternacht, Xbox ab 1 Uhr deutscher Zeit. Bis zu 212 GB, so machst du Platz. Mit Quellen.",
        "lead": "Wer GTA VI digital vorbestellt hat, muss am Release-Tag nicht stundenlang warten: Das Spiel lässt sich <b>ab dem 10. November</b> vorab laden, neun Tage vor dem Start.",
        "facts": [
            ("Start PS5", f"{T_OK} 10. November, 0:00 Uhr Ortszeit {q(PS_LOAD, 'PlayStation')}"),
            ("Start Xbox", f"{T_OK} 10. November, 0:00 Uhr britische Zeit, also 1:00 Uhr in Deutschland {q(VGC_LOAD, 'VGC')}"),
            ("Größe", f"{T_OK} Bis zu 212 GB, je nach Gerät {q(R_LOAD, 'Rockstar')}"),
            ("Freier Speicher", f"{T_OK} Sony rät zu mindestens 212 GB freiem Platz {q(PS_LOAD, 'PlayStation')}"),
            ("Wer darf vorladen", f"{T_OK} Digitale Vorbestellungen {q(PS_LOAD, 'PlayStation')}"),
            ("Box-Version", f"{T_OK} Nur Download-Code, im Handel ab 12. November {q(VGC_LOAD, 'VGC')}"),
            ("Spielen ab", f"{T_OK} 19. November, PS5 ab 0:00 Uhr {q(PSD, 'PS Store')}"),
        ],
        "sections": [
            ("So funktioniert der Vorab-Download",
             "<p>Auf der <b>PS5</b> startet der Download nach der Vorbestellung im PlayStation Store automatisch, wenn die Konsole im Ruhemodus mit dem Internet verbunden ist und automatische Downloads eingeschaltet sind. Sonst findest du GTA VI in der Spielebibliothek unter „Gekauft“ und startest den Download dort.</p>"
             "<p>Auf der <b>Xbox Series X|S</b> erscheint das Spiel nach der Vorbestellung unter „Meine Spiele und Apps“ in der Warteschlange. Läuft der Download nicht von selbst an, dort auf Installieren gehen.</p>"
             "<p>Spielen lässt sich GTA VI erst, wenn es am 19. November freigeschaltet wird. Am Release-Tag kann trotzdem noch ein Update nötig sein, plane dafür etwas Zeit ein.</p>"),
            ("Reicht mein Speicher?",
             "<p>212 GB sind viel. Auf einer PS5 mit 825 GB bleiben nach dem System nur gut 660 GB frei, auf der Xbox Series S mit 512 GB rund 360 GB. Mach also rechtzeitig Platz:</p>"
             "<ul class=\"pts\"><li>Große Spiele, die du gerade nicht spielst, löschen. Spielstände liegen in der Cloud oder bleiben auf der Konsole.</li>"
             "<li>PS4-Spiele und ältere Xbox-Spiele auf eine externe USB-Festplatte verschieben.</li>"
             "<li>Eine M.2-SSD in der PS5 oder eine Speichererweiterungskarte für die Xbox schafft dauerhaft Platz.</li></ul>"),
            ("Was ist mit der Box-Version?",
             f"<p>Die Box im Handel enthält <b>keine Disc</b>, nur einen Code. Sie kommt am 12. November in die Läden {q(VGC_LOAD, 'VGC')}. Laut Rockstar erscheint sie so früh, damit auch Box-Käufer vorab laden können: Code einlösen, dann startet der Download wie bei der digitalen Fassung {q(R_PRE, 'Rockstar')}. Vorladen geht damit ab dem 12. November, digital schon ab dem 10.</p>"
             "<p>Alles andere zum Start, also Preis, Editionen und Uhrzeit, steht im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>.</p>"),
        ],
        "faq": [
            ("Wann kann man GTA 6 vorladen?", "Ab dem 10. November 2026. Auf der PS5 ab Mitternacht Ortszeit, auf der Xbox ab 1 Uhr deutscher Zeit."),
            ("Wie groß ist GTA 6?", "Rockstar nennt bis zu 212 GB, je nach Gerät. Sony rät, mindestens 212 GB freizumachen."),
            ("Kann man mit der Box-Version vorladen?", "Ja. Die Box enthält einen Download-Code und kommt am 12. November in den Handel, laut Rockstar extra so früh, damit man vorladen kann. Digital geht es schon ab dem 10. November."),
            ("Kann man GTA 6 nach dem Vorab-Download schon spielen?", "Nein. Spielbar ist es erst ab dem Release am 19. November, auf der PS5 ab 0 Uhr."),
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
             "<p>Dazu gibt es keine Aussage von Rockstar oder der USK. GTA V erschien in Deutschland ungeschnitten. Sobald es belastbare Angaben gibt, tragen wir sie hier ein.</p>"),
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
        "desc": "GTA 6 PC: Rockstar hat noch keine PC-Version angekündigt. Was Berichte sagen (Anfang 2027), was Xbox dementiert hat und was du jetzt tun kannst.",
        "lead": "Zum Release am 19. November erscheint GTA VI <b>nur für PlayStation 5 und Xbox Series X|S</b>. Eine PC-Version hat Rockstar bisher nicht angekündigt.",
        "facts": [
            ("PC-Version", f"{T_O} Von Rockstar nicht angekündigt"),
            ("Bericht", f"{T_W} PC-Start im ersten Quartal 2027, laut vier anonymen Quellen {q(GB, 'GamesBeat')}"),
            ("Streaming am PC", f"{T_OK} Xbox hat am 7. Oktober dementiert, dass GTA VI zum Start per Xbox Cloud am PC läuft {q(XCLOUD, 'GosuGamers')}"),
            ("Konsolen", f"{T_OK} PS5 und Xbox Series X|S ab 19. November {q(R_PRE, 'Rockstar')}"),
        ],
        "sections": [
            ("Was ist bekannt?",
             f"<p>Rockstar spricht offiziell nur von PS5 und Xbox Series X|S. GamesBeat berichtete am 13. Oktober, der PC-Start sei für Januar bis März 2027 geplant, die PC-Fassung müsse vorher dieselbe Qualitätsprüfung bestehen wie die Konsolenversion {q(GB, 'GamesBeat')}. Bestätigt hat Rockstar das nicht.</p>"
             "<p>Bei früheren Teilen kam der PC deutlich später: GTA V erschien gut anderthalb Jahre nach der Konsolenfassung, Red Dead Redemption 2 rund ein Jahr danach.</p>"),
            ("Kann ich GTA 6 per Cloud am PC spielen?",
             f"<p>Zum Start nicht. Ein Bericht über exklusive Streaming-Rechte für Xbox Cloud Gaming wurde am 7. Oktober von Xbox-Strategiechef Matthew Ball zurückgewiesen {q(XCLOUD, 'GosuGamers')}.</p>"),
            ("Was heißt das für PC-Spieler?",
             "<p>Wer zum Start spielen will, braucht eine PS5 oder Xbox Series X|S. Wer warten kann, sollte nichts für den PC vorbestellen, solange es keine offizielle Ankündigung gibt: Angebote für „GTA 6 PC Keys“ sind derzeit unseriös.</p>"
             "<p>Alles zum Konsolen-Release steht im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>. Neue Infos zur PC-Version landen zuerst in unserem <a href=\"../\">Liveticker</a>.</p>"),
        ],
        "faq": [
            ("Kommt GTA 6 für den PC?", "Rockstar hat noch keine PC-Version angekündigt. GamesBeat berichtet von einem PC-Start im ersten Quartal 2027."),
            ("Kann man GTA 6 am PC streamen?", "Zum Start nicht. Xbox hat am 7. Oktober dementiert, dass GTA 6 zum Release über Xbox Cloud Gaming am PC spielbar ist."),
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
            ("Sprecher", f"{T_O} Rockstar hat die Besetzung nicht veröffentlicht"),
        ],
        "sections": [
            ("Jason Duval",
             "<p>Armeeveteran, der sein Leben lang von Kriminellen umgeben war. Zu Beginn arbeitet er für Drogenschmuggler in den Leonida Keys.</p>"),
            ("Lucia Caminos",
             "<p>Stammt aus Liberty City und wurde von ihrem Vater im Kampfsport trainiert. Sie saß im Leonida Penitentiary und will nach der Entlassung endlich das gute Leben. Ihre <b>Fußfessel</b> spielt laut Rockstar in der Geschichte eine wichtige Rolle.</p>"),
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
        "lead": "GTA VI gibt es in zwei Editionen: <b>Standard für 79,99 €</b> und <b>Ultimate für 99,99 €</b>. Dazu bekommen alle, die vor dem 20. November kaufen, das <b>Vintage Vice City Pack</b>. Hier steht, was genau drin ist.",
        "facts": [
            ("Standard Edition", f"{T_OK} 79,99 €, das komplette Spiel {q(PSD, 'PS Store')}"),
            ("Ultimate Edition", f"{T_OK} 99,99 €, Spiel plus Zusatzinhalte, Upgrade auch später möglich {q(PSD, 'PS Store')}"),
            ("Vorbesteller-Bonus", f"{T_OK} Vintage Vice City Pack für alle Käufe vor dem 20. November {q(R_PRE, 'Rockstar')}"),
            ("GTA+", f"{T_OK} Ein Monat gratis bei digitaler Vorbestellung {q(R_PRE, 'Rockstar')}"),
            ("Box-Version", f"{T_OK} Download-Code statt Disc, ab 12. November im Handel {q(R_PRE, 'Rockstar')}"),
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
             f"<p>Das Paket bekommt jeder, der <b>vor dem 20. November</b> kauft, egal welche Edition {q(R_PRE, 'Rockstar')}:</p>"
             "<ul class=\"pts\"><li><b>’55 Vapid Stanier:</b> Oldtimer-Limousine samt Garage Shore Court an Ocean Beach, mit Waffenschrank und Hehlerlager.</li>"
             "<li><b>Outfits und Frisuren:</b> Jason im Leinenanzug in Pastell, Lucia im roten Paillettenkleid.</li>"
             "<li><b>Waffenmuster:</b> Palmen-Muster nach Tommy Vercettis Hemd aus GTA Vice City.</li></ul>"),
            ("Lohnt sich die Ultimate Edition?",
             "<p>Für 20 € mehr gibt es kein zusätzliches Story-Kapitel, aber spürbar mehr Spielwelt: ein Salon, ein Klamottenladen, ein Tattoo-Studio und zwei Werkstätten öffnen nur damit, dazu Fahrzeuge, ein Bandengelände und ein Sammelauftrag. Wer viel Zeit in Leonida verbringen will, bekommt also mehr zu tun. Wer nur die Geschichte spielen will, verpasst nichts Wesentliches.</p>"
             "<p>Gut zu wissen: Das Upgrade lässt sich auch später kaufen. Man kann also mit der Standard Edition starten und erst danach entscheiden.</p>"
             "<p>Uhrzeit, Vorab-Download und Altersfreigabe stehen im <a href=\"gta-6-release-deutschland.html\">Ratgeber zum Release in Deutschland</a>.</p>"),
        ],
        "faq": [
            ("Was kostet die GTA 6 Ultimate Edition?", "99,99 Euro. Die Standard Edition kostet 79,99 Euro."),
            ("Was ist in der GTA 6 Ultimate Edition enthalten?", "Unter anderem ein Grotti Cheetah, zwei Revolver, ein Boot, ein Buggy mit Garage, eigene Outfits und Tattoos sowie mehrere Läden und Werkstätten, die nur mit der Ultimate Edition öffnen."),
            ("Kann man später auf die Ultimate Edition upgraden?", "Ja, laut PlayStation Store ist ein Upgrade auch später möglich."),
            ("Wer bekommt das Vintage Vice City Pack?", "Alle, die GTA 6 vor dem 20. November 2026 kaufen oder vorbestellen, egal welche Edition."),
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
             f"<p>Eine offizielle Gesamtkarte hat Rockstar noch nicht veröffentlicht. Zum Release gibt es laut Rockstar eine Karte von Leonida als kostenlosen Download {q(VGC_LOAD, 'VGC')}. Wir verlinken sie hier, sobald sie da ist.</p>"),
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
        "desc": "GTA 6 Soundtrack: The Album mit 34 Songs am 19. November, Filmmusik von Justice am 11. Dezember, alle bekannten Singles und Radiosender. Mit Quellen.",
        "lead": "Zu GTA VI gibt es zwei Alben: <b>„Grand Theft Auto VI: The Album“</b> mit 34 neuen Songs am 19. November und die <b>Filmmusik von Justice</b> am 11. Dezember. Im Spiel kommt die größte Radioauswahl der Reihe dazu.",
        "facts": [
            ("The Album", f"{T_OK} 34 neue Songs, erscheint am 19. November {q(R_ALBUM, 'Rockstar')}"),
            ("Original Score", f"{T_OK} Justice, 30 Stücke plus Bonus-Tracks, erscheint am 11. Dezember {q(R_MUSIC, 'Rockstar')}"),
            ("Radio", f"{T_OK} Größte Radioauswahl der Reihe, erstmals mit Podcasts {q(R_RADIO, 'Rockstar')}"),
            ("Vinyl und CD", f"{T_OK} Beide Alben vorbestellbar {q(R_MUSIC, 'Rockstar')}"),
        ],
        "sections": [
            ("Die Singles von „The Album“",
             f"<p>Diese Songs sind schon draußen {q(R_MUSIC, 'Rockstar')}:</p><ul class=\"pts\">"
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
            ("Wann erscheint der GTA 6 Soundtrack?", "„Grand Theft Auto VI: The Album“ erscheint am 19. November 2026 zusammen mit dem Spiel. Die Filmmusik von Justice folgt am 11. Dezember."),
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
         "datePublished": "2026-11-05", "dateModified": STAND[0],
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


ORDER = ["gta-6-release-deutschland", "gta-6-vorab-download", "gta-6-editionen", "gta-6-usk-ab-18",
         "gta-6-charaktere", "gta-6-karte-leonida", "gta-6-soundtrack-radio", "gta-6-pc-version"]
THUMB = {"gta-6-release-deutschland": "launch_03", "gta-6-vorab-download": "launch_39", "gta-6-editionen": "ue_01",
         "gta-6-usk-ab-18": "launch_02", "gta-6-charaktere": "jason_and_lucia_02", "gta-6-karte-leonida": "vice_city_01",
         "gta-6-soundtrack-radio": "radio_01", "gta-6-pc-version": "launch_35"}
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
    desc = "Alle GTA 6 Ratgeber auf Deutsch: Release-Uhrzeit, Vorab-Download, Editionen, USK, Charaktere, Karte, Musik und PC-Version. Jede Angabe mit Quelle."
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
