# NaturBuero-KI — KI-Assistent fuer Naturschutz-Verwaltung und Ehrenamt — Pitch & Foerderantrag

> Open-Source-KI-Assistent mit Mensch-prueft-alles-Prinzip, der Naturschutzbehoerden und ehrenamtlichen Verbaenden die Schreib- und Antragslast abnimmt — DSGVO-konform, auf EU-Hosting oder On-Premises, mit strikter Quellenbindung gegen Halluzination.
>
> Gruenderrolle: Soloselbststaendig/Nebenerwerb mit Wachstumsabsicht. Zahlen teils als Spanne/"ca."; Programm-Eckdaten nach allgemein bekanntem Stand, im Einzelfall vor Antragstellung zu verifizieren.

---

## Teil A — Pitch

### Elevator Pitch (30 Sekunden)
Naturschutz ist heute zu einem grossen Teil Schreibarbeit: Foerderantraege, Verwendungsnachweise, Stellungnahmen, Kartierungs-Protokolle, Pressetexte. Behoerden und Ehrenamt ertrinken darin, waehrend die Zeit fuer die eigentliche Naturschutzarbeit fehlt. **NaturBuero-KI** ist ein Open-Source-Assistent, der genau diese Texte als Entwuerfe erstellt — aber **nur aus den eigenen, hochgeladenen Dokumenten der Organisation**, jede Aussage mit Quellenbeleg, nichts frei erfunden. Der Mensch prueft und gibt frei. Betrieb DSGVO-konform auf EU-Hosting oder im eigenen Haus. Wir verkaufen keine Lizenz, sondern Hosting, Einrichtung und Schulung.

### Das Problem (mit Zahlen)
- Untere Naturschutzbehoerden (UNB) der rund 400 Landkreise und kreisfreien Staedte, ca. 180+ Landschaftspflegeverbaende, biologische Stationen und tausende ehrenamtliche NABU-/BUND-Ortsgruppen stemmen eine stetig wachsende Dokumentationslast.
- Treiber sind gesetzliche Berichtspflichten nach BNatSchG und FFH-/Vogelschutzrichtlinie, Nachweispflichten der Foerdermittelgeber (Bundesprogramm Biologische Vielfalt, LIFE, ELER/Agrarumwelt, kommunale Toepfe) und kurze Einreichfristen.
- Gleichzeitig: Fachkraeftemangel in den Behoerden und ein chronisch ueberlastetes Ehrenamt. Ein einzelner Verwendungsnachweis oder Foerderantrag bindet je nach Komplexitaet schnell einen bis mehrere Arbeitstage.
- Fertige Buero-KI aus den USA scheidet fuer Behoerden oft aus — wegen Datenschutz (schutzwuerdige Arten-/Standortdaten, personenbezogene Daten) und fehlender Fachlichkeit.

Kernnutzen ist damit **zurueckgewonnene Ehrenamts- und Verwaltungszeit** — Stunden pro Antrag, die wieder in die Flaeche fliessen koennen.

### Die Loesung
Eine Open-Source-Assistenzsoftware, spezialisiert auf Naturschutz-Verwaltungstexte:
- Nutzer laden eigene Daten in eine **lokale Wissensbasis** (Kartierungen, Massnahmenlisten, Foerderrichtlinie, Vorjahresberichte).
- Die KI erstellt Entwuerfe **strikt auf Basis dieser Quellen** (Retrieval-Augmented Generation). **Jede Aussage traegt einen Quellenbeleg** aus dem eigenen Dokument — frei erfundene Rechtsgrundlagen, Zahlen oder Zitate werden konstruktiv verhindert.
- Workflows: Foerderantrag ausfuellen, Bericht aus Rohdaten, Stellungnahme-Geruest zu Bauleitplanung/Eingriffen, Pressetext, Protokoll aus Stichpunkten.
- **Kernprinzip Mensch-prueft-alles:** Die KI liefert Entwuerfe und markiert Luecken/Unsicherheiten sichtbar; der Mensch gibt frei. Keine Voll-Automatisierung, keine selbststaendig abgesendeten Texte.
- Betrieb **On-Premises oder auf EU-Cloud**, mit offenen Modellen (z.B. Teuken/OpenGPT-X, Llama, Mistral) oder souveraenen EU-Modell-Endpunkten — kein Datenabfluss in US-Clouds.

Die Software ist offen; verdient wird an Hosting, Einrichtung, Vorlagen und Schulung.

### Markt & Kunde (oeffentliche Hand)
- **Untere Naturschutzbehoerden** der Landkreise/kreisfreien Staedte — **Direktauftrag** moeglich (seit 2026 Direktauftrag haeufig bis ca. 50.000 EUR netto, Verhandlungsvergabe bis ca. 100.000 EUR netto).
- **Landschaftspflegeverbaende und Biologische Stationen** (oft e.V. mit Behoerden-Finanzierung) — koennen direkt beauftragen, kurze Wege.
- **Nationalpark-, Naturpark- und Biosphaerenreservats-Verwaltungen** als **Rahmenvertrag** ueber mehrere Reviere.
- **Kommunale Umwelt-/Gruenflaechenaemter** fuer eigene Foerderantraege und Oeffentlichkeitsarbeit.
- **Zugang:** Einstieg ueber ein **gefoerdertes Pilot/Reallabor** mit einer Behoerde oder einem Dachverband (NABU-/BUND-Landesverband); Ergebnis als Referenz-Fallstudie. Danach Ausrollen an Nachbar-Landkreise unter der Direktauftragsschwelle, spaeter Rahmenvertraege.
- **Vertriebskanal openCode (ZenDiS):** Veroeffentlichung macht die Software fuer alle Verwaltungen sichtbar und nachnutzbar.

### Geschaeftsmodell & Finanzen
Open-Core plus B2G-SaaS und Dienstleistung. Der Assistenz-Kern ist offen und auditierbar; verkauft werden Betrieb, Einrichtung, Vorlagen und Schulung.

| Umsatzstrom | Preis (ca.) |
|---|---|
| SaaS je Arbeitsplatz (EU-Hosting) | 30–60 EUR / Platz / Monat |
| Organisations-Flat (kleine Behoerde/Verband) | 2.400–6.000 EUR / Jahr |
| Einrichtung + Datenanbindung | 3.000–12.000 EUR einmalig |
| On-Premises Lizenz + Support | 8.000–25.000 EUR / Jahr je nach Groesse |
| Schulung (Halbtag, Gruppe) | 600–1.200 EUR |
| Vorlagen-Paket je Foerderlinie | 500–1.500 EUR einmalig |

**Grober Break-even:** Hauptkostenblock ist Entwicklungszeit; laufend moderate GPU-/Inferenzkosten (kleine offene Modelle) und EU-Hosting. Als Soloselbststaendiger/kleines Team realistisch bei **ca. 15–25 zahlenden Organisationen im Flat-Abo** oder einigen On-Prem-Vertraegen (ca. **40–80 TEUR ARR**). Der erste gefoerderte Pilot plus zwei bis drei Einrichtungsauftraege decken die MVP-Phase. Groesstes Geschaeftsrisiko sind nicht Technik, sondern Beschaffungs- und Datenschutz-Freigabezyklen.

### Warum Open Source
Bei KI in der Verwaltung ist **Souveraenitaet das Verkaufsargument**, nicht ein Nebeneffekt:
- Offene Modelle + offener Code erlauben **On-Premises-Betrieb ohne Datenabfluss** an US-Clouds.
- **Nachpruefbare Prompts** und auditierbares Verhalten — Datenschutzbeauftragte und Behoerden-Juristen stimmen offenen Loesungen leichter zu.
- **Kein Vendor-Lock-in** (offene Formate/Exporte, austauschbare Modelle) — genau die Kriterien von ZenDiS/openCode und **Public Money Public Code**.
- Ehrliche Einordnung: Das ist ein reines Software-Projekt — die Alleinstellung liegt in **offenen Standards, Auditierbarkeit und Fachnische Naturschutz**, nicht in Hardware/3D-Druck. (Optional: gedruckte QR-Infotafeln fuer die Oeffentlichkeitsarbeit, Produktion ggf. in einer Inklusionswerkstatt als sozialer Vergabe-Bonus — aber nicht Kern des Geschaefts.)

Geld kommt nicht aus Lizenz, sondern aus EU-Hosting/Betrieb, fachlichen Vorlagen-Paketen, Einrichtung in die konkrete Datenlage und Schulung — das darf man trotz OSS berechnen.

### Traktion & naechste 90 Tage
- **Tag 1–30:** Einen konkreten Schmerz-Workflow waehlen (z.B. Verwendungsnachweis einer haeufigen Foerderlinie) und als MVP mit strikter Quellenbindung + Export spezifizieren. DSGVO-/On-Prem-Konzept als lebendes Dokument starten.
- **Tag 31–60:** MVP bauen; eine Partner-Behoerde oder einen Landschaftspflegeverband als Pilot gewinnen; mit echten, anonymisierten Dokumenten testen.
- **Tag 61–90:** Offenes Repo + Doku veroeffentlichen, auf openCode einstellen; 1-Seiten-Angebot fuer Direktauftrag erstellen; erste Fallstudie (Zeitersparnis in Stunden pro Antrag) vorbereiten.

---

## Teil B — Foerderantrag

### Zielprogramm & Begruendung
**Primaer: Prototype Fund** (Civic Tech / Verwaltung) fuer den **offenen Kern**. Foerderrahmen: bis ca. **47.500 EUR fuer Einzelpersonen**, bis ca. 158.333 EUR fuer Teams; Laufzeit **6 Monate**. Passt exakt, weil (a) das Ergebnis offener Code unter freier Lizenz wird, (b) das Projekt klaren Gemeinwohl-/Civic-Tech-Charakter hat (Entlastung von Behoerden und Ehrenamt) und (c) es sich im openCode/ZenDiS-Umfeld der digital-souveraenen Verwaltungssoftware verortet.

**Alternative/ergaenzend:** **EXIST-Gruenderstipendium** (ca. 2.500–3.000 EUR/Monat Lebensunterhalt + bis ca. 5.000 EUR Sachmittel, **12 Monate**, aus einer Hochschule heraus) fuer die Gruendungsphase und den Aufbau des Geschaeftsbetriebs rund um den offenen Kern. Weiter denkbar: DBU (Digitalisierung im Umwelt-/Naturschutz), Bundesprogramm Biologische Vielfalt (BfN), GovTech-/Digitalisierungsprogramme (OZG-Nachfolge, Modellkommunen), Deutsche Postcode Lotterie. Prototype Fund und EXIST schliessen sich zeitlich aus bzw. muessen getrennt gefahren werden; hier wird der Prototype-Fund-Antrag als Leitlinie ausformuliert und auf 6 Monate / 47.500 EUR ausgelegt, mit einer skizzierten 12-Monats-EXIST-Variante im Finanzplan.

### Projekttitel & Kurzfassung (max. 10 Zeilen)
**NaturBuero-KI — quellengebundener, menschlich gepruefter KI-Assistent fuer Naturschutz-Verwaltung und Ehrenamt.**
Naturschutzbehoerden und ehrenamtliche Verbaende verlieren einen Grossteil ihrer Zeit mit Antraegen, Nachweisen und Berichten. NaturBuero-KI erstellt diese Texte als Entwuerfe — ausschliesslich aus den eigenen Dokumenten der Organisation, jede Aussage mit Quellenbeleg, Unsicherheiten sichtbar markiert, Freigabe immer durch den Menschen. Der Betrieb ist DSGVO-konform auf EU-Hosting oder On-Premises mit offenen Modellen; es fliessen keine schutzwuerdigen Arten- oder Personendaten ab. Im Foerderzeitraum entsteht ein offener, auf openCode veroeffentlichter MVP fuer einen konkreten Antrags-/Berichts-Workflow, erprobt mit einem Praxispartner. Ziel ist nachweisbar zurueckgewonnene Verwaltungs- und Ehrenamtszeit sowie eine nachnutzbare, souveraene Grundlage statt einer proprietaeren Dateninsel.

### Ausgangslage & gesellschaftlicher/oekologischer Bedarf
Der Naturschutzvollzug in Deutschland ist strukturell ueberlastet. Berichtspflichten nach BNatSchG und FFH-/Vogelschutzrichtlinie, Nachweispflichten der Foerdermittelgeber und kurze Fristen treffen auf Fachkraeftemangel in den Behoerden und ein ehrenamtlich getragenes System am Limit. Die Folge: Zeit, die fuer Kartierung, Pflege und Umsetzung fehlt, versickert in Formularen. Marktseitig fehlt eine fachlich passende, datenschutzkonforme Loesung — US-Buero-KI ist fuer Behoerden wegen Datenabfluss und fehlender Naturschutz-Fachlichkeit meist nicht freigabefaehig. Oekologischer Bedarf: Jede eingesparte Verwaltungsstunde ist potenziell eine Stunde mehr fuer die Flaeche; zugleich erhoeht quellengebundene Textarbeit die Qualitaet und Fristtreue von Antraegen, was Foerdermittel besser abfliessen laesst.

### Projektziele & Innovationsgehalt
1. **Quellengebundener Entwurf (Anti-Halluzination):** Jede generierte Aussage ist auf ein konkretes Quelldokument der Organisation zurueckfuehrbar; nicht belegbare Inhalte werden nicht behauptet, sondern als Luecke markiert.
2. **Mensch-prueft-alles als Produktprinzip:** sichtbare Unsicherheits-/Luecken-Markierung, Pflicht-Freigabeschritt, kein selbststaendiges Absenden — als Qualitaets- und Haftungsargument.
3. **Souveraener Betrieb:** On-Premises und EU-Hosting mit offenen Modellen; dokumentiertes DSGVO-/Datenflusskonzept fuer Behoerden-Freigabe.
4. **Fachnische Naturschutz:** Vorlagen und Workflows fuer reale Naturschutz-Dokumente statt Allzweck-Buero-KI.

**Innovationsgehalt:** Die Kombination aus strikter Quellenbindung, erzwungener menschlicher Freigabe, voll-souveraenem Betrieb und fachlicher Spezialisierung auf Naturschutz-Verwaltung gibt es so nicht als offene, nachnutzbare Software. Der Fortschritt liegt nicht im Modell selbst, sondern in der verlaesslichen, auditierbaren Einbettung in einen risikoarmen Verwaltungs-Workflow.

### Arbeitspakete

**AP1 — Workflow- & Datenschutzfundament (Monat 1)**
- Ziel: Einen Schmerz-Workflow (z.B. Verwendungsnachweis einer haeufigen Foerderlinie) und das DSGVO-/On-Prem-Konzept festlegen.
- Inhalt: Anforderungsaufnahme mit Praxispartner, Dokumenttypen, Schutzbedarf (Arten-/Personendaten), Zielarchitektur (RAG, Modellwahl, Hosting).
- Deliverable: Workflow-Spezifikation + Datenschutz-/Datenflusskonzept (oeffentlich).
- Dauer: 1 Monat.

**AP2 — RAG-Kern mit Quellenbindung (Monat 1–3)**
- Ziel: Entwuerfe ausschliesslich aus eigenen Dokumenten, mit Beleg.
- Inhalt: Dokument-Ingestion/Wissensbasis, Retrieval, quellenverankerte Generierung, Zitier-/Nachweis-Layer, Luecken-/Unsicherheits-Markierung.
- Deliverable: Lauffaehiger Kern mit nachpruefbaren Quellenbelegen.
- Dauer: 2 Monate.

**AP3 — MVP-Workflow + Export + Pruef-/Freigabe-UI (Monat 3–4)**
- Ziel: Ein End-to-End-Workflow bis zum exportierbaren Dokument.
- Inhalt: Eingabe aus Rohdaten/Stichpunkten, Entwurfserstellung, Mensch-prueft-alles-Oberflaeche, Export (DOCX/PDF).
- Deliverable: Nutzbarer MVP fuer den gewaehlten Workflow.
- Dauer: 2 Monate.

**AP4 — Souveraener Betrieb (On-Prem + EU-Hosting) (Monat 4–5)**
- Ziel: Freigabefaehiger Betrieb ohne Datenabfluss.
- Inhalt: Container-Deployment, offenes Modell lokal/EU-Endpunkt, Rollen/Rechte, Standort-Unschaerfe fuer schutzwuerdige Arten, Betriebs-/Sicherheitsdoku.
- Deliverable: Deploybares Paket + Betriebsdoku.
- Dauer: 2 Monate (parallel zu AP3/AP5).

**AP5 — Pilot, Open-Source-Release & Fallstudie (Monat 5–6)**
- Ziel: Praxiserprobung, Veroeffentlichung, Wirkungsnachweis.
- Inhalt: Pilot mit Partner-Behoerde/-Verband (anonymisierte Echtdokumente), Release auf openCode unter freier Lizenz, Messung Zeitersparnis pro Antrag.
- Deliverable: Oeffentliches Repo + Doku + Fallstudie (Stunden/Antrag).
- Dauer: 2 Monate.

### Zeit- & Meilensteinplan (Monat 0–12)
- **M0 (Projektstart):** Setup, Praxispartner bestaetigt, Repo oeffentlich angelegt.
- **M1 (Ende Monat 1):** Workflow-Spezifikation + Datenschutzkonzept veroeffentlicht *(AP1)*.
- **M2 (Ende Monat 3):** RAG-Kern mit funktionierender Quellenbindung *(AP2)*.
- **M3 (Ende Monat 4):** Nutzbarer MVP-Workflow mit Pruef-/Freigabe-UI und Export *(AP3)*.
- **M4 (Ende Monat 6):** Souveraenes Deployment + Pilot abgeschlossen + Open-Source-Release + Fallstudie *(AP4/AP5)* — **Ende der Prototype-Fund-Foerderung**.
- *EXIST-Variante (bis Monat 12):* Monate 7–12 fuer Haertung, zweiten Workflow/Foerderlinie, Vertriebsaufbau (Angebot, Preisliste, Direktauftraege) und zwei bis drei Einrichtungsauftraege.

### Kosten- & Finanzierungsplan (EUR)

**Prototype-Fund-Variante (6 Monate, Zielsumme ca. 47.500 EUR)**

| Position | Betrag (EUR) |
|---|---|
| Personal (Entwicklung/Konzeption, ~6 Monate Soloselbststaendig, kalkulatorisch) | 38.000 |
| Sachkosten (Hardware-Anteil, Software-Lizenzen, Testdaten-Aufbereitung) | 2.500 |
| Cloud/Hosting + GPU-Inferenz (EU-Hosting, Test- und Pilotbetrieb) | 3.500 |
| Fremdleistung (Datenschutz-/Rechts-Review, Design/UX-Punktleistung) | 2.500 |
| Reise (Pilot-Vor-Ort-Termine, Community/openCode) | 1.000 |
| **Summe** | **47.500** |
| Eigenanteil | 0 (Prototype Fund foerdert i.d.R. 100 % im Rahmen) |

**EXIST-Variante (12 Monate, Orientierung)**

| Position | Betrag (EUR) |
|---|---|
| Stipendium Lebensunterhalt (ca. 2.500–3.000/Monat x 12) | 30.000–36.000 |
| Sachmittel (bis ca.) | 5.000 |
| Coaching/Gruendungsberatung (ueber Hochschule) | im Programm |
| **Summe (Orientierung)** | **ca. 35.000–41.000** |
| Eigenanteil | i.d.R. kein Baranteil (Stipendium) |

*Zahlen als Planung/Spanne; die konkrete Foerderquote und zulaessige Positionen richten sich nach den jeweils gueltigen Programmrichtlinien und sind vor Antragstellung zu verifizieren.*

### Verwertung & Tragfaehigkeit nach Foerderende
Nach der Foerderung traegt sich das Vorhaben ueber das Open-Core-B2G-Modell: wiederkehrende Betriebs-/Supportvertraege (SaaS-Flat, On-Prem-Support) plus Projektgeschaeft (Einrichtung, Datenanbindung, Vorlagen-Pakete, Schulung). Der im Pilot entstandene Referenz-Nachweis (Zeitersparnis pro Antrag) ist das zentrale Vertriebsargument fuer Nachbar-Landkreise und Dachverbaende. Break-even realistisch bei ca. 15–25 zahlenden Organisationen bzw. einigen On-Prem-Vertraegen (ca. 40–80 TEUR ARR). Abhaengigkeit von Foerdermitteln wird bewusst vermieden, indem frueh (bereits in Monat 5–6) erste kostenpflichtige Einrichtungs-/Betriebsgespraeche gefuehrt werden.

### Open-Source-/Gemeinwohl-Bezug
- **Lizenz:** offener Kern unter einer OSI-anerkannten freien Lizenz (z.B. EUPL oder AGPL fuer die serverseitige Software), inkl. oeffentlicher Doku.
- **Public Money Public Code:** Mit oeffentlichen Mitteln entwickelte Software wird oeffentlich und nachnutzbar — kein Lock-in, keine Parallelentwicklung in jeder Behoerde.
- **openCode/ZenDiS:** Veroeffentlichung auf openCode macht die Loesung fuer alle Verwaltungen auffindbar und nachnutzbar und verortet sie im souveraenen Verwaltungssoftware-Oekosystem (openDesk-Umfeld).
- **Gemeinwohl:** Entlastung von Behoerden und Ehrenamt, bessere Fristtreue/Qualitaet von Foerderantraegen, mehr Zeit fuer praktischen Naturschutz.

### Anwendungspartner oeffentliche Hand & LOI-Strategie
- **Zielpartner:** eine Untere Naturschutzbehoerde ODER ein Landschaftspflegeverband/eine Biologische Station (kurze Wege, direkt beauftragbar), alternativ ein NABU-/BUND-Landesverband als Dachverband-Pilot.
- **LOI-Strategie:** (1) Erstgespraech zum Schmerz-Workflow, (2) Absichtserklaerung (LOI) fuer die kostenlose Pilotteilnahme mit anonymisierten Echtdokumenten im Foerderzeitraum, (3) im LOI bereits die Option auf einen Einrichtungs-/Betriebsvertrag nach erfolgreichem Pilot skizzieren. Mehrere kleine LOIs (Partner + ein bis zwei interessierte Nachbar-Landkreise) sind staerker als ein einziger grosser.
- **Datenschutz zuerst:** Der/die Datenschutzbeauftragte des Partners wird frueh eingebunden; das On-Prem-/EU-Hosting-Konzept ist Teil des LOI-Pakets, um Freigabezyklen zu verkuerzen.

### Risiken & Gegenmassnahmen

| Risiko | Gegenmassnahme |
|---|---|
| KI-Halluzination (erfundene Rechtsgrundlagen/Zahlen/Quellen) in Verwaltungstexten | Strikte Quellenbindung (RAG), Beleg je Aussage, sichtbare Unsicherheits-/Luecken-Markierung, verpflichtende menschliche Freigabe, keine Voll-Automatisierung |
| Datenabfluss schutzwuerdiger Arten-/Personendaten | On-Premises/EU-Hosting zwingend, kein US-Cloud-Einsatz, Standort-Unschaerfe, Rollen-/Rechtekonzept, dokumentiertes Datenflusskonzept |
| Lange Behoerden-Beschaffungs-/Freigabezyklen | Direktauftrag unter Vergabeschwelle nutzen, Datenschutzbeauftragte frueh einbinden, gefoerderter Pilot als Tuerofffner, LOI-basierte Vorvertraege |
| Abhaengigkeit von Foerdermitteln | Frueh zahlende Einrichtungs-/Betriebsvertraege, Open-Core-Umsatz ab Monat 5–6 anbahnen |
| Wettbewerb durch kapitalstarke Anbieter (z.B. Aleph Alpha) | Nische Naturschutz-Fachlichkeit + Ehrenamt besetzen, nicht Allzweck-Verwaltung; Offenheit/Nachnutzbarkeit als Differenzierung |
| Modell-/Betriebskosten (GPU-Inferenz) laufen hoch | Kleine offene Modelle, Caching, bedarfsgerechtes Hosting, On-Prem-Option beim Kunden |
| Qualitaet/Akzeptanz unzureichend | Enger Pilot mit echtem Partner, Zeitersparnis messen, iterative Einbindung der Nutzer |
