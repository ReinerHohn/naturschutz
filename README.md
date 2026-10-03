# 🌱 Naturschutz effizient — Hebel-Katalog

Ein durchsuchbarer, evidenzbasierter Katalog: **Wo bringt jeder Euro und jede Stunde am meisten für die Natur?**
Von der **Grünbrücke** über **Insektenschutz** und **Hecken** bis zur **Flächenpolitik** — nach Wirkung sortiert,
mit ehrlichem Evidenz-Level (A/B/C), konkreter Umsetzung und **Low-Hanging Fruits zuerst**.

Gleiches Baumuster wie [`leistungsfaehigkeit`](https://github.com/ReinerHohn/leistungsfaehigkeit),
[`flirt`](https://github.com/ReinerHohn/flirt) & Co.: eine Karte = ein Hebel als JSON, ein Build-Skript
erzeugt ein **self-contained `dashboard.html`** (läuft offline, ohne Server, ohne Netz). Nur Python-Standardbibliothek.

## Schnellstart

```bash
python3 test.py     # validiert alle Karten
python3 build.py    # baut dashboard.html + KATALOG.md
./run.sh            # baut + öffnet das Dashboard im Browser
```

Dann `dashboard.html` im Browser öffnen. Oben stehen die **🍒 Low-Hanging Fruits** (bestes Verhältnis
Wirkung / Aufwand / Evidenz), darunter die volle, durchsuchbare Liste mit Kategorie-Filtern.

## Aufbau

```
hebel/*.json     # je eine Maßnahme (die Quelle der Wahrheit)
schema.json      # Feld-Definitionen
build.py         # baut dashboard.html + KATALOG.md
test.py          # validiert die JSONs
LIMITATIONEN.md  # ehrliche Grenzen der Bewertung
```

## Felder einer Karte (Kurzfassung)

- `impact` 1–5 — ökologische Wirkstärke (steuert die Sortierung)
- `effort` 1–5 — Aufwand/Kosten (1 = gratis/privat, 5 = teure Infrastruktur)
- `evidence_level` A/B/C — wie hart belegt
- `scale` — wer setzt es um (Privat / Kommune / Land&Bund / EU)
- `summary`, `key_facts`, `deep_dive`, `mechanism`, `protocol`, `mistakes`, `risks`, `evidence`, `sources`

Der **Low-Hanging-Fruit-Score** = (Wirkung − 0,6·Aufwand) × Evidenzgewicht (A=1,0 · B=0,7 · C=0,4).

## Kategorien

Vernetzung & Korridore · Insekten & Bestäuber · Garten & Siedlung · Landwirtschaft & Fläche ·
Gewässer & Feuchtgebiete · Wald & Totholz · Gefahren & Fallen · KI, Software & 3D-Druck · Politik & System-Hebel

## 💰 Gründerprojekte (projekte.html)

Zweiter Katalog im selben Repo: **wie man aus den Tech-Hebeln ein Geschäft macht, das die öffentliche Hand bedient und sich trägt.**
Für jede Tech-Option ein Projekt mit Markt, Zugang zur öffentlichen Hand (Direktauftrag/Vergabe/Pilot), Open-Source-Geschäftsmodell,
3D-Druck-Hebel, konkreten Preisen, Förderprogrammen, Break-even und den ersten 90 Tagen.

```bash
python3 build_projekte.py    # baut projekte.html + PROJEKTE.md
```

- Quelle: `projekte/*.json`, Schema: `schema_projekte.json`
- Sortiert nach **Ertrag ÷ Aufwand** (Score = (Ertrag − 0,6·Aufwand) × Marktgewicht A=1,0/B=0,7/C=0,4)
- Kern-Idee: **Open Source ist beim Staat ein Verkaufsargument** (Public Money Public Code, kein Lock-in, digitale Souveränität).
  Geld kommt aus Hardware, Betrieb/Service, SaaS-Auswertung und Förderung — nicht aus Software-Lizenzen. 3D-Druck senkt Stückkosten
  und ermöglicht lokale / Inklusionswerkstatt-Produktion (Vergabe-Vorteil).
- 11 Projekte, 4 Segmente: Monitoring-SaaS & Service · Open Hardware & 3D-Druck · Software & Plattform · Beratung & Planung.

_Keine Rechts-/Steuer-/Anlageberatung — Ertrag/Aufwand sind Einschätzungen, keine Prognosen._

## Prinzip

**Anti-Hype, Wirkung pro Aufwand.** Sichtbarkeit ≠ Wirkung: der Katalog benennt auch beliebte Maßnahmen,
die wenig bringen, und stellt die wirksamen, oft unspektakulären daneben. Siehe `LIMITATIONEN.md`.

_Keine Fachplanung — vor konkreten Maßnahmen lokale Naturschutzbehörde / NABU / BUND / Landschaftspflegeverband einbeziehen._
