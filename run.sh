#!/usr/bin/env bash
# Baut beide Dashboards (Hebel-Katalog + Gruenderprojekte) und oeffnet sie.
# Nur Python-Standardbibliothek noetig.
set -e
cd "$(dirname "$0")"
python3 test.py
python3 build.py
python3 build_projekte.py
echo "Fertig:"
echo "  $(pwd)/dashboard.html   (Naturschutz-Hebel)"
echo "  $(pwd)/projekte.html    (Gruenderprojekte)"
for f in dashboard.html projekte.html; do
  if command -v xdg-open >/dev/null 2>&1; then xdg-open "$(pwd)/$f" >/dev/null 2>&1 || true
  elif command -v open >/dev/null 2>&1; then open "$(pwd)/$f" || true
  fi
done
