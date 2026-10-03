#!/usr/bin/env python3
"""Baut eine self-contained index.html als Einstieg in alle drei Ebenen:
Naturschutz-Hebel (dashboard.html), Gruenderprojekte (projekte.html) und
Pitches/Foerderantraege (antraege/). Live-Zahlen aus den JSON-Quellen.

    python3 build_index.py

Nur Python-Standardbibliothek.
"""
import json
import glob
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "index.html")

EV = {"A": 1.0, "B": 0.7, "C": 0.4}


def load(pat):
    out = []
    for f in sorted(glob.glob(os.path.join(HERE, pat))):
        try:
            out.append(json.load(open(f, encoding="utf-8")))
        except json.JSONDecodeError:
            pass
    return out


def hebel_score(h):
    return (h.get("impact", 0) - 0.6 * h.get("effort", 3)) * EV.get(h.get("evidence_level"), 0.4)


def proj_score(d):
    return (d.get("ertragspotenzial", 0) - 0.6 * d.get("aufwand", 3)) * EV.get(d.get("marktreife"), 0.4)


def li(items):
    return "".join(f"<li>{html.escape(x)}</li>" for x in items)


def main():
    hebel = load("hebel/*.json")
    proj = load("projekte/*.json")
    antraege = sorted(glob.glob(os.path.join(HERE, "antraege", "*.md")))
    n_antr = len([a for a in antraege if not os.path.basename(a).startswith(("README", "VORLAGEN"))])
    n_modelle = len(glob.glob(os.path.join(HERE, "modelle", "*.scad")))

    top_h = [h["name"] for h in sorted(hebel, key=hebel_score, reverse=True)[:5]]
    top_p = [f'{d["name"].split(" - ")[0]} — Ertrag {d.get("ertragspotenzial","–")}/5, Aufwand {d.get("aufwand","–")}/5'
             for d in sorted(proj, key=proj_score, reverse=True)[:5]]

    css = """
    :root{--bg:#0d130e;--card:#161d17;--fg:#e9ece6;--mut:#93a493;--acc:#4caf7d;--acc2:#5bb3e0;--eur:#e0a24c;--line:#263021;}
    *{box-sizing:border-box}
    body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;}
    .wrap{max-width:1080px;margin:0 auto;padding:30px 20px 80px}
    h1{font-size:30px;margin:0 0 6px}
    .lead{color:var(--mut);max-width:760px;margin:0 0 28px}
    .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
    a.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 20px;
    text-decoration:none;color:var(--fg);transition:border-color .15s,transform .15s}
    a.card:hover{border-color:var(--acc);transform:translateY(-2px)}
    .card h2{margin:0 0 4px;font-size:21px}
    .card .n{font-size:13px;color:var(--mut);margin-bottom:10px}
    .card p{margin:0;font-size:14.5px;color:#d3d9cf}
    .pill{display:inline-block;font-size:12px;padding:2px 10px;border-radius:999px;margin-bottom:10px;font-weight:700}
    .p1{background:#143024;color:var(--acc)}.p2{background:#2a1e14;color:var(--eur)}.p3{background:#14222b;color:var(--acc2)}
    .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin-top:34px}
    .box{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px}
    .box h3{margin:0 0 10px;font-size:16px}
    .box ol{margin:0;padding-left:20px}.box li{margin:5px 0;font-size:14px}
    .flow{margin-top:34px;color:var(--mut);font-size:14px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 20px}
    .flow b{color:var(--fg)}
    footer{margin-top:40px;color:var(--mut);font-size:13px}
    code{background:#0f1710;padding:2px 6px;border-radius:5px;color:var(--acc)}
    """

    page = f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Naturschutz effizient — Hebel, Projekte & Foerderantraege</title>
<style>{css}</style></head><body><div class="wrap">
<h1>\U0001f331 Naturschutz effizient</h1>
<p class="lead">Von der Wirkung zur Umsetzung in drei Ebenen: <b>was</b> am meisten bringt,
<b>wie</b> man daraus ein tragfaehiges Projekt mit 3D-Druck &amp; Open Source fuer die oeffentliche Hand macht,
und <b>womit</b> man es finanziert. Alles offline, ohne Server.</p>

<div class="cards">
  <a class="card" href="dashboard.html">
    <span class="pill p1">Ebene 1 &middot; {len(hebel)} Hebel</span>
    <h2>Hebel-Katalog</h2>
    <div class="n">dashboard.html</div>
    <p>Die wirksamsten Naturschutz-Massnahmen, nach Wirkung pro Aufwand sortiert. Low-Hanging Fruits zuerst, mit Evidenz-Level A/B/C.</p>
  </a>
  <a class="card" href="projekte.html">
    <span class="pill p2">Ebene 2 &middot; {len(proj)} Projekte</span>
    <h2>Gruenderprojekte</h2>
    <div class="n">projekte.html</div>
    <p>Aus jedem Tech-Hebel ein Geschaeftskonzept: Zugang zur oeffentlichen Hand, Open-Source-Modell, Preise, Foerderung, Break-even.</p>
  </a>
  <a class="card" href="antraege/README.md">
    <span class="pill p3">Ebene 3 &middot; {n_antr} Antraege</span>
    <h2>Pitches &amp; Foerderantraege</h2>
    <div class="n">antraege/</div>
    <p>Pro Projekt ein fertiger Pitch + foerderfertiger Antrag (Arbeitspakete, Zeitplan, Kostenplan) plus Akquise-Vorlagen fuer Behoerden.</p>
  </a>
  <a class="card" href="finanzplan.html">
    <span class="pill p2">Finanzen &middot; {len(proj)} Plaene</span>
    <h2>24-Monats-Finanzplaene</h2>
    <div class="n">finanzplan.html</div>
    <p>Durchgerechneter Betriebs-Cashflow je Projekt: Foerderung traegt die Entwicklung, danach Umsatz. Break-even, Umsatz Jahr 2, Run-Rate.</p>
  </a>
  <a class="card" href="modelle/README.md">
    <span class="pill p1">Bauen &middot; {n_modelle} Druckvorlagen</span>
    <h2>Open-Source-Druckvorlagen</h2>
    <div class="n">modelle/ (OpenSCAD)</div>
    <p>Parametrische 3D-Druck-Modelle: Wildbienen-Nistblock, Ausstiegshilfe, AudioMoth-Gehaeuse. Freie Lizenz, artgerechte Masse.</p>
  </a>
</div>

<div class="cols">
  <div class="box">
    <h3>\U0001f352 Top Low-Hanging Fruits (Wirkung/Aufwand)</h3>
    <ol>{li(top_h)}</ol>
  </div>
  <div class="box">
    <h3>\U0001f4b0 Schnell &amp; lohnend (Ertrag/Aufwand)</h3>
    <ol>{li(top_p)}</ol>
  </div>
</div>

<div class="flow">
<b>Roter Faden:</b> Hebel waehlen (Ebene 1) &rarr; passenden Tech-Hebel zum Projekt machen (Ebene 2) &rarr;
Pilot bei einer Behoerde gewinnen &amp; ueber Foerderung/Direktauftrag finanzieren (Ebene 3). &nbsp;
Open Source ist beim Staat ein <b>Verkaufsargument</b> (kein Lock-in, digitale Souveraenitaet); Geld kommt aus
Hardware, Betrieb, SaaS und Foerderung &mdash; nicht aus Lizenzen. 3D-Druck senkt Stueckkosten und erlaubt lokale Produktion.
</div>

<footer>Bauen &amp; oeffnen: <code>./start.sh</code> (oder <code>./run.sh</code>). Alle Seiten sind self-contained (nur Python-Standardbibliothek).
Keine Rechts-/Steuer-/Foerderberatung. Siehe LIMITATIONEN.md.</footer>
</div></body></html>"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"geschrieben: {OUT} ({len(page)//1024} KB) — {len(hebel)} Hebel, {len(proj)} Projekte, {n_antr} Antraege")


if __name__ == "__main__":
    main()
