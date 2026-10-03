# WildAuge — KI-Auswertedienst fuer Kamerafallen — Pitch & Foerderantrag

> Soloselbststaendige Gruendung (Nebenerwerb mit Wachstumsziel): Cloud-/KI-Dienst, der Behoerden, Forst, Jagd und Gutachtern das manuelle Sichten riesiger Kamerafallen-Bildmengen abnimmt und pruefbare Artenlisten liefert. Offene Auswerte-Pipeline (MegaDetector), 3D-gedruckte Halterungen.

---

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
Kamerafallen sind in Monitoring, Wildmanagement und Gutachten Standard — eine Kamera liefert in einer Saison leicht **10.000 bis 50.000 Bilder**, davon oft **60 bis 80 Prozent Leer- oder Fehlausloesungen** (Wind, Gras). Das Sichten bindet tagelang Fachpersonal, das wegen Kartierer-Mangel kaum verfuegbar ist. **WildAuge** ist ein schlanker Dienst: Bilder hochladen (Upload, SD-Karte oder Postversand), die offene KI-Pipeline (MegaDetector V6 + Artbestimmung) filtert Leerbilder weg, zaehlt und sortiert und erzeugt einen behoerdentauglichen Report mit Artenliste, Aktivitaetsmuster, Fundkarte und Beleg-Thumbnails. Menschen-Treffer werden automatisch unkenntlich gemacht. Die Pipeline ist Open Source — pruefbar, vergabefreundlich, ohne Lock-in.

### Das Problem (mit Zahlen)
- Kamerafallen erzeugen **10.000–50.000 Bilder je Kamera und Saison**, davon **60–80 % Leer-/Fehlausloesungen**.
- Manuelles Sichten bindet tagelang Fachpersonal — das wegen **Kartierer- und Taxonomen-Mangel** kaum zu bekommen ist.
- Regulatorische Treiber: **Wolfs- und Luchs-Monitoring** nach FFH-Richtlinie, Nachweis **invasiver Arten** (Waschbaer, Marderhund, Nutria; EU-Verordnung 1143/2014 Frueherkennung), **Erfolgskontrolle von Ausgleichsmassnahmen** nach BNatSchG, **Wildbestandserfassung** fuer die Abschussplanung.
- Die vorhandene offene KI (MegaDetector) ist stark, aber Behoerden und kleine Bueros haben **weder Server noch Know-how**, sie produktiv und pruefsicher zu betreiben.

### Die Loesung
Kunde laedt Bilder hoch (Upload/SD-Karte/Postversand). Die Pipeline aus dem offenen **MegaDetector V6** (Tier/Mensch/Fahrzeug-Trennung, filtert Leerbilder) plus nachgeschalteter **Artbestimmung** sortiert, zaehlt und erstellt einen behoerdentauglichen Report: Artenliste, Aktivitaetsmuster, Fundkarte, Beleg-Thumbnails. **Mensch-Treffer werden zum Datenschutz automatisch unkenntlich gemacht.** Die gesamte Auswerte-Pipeline ist Open Source (MegaDetector ist MIT-lizenziert). Ergaenzend gibt es **3D-gedruckte, vandalismusarme Kamera-Gehaeuse, Baum-/Pfahl-Halterungen und Sicht-Blenden** gegen Fehlausloesung. Verkauft wird die gepruefte Auswertung je Bildpaket plus optional Hardware.

### Markt & Kunde (oeffentliche Hand)
- **Untere Naturschutz- und Jagdbehoerden** (Landkreise): **Direktauftrag unter Vergabeschwelle** — vielerorts formfrei oder Verhandlungsvergabe ohne Teilnahmewettbewerb (groessenordnungsmaessig bis ca. 15.000 EUR; Landesvergaberecht/kommunale Wertgrenze im Einzelfall pruefen).
- **Landesforstbetriebe und Landesanstalten fuer Wald/Jagd:** Rahmenvertrag ueber mehrere Reviere/Saisons.
- **Nationalpark-, Biosphaeren-, Naturpark-Verwaltungen:** laufendes Wildtier-Monitoring (Wolf/Luchs/Wildkatze).
- **Landesumweltaemter:** Monitoring invasiver Arten (EU-VO 1143/2014).
- **Planungs-/Gutachterbueros** als Nachauftragnehmer, die Bildmassen zukaufen.
- **Zugangsstrategie:** Einstieg ueber EIN gefoerdertes Pilot mit einer Behoerde/einem Nationalpark (Referenz vor Umsatz), Ergebnis als Fallstudie fuer Ausschreibungen.

### Geschaeftsmodell & Finanzen
B2G-Dienstleistung + Open-Core/Hardware+Service. Preismodell (Spannen):

| Leistung | Preis (ca.) |
|---|---|
| Auswertung pro 1.000 Bilder | 15–40 EUR (KI-Sortierung + Report-Anteil) |
| Kamera-Saison pauschal (inkl. Report) | 120–250 EUR pro Kamera |
| SaaS-Abo Behoerde (bis 20–50 Kameras) | 2.000–6.000 EUR/Jahr |
| 3D-Gehaeuse + Halterung | 25–45 EUR/Set (Material ~5–10 EUR) |
| Fach-Validierung/Gutachten-Zuschlag | 60–90 EUR/Stunde |

**Umsatzstroeme:** Auswertung je Bildpaket, SaaS-Jahresabo, Hardware, Fach-Validierung, Schulung/Support.
**Break-even:** Sehr niedrige Fixkosten (Cloud-GPU nur bei Last zuschaltbar, Modell kostenlos, schlankes Portal). Hauptaufwand sind Vertrieb und Fach-QS-Zeit. Als Soloselbststaendige/r realistisch bei **ca. 10–20 Behoerden-/Buero-Kunden im Jahresabo** bzw. dem Aequivalent von **rund 1,5–3 Mio. ausgewerteten Bildern/Jahr**. Der erste Pilotauftrag deckt die MVP-Entwicklung. Marginale Kosten pro Bild sind nach KI-Automatisierung sehr klein — das Modell skaliert gut.

### Warum Open Source + 3D-Druck
MegaDetector ist offen und MIT-lizenziert und laeuft bereits in **ueber 80 Naturschutzprogrammen weltweit** — das macht die Methode nachvollziehbar, pruefbar und damit behoerden- und gerichtsfest. "Public Money — Public Code" und digitale Souveraenitaet sprechen fuer offene Verfahren; fehlendes Vendor-Lock-in erleichtert die Vergabe und baut Vertrauen auf. Verdient wird nicht an der Software, sondern am Betrieb der Pipeline, an der gepruefen Auswertung mit Fach-QS und am Report.
3D-gedruckt werden wetterfeste Kamera-Gehaeuse (ASA/PETG, UV-fest), diebstahlhemmende Baum-/Pfahl-Halterungen, Neigungs-Adapter und Sicht-Blenden — Stueckkosten wenige Euro Material statt teurer Metall-Security-Boxen (30–80 EUR im Handel). On-demand, lokal reparierbar; die Fertigung laesst sich an eine **Inklusions-/Behindertenwerkstatt** vergeben (sozialer Vergabe-Bonus).

### Traktion & naechste 90 Tage
- MVP: MegaDetector-V6-Pipeline + Upload-Portal + automatischer PDF-Report mit Artenliste und Fundkarte (Ziel: 6–10 Wochen).
- Mensch-Anonymisierung und DSGVO-Workflow fest einbauen.
- Report-Vorlage mit einer unteren Naturschutzbehoerde abstimmen (behoerdentauglich, pruefbar).
- LOI fuer ein gefoerdertes Pilot mit einer Behoerde/einem Nationalpark/Forstamt einwerben.
- Open-Source-Repo + Doku veroeffentlichen; erstes 3D-Gehaeuse-Set drucken und testen.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: Prototype Fund** (BMBF, Open Knowledge Foundation Deutschland). Begruendung: Der Innovationskern ist die **offene, produktionsreife Auswerte-Pipeline** — die "letzte Meile" von rohen Bildmassen zu einem pruefbaren, datenschutzkonformen Behoerden-Report (MegaDetector-Integration, Artbestimmung, automatische Menschen-Anonymisierung, Fundkarte, Export). Das ist genau die Art quelloffener Software-Prototyp, die der Prototype Fund foerdert. Foerderrahmen: **bis ca. 47.500 EUR fuer rund 6 Monate** Teilzeit-Einzelfoerderung, kein Eigenanteil-Zwang — passend fuer eine Soloselbststaendige Gruendung. Die Marktreife ist hoch (A), weil die Grundtechnik (MegaDetector) bereits etabliert ist; das Vorhaben macht sie behoerdentauglich.

**Alternative: DBU (Deutsche Bundesstiftung Umwelt)**, Umwelttechnik/Digitalisierung. Begruendung: Fuer ein groesseres Feld-Pilot mit mehreren Behoerden/Forstbetrieben, Hardware-Kleinserie (3D-Gehaeuse, Halterungen, vorkonfigurierte Kameras) und laengerer Erprobung passt der groessere, laengere DBU-Rahmen besser (mittlere fuenf- bis sechsstellige Summen ueber 1–3 Jahre, mit Eigenanteil). Das BfN-Bundesprogramm Biologische Vielfalt ("innovative Monitoring-/Arterfassungs-Ansaetze") ist eine weitere Option fuer die Skalierungsphase. **Strategie:** Prototype Fund fuer die offene Pipeline, DBU/BfN anschliessend fuer Pilot + Hardware.

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**WildAuge — offene Auswerte-Pipeline fuer Kamerafallen im behoerdlichen Monitoring.** Ziel ist ein quelloffener, reproduzierbarer Dienst, der grosse Kamerafallen-Bildmengen automatisiert verarbeitet: MegaDetector V6 trennt Tier/Mensch/Fahrzeug und filtert Leerbilder, eine nachgeschaltete Artbestimmung sortiert und zaehlt, und ein Report-Generator erzeugt eine pruefbare Artenliste mit Aktivitaetsmuster, Fundkarte und Beleg-Thumbnails. Menschen-Treffer werden technisch unkenntlich gemacht (DSGVO). Behoerden, Forst, Jagd und Gutachter sparen so Tage manueller Sichtung bei nachvollziehbarer, vergabefreundlicher Methodik. Ergaenzend entstehen offene Bauplaene fuer 3D-gedruckte, vandalismusarme Kamera-Gehaeuse und Halterungen. Alle Ergebnisse erscheinen unter OSI-konformer Lizenz.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Kamerafallen sind Standardwerkzeug im Natur- und Wildtiermonitoring, erzeugen aber Datenmengen, die manuell kaum noch zu bewaeltigen sind (10.000–50.000 Bilder je Kamera/Saison, 60–80 % davon unbrauchbar). Gleichzeitig steigen rechtlich getriebene Monitoring-Pflichten (FFH-Arten wie Wolf/Luchs/Wildkatze, EU-Frueherkennung invasiver Arten, Ausgleichs-Erfolgskontrolle, Abschussplanung). Die beste offene KI (MegaDetector) existiert, ist aber ohne Betrieb, Report-Aufbereitung, Datenschutz-Workflow und Fach-QS fuer Behoerden nicht nutzbar. Es fehlt die offene, pruefsichere "letzte Meile".

### Projektziele & Innovationsgehalt (was ist neu/offen)
- **Produktionsreife offene Pipeline:** von Bildmasse zu pruefbarem Report in einem reproduzierbaren Workflow (nicht nur Modell, sondern Betriebskette).
- **Datenschutz by design:** automatische Anonymisierung von Menschen-Treffern als fester Bestandteil.
- **Behoerdentauglichkeit/Gerichtsfestigkeit:** transparente Konfidenz je Nachweis, Fach-QS-/Stichproben-Validierungs-Workflow, nachvollziehbare Export-Formate.
- **Offene Hardware-Doku:** 3D-druckbare, vandalismusarme Gehaeuse/Halterungen/Sicht-Blenden als Bauplan.
- **Reproduzierbarkeit:** versionierte Modelle/Konfiguration fuer vergleichbare Zeitreihen ueber Jahre.

### Arbeitspakete

**AP1 — Anforderungen & Report-Spezifikation.** Ziel: behoerdentaugliche Report-Vorgaben. Inhalt: Abstimmung mit mind. einer unteren Naturschutz-/Jagdbehoerde, Pflichtfelder, Konfidenz-Darstellung, Export-Formate (PDF/CSV). Deliverable: Anforderungsdokument + Report-Spezifikation. Dauer: 1 Monat.

**AP2 — Kern-Pipeline (Detektion & Filterung).** Ziel: zuverlaessige Leerbild-Filterung und Tier/Mensch/Fahrzeug-Trennung. Inhalt: MegaDetector-V6-Integration, Batch-Verarbeitung, Konfidenz-Scoring, versionierte Konfiguration. Deliverable: lauffaehige Open-Source-Pipeline (CLI/Service) mit Testdaten. Dauer: 1,5 Monate.

**AP3 — Artbestimmung + Datenschutz/Anonymisierung.** Ziel: Arten zaehlen, Menschen schuetzen. Inhalt: nachgeschaltete Artbestimmung (inkl. invasiver Arten), automatische Unkenntlichmachung von Menschen-Treffern, DSGVO-Workflow. Deliverable: Artbestimmungs- + Anonymisierungs-Modul mit Doku. Dauer: 1,5 Monate.

**AP4 — Upload-Portal, Report & Fundkarte.** Ziel: nutzbarer Dienst. Inhalt: schlankes Upload-Portal, automatischer PDF-/CSV-Report, Artenliste, Aktivitaetsmuster, Fundkarte, Beleg-Thumbnails. Deliverable: Portal + Report-Generator + Beispielreport. Dauer: 1,5 Monate.

**AP5 — Hardware-Doku, Veroeffentlichung, Pilot-Validierung.** Ziel: offener Gesamtstand + Praxisbeleg. Inhalt: 3D-Gehaeuse/Halterungs-Bauplaene drucken/testen, Repo/Doku/Lizenz veroeffentlichen, Pilot-Datensatz einer Behoerde auswerten und Report validieren. Deliverable: oeffentliches Repo (Release v0.1) + validierte Pilot-Fallstudie. Dauer: 1 Monat (teils parallel).

### Zeit- & Meilensteinplan (Monat 0–6; Prototype-Fund-Rahmen)
- Monat 0–1: AP1. **M1 (Ende M1):** Report-Spezifikation mit Behoerde abgestimmt.
- Monat 1–2,5: AP2. **M2 (Ende M2,5):** Leerbild-Filterung + Tier/Mensch-Trennung auf Testdaten reproduzierbar.
- Monat 2,5–4: AP3. **M3 (Ende M4):** Artbestimmung + automatische Menschen-Anonymisierung stehen (DSGVO-sicher).
- Monat 4–5,5: AP4; Monat 5–6: AP5. **M4 (Ende M6):** oeffentliches Release v0.1 + validierte Pilot-Fallstudie einer Behoerde.

### Kosten- & Finanzierungsplan (Prototype Fund, 6 Monate Teilzeit)

| Position | Betrag (EUR) |
|---|---|
| Personal (Entwicklung/Konzeption, Teilzeit 6 Monate, Soloselbststaendig) | 38.000 |
| Sachkosten/Material (Cloud/GPU bei Last, Hosting, Portal-Infrastruktur) | 2.500 |
| Hardware (Testkameras, 3D-Druck-Material fuer Gehaeuse/Halterungen) | 1.500 |
| Fremdleistung (Fach-Validierung Artbestimmung, DSGVO-/Behoerden-Review) | 4.000 |
| Reise (Behoerden-Abstimmung, Pilot) | 1.000 |
| **Summe** | **47.000** |
| Foerderquote | 100 % (Prototype Fund, bis ca. 47.500 EUR); kein Eigenanteil erforderlich |

*Hinweis: Betraege als realistische Spanne; Positionen je nach aktuellen Prototype-Fund-Vorgaben der laufenden Runde anpassen. DBU-Alternative (Pilot + Hardware-Kleinserie): deutlich groesseres Budget ueber 1–3 Jahre mit ueblichem Eigenanteil.*

### Verwertung & Tragfaehigkeit nach Foerderende
Nach der Foerderung traegt sich der Dienst ueber das kommerzielle Modell: Auswertung je Bildpaket (15–40 EUR/1.000 Bilder bzw. 120–250 EUR/Kamera-Saison), wiederkehrende SaaS-Jahresabos (2.000–6.000 EUR), 3D-Hardware und Fach-Validierung. Die sehr niedrigen marginalen Kosten pro Bild und die geringe Fixkostenbasis (bedarfsgesteuerte Cloud-GPU) machen das Modell schnell profitabel. Die validierte Pilot-Fallstudie oeffnet Direktauftraege unter Vergabeschwelle und Rahmenvertraege. Break-even bei ca. 10–20 Abo-Kunden.

### Open-Source-/Gemeinwohl-Bezug
Die gesamte Auswerte-Pipeline, Report-Vorlagen, Anonymisierungs-Modul und Hardware-Designs werden unter OSI-konformer Lizenz veroeffentlicht (Software z.B. MIT/Apache-2.0 — passend zur MIT-Lizenz von MegaDetector; Hardware z.B. CERN-OHL; Doku CC BY). Oeffentliches Git-Repo mit Issue-Tracker und Beitragsleitfaden. Das Vorhaben setzt "Public Money — Public Code" um: nachnutzbare, pruefbare Monitoring-Infrastruktur statt Blackbox — vergabefreundlich und ohne Lock-in.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
Angestrebt werden als Pilotpartner eine **untere Naturschutz-/Jagdbehoerde** (Report-Abstimmung + realer Bilddatensatz) sowie ergaenzend ein **Nationalpark/Forstbetrieb** mit grossem Kamerafallen-Bestand. LOI-Strategie: (1) Demo mit echtem Bilddatensatz, die die Zeitersparnis (Tage manueller Sichtung → Stunden) und die Leerbild-Filterrate zeigt, (2) kostenneutrales Pilot im Foerderrahmen (Partner stellt Bilder/Fachwissen, kein Budgetrisiko, erhaelt fertigen Report), (3) schriftlicher LOI mit Zusage zur Report-Abstimmung und Referenznutzung. LOI wird dem Antrag beigelegt.

### Risiken & Gegenmassnahmen

| Risiko | Massnahme |
|---|---|
| KI-Fehlerraten (aehnliche Arten, schlechte Nachtbilder) | Konfidenz je Nachweis, Fach-/Stichproben-Validierung, transparente Fehlerprofile |
| Datenschutz bei Menschenfotos | Automatische Unkenntlichmachung "by design", DSGVO-Workflow (AP3) |
| Lange, budgetgebundene Behoerden-Vertriebszyklen | Kostenneutrales gefoerdertes Pilot, Direktauftrag unter Vergabeschwelle, frueher LOI |
| Gratis-Stufen grosser Anbieter (z.B. Wildlife Insights) | Abgrenzung ueber Behoerdentauglichkeit, Datenschutz, gepruefte Reports, lokale Naehe |
| Abhaengigkeit von Foerdermitteln | Frueh echten Auftragsumsatz; Foerderung nur fuer offene Grundlage |
| Lastspitzen/Cloud-Kosten bei grossen Uploads | Bedarfsgesteuerte GPU, Batch-Verarbeitung, Preis je Bildmenge deckt variable Kosten |

---

### Quellen
- MegaDetector (Microsoft AI for Good): https://microsoft.github.io/MegaDetector/
- Wildlife Insights: https://www.wildlifeinsights.org/
- TrapTagger (Wildeye Conservation): https://wildeyeconservation.org/traptagger/
- Trapper — open camera trap platform: https://os-conservation.org/projects/trapper/
- Prototype Fund: https://prototypefund.de/
- Bundesprogramm Biologische Vielfalt (BfN): https://www.bfn.de/bundesprogramm-biologische-vielfalt
