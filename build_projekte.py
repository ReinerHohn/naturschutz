#!/usr/bin/env python3
"""Baut aus projekte/*.json ein durchsuchbares, self-contained projekte.html.

Gruender-/Projekt-Katalog: wie man aus den Naturschutz-Tech-Hebeln (hebel/)
Produkte macht, die mit 3D-Druck + Open Source die oeffentliche Hand bedienen
und sich finanziell tragen. Nur Python-Standardbibliothek.

    python3 build_projekte.py            # baut projekte.html + PROJEKTE.md
    python3 build_projekte.py --check    # nur validieren
"""
import json
import glob
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.join(HERE, "projekte")
OUT = os.path.join(HERE, "projekte.html")
MD = os.path.join(HERE, "PROJEKTE.md")

REQUIRED = ["id", "name", "pitch", "solution", "geschaeftsmodell"]
LEVELS = {"A", "B", "C"}

CATEGORY_ORDER = [
    "Monitoring-SaaS & Service",
    "Open Hardware & 3D-Druck",
    "Software & Plattform",
    "Beratung & Planung",
]

MR_WEIGHT = {"A": 1.0, "B": 0.7, "C": 0.4}


def load():
    items, errors = [], []
    for path in sorted(glob.glob(os.path.join(PROJ_DIR, "*.json"))):
        base = os.path.basename(path)
        try:
            with open(path, encoding="utf-8") as f:
                d = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{base}: ungueltiges JSON ({e})")
            continue
        for field in REQUIRED:
            if not d.get(field):
                errors.append(f"{base}: Pflichtfeld '{field}' fehlt/leer")
        if d.get("id") and d["id"] != base[:-5]:
            errors.append(f"{base}: id '{d['id']}' != Dateiname")
        if d.get("marktreife") and d["marktreife"] not in LEVELS:
            errors.append(f"{base}: marktreife '{d['marktreife']}' nicht in A/B/C")
        items.append(d)
    return items, errors


def score(d):
    mr = MR_WEIGHT.get(d.get("marktreife"), 0.4)
    return (d.get("ertragspotenzial", 0) - 0.6 * d.get("aufwand", 3)) * mr


def cat_key(d):
    c = d.get("category", "")
    idx = CATEGORY_ORDER.index(c) if c in CATEGORY_ORDER else len(CATEGORY_ORDER)
    return (idx, -(d.get("ertragspotenzial") or 0), d.get("name", ""))


CSS = """
:root{--bg:#0d1016;--card:#161a22;--card2:#1e2430;--fg:#e9ecf2;--mut:#93a0b4;
--acc:#e0a24c;--acc2:#5bb3e0;--a:#4caf7d;--b:#e0a24c;--c:#8a8f99;--line:#263040;--eur:#4caf7d;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
header{padding:26px 20px 10px;max-width:1180px;margin:0 auto}
h1{margin:0 0 4px;font-size:26px}
.sub{color:var(--mut);max-width:860px}
.controls{position:sticky;top:0;z-index:5;background:var(--bg);
padding:12px 20px;max-width:1180px;margin:0 auto;border-bottom:1px solid var(--line)}
#q{width:100%;padding:11px 13px;border-radius:10px;border:1px solid var(--line);
background:var(--card);color:var(--fg);font-size:15px}
.chips{margin-top:10px;display:flex;flex-wrap:wrap;gap:7px}
.chip{padding:5px 12px;border-radius:999px;border:1px solid var(--line);
background:var(--card);color:var(--mut);cursor:pointer;font-size:13px;user-select:none}
.chip.on{background:var(--acc);border-color:var(--acc);color:#1a1200}
.count{color:var(--mut);font-size:13px;margin-left:auto;align-self:center}
main{max-width:1180px;margin:0 auto;padding:16px 20px 80px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
padding:16px 16px 14px;display:flex;flex-direction:column;gap:8px}
.card h3{margin:0;font-size:19px}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.badge{font-size:11px;padding:2px 8px;border-radius:6px;background:var(--card2);color:var(--mut)}
.ev{font-weight:700;color:#111}
.ev.A{background:var(--a)}.ev.B{background:var(--b)}.ev.C{background:var(--c)}
.cat{background:transparent;border:1px solid var(--line);color:var(--acc2)}
.eur{color:var(--eur);font-weight:700}
.auf{color:var(--acc)}
.pitch{color:var(--fg);font-weight:600}
.facts{list-style:none;padding:0;margin:2px 0 0;font-size:13.5px}
.facts li{padding:3px 0;border-top:1px solid var(--line);display:flex;gap:8px}
.facts li:first-child{border-top:0}
.facts .fl{color:var(--mut);flex:0 0 42%}
.facts .fv{flex:1}
details{border-top:1px solid var(--line);padding-top:8px;margin-top:2px}
summary{cursor:pointer;color:var(--acc2);font-size:14px;list-style:none}
summary::-webkit-details-marker{display:none}
summary:before{content:"\\25b8 ";color:var(--mut)}
details[open] summary:before{content:"\\25be "}
.dd{font-size:14px;color:#d6dae2}
h4.sec{margin:12px 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.5px;color:var(--mut)}
ul.lst{margin:4px 0;padding-left:18px;font-size:14px}
ul.lst li{margin:3px 0}
.src a{color:var(--acc2);text-decoration:none;font-size:13px}
.src a:hover{text-decoration:underline}
.risk{background:#2a1e14;border-left:3px solid var(--acc);padding:8px 10px;border-radius:6px;font-size:13.5px}
.hl2{background:#10251a;border-left:3px solid var(--eur);padding:8px 10px;border-radius:6px;font-size:13.5px}
footer{max-width:1180px;margin:0 auto;padding:0 20px 60px;color:var(--mut);font-size:13px}
mark{background:#5a4b00;color:#fff;border-radius:2px}
.sweet{max-width:1180px;margin:0 auto 6px;padding:14px 20px 6px}
.sweet h2{font-size:16px;margin:0 0 4px}
.ss-note{color:var(--mut);font-size:13px;margin:0 0 10px}
.ss-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:8px}
.ss-item{display:flex;align-items:flex-start;gap:10px;background:#141b24;border:1px solid var(--line);border-radius:8px;padding:8px 10px;cursor:pointer}
.ss-item:hover{border-color:var(--acc)}
.ss-rank{font-weight:700;color:var(--acc);width:20px;text-align:center;flex:none}
.ss-name{font-size:14px}
.ss-meta{font-size:12px;color:var(--mut);margin-top:2px}
"""

JS = """
const DATA = __DATA__;
const state={q:"",cat:"Alle"};
const grid=document.getElementById('grid');
const count=document.getElementById('count');
function esc(s){return (s||"").replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function hl(s){if(!state.q)return esc(s);const q=state.q.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&');
return esc(s).replace(new RegExp('('+q+')','ig'),'<mark>$1</mark>');}
function matches(d){
  if(state.cat!=="Alle"&&d.category!==state.cat)return false;
  if(!state.q)return true;
  const blob=[d.name,d.pitch,d.problem,d.solution,d.geschaeftsmodell,d.open_source_hebel,d.druck_hebel,
    d.category,(d.aka||[]).join(' '),(d.tags||[]).join(' '),(d.einnahmequellen||[]).join(' '),
    (d.oeffentliche_hand||[]).join(' '),(d.vorbilder||[]).join(' '),(d.foerderung||[]).join(' '),
    (d.schritte||[]).join(' ')].join(' ').toLowerCase();
  return blob.includes(state.q.toLowerCase());
}
function price(d){return (d.preismodell||[]).map(f=>
  `<li><span class="fl">${esc(f.label)}</span><span class="fv">${hl(f.value)}</span></li>`).join('');}
function list(arr){return (arr||[]).map(x=>`<li>${hl(x)}</li>`).join('');}
function sources(d){return (d.sources||[]).map(s=>
  `<div class="src"><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a></div>`).join('');}
function card(d){
  return `<div class="card">
    <div class="meta">
      ${d.marktreife?`<span class="badge ev ${d.marktreife}">Markt ${d.marktreife}</span>`:''}
      <span class="badge cat">${esc(d.category||'')}</span>
      ${d.ertragspotenzial?`<span class="badge eur">Ertrag ${d.ertragspotenzial}/5</span>`:''}
      ${d.aufwand?`<span class="badge auf">Aufwand ${d.aufwand}/5</span>`:''}
      ${d.mvp_zeit?`<span class="badge">MVP: ${esc(d.mvp_zeit)}</span>`:''}
    </div>
    <h3>${hl(d.name)}</h3>
    ${d.based_on?`<div class="badge">basiert auf: ${esc(d.based_on)}</div>`:''}
    <div class="pitch">${hl(d.pitch)}</div>
    ${d.preismodell?`<ul class="facts">${price(d)}</ul>`:''}
    <details><summary>Businessplan: Markt, oeffentliche Hand, Geld &amp; Schritte</summary>
      ${d.problem?`<h4 class="sec">Problem / Bedarf</h4><div class="dd">${hl(d.problem)}</div>`:''}
      ${d.solution?`<h4 class="sec">Loesung (Open Source + 3D-Druck)</h4><div class="dd">${hl(d.solution)}</div>`:''}
      ${(d.oeffentliche_hand&&d.oeffentliche_hand.length)?`<h4 class="sec">Zugang zur oeffentlichen Hand</h4><ul class="lst">${list(d.oeffentliche_hand)}</ul>`:''}
      ${d.open_source_hebel?`<h4 class="sec">Open-Source-Hebel</h4><div class="dd">${esc(d.open_source_hebel)}</div>`:''}
      ${d.druck_hebel?`<h4 class="sec">3D-Druck-Hebel</h4><div class="dd">${esc(d.druck_hebel)}</div>`:''}
      ${d.geschaeftsmodell?`<h4 class="sec">Geschaeftsmodell</h4><div class="hl2">${esc(d.geschaeftsmodell)}</div>`:''}
      ${(d.einnahmequellen&&d.einnahmequellen.length)?`<h4 class="sec">Einnahmequellen</h4><ul class="lst">${list(d.einnahmequellen)}</ul>`:''}
      ${d.kosten_breakeven?`<h4 class="sec">Kosten &amp; Break-even</h4><div class="dd">${esc(d.kosten_breakeven)}</div>`:''}
      ${(d.foerderung&&d.foerderung.length)?`<h4 class="sec">Passende Foerderung</h4><ul class="lst">${list(d.foerderung)}</ul>`:''}
      ${(d.vorbilder&&d.vorbilder.length)?`<h4 class="sec">Vorbilder / Markt-Beleg</h4><div class="dd">${esc(d.vorbilder.join(', '))}</div>`:''}
      ${(d.schritte&&d.schritte.length)?`<h4 class="sec">Naechste Schritte (90 Tage)</h4><ul class="lst">${list(d.schritte)}</ul>`:''}
      ${d.risiken?`<h4 class="sec">Risiken</h4><div class="risk">${esc(d.risiken)}</div>`:''}
      ${(d.synergy&&d.synergy.length)?`<h4 class="sec">Kombiniert mit</h4><div class="dd">${esc(d.synergy.join(', '))}</div>`:''}
      ${d.sources?`<h4 class="sec">Quellen</h4>${sources(d)}`:''}
    </details>
  </div>`;
}
function render(){
  const vis=DATA.filter(matches);
  grid.innerHTML=vis.map(card).join('')||'<p style="color:var(--mut)">Nichts gefunden.</p>';
  count.textContent=vis.length+' / '+DATA.length+' Projekte';
}
document.getElementById('q').addEventListener('input',e=>{state.q=e.target.value;render();});
document.querySelectorAll('.chip').forEach(c=>c.addEventListener('click',()=>{
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  c.classList.add('on');state.cat=c.dataset.cat;render();}));
document.querySelectorAll('.ss-item').forEach(el=>el.addEventListener('click',()=>{
  const q=document.getElementById('q');q.value=el.dataset.q;state.q=el.dataset.q;
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  const all=document.querySelector('.chip[data-cat="Alle"]');if(all)all.classList.add('on');
  state.cat="Alle";render();
  document.querySelector('main').scrollIntoView({behavior:'smooth',block:'start'});}));
render();
"""


def sweet_html(items, n=6):
    ranked = sorted(items, key=score, reverse=True)[:n]
    li = []
    for i, d in enumerate(ranked, 1):
        nm = html.escape(d.get("name", ""))
        meta = (f"Ertrag {d.get('ertragspotenzial','–')}/5 &middot; Aufwand {d.get('aufwand','–')}/5 "
                f"&middot; Markt {d.get('marktreife','–')} &middot; MVP {html.escape(d.get('mvp_zeit',''))}")
        li.append(f'<li class="ss-item" data-q="{nm}"><span class="ss-rank">{i}</span>'
                  f'<span><span class="ss-name">{nm}</span><div class="ss-meta">{meta}</div></span></li>')
    return ('<section class="sweet"><h2>\U0001f4b0 Schnell &amp; lohnend &ndash; bestes Verhaeltnis '
            'Ertrag / Aufwand / Marktreife</h2>'
            '<p class="ss-note">Automatisch gerankt: hohes finanzielles Potenzial, wenig Aufwand, belegter Markt. '
            'Klick filtert die Liste.</p>'
            f'<ol class="ss-list">{"".join(li)}</ol></section>')


def build(items):
    items = sorted(items, key=cat_key)
    cats = ["Alle"] + [c for c in CATEGORY_ORDER if any(d.get("category") == c for d in items)]
    chips = "".join(
        f'<span class="chip{" on" if c=="Alle" else ""}" data-cat="{html.escape(c)}">{html.escape(c)}</span>'
        for c in cats)
    js = JS.replace("__DATA__", json.dumps(items, ensure_ascii=False))
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Naturschutz-Gruenderprojekte - 3D-Druck, Open Source & oeffentliche Hand</title>
<style>{CSS}</style></head><body>
<header>
<h1>\U0001f4b0 Gruenderprojekte &ndash; Naturschutz mit 3D-Druck &amp; Open Source</h1>
<div class="sub">Aus jedem Tech-Hebel ein Projekt: wie man mit 3D-Druck und offener Technik auf Kommunen,
Umwelt- und Naturschutzbehoerden zugeht &ndash; und dabei Geld verdient. Je Karte: Markt, Zugang zur
oeffentlichen Hand, Open-Source-Geschaeftsmodell, Preise, Foerderung, Break-even und die ersten 90 Tage.
Sortiert nach Ertrag pro Aufwand.</div>
</header>
<div class="controls">
<input id="q" placeholder="Suchen: Monitoring, Kommune, Foerderung, SaaS, Ausgleich, Vergabe ...">
<div class="chips">{chips}<span class="count" id="count"></span></div>
</div>
{sweet_html(items)}
<main><div class="grid" id="grid"></div></main>
<footer>{len(items)} Projekte &middot; Markt-Reife: A = vergleichbare Firmen existieren, B = Pilotmarkt, C = frueh/Hypothese.
Ertrag/Aufwand sind Einschaetzungen, keine Prognosen &ndash; keine Rechts-/Steuer-/Anlageberatung. Siehe LIMITATIONEN.md.</footer>
<script>{js}</script></body></html>"""


def md_projekte(items):
    items = sorted(items, key=cat_key)
    out = ["# Gruenderprojekte — Naturschutz mit 3D-Druck & Open Source\n"]
    out.append("_Automatisch aus `projekte/*.json` erzeugt (`python3 build_projekte.py`)._\n")
    out.append(f"**{len(items)} Projekte.** Marktreife: **A** = vergleichbare Firmen existieren, "
               "**B** = Pilotmarkt, **C** = frueh. Keine Rechts-/Steuer-/Anlageberatung.\n")
    out.append("## 💰 Schnell & lohnend — bestes Verhaeltnis Ertrag / Aufwand / Marktreife\n")
    out.append("_Score = (Ertrag − 0,6·Aufwand) × Marktgewicht (A=1,0 · B=0,7 · C=0,4)._\n")
    out.append("| # | Projekt | Ertrag | Aufwand | Markt | MVP |")
    out.append("|---|---|:---:|:---:|:---:|---|")
    for i, d in enumerate(sorted(items, key=score, reverse=True)[:10], 1):
        out.append(f"| {i} | **{d['name']}** (`{d['id']}`) | {d.get('ertragspotenzial','–')}/5 "
                   f"| {d.get('aufwand','–')}/5 | {d.get('marktreife','–')} | {d.get('mvp_zeit','')} |")
    out.append("")
    cats = [c for c in CATEGORY_ORDER if any(d.get("category") == c for d in items)]

    def bl(title, arr):
        if not arr:
            return
        out.append(f"**{title}**\n")
        for x in arr:
            out.append(f"- {x}")
        out.append("")

    for c in cats:
        out.append(f"\n## {c}\n")
        for d in [x for x in items if x.get("category") == c]:
            out.append(f"### {d['name']}\n")
            meta = []
            if d.get("marktreife"):
                meta.append(f"Markt **{d['marktreife']}**")
            if d.get("ertragspotenzial"):
                meta.append(f"Ertrag {d['ertragspotenzial']}/5")
            if d.get("aufwand"):
                meta.append(f"Aufwand {d['aufwand']}/5")
            if d.get("mvp_zeit"):
                meta.append(f"MVP {d['mvp_zeit']}")
            meta.append(f"`{d['id']}`")
            out.append(" · ".join(meta) + "\n")
            out.append("**" + d["pitch"] + "**\n")
            if d.get("problem"):
                out.append(f"_Problem:_ {d['problem']}\n")
            if d.get("solution"):
                out.append(f"_Loesung:_ {d['solution']}\n")
            bl("Zugang zur oeffentlichen Hand", d.get("oeffentliche_hand"))
            if d.get("open_source_hebel"):
                out.append(f"**Open-Source-Hebel:** {d['open_source_hebel']}\n")
            if d.get("druck_hebel"):
                out.append(f"**3D-Druck-Hebel:** {d['druck_hebel']}\n")
            if d.get("geschaeftsmodell"):
                out.append(f"**Geschaeftsmodell:** {d['geschaeftsmodell']}\n")
            bl("Einnahmequellen", d.get("einnahmequellen"))
            if d.get("preismodell"):
                out.append("| Preis / Kennzahl | Wert |")
                out.append("|---|---|")
                for p in d["preismodell"]:
                    out.append(f"| {p['label']} | {p['value'].replace('|','\\|')} |")
                out.append("")
            if d.get("kosten_breakeven"):
                out.append(f"**Kosten & Break-even:** {d['kosten_breakeven']}\n")
            bl("Passende Foerderung", d.get("foerderung"))
            if d.get("vorbilder"):
                out.append(f"**Vorbilder:** {', '.join(d['vorbilder'])}\n")
            bl("Naechste Schritte (90 Tage)", d.get("schritte"))
            if d.get("risiken"):
                out.append(f"> ⚠️ **Risiken:** {d['risiken']}\n")
            if d.get("sources"):
                out.append("**Quellen:** " + " · ".join(
                    f"[{s.get('title','Link')}]({s['url']})" for s in d["sources"] if s.get("url")) + "\n")
            out.append("---\n")
    return "\n".join(out)


def main():
    items, errors = load()
    if errors:
        print("VALIDIERUNGSFEHLER:")
        for e in errors:
            print("  -", e)
    print(f"{len(items)} Projekte geladen.")
    if "--check" in sys.argv:
        sys.exit(1 if errors else 0)
    page = build(items)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"geschrieben: {OUT} ({len(page)//1024} KB)")
    md = md_projekte(items)
    with open(MD, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"geschrieben: {MD} ({len(md)//1024} KB)")


if __name__ == "__main__":
    main()
