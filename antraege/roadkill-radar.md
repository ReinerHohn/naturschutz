# Roadkill-Radar — Melde- und Analyseplattform fuer Wildunfaelle — Pitch & Foerderantrag

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
In Deutschland gibt es jaehrlich hunderttausende Wildunfaelle — mit Personenschaeden, hohen Sachkosten und massivem Tierverlust, auch bei geschuetzten Arten. Die amtliche Statistik erfasst im Kern nur jagdbares Grosswild; Amphibien, Igel und Kleinsaeuger fehlen. Gleichzeitig kostet eine Gruenbruecke ab ca. 3 Mio. EUR (Beispiele 3,4 bis ueber 20 Mio. EUR). Roadkill-Radar sammelt Meldungen von Buergern, Jaegern und Polizei, findet per Statistik und KI die echten Hotspots und liefert Strassenbauverwaltungen eine datenbasierte Priorisierung — damit teure Querungshilfen dort entstehen, wo sie am meisten nuetzen.

### Das Problem (mit Zahlen)
Jaehrlich ereignen sich in Deutschland hunderttausende Wildunfaelle — mit Personenschaeden, hohen Sachkosten und erheblichem Verlust an Tieren, auch geschuetzten Arten. Die amtliche Statistik erfasst im Kern nur jagdbares Grosswild; Amphibien, Igel, Kleinsaeuger und viele Arten fehlen voellig. Gleichzeitig muss die oeffentliche Hand knappe Mittel fuer Querungshilfen priorisieren: Eine Gruenbruecke kostet grob 3 Mio. EUR und mehr (Beispiele 3,4 bis ueber 20 Mio. EUR), Amphibienanlagen entsprechend. Treiber sind das Bundesprogramm Wiedervernetzung, Verkehrssicherheit (Vision Zero), FFH-/Artenschutz und kommunale Amphibienschutz-Pflichten. Es fehlt eine belastbare, flaechendeckende Datengrundlage, um zu entscheiden, WO eine Querungshilfe oder ein Tempolimit den groessten Nutzen bringt.

### Die Loesung
Eine Plattform aus Melde-App/PWA und Auswerte-Backend:
- **Melder** (Buerger, Jaeger, Polizei, Strassenmeistereien) erfassen Fundort, Art und Zeit mit wenigen Klicks; Foto-Arterkennung und Plausibilitaetspruefung unterstuetzen.
- Das **Backend** verdichtet Meldungen zu Hotspots (raeumlich-zeitliche Statistik, Kernel-Dichte, saisonale Amphibienwanderungs-Muster) und verknuepft sie mit Strassen-, Habitat- und Verkehrsdaten, um Risiko-Abschnitte zu priorisieren.
- **Ergebnis** sind Karten und Reports, die Strassenbauverwaltungen direkt in die Massnahmenplanung uebernehmen koennen.

Der Code ist offen und GBIF-/Standard-anschlussfaehig; verdient wird an Plattform-Betrieb, Hotspot-Analysen und Beratung. Ausdruecklicher Datenaustausch mit bestehenden Katastern (z.B. Tierfund-Kataster des DJV) statt Konkurrenz.

### Markt & Kunde (oeffentliche Hand)
- **Autobahn GmbH des Bundes und Landesbetriebe Strassenbau** (z.B. Strassen.NRW, Landesbetrieb Mobilitaet) — Hotspot-Analysen und Priorisierung von Querungshilfen (Rahmenvertrag/Dienstleistung).
- **Untere Strassenverkehrs- und Naturschutzbehoerden der Landkreise** — kommunale Strassen, Amphibienschutzanlagen, Tempolimits (Direktauftrag, seit 2026 oft bis 50.000 EUR netto).
- **Kommunen** fuer innerstaedtische Gefahrenstellen und Amphibien-Querungen.
- **Landesjagdverbaende und Jaegerschaften** als Datenpartner und Multiplikatoren (Abgleich mit dem Tierfund-Kataster des DJV).
- **Landesanstalten fuer Umwelt / Strassenwesen (BASt)** und Verkehrssicherheits-Programme als Auftraggeber groesserer Studien.

Zugangsweg: Einstieg ueber ein gefoerdertes Pilotprojekt mit EINEM Landesbetrieb oder Landkreis; der Hotspot-Report dient als Referenz fuer Ausschreibungen. Kleinere Mandate laufen als Direktauftrag unter der Wertgrenze.

### Geschaeftsmodell & Finanzen
B2G-Datenplattform mit Open-Core. Preismodell (aus Projektkalkulation):
- Plattform-/Betriebs-Lizenz je Mandant: ca. 5.000–20.000 EUR/Jahr (Hosting, Support, Updates).
- Hotspot-Analyse-Report: ca. 3.000–15.000 EUR je Netz/Gebiet.
- Beratung/Priorisierung: ca. 800–1.200 EUR/Tag.
- Wirkungskontrolle nach Massnahme: ca. 2.000–8.000 EUR je Standort/Saison.

Fixkosten sind Entwicklung und Hosting/GIS-Infrastruktur; variable Kosten je Report gering. **Break-even** als kleines Team realistisch bei wenigen Betriebs-Lizenzen plus einigen Analyse-/Beratungsauftraegen (ca. 40–80 TEUR Umsatz). Der oekonomische Hebel ist gewaltig: Eine Gruenbruecke kostet ab ca. 3 Mio. EUR — eine einzelne vermiedene Fehlplanung oder gut platzierte Querungshilfe rechtfertigt die Analyse-Kosten um Groessenordnungen. Herausforderung ist nicht die Technik, sondern genug qualitativ hochwertige Meldungen (Datendichte) und der Zugang zu Strassenbauverwaltungen.

### Warum Open Source + 3D-Druck (bzw. offene Daten/Standards)
Dieses Projekt ist softwarelastig — der ehrliche Alleinstellungs-Hebel sind **offene Daten und Standards**, nicht 3D-Druck. Offener Code und offene Daten-Standards machen die Risikobewertung nachpruefbar und gerichtsfest — zentral, wenn damit Investitionen in Millionenhoehe (Gruenbruecke) begruendet werden. "Public Money, Public Code" und digitale Souveraenitaet senken die Vergabehuerde; keine Dateninsel, Anschluss an Tierfund-Kataster/GBIF schafft Vertrauen bei Jagd- und Naturschutzpartnern. Geld kommt nicht aus der Software-Lizenz, sondern aus gehostetem Betrieb, fachlich aufbereiteten Hotspot-Analysen und Massnahmen-Beratung. 3D-Druck ist nur ein optionaler Nebenhebel: gedruckte, reflektierende Melde-/Warnstelen und QR-Schilder an bekannten Hotspots (saisonale Amphibien-Warnung) mit wetterfesten Halterungen (PETG/ASA), lokal und in Inklusionswerkstaetten herstellbar; perspektivisch Schnittstelle zu gedruckten Sensor-/Zaehl-Gehaeusen an Querungshilfen (Wirkungskontrolle).

### Traktion & naechste 90 Tage
- **Tag 0–30:** Melde-MVP bauen (PWA plus Karte), Datenmodell GBIF-/Tierfund-Kataster-kompatibel, Doppelerfassung vermeiden.
- **Tag 30–60:** Daten-/Kooperationspartner sichern — Landesjagdverband oder DJV (Tierfund-Kataster), ggf. Polizei-Meldewege; einen Landesbetrieb Strassenbau oder Landkreis als Pilot ansprechen (moeglichst gefoerdert ueber Bundesprogramm Wiedervernetzung) plus LOI.
- **Tag 60–90:** Hotspot-Analyse-Methodik entwickeln und mit vorhandenen Daten validieren (raeumlich-zeitliche Statistik, Amphibien-Saisonalitaet, Bias-Korrektur); offenes Repo plus Doku auf openCode veroeffentlichen; mFUND-Antrag einreichen.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: mFUND (BMDV), Foerderlinie 1 — Machbarkeitsstudie.** mFUND foerdert datenbasierte digitale Anwendungen rund um Mobilitaet und Verkehr; Wildunfall-/Verkehrsdaten und die Verknuepfung mit Strassen-/Verkehrsnetzen passen inhaltlich perfekt. Foerderlinie 1 (Machbarkeit) umfasst grob bis ca. 100.000 EUR bei bis zu 12 Monaten Laufzeit — ideal, um Melde-MVP, Hotspot-Methodik mit Bias-Korrektur und Behoerden-Pilot auf Tragfaehigkeit zu pruefen. **Alternativen: Prototype Fund** fuer den offenen Plattform-Kern, **DBU** (Umwelttechnik/Digitalisierung, Verkehr und Natur), **Bundesprogramm Wiedervernetzung (BMUV/BfN)** fuer Querungshilfen samt begleitendem Monitoring, **Bundesprogramm Biologische Vielfalt (BfN)** sowie **BASt/Vision-Zero-Forschungsmittel** und **EU LIFE**.

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**Roadkill-Radar — offene Melde- und Analyseplattform zur datenbasierten Priorisierung von Querungshilfen.**
Wildunfaelle verursachen Personen- und Sachschaeden und toeten viele, auch geschuetzte Arten; die amtliche Statistik erfasst im Kern nur Grosswild. Querungshilfen kosten Millionen und muessen treffsicher platziert werden. Das Vorhaben entwickelt und erprobt eine offene Plattform (Melde-PWA plus Auswerte-Backend), die Meldungen von Buergern, Jaegern und Polizei bias-korrigiert zu belastbaren Hotspots verdichtet und mit Strassen-/Verkehrsdaten zu einer Priorisierungs-Entscheidungsvorlage fuer Strassenbauverwaltungen verknuepft. Datenmodell und Code sind GBIF-/Tierfund-Kataster-anschlussfaehig und offen. Ziel ist der Nachweis der technischen, methodischen und wirtschaftlichen Tragfaehigkeit mit einem Behoerdenpiloten.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Es fehlt eine flaechendeckende, belastbare Datengrundlage zu Wildunfaellen jenseits des Grosswilds. Ohne sie werden Millionen-Investitionen in Querungshilfen auf unsicherer Basis geplant. Treiber sind Bundesprogramm Wiedervernetzung, Vision Zero, FFH-/Artenschutz und kommunale Amphibienschutz-Pflichten. Citizen-Science-Melder liefern die Datenbasis nahezu kostenlos — Wertschoepfung liegt in Verdichtung, Bias-Korrektur, Validierung und Entscheidungsvorlage. Oekologisch und verkehrssicherheitstechnisch ist der Nutzen doppelt: weniger tote Tiere und weniger Unfaelle.

### Projektziele & Innovationsgehalt
- **Melde-PWA** mit Foto-Arterkennung und Plausibilitaetspruefung, GBIF-/Tierfund-Kataster-kompatibel.
- **Bias-korrigierte Hotspot-Methodik** (raeumlich-zeitliche Statistik, Kernel-Dichte, Verkehrsstaerke/Erfassungsaufwand, Amphibien-Saisonalitaet).
- **Verknuepfung mit Strassen-/Habitat-/Verkehrsdaten** zur Risiko-Priorisierung.
- **Gerichtsfeste, offene Entscheidungsvorlage** (Karten/Reports) fuer Strassenbauverwaltungen.
Innovationsgehalt: die bias-korrigierte, offene und nachpruefbare Verkettung von Citizen-Science-Meldung bis zur haushaltsrelevanten Massnahmen-Priorisierung — mit expliziter Kooperation statt Parallel-Kataster.

### Arbeitspakete

**AP1 — Melde-MVP & Datenmodell (Monat 1–3)**
- Ziel: Einfache, saubere Erfassung ohne Doppelstrukturen.
- Inhalt: PWA plus Karte, GBIF-/Tierfund-Kataster-kompatibles Datenmodell, Foto-Arterkennung, Plausibilitaetspruefung.
- Deliverable: Lauffaehige Melde-PWA plus Datenmodell-Spezifikation.
- Dauer: 3 Monate.

**AP2 — Datenpartner & Kooperation (Monat 2–5)**
- Ziel: Datendichte und Vertrauen sichern.
- Inhalt: Kooperation mit Landesjagdverband/DJV (Tierfund-Kataster), ggf. Polizei-Meldewege, DSGVO-Konzept, GBIF-Anbindung.
- Deliverable: Kooperationsvereinbarung(en) plus Datenaustausch-Schnittstelle.
- Dauer: 4 Monate.

**AP3 — Hotspot-Methodik mit Bias-Korrektur (Monat 3–8)**
- Ziel: Belastbare, nachpruefbare Hotspots statt Schein-Hotspots.
- Inhalt: Raeumlich-zeitliche Statistik, Kernel-Dichte, Verkehrsstaerke-Normierung, Saisonalitaet, Validierung an vorhandenen Daten.
- Deliverable: Dokumentierte, validierte Hotspot-Methodik plus Guetemasse.
- Dauer: 6 Monate.

**AP4 — Behoerden-Report & Priorisierung (Monat 6–10)**
- Ziel: Direkt uebernehmbare Entscheidungsvorlage.
- Inhalt: Verknuepfung mit Strassen-/Habitatdaten, Priorisierungs-Logik, Karten/Report-Generator, Experten-Validierung.
- Deliverable: Behoerden-tauglicher Hotspot-Report plus Priorisierungs-Werkzeug.
- Dauer: 5 Monate.

**AP5 — Pilot, Open-Source-Release & Verwertung (Monat 8–12)**
- Ziel: Referenz schaffen und Markteinstieg vorbereiten.
- Inhalt: Pilot mit Landesbetrieb/Landkreis, konkrete Massnahmen-Empfehlung, Repo plus Doku auf openCode, Geschaeftsmodell-Schaerfung.
- Deliverable: Pilot-Report (Massnahmen-Empfehlung), Open-Source-Release, Verwertungsplan.
- Dauer: 5 Monate.

### Zeit- & Meilensteinplan (Monat 0–12)
- **M1 (Monat 3):** Melde-PWA laeuft, Datenmodell kataster-kompatibel.
- **M2 (Monat 6):** Datenpartner gesichert, erste bias-korrigierte Hotspot-Auswertung.
- **M3 (Monat 9):** Behoerden-tauglicher Report plus Priorisierungs-Werkzeug, Pilot gestartet.
- **M4 (Monat 12):** Pilot-Report mit konkreter Massnahmen-Empfehlung, Open-Source-Release plus Verwertungsplan veroeffentlicht.

### Kosten- & Finanzierungsplan

| Position | Betrag (EUR) |
|---|---|
| Personal (Gruender/in Vollzeit 12 Mon. plus anteilig Entwicklung/Statistik) | 64.000 |
| Sachkosten / Material (Buero, optional 3D-Druck-Warnstelen fuer Feldtest) | 3.000 |
| Hardware / Cloud (Hosting, GIS-Infrastruktur, Datenbank, GPU-Arterkennung, Laptop) | 12.000 |
| Fremdleistung (DSGVO-/Rechtscheck, Fachgutachten Verkehr/Oekologie, UI/Design) | 13.000 |
| Reise (Datenpartner, Pilot-Behoerde, Feldtests, Fachkonferenz) | 4.000 |
| **Summe** | **96.000** |
| Foerderquote (mFUND Machbarkeit, bis 100 %) | bis 96.000 |
| Eigenanteil (bei anteiliger Foerderung, z.B. 10 %) | ca. 9.600 |

Hinweis: mFUND-Linie-1-Machbarkeit wird fuer einzelne Antragsteller haeufig mit hoher bis voller Quote gefoerdert; die konkrete Quote ist mit dem Programmtraeger abzustimmen. Zahlen als Planansatz, teils "ca.".

### Verwertung & Tragfaehigkeit nach Foerderende
Nach Projektende traegt sich die Plattform ueber wiederkehrende Betriebs-Lizenzen je Mandant, Hotspot-Analyse-Reports, Priorisierungs-/Wirkungskontroll-Beratung und Datenintegration. Der Pilot-Report dient als Referenz fuer die Autobahn GmbH, Landesbetriebe Strassenbau und Landkreise. Open-Core: offener Kern fuer Vergabefaehigkeit und Nachpruefbarkeit, bezahlte Leistung ist der gehostete Betrieb plus die fachliche Verdichtung/Beratung. Break-even bei grob 40–80 TEUR wiederkehrendem Umsatz; der Hebel gegenueber Millionen-Baukosten ist das staerkste Verkaufsargument.

### Open-Source-/Gemeinwohl-Bezug
Offener Code und offene Daten-Standards (GBIF-/Tierfund-Kataster-anschlussfaehig, auf openCode auffindbar) machen millionenschwere Investitions-Begruendungen gerichtsfest und souveraen und verhindern Dateninseln. Die Daten liefern Buerger, Jaeger und Polizei weitgehend kostenlos; Nachnutzung durch Forschung und weitere Behoerden ist erwuenscht. Gemeinwohl entsteht durch weniger Unfaelle (Vision Zero) und besseren Artenschutz/Wiedervernetzung.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
Konkrete Zielpartner fuer Letter of Intent (LOI):
- Ein **Landesbetrieb Strassenbau** (z.B. Strassen.NRW oder Landesbetrieb Mobilitaet) oder die **Autobahn GmbH des Bundes** als Pilot-Auftraggeber fuer Hotspot-Priorisierung.
- Eine **untere Strassenverkehrs-/Naturschutzbehoerde (Landkreis)** fuer kommunale Strassen und Amphibienanlagen (Direktauftrag unter Wertgrenze).
- Als **Datenpartner** der **Landesjagdverband/DJV** (Tierfund-Kataster) und ggf. Polizei-Meldewege.
LOI-Strategie: Fruehzeitig EINEN Landesbetrieb oder Landkreis mit konkretem Planungsbedarf (anstehende Querungshilfe/Amphibien-Hotspot) fuer einen gefoerderten Pilot plus LOI gewinnen; parallel Datenpartner-Kooperation (DJV) sichern, um Datendichte und Vertrauen zu belegen. Pilot-Report als Referenz fuer Ausschreibungen.

### Risiken & Gegenmassnahmen

| Risiko | Massnahme |
|---|---|
| Melde-Bias (Schein-Hotspots dort, wo viele Menschen sind) | Bias-Korrektur ueber Verkehrsstaerke/Erfassungsaufwand fest in die Methodik (AP3) |
| KI-Arterkennung mit Fehlerraten | Keine Auto-Entscheidung; Experten-Validierung fuer haushalts-/gerichtsrelevante Faelle |
| Datenschutz (Standort-/Personen-/Polizei-Daten, DSGVO) | DSGVO-Konzept, Pseudonymisierung, Sonderregeln fuer Polizeidaten beachten (AP2) |
| Doppelstruktur/Konkurrenz zum Tierfund-Kataster | Kooperation und Datenaustausch statt Parallel-Kataster (DJV/GBIF einbinden) |
| Zu geringe Datendichte | Fruehe Multiplikatoren (Jagd, Polizei, Vereine), einfache PWA, Anreize/Gamification |
| Lange Beschaffung, langfristig gebundene Strassenbau-Budgets | Gefoerderter Pilot, Direktauftrag-Einstieg unter Wertgrenze, Anbindung ans Bundesprogramm Wiedervernetzung |
| Foerderabhaengigkeit | Fruehe zahlende Mandate/Analysen, wiederkehrende Betriebs-Lizenzen aufbauen |
