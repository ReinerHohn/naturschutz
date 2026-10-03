# Lauschposten — Bioakustik-Monitoring as a Service — Pitch & Foerderantrag

> Soloselbststaendige Gruendung (Nebenerwerb mit Wachstumsziel) im Bereich automatisiertes Arten-Monitoring fuer die oeffentliche Hand. Open-Source-Hardware + offene KI-Pipeline, verdient wird an Hardware, Betrieb und pruefsicherer Auswertung.

---

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
Behoerden muessen Arten erfassen — fuer FFH-Monitoring, Eingriffs- und Ausgleichskontrolle und Renaturierungs-Erfolgskontrolle. Klassische Gutachter-Begehungen kosten schnell 5.000 bis 50.000 EUR, sind punktuell und kaum wiederholbar, und es fehlen die Kartierer. **Lauschposten** ist eine solarbetriebene, wetterfeste Audio-Box (offene Elektronik auf AudioMoth-Basis, 3D-gedrucktes Gehaeuse), deren Aufnahmen durch eine offene KI-Pipeline (BirdNET fuer Voegel, batdetect2 fuer Fledermaeuse) laufen und automatisch einen behoerdentauglichen Report liefern: Artenliste, Aktivitaetsmuster, Zeitreihe, Karte. Dauerhaftes, standardisiertes, preiswertes Monitoring statt teurer Stichproben — und weil die Methodik offen ist, ist sie nachvollziehbar und vergabefreundlich.

### Das Problem (mit Zahlen)
- Rechtlich getriebener Bedarf: Arterfassung nach BNatSchG (Eingriffs-/Ausgleichskontrolle), FFH-Monitoring, Umweltvertraeglichkeitspruefung, Vorher-Nachher bei Bau und Renaturierung.
- Klassische Gutachten sind teuer: je Projekt schnell **ca. 5.000 bis 50.000 EUR**, dazu einmalig und punktuell — schlecht wiederholbar und damit schlecht fuer Trendaussagen.
- **Fachkraeftemangel** bei Kartierern und Taxonomen verschaerft die Lage: selbst wer zahlen will, findet niemanden, der kartiert.
- Es fehlt schlicht ein guenstiges, dauerhaftes, standardisiertes und wiederholbares Monitoring, das ueber Jahre vergleichbare Daten liefert.

### Die Loesung
Ein Netz robuster, solarbetriebener Audio-Rekorder (Basis: offene AudioMoth-Elektronik) im 3D-gedruckten, wetterfesten Gehaeuse (PETG/ASA, UV-fest). Die Aufnahmen laufen durch eine offene KI-Pipeline (BirdNET fuer Voegel, batdetect2 fuer Fledermaeuse) und landen in einem Dashboard mit automatischem Behoerden-Report: Artenliste, Aktivitaet, Zeitreihe, Fundkarte. Hardware-Designs und Auswerte-Pipeline sind Open Source. Verkauft werden fertige, kalibrierte Boxen, der wartungsarme Betrieb und die pruefsichere, gutachterlich verwertbare Auswertung. Datenschutz: Mitschnitt menschlicher Sprache wird technisch ausgeschlossen bzw. automatisch verworfen.

### Markt & Kunde (oeffentliche Hand)
- **Untere Naturschutzbehoerden** (Landkreise/kreisfreie Staedte): Einstieg per **Direktauftrag unterhalb der Vergabeschwelle** — vielerorts formfrei bzw. Verhandlungsvergabe ohne Teilnahmewettbewerb (groessenordnungsmaessig bis ca. 15.000 EUR, abhaengig von Landesvergaberecht und kommunaler Wertgrenze; im Einzelfall pruefen).
- **Kommunale Gruenflaechen- und Umweltaemter** fuer Vorher-Nachher-Monitoring eigener Renaturierungen.
- **Landesbetriebe Forst, Nationalpark-, Biosphaeren- und Naturpark-Verwaltungen** als **Rahmenvertrag** ueber mehrere Standorte und Saisons.
- **Planungs- und Gutachterbueros** als Nachauftragnehmer, die Dauer-Monitoring zukaufen statt selbst zu bauen.
- **Zugangsstrategie:** Einstieg ueber EIN gefoerdertes Pilot-/Reallabor mit einer Kommune (Referenz vor Umsatz), Ergebnis als Fallstudie fuer Direktauftraege und Ausschreibungen nutzen.

### Geschaeftsmodell & Finanzen
Open-Core + Hardware & Service. Preismodell (Spannen, standortabhaengig):

| Leistung | Preis (ca.) |
|---|---|
| Box (Hardware, Verkauf) | 350–600 EUR/Stueck (Material ~120–180 EUR) |
| SaaS-Auswertung | 300–600 EUR pro Box und Jahr |
| Pilotprojekt Kommune (5–10 Boxen + Report, 1 Saison) | 8.000–15.000 EUR |
| Vergleich: klassisches Gutachten | oft 5.000–50.000 EUR, einmalig/punktuell |

**Umsatzstroeme:** Hardware-Verkauf (Marge auf Material + Montage), wiederkehrende SaaS-/Wartungsgebuehr pro Box, Dienstleistung (Aufbau, Wartung, Kalibrierung, gutachterliche Einordnung), Schulung/Support.
**Break-even:** Fixkosten gering (Cloud/Server, Entwicklungszeit), variable Kosten je Box klein. Als Soloselbststaendiger realistisch bei **ca. 30–60 aktiven Boxen im SaaS (ca. 15–30 TEUR wiederkehrend)**. Der erste Pilotauftrag deckt die MVP-Entwicklung. Groesstes Risiko ist Vertriebszeit, nicht Herstellkosten.

### Warum Open Source + 3D-Druck
Open Source ist beim Staat **Verkaufsargument, nicht Hindernis**: "Public Money — Public Code" und digitale Souveraenitaet sind politisch gewollt, fehlendes Vendor-Lock-in erleichtert die Vergabe, und eine offene, nachvollziehbare Methodik macht die Daten pruefbar und damit belastbarer vor Behoerde und ggf. Gericht. Geld kommt nicht aus der Lizenz, sondern aus Hardware, Betrieb, gepruefter Auswertung und Support.
3D-Druck senkt die Gehaeuse-Stueckkosten auf wenige Euro statt teurer Spezialgehaeuse, ist lokal und on-demand produzierbar sowie leicht reparierbar/nachruestbar. Die Serienfertigung laesst sich an eine **Inklusions-/Behindertenwerkstatt** vergeben (sozialer Vergabe-Bonus, planbare Kosten).

### Traktion & naechste 90 Tage
- MVP: AudioMoth + BirdNET-Pi im gedruckten Gehaeuse, ein automatisierter PDF-Report (Ziel: 2–3 Monate).
- Erstgespraech mit mindestens einer unteren Naturschutzbehoerde, um die Report-Vorlage behoerdentauglich abzustimmen.
- Letter of Intent (LOI) fuer ein gefoerdertes Pilot mit EINER Kommune einwerben.
- Open-Source-Repo + Doku veroeffentlichen (Vertrauensaufbau, Prototype-Fund-faehig).
- 1-Seiten-Angebot + Preisliste fuer Direktauftrag unter Vergabeschwelle erstellen.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: Prototype Fund** (BMBF, umgesetzt durch die Open Knowledge Foundation Deutschland). Begruendung: Der Kern der Innovation und der groesste Gemeinwohl-Hebel ist die **offene Auswerte-Pipeline** (Integration von BirdNET + batdetect2 zu einem reproduzierbaren, behoerdentauglichen Report inklusive Datenschutz-Filter fuer menschliche Sprache). Genau solche Open-Source-Software-Prototypen sind Fokus des Prototype Fund. Foerderrahmen: **bis ca. 47.500 EUR fuer rund 6 Monate** Teilzeit-Einzelfoerderung — passend zu einer Soloselbststaendigen Gruendung und ohne Eigenanteil-Zwang.

**Alternative: DBU (Deutsche Bundesstiftung Umwelt)**, Themenfeld Umwelttechnik/Digitalisierung. Begruendung: Sobald es um die **Hardware-Entwicklung und ein groesseres Feld-Pilot** (Boxen-Kleinserie, Solar-/Gehaeuse-Dauertest, mehrere Standorte, Behoerden-Partner) geht, sprengt das Budget und Laufzeit den Prototype-Fund-Rahmen. DBU-Projekte sind typischerweise groesser und laenger (groessenordnungsmaessig mittlere fuenf- bis sechsstellige Summen ueber 1–3 Jahre, mit Eigenanteil); das BfN-Bundesprogramm Biologische Vielfalt ("innovative Monitoring-Ansaetze") ist eine weitere Option fuer die Pilot-/Skalierungsphase. **Strategie:** Mit dem Prototype Fund die offene Pipeline bauen und veroeffentlichen, mit der dadurch erzeugten Referenz anschliessend DBU/BfN fuer Hardware + Pilot anschliessen.

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**Lauschposten — offene Bioakustik-Pipeline fuer behoerdliches Arten-Monitoring.** Ziel ist eine quelloffene, reproduzierbare Auswerte-Pipeline, die Audio-Aufnahmen solarbetriebener Rekorder automatisiert zu einem pruefbaren Behoerden-Report verarbeitet: Artbestimmung von Voegeln (BirdNET) und Fledermaeusen (batdetect2), Qualitaets-/Konfidenzkennzeichnung, Aktivitaets-Zeitreihen, Fundkarte und PDF-/CSV-Export. Ein datenschutzsicherer Filter schliesst menschliche Sprache technisch aus. Die Pipeline laeuft auf guenstiger offener Hardware (AudioMoth) in einem 3D-gedruckten Gehaeuse, dessen Bauplaene mitveroeffentlicht werden. Behoerden und Bueros erhalten damit ein dauerhaftes, standardisiertes und kostenguenstiges Monitoring statt teurer punktueller Begehungen. Alle Ergebnisse (Code, Modelle-Konfiguration, Report-Vorlagen, Hardware-Designs) erscheinen unter einer OSI-konformen Lizenz.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Deutschland und die EU verpflichten die oeffentliche Hand zu umfangreicher Arterfassung (BNatSchG, FFH-Richtlinie, UVP, Renaturierungs-Erfolgskontrolle). Gleichzeitig steigen die Kosten klassischer Gutachten (5.000–50.000 EUR je Projekt) und der Fachkraeftemangel bei Kartierern macht flaechendeckendes, wiederholbares Monitoring praktisch unmoeglich. Akustisches Monitoring ist ein etablierter, non-invasiver Ansatz; die Bausteine (AudioMoth, BirdNET, batdetect2) existieren offen, sind aber fuer Behoerden weder integriert noch pruefsicher aufbereitet. Es fehlt die "letzte Meile": eine offene, reproduzierbare Pipeline, die aus Rohaufnahmen einen rechtssicher nutzbaren Report macht.

### Projektziele & Innovationsgehalt (was ist neu/offen)
- **Integration statt Insellosung:** erstmals eine zusammenhaengende, offene Pipeline von Rohaudio bis behoerdentauglichem Report (Voegel + Fledermaeuse in einem Workflow).
- **Pruefbarkeit/Gerichtsfestigkeit:** transparente Konfidenz-/Qualitaetskennzeichnung je Nachweis und Stichproben-Validierungs-Workflow durch Fachpersonen.
- **Datenschutz by design:** technischer Ausschluss menschlicher Sprache aus Aufnahmen/Analyse.
- **Offene Hardware-Doku:** 3D-druckbares, UV-festes Gehaeuse + Solar-/Mast-Adapter als Bauplan.
- **Reproduzierbarkeit ueber Jahre:** versionierte Modelle und Konfiguration, damit Zeitreihen vergleichbar bleiben (kein Blackbox-Drift).

### Arbeitspakete

**AP1 — Daten- und Report-Anforderungen (Behoerdentauglichkeit).** Ziel: wissen, was ein Report rechtssicher enthalten muss. Inhalt: Abstimmung mit mind. einer unteren Naturschutzbehoerde, Ableitung von Pflichtfeldern, Konfidenz-Darstellung, Export-Formaten. Deliverable: Anforderungsdokument + Report-Spezifikation. Dauer: 1 Monat.

**AP2 — Kern-Pipeline Audio → Nachweise.** Ziel: robuste, reproduzierbare Verarbeitung. Inhalt: Einbindung BirdNET (Voegel) und batdetect2 (Fledermaeuse), Segmentierung, Konfidenz-Scoring, versionierte Modell-/Config-Verwaltung. Deliverable: lauffaehige Open-Source-Pipeline (CLI) mit Testdaten. Dauer: 2 Monate.

**AP3 — Datenschutz-Filter + Qualitaetssicherung.** Ziel: menschliche Sprache ausschliessen, Fehlerraten beherrschen. Inhalt: Sprach-Detektion/Verwerfung, Stichproben-Validierungs-Workflow, Dokumentation der Fehlerprofile. Deliverable: Datenschutz-Modul + QS-Leitfaden. Dauer: 1 Monat.

**AP4 — Report & Dashboard.** Ziel: aus Nachweisen ein behoerdentauglicher Report. Inhalt: Artenliste, Aktivitaets-Zeitreihe, Fundkarte, PDF-/CSV-Export, schlankes Dashboard. Deliverable: automatischer Report-Generator + Beispielreport. Dauer: 1,5 Monate.

**AP5 — Hardware-Doku, Veroeffentlichung, Feldtest.** Ziel: offener, nachbaubarer Gesamtstand. Inhalt: 3D-Gehaeuse-Bauplan + Montageanleitung, Repo/Doku/Lizenz veroeffentlichen, kurzer Feldtest an 1–2 Standorten. Deliverable: oeffentliches Repo (Release v0.1) + Feldtest-Notiz. Dauer: 1 Monat (teils parallel).

### Zeit- & Meilensteinplan (Monat 0–6; Prototype-Fund-Rahmen)
- Monat 0–1: AP1. **M1 (Ende M1):** Report-Spezifikation mit Behoerde abgestimmt.
- Monat 1–3: AP2. **M2 (Ende M3):** Kern-Pipeline erkennt Voegel + Fledermaeuse auf Testdaten reproduzierbar.
- Monat 3–4: AP3. **M3 (Ende M4):** Datenschutz-Filter + QS-Workflow stehen.
- Monat 4–5,5: AP4; Monat 5–6: AP5. **M4 (Ende M6):** oeffentliches Release v0.1 mit Report-Generator und Hardware-Doku, Feldtest dokumentiert.

### Kosten- & Finanzierungsplan (Prototype Fund, 6 Monate Teilzeit)

| Position | Betrag (EUR) |
|---|---|
| Personal (Entwicklung/Konzeption, Teilzeit 6 Monate, Soloselbststaendig) | 38.000 |
| Sachkosten/Material (Cloud/Server, Hosting, Konten) | 1.500 |
| Hardware (AudioMoth-Rekorder, Solar, Elektronik, 3D-Druck-Filament/Material) | 2.500 |
| Fremdleistung (Fach-Validierung Artbestimmung, Review Behoerdentauglichkeit) | 4.000 |
| Reise (Behoerden-Abstimmung, Feldtest) | 1.000 |
| **Summe** | **47.000** |
| Foerderquote | 100 % (Prototype Fund, bis ca. 47.500 EUR); kein Eigenanteil erforderlich |

*Hinweis: Betraege als realistische Spanne; exakte Positionen je nach aktuellen Prototype-Fund-Vorgaben der laufenden Runde anpassen. Fuer die DBU-Alternative (Hardware + Pilot) ist ein deutlich groesseres Budget ueber 1–3 Jahre mit ueblichem Eigenanteil anzusetzen.*

### Verwertung & Tragfaehigkeit nach Foerderende
Die Foerderung finanziert die offene Pipeline (Gemeinwohl). Getragen wird das Vorhaben danach durch das kommerzielle Hardware+Service-Modell: Verkauf fertiger Boxen, wiederkehrende SaaS-/Wartungsgebuehr pro Box (300–600 EUR/Jahr), Aufbau/Wartung/Kalibrierung und gutachterliche Einordnung sowie Schulung/Support. Das veroeffentlichte Repo dient als Vertrauens- und Vertriebsargument; der aus dem gefoerderten Feldtest entstehende Referenzreport ermoeglicht Direktauftraege unter Vergabeschwelle und spaeter Rahmenvertraege. Break-even als Soloselbststaendiger bei ca. 30–60 aktiven Boxen.

### Open-Source-/Gemeinwohl-Bezug
Gesamter Code, Report-Vorlagen, Modell-/Konfigurations-Metadaten und Hardware-Designs werden unter einer OSI-konformen Lizenz veroeffentlicht (Software z.B. MIT/Apache-2.0; Hardware-Designs z.B. CERN-OHL; Doku CC BY). Oeffentliches Git-Repo mit Issue-Tracker und Beitragsleitfaden. Das Vorhaben setzt "Public Money — Public Code" um: aus oeffentlichen Mitteln entsteht nachnutzbare, pruefbare Infrastruktur fuer das behoerdliche Monitoring — keine Blackbox, kein Vendor-Lock-in, reproduzierbare Zeitreihen.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
Konkret angestrebt wird eine **untere Naturschutzbehoerde eines Landkreises** als Pilot- und Abstimmungspartner (behoerdentaugliche Report-Vorlage), ergaenzt um eine Nationalpark-/Biosphaeren-Verwaltung fuer einen Mehr-Standort-Feldtest. LOI-Strategie: (1) Kurz-Demo mit Beispielreport und klarer Kostenersparnis gegenueber klassischem Gutachten, (2) Angebot eines kostenneutralen Pilots im Rahmen der Foerderung (Behoerde stellt Flaeche/Fachwissen, kein Budgetrisiko), (3) schriftlicher LOI mit Zusage zur Report-Abstimmung und Nutzung als Referenz. Der LOI wird dem Antrag beigelegt.

### Risiken & Gegenmassnahmen

| Risiko | Massnahme |
|---|---|
| Lange, budgetgebundene Behoerden-Vertriebszyklen | Einstieg ueber gefoerdertes, kostenneutrales Pilot; Direktauftrag unter Vergabeschwelle; frueh LOI sichern |
| KI-Fehlerraten bei der Artbestimmung (Haftung/Gerichtsfestigkeit) | Konfidenz-/Qualitaetskennzeichnung, Stichproben-Validierung durch Fachperson, transparente Fehlerprofile |
| Datenschutz (Mitschnitt menschlicher Stimmen) | Technischer Sprach-Filter/Verwerfung "by design", dokumentiert in AP3 |
| Abhaengigkeit von Foerdermitteln | Frueh echten Auftragsumsatz anstreben; Foerderung nur fuer offene Grundlage, Service traegt den Betrieb |
| Hardware/Solar im Dauerbetrieb (Ausfall, Wetter) | UV-feste 3D-Gehaeuse, Feldtest, einfache Reparierbarkeit/Nachruestbarkeit, Wartungsvertrag |
| Konkurrenz durch etablierte Service-Anbieter | Abgrenzung ueber Offenheit, Behoerdentauglichkeit, Datenschutz und lokale Naehe |

---

### Quellen
- Open Acoustic Devices — AudioMoth: https://www.openacousticdevices.info/
- BirdNET (Cornell Lab / TU Chemnitz): https://birdnet.cornell.edu/
- Prototype Fund: https://prototypefund.de/
- DBU Foerderung: https://www.dbu.de/foerderung/
- Bundesprogramm Biologische Vielfalt (BfN): https://www.bfn.de/bundesprogramm-biologische-vielfalt
