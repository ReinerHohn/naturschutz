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

## Prinzip

**Anti-Hype, Wirkung pro Aufwand.** Sichtbarkeit ≠ Wirkung: der Katalog benennt auch beliebte Maßnahmen,
die wenig bringen, und stellt die wirksamen, oft unspektakulären daneben. Siehe `LIMITATIONEN.md`.

_Keine Fachplanung — vor konkreten Maßnahmen lokale Naturschutzbehörde / NABU / BUND / Landschaftspflegeverband einbeziehen._
