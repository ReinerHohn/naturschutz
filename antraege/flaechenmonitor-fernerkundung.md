# FlaechenMonitor — Fernerkundungs-SaaS fuer Umwelt- und Agraraemter — Pitch & Foerderantrag

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
Behoerden muessen seit 2023 EU-weit alle Agrar-Antragsflaechen per Satellit ueberwachen (Area Monitoring System, AMS) — und zusaetzlich Moor-Wiedervernaessung, FFH-Gruenland und das EU-Renaturierungsgesetz belegen. Die Rohdaten von Copernicus/Sentinel sind gratis, aber den Aemtern fehlen Pipeline, KI und Personal, um daraus pruefbare Aussagen zu machen. FlaechenMonitor liefert parzellenscharfe Ampel-Karten: Wann wurde gemaeht? Ist das Moor nass? Wo wird versiegelt? Betriebener Dienst statt Lizenz, offener QGIS-Kern statt Vendor-Lock-in — rechtssicher, souveraen, guenstig.

### Das Problem (mit Zahlen)
Flaechengebundene Auflagen mussten frueher per teurer, stichprobenhafter Vor-Ort-Begehung kontrolliert werden — das deckt nur Bruchteile ab und ist nicht flaechendeckend beweisbar. Der regulatorische Treiber ist hart: Seit dem 1.1.2023 ist das Area Monitoring System (AMS) in der EU-Agrarfoerderung Pflicht — alle Antragsflaechen muessen regelmaessig per Sentinel-Satellit auf Aktivitaeten wie Mahd oder Beweidung geprueft werden. Hinzu kommen Nachweise fuer Agrarumwelt- und Klimamassnahmen (z.B. spaete Mahd zum Wiesenbrueter-Schutz), Moor-Wiedervernaessungs-Monitoring, FFH-Gruenland-Erhaltungszustand und die Zustands-Berichtspflichten des EU-Renaturierungsgesetzes. Die Rohdaten (Sentinel-1 Radar, Sentinel-2 optisch) sind bewusst gratis und offen — aber ohne Auswerte-Pipeline, KI-Modelle und Fachpersonal bleiben sie fuer viele Aemter unbrauchbar.

### Die Loesung
Eine SaaS-Plattform, die freie Sentinel-1- (Radar, wolkenunabhaengig) und Sentinel-2-Zeitreihen (optisch) automatisch auswertet:
- KI erkennt Mahd- und Beweidungs-Ereignisse samt Zeitpunkt.
- Vegetations- und Wasserindizes (NDVI/NDWI) verfolgen Gruenland- und Moor-Zustand ueber die Saison.
- Landnutzungs- und Versiegelungsaenderungen werden gemeldet.

Ausgabe: parzellenscharfe Ampel-Karten, Ereignis-Logs und ein pruefbarer Report pro Flaeche fuer die Akte. Die Auswerte-Pipeline (Datenzugriff ueber offene Copernicus-Dienste, KI-Modelle, QGIS-Export) ist Open Source und als QGIS-Plugin plus Web-Dashboard nutzbar. 3D-Druck spielt hier ehrlich nur eine Nebenrolle (optional guenstige Boden-Referenz-/Phaenologie-Kameras zur KI-Validierung). Verkauft wird der betriebene Dienst, nicht die Software.

### Markt & Kunde (oeffentliche Hand)
- **Landwirtschaftsaemter / Landesverwaltungen**, die das EU-AMS umsetzen und Agrarumweltmassnahmen pruefen — ueber Rahmenvertrag oder Ausschreibung (groessere Volumina).
- **Untere Naturschutzbehoerden (Landkreise)** fuer Mahd-Kontrolle in Schutzgebieten und Vertragsnaturschutz — Direktauftrag unter Vergabeschwelle.
- **Landesumweltaemter und Moorschutz-Programme** fuer Vernaessungs- und Gruenland-Zustands-Monitoring.
- **Nationalpark-/Biosphaeren-Verwaltungen** fuer grossflaechiges Landnutzungs-Monitoring.
- **Kommunen** fuer Flaechenverbrauch-/Versiegelungs-Monitoring (Smart Region).
- Als **Nachauftragnehmer/Datenlieferant** fuer GIS-Dienstleister und Planungsbueros ohne eigene Fernerkundung.

Zugangsweg: Einstieg ueber EINE untere Naturschutzbehoerde oder Agrarumwelt-Stelle als gefoerderten Piloten (Direktauftrag unter der Wertgrenze, seit 2026 oft bis 50.000 EUR netto), daraus eine Fallstudie, dann Landkreis-/Landes-Rahmenvertraege und AMS-nahe Ausschreibungen.

### Geschaeftsmodell & Finanzen
B2G-SaaS plus Service mit offenem Kern. Preismodell (aus Projektkalkulation):
- SaaS pro Flaeche: ca. 0,20–1,50 EUR/ha und Jahr (degressiv mit Flaeche).
- Behoerden-Pauschale: ca. 5.000–20.000 EUR/Jahr je nach Gebietsgroesse und Modulen.
- Einzel-Kampagne: ca. 3.000–8.000 EUR (eine Saison, definierte Kulisse, Report).
- Integration/Beratung: ca. 700–1.100 EUR/Tag.

Rohdaten sind gratis, variable Kosten pro Flaeche gering (nur Cloud-Rechenzeit) — das Modell skaliert stark. **Break-even** als kleines Team realistisch bei grob 40–80 TEUR wiederkehrendem Umsatz: ein mittlerer Landkreis-/Landes-Rahmenvertrag plus einige Einzelkampagnen. Ein einziger AMS-naher oder Agrarumwelt-Auftrag kann die Weiterentwicklung tragen. Groesstes Risiko: etablierte, kapitalstarke Grossanbieter und lange Behoerden-Beschaffung.

### Warum Open Source + 3D-Druck
Copernicus-Daten sind bewusst frei und offen — eine offene Auswerte-Pipeline passt exakt zur Linie "Public Money, Public Code" und zur digitalen Souveraenitaet. Entscheidend: Bei AMS-Entscheidungen sind Foerder- und Sanktionsfolgen haftungs- und rechtsrelevant — ein nachvollziehbarer, offener Algorithmus macht die Entscheidung gerichtsfest. Kein Vendor-Lock-in erleichtert Vergabe und Datenuebergabe zwischen Behoerden; ein offenes QGIS-Plugin senkt die Einstiegshuerde. 3D-Druck ist hier ehrlich Nebensache: optional wenige Euro teure, lokal druckbare Referenz-/Validierungsstationen (Wildkamera-/Phaenologie-Gehaeuse an Pegeln), um die Satelliten-KI ground-truth-fest zu kalibrieren; Serienfertigung an eine Inklusionswerkstatt vergebbar. Das Kerngeschaeft ist Software/Service.

### Traktion & naechste 90 Tage
- **Tag 0–30:** MVP-Kern — Sentinel-2-Zeitreihe plus Mahd-Detektion plus parzellenscharfes Karten-Dashboard fuer eine Pilotkulisse.
- **Tag 30–60:** Sentinel-1-Radar ergaenzen (wolkenunabhaengig) fuer zuverlaessige Mahd-/Beweidungs-Erkennung; erstes Gespraech mit einer unteren Naturschutzbehoerde / Agrarumwelt-Stelle plus LOI-Ansprache.
- **Tag 60–90:** Report-/Ausgabeformat mit der Behoerde auf Rechts- und Akten-Tauglichkeit abstimmen (AMS-/Agrarumwelt-konform); QGIS-Plugin plus Doku als Open-Source-Release vorbereiten; Foerderantrag (mFUND Machbarkeit) einreichen.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: mFUND (BMDV), Foerderlinie 1 — Machbarkeitsstudie.** mFUND foerdert datenbasierte digitale Anwendungen rund um Mobilitaet, Geo- und Raumdaten; Fernerkundung/Copernicus-Auswertung fuer die oeffentliche Hand passt in diese Linie. Foerderlinie 1 (Machbarkeit) umfasst grob bis ca. 100.000 EUR bei bis zu 12 Monaten Laufzeit — ideal, um die AMS-/Moor-Auswerte-Pipeline mit einem Behoerdenpiloten auf Trag- und Rechtsfaehigkeit zu pruefen. **Alternativ ESA BIC / Copernicus-Incubator** (Erdbeobachtung, Inkubations-Zuschuss plus Technik-Zugang) als EO-spezifischer Weg. **Weitere Alternativen: DBU** (Monitoring-Innovation Moor/Gruenland), **Prototype Fund** (offenes QGIS-Plugin) und **EXIST-Gruenderstipendium** fuer die Gruendungsphase (Lebensunterhalt plus Sachmittel plus Coaching, 12 Monate).

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**FlaechenMonitor — offene Fernerkundungs-Pipeline fuer rechtssicheres Flaechen-Monitoring in Umwelt- und Agrarverwaltung.**
Seit 2023 ist das EU Area Monitoring System (AMS) pflichtig; zusaetzlich steigen die Berichtspflichten fuer Moor, FFH-Gruenland und Renaturierung. Das Vorhaben entwickelt und erprobt eine offene, nachvollziehbare Auswerte-Pipeline, die freie Sentinel-1/2-Zeitreihen automatisch in parzellenscharfe, aktentaugliche Aussagen (Mahd-Zeitpunkt, Gruenland-/Moor-Zustand, Nutzungsaenderung) uebersetzt. Ergebnis sind ein QGIS-Plugin plus Web-Dashboard, eine validierte Mahd-Detektion und ein mit einer Behoerde abgestimmtes, rechtssicheres Reportformat. Ziel ist der Nachweis der technischen, rechtlichen und wirtschaftlichen Tragfaehigkeit eines betriebenen B2G-Dienstes mit offenem Kern.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Flaechendeckende Kontrolle und Zustandsberichte sind gesetzlich gefordert (AMS seit 1.1.2023, Agrarumweltmassnahmen, FFH, EU-Renaturierungsgesetz, Moorschutz). Vor-Ort-Begehung ist teuer, personalintensiv und nur stichprobenhaft. Die Copernicus-Infrastruktur stellt Sentinel-Daten gratis bereit — doch ohne Pipeline, KI und Fachpersonal koennen viele Aemter sie nicht in pruefbare Entscheidungen ueberfuehren. Oekologisch haengt daran viel: korrekte Mahd-Zeitpunkte schuetzen Wiesenbrueter, belastbares Moor-Monitoring sichert Klima- und Biodiversitaets-Investitionen ab. Gesellschaftlich geht es um rechtssichere, souveraene und guenstige Verwaltungsdigitalisierung ohne Vendor-Lock-in.

### Projektziele & Innovationsgehalt
- Automatische, validierte **Mahd-/Beweidungs-Detektion** aus kombinierten Sentinel-1/2-Zeitreihen (Radar gegen Wolkenluecken).
- **Zustands-Indikatoren** (NDVI/NDWI) fuer Gruenland und Moor mit saisonaler Interpretation.
- **Rechtssicheres, aktentaugliches Reportformat**, mit einer Behoerde abgestimmt (AMS-/Agrarumwelt-konform).
- **Offener Kern** (QGIS-Plugin plus dokumentierte Pipeline) fuer Nachpruefbarkeit und Vergabefaehigkeit.
Innovationsgehalt: Nicht die Rohdaten, sondern die offene, gerichtsfeste Verkettung von Detektion, Zustandsbewertung und behoerdentauglichem Nachweis — mit Naturschutz-/Moor-/Vertragsnaturschutz-Fokus als Nische gegenueber Grossanbietern.

### Arbeitspakete

**AP1 — Daten-Pipeline & Pilotkulisse (Monat 1–3)**
- Ziel: Robuster Zugriff auf Sentinel-1/2 ueber offene Copernicus-Dienste, Vorverarbeitung, Zeitreihen je Parzelle.
- Inhalt: Datenabruf, Cloud-/Wolkenmaskierung, Parzellen-Geometrien, Zeitreihen-Stacks fuer eine Pilotkulisse.
- Deliverable: Reproduzierbare Pipeline plus dokumentierter Pilot-Datensatz.
- Dauer: 3 Monate.

**AP2 — KI-Mahd-Detektion & Zustands-Indikatoren (Monat 2–6)**
- Ziel: Verlaessliche Erkennung von Mahd-/Beweidungs-Ereignissen plus NDVI/NDWI-Zustand.
- Inhalt: Modellbildung Radar+optisch, Zeitpunkt-Schaetzung, Moor-/Gruenland-Indikatoren, Genauigkeitsmessung.
- Deliverable: Validierte Detektions-Modelle plus Genauigkeitsbericht.
- Dauer: 5 Monate.

**AP3 — Ground-Truth & Validierung (Monat 3–7)**
- Ziel: Kalibrierung und Beleg der KI gegen Realitaet.
- Inhalt: Boden-Referenzpunkte, optional 3D-gedruckte Phaenologie-Kameras an Pegeln, Abgleich Satellit vs. Feld.
- Deliverable: Validierungsdatensatz plus Konfidenz-/Fehler-Dokumentation.
- Dauer: 5 Monate.

**AP4 — QGIS-Plugin, Dashboard & rechtssicheres Reportformat (Monat 5–10)**
- Ziel: Nutzbare Ausgabe fuer die Behoerde, aktentauglich.
- Inhalt: Ampel-Karten, Ereignis-Logs, Report-Generator; Abstimmung Rechts-/Aktentauglichkeit mit Pilotbehoerde.
- Deliverable: Open-Source-QGIS-Plugin plus Web-Dashboard plus abgestimmtes Reportmuster.
- Dauer: 6 Monate.

**AP5 — Pilotbetrieb, Fallstudie & Verwertung (Monat 8–12)**
- Ziel: Nachweis der Trag- und Vergabefaehigkeit, Markteinstieg vorbereiten.
- Inhalt: Pilotbetrieb mit Behoerde, Fallstudie, Kosten-/Nutzen-Vergleich zur Vor-Ort-Begehung, Geschaeftsmodell-Schaerfung.
- Deliverable: Fallstudie, Verwertungsplan, Open-Source-Release plus Doku.
- Dauer: 5 Monate.

### Zeit- & Meilensteinplan (Monat 0–12)
- **M1 (Monat 3):** Pipeline laeuft, Pilotkulisse steht, erste Mahd-Events detektiert.
- **M2 (Monat 6):** Validierte Mahd-Detektion plus Zustands-Indikatoren mit dokumentierter Genauigkeit.
- **M3 (Monat 9):** QGIS-Plugin plus Dashboard plus mit Behoerde abgestimmtes Reportformat.
- **M4 (Monat 12):** Pilotbetrieb abgeschlossen, Fallstudie plus Verwertungsplan plus Open-Source-Release veroeffentlicht.

### Kosten- & Finanzierungsplan

| Position | Betrag (EUR) |
|---|---|
| Personal (Gruender/in Vollzeit 12 Mon. plus anteilig studentische/freie Mitarbeit) | 62.000 |
| Sachkosten / Material (3D-Druck-Referenzstationen, Feldzubehoer, Buero) | 4.000 |
| Hardware / Cloud (Rechenzeit Sentinel-Zeitreihen, Speicher, GPU-Training, Laptop/GIS) | 14.000 |
| Fremdleistung (Rechtscheck AMS-/Aktentauglichkeit, Fachgutachten, UI/Design) | 12.000 |
| Reise (Pilotbehoerde, Feld-Ground-Truth, Fachkonferenz) | 4.000 |
| **Summe** | **96.000** |
| Foerderquote (mFUND Machbarkeit, bis 100 %) | bis 96.000 |
| Eigenanteil (bei anteiliger Foerderung, z.B. 10 %) | ca. 9.600 |

Hinweis: mFUND-Linie-1-Machbarkeit wird fuer einzelne Antragsteller haeufig mit hoher bis voller Quote gefoerdert; die konkrete Quote ist mit dem Programmtraeger abzustimmen. Zahlen als Planansatz, teils "ca.".

### Verwertung & Tragfaehigkeit nach Foerderende
Nach Projektende traegt sich der Dienst ueber den betriebenen Monitoring-Betrieb: SaaS-Abo pro Flaeche/Behoerde, gepruefte Reports, Einzel-Kampagnen und Integration in Fachverfahren. Die Fallstudie dient als Referenz fuer Landkreis-/Landes-Rahmenvertraege und AMS-nahe Ausschreibungen. Open-Core-Logik: Basis-Plugin offen, der skalierbare Cloud-Betrieb, die Fach-QS und die Behoerden-Integration sind die bezahlte Leistung. Break-even bei grob 40–80 TEUR wiederkehrendem Umsatz erreichbar.

### Open-Source-/Gemeinwohl-Bezug
Offene Pipeline und offenes QGIS-Plugin auf Copernicus-Basis setzen "Public Money, Public Code" konsequent um, staerken die digitale Souveraenitaet der Verwaltung und machen Foerder-/Sanktions-Entscheidungen nachpruefbar und gerichtsfest. Nachnutzung durch andere Aemter und Dienstleister ist ausdruecklich erwuenscht; Gemeinwohl entsteht durch besseren Wiesenbrueter-, Moor- und Gruenland-Schutz bei geringeren Verwaltungskosten.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
Konkrete Zielpartner fuer Letter of Intent (LOI):
- Eine **untere Naturschutzbehoerde (Landkreis)** fuer Mahd-Kontrolle in Schutz-/Vertragsnaturschutzflaechen (Direktauftrag unter Wertgrenze, schneller Pilot).
- Eine **Agrarumwelt-Stelle / ein Landwirtschaftsamt**, das das AMS umsetzt, fuer den regulatorischen Kernnachweis.
- Ein **Landesumwelt-/Moorschutz-Programm** fuer Vernaessungs-Monitoring.
LOI-Strategie: Fruehzeitig EINE Pilotbehoerde mit konkretem Schmerzpunkt (AMS-Umsetzung oder Moor-Nachweis) einbinden, kostenlosen/gefoerderten Pilot plus LOI vereinbaren, Reportformat gemeinsam rechtstauglich machen; daraus Referenz fuer weitere Verwaltungen.

### Risiken & Gegenmassnahmen

| Risiko | Massnahme |
|---|---|
| Starker Wettbewerb durch kapitalstarke EO-Anbieter/Platzhirsche | Nische ueber Naturschutz-/Moor-/Vertragsnaturschutz-Fokus plus offene, guenstige Pipeline |
| Sentinel-Aufloesung (10 m) begrenzt kleinteilige Flaechen | Realistische Kulissen waehlen; perspektivisch hochaufloesende Daten/Drohne als Ergaenzung |
| Wolken bei rein optischer Auswertung | Sentinel-1-Radar (wolkenunabhaengig) fest einplanen |
| AMS-Entscheidungen haftungs-/rechtsrelevant | Ground-Truth-Validierung, Konfidenzangaben, Experten-Review, abgestimmtes Reportformat |
| Lange, an Fachverfahren gebundene Behoerden-Beschaffung | Offener Kern/kein Lock-in, Direktauftrag-Einstieg unter Wertgrenze, Integration statt Ersatz |
| Foerder-/Projektabhaengigkeit | Fruehe zahlende Pilot-/Kampagnen-Auftraege, wiederkehrende Abos aufbauen |
