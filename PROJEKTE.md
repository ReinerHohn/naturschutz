# Gruenderprojekte — Naturschutz mit 3D-Druck & Open Source

_Automatisch aus `projekte/*.json` erzeugt (`python3 build_projekte.py`)._

**11 Projekte.** Marktreife: **A** = vergleichbare Firmen existieren, **B** = Pilotmarkt, **C** = frueh. Keine Rechts-/Steuer-/Anlageberatung.

## 💰 Schnell & lohnend — bestes Verhaeltnis Ertrag / Aufwand / Marktreife

_Score = (Ertrag − 0,6·Aufwand) × Marktgewicht (A=1,0 · B=0,7 · C=0,4)._

| # | Projekt | Ertrag | Aufwand | Markt | MVP |
|---|---|:---:|:---:|:---:|---|
| 1 | **WildAuge - KI-Auswertedienst fuer Kamerafallen** (`kamerafallen-auswertedienst`) | 4/5 | 2/5 | A | 6-10 Wochen (MegaDetector-Pipeline plus Upload-Portal plus PDF-Report) |
| 2 | **PrioritaetsPlaner - Open-Source-GIS-Beratung fuer wirksamen Naturschutz pro Euro** (`prioritaetsplaner-beratung`) | 4/5 | 2/5 | A | 1-2 Monate (QGIS/prioritizr-Workflow + ein Referenz-Datensatz + Angebotsvorlage) |
| 3 | **KitzRetter - Drohnen-Kitzrettung plus offene Halterungen** (`kitzretter-service`) | 3/5 | 2/5 | A | 4-8 Wochen (Waermebild-Drohne plus KI-Kitz-Erkennung plus Einsatz-/Routen-App) |
| 4 | **FlaechenMonitor - Fernerkundungs-SaaS fuer Umwelt- und Agraraemter** (`flaechenmonitor-fernerkundung`) | 4/5 | 3/5 | B | 3-4 Monate (Sentinel-2-Zeitreihe plus Mahd-Detektion plus Karten-Dashboard fuer eine Pilotflaeche) |
| 5 | **InsektenScanner - automatische Insekten-Monitoringstationen** (`insektenscanner-monitoring`) | 4/5 | 3/5 | B | 3-5 Monate (Kamera plus UV-Lockflaeche plus Insect-Detect-KI plus Dashboard) |
| 6 | **Lauschposten - Bioakustik-Monitoring as a Service** (`lauschposten-bioakustik`) | 4/5 | 3/5 | B | 2-3 Monate (AudioMoth + BirdNET-Pi + einfaches Report-PDF) |
| 7 | **ArtenschutzModul - 3D-gedruckte Nistquartiere fuer Sanierung und Neubau** (`artenschutz-module-bau`) | 4/5 | 3/5 | B | 3-5 Monate (2-3 freilandgetestete Modultypen + Einbau-Datenblatt + Nachweis-Vorlage) |
| 8 | **NaturBuero-KI - KI-Assistent fuer Naturschutz-Verwaltung und Ehrenamt** (`naturbuero-ki`) | 4/5 | 3/5 | B | 3-4 Monate (ein Antrags-/Berichts-Workflow fuer EINE Foerderlinie, mit Quellen-Beleg und Export) |
| 9 | **NaturDruck - offener 3D-Druck-Baukasten fuer den kommunalen Naturschutz** (`naturdruck-baukasten-fablab`) | 3/5 | 2/5 | B | 2-3 Monate (3-4 validierte Druckvorlagen + ein Starter-Set + eine Workshop-Vorlage) |
| 10 | **BuergerNatur - White-Label-Plattform fuer kommunale Citizen Science** (`buergernatur-plattform`) | 3/5 | 3/5 | B | 3-5 Monate (gebrandetes Web-Portal + PWA/App auf iNaturalist-/GBIF-Standards, eine Kampagne, Export) |


## Monitoring-SaaS & Service

### FlaechenMonitor - Fernerkundungs-SaaS fuer Umwelt- und Agraraemter

Markt **B** · Ertrag 4/5 · Aufwand 3/5 · MVP 3-4 Monate (Sentinel-2-Zeitreihe plus Mahd-Detektion plus Karten-Dashboard fuer eine Pilotflaeche) · `flaechenmonitor-fernerkundung`

**Fernerkundungs-SaaS auf Basis kostenloser Sentinel/Copernicus-Daten plus KI, die Umwelt- und Landwirtschaftsaemtern Mahd-Zeitpunkte, Moor-/Gruenland-Zustand und Landnutzungsaenderungen flaechendeckend und ohne Vor-Ort-Begehung nachweist.**

_Problem:_ Behoerden muessen Flaechen-Auflagen flaechendeckend kontrollieren - frueher per teurer, stichprobenhafter Vor-Ort-Begehung. Starker regulatorischer Treiber: Seit 1.1.2023 ist das Flaechenmonitoring (Area Monitoring System, AMS) in der EU-Agrarfoerderung Pflicht - alle Antragsflaechen muessen regelmaessig per Sentinel-Satellit auf Aktivitaeten wie Mahd oder Beweidung geprueft werden. Hinzu kommen Nachweise fuer Agrarumwelt- und Klimamassnahmen (z.B. spaete Mahd zum Wiesenbrueter-Schutz), Moor-Wiedervernaessungs-Monitoring, FFH-Gruenland-Erhaltungszustand und das EU-Renaturierungsgesetz (Zustands-Berichtspflichten). Rohdaten (Sentinel-1/2) sind gratis, aber Aemtern fehlen Pipeline, KI und Fachpersonal, um daraus pruefbare Aussagen zu machen.

_Loesung:_ Eine SaaS-Plattform, die freie Sentinel-1 (Radar, wolkenunabhaengig) und Sentinel-2 (optisch) Zeitreihen automatisch auswertet: KI erkennt Mahd-/Beweidungs-Ereignisse und deren Zeitpunkt, verfolgt Vegetationsindizes (NDVI/NDWI) fuer Gruenland- und Moor-Zustand und meldet Landnutzungs- und Versiegelungsaenderungen. Ausgabe: parzellenscharfe Ampel-Karten, Ereignis-Logs und Report pro Flaeche fuer die Akte. Die Auswerte-Pipeline (Datenzugriff ueber offene Copernicus-Dienste, KI-Modelle, QGIS-Export) ist Open Source und als QGIS-Plugin plus Web-Dashboard nutzbar; 3D-Druck spielt hier eine Nebenrolle (optional guenstige Boden-Referenzstationen/Kamera-Pegel zur KI-Validierung). Verkauft wird der betriebene Dienst, nicht die Software.

**Zugang zur oeffentlichen Hand**

- Landwirtschaftsaemter/Landesverwaltungen, die das EU-AMS umsetzen und Agrarumweltmassnahmen pruefen muessen - Rahmenvertrag oder Ausschreibung (groessere Volumina).
- Untere Naturschutzbehoerden (Landkreise) fuer Mahd-Kontrolle in Schutzgebieten und Vertragsnaturschutz - Direktauftrag unter Vergabeschwelle.
- Landesumweltaemter und Moorschutz-Programme fuer Vernaessungs- und Gruenland-Zustands-Monitoring.
- Nationalpark-/Biosphaeren-Verwaltungen fuer grossflaechiges Landnutzungs-Monitoring.
- Kommunen fuer Flaechenverbrauch-/Versiegelungs-Monitoring (Smart Region, Innenentwicklung).
- Als Nachauftragnehmer/Datenlieferant fuer GIS-Dienstleister und Planungsbueros, die keine eigene Fernerkundung haben.

**Open-Source-Hebel:** Copernicus-Daten sind bewusst frei und offen - eine offene Auswerte-Pipeline passt zur politischen Linie 'Public Money - Public Code' und zur digitalen Souveraenitaet, und sie macht Foerder-/Sanktions-Entscheidungen nachvollziehbar und rechtssicher (bei AMS-Entscheidungen haftungsrelevant). Kein Vendor-Lock-in erleichtert Vergabe und Datenuebergabe zwischen Behoerden; ein offenes QGIS-Plugin senkt die Einstiegshuerde. Geld kommt aus dem betriebenen Dienst, gepruefen Reports, Integration/Support und dem Rechen-/Daten-Betrieb - nicht aus Lizenzgebuehren.

**3D-Druck-Hebel:** 3D-Druck ist hier bewusst nur Nebensache: optional guenstige, 3D-gedruckte Boden-Referenz- und Validierungsstationen (Wildkamera-/Sensor-Gehaeuse, Phaenologie-Kameras an Pegeln), um die Satelliten-KI vor Ort zu kalibrieren und Mahd-Ereignisse ground-truth-fest zu belegen. Stueckkosten wenige Euro, lokal und reparierbar produzierbar; Fertigung an eine Inklusions-/Behindertenwerkstatt vergebbar. Das Kerngeschaeft ist jedoch Software/Service.

**Geschaeftsmodell:** B2G-SaaS plus Service mit offenem Kern: freie Satellitendaten plus offene Pipeline schaffen Vertrauen, Vergabefaehigkeit und Rechtssicherheit; Umsatz kommt aus dem betriebenen Monitoring-Abo (pro Flaeche/Behoerde), aus gepruefen Reports und aus Integration in die Fachverfahren. Open-Core: das Basis-Plugin ist offen, der skalierbare Cloud-Betrieb, die Fach-QS und die Behoerden-Integration sind die bezahlte Leistung.

**Einnahmequellen**

- SaaS-Abo nach Flaeche (EUR pro Hektar und Jahr) oder pro Behoerde/Pauschale.
- Projekt-/Werkauswertung je Kampagne (z.B. eine Mahd-Saison, eine Moor-Flaeche).
- Integration/Beratung: Einbindung in bestehende Fachverfahren und GIS der Behoerde.
- Report- und Gutachten-Zuschlag (gepruefte, rechtssichere Auswertung).
- Schulung/Support und Lizenz-Support fuer das offene QGIS-Plugin.
- Foerder-/Forschungsprojekte als Entwicklungsfinanzierung.

| Preis / Kennzahl | Wert |
|---|---|
| SaaS pro Flaeche | ca. 0,20-1,50 EUR pro Hektar und Jahr (degressiv mit Flaeche) |
| Behoerden-Pauschale | ca. 5.000-20.000 EUR/Jahr je nach Gebietsgroesse und Modulen |
| Einzel-Kampagne | ca. 3.000-8.000 EUR (eine Saison, definierte Kulisse, Report) |
| Integration/Beratung | ca. 700-1.100 EUR/Tag |
| Vergleich Vor-Ort-Begehung | oft hohe Kosten je Stichprobe plus nur Teilabdeckung statt flaechendeckend |

**Kosten & Break-even:** Fixkosten: Cloud-Rechenzeit fuer Sentinel-Zeitreihen und Entwicklung; variable Kosten pro Flaeche gering (Rohdaten gratis). Skaliert stark, weil zusaetzliche Flaechen fast nichts kosten. Break-even realistisch bei einem mittleren Landkreis-/Landes-Rahmenvertrag plus einigen Einzelkampagnen (grob 40-80 TEUR wiederkehrend) als kleines Team. Ein einziger AMS-naher oder Agrarumwelt-Auftrag kann die Entwicklung tragen. Groesstes Risiko: etablierte Grossanbieter und lange Behoerden-Beschaffung.

**Passende Foerderung**

- EU LIFE sowie Copernicus-/EU-Erdbeobachtungs-Foerderungen (auch ueber ESA-BIC-Inkubatoren).
- Bundesprogramm Biologische Vielfalt (BfN) und DBU fuer Monitoring-Innovation (Moor/Gruenland).
- Prototype Fund fuer das offene QGIS-Plugin / die Auswerte-Pipeline.
- Smart-City/Smart-Region-Mittel und Landes-Digitalisierungsprogramme der Agrar-/Umweltressorts.
- EXIST-Gruenderstipendium; KfW-Gruenderkredite fuer die Skalierung.

**Vorbilder:** LiveEO (Satelliten-Monitoring-SaaS fuer Infrastruktur/Vegetation, Berlin), OHB / OHB Digital (Erdbeobachtung und Geodatendienste), Constellr (Satelliten-Thermaldaten fuer Landwirtschaft/Wasser), CloudFerro / NEO (AMS-as-a-Service und agrarisches Satellitenmonitoring fuer Behoerden), kleine/mittlere GIS- und Fernerkundungs-Dienstleister (z.B. EFTAS, GAF) als Markt- und Behoerden-Beleg

**Naechste Schritte (90 Tage)**

- MVP bauen: Sentinel-2-Zeitreihe plus Mahd-Detektion plus parzellenscharfes Karten-Dashboard fuer eine Pilotkulisse.
- Sentinel-1-Radar ergaenzen (wolkenunabhaengig) fuer zuverlaessige Mahd-/Beweidungs-Erkennung.
- EINEN Pilotkunden gewinnen (untere Naturschutzbehoerde oder Agrarumwelt-Stelle), moeglichst gefoerdert; Ground-Truth mit 3D-Referenzstationen validieren.
- Report-/Ausgabeformat mit der Behoerde auf Rechts- und Akten-Tauglichkeit abstimmen (AMS-/Agrarumwelt-konform).
- Open-Source-QGIS-Plugin plus Doku veroeffentlichen (Vertrauen, Prototype-Fund-faehig).
- Fallstudie erstellen und auf Landkreis-/Landes-Rahmenvertraege sowie AMS-nahe Ausschreibungen zielen.

> ⚠️ **Risiken:** Starker Wettbewerb durch etablierte, kapitalstarke EO-Anbieter und Behoerden-Platzhirsche (EFTAS, GAF, GovTech-Konsortien) - Nische ueber Naturschutz-/Moor-/Vertragsnaturschutz-Fokus und offene, guenstige Pipeline suchen. Sentinel-Aufloesung (10 m) begrenzt kleinteilige Flaechen; Wolken bei rein optischer Auswertung (Radar ergaenzen). AMS-Entscheidungen sind haftungs-/rechtsrelevant - Genauigkeit, Ground-Truth und Dokumentation sind Pflicht. Behoerden-Beschaffung ist langwierig und oft an bestehende Fachverfahren gebunden.

**Quellen:** [Area Monitoring System (AMS) - TOOLS4CAP Briefing](https://www.tools4cap.eu/wp-content/uploads/2024/11/BR3-Area-Monitoring-System.pdf) · [Copernicus-Datenzugang in Deutschland](https://netzwerk-wald.d-copernicus.de/datenzugang/) · [Thuenen-Institut - automatische Erkennung von Agrarstrukturen (Fernerkundung)](https://www.thuenen.de/de/institutsuebergreifende-projekte/ich-sehe-was-was-du-nicht-siehst-automatische-erkennung-von-agrar-und-anbaustrukturen-mittels-satellitenbildern-fernerkundung/) · [Flaechenmonitoring Landwirtschaft Sachsen](https://www.landwirtschaft.sachsen.de/flaechenmonitoring-56898.html) · [Area Monitoring System as a Service (CloudFerro)](https://cloudferro.com/data-tools/area-monitoring-system-as-a-service/) · [LiveEO](https://www.live-eo.com/)

---

### InsektenScanner - automatische Insekten-Monitoringstationen

Markt **B** · Ertrag 4/5 · Aufwand 3/5 · MVP 3-5 Monate (Kamera plus UV-Lockflaeche plus Insect-Detect-KI plus Dashboard) · `insektenscanner-monitoring`

**Solarbetriebene, non-letale Insekten-Monitoringstation (Kamera plus KI, offenes Diopsis-/Insect-Detect-Prinzip) im 3D-gedruckten Gehaeuse, die Behoerden und Schutzgebieten das kommende EU-weite Insekten-/Bestaeuber-Monitoring automatisiert und standardisiert liefert.**

_Problem:_ Der Insektenschwund ist politisch anerkannt und loest Monitoring-Pflichten aus. Mit dem EU-Renaturierungsgesetz und dem im Aufbau befindlichen EU Pollinator Monitoring Scheme (EU PoMS, vorbereitet durch die EU-Projekte SPRING/STING) muessen die Mitgliedstaaten kuenftig flaechendeckend Bestaeuber (Wildbienen, Schmetterlinge, Schwebfliegen, Nachtfalter) erfassen und Trends berichten. Klassisches Insektenmonitoring (Malaise-Fallen, Handfang, mikroskopische Bestimmung) ist extrem arbeitsintensiv, toetet die Tiere und scheitert am Taxonomen-Mangel. Es fehlt eine guenstige, non-letale, standardisierte und automatisierbare Methode mit grossem Datendurchsatz.

_Loesung:_ Eine autonome Station nach offenem Vorbild (Diopsis-Kamera / UKCEH AMI-System / Insect Detect): eine UV-beleuchtete Lockflaeche, auf der eine Kamera anfliegende Insekten tags und nachts fotografiert; eine KI (offene Modelle, z.B. Insect Detect auf Basis von YOLO) erkennt, zaehlt und klassifiziert die Tiere nach Gruppen. Die Tiere werden nicht getoetet. Daten laufen in ein Dashboard mit Abundanz-Zeitreihen, Diversitaets-Indizes und Report. Hardware-Design (inkl. 3D-gedrucktem Gehaeuse) und KI-Pipeline sind Open Source; verkauft werden fertige Stationen, der Betrieb und die Auswertung. Insect Detect ist bereits als offene DIY-Loesung publiziert und dient als technische Basis.

**Zugang zur oeffentlichen Hand**

- Landesumweltaemter/Landesanstalten, die das EU PoMS national umsetzen muessen - Rahmenvertrag ueber Stationsnetze.
- Untere Naturschutzbehoerden (Landkreise) fuer lokale Bestaeuber-/Bluehflaechen-Erfolgskontrolle - Direktauftrag unter Vergabeschwelle.
- Nationalpark-, Biosphaeren- und Naturpark-Verwaltungen fuer Langzeit-Insektenmonitoring.
- Kommunen fuer Erfolgskontrolle eigener Bluehflaechen/Gruenanlagen (Smart-City-Umweltmonitoring).
- Universitaeten, Senckenberg/Thuenen und Monitoring-Konsortien als Technik-/Datenpartner und Referenzgeber.
- Einstieg ueber ein gefoerdertes Reallabor mit einem Land oder Nationalpark, Ergebnis als Referenz fuer die EU-PoMS-Ausschreibungen.

**Open-Source-Hebel:** Offene Hardware und offene KI sichern genau das, was staatliches Monitoring braucht: Standardisierung, Vergleichbarkeit und Nachvollziehbarkeit ueber Jahrzehnte (kein Lock-in an einen Hersteller, dessen Blackbox-Modell die Zeitreihe entwertet). 'Public Money - Public Code' und digitale Souveraenitaet sind politisch gewollt; offene Methodik macht die Daten wissenschaftlich und berichtssicher. Verdient wird an Hardware, Betrieb, Kalibrierung und gepruefter Auswertung, nicht an einer Lizenz (Open-Core / Hardware+Service).

**3D-Druck-Hebel:** 3D-gedruckt werden das wetterfeste Stations-Gehaeuse, Kamera-/UV-Lampen-Halter, die Lockflaechen-Rahmen, Regen-/Sonnenblenden und Mast-Adapter (ASA/PETG, UV-fest). Stueckkosten wenige Euro statt teurer Spezial-Gehaeuse; on-demand, lokal und reparierbar/nachruestbar, was ueber viele Standorte einen echten Kostenhebel ergibt. Serienfertigung der Gehaeuse laesst sich an eine Inklusions-/Behindertenwerkstatt vergeben (sozialer Vergabe-Bonus).

**Geschaeftsmodell:** Open-Core plus Hardware & Service mit stark regulatorischem Rueckenwind: offene, standardisierte Station (Vertrauen, Vergleichbarkeit, Vergabefaehigkeit), Geld aus Hardware-Verkauf, jaehrlicher SaaS-/Wartungsgebuehr pro Station und gepruefter Auswertung. Die Monetarisierung folgt dem Ausbau des EU PoMS - wer frueh standardkonforme, offene Technik liefert, wird zum Infrastruktur-Lieferanten eines wachsenden Pflicht-Marktes.

**Einnahmequellen**

- Hardware-Verkauf fertiger, kalibrierter Monitoringstationen.
- SaaS/Auswertung: Jahresgebuehr pro Station fuer Cloud-KI, Dashboard und Report.
- Betrieb/Wartung: Aufbau, saisonale Wartung, Reinigung der Lockflaeche, Kalibrierung.
- Fach-Validierung und taxonomische Einordnung von Zweifelsfaellen.
- Foerder-/Forschungsprojekte als Entwicklungs- und Pilotfinanzierung.
- Schulung/Support fuer Behoerden/Institute, die selbst betreiben wollen.

| Preis / Kennzahl | Wert |
|---|---|
| Station (Hardware, Verkauf) | ca. 1.200-2.500 EUR/Stueck (Material/Kamera/Solar ~400-700 EUR) |
| SaaS-Auswertung | ca. 600-1.200 EUR pro Station und Jahr |
| Betrieb/Wartung pro Station | ca. 300-600 EUR/Saison |
| Pilot-Netz Behoerde | ca. 20.000-40.000 EUR (10-20 Stationen plus Auswertung, 1 Saison) |
| Vergleich klassisches Insektenmonitoring | oft 500-1.500 EUR je Malaise-Standort plus hohe Bestimmungskosten |

**Kosten & Break-even:** Hoehere Stueckkosten als eine Audio-Box (Kamera, UV, Solar, Rechenmodul), dafuer hoeherer Preis. Fixkosten moderat (Cloud-Inferenz, Dev-Zeit); variable Kosten pro Station ueberschaubar. Break-even realistisch bei ca. 30-50 aktiven Stationen im SaaS plus Wartung (ca. 40-80 TEUR wiederkehrend). Der grosse Hebel ist das anlaufende EU PoMS: ein einziger Landes-Rahmenvertrag kann die Skalierung tragen. Groesstes Risiko ist das Timing der EU-Umsetzung.

**Passende Foerderung**

- Bundesprogramm Biologische Vielfalt (BfN) - Insekten-/Bestaeuber-Monitoring ist thematischer Schwerpunkt.
- EU LIFE sowie EU-Mittel im Umfeld von SPRING/STING und dem EU Pollinator Monitoring Scheme.
- DBU (Deutsche Bundesstiftung Umwelt) - Umwelttechnik/Digitalisierung.
- Prototype Fund fuer die offene KI-/Hardware-Pipeline; Deutsche Postcode Lotterie fuer Biodiversitaets-Projekte.
- EXIST-Gruenderstipendium; Landesprogramme Insektenschutz (z.B. Insektenschutz-Aktionsprogramme der Laender).

**Vorbilder:** DIOPSIS (kommerzielle smarte Insektenkamera, Niederlande) als naechster kommerzieller Vergleich, UKCEH AMI-System (automated monitoring of insects) als Referenzsystem, Insect Detect (offene DIY-Kamera-KI, publiziert) als offene technische Basis, Faunaphotonics, Wilder Sensing (KI-Insekten-/Biodiversitaets-Monitoring als Firma), Open Acoustic Devices / AudioMoth (offene Monitoring-Hardware als Geschaeftsbeleg)

**Naechste Schritte (90 Tage)**

- MVP bauen: Kamera plus UV-Lockflaeche plus Insect-Detect-KI im gedruckten Gehaeuse, Dashboard mit Abundanz-Zeitreihe.
- Methodik an die im EU PoMS/SPRING vorgeschlagenen Standards anlehnen (Vergleichbarkeit als Verkaufsargument).
- EINEN Landes-Partner oder Nationalpark als gefoerdertes Reallabor gewinnen (Referenz vor Umsatz).
- Non-letalen Ansatz und Datenschutz (keine Personen) sauber dokumentieren; Report mit einer Fachbehoerde abstimmen.
- Open-Source-Repo plus Doku veroeffentlichen; 3D-Gehaeuse in Kleinserie testen und Stueckkosten belegen.
- Fallstudie erstellen und sich fuer die anstehenden EU-PoMS-Ausschreibungen/Rahmenvertraege positionieren.

> ⚠️ **Risiken:** Timing-Risiko: das EU PoMS ist noch im Aufbau - wenn verbindliche Umsetzung und Budgets sich verzoegern, bleibt der Pflicht-Markt klein (daher Marktreife B/C). Automatische Artbestimmung ist bei vielen Insekten noch grob (eher Gruppen als Art) - ehrlich kommunizieren, Fach-Validierung einplanen. Hoehere Hardware-Komplexitaet als Audio-Boxen (Reinigung der Lockflaeche, Vandalismus, Energiebedarf nachts). Abhaengigkeit von Foerder-/EU-Geldern vermeiden, frueh echten Auftragsumsatz suchen.

**Quellen:** [SPRING - EU Pollinator Monitoring (UFZ)](https://www.ufz.de/spring-pollination/) · [Refined proposal for an EU Pollinator Monitoring Scheme (STING-2)](https://eugreenalliance.eu/wp-content/uploads/2025/03/STING-2-report-Refined-proposal-for-an-EU-pollinator-monitoring.pdf) · [Insect Detect - open-source DIY camera trap (Preprint)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10990185/) · [DIOPSIS - automated insect monitoring](https://diopsis.eu/) · [Bundesprogramm Biologische Vielfalt (BfN)](https://www.bfn.de/bundesprogramm-biologische-vielfalt) · [Prototype Fund](https://prototypefund.de/)

---

### Lauschposten - Bioakustik-Monitoring as a Service

Markt **B** · Ertrag 4/5 · Aufwand 3/5 · MVP 2-3 Monate (AudioMoth + BirdNET-Pi + einfaches Report-PDF) · `lauschposten-bioakustik`

**Solarbetriebene Lausch-Box (offene Hardware, 3D-gedrucktes Gehaeuse) plus Cloud-Auswertung mit BirdNET, die Kommunen und Behoerden ihr gesetzlich gefordertes Arten-Monitoring automatisiert und preiswert liefert.**

_Problem:_ Behoerden und Kommunen muessen Arten erfassen (FFH-Monitoring, Eingriffs-/Ausgleichs-Kontrolle nach BNatSchG, Umweltvertraeglichkeitspruefung, Vorher-Nachher bei Bau/Renaturierung). Klassische Gutachter-Begehungen sind teuer (schnell 5.000-50.000 EUR je Projekt), punktuell und schlecht wiederholbar. Fachkraeftemangel bei Kartierern verschaerft das. Es fehlt ein guenstiges, dauerhaftes, standardisiertes Monitoring.

_Loesung:_ Ein Netz aus robusten, solarbetriebenen Audio-Rekordern (Basis AudioMoth / offene Elektronik) im 3D-gedruckten, wetterfesten Gehaeuse. Die Aufnahmen laufen durch eine KI-Pipeline (BirdNET fuer Voegel, batdetect2 fuer Fledermaeuse) und landen in einem Dashboard mit automatischem Behoerden-Report (Artenliste, Aktivitaet, Zeitreihe, Karte). Hardware-Designs und Auswerte-Pipeline sind Open Source; verkauft werden fertige Boxen, der Betrieb und die pruefsichere Auswertung.

**Zugang zur oeffentlichen Hand**

- Untere Naturschutzbehoerden (Landkreise/kreisfreie Staedte) - Direktauftrag unterhalb der Vergabeschwelle moeglich (oft bis ca. 15.000 EUR formfrei/Verhandlungsvergabe).
- Kommunale Gruenflaechen-/Umweltaemter fuer Vorher-Nachher-Monitoring eigener Renaturierungen.
- Landesbetriebe Forst / Nationalpark-/Biosphaeren-Verwaltungen als Rahmenvertrag (mehrere Standorte).
- Einstieg ueber ein gefoerdertes Pilot-/Reallabor mit EINER Kommune, Ergebnis als Referenz fuer Ausschreibungen nutzen.
- Als Nachauftragnehmer von Planungsbueros/Gutachtern, die Dauer-Monitoring zukaufen statt selbst zu bauen.

**Open-Source-Hebel:** Open Source ist beim Staat ein Verkaufsargument, kein Hindernis: 'Public Money - Public Code' und digitale Souveraenitaet sind politisch gewollt, kein Vendor-Lock-in erleichtert die Vergabe, offene Methodik macht die Daten gerichtsfest/pruefbar. Geld kommt nicht aus der Software-Lizenz, sondern aus Hardware, Betrieb, gepruefter Auswertung und Support (Open-Core / Hardware+Service).

**3D-Druck-Hebel:** Das Gehaeuse, Halterungen und Solar-Mast-Adapter werden 3D-gedruckt (PETG/ASA, UV-fest): Stueckkosten wenige Euro statt teurer Spezialgehaeuse, lokal und on-demand produzierbar, einfach reparierbar/nachrüstbar. Produktion laesst sich an eine Inklusions-/Behindertenwerkstatt auslagern (sozialer Vergabe-Bonus, planbare Kosten).

**Geschaeftsmodell:** Open-Core + Hardware & Service: Die Designs und die Analyse-Pipeline sind offen (schafft Vertrauen und Vergabefaehigkeit), verkauft wird das Gesamtpaket aus fertiger Hardware, wartungsarmem Betrieb und pruefsicherer, gutachterlich verwertbarer Auswertung. Wiederkehrender Umsatz kommt aus der jaehrlichen SaaS-/Wartungsgebuehr pro Box.

**Einnahmequellen**

- Hardware-Verkauf: fertige, kalibrierte Boxen (Marge auf Material + Montage).
- SaaS/Auswertung: jaehrliche Gebuehr pro Box fuer Cloud-Analyse + Behoerden-Report.
- Dienstleistung: Aufbau, Wartung, jaehrliche Kalibrierung, gutachterliche Einordnung.
- Foerderprojekte als Entwicklungs-/Pilotfinanzierung.
- Schulung/Lizenz-Support fuer Behoerden/Bueros, die selbst betreiben wollen.

| Preis / Kennzahl | Wert |
|---|---|
| Box (Hardware, Verkauf) | ca. 350-600 EUR/Stueck (Material ~120-180 EUR) |
| SaaS-Auswertung | ca. 300-600 EUR pro Box und Jahr |
| Pilotprojekt Kommune | ca. 8.000-15.000 EUR (5-10 Boxen + Report, 1 Saison) |
| Vergleich Gutachten klassisch | oft 5.000-50.000 EUR, einmalig/punktuell |

**Kosten & Break-even:** Geringe Fixkosten (Cloud/Server, Dev-Zeit); variable Kosten je Box klein. Break-even realistisch bei ca. 30-60 aktiven Boxen im SaaS (ca. 15-30 TEUR ARR) als Soloselbststaendiger; der erste Pilotauftrag deckt die MVP-Entwicklung. Grootes Risiko ist Vertriebszeit, nicht Herstellkosten.

**Passende Foerderung**

- Prototype Fund (BMBF/Open Knowledge Foundation) fuer die Open-Source-Pipeline.
- DBU (Deutsche Bundesstiftung Umwelt) - Umwelttechnik/Digitalisierung.
- Bundesprogramm Biologische Vielfalt (BfN) - innovative Monitoring-Ansaetze.
- EXIST-Gruenderstipendium fuer die Gruendungsphase.
- Kommunale Mittel / Foerderung Smart City / Smart Region fuer den Pilot.

**Vorbilder:** Chirrup / Carbon Rewild (akustisches Biodiversitaets-Monitoring als Service, UK), Wilder Sensing, Sound of Norway, Faunaphotonics (KI-Biodiversitaets-Monitoring), Open Acoustic Devices / AudioMoth (offene Hardware als Marktbeleg), Wildlife Insights / Trapper (KI-gestuetzte Auswertung als Dienst)

**Naechste Schritte (90 Tage)**

- MVP bauen: AudioMoth + BirdNET-Pi im gedruckten Gehaeuse, ein PDF-Report automatisieren.
- EINE Kommune/Naturschutzbehoerde als Pilot gewinnen (Referenz > Umsatz), moeglichst gefoerdert.
- Report-Vorlage mit einer unteren Naturschutzbehoerde abstimmen, damit sie behoerdentauglich ist.
- Open-Source-Repo + Doku veroeffentlichen (Vertrauensaufbau, Prototype-Fund-faehig).
- Preisliste + 1-Seiten-Angebot fuer Direktauftrag unter Vergabeschwelle erstellen.
- Aus dem Pilot eine Fallstudie machen und an 20 weitere Landkreise ausrollen.

> ⚠️ **Risiken:** Behoerden-Vertriebszyklen sind lang und budgetgebunden; KI-Artbestimmung hat Fehlerraten (Haftung/Gerichtsfestigkeit absichern, Stichproben-Validierung durch Fachperson). Datenschutz/Mitschnitt menschlicher Stimmen technisch ausschliessen. Abhaengigkeit von Foerdermitteln vermeiden - frueh echten Auftragsumsatz suchen.

**Quellen:** [Open Acoustic Devices - AudioMoth](https://www.openacousticdevices.info/) · [BirdNET (Cornell Lab / TU Chemnitz)](https://birdnet.cornell.edu/) · [Prototype Fund](https://prototypefund.de/) · [DBU Foerderung](https://www.dbu.de/foerderung/) · [Bundesprogramm Biologische Vielfalt (BfN)](https://www.bfn.de/bundesprogramm-biologische-vielfalt)

---

### WildAuge - KI-Auswertedienst fuer Kamerafallen

Markt **A** · Ertrag 4/5 · Aufwand 2/5 · MVP 6-10 Wochen (MegaDetector-Pipeline plus Upload-Portal plus PDF-Report) · `kamerafallen-auswertedienst`

**Cloud- und KI-Dienst (MegaDetector plus Artbestimmung), der Naturschutzbehoerden, Forst, Jagd und Gutachtern das manuelle Sichten zehntausender Kamerafallen-Fotos abnimmt und pruefbare Artenlisten liefert - inklusive 3D-gedruckter, robuster Kamera-Halterungen.**

_Problem:_ Kamerafallen (Fotofallen) sind in Monitoring, Wildmanagement und Gutachten Standard, erzeugen aber riesige Bildmengen: eine Kamera liefert in einer Saison leicht 10.000-50.000 Bilder, davon oft 60-80 Prozent Leer- oder Fehlausloesungen (Wind, Gras). Das Sichten bindet tagelang Fachpersonal, das es wegen Kartierer-Mangel kaum gibt. Regulatorischer Treiber: Wolfs- und Luchs-Monitoring nach FFH-Richtlinie, Nachweis invasiver Arten (Waschbaer, Marderhund, Nutria), Erfolgskontrolle von Ausgleichsmassnahmen nach BNatSchG und Wildbestandserfassung fuer Abschussplanung. Vorhandene offene KI (MegaDetector) ist stark, aber Behoerden und kleine Bueros haben weder Server noch das Know-how, sie produktiv und pruefsicher zu betreiben.

_Loesung:_ Ein schlanker Dienst: Kunde laedt Bilder (SD-Karte, Upload oder Postversand) hoch; die Pipeline aus dem offenen MegaDetector V6 (Tier/Mensch/Fahrzeug-Trennung, filtert Leerbilder weg) plus nachgeschalteter Artbestimmung sortiert, zaehlt und erstellt einen behoerdentauglichen Report (Artenliste, Aktivitaetsmuster, Fundkarte, Beleg-Thumbnails). Mensch-Treffer werden zum Datenschutz automatisch unkenntlich gemacht. Die gesamte Auswerte-Pipeline ist Open Source (MegaDetector ist MIT-lizenziert); zusaetzlich gibt es 3D-gedruckte, vandalismusarme Kamera-Gehaeuse, Baum- und Pfahl-Halterungen sowie Sicht-Blenden gegen Fehlausloesung. Verkauft wird die gepruefte Auswertung je Bildpaket plus optional Hardware.

**Zugang zur oeffentlichen Hand**

- Untere Naturschutz- und Jagdbehoerden (Landkreise) - Direktauftrag unterhalb der Vergabeschwelle (vielerorts bis ca. 15.000 EUR formfrei oder Verhandlungsvergabe ohne Teilnahmewettbewerb).
- Landesforstbetriebe und Landesanstalten fuer Wald/Jagd - Rahmenvertrag ueber mehrere Reviere/Saisons.
- Nationalpark-, Biosphaeren- und Naturpark-Verwaltungen fuer laufendes Wildtier-Monitoring (Wolf/Luchs/Wildkatze).
- Landesumweltaemter beim Monitoring invasiver Arten (EU-Verordnung 1143/2014 Frueherkennung).
- Als Nachauftragnehmer von Planungs-/Gutachterbueros, die Bildmassen zukaufen statt selbst auswerten.
- Einstieg ueber ein gefoerdertes Pilot mit EINER Behoerde oder einem Nationalpark, Ergebnis als Referenz fuer Ausschreibungen.

**Open-Source-Hebel:** MegaDetector ist offen und MIT-lizenziert und laeuft bereits in ueber 80 Naturschutzprogrammen weltweit - das macht die Methode nachvollziehbar, pruefbar und damit gerichts- und behoerdenfest. 'Public Money - Public Code' und digitale Souveraenitaet sprechen fuer offene Verfahren; kein Vendor-Lock-in erleichtert die Vergabe und baut Vertrauen auf. Verdient wird nicht an der Software, sondern am Betrieb der Pipeline, an der gepruefen Auswertung mit Fach-Qualitaetssicherung und am Report (Hardware plus Service).

**3D-Druck-Hebel:** 3D-gedruckt werden wetterfeste Kamera-Gehaeuse (ASA/PETG, UV-fest), diebstahlhemmende Baum- und Pfahl-Halterungen, Neigungs-Adapter und Sicht-Blenden gegen Fehlausloesungen durch Vegetation. Stueckkosten wenige Euro Material statt teurer Metall-Security-Boxen (30-80 EUR im Handel). On-demand und lokal reparierbar; die Fertigung laesst sich an eine Inklusions-/Behindertenwerkstatt vergeben (sozialer Vergabe-Bonus, planbare Kosten).

**Geschaeftsmodell:** B2G-Dienstleistung plus Open-Core/Hardware+Service: Die KI-Pipeline ist offen (Vertrauen, Vergabefaehigkeit, Gerichtsfestigkeit), bezahlt wird fuer die betriebene, gepruefte Auswertung je Bildmenge sowie wiederkehrend ueber Jahres-Abos. Zusatzumsatz aus 3D-Hardware und Fach-Validierung. Skaliert gut, weil die marginalen Kosten pro Bild nach KI-Automatisierung sehr klein sind.

**Einnahmequellen**

- Auswertung je Bildpaket (Stueckpreis pro 1.000 Bilder oder pro Kamera-Saison).
- SaaS-Abo fuer Behoerden mit vielen Kameras (feste Jahresgebuehr, Portal-Zugang, unbegrenzte Uploads).
- Hardware-Verkauf: 3D-gedruckte Gehaeuse und Halterungen plus optional vorkonfigurierte Kameras.
- Fach-Qualitaetssicherung und gutachterliche Einordnung (manuelle Validierung der KI-Treffer).
- Schulung/Support fuer Behoerden/Bueros, die die offene Pipeline selbst betreiben wollen.
- Foerderprojekte als Entwicklungs-/Pilotfinanzierung.

| Preis / Kennzahl | Wert |
|---|---|
| Auswertung pro 1.000 Bilder | ca. 15-40 EUR (KI-Sortierung plus Report-Anteil) |
| Kamera-Saison pauschal | ca. 120-250 EUR pro Kamera und Saison inkl. Report |
| SaaS-Abo Behoerde | ca. 2.000-6.000 EUR/Jahr fuer bis zu 20-50 Kameras |
| 3D-Gehaeuse plus Halterung | ca. 25-45 EUR/Set (Material ~5-10 EUR) |
| Fach-Validierung/Gutachten-Zuschlag | ca. 60-90 EUR/Stunde |

**Kosten & Break-even:** Sehr niedrige Fixkosten (Cloud-GPU nur bei Last zuschaltbar, Open-Source-Modell kostenlos, Portal schlank). Hauptaufwand ist Vertrieb und Fach-QS-Zeit. Als Soloselbststaendige/r ist Break-even realistisch bei ca. 10-20 Behoerden-/Buero-Kunden im Jahresabo oder dem Aequivalent von rund 1,5-3 Mio. ausgewerteten Bildern pro Jahr. Der erste Pilotauftrag deckt die MVP-Entwicklung. Groesstes Risiko ist die Vertriebszeit, nicht die Herstellkosten.

**Passende Foerderung**

- Prototype Fund (BMBF/Open Knowledge Foundation) fuer die offene Auswerte-Pipeline.
- DBU (Deutsche Bundesstiftung Umwelt) - Umwelttechnik/Digitalisierung.
- Bundesprogramm Biologische Vielfalt (BfN) - innovative Monitoring- und Arterfassungs-Ansaetze.
- EXIST-Gruenderstipendium fuer die Gruendungsphase.
- Kommunale/Landes-Mittel Smart Region sowie Mittel fuer Wolfs-/Invasive-Arten-Monitoring der Laender.

**Vorbilder:** Wildlife Insights (Google/WWF/Conservation International - KI-Kamerafallen-Plattform als Dienst, Behoerden/Firmen zahlen), Trapper (offene Kamerafallen-Datenplattform), TrapTagger / Wildeye Conservation (KI-gestuetzte Kamerafallen-Auswertung), Conservation AI (KI-Artbestimmung aus Kamerafallen als Service), MegaDetector / Microsoft AI for Good (offene Kamerafallen-KI als Marktbeleg und Grundtechnik)

**Naechste Schritte (90 Tage)**

- MVP bauen: MegaDetector-V6-Pipeline plus Upload-Portal plus automatischer PDF-Report mit Artenliste und Fundkarte.
- Mensch-Anonymisierung und Datenschutz-Workflow fest einbauen (DSGVO-sicher).
- EINE Behoerde/Nationalpark/Forstamt als Pilot gewinnen (Referenz vor Umsatz), moeglichst gefoerdert.
- Report-Vorlage mit einer unteren Naturschutzbehoerde abstimmen (behoerdentauglich, pruefbar).
- Open-Source-Repo plus Doku veroeffentlichen (Vertrauen, Prototype-Fund-faehig) und 3D-Gehaeuse-Set drucken/testen.
- Aus dem Pilot eine Fallstudie machen und an weitere Landkreise/Forstbetriebe als Direktauftrag ausrollen.

> ⚠️ **Risiken:** KI-Artbestimmung hat Fehlerraten (Verwechslungen bei aehnlichen Arten, schlechte Nachtbilder) - Haftung/Gerichtsfestigkeit ueber Stichproben-Validierung durch Fachperson absichern. Behoerden-Vertriebszyklen sind lang und budgetgebunden. Grosse Anbieter (Wildlife Insights) bieten teils Gratis-Stufen fuer Nicht-Kommerzielle - Abgrenzung ueber Behoerden-Tauglichkeit, Datenschutz, lokale Naehe und gepruefte Reports. Datenschutz bei Menschenfotos muss technisch wasserdicht sein.

**Quellen:** [MegaDetector (Microsoft AI for Good)](https://microsoft.github.io/MegaDetector/) · [Wildlife Insights](https://www.wildlifeinsights.org/) · [TrapTagger (Wildeye Conservation)](https://wildeyeconservation.org/traptagger/) · [Trapper - open camera trap platform](https://os-conservation.org/projects/trapper/) · [Prototype Fund](https://prototypefund.de/) · [Bundesprogramm Biologische Vielfalt (BfN)](https://www.bfn.de/bundesprogramm-biologische-vielfalt)

---

### KitzRetter - Drohnen-Kitzrettung plus offene Halterungen

Markt **A** · Ertrag 3/5 · Aufwand 2/5 · MVP 4-8 Wochen (Waermebild-Drohne plus KI-Kitz-Erkennung plus Einsatz-/Routen-App) · `kitzretter-service`

**Mobiler Drohnen-Service mit Waermebild und KI, der vor der Mahd Rehkitze findet und rettet, plus offene 3D-gedruckte Halterungen/Gehaeuse und App fuer Landwirte, Jagdgenossenschaften und Kommunen - auf einem bereits foerder- und nachfragestarken Markt.**

_Problem:_ Bei der ersten Grasmahd im Mai/Juni werden in Deutschland zehntausende Rehkitze vom Maehwerk getoetet, weil sie sich bei Gefahr ducken statt zu fliehen - ein erhebliches Tierschutz-Problem (toeten ist nach Tierschutzgesetz verboten; der Bewirtschafter ist in der Sorgfaltspflicht). Waermebild-Drohnen finden die Kitze zuverlaessig in den fruehen Morgenstunden. Der Markt ist real und gefoerdert: Bund/BLE foerdert Drohnen mit bis zu 60 Prozent, maximal 4.000 EUR pro Waermebild-Drohne; in den Vorjahren wurden fast 2.000 Drohnen gefoerdert, 2024 gab es ueber 640 Antraege und das Budget wurde von 1,5 auf ueber 2,5 Mio. EUR aufgestockt; rund 15.000 Kitze wurden 2024 gerettet. Viele Landwirte wollen aber keine eigene Drohne betreiben (Technik, Pilotenschein, Zeit im engen Mahd-Fenster) und kaufen die Rettung lieber als Dienstleistung ein.

_Loesung:_ Zweigleisig: (1) Ein mobiler Rettungs-Service - zertifizierte Piloten fliegen im Auftrag die Flaechen vor der Mahd mit Waermebild-Drohne ab, eine KI (offene Kitz-Erkennungsmodelle) markiert Hotspots, das Team sichert/vertreibt die Kitze. (2) Offene Hardware und Software fuer die vielen ehrenamtlichen Kitzretter-Gruppen und Vereine: 3D-gedruckte Drohnen-Halterungen, Kitz-Transportkisten-Deckel/Griffe, Markierungs-Kaestchen, Smartphone-/Tablet-Halter und eine offene Einsatz-App (Flaechen-Planung, GPS-Fundpunkte, Nachweis-Protokoll fuer Landwirt und Behoerde). KI-Erkennung und App sind Open Source; verdient wird am Service, an Hardware-Sets und an Schulung/Support.

**Zugang zur oeffentlichen Hand**

- Kommunen/Staedte fuer eigene Gruenland- und Ausgleichsflaechen sowie als Foerderer lokaler Kitzretter-Initiativen - Direktauftrag unter Vergabeschwelle.
- Jagdgenossenschaften und Hegegemeinschaften (koerperschaftlich organisiert) als Sammel-Auftraggeber fuer Reviere.
- Untere Jagd-/Naturschutzbehoerden und Landkreise fuer Koordination, Foerderabwicklung und Nachweisfuehrung.
- Landesanstalten/Landwirtschaftskammern als Multiplikator und fuer Schulungen (Rahmenvertrag Weiterbildung).
- Als Dienstleister fuer landwirtschaftliche Betriebe und Maschinenringe im Umfeld oeffentlicher Flaechen.
- Einstieg: mit einer Kommune oder Jagdgenossenschaft eine Saison als Referenz fahren, Foerderfaehigkeit (BLE) gleich mitnutzen.

**Open-Source-Hebel:** Offene Kitz-Erkennungs-KI und offene Einsatz-App senken die Huerde fuer die vielen ehrenamtlichen Gruppen und passen zur foerderpolitischen Logik (Tierschutz als oeffentliches Gut, 'Public Money - Public Code'). Offene Nachweis-Protokolle schaffen Vertrauen bei Landwirt, Jagd und Behoerde (Sorgfalts-Nachweis). Kein Lock-in erleichtert, dass Kommunen den Dienst beauftragen oder foerdern. Verdient wird am betriebenen Flugservice, an gedruckten Hardware-Sets und an Schulung/Support - nicht an einer App-Lizenz.

**3D-Druck-Hebel:** 3D-gedruckt werden Drohnen-Zubehoer und Feld-Ausruestung: Halterungen und Gimbal-/Schirm-Adapter, Kitz-Transportkisten-Griffe und -Deckel, luftige Abdeck-Koerbe zum voruebergehenden Sichern, Markierungsstaebe/Faehnchen-Halter, Tablet-Sonnenschutz und Ersatzteile. Stueckkosten wenige Euro, sofort nachdruckbar bei Feldschaeden im engen Saison-Fenster, lokal reparierbar. Serienfertigung der Sets fuer Vereine an eine Inklusions-/Behindertenwerkstatt vergebbar (sozialer Vergabe-Bonus).

**Geschaeftsmodell:** Hardware+Service plus Open-Core: Kerngeschaeft ist die bezahlte, zeitkritische Rettungs-Dienstleistung in der Mahd-Saison, ergaenzt um 3D-gedruckte Hardware-Sets, Schulung und Foerderberatung. Offene KI/App machen das Angebot glaubwuerdig und ehrenamts-tauglich und schaffen Reichweite/Leads; Umsatz kommt aus Flugeinsaetzen, Paketen und Hardware. Entscheidend ist, die teure Drohne ganzjaehrig (anderes Monitoring) auszulasten, um die Saisonabhaengigkeit abzufedern.

**Einnahmequellen**

- Flug-/Rettungs-Service je Einsatz (pro Hektar oder pro Flug/Vormittag).
- Saison-Pakete fuer Landwirte/Jagdgenossenschaften/Kommunen (feste Flaechen, mehrere Termine).
- Hardware-Sets: 3D-gedruckte Halterungen, Transportkisten-Teile, Markierungs-Kits.
- Schulung und Pilotenbegleitung fuer ehrenamtliche Kitzretter-Gruppen (A1/A3-Drohnenkompetenz, Praxis).
- Foerderabwicklungs-Hilfe (Antrag BLE/Land) als Beratungsleistung.
- Winter-/Nebensaison: Nutzung derselben Drohnen/KI fuer anderes Monitoring (Wild-Zaehlung, Thermographie).

| Preis / Kennzahl | Wert |
|---|---|
| Rettungs-Service pro Hektar | ca. 15-35 EUR/ha (Mindestpauschale pro Einsatz ca. 80-150 EUR) |
| Vormittags-Einsatz pauschal | ca. 250-500 EUR (mehrere nahe Flaechen in einem Zeitfenster) |
| Saison-Paket Jagdgenossenschaft/Kommune | ca. 1.500-5.000 EUR je nach Flaeche/Terminen |
| Hardware-Set (3D-Druck) | ca. 20-60 EUR je Set |
| Schulung Ehrenamts-Gruppe | ca. 300-600 EUR/Tag |
| Foerderhinweis | BLE-Foerderung bis 60 Prozent, max. 4.000 EUR je Waermebild-Drohne |

**Kosten & Break-even:** Hauptinvestition ist die Waermebild-Drohne (grob 4.000-12.000 EUR, stark foerderfaehig) plus Pilotenkompetenz/Versicherung. Variable Kosten je Einsatz gering (Zeit, Anfahrt). Weil der Dienst extrem saisonal ist (nur wenige Wochen im Mai/Juni, nur fruehmorgens), muss in diesem Fenster ausgelastet werden. Break-even realistisch, wenn pro Saison grob 200-400 ha oder mehrere Saison-Pakete gefahren werden; die Drohne refinanziert sich durch Winter-Nutzung (Monitoring) und Foerderung schneller. Groesstes Risiko ist nicht die Technik, sondern die enge Saison und das Wetter.

**Passende Foerderung**

- BLE-Bundesfoerderung Drohnen zur Rehkitzrettung (BMEL) - bis 60 Prozent, max. 4.000 EUR je Waermebild-Drohne.
- Ergaenzende Landes-/NRW-Foerderprogramme fuer Rehkitzrettungs-Drohnen.
- Deutsche Postcode Lotterie und regionale Stiftungen fuer Tierschutz-/Kitzretter-Vereine (Hardware-Sets).
- Kommunale Mittel/Tierschutz-Budgets fuer lokale Initiativen.
- Prototype Fund fuer die offene Erkennungs-KI/App; DBU fuer den Mehrfachnutzen-Monitoring-Ansatz.

**Vorbilder:** Zahlreiche gewerbliche Kitzrettungs-Dienstleister und Drohnen-Pilot-Betriebe in DE (Markt existiert, A), Rehkitzrettung-Vereine und der Dachverband/die Kitzretter-Community (Nachfrage- und App-Beleg), DJI / Autel Thermaldrohnen plus etablierte Waermebild-Workflows (Hardware-Oekosystem), Wildlife Drones / Drohnen-Monitoring-Dienstleister (Mehrfachnutzen der Flotte ausserhalb der Saison), BLE/BMEL-Foerderprogramm als Markt- und Nachfrage-Beleg (ueber 640 Antraege 2024, ~15.000 gerettete Kitze)

**Naechste Schritte (90 Tage)**

- Drohnen-Kompetenznachweis (A1/A3), Betriebserlaubnis und Haftpflicht/Versicherung klaeren und absichern.
- MVP: Waermebild-Drohne plus offene Kitz-Erkennungs-KI plus einfache Einsatz-/Nachweis-App aufsetzen.
- BLE-Foerderantrag fuer die Drohne stellen (bis 4.000 EUR) und die Foerderlogik fuer Kunden verstehen.
- EINE Jagdgenossenschaft/Kommune fuer eine Pilot-Saison gewinnen (Referenz plus Nachweis-Protokoll).
- 3D-Hardware-Sets und die App fuer ehrenamtliche Gruppen veroeffentlichen (Reichweite, Leads, Prototype-Fund).
- Winter-Mehrfachnutzen (Wildzaehlung/Thermographie) aufbauen, um die Saisonabhaengigkeit abzufedern; Fallstudie ausrollen.

> ⚠️ **Risiken:** Stark saisonal (wenige Wochen, nur fruehmorgens, wetterabhaengig) - ohne ganzjaehrige Zweitnutzung der Drohne ist das Geschaeft duenn; das ist ehrlich einzuplanen. Zeitkritische Logistik: viele Flaechen wollen im selben kurzen Fenster bedient werden. Rechtlicher Rahmen (EU-Drohnenrecht, Betriebsgenehmigung, Versicherung, Naturschutz-/Vogelschutz-Auflagen beim Flug) muss sauber sein. Preisdruck durch guenstige Ehrenamtler und viele Wettbewerber; Foerderung ist politisch und jaehrlich unsicher (das gruene BMEL hatte die Drohnenfoerderung zwischenzeitlich gestrichen). Haftung bei uebersehenem Kitz vertraglich klar begrenzen.

**Quellen:** [Bis zu 4.000 Euro Foerderung pro Drohne fuer die Rehkitzrettung (agrarheute)](https://www.agrarheute.com/management/finanzen/4000-euro-pro-drohne-fuer-rehkitzrettung-579074) · [Bund stockt Foerderung fuer Drohnen zur Rettung von Rehkitzen auf (agrarheute)](https://www.agrarheute.com/politik/bund-stockt-foerderung-fuer-drohnen-rettung-rehkitzen-634343) · [Drohnen-Foerderung fuer Rehkitzrettung 2024 (drohnen.de)](https://www.drohnen.de/49703/drohnen-foerderung-fuer-rehkitzrettung-2024/) · [BLE - Bundesanstalt fuer Landwirtschaft und Ernaehrung (Foerderstelle)](https://www.ble.de/) · [Prototype Fund](https://prototypefund.de/)

---


## Open Hardware & 3D-Druck

### ArtenschutzModul - 3D-gedruckte Nistquartiere fuer Sanierung und Neubau

Markt **B** · Ertrag 4/5 · Aufwand 3/5 · MVP 3-5 Monate (2-3 freilandgetestete Modultypen + Einbau-Datenblatt + Nachweis-Vorlage) · `artenschutz-module-bau`

**3D-gedruckte, einbaufertige Artenschutz-Module (Mauersegler-, Schwalben-, Sperlingsnester, Fledermausquartiere) fuer Sanierung und Neubau - mit Einbauberatung und CEF-Massnahmen-Nachweis, getrieben von der gesetzlichen Ersatzquartier-Pflicht nach Paragraf 44 BNatSchG.**

_Problem:_ Gebaeudebrueter (Mauersegler, Schwalben, Haussperling) und Fledermaeuse verlieren bei Sanierung und Daemmung ihre Brutplaetze. Nach Paragraf 44 BNatSchG sind Fortpflanzungs- und Ruhestaetten streng geschuetzt - werden sie beseitigt, verlangt die Naturschutzbehoerde funktionserhaltende Ersatzquartiere (CEF-Massnahmen) als Bedingung der Baugenehmigung. Bautraeger, kommunale Wohnungsbaugesellschaften, Architekten und Planungsbueros MUESSEN liefern, oft unter Zeitdruck. Etablierte Holzbeton-Quartiere (Schwegler, Strobel) sind bewaehrt, aber vergleichsweise teuer, schwer und wenig an die konkrete Fassade anpassbar; es fehlt eine guenstige, leichte, massgeschneiderte und dokumentierte Loesung inklusive Nachweis.

_Loesung:_ Ein Katalog 3D-gedruckter Artenschutz-Module, die als Einbaustein (Putz-/WDVS-integriert) oder Aufbau-Quartier in Fassaden kommen: Mauerseglernest (langer flacher Nistraum ca. 30 x 15 cm, querer Einflug ca. 30 x 65 mm seitlich unten), Mehl-/Rauchschwalben-Kunstnester mit Kotbrett, Sperlingskoloniekaesten und Fledermausquartiere mit engem, oben geschlossenem Spalt (15-20 mm) und rauer Innenflaeche fuer Krallenhalt. Druck aus UV-/hitzebestaendigem PETG oder ASA (helles/reflektierendes Material, Doppelwand/Belueftung gegen toedliche Ueberhitzung, Wandstaerke ab 3 mm). Dateien und Einbaudetails sind offen (CC-BY-SA, von Fachverband geprueft); verkauft werden die Module plus Einbauberatung und der prueffaehige CEF-/Artenschutz-Nachweis fuer die Behoerde. 3D-Druck macht die Quartiere leichter, guenstiger und an die jeweilige Fassade anpassbar.

**Zugang zur oeffentlichen Hand**

- Kommunale Wohnungsbaugesellschaften und staedtische Liegenschaftsaemter bei Sanierung eigener Bestaende - Direktauftrag unter Wertgrenze oder Verhandlungsvergabe (je nach Bundesland bis ca. 100.000 EUR), oft als Rahmenvertrag ueber mehrere Objekte.
- Untere Naturschutzbehoerden als Nachfrage-Treiber und Qualitaetssicherer (sie fordern und pruefen die CEF-Massnahmen) - hier Referenz und Akzeptanz aufbauen.
- Staedtische Bauaemter/Hochbauaemter fuer oeffentliche Gebaeude (Schulen, Verwaltung) mit Sanierungsstau.
- Verwendung kommunaler Ersatzzahlungen nach Paragraf 15 BNatSchG fuer artenschutzrechtliche Massnahmen am eigenen Bestand.
- Indirekt ueber private Bautraeger, Architekten und Planungsbueros, die die Pflichtmassnahme einkaufen - der groesste Markt neben dem oeffentlichen Bestand.

**Open-Source-Hebel:** Offene, fachlich gepruefte Einbaudetails schaffen Vertrauen bei Behoerde und Planer und machen die CEF-Massnahme leichter genehmigungsfaehig (nachvollziehbare Maße, keine Blackbox, kein Lock-in). Public Money Public Code und digitale Souveraenitaet erleichtern die Vergabe im oeffentlichen Bestand. Verdient wird nicht an der Datei, sondern am qualitaetsgesicherten Modul, an der fassadenspezifischen Anpassung, der Einbauberatung und am prueffaehigen Nachweis - genau das, was Bautraeger unter Zeitdruck brauchen (Open-Core + Dienstleistung).

**3D-Druck-Hebel:** Gedruckt werden Nistraeume, Einflugblenden, Fledermaus-Spaltquartiere und Einbaurahmen aus PETG/ASA (UV-/hitzefest, hell/reflektierend, Doppelwand oder Belueftungsschlitze gegen Ueberhitzung, raue Innenflaechen fuer Krallenhalt/Nistanheftung). Materialkosten pro Modul grob 5-20 EUR gegenueber 35-260 EUR fuer Holzbeton-Produkte; leichter als Holzbeton (einfacherer Einbau in WDVS), on-demand und an die Fassadentiefe anpassbar, reparierbar und als Serie reproduzierbar. Produktion lokal oder ueber eine Inklusionswerkstatt/FabLab - planbare Kosten und sozialer Vergabe-Bonus. WICHTIG: vor Serienstart ein Muster ein Jahr freilandtesten (Temperatur, Verformung, Annahme), sonst ist Kunststoff schlechter als Holzbeton.

**Geschaeftsmodell:** Open-Core Hardware + B2G/B2B-Dienstleistung: Die gepruefte Konstruktion ist offen (Vertrauen und Genehmigungsfaehigkeit), verkauft werden guenstige, leichte, fassadenspezifisch angepasste Module plus die eigentlich knappe Leistung - Einbauberatung und der prueffaehige CEF-Nachweis, den Bautraeger zwingend brauchen. Wiederkehrender Umsatz aus Rahmenvertraegen mit Wohnungsgesellschaften und Monitoring/Wartung. Der gesetzliche Zwang (Paragraf 44 BNatSchG) sichert die Nachfrage unabhaengig von Foerderung.

**Einnahmequellen**

- Verkauf der Module (Einbaustein und Aufbauquartier) an Bautraeger, Wohnungsgesellschaften und Private.
- Einbauberatung und fassadenspezifische Anpassung (Konstruktion nach konkreter Sanierung).
- CEF-/Artenschutz-Nachweis und Dokumentation fuer die Baugenehmigung (Honorar pro Objekt).
- Rahmenvertraege und Wartungs-/Monitoringpakete (Funktionskontrolle der Quartiere).
- Schulung fuer Architekten/Planungsbueros und Lizenz-/Supportpaket fuer Eigenproduktion.

| Preis / Kennzahl | Wert |
|---|---|
| Mauersegler-Einbaustein (gedruckt) | ca. 25-60 EUR/Stueck (Material ~5-15 EUR; Holzbeton-Vergleich ~35-100 EUR) |
| Fledermaus-Spaltquartier (gedruckt) | ca. 20-50 EUR/Stueck |
| Mauersegler-Mehrfachsystem (gedruckt, 2-3 Nistraeume) | ca. 60-140 EUR (Holzbeton-Vergleich 190-260 EUR) |
| Einbauberatung + fassadenspezifische Anpassung | ca. 500-2.500 EUR je Objekt |
| CEF-Nachweis/Dokumentation | ca. 800-3.500 EUR je Objekt (je nach Umfang) |
| Rahmenvertrag Wohnungsgesellschaft | ca. 10.000-50.000 EUR/Jahr (mehrere Objekte) |

**Kosten & Break-even:** Fixkosten moderat (Drucker 1.000-5.000 EUR, CAD/Statik-Nachweis-Aufwand, Freilandtest-Jahr, Zertifizierungs-/Abstimmungsaufwand mit Behoerden). Variable Kosten je Modul klein. Der Hebel liegt im Beratungs- und Nachweisgeschaeft: schon wenige Objekte pro Monat (Module + Beratung + Nachweis) tragen einen Soloselbststaendigen; ein Rahmenvertrag mit einer Wohnungsgesellschaft stabilisiert die Auslastung. Break-even realistisch im ersten Jahr nach Freilandvalidierung und der ersten behoerdlich akzeptierten Referenz. Groesstes Zeitrisiko: Freilandtest und behoerdliche Akzeptanz vor dem Skalieren.

**Passende Foerderung**

- DBU (Deutsche Bundesstiftung Umwelt) - innovative Umwelttechnik/Material (Freilandtest und Materialvalidierung).
- Bundesprogramm Biologische Vielfalt (BfN) - Arten in besonderer Verantwortung Deutschlands (Gebaeudebrueter).
- Prototype Fund fuer die offene Konstruktions- und Nachweis-Dokumentation.
- KfW-Programme zu energetischer Sanierung als Nachbarschaft/Anknuepfungspunkt (CEF ist Teil vieler Sanierungen).
- Kommunale Ersatzzahlungen nach Paragraf 15 BNatSchG und EXIST-Gruenderstipendium fuer die Gruendungsphase.

**Vorbilder:** Schwegler (Holzbeton-Nisthilfen/Einbausteine, Marktfuehrer - belegt den Markt), Strobel Betonbau / Naturschutzprodukte (Einbaustein-Hersteller), Ehlert und Partner, Hasselfeldt, WBV (Einbau-Niststeine Gebaeudebrueter), Printednest und 3D-printed bat house-Forschung (Machbarkeit 3D-Druck, Marktbeleg)

**Naechste Schritte (90 Tage)**

- 2-3 Modultypen final konstruieren (Mauersegler-Einbaustein, Fledermaus-Spaltquartier, Schwalben-Kunstnest) nach NABU/LBV-Maßen.
- Je ein Muster ein Jahr im Freien testen (Temperatur, Verformung, Annahme) - ohne Freilandbeleg kein Verkauf.
- Fruehzeitig mit EINER unteren Naturschutzbehoerde die Akzeptanz der Module als CEF-Massnahme abstimmen.
- Offene Konstruktion + Einbau-Datenblatt + Nachweis-Vorlage veroeffentlichen (Prototype-Fund/DBU-faehig).
- Erstes Pilot-Objekt mit einer kommunalen Wohnungsbaugesellschaft (Module + Beratung + Nachweis).
- Fallstudie erstellen und gezielt Architekten, Planungsbueros und Wohnungsgesellschaften ansprechen; Rahmenvertrag anstreben.

> ⚠️ **Risiken:** Produkthaftung und Fachlichkeit: ein untauglich gedrucktes Quartier (Ueberhitzung, UV-Versproedung, falsche Maße) kann Bruten toeten und ist schlechter als kein Kasten - Freilandvalidierung und Behoerdenabstimmung sind Pflicht, nicht Kuer. Behoerdliche Akzeptanz von Kunststoff gegenueber bewaehrtem Holzbeton ist nicht garantiert (Thermik oft schlechter) - helle Farbe, Doppelwand/Belueftung, ggf. Komposit-Material. Lange Bauzyklen und Genehmigungsabhaengigkeit; Haftung fuer den Nachweis sauber abgrenzen (ggf. mit Gutachter kooperieren). Etablierte Hersteller sind stark - Differenzierung ueber Preis, Gewicht, Anpassbarkeit und Komplettservice.

**Quellen:** [Paragraf 44 BNatSchG - Vorschriften fuer besonders geschuetzte Arten (dejure.org)](https://dejure.org/gesetze/BNatSchG/44.html) · [Schwegler - Gebaeudebrueter-Nisthilfen fuer Bauherren, Architekten und Planer (PDF)](http://www.schwegler-natur.de/wp-content/uploads/2014/03/DEU_Gebaeudebrueter_ANSICHT.pdf) · [Beispiel CEF-Massnahmen Gebaeudebrueter (Stadt Garching, PDF)](https://www.garching.de/meldungen/vorhabenbezogener-bebauungsplan-nr_-193-%E2%80%9Enachverdichtung-freisinger-landstra%C3%9Fe-17-17a%E2%80%9C_/_/04_CEF_Ma%C3%9Fnahmen.pdf) · [Evaluating bat boxes: overheating risk (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041549/) · [3D printed bat houses with biomass-derived composites (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2950431725000668) · [NABU - Nist- und Bruthilfen fuer Gebaeudebrueter](https://www.nabu.de/tiere-und-pflanzen/voegel/helfen/nistkaesten/index.html) · [Schwellenwerte und Wertgrenzen im Vergaberecht (Baden-Wuerttemberg, Juni 2024)](https://wm.baden-wuerttemberg.de/fileadmin/redaktion/m-wm/intern/Dateien_Downloads/Wirtschaftsstandort/Schwellenwerte_Wertgrenzen_Vergaberecht_Stand_Juni_2024.pdf)

---

### NaturDruck - offener 3D-Druck-Baukasten fuer den kommunalen Naturschutz

Markt **B** · Ertrag 3/5 · Aufwand 2/5 · MVP 2-3 Monate (3-4 validierte Druckvorlagen + ein Starter-Set + eine Workshop-Vorlage) · `naturdruck-baukasten-fablab`

**Ein offener 3D-Druck-Baukasten artgerechter Naturschutz-Kleinbauten (Wildbienen-Nistbloecke, Gully-/Regentonnen-Ausstiegshilfen, Igeldurchlaesse) mit freien Druckvorlagen - verkauft werden fertige Sets, lokale Produktion ueber Inklusionswerkstatt und Workshops fuer Kommunen, Firmen und Schulen.**

_Problem:_ Kommunen, Bauhoefe und Umweltaemter sollen Artenschutz im Alltag umsetzen (Biodiversitaetsstrategie, kommunale Eh-da-Flaechen, Verkehrssicherung an Gullys, Regentonnen), haben aber weder Zeit noch guenstige, artgerechte Standardbauteile. Baumarkt-Insektenhotels sind oft untauglich (Glasroehrchen, zu weite Bohrungen, nicht reinigbar) und bleiben leer; Tierfallen wie offene Gullys und Regentonnen toeten Amphibien und Kleinsaeuger. Regulatorischer Treiber: kommunale Biodiversitaetsstrategien, das Buendnis Kommunen fuer biologische Vielfalt und Ersatzzahlungen nach Paragraf 15 BNatSchG (zweckgebunden fuer Naturschutzmassnahmen) schaffen Budgets fuer genau solche Kleinmassnahmen, aber es fehlt ein einfaches Beschaffungs-Produkt.

_Loesung:_ Ein modularer Baukasten aus fachlich geprueften, freien Druckvorlagen: Wildbienen-Nistbloecke mit herausnehmbaren, reinigbaren Einsaetzen und Papierhuelsen (Lochspanne 2-9 mm, Schwerpunkt 3-6 mm, 12-15 cm tief, hinten geschlossen), Ausstiegshilfen/Rampen fuer Gullys, Strassenablaeufe und Regentonnen (Amphibien/Kleinsaeuger), Igeldurchlaesse fuer Zaeune, Lichtschacht-Ausstiege, Reptilien-Sonnenplatten. Die STL/STEP-Dateien und Bauanleitungen sind offen (CC-BY-SA); verkauft werden fertige, montagebereite Sets aus UV-festem PETG/ASA plus Montagematerial, die lokale Produktion sowie Workshops. 3D-Druck sichert maßgenaue, reinigbare Teile - der eigentliche Mehrwert gegenueber Baumarktware.

**Zugang zur oeffentlichen Hand**

- Kommunale Bauhoefe, Gruenflaechen- und Umweltaemter - Direktauftrag unterhalb der Wertgrenze (je nach Bundesland oft bis 10.000 EUR formfrei als Direktauftrag, Verhandlungsvergabe bis ca. 100.000 EUR) fuer Sets und Montage.
- Untere Naturschutzbehoerden als Multiplikator und fuer die Verwendung von Ersatzzahlungen nach Paragraf 15 BNatSchG (zweckgebundene Naturschutz-Budgets).
- Buendnis Kommunen fuer biologische Vielfalt / Label StadtGruen naturnah als Tueroeffner und Referenzkanal.
- Rahmenvertrag mit Landkreis oder Stadtwerk fuer wiederkehrende Lieferung an mehrere Standorte (Schulen, Kitas, Friedhoefe, Kleingaerten).
- Einstieg ueber ein gefoerdertes Pilot mit EINER Kommune (Referenz vor Umsatz), Ergebnis als Fallstudie fuer weitere Landkreise.

**Open-Source-Hebel:** Offene Designs sind beim Staat ein Vorteil: Public Money Public Code und kein Vendor-Lock-in erleichtern Beschaffung und Weitergabe an Vereine/Schulen; die offene, fachlich gepruefte Methodik macht die Massnahme nachvollziehbar und foerderfaehig. Geld kommt nicht aus der Datei, sondern aus fertigen, qualitaetsgesicherten Sets, lokaler Produktion, Montage und Workshops (Open-Core: Vorlage frei, Produkt und Service bezahlt). Die freien Vorlagen sind zugleich Marketing und Prototype-Fund-faehig.

**3D-Druck-Hebel:** Gedruckt werden Nistblock-Rahmen und Einsaetze, Ausstiegsrampen, Igeldurchlass-Rahmen, Sonnenplatten und Halterungen aus UV-/hitzebestaendigem PETG oder ASA (helle Farben gegen Hitzestau), Wandstaerke ab 2 mm, mit Papier-Nisthuelsen gegen Kondens. Materialkosten pro Teil wenige Euro (Filament ca. 20-30 EUR/kg); on-demand und lokal produzierbar, modular und reparierbar (Einsaetze jaehrlich tauschbar). Produktion laesst sich an eine Inklusions-/Behindertenwerkstatt oder ein FabLab auslagern - planbare Kosten, lokale Wertschoepfung und ein sozialer Vergabe-Bonus fuer die Kommune.

**Geschaeftsmodell:** Open-Core Hardware & Service: Die Druckvorlagen und Anleitungen sind offen (Vertrauen, Vergabefaehigkeit, Reichweite), verdient wird an fertigen, qualitaetsgesicherten Sets, lokaler Produktion ueber eine Inklusionswerkstatt/FabLab, Montage, Workshops und einem Huelsen-/Pflege-Abo. Wiederkehrender Umsatz kommt aus Service-Abos und Rahmenvertraegen mit Kommunen; Firmen-CSR und Schulen verbreitern die Basis.

**Einnahmequellen**

- Verkauf fertiger Sets (Wildbienen-Starter, Gully-Ausstieg, Igel-Set) an Kommunen, Firmen und Private.
- Workshops/Mitmachaktionen fuer Kommunen, Schulen und Firmen-CSR (Teambuilding mit Naturschutznutzen).
- Jahres-Service: Reinigungseinsaetze/Papierhuelsen-Nachschub und Pflege-Checks als Abo.
- Lohn-Druck und Konfektionierung als Auftrag (Inklusionswerkstatt als Produktionspartner).
- Foerderprojekte als Entwicklungs- und Pilotfinanzierung; Lizenz-/Supportpaket fuer Bauhoefe, die selbst drucken.

| Preis / Kennzahl | Wert |
|---|---|
| Wildbienen-Starter-Set (Block + Einsaetze + Huelsen + Montage) | ca. 45-80 EUR (Material/Druck ~8-15 EUR) |
| Gully-/Regentonnen-Ausstiegshilfe | ca. 15-35 EUR/Stueck, Staffel ab 50 Stueck guenstiger |
| Kommunen-Paket (20 Sets gemischt + Einweisung) | ca. 1.500-3.000 EUR |
| Workshop (halber Tag, bis 20 Personen, Material inkl.) | ca. 600-1.200 EUR |
| Jahres-Service Huelsen/Pflege | ca. 3-8 EUR pro Set und Jahr |

**Kosten & Break-even:** Geringe Fixkosten (ein bis zwei 3D-Drucker ca. 500-2.000 EUR, Materiallager, Web/Shop). Variable Kosten je Set klein (Material + Druckzeit + Konfektion). Als Soloselbststaendige(r) oder Kleinteam traegt es sich bei grob 150-300 verkauften Sets plus einigen Workshops und einem Kommunen-Paket pro Monat (Richtwert 2.500-5.000 EUR Deckungsbeitrag/Monat). Engpass ist nicht die Herstellung, sondern Vertrieb und Workshop-Akquise; Lohn-Druck ueber die Inklusionswerkstatt haelt die Skalierungskosten planbar.

**Passende Foerderung**

- Prototype Fund (BMBF/Open Knowledge Foundation) fuer die offenen Druckvorlagen und die Doku-Plattform.
- DBU (Deutsche Bundesstiftung Umwelt) - Umweltbildung/Umwelttechnik, auch fuer Werkstatt-Kooperation.
- Bundesprogramm Biologische Vielfalt (BfN) und chance.natur fuer kommunale Umsetzungsprojekte.
- Kommunale Mittel aus Ersatzzahlungen nach Paragraf 15 BNatSchG und Landschaftspflege-Budgets.
- Deutsche Postcode Lotterie und regionale Stiftungen fuer Bildungs-/Mitmachaktionen; Aktion Mensch fuer die Inklusionswerkstatt-Kooperation.

**Vorbilder:** Printednest (offene, in ueber 20 Laendern installierte 3D-gedruckte Vogelnester als Marktbeleg), Precious Plastic / Print Your City (dezentrale, recycelte Kunststoff-Fertigung als Modell), Wildlife World, Schwegler, habibi.home (kommerzielle Nisthilfen-/Naturschutzprodukte als Markt), FabLabs und Inklusionswerkstaetten mit Lohn-Druck (z.B. Caritas-/Lebenshilfe-Werkstaetten) als Produktionspartner

**Naechste Schritte (90 Tage)**

- 3-4 Vorlagen final validieren und mit NABU/BUND-Kriterien abgleichen (Wildbienenblock, Gully-Ausstieg, Igeldurchlass, Sonnenplatte).
- Ein Muster je Typ ein Saison im Freien testen (Verformung, Annahme) und Fotos/Belege sammeln.
- Produktionspartner finden: Kooperationsgespraech mit einer Inklusionswerkstatt/FabLab zu Lohn-Druck und Kalkulation.
- STL/STEP + Anleitung als CC-BY-SA veroeffentlichen (Vertrauensaufbau, Prototype-Fund-Antrag starten).
- EINE Kommune/Bauhof als Pilot gewinnen (Direktauftrag unter Wertgrenze) und eine Workshop-Vorlage erproben.
- Fallstudie und 1-Seiten-Angebot erstellen, an Buendnis-Kommunen und 20 weitere Landkreise ausrollen.

> ⚠️ **Risiken:** Kleine Stueckdeckungsbeitraege - ohne Workshops und Rahmenvertraege bleibt es ein Hobby-Umsatz. Kunststoff-Risiken real (Kondens/Hitzestau, Mikroplastik, UV-Alterung) - Material, helle Farben, Belueftung und Papierhuelsen ernst nehmen, sonst schadet schlechtes Design mehr als es nutzt. Billig-Konkurrenz und kostenlose STLs druecken Preise; der Mehrwert muss ueber Qualitaet, Beratung, Montage und Service verteidigt werden. Abhaengigkeit von Foerdermitteln vermeiden, frueh echten Auftragsumsatz suchen. Wildbienen-Nisthilfen ersetzen keine Bluehflaechen/Bodenniststrukturen - ehrlich kommunizieren, kein Greenwashing.

**Quellen:** [NABU - Tipps fuer wirksame Wildbienen-Nisthilfen](https://www.nabu.de/tiere-und-pflanzen/insekten-und-spinnen/hautfluegler/bienen/13704.html) · [wildbienen.info - Untaugliche Nisthilfen](https://www.wildbienen.info/artenschutz/untaugliche_nisthilfen_A.php) · [Printednest - 3D Printing the Birds Back to the City](https://3dprintingindustry.com/news/3d-printing-bird-nest-26278/) · [Schwellenwerte und Wertgrenzen im Vergaberecht (Baden-Wuerttemberg, Juni 2024)](https://wm.baden-wuerttemberg.de/fileadmin/redaktion/m-wm/intern/Dateien_Downloads/Wirtschaftsstandort/Schwellenwerte_Wertgrenzen_Vergaberecht_Stand_Juni_2024.pdf) · [Paragraf 15 BNatSchG - Verursacherpflichten und Ersatzzahlung (dejure.org)](https://dejure.org/gesetze/BNatSchG/15.html) · [Prototype Fund](https://prototypefund.de/) · [Buendnis Kommunen fuer biologische Vielfalt](https://www.kommbio.de/)

---


## Software & Plattform

### NaturBuero-KI - KI-Assistent fuer Naturschutz-Verwaltung und Ehrenamt

Markt **B** · Ertrag 4/5 · Aufwand 3/5 · MVP 3-4 Monate (ein Antrags-/Berichts-Workflow fuer EINE Foerderlinie, mit Quellen-Beleg und Export) · `naturbuero-ki`

**Ein KI-Assistent mit Mensch-prueft-alles-Prinzip, der Naturschutzbehoerden und ehrenamtlichen Verbaenden die laestige Schreibarbeit abnimmt - Foerderantraege, Berichte, Kartierungs-Protokolle, Stellungnahmen und Oeffentlichkeitsarbeit - auf EU-Hosting und DSGVO-konform.**

_Problem:_ Naturschutz ist eine Schreib- und Antragslast. Untere Naturschutzbehoerden, Landschaftspflegeverbaende und ehrenamtliche NABU-/BUND-Ortsgruppen verbringen einen grossen Teil ihrer knappen Zeit mit Formularen: Foerderantraege (Bundesprogramm Biologische Vielfalt, LIFE, ELER/Agrarumwelt, kommunale Toepfe), Verwendungsnachweise und Zwischenberichte, Kartierungs-Protokolle, naturschutzfachliche Stellungnahmen zu Bauleitplanung und Eingriffen, Pflege- und Entwicklungsplaene, Pressetexte. Regulatorische Treiber: Berichtspflichten nach BNatSchG und FFH-/Vogelschutzrichtlinie, Nachweispflichten der Foerdermittelgeber, kurze Einreichfristen. Gleichzeitig Fachkraeftemangel und ueberlastetes Ehrenamt. Fertige Buero-KI aus den USA scheidet fuer Behoerden oft wegen Datenschutz und fehlender Fachlichkeit aus.

_Loesung:_ Eine Open-Source-Assistenzsoftware, spezialisiert auf Naturschutz-Verwaltungstexte. Nutzer laden eigene Daten (Kartierungen, Massnahmenlisten, Foerderrichtlinie, Vorjahresberichte) in eine lokale Wissensbasis; die KI erstellt Entwuerfe strikt auf Basis dieser Quellen (Retrieval-Augmented, jede Aussage mit Quellenbeleg aus dem eigenen Dokument), nie frei erfunden. Workflows: Foerderantrag ausfuellen, Bericht aus Rohdaten, Stellungnahme-Geruest, Pressetext, Protokoll aus Stichpunkten. Kernprinzip Mensch-prueft-alles: die KI liefert Entwuerfe und markiert Luecken/Unsicherheiten, der Mensch gibt frei. Betrieb on-premises oder auf EU-Cloud (offene Modelle wie Teuken/Llama/Mistral, oder Anbindung an souveraene Modelle). Die Software ist offen, verdient wird an Hosting, Einrichtung, Vorlagen und Schulung.

**Zugang zur oeffentlichen Hand**

- Untere Naturschutzbehoerden der Landkreise und kreisfreien Staedte - Direktauftrag moeglich (seit 2026 Direktauftrag haeufig bis 50.000 EUR netto, Verhandlungsvergabe bis 100.000 EUR netto).
- Landschaftspflegeverbaende und Biologische Stationen (oft e.V. mit Behoerden-Finanzierung) - koennen direkt beauftragen, kurze Wege.
- Nationalpark-, Naturpark- und Biosphaerenreservats-Verwaltungen als Rahmenvertrag ueber mehrere Reviere.
- Kommunale Umwelt-/Gruenflaechenaemter fuer eigene Foerderantraege und Oeffentlichkeitsarbeit.
- Einstieg ueber ein gefoerdertes Pilot-/Reallabor mit einer Behoerde oder einem Dachverband (NABU-/BUND-Landesverband), Ergebnis als Referenz.
- Veroeffentlichung auf openCode (ZenDiS) macht die Software fuer alle Verwaltungen sichtbar und nachnutzbar - Vertriebskanal ueber Behoerden-Community.

**Open-Source-Hebel:** Bei KI in der Verwaltung ist Souveraenitaet das Verkaufsargument: offene Modelle und offener Code erlauben On-Premises-Betrieb ohne Datenabfluss an US-Clouds, nachpruefbare Prompts und kein Vendor-Lock-in - genau die Kriterien von ZenDiS/openCode und Public Money Public Code. Behoerden-Juristen und Datenschutzbeauftragte stimmen offenen, auditierbaren Loesungen leichter zu. Geld kommt nicht aus Lizenz, sondern aus EU-Hosting/Betrieb, fachlichen Vorlagen-Paketen (Foerderlinien), Einrichtung in die jeweilige Datenlage und Schulung - das darf man trotz OSS berechnen.

**3D-Druck-Hebel:** Hier softwarelastig - kein 3D-Druck-Kern. Optional als Zusatz: gedruckte QR-Infotafeln fuer die Oeffentlichkeitsarbeit (die die KI mit Text/Layout bestueckt) oder gedruckte Aufsteller fuer Buergerbeteiligungs-Termine; Produktion in einer Inklusionswerkstatt als sozialer Vergabe-Bonus moeglich.

**Geschaeftsmodell:** Open-Core plus B2G-SaaS und Dienstleistung: Der KI-Assistenz-Kern ist offen (auditierbar, souveraen, vergabefreundlich, auf openCode auffindbar); verkauft werden EU-Hosting/On-Prem-Betrieb, die fachliche Einrichtung in die konkrete Datenlage, Foerderlinien-Vorlagen und Schulung. Wiederkehrender Umsatz aus Abo- und Supportvertraegen; Projektgeschaeft aus Einrichtung. Das Mensch-prueft-alles-Prinzip ist zugleich Haftungs- und Qualitaets-Argument im Vertrieb.

**Einnahmequellen**

- SaaS-Abo je Arbeitsplatz oder je Organisation (EU-Hosting inklusive).
- On-Premises-Lizenz-/Supportvertrag fuer Behoerden mit eigenem Rechenzentrum.
- Einrichtung: Anbindung der eigenen Dokumente/Datenbanken, Aufbau der Wissensbasis.
- Vorlagen-Pakete je Foerderlinie (Bundesprogramm Biologische Vielfalt, LIFE, ELER) als Add-on.
- Schulung/Workshops fuer Behoerden und Ehrenamt (Prompting, Pruefpflicht, Grenzen der KI).
- Foerderprojekte als Entwicklungsfinanzierung des offenen Kerns.

| Preis / Kennzahl | Wert |
|---|---|
| SaaS je Arbeitsplatz | ca. 30-60 EUR pro Platz und Monat (EU-Hosting) |
| Organisations-Flat kleine Behoerde/Verband | ca. 2.400-6.000 EUR pro Jahr |
| Einrichtung + Datenanbindung | ca. 3.000-12.000 EUR einmalig |
| On-Premises Lizenz + Support | ca. 8.000-25.000 EUR pro Jahr je nach Groesse |
| Schulung (Halbtag, Gruppe) | ca. 600-1.200 EUR |
| Vorlagen-Paket je Foerderlinie | ca. 500-1.500 EUR einmalig |

**Kosten & Break-even:** Hauptkostenblock ist Entwicklungszeit; laufend GPU-/Inferenz-Kosten (bei kleinen offenen Modellen moderat) und EU-Hosting. Als Soloselbststaendiger/kleines Team Break-even realistisch bei ca. 15-25 zahlenden Organisationen im Flat-Abo oder einigen On-Prem-Vertraegen (ca. 40-80 TEUR ARR). Der erste gefoerderte Pilot plus zwei bis drei Einrichtungsauftraege decken die MVP-Phase. Groesstes Risiko ist nicht Technik, sondern Beschaffungs- und Datenschutz-Freigabezyklen.

**Passende Foerderung**

- Prototype Fund (bis 47.500 EUR fuer Einzelperson, bis 158.333 EUR fuer Teams) fuer den offenen Kern - thematisch Civic Tech / Verwaltung.
- EXIST-Gruenderstipendium (2.500-3.000 EUR/Monat + bis 5.000 EUR Sachmittel) fuer die Gruendungsphase aus einer Hochschule.
- DBU - Digitalisierung im Umwelt-/Naturschutz.
- Bundesprogramm Biologische Vielfalt (BfN) - innovative Werkzeuge fuer Umsetzung und Ehrenamt.
- GovTech-/Digitalisierungsprogramme von Bund und Laendern (OZG-Nachfolge, Modellkommunen), ZenDiS/openCode-Umfeld.
- Deutsche Postcode Lotterie - Projekte fuer ehrenamtlichen Naturschutz.

**Vorbilder:** Aleph Alpha (Verwaltungs-KI, souveraen; Referenzen Bundesagentur fuer Arbeit, Baden-Wuerttemberg, Partnerschaft mit Bayern) als Markt-Beleg fuer Behoerden-KI, ZenDiS / openCode und openDesk (offene Verwaltungssoftware als anerkanntes Modell), GovTech-Startups mit Antrags-/Bescheid-Assistenz fuer Kommunen, spezialisierte Foerderantrags-KI-Anbieter (Fundraising-/Antrags-Copiloten) als Markt-Beleg, Deutsche Teuken/OpenGPT-X und andere offene EU-Modelle als souveraene Basis

**Naechste Schritte (90 Tage)**

- Einen konkreten Schmerz-Workflow waehlen (z.B. Verwendungsnachweis einer haeufigen Foerderlinie) und als MVP bauen - mit strikter Quellen-Bindung und Export.
- Eine Partner-Behoerde oder einen Landschaftspflegeverband als Pilot gewinnen, echte (anonymisierte) Dokumente nutzen.
- Datenschutz-/DSGVO-Konzept und On-Prem-/EU-Hosting-Variante von Anfang an dokumentieren (fuer die Freigabe durch Datenschutzbeauftragte).
- Offenes Repo + Doku veroeffentlichen und auf openCode einstellen (Sichtbarkeit, Prototype-Fund-faehig).
- Preisliste und 1-Seiten-Angebot fuer Direktauftrag unter Vergabeschwelle erstellen.
- Aus dem Pilot eine Fallstudie machen (Zeitersparnis in Stunden pro Antrag) und an Nachbar-Landkreise/Verbaende ausrollen.

> ⚠️ **Risiken:** Groesstes Risiko ist KI-Halluzination in Verwaltungstexten: frei erfundene Rechtsgrundlagen, Zahlen oder Quellen koennen zu fehlerhaften Antraegen/Bescheiden fuehren - deshalb strikte Quellen-Bindung, sichtbare Unsicherheits-Markierung und verpflichtende menschliche Freigabe, keine Voll-Automatisierung. Datenschutz: personen- und ggf. standortbezogene (schutzwuerdige Arten-)Daten duerfen nicht abfliessen - On-Prem/EU-Hosting zwingend. Behoerden-Beschaffungs- und Freigabezyklen sind lang; Abhaengigkeit von Foerdermitteln vermeiden. Markt mit kapitalstarken Anbietern (Aleph Alpha) - deshalb Nische Naturschutz-Fachlichkeit und Ehrenamt besetzen, nicht Allzweck-Verwaltung.

**Quellen:** [Baden-Wuerttemberg nimmt KI-System von Aleph Alpha in Betrieb](https://www.egovernment.de/baden-wuerttemberg-nimmt-ki-system-von-aleph-alpha-in-betrieb-a-6ebe5e669c8ca83faff0fdd61106a85f/) · [Digitalministerium Bayern und Aleph Alpha - Partnerschaft Verwaltung](https://www.stmd.bayern.de/digitalministerium-und-aleph-alpha-verkuenden-strategische-partnerschaft-zur-digitalisierung-der-verwaltung-aleph-alpha-eroeffnet-standort-muenchen/) · [ZenDiS / openCode - Plattform fuer digitale Souveraenitaet](https://www.zendis.de/) · [Prototype Fund](https://prototypefund.de/) · [EXIST-Gruendungsstipendium (Foerderdatenbank)](https://www.foerderdatenbank.de/FDB/Content/DE/Foerderprogramm/Bund/BMWi/exist-gruendungsstipendium.html) · [Vergaberecht 2026 - neue Wertgrenzen Direktauftrag/Verhandlungsvergabe](https://subreport.de/blog/vergaberecht-2026-neue-spielraeume-neue-unsicherheiten/) · [Bundesprogramm Biologische Vielfalt (BfN)](https://www.bfn.de/bundesprogramm-biologische-vielfalt)

---

### BuergerNatur - White-Label-Plattform fuer kommunale Citizen Science

Markt **B** · Ertrag 3/5 · Aufwand 3/5 · MVP 3-5 Monate (gebrandetes Web-Portal + PWA/App auf iNaturalist-/GBIF-Standards, eine Kampagne, Export) · `buergernatur-plattform`

**Ein eigenes, im Kommunen-/Schutzgebiets-Design gebrandetes Arterfassungs-Portal mit App - aufgesetzt auf offene Standards (GBIF, iNaturalist/observation.org) - mit dem Buerger Beobachtungen melden und die Verwaltung daraus Monitoring-Daten gewinnt.**

_Problem:_ Kommunen, Naturparke, Biosphaerenreservate und Schutzgebiets-Verwaltungen sollen Buerger beteiligen und gleichzeitig verlaessliche Daten ueber ihre Arten gewinnen - fuer Pflegeplaene, Berichtspflichten (FFH, Natura 2000), Gruenflaechen-Monitoring, Klimaanpassung und Oeffentlichkeitsarbeit. Regulatorische/politische Treiber: Biodiversitaetsstrategien von Bund/Laendern/EU, Natura-2000-Managementplaene, kommunale Nachhaltigkeits-/Biodiversitaetskonzepte, Pflicht zur Buergerbeteiligung. In der Praxis gibt es keine eigene Plattform: Daten liegen verstreut in Excel, generischen Apps oder gar nicht; eine eigene von Grund auf zu bauen ist zu teuer, und reine Fremd-Apps liefern keine kommunal nutzbaren, gefilterten Daten.

_Loesung:_ Eine Mehrmandanten-Plattform (Software-as-a-Service), die jede Kommune/jedes Schutzgebiet als eigenes, gebrandetes Portal plus App (PWA/native) bekommt. Technisch setzt sie auf offene Standards und bestehende Infrastruktur auf: Arterkennung und Daten koennen mit iNaturalist/observation.org und FloraIncognita-/Pl@ntNet-Erkennung verknuepft werden, Export nach GBIF im Darwin-Core-Standard, keine Dateninsel. Features: Beobachtungen melden (Foto/Ton/Ort), Bestimmungshilfe, thematische Kampagnen (z.B. Wildbienen, Amphibien, Stadtbaeume), Qualitaetssicherung durch Experten, Dashboards und Export fuers kommunale Monitoring, Buergerbeteiligungs-Modul. Code offen, verdient wird an Einrichtung, Betrieb und Auswertung.

**Zugang zur oeffentlichen Hand**

- Kommunale Umwelt-/Gruenflaechenaemter - Direktauftrag moeglich (seit 2026 oft bis 50.000 EUR netto Direktauftrag, bis 100.000 EUR netto Verhandlungsvergabe).
- Naturpark-, Biosphaerenreservats- und Nationalpark-Verwaltungen (Dauer-Monitoring, Umweltbildung) - als Rahmenvertrag ueber mehrere Jahre.
- Untere Naturschutzbehoerden und Biologische Stationen fuer ehrenamtlich getragenes Monitoring.
- Landes-Biodiversitaetsstrategien / Stiftungen Naturschutz der Laender als Mehr-Standort-Auftraggeber.
- Einstieg ueber ein gefoerdertes Reallabor mit EINER Modellkommune/einem Schutzgebiet; Referenz fuer weitere.
- Veroeffentlichung auf openCode macht das Portal fuer andere Kommunen nachnutzbar - Betrieb/Anpassung wird zugekauft.

**Open-Source-Hebel:** Offener Code plus offene Datenstandards (GBIF/Darwin Core) sind fuer Kommunen ein doppelter Vorteil: digitale Souveraenitaet und kein Lock-in (Public Money Public Code), und die Buergerdaten fliessen nachpruefbar in die wissenschaftliche Infrastruktur statt in eine proprietaere Insel. Das erhoeht Vertrauen, Datenqualitaet und Vergabefaehigkeit. Verdient wird trotzdem: an Einrichtung/Branding, gehostetem Betrieb, Moderation/Qualitaetssicherung und der Aufbereitung der Daten zu kommunal verwertbaren Berichten.

**3D-Druck-Hebel:** Hier softwarelastig. Optionaler 3D-Druck-Hebel: gedruckte, wetterfeste QR-Infotafeln und Melde-Stelen an Wanderwegen/Schutzgebieten, die auf die App verweisen und Kampagnen bewerben; Halterungen und Gehaeuse lokal gedruckt (PETG/ASA), Produktion in einer Inklusionswerkstatt moeglich (sozialer Vergabe-Bonus, Reparierbarkeit).

**Geschaeftsmodell:** Mehrmandanten-SaaS mit Open-Core: Ein offener Plattform-Kern (vergabefreundlich, souveraen, GBIF-anschlussfaehig, auf openCode auffindbar), der je Kunde als gebrandetes Portal betrieben wird. Umsatz aus Einrichtung (Projekt), jaehrlicher Betriebsgebuehr (wiederkehrend) und datennaher Dienstleistung (Auswertung, Moderation, Kampagnen). Skalierung ueber viele Mandanten auf einer Codebasis; der Open-Source-Charakter senkt die Beschaffungshuerde und schafft Nachnutzung statt Parallelentwicklung.

**Einnahmequellen**

- Einrichtung: Branding, Konfiguration, Artenlisten, Kampagnen-Setup, Datenanbindung.
- Jaehrliche Betriebsgebuehr je Mandant (Hosting, Updates, Support).
- Auswertung/Reports: kommunal verwertbare Monitoring-Auswertungen und GBIF-Export.
- Moderation/Qualitaetssicherung als Service (Experten-Validierung).
- Umweltbildungs-/Kampagnen-Pakete und Begleitung (Schulklassen, Aktionstage).
- Foerderprojekte als Entwicklungs- und Pilotfinanzierung.
- Optional gedruckte Infotafeln/Stelen.

| Preis / Kennzahl | Wert |
|---|---|
| Einrichtung je Mandant | ca. 4.000-15.000 EUR einmalig (Branding, Konfiguration, Kampagnen) |
| Jahres-Betriebsgebuehr je Mandant | ca. 3.000-9.000 EUR pro Jahr (Hosting, Updates, Support) |
| Auswertung/Monitoring-Report | ca. 1.500-5.000 EUR pro Saison/Report |
| Kampagnen-Paket + Begleitung | ca. 2.000-6.000 EUR je Kampagne |
| gedruckte QR-Infotafel | ca. 40-120 EUR pro Stueck (Material wenige Euro) |

**Kosten & Break-even:** Fixkosten sind Entwicklung und gemeinsame Hosting-/Mehrmandanten-Infrastruktur (skaliert gut: ein Kern, viele Mandanten). Variable Kosten je neuem Mandant gering (Konfiguration). Break-even als kleines Team realistisch bei ca. 8-15 Mandanten im Jahres-Betrieb plus Einrichtungs- und Auswertungsumsatz (ca. 40-80 TEUR ARR). Der erste gefoerderte Modell-Mandant finanziert die Plattform-Basis; danach ist jeder weitere Mandant margenstark, weil er auf dem gleichen Kern laeuft.

**Passende Foerderung**

- Bundesprogramm Biologische Vielfalt (BfN) - Citizen Science / Monitoring / Buergerbeteiligung.
- DBU - Umweltbildung und Digitalisierung im Naturschutz.
- Prototype Fund fuer den offenen Plattform-Kern.
- EU LIFE (Natur und Biodiversitaet) fuer groessere Schutzgebiets-Verbuende.
- Deutsche Postcode Lotterie - buergerschaftliches Engagement im Naturschutz.
- Kommunale Mittel / Smart City / Smart Region fuer die Modellkommune.
- Laender-Stiftungen Naturschutz und Buergerbeteiligungs-Foerderung.

**Vorbilder:** iNaturalist (globaler Standard, Netzwerk-Knoten-Modell als Vorbild fuer White-Label), observation.org / Observation International (Plattform-Betrieb fuer Regionen und Organisationen), Naturblick (Museum fuer Naturkunde Berlin; ~120.000-130.000 Nutzer, von Berlin-Pilot auf ganz Deutschland skaliert), Flora Incognita / Pl@ntNet (Arterkennung als anschlussfaehige Komponente), GBIF / GBIF Deutschland (offene Dateninfrastruktur als Ziel-Standard), SPOTTERON (White-Label-Citizen-Science-App-Anbieter aus Oesterreich als direkter Markt-Beleg)

**Naechste Schritte (90 Tage)**

- Technik-Fundament entscheiden: auf iNaturalist-/observation.org-Standards aufsetzen, Darwin-Core-/GBIF-Export sicherstellen (keine Dateninsel).
- MVP: ein gebrandetes Portal + PWA mit einer Kampagne (z.B. Amphibien oder Wildbienen) fuer EINEN Modell-Mandanten.
- Eine Modellkommune / ein Naturpark als Pilot gewinnen, moeglichst gefoerdert; echte Kampagne durchfuehren.
- Report-Vorlage mit der unteren Naturschutzbehoerde abstimmen (behoerdentauglich, berichtsfaehig).
- Offenes Repo + Doku veroeffentlichen, auf openCode einstellen (Nachnutzung, Prototype-Fund-faehig).
- Fallstudie mit Zahlen (Teilnehmer, Beobachtungen, Datenqualitaet) erstellen und an weitere Kommunen/Schutzgebiete ausrollen.

> ⚠️ **Risiken:** Datenschutz und Artenschutz-Geheimhaltung: Standortdaten schutzwuerdiger/stoerungsempfindlicher Arten (z.B. Greifvogel-Horste) duerfen nicht oeffentlich werden - Unschaerfe/Zugriffsschutz noetig; personenbezogene Melder-Daten DSGVO-konform. Datenqualitaet aus Laienmeldungen schwankt (Fehlbestimmungen) - Experten-Validierung und Plausibilitaetspruefung noetig, sonst untauglich fuers amtliche Monitoring. Konkurrenz durch etablierte kostenlose Apps (iNaturalist, Naturblick) - der Mehrwert muss das Branding, die kommunale Auswertung und die Integration sein, nicht die reine Melde-Funktion. Behoerden-Beschaffungszyklen lang; Abhaengigkeit von Foerdermitteln vermeiden, frueh Betriebsvertraege sichern.

**Quellen:** [Naturblick - Museum fuer Naturkunde Berlin (Projektseite)](https://www.museumfuernaturkunde.berlin/de/forschung/projekte/naturblick-stadtnatur-entdecken) · [iNaturalist](https://www.inaturalist.org/) · [observation.org](https://observation.org/) · [GBIF Deutschland](https://www.gbif.de/) · [SPOTTERON - White-Label Citizen Science Apps](https://www.spotteron.net/) · [Bundesprogramm Biologische Vielfalt (BfN)](https://www.bfn.de/bundesprogramm-biologische-vielfalt) · [Vergaberecht 2026 - neue Wertgrenzen](https://subreport.de/blog/vergaberecht-2026-neue-spielraeume-neue-unsicherheiten/)

---

### Roadkill-Radar - Melde- und Analyseplattform fuer Wildunfaelle

Markt **B** · Ertrag 3/5 · Aufwand 3/5 · MVP 3-4 Monate (Melde-PWA + Karte + einfache Hotspot-Statistik + Behoerden-Export) · `roadkill-radar`

**Eine Melde- und Datenplattform fuer Wildunfaelle und Roadkill, auf der Buerger, Polizei und Jaeger Funde erfassen; Statistik und KI finden Unfall-Hotspots und liefern Strassenbauverwaltungen eine datenbasierte Priorisierung fuer Gruenbruecken, Amphibientunnel und Tempolimits.**

_Problem:_ Jaehrlich gibt es in Deutschland hunderttausende Wildunfaelle - mit Personenschaeden, hohen Sachkosten und massivem Verlust an Tieren, auch geschuetzten Arten. Die amtliche Statistik erfasst im Kern nur jagdbares Grosswild; Amphibien, Igel, Kleinsaeuger und viele Arten fehlen voellig. Gleichzeitig muss die oeffentliche Hand knappe Mittel fuer Querungshilfen priorisieren: Eine Gruenbruecke kostet grob 3 Mio. EUR und mehr (Beispiele 3,4 bis ueber 20 Mio. EUR), Amphibienanlagen entsprechend. Treiber: Bundesprogramm Wiedervernetzung, Verkehrssicherheit (Vision Zero), FFH-/Artenschutz, kommunale Amphibienschutz-Pflichten. Es fehlt eine belastbare, flaechendeckende Datengrundlage, um zu entscheiden, WO eine Querungshilfe oder ein Tempolimit den groessten Nutzen bringt.

_Loesung:_ Eine Plattform aus Melde-App/PWA und Auswerte-Backend. Melder (Buerger, Jaeger, Polizei, Strassenmeistereien) erfassen Fundort, Art und Zeit mit wenigen Klicks; Foto-Arterkennung und Plausibilitaetspruefung unterstuetzen. Das Backend verdichtet Meldungen zu Hotspots (raeumlich-zeitliche Statistik, Kernel-Dichte, saisonale Muster bei Amphibienwanderung) und verknuepft sie mit Strassen-, Habitat- und Verkehrsdaten, um Risiko-Abschnitte zu priorisieren. Ergebnis sind Karten und Reports, die Strassenbauverwaltungen direkt in die Massnahmenplanung uebernehmen koennen. Code offen und GBIF-/Standard-anschlussfaehig; verdient wird an Plattform-Betrieb, Hotspot-Analysen und Beratung. Datenaustausch mit bestehenden Katastern (z.B. Tierfund-Kataster) statt Konkurrenz.

**Zugang zur oeffentlichen Hand**

- Autobahn GmbH des Bundes und Landesbetriebe Strassenbau (Strassen.NRW, Landesbetrieb Mobilitaet u.a.) - fuer Hotspot-Analysen und Priorisierung von Querungshilfen (Rahmenvertrag/Dienstleistung).
- Untere Strassenverkehrs- und Naturschutzbehoerden der Landkreise - fuer kommunale Strassen, Amphibienschutzanlagen und Tempolimits (Direktauftrag seit 2026 oft bis 50.000 EUR netto).
- Kommunen fuer innerstaedtische Gefahrenstellen und Amphibien-Querungen.
- Landesjagdverbaende und Jaegerschaften als Datenpartner und Multiplikatoren (Anbindung ans/Abgleich mit dem Tierfund-Kataster des DJV).
- Landesanstalten fuer Umwelt / Strassenwesen (BASt) und Verkehrssicherheits-Programme als Auftraggeber groesserer Studien.
- Einstieg ueber ein gefoerdertes Pilotprojekt mit EINEM Landesbetrieb oder Landkreis; Hotspot-Report als Referenz fuer Ausschreibungen.

**Open-Source-Hebel:** Offener Code und offene Daten-Standards machen die Risikobewertung nachpruefbar und gerichtsfest - wichtig, wenn damit Investitionen in Millionenhoehe (Gruenbruecke) begruendet werden. Public Money Public Code und digitale Souveraenitaet senken die Vergabehuerde; keine Dateninsel, Anschluss an Tierfund-Kataster/GBIF schafft Vertrauen bei Jagd- und Naturschutzpartnern. Geld kommt nicht aus der Software-Lizenz, sondern aus dem gehosteten Plattform-Betrieb, den fachlich aufbereiteten Hotspot-Analysen und der Massnahmen-Beratung.

**3D-Druck-Hebel:** Hier softwarelastig. Optionaler 3D-Druck-Hebel: gedruckte, reflektierende Melde-/Warnstelen und QR-Schilder an bekannten Hotspots (saisonale Amphibien-Warnung), die auf die App verweisen; wetterfeste Halterungen (PETG/ASA) lokal gedruckt, Produktion in einer Inklusionswerkstatt moeglich. Perspektivisch Schnittstelle zu gedruckten Sensor-/Zaehl-Gehaeusen an Querungshilfen (Wirkungskontrolle).

**Geschaeftsmodell:** B2G-Datenplattform mit Open-Core: Der offene Melde-/Analyse-Kern (nachpruefbar, souveraen, kataster-anschlussfaehig, auf openCode auffindbar) senkt die Vergabehuerde; verdient wird am gehosteten Betrieb je Mandant, an fachlich aufbereiteten Hotspot-Analysen und an Massnahmen-/Wirkungskontroll-Beratung. Wiederkehrender Umsatz aus Betriebs-Lizenz und Monitoring; Projektgeschaeft aus Analysen. Die Daten liefern Buerger/Jaeger/Polizei weitgehend kostenlos - Wertschoepfung liegt in Verdichtung, Validierung und Entscheidungsvorlage.

**Einnahmequellen**

- Plattform-/Betriebs-Lizenz je Auftraggeber (Hosting, Updates, Support, Mandant).
- Hotspot-Analyse-Reports (einmalig je Netz/Gebiet, wiederkehrend als Monitoring).
- Beratung: Massnahmen-Priorisierung, Wirkungskontrolle nach Bau einer Querungshilfe.
- Datenintegration/Schnittstellen (Verkehrsdaten, Kataster, GIS der Verwaltung).
- Foerderprojekte als Entwicklungs- und Pilotfinanzierung.
- Optional gedruckte Warn-/Melde-Stelen.

| Preis / Kennzahl | Wert |
|---|---|
| Plattform-/Betriebs-Lizenz je Mandant | ca. 5.000-20.000 EUR pro Jahr (Hosting, Support, Updates) |
| Hotspot-Analyse-Report | ca. 3.000-15.000 EUR je Netz/Gebiet |
| Beratung/Priorisierung (Tagessatz) | ca. 800-1.200 EUR pro Tag |
| Wirkungskontrolle nach Massnahme | ca. 2.000-8.000 EUR pro Standort/Saison |
| Bezug zur Massnahme (Einordnung) | Gruenbruecke ab ca. 3 Mio. EUR - Analyse ist Bruchteil der Fehlinvestition |

**Kosten & Break-even:** Fixkosten sind Entwicklung und Hosting/GIS-Infrastruktur; variable Kosten je Report gering (Analyse-Zeit). Break-even als kleines Team realistisch bei wenigen Betriebs-Lizenzen plus einigen Analyse-/Beratungsauftraegen (ca. 40-80 TEUR Umsatz). Hebel: Eine einzelne vermiedene Fehlplanung oder gut platzierte Querungshilfe rechtfertigt die Analyse-Kosten um Groessenordnungen. Herausforderung ist nicht die Technik, sondern genug qualitativ hochwertige Meldungen (Datendichte) und der Zugang zu Strassenbauverwaltungen.

**Passende Foerderung**

- Bundesprogramm Wiedervernetzung (BMUV/BfN) - Querungshilfen und begleitendes Monitoring.
- Bundesprogramm Biologische Vielfalt (BfN) - innovative Datengrundlagen fuer Artenschutz.
- DBU - Umwelttechnik/Digitalisierung, Verkehr und Natur.
- Prototype Fund fuer den offenen Plattform-Kern.
- EU LIFE - Natur/Biodiversitaet und Wiedervernetzung.
- Forschungsmittel BASt / Verkehrssicherheitsprogramme (Vision Zero), Laender-Strassenbau.
- Deutsche Postcode Lotterie - Projekte fuer Wildtier-/Artenschutz.

**Vorbilder:** Projekt Roadkill (BOKU Wien) - Citizen-Science-Hotspot-Analyse von Wildunfaellen, mehrfach ausgezeichnet, Tierfund-Kataster des Deutschen Jagdverbands (DJV) mit Uni Kiel - bundesweite Erfassung, GBIF-Anbindung, als Partner nicht Konkurrent, SPOTTERON (betreibt u.a. die Roadkill-App) als Plattform-Betriebsmodell-Beleg, diverse Roadkill-Melde-Apps international (z.B. in UK/USA) als Markt-Beleg, GBIF Deutschland als Ziel-Dateninfrastruktur

**Naechste Schritte (90 Tage)**

- Melde-MVP bauen (PWA + Karte), Datenmodell GBIF-/Tierfund-Kataster-kompatibel, Doppelerfassung vermeiden.
- Daten-/Kooperationspartner sichern: Landesjagdverband oder DJV (Tierfund-Kataster), ggf. Polizei-Meldewege.
- Einen Landesbetrieb Strassenbau oder Landkreis als Pilot gewinnen, moeglichst gefoerdert (Bundesprogramm Wiedervernetzung).
- Hotspot-Analyse-Methodik entwickeln und mit vorhandenen Daten validieren (raeumlich-zeitliche Statistik, Saisonalitaet Amphibien).
- Offenes Repo + Doku veroeffentlichen, auf openCode einstellen (Nachnutzung, Prototype-Fund-faehig).
- Pilot-Report zu einer konkreten Massnahmen-Empfehlung zuspitzen und als Referenz an weitere Strassenbauverwaltungen tragen.

> ⚠️ **Risiken:** Datendichte/Melde-Bias: Meldungen haeufen sich dort, wo viele Menschen unterwegs sind - ohne Bias-Korrektur entstehen Schein-Hotspots; Methodik muss Verkehrsstaerke/Erfassungsaufwand beruecksichtigen, sonst Fehlpriorisierung millionenschwerer Massnahmen. KI-Arterkennung hat Fehlerraten - fuer gerichtsfeste/haushaltsrelevante Entscheidungen Experten-Validierung noetig, keine Auto-Entscheidung. Datenschutz: Unfall-/Standort- und ggf. Personendaten DSGVO-konform; Polizei-Daten unterliegen Sonderregeln. Konkurrenz/Doppelstruktur zum etablierten Tierfund-Kataster - unbedingt Kooperation/Datenaustausch statt Parallel-Kataster. Behoerden-Beschaffungszyklen lang und Budgets im Strassenbau langfristig gebunden; Abhaengigkeit von Foerdermitteln vermeiden.

**Quellen:** [Tierfund-Kataster des DJV - App gegen Wildunfaelle](https://www.jagdverband.de/tierfund-kataster-app-gegen-wildunfaelle) · [Tierfund-Kataster bei GBIF Deutschland](https://land.gbif.de/datenschaetze/tierfundkataster/) · [Projekt Roadkill (BOKU Wien)](https://roadkill.at/ueber-projekt-roadkill) · [Projekt Roadkill / SPOTTERON](https://www.spotteron.net/de/citizen-science-apps/regionale-community-science-projekte/projekt-roadkill) · [Bundesprogramm Wiedervernetzung (BMUV) - Gruenbruecken/Kosten](https://www.bundesumweltministerium.de/fileadmin/Daten_BMU/Download_PDF/Naturschutz/bundesprogramm_wiedervernetzung_beispiel_kiebitzholm_bf.pdf) · [Gruenbruecke A8 Merklingen - 3,4 Mio. EUR (Beispiel Kosten)](https://www.baden-wuerttemberg.de/de/service/presse/pressemitteilung/pid/freigabe-der-gruenbruecke-an-der-a-8-bei-merklingen-1) · [Vergaberecht 2026 - neue Wertgrenzen](https://subreport.de/blog/vergaberecht-2026-neue-spielraeume-neue-unsicherheiten/)

---


## Beratung & Planung

### PrioritaetsPlaner - Open-Source-GIS-Beratung fuer wirksamen Naturschutz pro Euro

Markt **A** · Ertrag 4/5 · Aufwand 2/5 · MVP 1-2 Monate (QGIS/prioritizr-Workflow + ein Referenz-Datensatz + Angebotsvorlage) · `prioritaetsplaner-beratung`

**Beratung plus Open-Source-GIS (QGIS, prioritizr, Zonation), die Kommunen und Naturschutzverbaenden zeigt, wo Schutz und Renaturierung pro Euro am meisten bringen - samt Biotopverbund-Konzept und Foerdermittel-Antragshilfe.**

_Problem:_ Naturschutzbudgets sind knapp und werden oft nach Bauchgefuehl oder Verfuegbarkeit von Flaechen verteilt statt nach Wirkung. Kommunen und Verbaende muessen zunehmend liefern: kommunale Biotopverbundplanung, Umsetzung der nationalen Biodiversitaetsstrategie, das EU-Renaturierungsgesetz (NRL) mit verbindlichen Wiederherstellungszielen und die Verwendung zweckgebundener Ersatzzahlungen nach Paragraf 15 BNatSchG. Ihnen fehlen GIS-Fachkompetenz, eine systematische Methode und die Kapazitaet fuer tragfaehige Foerderantraege - die Mittel bleiben teils ungenutzt oder schlecht eingesetzt.

_Loesung:_ Eine Beratung, die systematic conservation planning praxistauglich macht: Mit QGIS (gratis) und den Optimierern prioritizr (exakte ILP, garantiert optimal), Marxan und Zonation werden aus Arten-/Habitatdaten und realistischen Kostenschichten die kosteneffizientesten Flaechen fuer Schutz, Renaturierung und Biotopverbund berechnet - nachvollziehbar, in mehreren Szenarien, mit Konnektivitaet als Nebenbedingung. Ergebnis sind entscheidungsreife Karten, ein Biotopverbund-/Trittstein-Konzept und fertige Bausteine fuer Foerderantraege. Die genutzte Software ist Open Source; verkauft wird die Fachleistung (Daten, Optimierung, Interpretation, Antragshilfe) sowie Support fuer ein QGIS-Plugin, das den Workflow fuer Behoerden reproduzierbar macht.

**Zugang zur oeffentlichen Hand**

- Kommunen und Landkreise fuer kommunale Biotopverbund- und Gruenflaechenkonzepte - Direktauftrag unter Wertgrenze (je nach Bundesland oft bis 10.000 EUR formfrei) oder Verhandlungsvergabe bis ca. 100.000 EUR.
- Untere und obere Naturschutzbehoerden sowie Landesaemter fuer Umwelt bei Priorisierung und Mittelverwendung (Ersatzzahlungen Paragraf 15 BNatSchG).
- Naturschutzverbaende, Stiftungen und Naturschutzfonds der Laender als Auftraggeber und Multiplikatoren.
- Regionalverbaende/Planungsregionen fuer NRL-Umsetzung und laenderuebergreifende Biotopverbundachsen (Rahmenvertrag moeglich).
- Als Nachauftragnehmer etablierter Landschaftsplanungsbueros, die die Priorisierungs-/GIS-Kompetenz zukaufen.

**Open-Source-Hebel:** Open Source ist hier doppelt Vorteil: QGIS/prioritizr/Zonation sind gratis und quelloffen (keine Lizenzkosten, Public Money Public Code, digitale Souveraenitaet, kein Vendor-Lock-in), und offene, nachvollziehbare Optimierung macht die Priorisierung gerichtsfest und politisch verteidigbar (kein Blackbox-Vorwurf). Geld kommt nicht aus der Software, sondern aus der knappen Kompetenz: gute Eingangsdaten, richtige Modellierung, belastbare Interpretation, Antragshilfe und Plugin-Support (Open-Core-Beratung).

**3D-Druck-Hebel:** Dieses Projekt ist Beratung/Software und nutzt keinen 3D-Druck - der Kern ist Fachleistung auf offener Software. Falls physische Ergebnisse gebraucht werden (Modelle, haptische Planungskarten, Gelaende-/Trittstein-Modelle fuer Buergerbeteiligung), lassen sich diese guenstig 3D-drucken und als Zusatzleistung anbieten; ansonsten bewusst kein Druck-Hebel.

**Geschaeftsmodell:** B2G-Dienstleistung auf Open-Core-Basis: Die Software ist frei, verkauft wird die knappe Fachkompetenz (Datenaufbereitung, Optimierung, Interpretation, Antragshilfe, Schulung) zu Tagessaetzen und als gefoerderte Konzepte. Wiederkehrender Umsatz aus Plugin-Support, Datenpflege und Rahmenvertraegen. Niedrige Kapitalbindung, hohe Marge - das Geschaeft existiert als Planungsbuero-Markt bereits (Marktreife A), die Differenzierung ist der explizite Kosten-pro-Wirkung-Ansatz plus offene, reproduzierbare Methodik.

**Einnahmequellen**

- Beraterhonorar/Tagessaetze fuer Priorisierungs- und Biotopverbund-Projekte.
- Gefoerderte Konzepte (Honorar aus dem Foerderbudget der Kommune/des Verbands).
- Foerdermittel-Antragshilfe (Erfolgs-/Pauschalhonorar fuer Antragsbegleitung).
- Schulungen/Workshops in QGIS und systematic conservation planning fuer Behoerdenpersonal.
- Support-/Pflegevertrag fuer ein Open-Source-QGIS-Plugin (Priorisierungs-Workflow reproduzierbar) und wiederkehrende Datenupdates.

| Preis / Kennzahl | Wert |
|---|---|
| Tagessatz Beratung/GIS | ca. 700-1.200 EUR/Tag (Richtwert freie Umwelt-/Planungsleistung) |
| Priorisierungs-/Biotopverbund-Konzept (Kommune) | ca. 8.000-40.000 EUR je nach Flaeche und Datenlage |
| Foerdermittel-Antragshilfe | ca. 1.500-6.000 EUR pro Antrag (oder Erfolgshonorar) |
| QGIS-Schulung (2 Tage, bis 10 Personen) | ca. 2.500-4.500 EUR |
| Plugin-Support/Datenpflege | ca. 2.000-6.000 EUR/Jahr |

**Kosten & Break-even:** Sehr geringe Fixkosten (Software gratis, nur Rechner, Daten, Weiterbildung, Akquise) - das ist der Charme. Als Soloselbststaendige(r) traegt es sich bei grob 60-100 fakturierten Tagen/Jahr (ca. 50-100 TEUR Umsatz), erreichbar mit 2-4 Konzept-Projekten plus Schulungen jaehrlich. Break-even praktisch ab dem ersten groesseren Konzept. Engpass ist Akquise/Reputation und die Datenbeschaffung, nicht die Kosten; Risiko ist Auslastungsschwankung (Projektgeschaeft), das ueber Support-Vertraege und Rahmenvertraege geglaettet wird.

**Passende Foerderung**

- Bundesprogramm Biologische Vielfalt (BfN) und chance.natur - gefoerderte Konzepte und Umsetzungsprojekte (als Auftragsgrundlage der Kommune).
- EU LIFE und EU-Mittel zur Umsetzung des Renaturierungsgesetzes (NRL) - Planungsleistungen foerderfaehig.
- DBU fuer methodische Weiterentwicklung und Transfer; Prototype Fund fuer das offene QGIS-Plugin.
- Laender-Naturschutzfonds (gespeist u.a. aus Ersatzzahlungen Paragraf 15 BNatSchG) und laenderspezifische Biotopverbund-Foerderung.
- EXIST-Gruenderstipendium fuer die Gruendungsphase.

**Vorbilder:** Landschaftsplanungs- und Umweltplanungsbueros (etablierter Markt, belegt Zahlungsbereitschaft), The Nature Conservancy (grossflaechige Marxan-Anwendung als Methodenbeleg), Marxan Solutions, prioritizr (prioritizr.net), Zonation (Werkzeug-/Methodenanbieter), GIS-/Fernerkundungs-Dienstleister und Oekologie-Consultings im B2G-Geschaeft

**Naechste Schritte (90 Tage)**

- Referenz-Workflow bauen: QGIS + prioritizr an einem echten Beispieldatensatz (ein Landkreis) durchrechnen und als Fallbeispiel dokumentieren.
- Angebotsvorlage und 1-Seiten-Leistungsbeschreibung fuer Direktauftrag unter Wertgrenze erstellen.
- Netzwerk aktivieren: eine Kommune/einen Naturschutzverband als Pilot gewinnen (idealerweise gefoerdert).
- Methodik mit einer Naturschutzbehoerde abstimmen (Datenquellen, Zielsetzung, Nachvollziehbarkeit).
- Open-Source-QGIS-Plugin als Minimalversion veroeffentlichen (Reichweite, Prototype-Fund-faehig).
- Aus dem Pilot eine Fallstudie machen, Schulungsangebot ergaenzen und an weitere Kommunen/Regionalverbaende ausrollen.

> ⚠️ **Risiken:** Scheingenauigkeit: optisch ueberzeugende Karten auf schwacher Datenbasis legitimieren Fehlinvestitionen - Datenqualitaet, Kostenmodell und Umsetzbarkeit/Akzeptanz muessen ehrlich eingeordnet werden, sonst Reputationsschaden. Projektgeschaeft schwankt (Auslastung, Zahlungsziele der oeffentlichen Hand). Etablierte Planungsbueros sind Wettbewerb und zugleich moegliche Partner; Zugang zu aktuellen Arten-/Habitatdaten ist oft der Flaschenhals. Keine 3D-Druck-Komponente - das Profil weicht bewusst vom Hardware-Fokus ab. Abhaengigkeit von einzelnen Grossauftraegen ueber Support-Vertraege und mehrere Kunden streuen.

**Quellen:** [QGIS - Open-Source-GIS (OSGeo)](https://www.osgeo.org/projects/qgis/) · [prioritizr - Systematic Conservation Prioritization in R](https://prioritizr.net/) · [Marxan Solutions - What is Marxan](https://marxansolutions.org/what-is-marxan/) · [BBN - Eckpunkte Honorare freiberuflicher Naturschutz (PDF)](https://www.bbn-online.de/fileadmin/AK_Freie_Berufe/Honorare_10-10-20.pdf) · [Paragraf 15 BNatSchG - Verursacherpflichten und Ersatzzahlung (dejure.org)](https://dejure.org/gesetze/BNatSchG/15.html) · [Bundesprogramm Biologische Vielfalt (BfN)](https://www.bfn.de/bundesprogramm-biologische-vielfalt) · [Schwellenwerte und Wertgrenzen im Vergaberecht (Baden-Wuerttemberg, Juni 2024)](https://wm.baden-wuerttemberg.de/fileadmin/redaktion/m-wm/intern/Dateien_Downloads/Wirtschaftsstandort/Schwellenwerte_Wertgrenzen_Vergaberecht_Stand_Juni_2024.pdf)

---
