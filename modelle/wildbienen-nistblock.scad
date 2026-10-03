// Wildbienen-Nistblock - parametrische, artgerechte Druckvorlage
// Projekt: naturdruck-baukasten-fablab / Hebel: 3d-wildbienen-nistblock, wildbienen-nisthabitat
// Lizenz: CERN-OHL-S (Open Hardware) bzw. CC-BY-SA 4.0
//
// Biologisch korrekt (das ist der eigentliche Wert, nicht "3D-gedruckt"):
//  - Lochdurchmesser gemischt 3-8 mm (verschiedene Arten), Schwerpunkt 4-6 mm
//  - Tiefe >= 10 cm, hinten GESCHLOSSEN (Sackloch) - Durchzug = unbesiedelt
//  - Innenwand glatt, Eingang gefast/entgratet (keine Fransen -> sonst Fluegelschaeden)
//  - herausnehmbar/reinigbar gedacht: dieser Block ist ein Einsatz fuer ein Schutzdach
//
// Druck: PETG oder ASA (UV-/witterungsfest; KEIN PLA - versproedet/schmilzt in Sonne).
//  Hohlraeume liegend drucken waere besser fuer glatte Bohrung -> hier stehend mit
//  feiner Schicht (0.15 mm) + ggf. Bohrung mit Holzbohrer glatt nacharbeiten.

/* [Block] */
block_breite   = 120;   // mm
block_hoehe    = 120;   // mm
block_tiefe    = 115;   // mm (Lochtiefe = tiefe - rueckwand)
rueckwand      = 8;     // mm geschlossene Rueckwand
/* [Loecher] */
durchmesser    = [3, 4, 5, 6, 7, 8]; // gemischte Groessen (werden zyklisch verteilt)
rand           = 12;    // Randabstand mm
min_abstand    = 6;     // Mindest-Stegbreite zwischen Loechern mm
fase           = 1.2;   // Eingangsfase mm
/* [Aufhaengung] */
aufhaengung    = true;
loch_oben      = 7;     // Durchmesser Aufhaengeloch mm

$fn = 48;
loch_tiefe = block_tiefe - rueckwand;
max_d = max(durchmesser);
raster = max_d + min_abstand;           // einheitliches Raster nach groesstem Loch
nx = floor((block_breite - 2*rand) / raster) + 1;
ny = floor((block_hoehe  - 2*rand) / raster) + 1;
off_x = (block_breite - (nx-1)*raster)/2;
off_y = (block_hoehe  - (ny-1)*raster)/2;

module loch(d) {
    // Sackloch von vorne (y = tiefe) nach hinten, bleibt rueckwand stehen
    translate([0, block_tiefe + 0.1, 0])
        rotate([90,0,0])
            cylinder(h = loch_tiefe + 0.1, d = d);
    // Eingangsfase
    translate([0, block_tiefe + 0.1, 0])
        rotate([90,0,0])
            cylinder(h = fase + 0.1, d1 = d + 2*fase, d2 = d);
}

difference() {
    cube([block_breite, block_tiefe, block_hoehe]);
    for (ix = [0:nx-1])
        for (iy = [0:ny-1]) {
            idx = (ix + iy*nx) % len(durchmesser);
            translate([off_x + ix*raster, 0, off_y + iy*raster])
                loch(durchmesser[idx]);
        }
    if (aufhaengung)
        translate([block_breite/2, -1, block_hoehe - rand/2])
            rotate([-90,0,0]) cylinder(h = rueckwand + 2, d = loch_oben);
}

// Hinweis fuers Aufstellen (nur Kommentar): sonnig-warm, Loecher waagerecht/leicht
// geneigt, regengeschuetzt (Dachueberstand), bodennah bis 1.5 m, ganzjaehrig stehen lassen.
