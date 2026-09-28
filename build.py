#!/usr/bin/env python3
"""Baut aus hebel/*.json ein durchsuchbares, self-contained dashboard.html.

Nur Python-Standardbibliothek. Aufruf:

    python3 build.py            # baut dashboard.html + KATALOG.md
    python3 build.py --check    # nur validieren, nichts schreiben

Design-Prinzipien (Baumuster wie ../leistungsfaehigkeit, ../flirt):
- eine Karte = ein Naturschutz-Hebel (hebel/<id>.json)
- Evidenz-Level A/B/C ehrlich ausgewiesen, Anti-Hype
- nach Wirkung/Aufwand sortiert: Low-Hanging Fruits zuerst
- alles inline (CSS+JS+Daten) -> HTML laeuft ohne Server/Netz
"""
import json
import glob
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HEBEL_DIR = os.path.join(HERE, "hebel")
OUT = os.path.join(HERE, "dashboard.html")

REQUIRED = ["id", "name", "category", "summary", "protocol"]
LEVELS = {"A", "B", "C"}

CATEGORY_ORDER = [
    "Vernetzung & Korridore",
    "Insekten & Bestäuber",
    "Garten & Siedlung",
    "Landwirtschaft & Fläche",
    "Gewässer & Feuchtgebiete",
    "Wald & Totholz",
    "Gefahren & Fallen",
    "Politik & System-Hebel",
]


def load_hebel():
    hebel, errors = [], []
    for path in sorted(glob.glob(os.path.join(HEBEL_DIR, "*.json"))):
        base = os.path.basename(path)
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{base}: ungueltiges JSON ({e})")
            continue
        for field in REQUIRED:
            if not data.get(field):
                errors.append(f"{base}: Pflichtfeld '{field}' fehlt/leer")
        if data.get("id") and data["id"] != base[:-5]:
            errors.append(f"{base}: id '{data['id']}' != Dateiname")
        if data.get("evidence_level") and data["evidence_level"] not in LEVELS:
            errors.append(f"{base}: evidence_level '{data['evidence_level']}' nicht in A/B/C")
        hebel.append(data)
    return hebel, errors


def cat_key(h):
    c = h.get("category", "")
    idx = CATEGORY_ORDER.index(c) if c in CATEGORY_ORDER else len(CATEGORY_ORDER)
    return (idx, -(h.get("impact") or 0), h.get("name", ""))


CSS = """
:root{--bg:#0e1410;--card:#161d17;--card2:#1d261e;--fg:#e8ece6;--mut:#96a496;
--acc:#4caf7d;--acc2:#7bc47f;--a:#4caf7d;--b:#e0a24c;--c:#8a8f99;--line:#28321f;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
header{padding:26px 20px 10px;max-width:1180px;margin:0 auto}
h1{margin:0 0 4px;font-size:26px}
.sub{color:var(--mut);max-width:820px}
.controls{position:sticky;top:0;z-index:5;background:var(--bg);
padding:12px 20px;max-width:1180px;margin:0 auto;border-bottom:1px solid var(--line)}
#q{width:100%;padding:11px 13px;border-radius:10px;border:1px solid var(--line);
background:var(--card);color:var(--fg);font-size:15px}
.chips{margin-top:10px;display:flex;flex-wrap:wrap;gap:7px}
.chip{padding:5px 12px;border-radius:999px;border:1px solid var(--line);
background:var(--card);color:var(--mut);cursor:pointer;font-size:13px;user-select:none}
.chip.on{background:var(--acc);border-color:var(--acc);color:#08120b}
.count{color:var(--mut);font-size:13px;margin-left:auto;align-self:center}
main{max-width:1180px;margin:0 auto;padding:16px 20px 80px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
padding:16px 16px 14px;display:flex;flex-direction:column;gap:8px}
.card h3{margin:0;font-size:18px}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.badge{font-size:11px;padding:2px 8px;border-radius:6px;background:var(--card2);color:var(--mut)}
.ev{font-weight:700;color:#08120b}
.ev.A{background:var(--a)}.ev.B{background:var(--b)}.ev.C{background:var(--c)}
.cat{background:transparent;border:1px solid var(--line);color:var(--acc2)}
.imp{color:var(--acc2)}
.sum{color:var(--fg)}
.facts{list-style:none;padding:0;margin:2px 0 0;font-size:13.5px}
.facts li{padding:3px 0;border-top:1px solid var(--line);display:flex;gap:8px}
.facts li:first-child{border-top:0}
.facts .fl{color:var(--mut);flex:0 0 40%}
.facts .fv{flex:1}
details{border-top:1px solid var(--line);padding-top:8px;margin-top:2px}
summary{cursor:pointer;color:var(--acc2);font-size:14px;list-style:none}
summary::-webkit-details-marker{display:none}
summary:before{content:"\\25b8 ";color:var(--mut)}
details[open] summary:before{content:"\\25be "}
.dd{font-size:14px;color:#d3d9cf}
h4.sec{margin:12px 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.5px;color:var(--mut)}
ul.lst{margin:4px 0;padding-left:18px;font-size:14px}
ul.lst li{margin:3px 0}
.src a{color:var(--acc2);text-decoration:none;font-size:13px}
.src a:hover{text-decoration:underline}
.risk{background:#2a1e14;border-left:3px solid var(--b);padding:8px 10px;border-radius:6px;font-size:13.5px}
footer{max-width:1180px;margin:0 auto;padding:0 20px 60px;color:var(--mut);font-size:13px}
.hidden{display:none!important}
mark{background:#3d5a00;color:#fff;border-radius:2px}
.sweet{max-width:1180px;margin:0 auto 6px;padding:14px 20px 6px}
.sweet h2{font-size:16px;margin:0 0 4px}
.ss-note{color:var(--mut);font-size:13px;margin:0 0 10px}
.ss-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:8px}
.ss-item{display:flex;align-items:flex-start;gap:10px;background:#141b15;border:1px solid var(--line);border-radius:8px;padding:8px 10px;cursor:pointer}
.ss-item:hover{border-color:var(--acc2)}
.ss-rank{font-weight:700;color:var(--acc2);width:20px;text-align:center;flex:none}
.ss-name{font-size:14px}
.ss-meta{font-size:12px;color:var(--mut);margin-top:2px}
.summ{max-width:1180px;margin:0 auto 6px;padding:6px 20px 10px}
.summ>summary{font-size:17px;font-weight:700;color:var(--fg);list-style:none;padding:8px 0}
.summ>summary:before{content:"\\25b8 ";color:var(--acc)}
.summ[open]>summary:before{content:"\\25be "}
.summ-intro{color:#d3d9cf;font-size:14.5px;max-width:900px;margin:2px 0 12px}
.summ-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:12px}
.summ-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.summ-card h3{margin:0 0 4px;font-size:15px;color:var(--acc2)}
.summ-card .si{color:var(--mut);font-size:13px;margin:0 0 6px}
.summ-card ul{margin:0;padding-left:17px;font-size:13.5px}
.summ-card li{margin:4px 0}
"""

JS = """
const DATA = __DATA__;
const state={q:"",cat:"Alle"};
const grid=document.getElementById('grid');
const count=document.getElementById('count');
function esc(s){return (s||"").replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function hl(s){if(!state.q)return esc(s);const q=state.q.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&');
return esc(s).replace(new RegExp('('+q+')','ig'),'<mark>$1</mark>');}
function matches(h){
  if(state.cat!=="Alle"&&h.category!==state.cat)return false;
  if(!state.q)return true;
  const blob=[h.name,h.summary,h.deep_dive,h.category,(h.aka||[]).join(' '),(h.tags||[]).join(' '),
    (h.key_facts||[]).map(f=>f.label+' '+f.value).join(' '),
    (h.protocol||[]).join(' '),(h.mistakes||[]).join(' ')].join(' ').toLowerCase();
  return blob.includes(state.q.toLowerCase());
}
function facts(h){return (h.key_facts||[]).map(f=>
  `<li><span class="fl">${esc(f.label)}</span><span class="fv">${hl(f.value)}${f.source?` <span class="badge">${esc(f.source)}</span>`:''}</span></li>`).join('');}
function list(arr){return (arr||[]).map(x=>`<li>${hl(x)}</li>`).join('');}
function evidence(h){return (h.evidence||[]).map(e=>
  `<li><b>${esc(e.source)}${e.year?' ('+e.year+')':''}:</b> ${esc(e.finding)}</li>`).join('');}
function sources(h){return (h.sources||[]).map(s=>
  `<div class="src"><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a></div>`).join('');}
function card(h){
  const rob=h.robustness||{};
  return `<div class="card">
    <div class="meta">
      ${h.evidence_level?`<span class="badge ev ${h.evidence_level}">Evidenz ${h.evidence_level}</span>`:''}
      <span class="badge cat">${esc(h.category)}</span>
      ${h.impact?`<span class="badge imp">Wirkung ${h.impact}/5</span>`:''}
      ${h.effort?`<span class="badge">Aufwand ${h.effort}/5</span>`:''}
    </div>
    <h3>${hl(h.name)}</h3>
    ${(h.aka&&h.aka.length)?`<div class="badge">${esc(h.aka.join(' \\u00b7 '))}</div>`:''}
    <div class="sum">${hl(h.summary)}</div>
    ${h.key_facts?`<ul class="facts">${facts(h)}</ul>`:''}
    <details><summary>Details, Evidenz &amp; Umsetzung</summary>
      ${h.deep_dive?`<h4 class="sec">Vertiefung</h4><div class="dd">${hl(h.deep_dive)}</div>`:''}
      ${h.mechanism?`<h4 class="sec">Wirkmechanismus</h4><div class="dd">${esc(h.mechanism)}</div>`:''}
      ${h.protocol?`<h4 class="sec">Umsetzung</h4><ul class="lst">${list(h.protocol)}</ul>`:''}
      ${h.mistakes?`<h4 class="sec">Haeufige Fehler</h4><ul class="lst">${list(h.mistakes)}</ul>`:''}
      ${h.evidence?`<h4 class="sec">Belege / Studien</h4><ul class="lst">${evidence(h)}</ul>`:''}
      ${(rob.replication||rob.effect_size||rob.caveats)?`<h4 class="sec">Robustheit</h4><div class="dd">
        ${rob.effect_size?`<b>Effektgroesse:</b> ${esc(rob.effect_size)}<br>`:''}
        ${rob.replication?`<b>Replikation:</b> ${esc(rob.replication)}<br>`:''}
        ${rob.caveats?`<b>Vorbehalte:</b> ${esc(rob.caveats)}`:''}</div>`:''}
      ${h.risks?`<h4 class="sec">Risiken / Grenzen</h4><div class="risk">${esc(h.risks)}</div>`:''}
      ${(h.synergy&&h.synergy.length)?`<h4 class="sec">Kombiniert gut mit</h4><div class="dd">${esc(h.synergy.join(', '))}</div>`:''}
      ${h.sources?`<h4 class="sec">Quellen</h4>${sources(h)}`:''}
    </details>
  </div>`;
}
function render(){
  const vis=DATA.filter(matches);
  grid.innerHTML=vis.map(card).join('')||'<p style="color:var(--mut)">Nichts gefunden.</p>';
  count.textContent=vis.length+' / '+DATA.length+' Hebel';
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


EV_WEIGHT = {"A": 1.0, "B": 0.7, "C": 0.4}


def sweet_score(h):
    """Low-Hanging-Fruit-Score: viel Wirkung, wenig Aufwand, starke Evidenz."""
    ev = EV_WEIGHT.get(h.get("evidence_level"), 0.4)
    return (h.get("impact", 0) - 0.6 * h.get("effort", 3)) * ev


def sweet_html(hebel, n=8):
    """Statische Low-Hanging-Fruit-Sektion fuers Dashboard (Klick filtert die Liste)."""
    ranked = sorted(hebel, key=sweet_score, reverse=True)[:n]
    items = []
    for i, h in enumerate(ranked, 1):
        nm = html.escape(h.get("name", ""))
        meta = (f"Wirkung {h.get('impact','–')}/5 &middot; Aufwand {h.get('effort','–')}/5 "
                f"&middot; Evidenz {h.get('evidence_level','–')} &middot; {html.escape(h.get('category',''))}")
        items.append(
            f'<li class="ss-item" data-q="{nm}"><span class="ss-rank">{i}</span>'
            f'<span><span class="ss-name">{nm}</span><div class="ss-meta">{meta}</div></span></li>')
    return ('<section class="sweet"><h2>\U0001f352 Low-Hanging Fruits &ndash; bester Naturschutz '
            'pro Aufwand</h2>'
            '<p class="ss-note">Automatisch gerankt: viel ökologische Wirkung, wenig Aufwand, starke Evidenz. '
            'Klick auf einen Hebel filtert die Liste unten.</p>'
            f'<ol class="ss-list">{"".join(items)}</ol></section>')


SUMMARY_JSON = os.path.join(HERE, "zusammenfassung.json")


def summary_html():
    """Intensive Gesamt-Zusammenfassung (aus zusammenfassung.json, optional)."""
    try:
        with open(SUMMARY_JSON, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return ""
    sections = data.get("sections") or []
    if not sections:
        return ""
    cards = []
    for s in sections:
        pts = "".join(f"<li>{html.escape(p)}</li>" for p in (s.get("points") or []))
        intro = f'<p class="si">{html.escape(s.get("intro",""))}</p>' if s.get("intro") else ""
        cards.append(
            f'<div class="summ-card"><h3>{html.escape(s.get("heading",""))}</h3>{intro}<ul>{pts}</ul></div>')
    intro = f'<p class="summ-intro">{html.escape(data.get("intro",""))}</p>' if data.get("intro") else ""
    return ('<details class="summ" open><summary>\U0001f4d6 Intensiv-Zusammenfassung &ndash; '
            'das ganze Wissen auf einen Blick</summary>'
            f'{intro}<div class="summ-grid">{"".join(cards)}</div></details>')


def build(hebel):
    hebel = sorted(hebel, key=cat_key)
    cats = ["Alle"] + [c for c in CATEGORY_ORDER if any(h.get("category") == c for h in hebel)]
    chips = "".join(
        f'<span class="chip{" on" if c=="Alle" else ""}" data-cat="{html.escape(c)}">{html.escape(c)}</span>'
        for c in cats
    )
    data_json = json.dumps(hebel, ensure_ascii=False)
    js = JS.replace("__DATA__", data_json)
    page = f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Naturschutz effizient - Hebel-Katalog</title>
<style>{CSS}</style></head><body>
<header>
<h1>\U0001f331 Naturschutz effizient &ndash; die wirksamsten Hebel</h1>
<div class="sub">Wo bringt jeder investierte Euro und jede Stunde am meisten für die Natur? &ndash;
Maßnahmen von der Grünbrücke über Insektenschutz bis zur Flächenpolitik, nach Wirkung sortiert,
mit ehrlichem Evidenz-Level (A/B/C) und konkreter Umsetzung. Low-Hanging Fruits zuerst.</div>
</header>
<div class="controls">
<input id="q" placeholder="Suchen: Grünbrücke, Insekten, Hecke, Moor, Vogelschlag ...">
<div class="chips">{chips}<span class="count" id="count"></span></div>
</div>
{summary_html()}
{sweet_html(hebel)}
<main><div class="grid" id="grid"></div></main>
<footer>{len(hebel)} Hebel &middot; Evidenz-Level: A = Meta-Analysen/robuste Studienlage, B = einzelne Studien/konsistente Praxis, C = Mechanismus/Experten-Heuristik.
Wirkung &amp; Aufwand sind gerundete Einschätzungen, keine Einzelfallgarantie. Siehe LIMITATIONEN.md.</footer>
<script>{js}</script></body></html>"""
    return page


KATALOG = os.path.join(HERE, "KATALOG.md")


def md_katalog(hebel):
    """Erzeugt ein lesbares Markdown aller Hebel, gruppiert nach Kategorie."""
    hebel = sorted(hebel, key=cat_key)
    out = []
    out.append("# Katalog — Naturschutz effizient\n")
    out.append("_Automatisch aus `hebel/*.json` erzeugt (`python3 build.py`). "
               "Nicht von Hand editieren — die JSON-Dateien sind die Quelle._\n")
    out.append(f"**{len(hebel)} Hebel.** Evidenz-Level: **A** = Meta-Analysen/robust, "
               "**B** = einzelne Studien/konsistente Praxis, **C** = Mechanismus/Heuristik. "
               "Wirkung/Aufwand sind Einschätzungen — siehe `LIMITATIONEN.md`.\n")

    cats = [c for c in CATEGORY_ORDER if any(h.get("category") == c for h in hebel)]
    out.append("## Inhalt\n")
    for c in cats:
        items = [h for h in hebel if h.get("category") == c]
        out.append(f"- **{c}** ({len(items)})")
    out.append("")

    out.append("## 🍒 Low-Hanging Fruits — bester Naturschutz pro Aufwand\n")
    out.append("_Automatisch gerankt. Score = (Wirkung − 0,6·Aufwand) × Evidenzgewicht "
               "(A=1,0 · B=0,7 · C=0,4). Das sind die Hebel mit dem größten ökologischen Ertrag pro Aufwand._\n")
    ranked = sorted(hebel, key=sweet_score, reverse=True)[:12]
    out.append("| # | Hebel | Wirkung | Aufwand | Ev | Kategorie |")
    out.append("|---|---|:---:|:---:|:---:|---|")
    for i, h in enumerate(ranked, 1):
        out.append(f"| {i} | **{h['name']}** (`{h['id']}`) | {h.get('impact','–')}/5 "
                   f"| {h.get('effort','–')}/5 | {h.get('evidence_level','–')} | {h.get('category','')} |")
    out.append("")

    def bullets(title, arr):
        if not arr:
            return
        out.append(f"**{title}**\n")
        for x in arr:
            out.append(f"- {x}")
        out.append("")

    for c in cats:
        out.append(f"\n## {c}\n")
        for h in [x for x in hebel if x.get("category") == c]:
            out.append(f"### {h['name']}\n")
            meta = []
            if h.get("evidence_level"):
                meta.append(f"Evidenz **{h['evidence_level']}**")
            if h.get("impact"):
                meta.append(f"Wirkung {h['impact']}/5")
            if h.get("effort"):
                meta.append(f"Aufwand {h['effort']}/5")
            meta.append(f"`{h['id']}`")
            out.append(" · ".join(meta) + "\n")
            if h.get("aka"):
                out.append(f"_Auch: {', '.join(h['aka'])}_\n")
            out.append(h["summary"] + "\n")
            if h.get("key_facts"):
                out.append("| Kennzahl | Wert |")
                out.append("|---|---|")
                for f in h["key_facts"]:
                    val = f["value"].replace("|", "\\|")
                    src = f" _({f['source']})_" if f.get("source") else ""
                    out.append(f"| {f['label']} | {val}{src} |")
                out.append("")
            if h.get("deep_dive"):
                out.append(h["deep_dive"] + "\n")
            if h.get("mechanism"):
                out.append(f"**Wirkmechanismus:** {h['mechanism']}\n")
            bullets("Umsetzung", h.get("protocol"))
            bullets("Häufige Fehler", h.get("mistakes"))
            if h.get("evidence"):
                out.append("**Belege / Studien**\n")
                for e in h["evidence"]:
                    yr = f" ({e['year']})" if e.get("year") else ""
                    out.append(f"- _{e['source']}{yr}:_ {e['finding']}")
                out.append("")
            rob = h.get("robustness") or {}
            if any(rob.get(k) for k in ("replication", "effect_size", "caveats")):
                out.append("**Robustheit** — "
                           + " ".join(filter(None, [
                               f"Effektgröße: {rob['effect_size']}." if rob.get("effect_size") else "",
                               f"Replikation: {rob['replication']}." if rob.get("replication") else "",
                               f"Vorbehalte: {rob['caveats']}" if rob.get("caveats") else "",
                           ])) + "\n")
            if h.get("risks"):
                out.append(f"> ⚠️ **Risiken / Grenzen:** {h['risks']}\n")
            if h.get("synergy"):
                out.append(f"**Kombiniert mit:** {', '.join(h['synergy'])}\n")
            if h.get("sources"):
                out.append("**Quellen:** " + " · ".join(
                    f"[{s.get('title','Link')}]({s['url']})" for s in h["sources"] if s.get("url")) + "\n")
            out.append("---\n")
    return "\n".join(out)


def main():
    hebel, errors = load_hebel()
    if errors:
        print("VALIDIERUNGSFEHLER:")
        for e in errors:
            print("  -", e)
    print(f"{len(hebel)} Hebel geladen.")
    if "--check" in sys.argv:
        sys.exit(1 if errors else 0)
    if errors:
        print("Baue trotzdem (Fehler oben pruefen).")
    page = build(hebel)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"geschrieben: {OUT} ({len(page)//1024} KB)")
    katalog = md_katalog(hebel)
    with open(KATALOG, "w", encoding="utf-8") as f:
        f.write(katalog)
    print(f"geschrieben: {KATALOG} ({len(katalog)//1024} KB)")


if __name__ == "__main__":
    main()
