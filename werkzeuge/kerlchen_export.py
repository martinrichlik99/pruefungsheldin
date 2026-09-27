"""Schreibt den APHI1-Katalog im Format des Schlauen Kerlchens nach Schlaues Kerlchen/daten/aphi1.json."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
fragen = json.loads((root / "pruefungen/aphi1/fragen.json").read_text(encoding="utf-8"))
ziel = root.parent / "Schlaues Kerlchen/daten/aphi1.json"

aus = []
for f in fragen:
    e = {"id": f["id"], "kategorie": "APHI Prüfung", "frage": f["frage"]}
    if f["typ"] == "mc":
        e["optionen"] = f["optionen"]
    e["antwortKurz"] = f["antwortKurz"]
    e["erklaerung"] = f["erklaerung"] + " (Skript Seite " + str(f["seite"]) + ")"
    aus.append(e)

ziel.write_text("[\n" + ",\n".join(json.dumps(e, ensure_ascii=False) for e in aus) + "\n]\n", encoding="utf-8")
print(f"{len(aus)} Fragen → {ziel}")
