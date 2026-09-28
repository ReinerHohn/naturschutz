#!/usr/bin/env python3
"""Tests fuer den Naturschutz-Katalog. Nur Standardbibliothek.

    python3 test.py

Prueft: JSON valide, Pflichtfelder, id == Dateiname, Evidenz-Level in A/B/C,
impact/effort im Bereich 1-5, Kategorien bekannt, Quellen-URLs plausibel,
und dass build.py ohne Validierungsfehler durchlaeuft.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HEBEL_DIR = os.path.join(HERE, "hebel")

REQUIRED = ["id", "name", "category", "summary", "protocol"]
LEVELS = {"A", "B", "C"}
CATEGORIES = {
    "Vernetzung & Korridore",
    "Insekten & Bestäuber",
    "Garten & Siedlung",
    "Landwirtschaft & Fläche",
    "Gewässer & Feuchtgebiete",
    "Wald & Totholz",
    "Gefahren & Fallen",
    "Politik & System-Hebel",
}

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def main():
    paths = sorted(glob.glob(os.path.join(HEBEL_DIR, "*.json")))
    check(len(paths) >= 1, "keine Hebel gefunden")
    ids = set()
    for path in paths:
        base = os.path.basename(path)
        try:
            with open(path, encoding="utf-8") as f:
                d = json.load(f)
        except json.JSONDecodeError as e:
            fails.append(f"{base}: ungueltiges JSON ({e})")
            continue

        for field in REQUIRED:
            check(bool(d.get(field)), f"{base}: Pflichtfeld '{field}' fehlt/leer")

        check(d.get("id") == base[:-5], f"{base}: id '{d.get('id')}' != Dateiname")
        check(d.get("id") not in ids, f"{base}: doppelte id '{d.get('id')}'")
        ids.add(d.get("id"))

        if d.get("category"):
            check(d["category"] in CATEGORIES, f"{base}: unbekannte Kategorie '{d['category']}'")
        if d.get("evidence_level"):
            check(d["evidence_level"] in LEVELS, f"{base}: evidence_level nicht A/B/C")
        for k in ("impact", "effort"):
            if d.get(k) is not None:
                check(isinstance(d[k], int) and 1 <= d[k] <= 5, f"{base}: {k} nicht 1..5")

        check(isinstance(d.get("protocol"), list) and len(d["protocol"]) >= 1,
              f"{base}: protocol muss nicht-leere Liste sein")

        for kf in d.get("key_facts", []):
            check("label" in kf and "value" in kf, f"{base}: key_fact ohne label/value")
        for ev in d.get("evidence", []):
            check("source" in ev and "finding" in ev, f"{base}: evidence ohne source/finding")
        for s in d.get("sources", []):
            url = s.get("url", "")
            check(url.startswith("http"), f"{base}: Quelle ohne http-URL ({s.get('title','?')})")

    rc = os.system(f"cd {HERE} && python3 build.py --check >/dev/null 2>&1")
    check(rc == 0, "build.py --check meldet Validierungsfehler")

    if fails:
        print(f"FEHLGESCHLAGEN ({len(fails)}):")
        for m in fails:
            print("  -", m)
        sys.exit(1)
    print(f"OK: {len(ids)} Hebel, alle Checks bestanden.")


if __name__ == "__main__":
    main()
