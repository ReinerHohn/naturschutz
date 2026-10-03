// Ausstiegshilfe / Rettungsrampe - parametrische Druckvorlage
// Projekt: naturdruck-baukasten-fablab / Hebel: 3d-ausstiegshilfen-kleintiere, zaeune-schaechte-fallen
// Lizenz: CERN-OHL-S bzw. CC-BY-SA 4.0
//
// Zweck: Insekten, Amphibien, Kleinsaeuger ertrinken massenhaft in Regentonnen,
// Viehtraenken, Gullys, Lichtschaechten. Eine griffige, flach genug geneigte Rampe
// mit Querstegen (Grip) und einem Haken ueber den Rand rettet sie - Cent-Betraege.
//
// Prinzip-Kennwerte:
//  - Neigung <= 45 Grad (flacher = besser), Oberflaeche griffig (Querstege)
//  - Haken/Lippe haengt ueber den Behaelterrand, Rampe reicht bis unter Wasserlinie
//  - Seitenwaende verhindern Abrutschen
//
// Druck: PETG/ASA (witterungs-/UV-fest). Schwimmfaehige Variante: an Rampenende
//  kleinen Hohlkoerper/Kork ankleben, damit sie dem Wasserstand folgt.

/* [Rampe] */
laenge      = 200;   // mm Rampenlaenge
breite      = 60;    // mm
dicke       = 3;     // mm Grundplatte
seitenwand  = 8;     // mm Hoehe Seitenwaende
/* [Grip] */
steg_hoehe  = 2.5;   // mm Querstege
steg_breite = 3;     // mm
steg_abstand= 10;    // mm Mitte-zu-Mitte
/* [Haken ueber den Rand] */
rand_dicke  = 18;    // mm Materialstaerke des Behaelterrands (z.B. Regentonne)
haken_tief  = 30;    // mm wie weit der Haken aussen herunterreicht

$fn = 32;

module grundplatte() {
    cube([breite, laenge, dicke]);
    // Seitenwaende
    cube([seitenwand, laenge, seitenwand]);
    translate([breite - seitenwand, 0, 0]) cube([seitenwand, laenge, seitenwand]);
}

module querstege() {
    n = floor(laenge / steg_abstand);
    for (i = [1:n-1])
        translate([seitenwand, i*steg_abstand, dicke])
            cube([breite - 2*seitenwand, steg_breite, steg_hoehe]);
}

module haken() {
    // U-foermiger Haken am oberen Ende, greift ueber den Behaelterrand
    translate([0, laenge, 0]) {
        cube([breite, dicke, rand_dicke + 2*dicke]);                 // Innenwange (Behaelterseite)
        translate([0, dicke + rand_dicke, 0])
            cube([breite, dicke, haken_tief]);                        // Aussenwange
        translate([0, 0, rand_dicke + dicke])
            cube([breite, dicke + rand_dicke + dicke, dicke]);        // Steg oben
    }
}

union() {
    grundplatte();
    querstege();
    haken();
}
