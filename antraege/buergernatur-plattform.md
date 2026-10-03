# BuergerNatur — White-Label-Plattform fuer kommunale Citizen Science — Pitch & Foerderantrag

> Mehrmandanten-Plattform (SaaS) mit App, die jede Kommune/jedes Schutzgebiet als eigenes, gebrandetes Arterfassungs-Portal bekommt — aufgesetzt auf offene Standards (GBIF/Darwin Core, iNaturalist/observation.org), keine Dateninsel. Buerger melden Beobachtungen, die Verwaltung gewinnt daraus nutzbare Monitoring-Daten.
>
> Gruenderrolle: Soloselbststaendig/Nebenerwerb mit Wachstumsabsicht. Zahlen teils als Spanne/"ca."; Programm-Eckdaten nach allgemein bekanntem Stand, im Einzelfall vor Antragstellung zu verifizieren.

---

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
Kommunen und Schutzgebiete sollen Buerger beteiligen und gleichzeitig verlaessliche Daten ueber ihre Arten gewinnen — doch die Daten liegen in Excel, in generischen Apps oder gar nicht vor, und eine eigene Plattform zu bauen ist zu teuer. **BuergerNatur** gibt jeder Kommune/jedem Schutzgebiet ein **eigenes, gebrandetes Melde-Portal plus App** auf **offenen Standards** (Export nach GBIF im Darwin-Core-Format, Anbindung an iNaturalist/observation.org und Flora-Incognita-/Pl@ntNet-Erkennung). Buerger melden Fund, Foto, Ort; die Verwaltung bekommt gefilterte, berichtsfaehige Monitoring-Daten. Der Code ist offen; verdient wird an Einrichtung, Betrieb und Auswertung. Vorbilder: SPOTTERON (White-Label) und Naturblick.

### Das Problem (mit Zahlen)
- Kommunen, Naturparke, Biosphaerenreservate und Schutzgebiets-Verwaltungen muessen Buerger beteiligen und Daten fuer Pflegeplaene, Berichtspflichten (FFH, Natura 2000), Gruenflaechen-Monitoring, Klimaanpassung und Oeffentlichkeitsarbeit erzeugen.
- Treiber: Biodiversitaetsstrategien von Bund/Laendern/EU, Natura-2000-Managementplaene, kommunale Nachhaltigkeits-/Biodiversitaetskonzepte, Pflicht zur Buergerbeteiligung.
- In der Praxis: **keine eigene Plattform.** Daten liegen verstreut in Excel, generischen Apps oder entstehen gar nicht; eine von Grund auf gebaute Plattform ist zu teuer, und reine Fremd-Apps liefern keine kommunal nutzbaren, gefilterten Daten.
- Markt existiert nachweislich: SPOTTERON (White-Label-Citizen-Science aus Oesterreich) betreibt zahlreiche Projekte; Naturblick (Museum fuer Naturkunde Berlin) erreichte vom Berlin-Pilot aus **ca. 120.000–130.000 Nutzer** und skalierte auf ganz Deutschland — Beleg fuer Nachfrage und Skalierbarkeit.

### Die Loesung
Eine **Mehrmandanten-Plattform (SaaS)**: jede Kommune/jedes Schutzgebiet bekommt ein eigenes, gebrandetes Portal **plus App (PWA/nativ)**.
- **Offene Standards & bestehende Infrastruktur:** Arterkennung/Daten koppelbar mit iNaturalist/observation.org und Flora-Incognita-/Pl@ntNet-Erkennung; **Export nach GBIF im Darwin-Core-Standard** — keine Dateninsel.
- **Features:** Beobachtungen melden (Foto/Ton/Ort), Bestimmungshilfe, thematische Kampagnen (z.B. Wildbienen, Amphibien, Stadtbaeume), Qualitaetssicherung durch Experten, Dashboards und Export fuers kommunale Monitoring, Buergerbeteiligungs-Modul.
- **Datenschutz/Artenschutz-Geheimhaltung:** Standort-Unschaerfe/Zugriffsschutz fuer schutzwuerdige Arten (z.B. Greifvogel-Horste), DSGVO-konforme Melder-Daten.
- **Code offen;** verdient wird an Einrichtung, Betrieb und Auswertung.

### Markt & Kunde (oeffentliche Hand)
- **Kommunale Umwelt-/Gruenflaechenaemter** — **Direktauftrag** moeglich (seit 2026 oft bis ca. 50.000 EUR netto Direktauftrag, bis ca. 100.000 EUR netto Verhandlungsvergabe).
- **Naturpark-, Biosphaerenreservats- und Nationalpark-Verwaltungen** (Dauer-Monitoring, Umweltbildung) — als **mehrjaehriger Rahmenvertrag**.
- **Untere Naturschutzbehoerden und Biologische Stationen** fuer ehrenamtlich getragenes Monitoring.
- **Landes-Biodiversitaetsstrategien / Stiftungen Naturschutz der Laender** als Mehr-Standort-Auftraggeber.
- **Zugang:** Einstieg ueber ein **gefoerdertes Reallabor** mit EINER Modellkommune/einem Schutzgebiet; Referenz-Fallstudie fuer weitere. **openCode-Veroeffentlichung** macht das Portal fuer andere Kommunen nachnutzbar — Betrieb/Anpassung wird zugekauft.

### Geschaeftsmodell & Finanzen
Mehrmandanten-SaaS mit Open-Core: ein offener Plattform-Kern, je Kunde als gebrandetes Portal betrieben. Skalierung ueber viele Mandanten auf einer Codebasis — jeder weitere Mandant ist margenstark.

| Umsatzstrom | Preis (ca.) |
|---|---|
| Einrichtung je Mandant (Branding, Konfiguration, Kampagnen) | 4.000–15.000 EUR einmalig |
| Jahres-Betriebsgebuehr je Mandant (Hosting, Updates, Support) | 3.000–9.000 EUR / Jahr |
| Auswertung/Monitoring-Report | 1.500–5.000 EUR / Saison bzw. Report |
| Kampagnen-Paket + Begleitung | 2.000–6.000 EUR / Kampagne |
| Gedruckte QR-Infotafel (optional) | 40–120 EUR / Stueck (Material wenige Euro) |

**Grober Break-even:** Fixkosten sind Entwicklung + gemeinsame Mehrmandanten-Infrastruktur (skaliert gut: ein Kern, viele Mandanten); variable Kosten je neuem Mandant gering. Als kleines Team realistisch bei **ca. 8–15 Mandanten im Jahres-Betrieb** plus Einrichtungs-/Auswertungsumsatz (ca. **40–80 TEUR ARR**). Der erste gefoerderte Modell-Mandant finanziert die Plattform-Basis.

### Warum Open Source
- **Offener Code + offene Datenstandards (GBIF/Darwin Core)** geben Kommunen einen doppelten Vorteil: **digitale Souveraenitaet und kein Lock-in** (Public Money Public Code) UND Buergerdaten fliessen **nachpruefbar in die wissenschaftliche Infrastruktur** statt in eine proprietaere Insel.
- Das erhoeht Vertrauen, Datenqualitaet und Vergabefaehigkeit.
- Ehrliche Einordnung: Dies ist ein Software-Projekt — die Alleinstellung liegt in **offenen Standards/kein Lock-in**, nicht in 3D-Druck. (Optionaler Zusatz: wetterfeste, lokal gedruckte QR-Infotafeln/Melde-Stelen an Wanderwegen, Produktion ggf. in einer Inklusionswerkstatt als sozialer Vergabe-Bonus — aber nicht Geschaeftskern.)
- Verdient wird trotzdem: an Einrichtung/Branding, gehostetem Betrieb, Moderation/Qualitaetssicherung und der Aufbereitung zu kommunal verwertbaren Berichten.

### Traktion & naechste 90 Tage
- **Tag 1–30:** Technik-Fundament festlegen (auf iNaturalist-/observation.org-Standards aufsetzen, Darwin-Core-/GBIF-Export sicherstellen); eine Modellkommune/einen Naturpark als Pilot ansprechen.
- **Tag 31–60:** MVP bauen — ein gebrandetes Portal + PWA mit einer Kampagne (z.B. Amphibien oder Wildbienen) fuer EINEN Mandanten; Report-Vorlage mit der UNB abstimmen.
- **Tag 61–90:** Pilot-Kampagne starten; offenes Repo + Doku veroeffentlichen, auf openCode einstellen; Fallstudie (Teilnehmer, Beobachtungen, Datenqualitaet) vorbereiten.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: DBU (Deutsche Bundesstiftung Umwelt)** bzw. **Bundesprogramm Biologische Vielfalt (BfN)** — beide foerdern Citizen Science, Monitoring, Buergerbeteiligung und Digitalisierung/Umweltbildung im Naturschutz und erlauben **groessere, laengere Vorhaben** (typisch ca. 1–3 Jahre, Foerdervolumen deutlich oberhalb reiner Prototyp-Programme; DBU-Projekte oft im sechsstelligen Bereich, BfN-Vorhaben im Bundesprogramm teils deutlich groesser — konkrete Hoehe je Modul/Call). Passt, weil BuergerNatur direkt auf nationale/laenderseitige Biodiversitaetsstrategien, Natura-2000-Managementplaene und kommunale Biodiversitaetskonzepte einzahlt und einen Praxis-Modell-Mandanten einbindet.

**Alternative: Prototype Fund** fuer den **offenen Plattform-Kern** (bis ca. **47.500 EUR / 6 Monate** fuer Einzelpersonen) — ideal, um den MVP-Kern unabhaengig und schnell als Open Source zu entwickeln, bevor ein groesseres DBU-/BfN-Vorhaben den Praxis-Rollout finanziert. Weiter denkbar: EU LIFE (Natur/Biodiversitaet) fuer groessere Schutzgebiets-Verbuende, Deutsche Postcode Lotterie, kommunale Smart-City-/Smart-Region-Mittel, Laender-Stiftungen Naturschutz.

Dieser Antrag ist als **DBU-/BfN-Projektskizze** ausformuliert (Laufzeit 12 Monate als foerderbarer Erst-Abschnitt, mit Option auf Verlaengerung/Rollout), mit einer kompakten Prototype-Fund-Variante im Finanzplan.

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**BuergerNatur — offene White-Label-Plattform fuer kommunale Citizen Science mit GBIF-Anschluss.**
Kommunen und Schutzgebiete brauchen Buergerbeteiligung und zugleich berichtsfaehige Arten-Daten, haben aber keine eigene, bezahlbare Plattform. BuergerNatur gibt jeder Verwaltung ein gebrandetes Melde-Portal plus App auf offenen Standards: Beobachtungen mit Foto/Ort, Bestimmungshilfe, thematische Kampagnen, Experten-Qualitaetssicherung, Dashboards und Export nach GBIF im Darwin-Core-Format — keine Dateninsel. Schutzwuerdige Arten-Standorte werden unscharf gehalten, Melder-Daten DSGVO-konform. Im Projekt entsteht ein offener, auf openCode veroeffentlichter MVP, erprobt mit einer Modellkommune/einem Schutzgebiet in einer echten Kampagne, mit behoerdentauglicher Report-Vorlage. Ziel sind verlaessliche, nachnutzbare Monitoring-Daten und aktivierte Buergerschaft — als souveraene Alternative zu proprietaeren Insellaesungen.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Der Biodiversitaetsverlust ist eine der zentralen oekologischen Krisen; wirksame Gegenmassnahmen brauchen Daten und Beteiligung. Kommunen und Schutzgebiete sind durch Biodiversitaetsstrategien, Natura-2000-Managementplaene und Berichtspflichten (FFH) gefordert, verfuegen aber selten ueber eigene, berichtsfaehige Erfassungssysteme. Gleichzeitig ist das Potenzial der Buergerbeteiligung gross (Naturblick: ca. 120.000–130.000 Nutzer), wird aber mangels kommunal nutzbarer, qualitaetsgesicherter Plattformen kaum gehoben. Oekologischer Nutzen: bessere Datengrundlage fuer Pflege- und Entwicklungsplaene, frueheres Erkennen von Bestandsveraenderungen (inkl. invasiver Arten), staerkere Naturverbundenheit und Umweltbildung in der Bevoelkerung — und durch GBIF-Export ein Beitrag zur offenen wissenschaftlichen Infrastruktur.

### Projektziele & Innovationsgehalt
1. **White-Label-Mehrmandanten-Kern:** ein offener Kern, der je Kommune/Schutzgebiet gebrandet betrieben wird — guenstig, souveraen, schnell ausrollbar.
2. **Offene Standards statt Insel:** verlustfreier Export nach GBIF (Darwin Core) und Anschluss an iNaturalist/observation.org sowie Flora-Incognita-/Pl@ntNet-Erkennung.
3. **Behoerdentaugliche Daten:** Experten-Qualitaetssicherung, Plausibilitaetspruefung, gefilterte Dashboards und abgestimmte Report-Vorlagen fuer amtliches Monitoring.
4. **Artenschutz-Geheimhaltung & DSGVO:** Standort-Unschaerfe/Zugriffsschutz fuer schutzwuerdige Arten, datenschutzkonforme Melder-Daten.

**Innovationsgehalt:** Nicht die Melde-Funktion an sich (die gibt es), sondern die **Kombination aus kommunalem White-Label-Branding, offenen Datenstandards mit GBIF-Anschluss, behoerdentauglicher Auswertung und offenem, nachnutzbarem Code** ist neu — ein souveraenes Gegenmodell zu proprietaeren Plattformen und zu reinen Fremd-Apps ohne kommunalen Datennutzen.

### Arbeitspakete

**AP1 — Technik-Fundament & Standards (Monat 1–2)**
- Ziel: Architektur und Standard-Anschluss festlegen.
- Inhalt: Aufsetzen auf iNaturalist-/observation.org-Standards, Darwin-Core-/GBIF-Export-Konzept, Mehrmandanten-Architektur, Datenschutz-/Artenschutz-Konzept (Standort-Unschaerfe).
- Deliverable: Architektur- + Datenschutz-/Standardkonzept (oeffentlich).
- Dauer: 2 Monate.

**AP2 — Plattform-Kern (Mehrmandanten) (Monat 2–5)**
- Ziel: Lauffaehiger Mehrmandanten-Kern mit Melde- und Verwaltungsfunktion.
- Inhalt: Beobachtungserfassung (Foto/Ton/Ort), Mandanten-/Branding-Verwaltung, Rollen/Rechte, Zugriffsschutz schutzwuerdiger Arten, GBIF-/Darwin-Core-Export.
- Deliverable: Betriebsfaehiger Kern + funktionierender GBIF-Export.
- Dauer: 3 Monate.

**AP3 — App (PWA) + Kampagnen + Bestimmungshilfe (Monat 4–7)**
- Ziel: Buergertaugliche App und erste Kampagne.
- Inhalt: PWA fuer Melder, Kampagnen-Modul (z.B. Amphibien/Wildbienen), Anbindung Flora-Incognita-/Pl@ntNet-Erkennung, Bestimmungshilfe.
- Deliverable: Nutzbare App + eine konfigurierte Kampagne.
- Dauer: 3 Monate (parallel zu AP2).

**AP4 — Qualitaetssicherung, Dashboards & behoerdentaugliche Reports (Monat 6–9)**
- Ziel: Aus Laienmeldungen verwertbare Monitoring-Daten machen.
- Inhalt: Experten-Validierung, Plausibilitaetspruefung, Dashboards, Report-Vorlage **mit der unteren Naturschutzbehoerde abgestimmt**.
- Deliverable: QS-Workflow + Dashboard + abgestimmte Report-Vorlage.
- Dauer: 3 Monate.

**AP5 — Pilot-Kampagne, Open-Source-Release & Fallstudie (Monat 9–12)**
- Ziel: Praxiserprobung, Veroeffentlichung, Wirkungsnachweis.
- Inhalt: echte Kampagne mit Modellkommune/Schutzgebiet, Release auf openCode unter freier Lizenz, Messung (Teilnehmer, Beobachtungen, Datenqualitaet, Validierungsquote).
- Deliverable: Oeffentliches Repo + Doku + Fallstudie mit Zahlen.
- Dauer: 3 Monate.

### Zeit- & Meilensteinplan (Monat 0–12)
- **M0 (Projektstart):** Setup, Modell-Mandant bestaetigt, Repo oeffentlich angelegt.
- **M1 (Ende Monat 2):** Architektur-, Datenschutz- und Standard-/GBIF-Konzept veroeffentlicht *(AP1)*.
- **M2 (Ende Monat 5):** Mehrmandanten-Kern mit funktionierendem GBIF-/Darwin-Core-Export *(AP2)*.
- **M3 (Ende Monat 9):** App + Kampagne live, QS-Workflow + behoerdentaugliche Report-Vorlage *(AP3/AP4)*.
- **M4 (Ende Monat 12):** Pilot-Kampagne abgeschlossen + Open-Source-Release + Fallstudie *(AP5)* — Ende des Erst-Foerderabschnitts, Option auf Rollout-Phase.

### Kosten- & Finanzierungsplan (EUR)

**DBU-/BfN-Variante (12 Monate, Erst-Abschnitt)**

| Position | Betrag (EUR) |
|---|---|
| Personal (Entwicklung, Projektleitung, QS-Konzept, ~12 Monate) | 95.000 |
| Sachkosten (Hardware, Software-Lizenzen, Kampagnen-Material, optionale QR-Infotafeln) | 8.000 |
| Cloud/Hosting (Mehrmandanten-Infrastruktur, Pilot- und Testbetrieb) | 9.000 |
| Fremdleistung (UX/Design, Datenschutz-/Rechts-Review, Experten-Validierung im Pilot) | 18.000 |
| Reise (Pilot-Vor-Ort-Termine, Kampagnen-Begleitung, Community/openCode) | 4.000 |
| **Summe** | **134.000** |
| Eigenanteil / Foerderquote | DBU/BfN i.d.R. Teilfoerderung; Eigenanteil ca. 10–50 % je nach Programm/Antragsteller (z.B. Eigenleistung + Modell-Mandant-Beitrag), konkret je Call zu verifizieren |

**Prototype-Fund-Variante (6 Monate, nur offener Kern, Orientierung)**

| Position | Betrag (EUR) |
|---|---|
| Personal (Entwicklung Kern + GBIF-Export, ~6 Monate) | 39.000 |
| Sachkosten | 2.000 |
| Cloud/Hosting | 3.500 |
| Fremdleistung (Datenschutz-Review, UX-Punktleistung) | 2.000 |
| Reise | 1.000 |
| **Summe** | **47.500** |
| Eigenanteil | 0 (im Programmrahmen) |

*Zahlen als Planung/Spanne; Foerderquote, Eigenanteil und zulaessige Positionen richten sich nach den jeweils gueltigen Programmrichtlinien (DBU/BfN/Prototype Fund) und sind vor Antragstellung zu verifizieren.*

### Verwertung & Tragfaehigkeit nach Foerderende
Nach dem gefoerderten Erst-Abschnitt traegt sich das Vorhaben ueber das Open-Core-Mehrmandanten-Modell: einmalige Einrichtung je Mandant + jaehrliche Betriebsgebuehr (wiederkehrend) + datennahe Dienstleistung (Auswertung/Reports, Moderation/QS, Kampagnen-Begleitung). Der im Pilot entstandene Referenz-Mandant und die Fallstudie (Teilnehmer, Beobachtungen, Datenqualitaet) sind der Vertriebshebel fuer weitere Kommunen/Schutzgebiete. Jeder neue Mandant laeuft auf derselben Codebasis und ist damit margenstark. Break-even realistisch bei ca. 8–15 Mandanten im Jahres-Betrieb (ca. 40–80 TEUR ARR). Foerderabhaengigkeit wird vermieden, indem frueh (bereits im Pilotjahr) Betriebsvertraege gesichert werden.

### Open-Source-/Gemeinwohl-Bezug
- **Lizenz:** offener Plattform-Kern unter OSI-anerkannter freier Lizenz (z.B. EUPL/AGPL), oeffentliche Doku.
- **Public Money Public Code:** oeffentlich finanzierte Software wird oeffentlich/nachnutzbar — statt dass jede Kommune parallel entwickelt oder sich an einen proprietaeren Anbieter bindet.
- **Offene Datenstandards (GBIF/Darwin Core):** Buergerdaten fliessen nachpruefbar in die wissenschaftliche Infrastruktur (GBIF Deutschland) — Gemeinwohl ueber die einzelne Kommune hinaus.
- **openCode:** Veroeffentlichung macht das Portal fuer andere Verwaltungen auffindbar und nachnutzbar; Betrieb/Anpassung wird zugekauft.
- **Gemeinwohl:** Buergerbeteiligung, Umweltbildung, verlaessliche Biodiversitaets-Daten fuer Schutz und Berichtspflichten.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
- **Zielpartner:** EINE Modellkommune (Umwelt-/Gruenflaechenamt) ODER ein Naturpark/Biosphaerenreservat als Modell-Mandant; begleitend die zustaendige **Untere Naturschutzbehoerde** fuer die Abstimmung der behoerdentauglichen Report-Vorlage.
- **LOI-Strategie:** (1) Erstgespraech zu Kampagnen-Thema und Datenbedarf, (2) LOI des Modell-Mandanten fuer die Pilotteilnahme (Kampagne, Testdaten, Abnahme der Report-Vorlage), (3) separate Unterstuetzungs-/Interessens-LOIs von einer bis zwei weiteren Kommunen/Schutzgebieten als Rollout-Perspektive, (4) im LOI die Option auf einen Betriebsvertrag nach erfolgreichem Pilot skizzieren.
- **Fruehe Behoerden-Einbindung:** Datenschutz-/Artenschutz-Fragen (Standort-Unschaerfe) und Berichtstauglichkeit werden ab AP1 mit der UNB geklaert, um Akzeptanz und Vergabefaehigkeit zu sichern.

### Risiken & Gegenmassnahmen

| Risiko | Gegenmassnahme |
|---|---|
| Veroeffentlichung sensibler Standorte schutzwuerdiger Arten (z.B. Greifvogel-Horste) | Standort-Unschaerfe/Zugriffsschutz, abgestufte Sichtbarkeit, Rollen-/Rechtekonzept, Abstimmung mit UNB |
| DSGVO-Verstoss bei Melder-Daten | Datensparsamkeit, Einwilligung, EU-Hosting, dokumentiertes Datenschutzkonzept ab AP1 |
| Schwankende Datenqualitaet aus Laienmeldungen | Experten-Validierung, Plausibilitaetspruefung, QS-Workflow (AP4), Bestimmungshilfe/Arterkennungs-Anbindung |
| Konkurrenz durch etablierte kostenlose Apps (iNaturalist, Naturblick) | Mehrwert = Branding, kommunale Auswertung/Reports, Integration/GBIF-Export — nicht die reine Melde-Funktion |
| Lange Behoerden-Beschaffungszyklen / Foerderabhaengigkeit | Direktauftrag unter Vergabeschwelle, gefoerderter Modell-Mandant als Tueroeffner, frueh Betriebsvertraege sichern |
| Dateninsel-Gefahr / Lock-in-Vorwurf | Konsequent offene Standards (GBIF/Darwin Core) + offener Code, keine proprietaeren Formate |
| Geringe Buergerbeteiligung in der Kampagne | Attraktive Kampagnen-Themen, Umweltbildungs-Begleitung, QR-Infotafeln/Aktionstage, Social Proof |
| Technische Abhaengigkeit von Drittdiensten (Arterkennung) | Austauschbare, standardbasierte Anbindung; Kernfunktion bleibt ohne Drittdienst nutzbar |
