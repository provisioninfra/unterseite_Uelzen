#!/usr/bin/env python3
"""Baut die Elementor-Daten (elements + page settings + Yoast-Werte) der Seite /uelzen/.

Quelle ist die fertige Lüneburg-Seite (Repo provisioninfra/schliessanlagen-lueneburg,
elementor/lueneburg.elementor.json; Kopie in elementor/quelle-lueneburg.elementor.json).
Design, Animationen, Medien und Abschnittsfolge bleiben 1:1 erhalten. Ersetzt werden
ausschließlich Texte, Anker-Bezeichnungen, Menü-Slug, FAQ, Schema-Markup und SEO-Werte –
alle Inhalte neu für Uelzen und den Landkreis Uelzen formuliert (keine Textduplikate zur
Lüneburg-Seite).

Aufruf: python3 -I tools/build_uelzen.py elementor/quelle-lueneburg.elementor.json elementor [--publish]
Erzeugt: elementor/uelzen.elementor.json, elementor/media-alt-texte.json, seo/uelzen-texte.md
"""
import copy, json, os, random, re, sys

SRC = sys.argv[1]
OUT = sys.argv[2]
POST_STATUS = 'publish' if '--publish' in sys.argv else 'draft'  # neue Seite zuerst als Entwurf prüfen

L = json.load(open(SRC, encoding='utf-8'))
GEO = json.load(open(os.path.join(os.path.dirname(SRC), 'geo.json'), encoding='utf-8'))

SITE = 'https://provision-infra.de'
SLUG = 'uelzen'
PAGE_URL = f'{SITE}/{SLUG}/'
FUNNEL_URL = '/anfrage-auswahl/'      # gemeinsamer Funnel aller Stadtseiten (Formular „Funnel Auswahl“, ID 5)
MENU_SLUG = 'menue-uelzen'            # WordPress-Menü „Menü Uelzen“ (muss in WP angelegt werden, Name mit „Me…“ beginnen)


def walk(e):
    yield e
    for c in e.get('elements', []):
        yield from walk(c)


def _find(els, eid):
    for e in els:
        if e['id'] == eid:
            return e
        r = _find(e.get('elements', []), eid)
        if r:
            return r
    return None


def find(els, eid):
    r = _find(els, eid)
    if r is None:
        raise KeyError(eid)
    return r


def set_setting(els, eid, key, value):
    find(els, eid)['settings'][key] = value


used = set()
random.seed('uelzen-2026')  # reproduzierbare IDs für neue Elemente (FAQ-Einträge)


def new_id():
    while True:
        i = '%07x' % random.randrange(16 ** 7)
        if i not in used:
            used.add(i)
            return i


class Mapping(dict):
    """Exakte Textersetzung; merkt sich, welche Schlüssel getroffen wurden."""
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.hits = set()


def replace_text(els, mapping):
    def rep(v):
        if isinstance(v, str):
            for a, b in mapping.items():
                if a in v:
                    v = v.replace(a, b)
                    mapping.hits.add(a)
            return v
        if isinstance(v, list):
            return [rep(x) for x in v]
        if isinstance(v, dict):
            return {k: rep(x) for k, x in v.items()}
        return v
    for root in els:
        for e in walk(root):
            e['settings'] = rep(e['settings'])


# ================================================================== Inhalte Uelzen
H1 = ('<span style="font-weight: 700;">Mechanische &amp; elektronische Schließanlagen</span>'
      '<br>sowie Videoüberwachung in Uelzen')

HERO_SUB = ('Nachgemachte Schlüssel im Umlauf, ein Lager am Stadtrand ohne Blick aufs Tor, eine Hintertür, die jeder kennt: '
            'Solche Lücken fallen in Uelzener Betrieben meist erst auf, wenn etwas fehlt. <br><br>'
            'ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Uelzen '
            'und im ganzen Landkreis – mechanisch, elektronisch oder beides zusammen. Unser Sitz liegt in Bad Bevensen, '
            'keine 20 Minuten von der Uelzener Innenstadt entfernt.')

TEXT = Mapping({
    # ---- Hero
    '<span style="font-weight: 700;">Mechanische &amp; elektronische Schließanlagen</span><br>sowie Videoüberwachung in Lüneburg': H1,
    'Ein verlorener Schlüssel, ein unbeobachteter Hof, eine Tür, die nachts offen steht: Jede dieser Lücken kostet Lüneburger Betriebe schnell einen fünfstelligen Betrag. <br><br>ProVision Infra plant, installiert und betreut Schließanlagen und Videoüberwachung in Lüneburg – mechanisch, elektronisch oder kombiniert, für Betriebe, Praxen und Gewerbe. Von unserem Sitz in Bad Bevensen sind wir in rund einer halben Stunde bei dir vor Ort.': HERO_SUB,

    # ---- Region + Film
    'Region Lüneburg + Film': 'Region Uelzen + Film',
    'Sicherheitstechnik für Lüneburg – geplant und montiert aus der Region.':
        'Sicherheitstechnik für Uelzen – geplant und montiert aus dem eigenen Landkreis.',
    '<p>Unser Sitz liegt in Bad Bevensen im Landkreis Uelzen, rund 30 Kilometer südlich von Lüneburg. Beratung, Aufmaß, Montage und Service übernehmen wir selbst – ohne Subunternehmer, ohne lange Anfahrt und mit einem festen Ansprechpartner.</p>':
        '<p>Uelzen ist für uns kein Punkt auf der Karte, sondern Heimat: ProVision Infra sitzt in Bad Bevensen im Landkreis Uelzen, rund 15 Kilometer nördlich der Kreisstadt. Beratung, Aufmaß, Montage und Service machen wir selbst – kurze Wege, ein fester Ansprechpartner, keine Subunternehmer.</p>',
    '<p>Ob Handwerksbetrieb in der Lüneburger Altstadt, Lager im Gewerbegebiet am Stadtrand oder Praxis in Adendorf: Wir sehen uns dein Objekt vor Ort an und planen Schließanlage und Kameras so, dass beides zusammenpasst – ein Konzept, ein Angebot, ein Ansprechpartner.</p>':
        '<p>Ob Werkstatt in Veerßen, Lagerhalle im Gewerbegebiet an der B4, Praxis in der Innenstadt oder Hausverwaltung mit Objekten in Oldenstadt und Holdenstedt: Wir sehen uns dein Gebäude an und planen Schließanlage und Kameras als ein System – ein Konzept, ein Angebot, ein Ansprechpartner.</p>',

    # ---- Schließanlagen-Karten
    'Schließanlagen Lüneburg': 'Schließanlagen Uelzen',
    'Schließanlagen &amp; Zutrittskontrolle für Lüneburg: <span style="font-weight: 700; ">mechanisch, elektronisch oder kombiniert</span>':
        'Schließanlagen &amp; Zutrittskontrolle in Uelzen: <span style="font-weight: 700; ">vom Schließzylinder bis zur App</span>',
    '<p>Vom klassischen Schließzylinder bis zur App-gesteuerten Zutrittskontrolle: fünf Lösungen, die wir in Lüneburg und Umgebung planen, einbauen und betreuen.</p>':
        '<p>Mechanisch mit Sicherungskarte, elektronisch mit Transponder oder smart per App: fünf Wege, wie wir Türen, Tore und Räume in Uelzen und im Landkreis absichern – geplant nach einer Begehung bei dir vor Ort.</p>',
    # Karte 1
    '<p>Gleichschließende und zentral geschlossene Anlagen mit Sicherungskarte, zum Beispiel von EVVA. Ein Schlüssel pro Person, ein Schließplan für das ganze Gebäude – vom Haupteingang bis zum Serverraum.</p>':
        '<p>Eine Anlage, ein Schließplan, ein Schlüssel pro Person: Mechanische Schließanlagen mit Sicherungskarte, zum Beispiel von EVVA, regeln verlässlich, wer Haupteingang, Büro, Lager oder Serverraum öffnet. Nachschlüssel gibt es nur gegen Karte – nicht an jeder Ecke.</p>',
    '<p>Kopierschutz und Schließplan sorgen dafür, dass du jederzeit weißt, welcher Schlüssel welche Tür in deinem Betrieb öffnet.</p>':
        '<p>Der Schließplan ist bei dir und bei uns dokumentiert. Du weißt jederzeit, welcher Schlüssel welche Tür in deinem Betrieb in Uelzen öffnet.</p>',
    # Karte 2
    '<p>Digitale Zylinder und Beschläge, zum Beispiel von SimonsVoss: Zutritt per Transponder, KeyCard oder App. Berechtigungen vergibst und entziehst du in Sekunden – für Mitarbeitende, Reinigung, Handwerker oder Lieferanten. Mehr dazu auf unserer Seite zum <a href="/zutrittssystem/">digitalen Zutrittssystem</a>.</p>':
        '<p>Digitale Zylinder, Beschläge und Wandleser, etwa von SimonsVoss: Zutritt per Transponder, KeyCard oder Smartphone. Berechtigungen änderst du in Sekunden – für neue Mitarbeitende, die Reinigungsfirma, Lieferanten oder Handwerker. Wie das im Detail funktioniert, zeigt unsere Seite zum <a href="/zutrittssystem/">digitalen Zutrittssystem</a>.</p>',
    '<p>Geht ein Transponder verloren, sperrst du ihn mit einem Klick – statt Zylinder zu tauschen und neue Schlüssel zu verteilen.</p>':
        '<p>Verlorener Transponder? Ein Klick, und er öffnet nichts mehr. Kein Zylindertausch, keine neuen Schlüssel für alle.</p>',
    # Karte 3
    '<p>Nachrüstbare Lösungen wie NUKI für einzelne Türen: ohne Verkabelung, in wenigen Stunden montiert, bedienbar per App, Code oder Transponder.</p>':
        '<p>Für einzelne Türen reicht oft ein nachrüstbares Schloss wie NUKI: ohne Kabel, in wenigen Stunden montiert, geöffnet per App, Zahlencode oder Transponder – passend für Praxis, Kanzlei, Ferienwohnung oder Vereinsheim.</p>',
    '<p>Zeitfenster für Reinigungskräfte, Handwerker oder Gäste richtest du selbst am Handy ein – ohne Schlüsselübergabe.</p>':
        '<p>Reinigung, Handwerker oder Gäste bekommen ein Zeitfenster statt eines Schlüssels – eingerichtet in zwei Minuten am Handy.</p>',
    # Karte 4
    '<p>Du hast bereits eine mechanische Anlage? Wir ersetzen einzelne Zylinder durch digitale Komponenten und bauen schrittweise um, während der Betrieb weiterläuft. Herstellerneutral mit EVVA, SimonsVoss, Keyota, Keyrent und NUKI.</p>':
        '<p>Deine mechanische Anlage ist in die Jahre gekommen, oder es sind zu viele Schlüssel im Umlauf? Wir tauschen Zylinder gegen digitale Komponenten – Tür für Tür, bei laufendem Betrieb. Herstellerneutral mit EVVA, SimonsVoss, Keyota, Keyrent und NUKI.</p>',
    '<p>Kein Stillstand und keine neue Anlage auf einen Schlag – am Ende stimmt der Schließplan wieder und jede Tür ist dokumentiert.</p>':
        '<p>Kein Betriebsstillstand, keine Komplettinvestition auf einen Schlag – und am Ende ein Schließplan, der wieder stimmt.</p>',
    # Karte 5
    '<p>Schließanlage und Kamerasystem planen wir gemeinsam: Wer wann welche Tür geöffnet hat, siehst du im Protokoll – und auf der Aufnahme, was dabei passiert ist. Alle Details zur <a href="/kamerasysteme/">Kamera- und Videoüberwachung für Unternehmen</a>.</p>':
        '<p>Wer wann welche Tür geöffnet hat, steht im Protokoll der Schließanlage. Was dabei passiert ist, zeigt die Kamera. Wir planen beides gemeinsam, damit Kamerastandorte, Zugänge und Hinweisschilder zusammenpassen. Alle Details zur <a href="/kamerasysteme/">Kamera- und Videoüberwachung für Unternehmen</a>.</p>',
    '<p>Kameras von TP-Link VIGI, Zutritt von EVVA, SimonsVoss, Keyota, Keyrent oder NUKI – wir wählen die Technik nach deinem Objekt aus, nicht nach Katalog.</p>':
        '<p>TP-Link VIGI für die Kameras, EVVA, SimonsVoss, Keyota, Keyrent oder NUKI für den Zutritt – ausgewählt nach deinem Objekt in Uelzen, nicht nach Prospekt.</p>',
    '<p>Eine Begehung in Lüneburg, ein Konzept, ein Ansprechpartner – für Türen, Tore und Gelände.</p>':
        '<p>Ein Termin in Uelzen, ein Konzept, ein Ansprechpartner – für Türen, Tore, Hof und Lager.</p>',

    # ---- Videoüberwachung (Glass-Cards)
    'Videoüberwachung Lüneburg': 'Videoüberwachung Uelzen',
    'Videoüberwachung in Lüneburg: Kamerasysteme für Betrieb, Lager und Praxis':
        'Videoüberwachung in Uelzen: Kamerasysteme für Gewerbe, Lager und Praxis',
    'Jede Kamera planen wir nach einer Begehung vor Ort in Lüneburg. Im Ernstfall zeigt sie den Täter, nicht den Parkplatz.':
        'Jede Kamera planen wir nach einer Begehung bei dir in Uelzen – so, dass sie im Ernstfall ein Gesicht zeigt und nicht nur den Parkplatz.',
    'Live-Bild und Aufzeichnung siehst du per App. Dein Handy meldet sich, sobald sich nachts jemand am Tor, am Lager oder auf dem Hof bewegt.':
        'Live-Bild und Aufzeichnung hast du in der App. Bewegt sich nachts jemand am Tor, an der Laderampe oder auf dem Hof, meldet sich dein Handy.',
    '<p>Die Aufnahmen bleiben auf deinem Rekorder im Gebäude, datenschutzkonform mit Hinweisschildern. Polizei und Versicherung bekommen Bilder, die etwas beweisen.</p>':
        '<p>Aufgezeichnet wird lokal auf deinem Rekorder, mit Hinweisschildern und klar begrenzten Kamerawinkeln – DSGVO-konform geplant. Polizei und Versicherung bekommen Aufnahmen, mit denen sie arbeiten können.</p>',

    # ---- Leistungen (Desktop + Handy, identische Strings)
    'Leistungen Lüneburg': 'Leistungen Uelzen',
    '<b>Unsere Leistungen</b> in Lüneburg im Überblick': '<b>Unsere Leistungen</b> in Uelzen im Überblick',
    'Planung und Montage mechanischer Schließanlagen mit Schließplan und Sicherungskarte.':
        'Mechanische Schließanlagen für Betriebe in Uelzen: Schließplan, Sicherungskarte, Montage.',
    'Elektronische Zutrittskontrolle mit Transponder, KeyCard oder App – auch als Nachrüstung.':
        'Elektronische Zutrittskontrolle per Transponder, KeyCard oder Smartphone – neu oder nachgerüstet.',
    'Umrüstung bestehender Anlagen: Zylindertausch, neuer Schließplan, Nachschlüssel-Management.':
        'Umrüstung von mechanisch auf digital: Zylindertausch bei laufendem Betrieb, Schließplan neu aufgesetzt.',
    'Smarte Türschlösser für Büro, Praxis und Ferienwohnung, zum Beispiel NUKI.':
        'Smarte Türschlösser (NUKI) für Praxis, Büro, Ferienwohnung und Vereinsheim.',
    'Videoüberwachung für Hof, Tor, Lager und Eingang mit Live-Bild per App.':
        'Videoüberwachung für Hof, Tor, Laderampe und Eingang – Live-Bild und Alarm per App.',
    'Kamera-Installation inklusive Rekorder, Verkabelung, Hinweisschildern und Einweisung.':
        'Komplette Kamera-Installation: Rekorder, Verkabelung, Hinweisschilder, Einweisung.',
    'Zutritt und Kamera als ein System: Türprotokoll und Aufnahme auf einen Blick.':
        'Zutritt und Kamera verbunden: Türprotokoll und Videoaufnahme auf einen Blick.',
    'Wartung, Service und Erweiterung – ein fester Ansprechpartner für Lüneburg.':
        'Wartung, Service und Erweiterung – ein fester Ansprechpartner im Landkreis Uelzen.',

    # ---- Zielgruppen
    'Zielgruppen Lüneburg': 'Zielgruppen Uelzen',
    'Für wen wir in Lüneburg arbeiten': 'Für wen wir in Uelzen arbeiten',
    'Handwerk, Gewerbe und Produktion: Werkstatt, Lager und Büro mit einer Schließanlage – Hof und Tor per Kamera im Blick.':
        'Handwerk, Produktion, Logistik und Landwirtschaft: Werkstatt, Halle, Maschinenhalle und Büro mit einer Schließanlage – Hof, Tor und Laderampe per Kamera im Blick.',
    'Praxen, Kanzleien und Büros: sensible Räume nur für Berechtigte, Reinigung mit Zeitfenster, jeder Zutritt dokumentiert.':
        'Praxen, Kanzleien und Verwaltung: Medikamenten- und Aktenräume nur für Berechtigte, Reinigung mit Zeitfenster, jeder Zutritt protokolliert.',
    '<p>Hausverwaltungen und Einzelhandel in Lüneburg: Schließplan für viele Nutzer, Nachschlüssel ohne Zylindertausch, Kassen- und Lagerbereiche überwacht.</p>':
        '<p>Hausverwaltungen, Einzelhandel und Gastronomie in Uelzen: Schließplan für viele Nutzer, Mieterwechsel ohne Zylindertausch, Kasse, Lager und Eingang im Blick.</p>',

    # ---- Ablauf (Lottie-Timeline Desktop + EA-Timeline Handy, identische Strings)
    '<p>Ein kurzes Telefonat: Geht es um Schlüssel, um Kameras oder um beides? Du bekommst eine erste ehrliche Einschätzung.</p>':
        '<p>Ein kurzes Telefonat: Was soll bei dir in Uelzen abgesichert werden – Türen, Gelände oder beides? Du bekommst sofort eine ehrliche erste Einschätzung.</p>',
    '<p>Wir kommen zu dir nach Lüneburg, gehen durch das Gebäude und über das Gelände und zeigen dir, wo Schlüssel, Türen und Kameras heute Lücken lassen. Den Kostenrahmen nennen wir dir noch vor Ort.</p>':
        '<p>Wir kommen von Bad Bevensen zu dir nach Uelzen, gehen mit dir durch Gebäude und Gelände und zeigen dir, wo Schlüssel, Türen und Kameras heute Lücken lassen. Den Kostenrahmen nennen wir dir noch vor Ort.</p>',
    '<p>Du bekommst ein Konzept mit Schließplan und Kamerastandorten sowie ein Angebot, das zu deinem Budget passt. Dann entscheidest du.</p>':
        '<p>Du erhältst ein Konzept mit Schließplan und Kamerastandorten und ein Angebot, das zu deinem Budget passt. Entscheiden kannst du in Ruhe.</p>',
    '<p>Zylinder, Beschläge und Kameras montieren wir, Schließplan, Software und App richten wir komplett ein. Du musst nichts selbst konfigurieren.</p>':
        '<p>Zylinder, Beschläge und Kameras montieren wir, Schließplan, Software und App richten wir vollständig ein. Konfigurieren musst du nichts.</p>',
    '<p>Gemeinsam prüfen wir, ob die Anlage leistet, was vereinbart war, und halten das schriftlich fest. Danach bleiben wir erreichbar.</p>':
        '<p>Gemeinsam prüfen wir, ob alles so läuft wie vereinbart, und halten das schriftlich fest. Danach bleiben wir erreichbar – von Bad Bevensen aus in 20 Minuten bei dir.</p>',

    # ---- Standort / Karte (NAP-Block)
    'ProVision Infra <br><span style="font-weight: 700; ">in Lüneburg und Umgebung</span>':
        'ProVision Infra <br><span style="font-weight: 700; ">in Uelzen und im Landkreis</span>',
    '<p>Unser Sitz ist Bad Bevensen, rund 30 Kilometer von Lüneburg entfernt. Regelmäßig sind wir in Lüneburg, Adendorf, Bardowick, Reppenstedt, Scharnebeck, Bleckede, Winsen (Luhe), Uelzen und im gesamten Landkreis Lüneburg unterwegs.</p><p>Für Beratung, Aufmaß und Montage kommen wir direkt zu dir, sehen uns Türen, Zugänge und Gelände an und setzen Schließanlage und Kameras dort um, wo sie gebraucht werden.</p>':
        '<p>Unser Firmensitz liegt in Bad Bevensen, rund 15 Kilometer nördlich von Uelzen – wir arbeiten also in unserem eigenen Landkreis. Regelmäßig sind wir in der Hansestadt Uelzen, in Bad Bevensen, Ebstorf, Bienenbüttel, Suderburg, Wrestedt, Rosche, Bad Bodenteich, Altenmedingen und Himbergen unterwegs, ebenso im angrenzenden Landkreis Lüchow-Dannenberg und Richtung Lüneburg.</p><p>Für Beratung, Aufmaß und Montage kommen wir zu dir, schauen uns Türen, Zugänge und Gelände an und setzen Schließanlage und Kameras genau dort um, wo sie gebraucht werden.</p>',

    # ---- FAQ-Überschriften
    'Häufige Fragen zu Schließanlagen &amp; Videoüberwachung in <b>Lüneburg</b>':
        'Häufige Fragen zu Schließanlagen &amp; Videoüberwachung in <b>Uelzen</b>',
    'Häufige Fragen zu Schließanlagen &amp; <br>Videoüberwachung in <b>Lüneburg</b>':
        'Häufige Fragen zu Schließanlagen &amp; <br>Videoüberwachung in <b>Uelzen</b>',

    # ---- Menü (Header + Footer)
    'menue-lueneburg': MENU_SLUG,
})

FAQ = [
    ('Was kostet eine Schließanlage in Uelzen?',
     '<p>Entscheidend sind die Zahl der Türen, die Art der Zylinder und die Frage: mechanisch, elektronisch oder kombiniert? Eine mechanische Anlage mit Sicherungskarte für ein kleines Büro ist deutlich günstiger als eine digitale Lösung mit Transponder und App – dafür sparst du dort jeden späteren Zylindertausch. Einen ersten Rahmen nennen wir dir im Erstgespräch, den verbindlichen Preis nach dem Termin bei dir in Uelzen.</p>'),
    ('Mechanische oder elektronische Schließanlage – was passt zu meinem Betrieb?',
     '<p>Wenige Türen, feste Belegschaft, kaum Wechsel: Dann ist eine mechanische Anlage mit Sicherungskarte oft die wirtschaftlichste Lösung. Viele Mitarbeitende, Dienstleister, Schichtbetrieb oder mehrere Standorte im Landkreis Uelzen: Dann rechnet sich eine elektronische Anlage, weil du Berechtigungen in Sekunden änderst, statt Schlüssel einzusammeln. Häufig ist die Mischung sinnvoll – Haupteingang und Lager digital, Nebenräume mechanisch.</p>'),
    ('Schlüssel der Schließanlage verloren – was jetzt?',
     '<p>Bei einer mechanischen Anlage kommt es auf den Schlüssel an: Ein Einzelschlüssel lässt sich oft mit dem Tausch eines Zylinders auffangen, ein verlorener Generalschlüssel kann den Austausch der ganzen Anlage bedeuten. Bei einer elektronischen Anlage sperrst du den verlorenen Transponder einfach – ohne Zylindertausch. Genau deshalb raten wir Betrieben mit vielen Schlüsseln zur Umrüstung. Ruf uns an, wir bewerten die Lage ehrlich.</p>'),
    ('Kann ich meine bestehende Schließanlage auf elektronisch umrüsten?',
     '<p>Ja. Digitale Zylinder von SimonsVoss oder smarte Schlösser wie NUKI passen in vorhandene Türen, meist ohne Kabel und ohne Bauarbeiten. Wir rüsten Tür für Tür um, dein Betrieb läuft weiter. Türen, die selten genutzt werden, können mechanisch bleiben.</p>'),
    ('Wie schnell seid ihr in Uelzen vor Ort?',
     '<p>Von Bad Bevensen aus sind wir in rund 20 Minuten in Uelzen – und ähnlich schnell in Ebstorf, Bienenbüttel, Suderburg, Wrestedt oder Bad Bodenteich. Begehung und Montage legen wir so, dass dein Betrieb nicht stillsteht; auch Termine am frühen Morgen oder nach Ladenschluss sind möglich.</p>'),
    ('Darf ich mein Firmengelände in Uelzen per Kamera überwachen?',
     '<p>Ja, innerhalb klarer Regeln: Erlaubt sind dein eigenes Gelände, deine Gebäude und Zugänge – nicht der Gehweg, die Straße oder das Nachbargrundstück. Mitarbeitende müssen informiert sein, ein Hinweisschild ist Pflicht, Pausen- und Sozialräume bleiben kamerafrei. Wir planen die Kamerawinkel entsprechend und liefern Schilder und Unterlagen für deine Dokumentation mit.</p>'),
    ('Kann ich Zutritt und Kameras in einem System verbinden?',
     '<p>Ja. Öffnet jemand per Transponder oder App eine Tür, steht im Protokoll, wer es war – und die Aufnahme zeigt, was danach passiert ist. Wir planen beides zusammen, damit Kamerastandorte und Zugänge zueinander passen und du nur einen Ansprechpartner hast.</p>'),
    ('Welche Hersteller verbaut ProVision Infra?',
     '<p>Bei Schließanlagen arbeiten wir unter anderem mit EVVA, SimonsVoss, Keyota, Keyrent und NUKI, bei Kamerasystemen mit TP-Link VIGI. Welche Komponenten zu deinem Objekt passen, entscheiden wir nach der Begehung. Hintergründe findest du auf unseren Seiten zum <a href="/zutrittssystem/">Zutrittssystem</a> und zu <a href="/kamerasysteme/">Kamerasystemen</a>.</p>'),
    ('Wie lange dauert der Einbau einer Schließanlage in Uelzen?',
     '<p>Eine mechanische Anlage für ein kleines Objekt ist meist an einem Tag montiert, digitale Zylinder sitzen in wenigen Minuten pro Tür. Größere Objekte – etwa ein Betrieb mit Halle, Büro und Außentoren – planen wir in Abschnitten. Den Zeitplan bekommst du zusammen mit dem Angebot.</p>'),
    ('Arbeitet ihr auch für Hausverwaltungen und Mehrfamilienhäuser in Uelzen?',
     '<p>Ja. Für Wohnanlagen planen wir Schließanlagen mit Schließplan für viele Nutzer; Haustür und Nebeneingänge gern digital, damit ein Mieterwechsel keinen Zylindertausch mehr bedeutet. Kameras an Eingang, Fahrradkeller oder Tiefgarage planen wir mit dem nötigen Datenschutz für die Bewohner.</p>'),
    ('Übernehmt ihr Wartung und Service für Schließanlagen und Kameras im Landkreis Uelzen?',
     '<p>Ja. Nach der Übergabe bleiben wir dein Ansprechpartner: Erweiterungen, Nachschlüssel und neue Transponder, Updates für Zutrittssoftware und Rekorder sowie die Wartung der Kameras. Weil wir selbst im Landkreis Uelzen sitzen, sind Servicetermine kurzfristig möglich.</p>'),
]

SEO_TITLE = 'Schließanlagen & Videoüberwachung Uelzen | ProVision Infra'
SEO_DESC = ('Schließanlagen, Zutrittskontrolle & Videoüberwachung in Uelzen: ProVision Infra aus Bad Bevensen plant, '
            'montiert und betreut dein System. Jetzt anfragen!')
FOCUS_KW = 'Schließanlagen Uelzen'
assert len(SEO_TITLE) <= 60, len(SEO_TITLE)
assert len(SEO_DESC) <= 160, len(SEO_DESC)

# WebPage + BreadcrumbList liefert Yoast, FAQPage das EA-Akkordeon, Product/AggregateRating ProvenExpert.
# Eigene Kopien davon führten auf /lueneburg/ zu @id-Kollisionen (GSC: „Feld item fehlt“) – deshalb hier nur
# Organisation + zwei Service-Knoten, ergänzt um Geokoordinaten des Firmensitzes.
ORG_ID = f'{SITE}/#organisation'
SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": ["LocalBusiness", "Locksmith"], "@id": ORG_ID, "name": "ProVision Infra GmbH",
         "url": f"{SITE}/", "logo": f"{SITE}/wp-content/uploads/2026/10/kamera-logo-provision-infra-1032.png",
         "image": f"{SITE}/wp-content/uploads/2026/05/provision_header_02-1.png",
         "telephone": "+49 5821 4049040", "email": "info@provision-infra.de", "priceRange": "$$",
         "address": {"@type": "PostalAddress", "streetAddress": "Klein Hesebecker Straße 11", "postalCode": "29549",
                     "addressLocality": "Bad Bevensen", "addressRegion": "Niedersachsen", "addressCountry": "DE"},
         "geo": {"@type": "GeoCoordinates", "latitude": GEO['lat'], "longitude": GEO['lon']},
         "openingHoursSpecification": [
             {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "09:00", "closes": "18:00"},
             {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "09:00", "closes": "14:00"}],
         "areaServed": [{"@type": "City", "name": "Uelzen"}, {"@type": "AdministrativeArea", "name": "Landkreis Uelzen"},
                        {"@type": "City", "name": "Bad Bevensen"}, {"@type": "City", "name": "Ebstorf"},
                        {"@type": "City", "name": "Bienenbüttel"}, {"@type": "City", "name": "Suderburg"},
                        {"@type": "City", "name": "Bad Bodenteich"}, {"@type": "City", "name": "Lüneburg"},
                        {"@type": "State", "name": "Niedersachsen"}],
         "sameAs": ["https://www.instagram.com/provision_infra_gmbh/", "https://www.facebook.com/share/1CWs2rohMt/",
                    "https://www.linkedin.com/company/provision-infra-gmbh-i-g/"]},
        {"@type": "Service", "@id": f"{PAGE_URL}#schliessanlagen", "name": "Mechanische und elektronische Schließanlagen in Uelzen",
         "serviceType": "Schließanlagen und Zutrittskontrolle", "url": f"{PAGE_URL}#schliessanlagen",
         "description": "Planung, Montage, Umrüstung und Betreuung mechanischer und elektronischer Schließanlagen (EVVA, SimonsVoss, Keyota, Keyrent, NUKI) für Betriebe, Praxen und Hausverwaltungen in Uelzen und im Landkreis Uelzen.",
         "provider": {"@id": ORG_ID},
         "areaServed": [{"@type": "City", "name": "Uelzen"}, {"@type": "AdministrativeArea", "name": "Landkreis Uelzen"}],
         "audience": {"@type": "BusinessAudience", "name": "Unternehmen, Betriebe, Praxen und Hausverwaltungen"}},
        {"@type": "Service", "@id": f"{PAGE_URL}#kamera", "name": "Video- und Kameraüberwachung in Uelzen",
         "serviceType": "Videoüberwachung", "url": f"{PAGE_URL}#kamera",
         "description": "Planung und Installation DSGVO-konformer Kamerasysteme (TP-Link VIGI) mit App-Zugriff und lokaler Aufzeichnung für Hof, Tor, Lager und Eingang von Betrieben in Uelzen und Umgebung.",
         "provider": {"@id": ORG_ID},
         "areaServed": [{"@type": "City", "name": "Uelzen"}, {"@type": "AdministrativeArea", "name": "Landkreis Uelzen"}],
         "audience": {"@type": "BusinessAudience", "name": "Unternehmen, Betriebe und Gewerbe"}},
    ]
}

# ================================================================== Seite bauen
els = copy.deepcopy(L['elements'])
for root in els:
    for e in walk(root):
        e.pop('htmlCache', None)

replace_text(els, TEXT)
missed = set(TEXT) - TEXT.hits
assert not missed, 'Quelltexte nicht gefunden (Lüneburg-Quelle geändert?):\n' + '\n'.join(sorted(missed))

# FAQ-Einträge neu aufsetzen (Vorlage: erster Eintrag der Lüneburg-Seite)
acc = find(els, 'ed852c3')['settings']
tmpl = acc['eael_adv_accordion_tab'][0]
acc['eael_adv_accordion_tab'] = []
for q, a in FAQ:
    item = copy.deepcopy(tmpl)
    item['eael_adv_accordion_tab_title'] = q
    item['eael_adv_accordion_tab_content'] = a
    item['_id'] = new_id()
    acc['eael_adv_accordion_tab'].append(item)

# Strukturierte Daten
set_setting(els, 'f058554', 'html', '<script type="application/ld+json">' + json.dumps(SCHEMA, ensure_ascii=False) + '</script>')

# Hero-Überschriften: Elementor-Editor-Label für die Übersicht im Navigator
set_setting(els, '9dcea29', '_title', 'H1 Schließanlagen & Videoüberwachung Uelzen')
set_setting(els, 'e429076', '_title', 'Hero-Text Uelzen')

# ---- Prüfungen
ids = [e['id'] for root in els for e in walk(root)]
dups = {i for i in ids if ids.count(i) > 1}
assert not dups, dups
ids.extend(t['_id'] for t in acc['eael_adv_accordion_tab'])
used.update(ids)

rest = []
pat = re.compile(r'l[üu]e?neburg', re.I)
def scan(v, path):
    if isinstance(v, str):
        if pat.search(v): rest.append((path, v[:120]))
    elif isinstance(v, dict):
        for k, x in v.items(): scan(x, f'{path}.{k}')
    elif isinstance(v, list):
        for i, x in enumerate(v): scan(x, f'{path}[{i}]')
for root in els:
    for e in walk(root):
        if e['id'] == 'f058554':
            continue  # Schema nennt Lüneburg bewusst als Nachbarstadt in areaServed
        scan(e['settings'], e['id'])
# Einzige erlaubte Nennungen: Nachbarregion im Standort-Text und Kameraseite als Nachbarschaft
allowed = {'5c65e03.editor'}
bad = [r for r in rest if r[0] not in allowed]
assert not bad, 'Lüneburg-Reste:\n' + '\n'.join(f'{p}: {v}' for p, v in bad)
for root in els:
    for e in walk(root):
        l = e['settings'].get('link')
        if isinstance(l, dict) and l.get('url') in ('/kontakt', '/kontakt-kamerasysteme/'):
            raise SystemExit(f'Alter CTA-Link in {e["id"]}')
assert all(e['settings'].get('menu') == MENU_SLUG for root in els for e in walk(root) if e.get('widgetType') == 'nav-menu')

page_settings = copy.deepcopy(L['settings'])
page_settings.update({'post_title': 'Schließanlagen & Videoüberwachung Uelzen', 'post_status': POST_STATUS})

os.makedirs(OUT, exist_ok=True)
json.dump({'elements': els, 'settings': page_settings,
           'seo': {'title': SEO_TITLE, 'description': SEO_DESC, 'focuskw': FOCUS_KW,
                   'slug': SLUG, 'robots_noindex': '2', 'bctitle': 'Uelzen',
                   'og_image': f'{SITE}/wp-content/uploads/2026/05/provision_header_02-1.png'}},
          open(f'{OUT}/uelzen.elementor.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# Alt-Texte der Mediathek (gelten site-weit, deshalb ortsneutral formuliert; ID = Medien-ID in WordPress)
MEDIA_ALT = {
    407: 'ProVision Infra GmbH Logo',
    397: 'Google-Bewertung: 5 von 5 Sternen',
    3058: 'Film: ProVision Infra plant und installiert Schließanlagen und Zutrittssysteme',
    276: 'Karte Norddeutschland: Einsatzgebiet von ProVision Infra rund um Uelzen, Lüneburg, Hamburg und Hannover',
    176: 'Fünf Sterne Google-Bewertung',
    273: 'Partner-Logos: Keyota, EVVA Certified Partner, Keyrent, SimonsVoss, EVVA',
    1337: 'Partner-Logos: Keyota und EVVA Certified Partner',
    1338: 'Partner-Logos: Keyrent und SimonsVoss',
    1339: 'Partner-Logo: EVVA',
}
json.dump(MEDIA_ALT, open(f'{OUT}/media-alt-texte.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ================================================================== Textfassung zum Gegenlesen (seo/uelzen-texte.md)
def strip_tags(s):
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'</p>\s*<p>', '\n\n', s)
    return re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', s)).replace('&amp;', '&').replace('&nbsp;', ' ').strip()

lines = ['# Texte der Seite /uelzen/ in Lesereihenfolge', '',
         f'Erzeugt von `tools/build_uelzen.py` aus `elementor/uelzen.elementor.json`. Fett = Überschrift (H-Ebene aus Elementor).', '',
         f'- **SEO-Titel:** {SEO_TITLE} ({len(SEO_TITLE)} Zeichen)',
         f'- **Meta-Description:** {SEO_DESC} ({len(SEO_DESC)} Zeichen)',
         f'- **Fokus-Keyphrase:** {FOCUS_KW} · **URL:** {PAGE_URL} · **Menü:** {MENU_SLUG}', '']
seen_mobile = {'d135e80', '67b8213', '7dfd9f6', 'bec6cfd'}
for root in els:
    title = root['settings'].get('_title') or root['settings'].get('_element_id') or root['id']
    lines.append(f'## Abschnitt {title}  `#{root["settings"].get("_element_id", "")}`'.replace('  `#`', ''))
    lines.append('')
    for e in walk(root):
        s = e['settings']; wt = e.get('widgetType')
        if wt == 'heading' and s.get('title'):
            lvl = (s.get('header_size') or 'h2').upper()
            lines.append(f'**{lvl}:** {strip_tags(s["title"])}'); lines.append('')
        elif wt == 'text-editor' and s.get('editor'):
            lines.append(strip_tags(s['editor'])); lines.append('')
        elif wt == 'button' and s.get('text'):
            lines.append(f'[Button] {s["text"]} → {s.get("link", {}).get("url", "")}'); lines.append('')
        elif wt == 'nav-menu':
            lines.append(f'[Menü] {s.get("menu")}'); lines.append('')
        elif wt == 'eael-adv-accordion':
            for t in s['eael_adv_accordion_tab']:
                lines.append(f'**FAQ:** {t["eael_adv_accordion_tab_title"]}'); lines.append('')
                lines.append(strip_tags(t['eael_adv_accordion_tab_content'])); lines.append('')
        elif wt == 'icon-box' and s.get('description_text'):
            lines.append(f'[Kundenstimme] {s["description_text"]}'); lines.append('')
        elif wt == 'image-box' and s.get('title_text'):
            lines.append(f'[Kunde] {s["title_text"].strip()} – {s.get("description_text", "").strip()}'); lines.append('')
        elif wt == 'eael-content-timeline':
            for p in s.get('eael_coustom_content_posts', []):
                lines.append(f'[Ablauf Handy] **{strip_tags(p.get("eael_custom_title", ""))}** – {strip_tags(p.get("eael_custom_excerpt", ""))}'); lines.append('')
        elif wt == 'html' and 'ld+json' in (s.get('html') or ''):
            lines.append('```json'); lines.append(json.dumps(SCHEMA, ensure_ascii=False, indent=1)); lines.append('```'); lines.append('')
os.makedirs(os.path.join(os.path.dirname(OUT.rstrip('/')) or '.', 'seo'), exist_ok=True)
open(os.path.join(os.path.dirname(OUT.rstrip('/')) or '.', 'seo', 'uelzen-texte.md'), 'w', encoding='utf-8').write('\n'.join(lines).rstrip() + '\n')

words = len(re.findall(r"[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\-]+", ' '.join(l for l in lines if not l.startswith(('```', '{', '"', ' ')))))
print(f'OK {len(els)} Abschnitte; {len(ids)} Elemente; FAQ {len(FAQ)}; Status {POST_STATUS}; ca. {words} Wörter sichtbarer Text')
