#!/usr/bin/env bash
# Baut alles (Tests + beide Dashboards + Landing-Index) und oeffnet die Startseite.
# Nur Python-Standardbibliothek noetig.
set -e
cd "$(dirname "$0")"
python3 test.py
python3 build.py
python3 build_projekte.py
python3 build_index.py
OUT="$(pwd)/index.html"
echo "Fertig. Start: $OUT"
if command -v xdg-open >/dev/null 2>&1; then xdg-open "$OUT" >/dev/null 2>&1 || true
elif command -v open >/dev/null 2>&1; then open "$OUT" || true
fi
