"""Pathologie-Altfragen 1:1 aus quellen/Pathologie_Altfragen.json (Text aus Testfragen_AllgemeinePatho.pdf) -> pruefungen/patho-alt/.

Im Original-PDF ist keine Lösung markiert. LOESUNG = Index der richtigen Antwort, aus dem Pathologie-Skript ermittelt (Seite in SEITE).
"""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
ziel = root / "pruefungen/patho-alt"
roh = json.loads((root / "quellen/Pathologie_Altfragen.json").read_text(encoding="utf-8"))

LOESUNG = [2,1,1,0,0,0,1,2,0,0, 1,1,0,0,0,0,0,1,1,1, 0,0,0,0,0,0,1,0,0,2, 1,0,0,0,1,2,0,3,1,1,
           1,1,1,0,1,1,1,1,2,3, 1,2,0,1,1,1,0,1,1,1, 1,2,0,0,0]
SEITE = [136,208,218,223,226,249,256,54,269,264, 278,281,281,287,291,300,302,58,317,327, 338,345,377,378,140,398,65,385,391,413,
         71,308,145,147,259,345,250,36,104,207, 205,193,169,269,34,307,176,208,366,38, 157,160,172,181,190,207,207,233,27,104,
         124,226,264,242,260]
KAPITEL = [("1", "Grundlagen", [59]), ("2", "Tod & Obduktion", [8, 18, 38, 45, 50]), ("3", "Krankheitslehre", [27, 31, 43]),
           ("4", "Zellpathologie", [1, 25, 33, 34, 39, 60, 61]), ("5", "Entzündung & Wundheilung", [42, 47, 51, 52, 53, 54, 55]),
           ("6", "Tumorpathologie", [2, 3, 4, 5, 6, 7, 9, 10, 35, 37, 40, 41, 44, 48, 56, 57, 58, 62, 63, 64, 65]),
           ("7", "Kreislaufstörungen", [11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 32, 36, 46, 49]),
           ("8", "Stoffwechsel & Gefäße", [23, 24, 26, 28, 29, 30])]
kap_von = {nr: k for k, _, nrn in KAPITEL for nr in nrn}

assert len(roh) == len(LOESUNG) == len(SEITE) == 65 and sorted(kap_von) == list(range(1, 66))
fragen = []
for q, r, s in zip(roh, LOESUNG, SEITE):
    opt = [re.sub(r"^[A-D]\) ", "", o) for o in q["optionen"]]
    fragen.append({"id": f"patalt-{q['nr']:03d}", "kapitel": kap_von[q["nr"]], "typ": "mc", "frage": q["frage"], "optionen": opt, "richtig": [r],
                   "antwortKurz": opt[r], "erklaerung": f"Altfrage {q['nr']} von 65. Lösung im Original nicht markiert – aus dem Skript ermittelt.",
                   "seite": s, "prio": "hoch"})

ziel.mkdir(exist_ok=True)
(ziel / "fragen.json").write_text("[\n" + ",\n".join(json.dumps(f, ensure_ascii=False) for f in fragen) + "\n]\n", encoding="utf-8")
meta = {"id": "patho-alt", "titel": "Pathologie – Altfragen", "kurz": "PATHO-ALT", "datum": "2026-11-30", "aktiv": True,
        "form": "MC-Test, Fragen aus der Prüfung des Vorjahrgangs (1 Antwort richtig)",
        "kapitel": [{"nr": k, "titel": t} for k, t, _ in KAPITEL],
        "gruppen": [{"nr": k, "titel": t, "thema": "", "praefix": [k]} for k, t, _ in KAPITEL]}
(ziel / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(len(fragen), "Altfragen geschrieben")
for f in fragen:
    print(f["id"][-2:], f["frage"][:60], "→", f["antwortKurz"])
