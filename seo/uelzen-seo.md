# SEO-Konzept: /uelzen/ – Schließanlagen & Videoüberwachung Uelzen

Stand: 27.10.2026 · Seite: https://provision-infra.de/uelzen/ (WordPress-Seite #4605, Elementor, **veröffentlicht am 27.10.2026**) ·
Vorlage: /lueneburg/ (Seite #4496, Repo `provisioninfra/schliessanlagen-lueneburg`)

Ziel: bestmögliche Google-Platzierung für lokale, kommerzielle Suchanfragen rund um Schließanlagen, Zutrittskontrolle,
Sicherheitstechnik und Videoüberwachung in Uelzen und im Landkreis Uelzen. Besonderheit gegenüber Lüneburg: Uelzen ist
der **Heimat-Landkreis** von ProVision Infra (Sitz Bad Bevensen, rund 15 km nördlich der Kreisstadt). Dieser Vorteil
(„aus dem eigenen Landkreis“, „in 20 Minuten vor Ort“) ist das Leitmotiv aller Texte.

Angelegte Objekte in WordPress (27.10.2026):

| Objekt | ID | Hinweis |
| --- | --- | --- |
| Seite „Schließanlagen & Videoüberwachung Uelzen“ | 4605 | `/uelzen/`, index, in `page-sitemap.xml` |
| Menü „Menü Uelzen“ (Slug `menue-uelzen`) | 19 | fünf Anker-Links (Schließanlagen, Videoüberwachung, So arbeiten wir, Über uns, FAQ), in Header und Footer der Seite |

Formulare und Funnel-Seiten wurden nicht angelegt; die Seite nutzt den gemeinsamen Funnel `/anfrage-auswahl/` (Formular 5).

## 1. Keyword-Set

Grundlage: Google-Suggest-Vervollständigungen (Deutschland, Deutsch, abgefragt 26.10.2026) plus das Keyword-Set der
Lüneburg- und der Kamera-Seite. Für „schließanlage uelzen“, „videoüberwachung uelzen“, „zutrittskontrolle uelzen“ gibt es
keine Vervollständigungen (geringes Volumen, dafür kaum Wettbewerb). Belegt sind **„sicherheitstechnik uelzen“** und
**„schlüsseldienst uelzen“** (mit „kosten“); die Seite nutzt deshalb „Sicherheitstechnik“ als Oberbegriff in der
Region-Überschrift. Produkt-Longtails ohne Ortsbezug mit Vervollständigungen: „elektronische schließanlage mit
chip/transponder/kosten“, „schließanlage firma kosten“, „schlüssel verloren schließanlage firma“, „schließanlage
mehrfamilienhaus“ – daraus sind FAQ 1, 2, 3 und 10 entstanden.

| Priorität | Keyword (Suchintention) | Einsatz auf der Seite |
| --- | --- | --- |
| 1 | **Schließanlagen Uelzen** (Fokus-Keyphrase, kommerziell, lokal) | Title, H1, Hero-Text, URL `/uelzen/`, H2 Karten, FAQ 1/9, Schema `Service` |
| 1 | **Videoüberwachung Uelzen** | Title, H1, H2 „Videoüberwachung in Uelzen“, Hero-Text, FAQ 6, Schema `Service` |
| 2 | Zutrittskontrolle Uelzen | Description, H2 „Schließanlagen & Zutrittskontrolle in Uelzen“, Leistungen |
| 2 | Sicherheitstechnik Uelzen (Suggest belegt) | H2/Region „Sicherheitstechnik für Uelzen“ |
| 2 | elektronische / mechanische Schließanlage, Transponder, Chip | H3-Karten 1–2, Leistungen, FAQ 2 |
| 2 | Kamerasysteme Uelzen, Kameraüberwachung, Kamera Firmengelände | H2 Kamera, Glass-Cards, Technik-Karussell, FAQ 6 |
| 3 | Schließanlage umrüsten, Schlüssel verloren, Schließplan, Sicherungskarte | Karte 4, FAQ 3/4, Leistungen |
| 3 | Schließanlage Mehrfamilienhaus / Hausverwaltung | Zielgruppen, FAQ 10 |
| 3 | Hersteller (EVVA, SimonsVoss, NUKI, Keyota, Keyrent, TP-Link VIGI) | Karten, FAQ 8, Partner-Logos |
| Lokal | Uelzen, Hansestadt Uelzen, Kreisstadt, Landkreis Uelzen, Veerßen, Oldenstadt, Holdenstedt, Bad Bevensen, Ebstorf, Bienenbüttel, Suderburg, Wrestedt, Rosche, Bad Bodenteich, Altenmedingen, Himbergen, Landkreis Lüchow-Dannenberg, B4 | Hero, Region, Standort/NAP, FAQ 5, Schema `areaServed` |

Zielgruppen und Ansprache: gewerbliche Entscheider (Handwerk, Produktion, Logistik, Landwirtschaft, Praxen, Kanzleien,
Hausverwaltungen, Einzelhandel, Gastronomie) in Uelzen und im Landkreis, Du-Form wie auf der gesamten Website.

### Abgrenzung (keine Kannibalisierung)

- `/lueneburg/` zielt auf Stadt und Landkreis Lüneburg, `/uelzen/` ausschließlich auf Uelzen und den Landkreis Uelzen.
  Alle Fließtexte, Karten, Leistungen, Ablauf-Texte und FAQ sind neu formuliert; nur H1-Muster, Abschnittsfolge,
  Gründer-Abschnitt und Kundenstimmen sind identisch (site-weite Bausteine).
- `/zutrittssystem/` und `/kamerasysteme/` bleiben die überregionalen Produktseiten (Hamburg, Hannover, Niedersachsen);
  die Uelzen-Seite verlinkt beide aus Karte 2, Karte 5 und FAQ 8.
- Lüneburg wird auf der Uelzen-Seite nur als Nachbarregion genannt (Standort-Text, `areaServed`), umgekehrt nennt die
  Lüneburg-Seite bereits Uelzen – beide Seiten sollten sich gegenseitig verlinken (siehe Abschnitt 8).

## 2. Meta-Daten (Yoast SEO)

| Feld | Wert |
| --- | --- |
| SEO-Titel (58 Zeichen) | `Schließanlagen & Videoüberwachung Uelzen \| ProVision Infra` |
| Meta-Description (153 Zeichen, mit CTA) | `Schließanlagen, Zutrittskontrolle & Videoüberwachung in Uelzen: ProVision Infra aus Bad Bevensen plant, montiert und betreut dein System. Jetzt anfragen!` |
| Fokus-Keyphrase | `Schließanlagen Uelzen` |
| Slug / Canonical | `/uelzen/` → `https://provision-infra.de/uelzen/` |
| Breadcrumb-Titel | `Uelzen` |
| Robots | index, follow (`robots_noindex` = 2) |
| OG/Twitter | Titel + Description wie oben, Bild `provision_header_02-1.png` (1305×980, wie Lüneburg) |

Die Werte stehen im `seo`-Block von `elementor/uelzen.elementor.json`.

## 3. Seitenstruktur (22 Elementor-Abschnitte, identisch zur Lüneburg-Seite)

| # | Abschnitt (Anker) | Design-Herkunft | Inhalt Uelzen |
| --- | --- | --- | --- |
| 1 | Header (sticky Glass-Navigation) | Kamera-Seite | Logo, Menü `menue-uelzen` |
| 2–4 | Hero mit Tür-Video, Mobil-Video, Kennzahlen | Startseite / Kamera-Seite | H1 + Hero-Text (beide Keyphrasen in den ersten 60 Wörtern) + CTA |
| 5 | Region + Film (`#region`) | Startseite | „Sicherheitstechnik für Uelzen – aus dem eigenen Landkreis“, Sitz 15 km nördlich, Veerßen/Oldenstadt/Holdenstedt |
| 6 | Schließanlagen (`#schliessanlagen`) | Kamera-Seite „5 Karten“ | H2 + 5 H3-Karten: mechanisch, elektronisch, smart, Umrüstung, kombiniert; CTA |
| 7 | Videoüberwachung (`#kamera`) | Glass-Cards | H2 + 3 Nutzen-Karten (Begehung, App-Alarm, DSGVO/Rekorder) |
| 8–10 | Leistungen (`#leistungen`, Desktop + Handy) | Kamera-Seite „Stell dir mal vor“ | H2 + 8 Leistungen mit Neben-Keywords, Lottie-Kamera |
| 11 | Zielgruppen (`#zielgruppen`) | Glass-Cards | Handwerk/Produktion/Logistik/Landwirtschaft, Praxen/Kanzleien/Verwaltung, Hausverwaltungen/Einzelhandel/Gastronomie |
| 12 | Technik (`#technik`) | Produkt-Karussell | TP-Link VIGI Kameras (unverändert) |
| 13 | Kundenstimmen | Testimonial-Karussell | unverändert (eine Stimme nennt Bad Bevensen) |
| 14 | Ablauf (`#arbeiten`) | Lottie-Timeline / EA-Timeline | 5 Schritte mit Uelzen- und Anfahrtsbezug |
| 15–16 | Gründer (`#ueber`) | Glass-Container | unverändert |
| 17 | Standort (`#standort`) | Deutschlandkarte + Glass-Card | H2 „in Uelzen und im Landkreis“, Ortsliste, NAP-Block, CTA |
| 18 | FAQ (`#FAQ`) | EA Advanced Accordion | 11 Fragen (Abschnitt 5) |
| 19–21 | Partner, Footer (Menü `menue-uelzen`), ProvenExpert-Badge | unverändert | – |
| 22 | Strukturierte Daten | HTML-Widget | JSON-LD (Abschnitt 4) |

Überschriften: 1× H1, H2 je Abschnitt, H3 nur in Karten, Ablauf und FAQ. Sichtbarer Text rund 2.100 Wörter.
Interne Links: `/zutrittssystem/` (Karte 2, FAQ 8), `/kamerasysteme/` (Karte 5, FAQ 8), alle CTAs → `/anfrage-auswahl/`,
`tel:`- und `mailto:`-Link im NAP-Block.

## 4. Strukturierte Daten

Eigenes JSON-LD im letzten Abschnitt (`tools/build_uelzen.py`, `SCHEMA`):

- `LocalBusiness` + `Locksmith` (`@id` `/#organisation`): Adresse Bad Bevensen, Telefon, E-Mail, Öffnungszeiten,
  **`geo`** (Koordinaten aus `elementor/geo.json`), `areaServed` Uelzen, Landkreis Uelzen, Bad Bevensen, Ebstorf,
  Bienenbüttel, Suderburg, Bad Bodenteich, Lüneburg, Niedersachsen, `sameAs` Social-Profile.
- 2× `Service` (`/uelzen/#schliessanlagen`, `/uelzen/#kamera`) mit `areaServed` Uelzen / Landkreis Uelzen und
  `BusinessAudience`.

Von Plugins erzeugt und deshalb **nicht** im eigenen JSON-LD (Lerneffekt Lüneburg: doppelte `BreadcrumbList` führte in
der Search Console zu „Feld item fehlt“): Yoast `WebSite`/`WebPage`/`BreadcrumbList`, Essential Addons `FAQPage`
(alle 11 Fragen), ProvenExpert `Product`/`AggregateRating`.

## 5. FAQ (Longtail-Abdeckung)

1. Was kostet eine Schließanlage in Uelzen? („schließanlage firma kosten“)
2. Mechanische oder elektronische Schließanlage – was passt zu meinem Betrieb? („elektronische schließanlage mit transponder“)
3. Schlüssel der Schließanlage verloren – was jetzt? („schlüssel verloren schließanlage firma“)
4. Kann ich meine bestehende Schließanlage auf elektronisch umrüsten?
5. Wie schnell seid ihr in Uelzen vor Ort? (Anfahrt, Ortsnamen im Landkreis)
6. Darf ich mein Firmengelände in Uelzen per Kamera überwachen? (DSGVO, Hinweisschild, Mitarbeitende)
7. Kann ich Zutritt und Kameras in einem System verbinden?
8. Welche Hersteller verbaut ProVision Infra? (interne Links auf beide Produktseiten)
9. Wie lange dauert der Einbau einer Schließanlage in Uelzen?
10. Arbeitet ihr auch für Hausverwaltungen und Mehrfamilienhäuser in Uelzen? („schließanlage mehrfamilienhaus“)
11. Übernehmt ihr Wartung und Service für Schließanlagen und Kameras im Landkreis Uelzen?

## 6. Funnel

Unverändert gegenüber Lüneburg; der Funnel ist für alle Stadtseiten gebaut:

```
/uelzen/  ──CTA──▶  /anfrage-auswahl/  (Formular 5: Schließsystem | Kamerasysteme | Beides)
                         │ Schließsystem  ──▶ /kontakt/                 ──▶ /termin/
                         │ Kamerasysteme  ──▶ /kontakt-kamerasysteme/   ──▶ /termin-kamerasysteme/
                         └ Beides         ──▶ /kontakt-kombiniert/ (Formular 6) ──▶ /termin/ bzw. /termin-gebucht/
```

Option für die Auswertung nach Stadtseite: CTAs mit `?utm_source=website&utm_medium=stadtseite&utm_campaign=uelzen`
versehen – das Funnel-Formular übernimmt UTM-Parameter als versteckte Felder. Im Build bewusst nicht gesetzt, damit die
Links identisch zur Lüneburg-Seite bleiben; bei Bedarf `FUNNEL_URL` in `tools/build_uelzen.py` anpassen.

## 7. Technik (Erwartung nach Veröffentlichung)

| Prüfpunkt | Erwartung |
| --- | --- |
| HTTP 200, HTTPS, Canonical auf sich selbst | Yoast-Standard |
| robots `index, follow`, Aufnahme in `page-sitemap.xml` | automatisch nach Veröffentlichung |
| Mobil: eigener Hero-Block ohne Hintergrundvideo, keine horizontale Scrollbar | wie Lüneburg (identische Abschnitte) |
| Lazy Loading: Vimeo erst nach Consent (Borlabs), Bilder per WordPress-Lazy-Loading | wie Lüneburg |
| Schema-Test (Rich-Results-Test) ohne Fehler | eigene Knoten kollidieren nicht mit Yoast/EA |
| Audit: `python3 -I tools/audit_live.py <html>` | Titel ≤ 60, Description ≤ 160, 1× H1, Keywords vorhanden |

## 8. Veröffentlichung und Indexierung – Checkliste

- [x] Seite in WordPress anlegen (Entwurf), Elementor-Daten speichern, Yoast-Werte setzen (27.10.2026, Seite #4605)
- [x] Menü „Menü Uelzen“ (`menue-uelzen`, ID 19) mit fünf Anker-Links angelegt; Header- und Footer-Widgets zeigen darauf
- [x] Vorschau Desktop (1440 px) und Mobil (iPhone 13) geprüft: keine horizontale Scrollbar, Menü, NAP-Block, 11 FAQ, Leistungs-Animation wie auf /lueneburg/
- [x] Veröffentlicht; geprüft: `https://provision-infra.de/uelzen/` liefert 200, Canonical auf sich selbst, `index, follow`, in `page-sitemap.xml` (27.10.2026)
- [ ] **Interne Verlinkung** (stärkster Hebel): Hauptmenü „Mehr“ → Uelzen (wie Lüneburg) in Header und Footer aller Seiten;
      auf `/lueneburg/` im Standort-Text „Uelzen“ auf `/uelzen/` verlinken, auf `/uelzen/` „Lüneburg“ auf `/lueneburg/`;
      Startseite oder Footer „Standorte: Lüneburg · Uelzen“
- [ ] Google Search Console: URL-Prüfung → Live-URL testen → Indexierung beantragen; Rich-Results-Test
- [ ] Bing: IndexNow-Plugin oder URL in Bing Webmaster Tools einreichen (IndexNow ohne Schlüsseldatei im Root scheitert, siehe Lüneburg)
- [ ] Google Unternehmensprofil: Leistungsgebiet Uelzen/Landkreis Uelzen, Leistungen „Schließanlagen“, „Zutrittskontrolle“,
      „Videoüberwachung“, Beitrag mit Link auf `/uelzen/`; Bewertungen mit Ortsnennung erbitten
- [ ] Lokale Zitationen (NAP identisch mit Impressum und Schema): IHK Lüneburg-Wolfsburg, Handwerkskammer, Gelbe Seiten,
      11880, Das Örtliche, Cylex, Bing Places, Apple Business Connect – jeweils mit Website-Link
- [ ] Backlinks mit Uelzen-Bezug: Partnerverzeichnisse (EVVA Certified Partner, SimonsVoss-Partnersuche), Kundenreferenzen,
      lokale Presse (AZ Uelzen), Vereins-/Veranstaltungssponsoring im Landkreis
- [ ] Alt-Texte der Mediathek nach `elementor/media-alt-texte.json` prüfen (gelten site-weit, deshalb ortsneutral formuliert)
- [ ] Nach 2–4 Wochen: Search-Console-Leistungsbericht nach „Uelzen“ filtern, Texte an echte Suchanfragen anpassen

## 8a. Messwerte nach Veröffentlichung (27.10.2026, `tools/audit_live.py`)

| Prüfpunkt | Wert |
| --- | --- |
| HTTP / Canonical / Robots | 200 · `https://provision-infra.de/uelzen/` · index, follow |
| Titel / Description | 58 Zeichen / 153 Zeichen (Yoast, wie Abschnitt 2) |
| H1 | 1× „Mechanische & elektronische Schließanlagen sowie Videoüberwachung in Uelzen“ |
| Sichtbarer Text | ca. 2.100 Wörter |
| Vorkommen | Uelzen 40 · Landkreis Uelzen 6 · Schließanlage 29 · Videoüberwachung 15 (davon „Videoüberwachung in Uelzen“ 5) · Zutrittskontrolle 5 · Bad Bevensen 11 |
| Interne Links | `/zutrittssystem/`, `/kamerasysteme/`, `/anfrage-auswahl/`, `tel:`, `mailto:` |
| Schema | Yoast WebPage/BreadcrumbList/WebSite · ProvenExpert Product · eigenes LocalBusiness+Locksmith mit 2× Service · EA FAQPage (11 Fragen) |
| Bilder ohne Alt | 10 (dekorative Linien/Icons, wie auf /lueneburg/) |

Hinweis: Die exakte Phrase „Schließanlagen Uelzen“ steht nur im Titel; im Text wird sie natürlich getrennt verwendet
(„Schließanlagen & Zutrittskontrolle in Uelzen“, „Schließanlage in Uelzen“). Yoast wertet das bei flexibler
Keyphrase-Erkennung, Google ohnehin.

## 9. Erfolgsmessung

- Search Console: Impressionen/Klicks für Anfragen mit „Uelzen“, Position für „Schließanlagen Uelzen“, „Videoüberwachung
  Uelzen“, „Sicherheitstechnik Uelzen“ (Ziel: Top 3 innerhalb von 3–6 Monaten, da geringer Wettbewerb im Heimatlandkreis).
- Google Unternehmensprofil: Anrufe, Routenanfragen, Website-Klicks aus Uelzen.
- Website: Formular-Starts auf `/anfrage-auswahl/` mit Referrer `/uelzen/`, Abschlussquote je Formular.

## 10. Erweiterung

- Referenzprojekt in Uelzen mit Foto als eigener Abschnitt (gleiches Glass-Card-Design).
- Weitere Stadtseiten nach demselben Muster: `tools/build_uelzen.py` kopieren, `TEXT`, `FAQ`, `SCHEMA`, `SEO_*`,
  `SLUG`, `MENU_SLUG` austauschen – das Skript meldet jede nicht ersetzte Quellstelle.
