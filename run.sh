#!/usr/bin/env bash
# Baut das Dashboard und oeffnet es (Linux/macOS). Nur Standardbibliothek noetig.
set -e
cd "$(dirname "$0")"
python3 test.py
python3 build.py
OUT="$(pwd)/dashboard.html"
echo "Fertig: $OUT"
if command -v xdg-open >/dev/null 2>&1; then xdg-open "$OUT" >/dev/null 2>&1 || true
elif command -v open >/dev/null 2>&1; then open "$OUT" || true
fi
