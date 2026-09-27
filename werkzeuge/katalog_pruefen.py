"""Fügt werkzeuge/teile/*.json zu pruefungen/aphi1/fragen.json zusammen und prüft den Katalog."""
import json, sys, collections
from pathlib import Path

root = Path(__file__).resolve().parent.parent
ziel = root / "pruefungen/aphi1"
meta = json.loads((ziel / "meta.json").read_text(encoding="utf-8"))
kapitel = [k["nr"] for k in meta["kapitel"]]

fragen = []
for teil in sorted((root / "werkzeuge/teile").glob("*.json")):
    fragen += json.loads(teil.read_text(encoding="utf-8"))

naechste = max((int(f["id"][6:]) for f in fragen if "id" in f), default=0)
for f in fragen:
    if "id" not in f:
        naechste += 1
        f["id"] = f"aphi1-{naechste:03d}"
        print("neue ID:", f["id"], "– bitte in die Teil-Datei übernehmen")

fehler = []
ids = collections.Counter(f["id"] for f in fragen)
fehler += [f"doppelte ID: {i}" for i, n in ids.items() if n > 1]
for f in fragen:
    ort = f'{f["id"]} ({f.get("frage","")[:40]})'
    for feld in ("kapitel", "typ", "frage", "antwortKurz", "erklaerung", "seite", "prio"):
        if not f.get(feld):
            fehler.append(f"{ort}: Feld '{feld}' fehlt")
    if f.get("kapitel") not in kapitel:
        fehler.append(f"{ort}: unbekanntes Kapitel {f.get('kapitel')}")
    if f.get("prio") not in ("hoch", "normal", "niedrig"):
        fehler.append(f"{ort}: prio ungültig")
    if not 3 <= f.get("seite", 0) <= 50:
        fehler.append(f"{ort}: Seite außerhalb 3–50")
    typ = f.get("typ")
    if typ == "wf" and not isinstance(f.get("richtig"), bool):
        fehler.append(f"{ort}: wf braucht richtig=true/false")
    if typ == "mc":
        opt, r = f.get("optionen", []), f.get("richtig", [])
        if len(opt) < 3 or not r or any(not isinstance(x, int) or x >= len(opt) for x in r):
            fehler.append(f"{ort}: mc-Optionen/Indizes ungültig")
    if typ == "kurz" and ("optionen" in f or "richtig" in f):
        fehler.append(f"{ort}: kurz darf keine optionen/richtig haben")
    if typ not in ("wf", "mc", "kurz"):
        fehler.append(f"{ort}: typ ungültig")

doppelt = [t for t, n in collections.Counter(f["frage"] for f in fragen).items() if n > 1]
fehler += [f"doppelte Frage: {t}" for t in doppelt]
fehlend = [k for k in kapitel if not any(f.get("kapitel") == k for f in fragen)]
fehler += [f"Kapitel ohne Frage: {k}" for k in fehlend]

if fehler:
    print("\n".join(fehler)); print(f"FEHLER: {len(fehler)}"); sys.exit(1)

reihenfolge = ["id", "kapitel", "typ", "frage", "optionen", "richtig", "antwortKurz", "erklaerung", "seite", "vorlesung", "prio"]
fragen = [{k: f[k] for k in reihenfolge if k in f} for f in fragen]
(ziel / "fragen.json").write_text(
    "[\n" + ",\n".join(json.dumps(f, ensure_ascii=False) for f in fragen) + "\n]\n", encoding="utf-8")

c = collections.Counter
print(f"OK: {len(fragen)} Fragen, {len(kapitel)} Kapitel abgedeckt")
print("Typ:", dict(c(f["typ"] for f in fragen)))
print("Prio:", dict(c(f["prio"] for f in fragen)))
print("mit Vorlesung:", sum("vorlesung" in f for f in fragen))
print("wf richtig/falsch:", dict(c(f["richtig"] for f in fragen if f["typ"] == "wf")))
