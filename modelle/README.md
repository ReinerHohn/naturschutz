# 🛠️ Open-Source-Druckvorlagen (3D-Druck)

Parametrische, quelloffene Modelle zu den Hardware-Projekten. Format: **OpenSCAD** (`.scad`) —
der offene Standard für versionierbare, parametrische 3D-Druck-Hardware. Text statt Binär:
git-freundlich, jede:r kann Maße anpassen und tausendfach drucken. **Der Wert liegt in den
korrekten, artgerechten Maßen**, die hier einmal offen geteilt werden — nicht im „gedruckt".

## Modelle

| Datei | Zweck | Projekt / Hebel |
|---|---|---|
| `wildbienen-nistblock.scad` | Nistblock, gemischte Lochdurchmesser 3–8 mm, Sacklöcher ≥10 cm, gefaste Eingänge | NaturDruck · `3d-wildbienen-nistblock` |
| `ausstiegshilfe-rampe.scad` | Rettungsrampe mit Grip-Stegen + Haken über den Rand (Regentonne/Tränke/Gully) | NaturDruck · `3d-ausstiegshilfen-kleintiere` |
| `audiomoth-gehaeuse.scad` | wetterfestes Gehäuse (Unterteil + Deckel + Montage-Ohren + Mikro-Port) für AudioMoth | Lauschposten · `3d-monitoring-gehaeuse` |

## Rendern & Drucken

1. [OpenSCAD](https://openscad.org) installieren (kostenlos), Datei öffnen.
2. Parameter oben in der Datei (bzw. im Customizer) anpassen → **F6** (Render) → als STL exportieren.
   CLI: `openscad -o teil.stl modelle/wildbienen-nistblock.scad`
3. Slicen & drucken.

**Druckempfehlung (wichtig!):**
- **Material: PETG oder ASA** — UV- und witterungsfest. **Kein PLA** im Außenbereich (versprödet, verzieht sich/erweicht in der Sonne ab ~55 °C).
- Helle Farbe bei sonnenexponierten Nisthilfen (Überhitzung vermeiden).
- 3 Wandlinien, 20–30 % Infill, Schichthöhe 0,15–0,2 mm.
- Wildbienen: Bohrungen möglichst glatt (feine Schicht; bei Bedarf mit Holzbohrer nacharbeiten — keine Fransen, sonst Flügelschäden).
- AudioMoth: Mikro-Port mit schalldurchlässiger PTFE-/Gore-Membran bekleben, Deckellippe mit Dichtband/Fett.

## Hinweise zur Wirksamkeit (sonst nützt das schönste Teil nichts)

- **Wildbienen-Nistblock:** sonnig-warm, Löcher waagerecht, regengeschützt (Dachüberstand), ganzjährig stehen lassen, reinigbar halten. Ergänzt echte Bodennist-Habitate — ersetzt sie nicht (~75 % der Wildbienen nisten im Boden).
- **Ausstiegshilfe:** flach genug (≤ 45°), bis unter die Wasserlinie reichend; schwimmende Variante folgt dem Pegel.
- **AudioMoth-Gehäuse:** Maße an die konkrete Platinen-/Batteriehalter-Version anpassen (Mikro-Position prüfen!).

## Lizenz

**CERN-OHL-S** (Open Hardware) bzw. **CC-BY-SA 4.0** für die Vorlagen. Weitergeben, anpassen und
lokal/über Inklusionswerkstätten produzieren ausdrücklich erwünscht (siehe Projekt `naturdruck-baukasten-fablab`).
Beim Staat ist genau das ein Vorteil: offene Designs = kein Lock-in, lokale Wertschöpfung, Vergabe-Bonus.
