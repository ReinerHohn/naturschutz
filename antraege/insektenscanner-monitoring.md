# InsektenScanner — automatische Insekten-Monitoringstationen — Pitch & Foerderantrag

> Soloselbststaendige Gruendung (Nebenerwerb mit Wachstumsziel): solarbetriebene, non-letale Insekten-Monitoringstation (Kamera + KI, offenes Diopsis-/Insect-Detect-Prinzip) im 3D-gedruckten Gehaeuse. Positioniert als offener Infrastruktur-Lieferant fuer das anlaufende EU Pollinator Monitoring Scheme.

---

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
Der Insektenschwund ist politisch anerkannt und loest Monitoring-Pflichten aus: Mit dem EU-Renaturierungsgesetz und dem im Aufbau befindlichen **EU Pollinator Monitoring Scheme (EU PoMS)** muessen die Mitgliedstaaten kuenftig flaechendeckend Bestaeuber erfassen und Trends berichten. Klassisches Insektenmonitoring (Malaise-Fallen, Handfang, Mikroskopie) ist extrem arbeitsintensiv, toetet die Tiere und scheitert am Taxonomen-Mangel. **InsektenScanner** ist eine autonome, solarbetriebene Station: eine UV-beleuchtete Lockflaeche, auf der eine Kamera anfliegende Insekten tags und nachts fotografiert, und eine offene KI (Insect Detect auf YOLO-Basis), die erkennt, zaehlt und nach Gruppen klassifiziert — **ohne die Tiere zu toeten**. Hardware und KI sind Open Source; das sichert Standardisierung, Vergleichbarkeit und Berichtssicherheit ueber Jahrzehnte.

### Das Problem (mit Zahlen)
- Der Insektenschwund ist politisch anerkannt und loest **Monitoring-Pflichten** aus (EU-Renaturierungsgesetz; EU PoMS, vorbereitet durch die EU-Projekte SPRING/STING).
- Kuenftig muessen Mitgliedstaaten **flaechendeckend Bestaeuber** (Wildbienen, Schmetterlinge, Schwebfliegen, Nachtfalter) erfassen und Trends berichten.
- Klassisches Monitoring ist extrem **arbeitsintensiv**, **toetet** die Tiere und scheitert am **Taxonomen-Mangel**.
- Kostenvergleich: klassisches Insektenmonitoring oft **500–1.500 EUR je Malaise-Standort plus hohe Bestimmungskosten** — und dennoch punktuell.
- Es fehlt eine guenstige, **non-letale, standardisierte, automatisierbare** Methode mit grossem Datendurchsatz.

### Die Loesung
Eine autonome Station nach offenem Vorbild (Diopsis-Kamera / UKCEH AMI-System / Insect Detect): eine UV-beleuchtete Lockflaeche, auf der eine Kamera anfliegende Insekten tags und nachts fotografiert; eine offene KI (z.B. Insect Detect auf YOLO-Basis) erkennt, zaehlt und klassifiziert nach Gruppen. **Die Tiere werden nicht getoetet.** Daten laufen in ein Dashboard mit Abundanz-Zeitreihen, Diversitaets-Indizes und Report. Hardware-Design (inkl. 3D-gedrucktem Gehaeuse) und KI-Pipeline sind Open Source. Verkauft werden fertige, kalibrierte Stationen, Betrieb und Auswertung. Insect Detect ist bereits als offene DIY-Loesung publiziert und dient als technische Basis.

### Markt & Kunde (oeffentliche Hand)
- **Landesumweltaemter/Landesanstalten**, die das EU PoMS national umsetzen muessen: **Rahmenvertrag ueber Stationsnetze** — der groesste Hebel.
- **Untere Naturschutzbehoerden** (Landkreise) fuer lokale Bestaeuber-/Bluehflaechen-Erfolgskontrolle: **Direktauftrag unter Vergabeschwelle** (groessenordnungsmaessig bis ca. 15.000 EUR, Landesvergaberecht im Einzelfall pruefen).
- **Nationalpark-, Biosphaeren-, Naturpark-Verwaltungen** fuer Langzeit-Insektenmonitoring.
- **Kommunen** fuer Erfolgskontrolle eigener Bluehflaechen/Gruenanlagen (Smart-City-Umweltmonitoring).
- **Universitaeten, Senckenberg/Thuenen, Monitoring-Konsortien** als Technik-/Datenpartner und Referenzgeber.
- **Zugangsstrategie:** Einstieg ueber ein gefoerdertes **Reallabor** mit einem Land oder Nationalpark, Ergebnis als Referenz fuer die kommenden EU-PoMS-Ausschreibungen/Rahmenvertraege.

### Geschaeftsmodell & Finanzen
Open-Core + Hardware & Service mit starkem regulatorischem Rueckenwind. Preismodell (Spannen):

| Leistung | Preis (ca.) |
|---|---|
| Station (Hardware, Verkauf) | 1.200–2.500 EUR/Stueck (Material/Kamera/Solar ~400–700 EUR) |
| SaaS-Auswertung | 600–1.200 EUR pro Station und Jahr |
| Betrieb/Wartung pro Station | 300–600 EUR/Saison |
| Pilot-Netz Behoerde (10–20 Stationen + Auswertung, 1 Saison) | 20.000–40.000 EUR |
| Vergleich klassisches Insektenmonitoring | oft 500–1.500 EUR je Malaise-Standort + hohe Bestimmungskosten |

**Umsatzstroeme:** Hardware-Verkauf, jaehrliche SaaS-/Wartungsgebuehr pro Station, Betrieb/Wartung/Kalibrierung, Fach-Validierung, Schulung/Support.
**Break-even:** Hoehere Stueckkosten als eine Audio-Box (Kamera, UV, Solar, Rechenmodul), dafuer hoeherer Preis. Fixkosten moderat, variable Kosten je Station ueberschaubar. Break-even realistisch bei **ca. 30–50 aktiven Stationen im SaaS plus Wartung (ca. 40–80 TEUR wiederkehrend)**. Der grosse Hebel ist das anlaufende EU PoMS: **ein einziger Landes-Rahmenvertrag kann die Skalierung tragen.** Groesstes Risiko ist das Timing der EU-Umsetzung.

### Warum Open Source + 3D-Druck
Offene Hardware und offene KI sichern genau das, was staatliches Monitoring braucht: **Standardisierung, Vergleichbarkeit und Nachvollziehbarkeit ueber Jahrzehnte** — kein Lock-in an einen Hersteller, dessen Blackbox-Modell die Zeitreihe entwerten koennte. "Public Money — Public Code" und digitale Souveraenitaet sind politisch gewollt; offene Methodik macht die Daten wissenschaftlich und berichtssicher. Verdient wird an Hardware, Betrieb, Kalibrierung und gepruefter Auswertung, nicht an einer Lizenz.
3D-gedruckt werden Stations-Gehaeuse, Kamera-/UV-Lampen-Halter, Lockflaechen-Rahmen, Regen-/Sonnenblenden und Mast-Adapter (ASA/PETG, UV-fest): Stueckkosten wenige Euro, on-demand, lokal, reparierbar/nachruestbar — ueber viele Standorte ein echter Kostenhebel. Serienfertigung laesst sich an eine **Inklusions-/Behindertenwerkstatt** vergeben (sozialer Vergabe-Bonus).

### Traktion & naechste 90 Tage
- MVP: Kamera + UV-Lockflaeche + Insect-Detect-KI im gedruckten Gehaeuse, Dashboard mit Abundanz-Zeitreihe (Ziel: 3–5 Monate).
- Methodik an die im EU PoMS/SPRING vorgeschlagenen Standards anlehnen (Vergleichbarkeit als Verkaufsargument).
- Einen Landes-Partner oder Nationalpark als gefoerdertes Reallabor ansprechen.
- Non-letalen Ansatz und Datenschutz (keine Personen) sauber dokumentieren; Report mit einer Fachbehoerde abstimmen.
- Open-Source-Repo + Doku vorbereiten; 3D-Gehaeuse in Kleinserie testen und Stueckkosten belegen.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: Bundesprogramm Biologische Vielfalt (BfN) bzw. DBU (Deutsche Bundesstiftung Umwelt).** Begruendung: Dieses Vorhaben ist **hardware- und feldintensiv** (Kamera, UV, Solar, Rechenmodul, Lockflaeche, Dauerbetrieb, Kleinserie, Mehr-Standort-Erprobung) und zielt auf ein **Pilot-Stationsnetz mit einem Landespartner**. Insekten-/Bestaeuber-Monitoring ist thematischer Schwerpunkt des BfN-Bundesprogramms Biologische Vielfalt; die DBU foerdert passend dazu innovative Umwelttechnik/Digitalisierung. Beide bieten den fuer Hardware + Pilot noetigen groesseren, laengeren Rahmen (groessenordnungsmaessig mittlere fuenf- bis sechsstellige Summen ueber **1–3 Jahre**, mit uebl. Eigenanteil). **Regulatorischer Rueckenwind:** das anlaufende **EU Pollinator Monitoring Scheme** macht standardkonforme, offene Monitoring-Technik zu einem absehbaren Pflicht-Markt — ein starkes Foerderargument.

**Alternative: Prototype Fund** fuer die rein offene KI-/Software-Pipeline (Erkennung/Zaehlung/Klassifikation, Dashboard, Report) — **bis ca. 47.500 EUR / rund 6 Monate** Teilzeit, kein Eigenanteil. Das deckt den Software-Kern ab, aber nicht die Hardware-/Felderprobung. Weitere Optionen fuer Skalierung/Netze: **EU LIFE** sowie EU-Mittel im Umfeld von SPRING/STING und dem EU PoMS; Deutsche Postcode Lotterie fuer Biodiversitaets-Projekte; Landesprogramme Insektenschutz. **Strategie:** ggf. Prototype Fund fuer die offene Pipeline vorziehen, dann BfN/DBU fuer Hardware + Pilot-Netz; mittelfristig in EU-PoMS-Ausschreibungen hineinskalieren.

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**InsektenScanner — offene, non-letale Monitoringstation fuer das kommende EU-Bestaeuber-Monitoring.** Ziel ist eine standardisierte, solarbetriebene Kamera-KI-Station, die Insekten an einer UV-Lockflaeche tags und nachts fotografiert und mit offener KI (Insect Detect/YOLO) nach Gruppen erkennt, zaehlt und klassifiziert — ohne die Tiere zu toeten. Ein Dashboard liefert Abundanz-Zeitreihen, Diversitaets-Indizes und Report. Hardware (3D-gedrucktes, UV-festes Gehaeuse) und KI-Pipeline sind Open Source, angelehnt an die im EU PoMS/SPRING vorgeschlagenen Standards. Erprobt wird ein Pilot-Stationsnetz mit einem Landespartner/Nationalpark. So entsteht guenstiges, vergleichbares, berichtssicheres Bestaeuber-Monitoring fuer den anlaufenden EU-Pflicht-Markt — offen, ohne Hersteller-Lock-in und damit vergabefreundlich.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Der dokumentierte Insektenschwund bedroht Bestaeubungsleistung und Oekosysteme. Die EU reagiert mit dem Renaturierungsgesetz und dem in Vorbereitung befindlichen EU Pollinator Monitoring Scheme, das den Mitgliedstaaten flaechendeckendes, standardisiertes Bestaeuber-Monitoring und Trendberichte abverlangen wird. Die klassische Methodik (Malaise-Fallen, Handfang, Mikroskopie) ist teuer, letal und durch den Taxonomen-Mangel nicht skalierbar. Automatische, kamerabasierte, non-letale Systeme (Diopsis, UKCEH AMI, Insect Detect) zeigen, dass es anders geht — es fehlt aber eine offene, standardkonforme, in Deutschland betriebsreife Loesung samt Hardware, Betrieb und pruefbarer Auswertung.

### Projektziele & Innovationsgehalt (was ist neu/offen)
- **Standardkonforme offene Station:** Hardware + KI an die EU-PoMS/SPRING-Vorschlaege angelehnt, damit Daten EU-berichtssicher und ueber Jahrzehnte vergleichbar bleiben.
- **Non-letal:** Erfassung ohne Toeten der Tiere — ethisch und oekologisch ueberlegen gegenueber Fallen.
- **Offenheit gegen Blackbox-Risiko:** kein Hersteller-Lock-in, der eine Langzeit-Zeitreihe entwerten koennte; versionierte Modelle/Konfiguration.
- **Kosten-/Serienhebel:** 3D-gedruckte Gehaeuse mit belegten Stueckkosten, on-demand und reparierbar, Kleinserien-tauglich.
- **Ehrliche Aufloesung:** Klassifikation eher nach Gruppen als sicher nach Art, mit transparenter Konfidenz und Fach-Validierung von Zweifelsfaellen.

### Arbeitspakete

**AP1 — Standard- & Anforderungsanalyse (EU PoMS/SPRING).** Ziel: Methodik standardkonform ausrichten. Inhalt: Abgleich mit EU-PoMS/SPRING-Vorschlaegen, Abstimmung mit einer Fachbehoerde, Definition von Report- und Datenanforderungen. Deliverable: Methodik-/Anforderungsdokument. Dauer: 2 Monate.

**AP2 — Stationshardware (offenes Design).** Ziel: robuste, solarbetriebene Station. Inhalt: Kamera + UV-Lockflaeche + Solar/Energie + Rechenmodul, 3D-gedrucktes UV-festes Gehaeuse, Halter, Blenden, Mast-Adapter; Stueckkosten belegen. Deliverable: funktionsfaehiger Stations-Prototyp + offene Bauplaene. Dauer: 4 Monate.

**AP3 — KI-Pipeline (Erkennung, Zaehlung, Klassifikation).** Ziel: zuverlaessige non-letale Auswertung. Inhalt: Insect-Detect-/YOLO-basierte Erkennung tag/nacht, Zaehlung, Gruppen-Klassifikation, Konfidenz-Scoring, versionierte Modelle. Deliverable: offene KI-Pipeline mit Testdaten. Dauer: 4 Monate (parallel zu AP2).

**AP4 — Dashboard, Report & Fach-Validierung.** Ziel: nutzbare, pruefbare Auswertung. Inhalt: Dashboard mit Abundanz-Zeitreihe/Diversitaets-Indizes, automatischer Report, Datenschutz-Doku (keine Personen), Workflow zur taxonomischen Validierung von Zweifelsfaellen. Deliverable: Dashboard + Report-Generator + QS-Leitfaden. Dauer: 3 Monate.

**AP5 — Pilot-Stationsnetz & Veroeffentlichung.** Ziel: Praxisbeleg + offener Gesamtstand. Inhalt: Aufbau mehrerer Stationen mit Landespartner/Nationalpark ueber eine Saison, Betrieb/Wartung/Reinigung der Lockflaeche, Datenauswertung, Fallstudie; Repo/Doku/Lizenz veroeffentlichen. Deliverable: Pilot-Fallstudie + oeffentliches Repo (Release). Dauer: 6 Monate (ueberlappend, inkl. Saison).

### Zeit- & Meilensteinplan (Monat 0–12; BfN/DBU-Rahmen, Beispiel 12 Monate)
- Monat 0–2: AP1. **M1 (Ende M2):** standardkonformes Methodik-/Anforderungsdokument mit Fachbehoerde abgestimmt.
- Monat 2–6: AP2 + AP3 (parallel). **M2 (Ende M6):** funktionsfaehiger Stations-Prototyp + KI-Pipeline erkennt/zaehlt auf Testdaten.
- Monat 5–8: AP4. **M3 (Ende M8):** Dashboard + Report + Fach-Validierungs-Workflow stehen.
- Monat 6–12: AP5 (Saison). **M4 (Ende M12):** Pilot-Stationsnetz ueber eine Saison betrieben, Fallstudie + oeffentliches Release.

### Kosten- & Finanzierungsplan (BfN/DBU-Rahmen, 12 Monate; Beispiel)

| Position | Betrag (EUR) |
|---|---|
| Personal (Entwicklung/Betrieb, ~1 VZAE ueber 12 Monate bzw. Soloselbststaendig + Zuarbeit) | 90.000 |
| Sachkosten/Material (Cloud-Inferenz, Hosting, 3D-Druck-Material, Lockflaechen/Verschleiss) | 12.000 |
| Hardware (10–15 Pilot-Stationen: Kameras, UV, Solar, Rechenmodule, Elektronik) | 25.000 |
| Fremdleistung (taxonomische Fach-Validierung, Gehaeuse-Kleinserie Werkstatt, Behoerden-Review) | 18.000 |
| Reise (Aufbau/Wartung Stationsnetz, Fachabstimmung) | 5.000 |
| **Summe** | **150.000** |
| Eigenanteil (programmueblich, z.B. ca. 10 % — hier ca. 15.000; exakt nach Programm) | ~15.000 |
| Foerderquote | ca. 85–90 % (programmabhaengig; bei DBU/BfN ueblicher Eigenanteil) |

*Hinweis: Betraege als realistische Groessenordnung fuer ein einjaehriges Pilot; BfN-/DBU-Projekte koennen groesser und bis ca. 3 Jahre laufen. Eigenanteil/Foerderquote exakt nach aktuellen Programmbedingungen festlegen. Fuer die Prototype-Fund-Alternative (reine Software-Pipeline) gilt ein Rahmen bis ca. 47.500 EUR / 6 Monate ohne Eigenanteil.*

### Verwertung & Tragfaehigkeit nach Foerderende
Nach der Foerderung traegt sich das Vorhaben ueber Hardware-Verkauf (1.200–2.500 EUR/Station), wiederkehrende SaaS-/Wartungsgebuehren (600–1.200 EUR/Station/Jahr plus 300–600 EUR Wartung/Saison) und Fach-Validierung. Entscheidend ist der regulatorische Rueckenwind: Mit dem Ausbau des EU PoMS entsteht ein Pflicht-Markt, in dem ein einziger Landes-Rahmenvertrag die Skalierung tragen kann. Wer frueh standardkonforme, offene Technik liefert, wird zum Infrastruktur-Lieferanten dieses wachsenden Marktes. Break-even bei ca. 30–50 aktiven Stationen. Um Foerderabhaengigkeit zu vermeiden, wird frueh echter Auftragsumsatz (lokale Bluehflaechen-Erfolgskontrolle) gesucht.

### Open-Source-/Gemeinwohl-Bezug
KI-Pipeline, Dashboard, Report-Vorlagen und Hardware-Designs werden unter OSI-konformer Lizenz veroeffentlicht (Software z.B. MIT/Apache-2.0; Hardware z.B. CERN-OHL; Doku CC BY), aufbauend auf dem bereits offen publizierten Insect Detect. Oeffentliches Git-Repo mit Doku und Beitragsleitfaden. Das Vorhaben setzt "Public Money — Public Code" um und sichert fuer das staatliche Bestaeuber-Monitoring offene, standardisierte, vergleichbare und berichtssichere Infrastruktur — ohne Hersteller-Lock-in, der Langzeit-Zeitreihen entwerten koennte.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
Angestrebt wird als Hauptpartner ein **Landesumweltamt/eine Landesanstalt** (EU-PoMS-Umsetzung, Stationsnetz-Pilot) oder ein **Nationalpark/Biosphaerenreservat** fuer Langzeit-Monitoring, ergaenzt um einen wissenschaftlichen Referenzgeber (z.B. Universitaet, Senckenberg/Thuenen) zur Methoden-Validierung. LOI-Strategie: (1) Demo des Prototyps mit Abundanz-Zeitreihe und Kostenvergleich gegen Malaise-Monitoring, (2) Angebot eines gefoerderten Reallabors (Partner stellt Flaeche/Fachwissen, geringes Budgetrisiko, erhaelt standardkonforme Daten), (3) schriftlicher LOI mit Zusage zu Flaeche, Datenabstimmung und Referenznutzung fuer kommende EU-PoMS-Ausschreibungen. LOIs werden dem Antrag beigelegt.

### Risiken & Gegenmassnahmen

| Risiko | Massnahme |
|---|---|
| Timing-Risiko EU PoMS (verzoegerte verbindliche Umsetzung/Budgets) | Frueh lokalen Auftragsumsatz (Bluehflaechen-Erfolgskontrolle) suchen; nicht allein auf den Pflicht-Markt setzen |
| Grobe automatische Artbestimmung (eher Gruppen als Art) | Ehrlich kommunizieren, Konfidenz-Scoring, taxonomische Fach-Validierung von Zweifelsfaellen |
| Hardware-Komplexitaet (Lockflaechen-Reinigung, Vandalismus, Nacht-Energiebedarf) | Robustes UV-festes Design, Wartungskonzept/-vertrag, Energiebudget im Prototyp belegen |
| Abhaengigkeit von Foerder-/EU-Geldern | Open-Core-Service-Modell traegt den Betrieb; Foerderung nur fuer Entwicklung/Pilot |
| Lange, budgetgebundene Behoerden-Vertriebszyklen | Gefoerdertes Reallabor als Referenz, Direktauftrag unter Vergabeschwelle, frueher LOI |
| Konkurrenz durch kommerzielle Systeme (z.B. Diopsis) | Abgrenzung ueber Offenheit, Standardkonformitaet, Vergleichbarkeit, Vergabefreundlichkeit und lokale Naehe |

---

### Quellen
- SPRING — EU Pollinator Monitoring (UFZ): https://www.ufz.de/spring-pollination/
- Refined proposal for an EU Pollinator Monitoring Scheme (STING-2): https://eugreenalliance.eu/wp-content/uploads/2025/03/STING-2-report-Refined-proposal-for-an-EU-pollinator-monitoring.pdf
- Insect Detect — open-source DIY camera trap (Preprint): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10990185/
- DIOPSIS — automated insect monitoring: https://diopsis.eu/
- Bundesprogramm Biologische Vielfalt (BfN): https://www.bfn.de/bundesprogramm-biologische-vielfalt
- Prototype Fund: https://prototypefund.de/
