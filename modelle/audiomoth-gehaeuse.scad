// AudioMoth-Gehaeuse (wetterfest) - parametrische Druckvorlage
// Projekt: lauschposten-bioakustik / Hebel: 3d-monitoring-gehaeuse, bioakustik-monitoring-ki
// Lizenz: CERN-OHL-S bzw. CC-BY-SA 4.0
//
// Senkt die Kosten pro Messpunkt drastisch: ein gedrucktes Case kostet ~2-3 EUR
// Material statt teurer Spezialgehaeuse. AudioMoth-Platine ca. 58 x 48 mm.
//
// Enthalten: Unterteil mit Standoffs + Mikro-Port, Deckel mit umlaufender Lippe,
// Montage-Ohren mit Loechern. Fuer echten Wetterschutz: Mikro-Port mit
// Gore-/PTFE-Membran bekleben (schalldurchlaessig, wasserdicht) und Lippe mit
// duennem Dichtband/Fett versehen. Druck: PETG/ASA, 3 Wandlinien, 20-30% Infill.

/* [Platine] */
pcb_x       = 58;   // mm
pcb_y       = 48;   // mm
pcb_rand    = 3;    // mm Luft rundum
/* [Gehaeuse] */
wand        = 2.4;  // mm Wandstaerke
hoehe_innen = 22;   // mm Innenhoehe (Platine + AA-Batterien/Halter)
boden       = 2.4;  // mm
lippe       = 4;    // mm Ueberlappung Deckel/Unterteil
/* [Mikrofon-Port] */
mic_x       = 44;   // Position ab Innenkante (an Platinen-Mikro anpassen!)
mic_y       = 8;
mic_d       = 4;    // mm Portdurchmesser
/* [Montage] */
ohren       = true;
ohr_loch    = 4.5;  // mm (M4 / Kabelbinder)

$fn = 48;
ix = pcb_x + 2*pcb_rand;      // Innenmass
iy = pcb_y + 2*pcb_rand;
ox = ix + 2*wand;             // Aussenmass
oy = iy + 2*wand;

module box(w, d, h, r=3) {   // abgerundeter Quader (Grundflaeche)
    linear_extrude(h)
        offset(r) offset(-r) square([w, d]);
}

module unterteil() {
    difference() {
        box(ox, oy, boden + hoehe_innen);
        translate([wand, wand, boden]) box(ix, iy, hoehe_innen + 1);
        // Mikro-Port
        translate([wand + mic_x, wand + mic_y, -1]) cylinder(h = boden + 2, d = mic_d);
    }
    // Standoffs fuer die Platine (4 Ecken), 3 mm hoch, mit 1.8 mm Pilotloch
    for (sx = [wand + pcb_rand + 2, wand + pcb_rand + pcb_x - 2])
        for (sy = [wand + pcb_rand + 2, wand + pcb_rand + pcb_y - 2])
            translate([sx, sy, boden]) difference() {
                cylinder(h = 3, d = 5);
                translate([0,0,-0.1]) cylinder(h = 3.5, d = 1.8);
            }
    if (ohren) ohrenpaar(boden + hoehe_innen);
}

module ohrenpaar(h) {
    for (my = [oy*0.25, oy*0.75])
        translate([-10, my, 0]) difference() {
            hull() {
                cube([0.1, 12, 4]);
                translate([-6, 6, 0]) cylinder(h = 4, d = 12);
            }
            translate([-6, 6, -1]) cylinder(h = 6, d = ohr_loch);
        }
}

module deckel() {
    translate([0, oy + 10, 0]) {
        box(ox, oy, wand);
        // Innenlippe, die in das Unterteil greift
        translate([wand + 0.3, wand + 0.3, wand])
            difference() {
                box(ix - 0.6, iy - 0.6, lippe);
                translate([wand, wand, -0.1]) box(ix - 0.6 - 2*wand, iy - 0.6 - 2*wand, lippe + 0.2);
            }
    }
}

unterteil();
deckel();
