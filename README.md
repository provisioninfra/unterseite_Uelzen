# unterseite_Uelzen

Unterseite **/uelzen/** für provision-infra.de: mechanische & elektronische Schließanlagen, Zutrittskontrolle sowie
Video- und Kameraüberwachung für Betriebe, Praxen und Hausverwaltungen in Uelzen und im Landkreis Uelzen.

**Live seit 27.10.2026:** https://provision-infra.de/uelzen/ (WordPress-Seite #4605, Elementor; Menü „Menü Uelzen“ #19,
Slug `menue-uelzen`). Dieses Repository enthält die Quelle der Elementor-Daten, das Build-Skript und das SEO-Konzept.

Die Seite ist das Uelzen-Gegenstück zur Lüneburg-Seite (Repo `provisioninfra/schliessanlagen-lueneburg`, Seite #4496,
https://provision-infra.de/lueneburg/). Design, Abschnittsfolge, Animationen und Medien sind 1:1 übernommen; alle Texte,
die FAQ, das Schema-Markup und die SEO-Werte sind neu für Uelzen geschrieben (keine Textduplikate zur Lüneburg-Seite).

## Inhalt

| Pfad | Zweck |
| --- | --- |
| `elementor/uelzen.elementor.json` | Elementor-Elemente + Seiteneinstellungen + Yoast-Werte der Uelzen-Seite (Ergebnis des Builds) |
| `elementor/uelzen.live-2026-11-02.json` | Live-Stand der Seite nach dem Eingriff vom 02.11.2026 (Export aus dem Editor); enthält zusätzlich die in WordPress nachträglich eingebaute vierte Kundenstimme und den Absatz mit Links auf /lueneburg/ und die Startseite im Standort-Text |
| `tools/seitenweit-querformat-hero-video.html` | Steuer-Snippet (CSS + JS) für Handy-Querformat und Hero-Video, liegt als HTML-Widget am Seitenende aller Landingpages; Hintergrund im Kamera-Repo `QUERFORMAT-UND-HERO-VIDEO.md` |
| `elementor/quelle-lueneburg.elementor.json` | Quelle: Elementor-Daten der Live-Seite /lueneburg/ (Stand 26.10.2026, nur lesen) |
| `elementor/geo.json` | Geokoordinaten des Firmensitzes (für `LocalBusiness.geo`) |
| `elementor/media-alt-texte.json` | Alt-Texte der verwendeten Mediathek-Bilder (site-weit gültig, deshalb ortsneutral) |
| `tools/build_uelzen.py` | Baut `uelzen.elementor.json` aus der Lüneburg-Quelle: Textersetzung, FAQ, Schema, SEO, Prüfungen |
| `tools/audit_live.py` | On-Page-Audit der veröffentlichten Seite (Titel, Description, H1, Wortzahl, Keywords, Schema) |
| `seo/uelzen-seo.md` | Keyword-Konzept, Meta-Daten, Struktur, Schema, Funnel, Veröffentlichung und Indexierungs-Checkliste |
| `seo/uelzen-texte.md` | Alle Texte der Seite in Lesereihenfolge zum Gegenlesen (vom Build erzeugt) |

Formulare und Funnel-Seiten werden nicht dupliziert: alle CTAs führen auf den gemeinsamen Funnel `/anfrage-auswahl/`
(Gravity Form 5), der laut Lüneburg-Konzept für alle Stadtseiten gedacht ist.

## Änderungen vom 02.11.2026 (live)

- Hero-Videos auf kleine Fassungen umgestellt: Desktop `startseite-hero-tuer-desktop-2160.mp4` (1,9 MB statt 13,8 MB),
  Handy `startseite-hero-tuer-handy-1440.mp4` (0,8 MB statt 15,4 MB); Start-/Endzeiten unverändert. Der Build setzt die
  URLs über `VIDEO_NEU` in `tools/build_uelzen.py`.
- Steuer-Snippet als letzter Container: blendet im Handy-Querformat das feste ProvenExpert-Siegel aus und verkleinert das
  Cookie-Symbol, lädt unsichtbare Hero-Videos nicht, spielt das Hero-Video einmal und nach dem Zurückscrollen erneut ab
  und startet es bei blockiertem Autoplay (Stromsparmodus) mit der ersten Berührung.
- Achtung: Die Live-Seite wurde nach dem Build vom 27.10. direkt in WordPress erweitert (vierte Kundenstimme „Vincent
  Oswald“, Absatz mit internen Links im Standort-Text). Der Build bildet das nicht ab; für Änderungen an der Live-Seite
  immer vom Editor-Export ausgehen (`elementor/uelzen.live-2026-11-02.json`).
- Am 02.11.2026 hat parallel die Sitzung „Neue Unterseite mit Videoüberwachung“ (Kamera-Repo) auf derselben Seite einen
  eigenen Container „Steuerung Ladeverhalten“ (unsichtbare Lottie-/Video-Blöcke nicht laden, ProvenExpert-Product-Schema
  aus dem DOM entfernen) ergänzt und am Siegel-Widget die Handy-Ausblendung entfernt sowie eine Querformat-Regel gesetzt.
  Beide Steuer-Container liegen getrennt am Seitenende; vor jedem Speichern frisch exportieren und die andere Sitzung
  informieren, sonst überschreibt der jeweils letzte Speichervorgang den anderen (so geschehen am 02.11. um 09:56 auf
  /lueneburg/, danach wiederhergestellt).

- 02.11.2026, 13:23 Uhr: Kundenstimme „Pia-Theresa“ ergänzt um die Firma („Geschäftsführerin, Digitale Hanseaten“),
  gleichzeitig auf Startseite, /kamerasysteme/ und /lueneburg/. Im Build über das Element `426f36df` gesetzt.

## Design

Farben (Kit: `#000D30`, `#263E96`, `#FBC91B`), Typografie (Poppins/Roboto) und Animationen (fadeInLeft/Right/Up,
Glass-Container, Lottie-Kamera mit Leuchtlinie, Lottie-Timeline, Hero-Video, Vimeo-Film) stammen unverändert aus der
Lüneburg-Seite und damit aus den Elementor-Abschnitten der Startseite und der Kamera-Seite.

## Nachbauen

```bash
python3 -I tools/build_uelzen.py elementor/quelle-lueneburg.elementor.json elementor            # post_status: draft
python3 -I tools/build_uelzen.py elementor/quelle-lueneburg.elementor.json elementor --publish  # post_status: publish
```

Das Skript bricht ab, wenn ein Quelltext nicht mehr gefunden wird, ein Lüneburg-Rest übrig bleibt, ein alter
CTA-Link steht, Element-IDs doppelt sind oder Titel/Description zu lang werden.

## In WordPress anlegen (so wurde die Seite am 27.10.2026 angelegt)

Zugangsdaten gehören nicht in dieses Repo (siehe `WORDPRESS-REGELN.md` im Kamera-Repo). Vorgehen wie bei /lueneburg/:

1. Seite anlegen: REST `POST /wp-json/wp/v2/pages` (Cookie-Login + `X-WP-Nonce`), `title` „Schließanlagen &
   Videoüberwachung Uelzen“, `slug` `uelzen`, `status` `draft`.
2. Menü „Menü Uelzen“ (Slug `menue-uelzen`) anlegen – Name muss mit „Me…“ beginnen, damit „Main“ alphabetisch erstes
   Menü bleibt (Fallback der Footer-Nav-Widgets). Einträge wie im Menü Lüneburg: Schließanlagen `#schliessanlagen`,
   Videoüberwachung `#kamera`, So arbeiten wir `#arbeiten`, Über uns `#ueber`, FAQ `#FAQ`.
3. Elementor-Editor der neuen Seite öffnen (`post.php?post=ID&action=elementor`) und speichern:
   `elementorCommon.ajax.addRequest('save_builder', { data: { status: 'draft', elements, settings } })` mit `elements`
   und `settings` aus `elementor/uelzen.elementor.json`. Kein Vorlagen-Import (verliert das Design).
4. Yoast im Block-Editor über `wp.data.dispatch('yoast-seo/editor')` setzen: Werte aus dem `seo`-Block der JSON
   (Titel, Description, Fokus-Keyphrase, Breadcrumb-Titel `Uelzen`, `index`, OG-Bild), dann `savePost()`.
   Lerneffekt: nach `updateData` etwa 6 Sekunden warten, bis Yoast die Metabox-Felder (`#yoast_wpseo_title`,
   `#yoast_wpseo_metadesc`, …) befüllt hat, sonst speichert der Beitrag ohne SEO-Werte; Ergebnis per REST
   (`yoast_head_json`) prüfen.
5. Vorschau prüfen (Desktop/Mobil, `?nowprocket=1`), dann veröffentlichen und die Checkliste in `seo/uelzen-seo.md`
   Abschnitt 8 abarbeiten (Sitemap, Search Console, interne Links, Unternehmensprofil).

Der Server drosselt schnelle Folgeaufrufe (HTTP 429, nginx): zwischen REST-Aufrufen 3–5 Sekunden Pause, Elementor-Save
bei 429 nach 30 Sekunden wiederholen.
