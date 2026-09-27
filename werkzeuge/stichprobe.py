"""Erzeugt eine druckbare Stichprobe (HTML) aus fragen.json – gleichmäßig über alle Kapitel verteilt."""
import json, random, html
from pathlib import Path

root = Path(__file__).resolve().parent.parent
fragen = json.loads((root / "pruefungen/aphi1/fragen.json").read_text(encoding="utf-8"))
meta = json.loads((root / "pruefungen/aphi1/meta.json").read_text(encoding="utf-8"))
titel = {k["nr"]: k["titel"] for k in meta["kapitel"]}
ANZAHL = 40

random.seed(12)
schritt = len(fragen) / ANZAHL
auswahl = [random.choice(fragen[int(i * schritt):int((i + 1) * schritt)]) for i in range(ANZAHL)]
typname = {"wf": "Richtig/Falsch", "mc": "Ankreuzen", "kurz": "Kurze Antwort"}
e = html.escape

karten = []
for n, f in enumerate(auswahl, 1):
    loesung = ""
    if f["typ"] == "mc":
        loesung = "<ul>" + "".join(
            f'<li class="{"ok" if i in f["richtig"] else ""}">{"☑" if i in f["richtig"] else "☐"} {e(o)}</li>'
            for i, o in enumerate(f["optionen"])) + "</ul>"
    quelle = f'Skript S. {f["seite"]}' + (f' · Erklärung aus Vorlesung {f["vorlesung"]}' if "vorlesung" in f else "")
    karten.append(f"""<section>
<div class="kopf">{n}. · Kap. {e(f["kapitel"])} {e(titel[f["kapitel"]])} · {typname[f["typ"]]} · {e(f["id"])}</div>
<p class="frage">{e(f["frage"])}</p>{loesung}
<p><b>Lösung:</b> {e(f["antwortKurz"])}</p>
<p class="erk">{e(f["erklaerung"])}</p>
<div class="fuss">{quelle}<span>☐ passt &nbsp; ☐ falsch &nbsp; ☐ unwichtig &nbsp; Notiz: ______________</span></div>
</section>""")

seite = f"""<!doctype html><html lang="de"><meta charset="utf-8"><title>Prüfungsheldin – Stichprobe APHI1</title>
<style>
body{{font:10.5pt/1.4 -apple-system,Helvetica,Arial,sans-serif;color:#1d1d1f;margin:0}}
h1{{font-size:17pt;margin:0 0 4px}} .intro{{color:#555;margin:0 0 14px}}
section{{border:1px solid #d8d8dc;border-radius:8px;padding:9px 12px;margin:0 0 9px;break-inside:avoid}}
.kopf{{font-size:8.5pt;color:#6e6e73;text-transform:uppercase;letter-spacing:.02em}}
.frage{{font-weight:600;margin:4px 0}} p{{margin:3px 0}} ul{{margin:2px 0 4px;padding-left:4px;list-style:none}}
li.ok{{font-weight:600;color:#1a7f37}} .erk{{color:#444}}
.fuss{{display:flex;justify-content:space-between;font-size:8.5pt;color:#6e6e73;margin-top:5px}}
@page{{margin:14mm}}
</style>
<h1>Prüfungsheldin – Stichprobe APHI1</h1>
<p class="intro">{ANZAHL} von {len(fragen)} Fragen, über alle Skript-Kapitel verteilt. Bitte je Frage ankreuzen:
stimmt die Lösung, ist etwas falsch, oder ist die Frage für die Prüfung unwichtig? Seitenangaben = Seitenzahl unten im Skript.</p>
{"".join(karten)}
</html>"""
(root / "stichprobe/Stichprobe APHI1.html").write_text(seite, encoding="utf-8")
print("Stichprobe:", len(auswahl), "Fragen,", len({f['kapitel'] for f in auswahl}), "Kapitel")
