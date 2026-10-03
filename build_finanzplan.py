#!/usr/bin/env python3
"""Rechnet fuer jedes Gruenderprojekt einen 24-Monats-Finanzplan (Cashflow) und
baut daraus ein self-contained finanzplan.html + FINANZPLAN.md.

Modell (bewusst einfach & transparent, ILLUSTRATIV):
- Betrachtet nur BETRIEBS-Cashflow (Material, Cloud, Hardware, Marketing, Versicherung).
  Gruenderlohn ist NICHT enthalten (Annahme: Nebenerwerb/Stipendium traegt den
  Lebensunterhalt) - das steht transparent dabei.
- Foerderung fliesst waehrend der Entwicklungsphase (dev_monate), danach traegt
  echter Umsatz (Verkauf + wiederkehrende SaaS/Service).
- Break-even = erster Monat mit kumuliertem Saldo >= 0.

Zahlen sind EINSCHAETZUNGEN zum Zeigen der Hebel, keine Prognose. Alle Annahmen
stehen offen im ASSUMPTIONS-Dict und sind editierbar.

    python3 build_finanzplan.py
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "finanzplan.html")
MD = os.path.join(HERE, "FINANZPLAN.md")
MONATE = 24

# Pro Projekt: Annahmen. Betraege in EUR.
#  foerderung        Foerdersumme gesamt (fliesst gleichmaessig ueber dev_monate)
#  dev_monate        Entwicklungsphase (Monate), erst danach Verkauf
#  fix_monat         fixe Betriebskosten/Monat (Cloud, Versicherung, Tools)
#  einheit           was verkauft wird (Label)
#  db_einheit        Deckungsbeitrag je Einheit beim Verkauf (Preis - variable Kosten)
#  absatz_start      verkaufte Einheiten im ersten Verkaufsmonat
#  absatz_plus       zusaetzliche Einheiten pro Folgemonat (additiv)
#  absatz_cap        Obergrenze Einheiten/Monat
#  saas_monat        wiederkehrender Deckungsbeitrag je aktiver Einheit/Monat (0 = keiner)
#  dev_extra_monat   zusaetzliche Sachkosten/Monat waehrend der Entwicklung (Hardware/Test)
ASSUMPTIONS = {
    "prioritaetsplaner-beratung": dict(name="PrioritaetsPlaner", foerderung=47000, dev_monate=6,
        fix_monat=150, einheit="Beratungstage", db_einheit=850, absatz_start=2, absatz_plus=0.5,
        absatz_cap=9, saas_monat=0, dev_extra_monat=100),
    "kamerafallen-auswertedienst": dict(name="WildAuge", foerderung=47500, dev_monate=6,
        fix_monat=250, einheit="Neukunden", db_einheit=500, absatz_start=1, absatz_plus=0.5,
        absatz_cap=10, saas_monat=300, dev_extra_monat=150),
    "kitzretter-service": dict(name="KitzRetter", foerderung=20000, dev_monate=5,
        fix_monat=200, einheit="Flaechen-Auftraege", db_einheit=280, absatz_start=6, absatz_plus=2,
        absatz_cap=40, saas_monat=0, dev_extra_monat=500),
    "lauschposten-bioakustik": dict(name="Lauschposten", foerderung=47500, dev_monate=6,
        fix_monat=300, einheit="Boxen", db_einheit=300, absatz_start=2, absatz_plus=1,
        absatz_cap=15, saas_monat=38, dev_extra_monat=400),
    "artenschutz-module-bau": dict(name="ArtenschutzModul", foerderung=60000, dev_monate=9,
        fix_monat=350, einheit="Module", db_einheit=30, absatz_start=20, absatz_plus=10,
        absatz_cap=250, saas_monat=0, dev_extra_monat=400),
    "flaechenmonitor-fernerkundung": dict(name="FlaechenMonitor", foerderung=90000, dev_monate=12,
        fix_monat=600, einheit="Behoerden-Abos", db_einheit=0, absatz_start=1, absatz_plus=0.5,
        absatz_cap=8, saas_monat=800, dev_extra_monat=300),
    "naturbuero-ki": dict(name="NaturBuero-KI", foerderung=47500, dev_monate=6,
        fix_monat=400, einheit="Organisationen", db_einheit=0, absatz_start=2, absatz_plus=1,
        absatz_cap=25, saas_monat=350, dev_extra_monat=150),
    "insektenscanner-monitoring": dict(name="InsektenScanner", foerderung=135000, dev_monate=12,
        fix_monat=500, einheit="Stationen", db_einheit=600, absatz_start=4, absatz_plus=2,
        absatz_cap=40, saas_monat=75, dev_extra_monat=600),
    "naturdruck-baukasten-fablab": dict(name="NaturDruck", foerderung=46500, dev_monate=6,
        fix_monat=250, einheit="Sets/Workshops", db_einheit=45, absatz_start=20, absatz_plus=8,
        absatz_cap=200, saas_monat=0, dev_extra_monat=300),
    "roadkill-radar": dict(name="Roadkill-Radar", foerderung=95000, dev_monate=12,
        fix_monat=450, einheit="Verwaltungs-Lizenzen", db_einheit=0, absatz_start=1, absatz_plus=0.4,
        absatz_cap=10, saas_monat=900, dev_extra_monat=200),
    "buergernatur-plattform": dict(name="BuergerNatur", foerderung=90000, dev_monate=12,
        fix_monat=400, einheit="Mandanten", db_einheit=3000, absatz_start=1, absatz_plus=0.5,
        absatz_cap=15, saas_monat=500, dev_extra_monat=200),
}


def plan(a):
    rows = []
    kum = 0.0
    aktive_saas = 0.0
    breakeven = None
    foerder_monat = a["foerderung"] / a["dev_monate"] if a["dev_monate"] else 0
    for m in range(MONATE):
        foerd = foerder_monat if m < a["dev_monate"] else 0.0
        if m >= a["dev_monate"]:
            k = m - a["dev_monate"]
            einh = min(a["absatz_cap"], a["absatz_start"] + a["absatz_plus"] * k)
        else:
            einh = 0.0
        verkauf = einh * a["db_einheit"]
        aktive_saas += einh  # verkaufte Einheiten bleiben als wiederkehrend aktiv
        saas = aktive_saas * a["saas_monat"]
        einnahmen = foerd + verkauf + saas
        ausgaben = a["fix_monat"] + (a["dev_extra_monat"] if m < a["dev_monate"] else 0)
        saldo = einnahmen - ausgaben
        kum += saldo
        if breakeven is None and kum >= 0 and m >= a["dev_monate"]:
            breakeven = m + 1
        rows.append(dict(m=m + 1, foerd=foerd, umsatz=verkauf + saas, ausg=ausgaben,
                         saldo=saldo, kum=kum, einh=einh))
    jahr2_umsatz = sum(r["umsatz"] for r in rows[12:24])
    run_rate = rows[-1]["umsatz"] * 12  # annualisierter Lauf am Monat 24
    return rows, dict(breakeven=breakeven, kum24=kum, jahr2_umsatz=jahr2_umsatz, run_rate=run_rate)


def eur(x):
    return f"{round(x):,}".replace(",", ".") + " EUR"


def quarter_table(rows):
    qs = []
    for q in range(8):
        seg = rows[q * 3:q * 3 + 3]
        qs.append(dict(q=q + 1,
                       foerd=sum(r["foerd"] for r in seg),
                       umsatz=sum(r["umsatz"] for r in seg),
                       ausg=sum(r["ausg"] for r in seg),
                       saldo=sum(r["saldo"] for r in seg),
                       kum=seg[-1]["kum"]))
    return qs


CSS = """
body{margin:0;background:#0d130e;color:#e9ece6;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:26px;margin:0 0 4px}.lead{color:#93a493;max-width:820px}
.proj{background:#161d17;border:1px solid #263021;border-radius:14px;padding:16px 18px;margin:16px 0}
.proj h2{margin:0 0 2px;font-size:19px}.sub{color:#93a493;font-size:13px;margin-bottom:10px}
.kpi{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 12px}
.kpi div{background:#1e2a1f;border-radius:8px;padding:8px 12px;font-size:13px}
.kpi b{display:block;font-size:16px;color:#7bc47f}
.kpi .eur{color:#e0a24c}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:5px 8px;text-align:right;border-bottom:1px solid #263021}
th:first-child,td:first-child{text-align:left}
th{color:#93a493;font-weight:600}
td.pos{color:#7bc47f}td.neg{color:#e0866a}
footer{color:#93a493;font-size:13px;margin-top:30px}
"""


def build_html(results):
    cards = []
    for pid, (rows, kpi) in results:
        a = ASSUMPTIONS[pid]
        be = f"Monat {kpi['breakeven']}" if kpi["breakeven"] else "> 24 Monate"
        qs = quarter_table(rows)
        qrows = "".join(
            f"<tr><td>Q{q['q']}</td><td class='eur'>{eur(q['foerd'])}</td>"
            f"<td>{eur(q['umsatz'])}</td><td>{eur(q['ausg'])}</td>"
            f"<td class='{'pos' if q['saldo']>=0 else 'neg'}'>{eur(q['saldo'])}</td>"
            f"<td class='{'pos' if q['kum']>=0 else 'neg'}'>{eur(q['kum'])}</td></tr>"
            for q in qs)
        cards.append(f"""<div class="proj"><h2>{html.escape(a['name'])}</h2>
<div class="sub">Foerderung {eur(a['foerderung'])} ueber {a['dev_monate']} Mon. Entwicklung &middot; danach {html.escape(a['einheit'])}
{' + wiederkehrende Erloese' if a['saas_monat'] else ''}</div>
<div class="kpi">
<div>Break-even<b>{be}</b></div>
<div>Kum. Saldo M24<b class="{'pos' if kpi['kum24']>=0 else 'neg'}">{eur(kpi['kum24'])}</b></div>
<div>Umsatz Jahr 2<b>{eur(kpi['jahr2_umsatz'])}</b></div>
<div>Run-Rate M24 (annualisiert)<b>{eur(kpi['run_rate'])}</b></div>
</div>
<table><tr><th>Quartal</th><th>Foerderung</th><th>Umsatz</th><th>Ausgaben</th><th>Saldo</th><th>kumuliert</th></tr>
{qrows}</table></div>""")
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Finanzplaene - Naturschutz-Gruenderprojekte</title><style>{CSS}</style></head><body><div class="wrap">
<h1>\U0001f4b9 24-Monats-Finanzplaene</h1>
<p class="lead">Betriebs-Cashflow je Projekt: Foerderung traegt die Entwicklung, danach echter Umsatz.
Gruenderlohn NICHT enthalten (Annahme Nebenerwerb/Stipendium). Alle Zahlen sind editierbare
Annahmen zum Zeigen der Hebel - keine Prognose. Quelle: build_finanzplan.py.</p>
{''.join(cards)}
<footer>Break-even = erster Monat mit kumuliertem Saldo &ge; 0 nach der Entwicklungsphase.
Annahmen im Skript (ASSUMPTIONS) anpassbar. Keine Steuer-/Finanzberatung.</footer>
</div></body></html>"""


def build_md(results):
    out = ["# Finanzplaene — Naturschutz-Gruenderprojekte\n",
           "_Auto-generiert (`python3 build_finanzplan.py`). 24-Monats-Betriebs-Cashflow je Projekt. "
           "Gruenderlohn nicht enthalten (Nebenerwerb/Stipendium-Annahme). Zahlen sind editierbare "
           "Annahmen, keine Prognose._\n"]
    out.append("## Uebersicht\n")
    out.append("| Projekt | Foerderung | Break-even | Umsatz Jahr 2 | Run-Rate M24 | kum. Saldo M24 |")
    out.append("|---|--:|:--:|--:|--:|--:|")
    for pid, (rows, kpi) in results:
        a = ASSUMPTIONS[pid]
        be = f"M{kpi['breakeven']}" if kpi["breakeven"] else ">24M"
        out.append(f"| **{a['name']}** | {eur(a['foerderung'])} | {be} | {eur(kpi['jahr2_umsatz'])} "
                   f"| {eur(kpi['run_rate'])} | {eur(kpi['kum24'])} |")
    out.append("")
    for pid, (rows, kpi) in results:
        a = ASSUMPTIONS[pid]
        out.append(f"\n## {a['name']}\n")
        out.append(f"Foerderung {eur(a['foerderung'])} ueber {a['dev_monate']} Monate Entwicklung; "
                   f"danach Verkauf von {a['einheit']}"
                   + (", plus wiederkehrende Erloese." if a['saas_monat'] else ".") + "\n")
        out.append("| Quartal | Foerderung | Umsatz | Ausgaben | Saldo | kumuliert |")
        out.append("|---|--:|--:|--:|--:|--:|")
        for q in quarter_table(rows):
            out.append(f"| Q{q['q']} | {eur(q['foerd'])} | {eur(q['umsatz'])} | {eur(q['ausg'])} "
                       f"| {eur(q['saldo'])} | {eur(q['kum'])} |")
        out.append("")
    return "\n".join(out)


def main():
    # gleiche Reihenfolge wie Projekt-Ranking (grob nach Ertrag/Aufwand): hier nach kum24 absteigend
    results = [(pid, plan(a)) for pid, a in ASSUMPTIONS.items()]
    results.sort(key=lambda r: r[1][1]["kum24"], reverse=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(build_html(results))
    with open(MD, "w", encoding="utf-8") as f:
        f.write(build_md(results))
    print(f"geschrieben: {OUT} und {MD} ({len(results)} Projekte)")
    for pid, (rows, kpi) in results:
        be = kpi["breakeven"] or ">24"
        print(f"  {ASSUMPTIONS[pid]['name']:18} Break-even M{be:<4} kum24 {eur(kpi['kum24'])}")


if __name__ == "__main__":
    main()
