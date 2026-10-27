# unterseite_Uelzen

Unterseite **/uelzen/** für provision-infra.de: mechanische & elektronische Schließanlagen, Zutrittskontrolle sowie
Video- und Kameraüberwachung für Betriebe, Praxen und Hausverwaltungen in Uelzen und im Landkreis Uelzen.

Die Seite ist das Uelzen-Gegenstück zur Lüneburg-Seite (Repo `provisioninfra/schliessanlagen-lueneburg`, Seite #4496,
https://provision-infra.de/lueneburg/). Design, Abschnittsfolge, Animationen und Medien sind 1:1 übernommen; alle Texte,
die FAQ, das Schema-Markup und die SEO-Werte sind neu für Uelzen geschrieben (keine Textduplikate zur Lüneburg-Seite).

## Inhalt

| Pfad | Zweck |
| --- | --- |
| `elementor/uelzen.elementor.json` | Elementor-Elemente + Seiteneinstellungen + Yoast-Werte der Uelzen-Seite (Ergebnis des Builds) |
| `elementor/quelle-lueneburg.elementor.json` | Quelle: Elementor-Daten der Live-Seite /lueneburg/ (Stand 26.10.2026, nur lesen) |
| `elementor/geo.json` | Geokoordinaten des Firmensitzes (für `LocalBusiness.geo`) |
| `elementor/media-alt-texte.json` | Alt-Texte der verwendeten Mediathek-Bilder (site-weit gültig, deshalb ortsneutral) |
| `tools/build_uelzen.py` | Baut `uelzen.elementor.json` aus der Lüneburg-Quelle: Textersetzung, FAQ, Schema, SEO, Prüfungen |
| `tools/audit_live.py` | On-Page-Audit der veröffentlichten Seite (Titel, Description, H1, Wortzahl, Keywords, Schema) |
| `seo/uelzen-seo.md` | Keyword-Konzept, Meta-Daten, Struktur, Schema, Funnel, Veröffentlichung und Indexierungs-Checkliste |
| `seo/uelzen-texte.md` | Alle Texte der Seite in Lesereihenfolge zum Gegenlesen (vom Build erzeugt) |

Formulare und Funnel-Seiten werden nicht dupliziert: alle CTAs führen auf den gemeinsamen Funnel `/anfrage-auswahl/`
(Gravity Form 5), der laut Lüneburg-Konzept für alle Stadtseiten gedacht ist.

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

## In WordPress anlegen

Zugangsdaten gehören nicht in dieses Repo (siehe `WORDPRESS-REGELN.md` im Kamera-Repo). Vorgehen wie bei /lueneburg/:

1. Seite anlegen: REST `POST /wp-json/wp/v2/pages` (Cookie-Login + `X-WP-Nonce`), `title` „Schließanlagen &
   Videoüberwachung Uelzen“, `slug` `uelzen`, `status` `draft`.
2. Menü „Menü Uelzen“ (Slug `menue-uelzen`) anlegen – Name muss mit „Me…“ beginnen, damit „Main“ alphabetisch erstes
   Menü bleibt (Fallback der Footer-Nav-Widgets). Einträge wie im Menü Lüneburg: Schließanlagen `#schliessanlagen`,
   Videoüberwachung `#kamera`, Ablauf `#arbeiten`, Standort `#standort`, FAQ `#FAQ`.
3. Elementor-Editor der neuen Seite öffnen (`post.php?post=ID&action=elementor`) und speichern:
   `elementorCommon.ajax.addRequest('save_builder', { data: { status: 'draft', elements, settings } })` mit `elements`
   und `settings` aus `elementor/uelzen.elementor.json`. Kein Vorlagen-Import (verliert das Design).
4. Yoast im Block-Editor über `wp.data.dispatch('yoast-seo/editor')` setzen: Werte aus dem `seo`-Block der JSON
   (Titel, Description, Fokus-Keyphrase, Breadcrumb-Titel `Uelzen`, `index`, OG-Bild), dann `savePost()`.
5. Vorschau prüfen (Desktop/Mobil, `?nowprocket=1`), dann veröffentlichen und die Checkliste in `seo/uelzen-seo.md`
   Abschnitt 8 abarbeiten (Sitemap, Search Console, interne Links, Unternehmensprofil).
