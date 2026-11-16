"""Erzeugt pruefungen/kim/fragen.json + meta.json aus quellen/Klinische Innere Medizin.md (Fragen von Hand formuliert).

Kurzschreibweise:
  S(frage, optionen, richtig_indizes, erklaerung, seite)  -> typ "mc" (1 oder mehrere richtig; App mischt die Reihenfolge)
  L(text_mit___, [luecken], erklaerung, seite)              -> typ "lueckentext"
  F(frage, stichworte, erklaerung, seite)                   -> typ "kurz" (Freitext, Antwort in Stichworten)
Ein * vor der Frage = prio "hoch" (im Skript als prüfungsrelevant markiert).
"""
import json, sys, collections
from pathlib import Path

root = Path(__file__).resolve().parent.parent
ziel = root / "pruefungen/kim"

KAPITEL = [
    ("1", "Grundlagen", "Anamnese, Untersuchung, Bildgebung, Therapie, Prävention"),
    ("2", "Kardiologie", "Rhythmus, Hypertonie, KHK, Herzinfarkt, Reanimation"),
    ("3", "Angiologie", "Arteriosklerose, Rauchen, pAVK, Aneurysma, Venen, Lungenembolie"),
    ("4", "Pulmologie", "Spirometrie, Asthma, COPD, Pneumonie, Lungenkrebs"),
    ("5", "Gastroenterologie", "Gastritis, Ulcus, Unverträglichkeiten, CED, Darmkrebs, Leber"),
    ("6", "Nephrologie", "Nierenfunktion, Nierenversagen, Niereninsuffizienz"),
    ("7", "Endokrinologie & Stoffwechsel", "Diabetes, Adipositas, Ernährung, Schilddrüse, Nebenniere"),
    ("8", "Hämatologie", "Blut, Anämie, Leukämie, Lymphome, Gerinnung"),
    ("9", "Infektiologie & Allergien", "Impfung, Fieber, Infektionswege, Harnwegsinfekt, Kinderkrankheiten, Allergie"),
]

fragen, kap = [], None


def K(nr):
    global kap
    kap = nr


def _neu(frage, **rest):
    prio = "hoch" if frage.startswith("*") else "normal"
    fragen.append({"kapitel": kap, "frage": frage.lstrip("*"), "prio": prio, **rest})


def S(frage, optionen, richtig, erkl, seite):
    _neu(frage, typ="mc", optionen=optionen, richtig=richtig,
         antwortKurz=", ".join(optionen[i] for i in richtig), erklaerung=erkl, seite=seite)


def L(text, luecken, erkl, seite):
    teile = text.lstrip("*").split("___")
    assert len(teile) == len(luecken) + 1, text
    voll = teile[0] + "".join(l + t for l, t in zip(luecken, teile[1:]))
    _neu(text, typ="lueckentext", luecken=luecken, antwortKurz=voll, erklaerung=erkl, seite=seite)


def F(frage, antwort, erkl, seite):
    _neu(frage, typ="kurz", antwortKurz=antwort, erklaerung=erkl, seite=seite)


# ---------------------------------------------------------------- 1 Grundlagen
K("1")
S("Welches Fachgebiet beschäftigt sich mit den Blutgefäßen?", ["Angiologie", "Hämatologie", "Nephrologie", "Pulmologie"], [0],
  "Angiologie = Lehre von den Blutgefäßen; Hämatologie = Blut.", 2)
S("Welches Fachgebiet ist für Hormone zuständig?", ["Endokrinologie", "Gastroenterologie", "Rheumatologie", "Infektiologie"], [0],
  "Endokrinologie → Hormone.", 2)
S("Wofür steht die Nephrologie?", ["Niere", "Nerven", "Lunge", "Leber"], [0], "Nephrologie → Niere.", 2)
L("Die Gastroenterologie ist die Lehre vom ___, die Pulmologie die Lehre von der ___.", ["Magen-Darm-Trakt", "Lunge"],
  "-logie = Lehre von etwas.", 2)
F("Nenne die sechs Bereiche der Anamnese laut Skript.",
  "Aktuelle Beschwerden, vegetative Anamnese, Vorerkrankungen/Operationen, Familienanamnese, Sozialanamnese, Medikamente/Ergänzungsmittel",
  "Die Anamnese grenzt die Untersuchung ein und gibt Orientierung.", 21)
S("Was erfragt die vegetative Anamnese?", ["Was automatisch im Körper abläuft (z. B. Schlaf, Atmung, Stuhlgang)", "Erkrankungen in der Familie",
  "Wohnsituation und soziales Umfeld", "Frühere Operationen"], [0], "Vegetativ = automatisch ablaufende Körperfunktionen.", 2)
S("Was wird bei der Sozialanamnese erfragt?", ["Wohnsituation und soziales Umfeld", "Familiäre Erkrankungen", "Medikamente", "Aktuelle Beschwerden"], [0],
  "Sozialanamnese → Wohnsituation, soziales Umfeld.", 2)
F("Nenne die fünf Elemente der körperlichen Untersuchung (Status präsens).",
  "Inspektion, Palpation, Auskultation, Perkussion, klinische Funktionsprüfungen", "Reihenfolge in der Mitschrift: Inspektion – Auskultation – Palpation.", 22)
L("Die ___ ist das Abhören von Organen, die ___ das Abtasten, die ___ das Beklopfen.", ["Auskultation", "Palpation", "Perkussion"],
  "Inspektion = alles, was man sieht.", 3)
S("Was ist bei der Auskultation mit dem Stethoskop wichtig?", ["Stethoskop immer direkt auf die Haut legen", "Über der Kleidung abhören",
  "Nur am Rücken abhören", "Patient muss liegen"], [0], "Sonst entstehen falsche Geräusche.", 3)
S("Womit beginnt die körperliche Untersuchung laut Mitschrift?", ["Inspektion", "Palpation", "Perkussion", "Auskultation"], [0],
  "Schauen schon vor Anamnese/Gespräch: Gang, Haltung.", 3)
S("Welches Blut ist heller?", ["Sauerstoffreiches, arterielles Blut", "Sauerstoffarmes, venöses Blut", "Beide gleich", "Kapillarblut immer"], [0],
  "Arterien = Schlagadern führen sauerstoffreiches, helleres Blut.", 4)
F("Nenne Materialien, die im Labor untersucht werden können.",
  "Blut (Vollblut, Serum), Urin, Stuhl, Sputum, Liquor, Material von Punktionen/Abstrichen", "Sputum = Auswurf, Liquor = Hirn-Rückenmarks-Flüssigkeit.", 23)
L("Liquor ist die ___-Flüssigkeit, Sputum ist der ___ aus Lunge und Atemwegen.", ["Hirn-Rückenmarks", "Auswurf (Spucke)"],
  "Farbe des Sputums gibt Hinweise auf Krankheitserreger.", 4)
S("Welches bildgebende Verfahren arbeitet OHNE schädliche Strahlung?", ["MRT", "Sonographie", "CT", "Konventionelles Röntgen"], [0, 1],
  "MRT nutzt Magnetfeld und Radiowellen, Ultraschall hochfrequente Schallwellen. CT und Röntgen nutzen ionisierende Strahlung.", 5)
S("Warum erscheinen Knochen im Röntgenbild weiß?", ["Knochen lassen die Strahlung nicht durch", "Knochen enthalten Luft",
  "Knochen reflektieren Schallwellen", "Knochen nehmen Kontrastmittel auf"], [0], "Luft lässt Strahlung durch → schwarz.", 5)
S("Bei welchen Situationen wird typischerweise ein CT gemacht?", ["Polytrauma / schwere Unfälle", "Verdacht auf Schlaganfall",
  "Schwangerschaftskontrolle", "Routinekontrolle der Schilddrüse"], [0, 1], "CT ist schnell (wenige Minuten): Unfälle, innere Blutungen, Schlaganfall, Tumoren.", 5)
S("Wie funktioniert eine PET?", ["Schwach radioaktiver Tracer (meist Traubenzucker) wird von Zellen mit hohem Energiebedarf aufgenommen",
  "Magnetfeld richtet Wasserstoffatome aus", "Schallwellen werden reflektiert", "Röntgenstrahlen durchdringen den Körper"], [0],
  "Krebszellen verbrauchen viel Zucker → PET hilft Tumoren und Metastasen aufzuspüren.", 5)
F("Wofür wird die Szintigraphie z. B. eingesetzt?", "Schilddrüse (Knoten mit Über-/Unterfunktion), Knochenmetastasen, Entzündungen, Knochenschmerzen",
  "Tracer reichert sich in Gewebe mit hoher Stoffwechselaktivität an.", 6)
L("Die Lungenfunktion (LuFu) heißt auch ___; ein Belastungs-EKG heißt ___.", ["Spirometrie", "Ergometrie"],
  "Spiroergometrie = Herz-, Kreislauf- und Lungenfunktion unter Belastung.", 6)
S("Was misst ein EEG?", ["Elektrische Aktivität des Gehirns", "Elektrische Aktivität des Herzmuskels", "Nervenleitgeschwindigkeit in Armen und Beinen", "Lungenvolumen"], [0],
  "EEG = Elektroenzephalographie, Elektroden auf der Kopfhaut.", 6)
S("Was misst die NLG?", ["Wie schnell elektrische Impulse durch die Nerven geleitet werden", "Herzrhythmus", "Hirnströme", "Atemstrom"], [0],
  "NLG = Nervenleitgeschwindigkeit.", 6)
L("Endo bedeutet ___, -skopie bedeutet ___.", ["in den Körper (innen)", "hineinschauen"], "Exo/Ekto = außen.", 7)
S("Wie heißt die Spiegelung des Darms?", ["Koloskopie", "Gastroskopie", "Bronchoskopie", "Arthroskopie"], [0],
  "Gastroskopie = Magen, Bronchoskopie = Lunge, Arthroskopie = Gelenk.", 7)
S("Warum braucht eine Arthroskopie eine OP?", ["Weil man nicht durch eine natürliche Körperöffnung ins Gelenk kommt", "Weil Gelenke sehr klein sind",
  "Weil sie unter Vollnarkose sein muss", "Weil Strahlung verwendet wird"], [0], "Andere Endoskopien nutzen natürliche Körperöffnungen.", 7)
F("Welche drei Faktoren fließen in die Therapieentscheidung ein?", "Erfahrung (des Therapeuten), wissenschaftliche Erkenntnisse, Wünsche der Patient:innen",
  "Optionen abwägen und möglichst neutral beraten.", 27)
L("Off-Label bedeutet, ein ___ für etwas ganz anderes zu verwenden als eigentlich gedacht.", ["Medikament"], "Therapieoptionen haben erwünschte und unerwünschte Nebenwirkungen.", 8)
F("Nenne die drei Betätigungsbereiche, in denen die Ergotherapie Menschen stärkt (DVE-Definition).", "Selbstversorgung, Produktivität, Freizeit",
  "Ziel: Handlungsfähigkeit im Alltag, gesellschaftliche Teilhabe, Lebensqualität.", 28)
S("Was ist die Voraussetzung für jede Therapie?", ["Eine Diagnose bzw. Differentialdiagnose", "Eine Überweisung", "Ein Laborbefund", "Ein Röntgenbild"], [0],
  "Therapie – Prinzipien: Voraussetzung ist die DIAGNOSE.", 29)
S("Was ist eine Kontraindikation?", ["Ein Grund, der gegen eine Maßnahme spricht", "Ein Grund, eine Maßnahme durchzuführen", "Eine Nebenwirkung", "Eine Diagnose"], [0],
  "z. B. bei Fieber kein Sport. Absolut = in jedem Fall, relativ = manchmal.", 9)
L("Eine ___ Therapie hat heilende Absicht, eine ___ Therapie lindert Schmerzen/Beschwerden, eine ___ Therapie unterstützt.", ["kurative", "palliative", "supportive"],
  "kurativ / palliativ / supportiv", 9)
S("Was bedeutet „kausale“ Therapie?", ["Behandlung der Ursache", "Behandlung der Symptome", "Bewahrende Therapie", "Operative Therapie"], [0],
  "Gegenteil: symptomatisch → behandelt die Symptome.", 9)
S("Was bedeutet „elektiv“ bei einer Operation?", ["Wahlweise – irgendwann gehört es gemacht", "Sofort", "Sehr bald", "Gar nicht"], [0],
  "Reihenfolge der Dringlichkeit: elektiv – dringlich – akut – Notfall.", 9)
S("Was ist eine konservative Therapie?", ["Bewahrende Therapie ohne Operation", "Verändernde Therapie mit Operation", "Therapie der Ursache", "Schmerzlindernde Therapie"], [0],
  "Konservativ (bewahrend) ↔ operativ (verändernd).", 9)
F("Definiere Prävention.", "Maßnahme, um eine gesundheitliche Schädigung durch gezielte Aktivitäten zu verhindern, weniger wahrscheinlich zu machen oder zu verzögern",
  "Prävention = Prophylaxe.", 30)
S("*Eine Ernährungsumstellung nach einem Herzinfarkt ist welche Form der Prävention?", ["Tertiärprävention", "Primärprävention", "Sekundärprävention", "Quartäre Prävention"], [0],
  "Tertiär = Verschlimmerung einer manifesten Erkrankung vermeiden.", 10)
S("*Bei Schnupfen kein Antibiotikum zu geben ist ein Beispiel für …", ["Quartäre Prävention", "Primärprävention", "Sekundärprävention", "Rehabilitation"], [0],
  "Quartär = unnötige Maßnahmen, Übermedikation und Überversorgung vermeiden.", 10)
S("*Nicht zu rauchen ist ein Beispiel für …", ["Primärprävention", "Sekundärprävention", "Tertiärprävention", "Quartäre Prävention"], [0],
  "Primär = Gesundheit erhalten, Risikofaktoren vermeiden.", 10)
L("Die Sekundärprävention verhindert das Fortschreiten eines ___, z. B. Ernährungsumstellung bei beginnendem ___.", ["Erkrankungsfrühstadiums", "Diabetes"],
  "Sie greift in bestehende Risikofaktoren ein.", 31)
F("Nenne die vier Phasen des Rehabilitations-Phasenmodells.", "I im Krankenhaus; II stationäre Reha; III ambulante Reha/Alltag; IV Rekonstitution/Alltag",
  "Reha = Wiederherstellung des Ausgangszustandes vor einem Ereignis.", 32)


# ---------------------------------------------------------------- 2 Kardiologie
K("2")
S("Wie viel Blut pumpt das Herz ungefähr pro Minute?", ["ca. 5 Liter", "ca. 1 Liter", "ca. 10 Liter", "ca. 0,5 Liter"], [0], "Herz = elektrisches Organ, Puls = Ergebnis des Herzschlags.", 11)
S("Welche Struktur gibt den normalen Herzrhythmus vor?", ["Sinusknoten", "AV-Knoten", "His-Bündel", "Herzklappe"], [0],
  "Reizleitung: Sinusknoten → AV-Knoten → His-Bündel.", 34)
L("Der normale Herzrhythmus heißt ___ und liegt bei ___ Schlägen pro Minute.", ["Sinusrhythmus", "60–80 (90)"], "Etwa 100.000 Schläge pro Tag.", 35)
S("*Ab welcher Herzfrequenz spricht man von einer Tachykardie?", ["> 100/min", "> 80/min", "> 60/min", "> 150/min"], [0],
  "tachy = schnell. Bradykardie: < 55/min.", 35)
S("*Ab welcher Herzfrequenz spricht man laut Skript von einer Bradykardie?", ["< 55/min", "< 70/min", "< 40/min", "< 90/min"], [0],
  "brady = langsam.", 35)
S("Womit tastet man den Puls?", ["Mit Zeige- und Mittelfinger", "Mit dem Daumen", "Mit der ganzen Handfläche", "Nur mit dem Stethoskop"], [0],
  "Der Daumen hat einen eigenen Puls → Verwechslungsgefahr.", 11)
L("Atrial bedeutet den ___ betreffend und wird auch als ___ bezeichnet.", ["Vorhof", "supraventrikulär"], "supraventrikulär = über den Kammern.", 11)
S("Welche Rhythmusstörungen sind atrial (supraventrikulär)?", ["Vorhofflimmern", "pSVT", "Kammerflimmern", "Ventrikuläre Tachykardie"], [0, 1],
  "Ventrikulär: Kammerflattern, Kammerflimmern, ventrikuläre Tachykardie.", 37)
F("Was passiert beim Kammerflimmern?", "Kammern schlagen unkontrolliert, extrem schnell → kein geordnetes Zusammenziehen → kein Blut wird mehr gepumpt",
  "Lebensbedrohlich → Reanimation/Defibrillation.", 12)
S("Was ist eine Extrasystole?", ["Ein Herzschlag außerhalb des normalen Taktes, ausgelöst durch einen zusätzlichen Impuls", "Ein dauerhaft zu langsamer Puls",
  "Ein Verschluss eines Herzkranzgefäßes", "Eine defekte Herzklappe"], [0], "Kann im Vorhof (atrial) oder in der Kammer (ventrikulär) entstehen.", 11)
S("Was beschreibt eine pSVT?", ["Immer wieder plötzlich schnelles Herz, dann wieder normal", "Dauerhaft langsamer Herzschlag",
  "Vorhof schlägt regelmäßig, aber schnell", "Kammern schlagen unkontrolliert"], [0], "paroxysmal = anfallsartig, plötzlich und ohne Vorwarnung.", 11)
L("Beim Blutdruckmessen mit Oberarmmanschette sind der 1. und 2. Wert der ___, der 3. Wert der ___.", ["Blutdruck", "Puls"], "Abkürzung RR, Einheit mmHg (Millimeter Quecksilbersäule).", 12)
S("*Wie hoch ist der ideale Blutdruck?", ["< 120/80 mmHg", "< 140/90 mmHg", "< 135/85 mmHg", "< 100/60 mmHg"], [0],
  "Normal 120–129/80–84; hoch normal 130–139/85–89.", 39)
S("*Ab welchem Wert spricht man in der Ordination von Hypertonie?", ["≥ 140/90 mmHg", "≥ 120/80 mmHg", "≥ 130/85 mmHg", "≥ 160/100 mmHg"], [0],
  "Selbstmessung: 7 oder mehr von 30 Werten ≥ 135/85 mmHg.", 38)
S("*Ein Blutdruck von 165/102 mmHg entspricht …", ["Hypertonie-Stadium 2", "Hypertonie-Stadium 1", "Hypertonie-Stadium 3", "hoch normal"], [0],
  "Stadium 2: ≥ 160–179 / 100–109 mmHg.", 39)
S("Was ist eine isolierte systolische Hypertonie?", ["Systolisch ≥ 140, diastolisch < 90 mmHg", "Diastolisch ≥ 90, systolisch < 140 mmHg",
  "Beide Werte ≥ 180/110 mmHg", "Nur nachts erhöhter Blutdruck"], [0], "Nur der obere Wert ist erhöht.", 39)
L("Der Goldstandard der Blutdruckdiagnose ist die ___-Messung; das Absinken des Blutdrucks in der Nacht heißt physiologisches ___.", ["24h-RR", "Dipping"],
  "24h-RR: 60–70 Messungen mit Tag/Nacht-Vergleich.", 38)
S("Warum muss man Bluthochdruck mehrmals messen?", ["Ein einzelner Wert kann z. B. durch Stress erhöht sein", "Das Gerät ist ungenau", "Der Puls stört die Messung", "Wegen des Dippings"], [0],
  "Mehrmals, auch unterwegs messen.", 12)
S("In wie viel Prozent hat Bluthochdruck keine eindeutige organische Ursache?", ["90–95 %", "50 %", "5–10 %", "100 %"], [0],
  "Nur 5–10 % haben eine organische Ursache (z. B. Niere, Nebenniere, Schlafapnoe).", 40)
F("Nenne Risikofaktoren für Bluthochdruck.", "Familiäre Neigung, Übergewicht, Bewegungsmangel, hoher Salzkonsum, Stress", "In 90–95 % keine organische Ursache.", 40)
S("Welche Aussage zu Symptomen des Bluthochdrucks stimmt?", ["Oft gibt es gar keine Symptome", "Er verursacht immer Kopfschmerzen", "Er ist immer schmerzhaft", "Er zeigt sich durch Fieber"], [0],
  "Mögliche Symptome: Schwindel, Kopfschmerzen, Nasenbluten, Atemnot, Angina pectoris.", 41)
F("Nenne nicht-medikamentöse Maßnahmen gegen Bluthochdruck.",
  "Selbstmessung, Gewichtsreduktion, Bewegung, Salz reduzieren (< 5 g/Tag), ausreichend Schlaf, Entspannung, weniger Alkohol, Rauchstopp",
  "Medikamente sind laut Mitschrift für die Prüfung nicht so wichtig.", 42)
L("Bei Bluthochdruck sollte der Salzkonsum unter ___ pro Tag liegen.", ["5 g"], "Kalium und Ballaststoffe unterstützen.", 42)
S("Was lagert sich bei der Arteriosklerose in der Gefäßinnenschicht ab?", ["Blutfette, Thromben, Bindegewebe, Kalk (Plaques)", "Nur Wasser", "Harnsäurekristalle", "Bakterien"], [0],
  "Folge: Einengung des Gefäßdurchmessers und verminderte Durchblutung.", 44)
F("Nenne Folgekrankheiten der Arteriosklerose.", "KHK, Herzinfarkt, Schlaganfall, pAVK, Aortenaneurysma, Niereninsuffizienz, Erblindung",
  "Herz → Infarkt, Halsschlagader → Schlaganfall, Beine → pAVK.", 47)
S("Warum zeigt sich Arteriosklerose oft erst unter Belastung?", ["In Ruhe reicht die Durchblutung oft noch aus", "Weil sich die Gefäße in Ruhe weiten", "Weil der Blutdruck in Ruhe steigt", "Weil Plaques nur bei Bewegung entstehen"], [0],
  "Darum wird ein Belastungs-EKG gemacht.", 13)
S("Was ist die koronare Herzkrankheit (KHK)?", ["Verengung der Herzkranzgefäße", "Entzündung des Herzmuskels", "Defekte Herzklappe", "Rhythmusstörung im Vorhof"], [0],
  "Eine der häufigsten Erkrankungen in westlichen Industrienationen; Männer > Frauen; zunächst unbemerkt.", 48)
L("Das Leitsymptom der KHK ist die Angina pectoris, übersetzt ___.", ["Brustenge"], "Ziehen und Brennen im Brustkorb, manchmal mit Ausstrahlung.", 49)
S("Was kennzeichnet eine INSTABILE Angina pectoris?", ["Neu aufgetreten", "Beschwerden in Ruhe", "Über Monate gleichbleibend", "Nur bei Belastung"], [0, 1],
  "Stabil: bei Belastung, über Monate gleichbleibend. Instabil: neu, Verschlechterung, Ruhebeschwerden.", 49)
S("Warum spricht man bei Herzinfarkt-Symptomen von einem „Genderproblem“?", ["Die typische Symptombeschreibung ist männlich – Frauen haben oft andere Symptome", "Frauen bekommen nie Herzinfarkte",
  "Männer haben nie Brustschmerzen", "Nur Frauen haben Angina pectoris"], [0], "Schmerzen sind bei Männern typischer als bei Frauen.", 14)
F("Was passiert beim Herzinfarkt?", "Verschluss eines Herzkranzgefäßes → Sauerstoffmangel → Herzmuskel stirbt ab (Nekrose), kann nicht mehr kontrahieren → Narbe",
  "Konsequenz: Herzschwäche.", 50)
S("*Woran erkennt man einen Herzinfarkt im Unterschied zur Angina pectoris?", ["Schmerz intensiver und länger als 20 Minuten", "Nitroglyzerin hilft nicht mehr",
  "Schmerz verschwindet nach wenigen Sekunden", "Nur bei Belastung"], [0, 1], "Sonst wie instabile Angina pectoris.", 51)
F("*Was tust du bei Verdacht auf Herzinfarkt?", "Notarzt rufen („time is muscle“), nicht selbst fahren, Oberkörper hoch lagern, Frischluft, beengende Kleidung öffnen, ggf. Nitroglyzerin/Aspirin",
  "Jede Minute zählt für den Herzmuskel.", 51)
L("Beim Herzinfarkt gilt: „time is ___“.", ["muscle"], "Je schneller behandelt wird, desto mehr Herzmuskel überlebt.", 51)
F("Womit wird ein Herzinfarkt diagnostiziert?", "Beschwerdebild, EKG, Blut (Herzenzyme), Herzultraschall", "", 52)
S("Was ist das Ziel der Behandlung beim Herzinfarkt?", ["Wiedereröffnung des verschlossenen Gefäßes", "Senkung der Herzfrequenz", "Entfernung der Narbe", "Herztransplantation"], [0],
  "Coronarangiographie mit Dehnung und Stent, Lysetherapie, Medikamente.", 53)
S("Was ist Herzinsuffizienz?", ["Unvermögen des Herzens, Organe ausreichend mit Blut und Sauerstoff zu versorgen", "Zu schneller Herzschlag", "Verkalkung der Beinarterien", "Entzündung der Herzklappen"], [0],
  "Systolisch = Pumpschwäche (HFREF), diastolisch = Füllungsstörung (HFPEF).", 54)
F("Nenne Ursachen der Herzinsuffizienz.", "Herzinfarkt (häufigste), Bluthochdruck, defekte Herzklappen, Herzmuskelerkrankungen", "", 55)
F("Nenne die vier Säulen der Therapie der Herzinsuffizienz.", "Lifestyle, Medikamente, Trainingstherapie, Interventionen/Devices", "", 56)
S("*In welchem Verhältnis werden bei der Reanimation Herzdruckmassage und Beatmung durchgeführt?", ["30 : 2", "15 : 2", "5 : 1", "30 : 5"], [0],
  "Wenn keine Beatmung möglich: nur Herzdruckmassage!", 58)
S("*Wie wird die Herzdruckmassage durchgeführt?", ["Frequenz 100/min", "Drucktiefe ca. 5 cm", "Druckpunkt am Bauch", "Drucktiefe ca. 1 cm"], [0, 1],
  "Druckpunkt: Mitte des Brustkorbs (untere Sternumhälfte), gestreckte Arme.", 67)
S("Was gilt bei der Atemkontrolle als Atemstillstand?", ["Schnappatmung", "Schaukelatmung", "Ruhige, normale Atmung", "Schnarchen"], [0, 1],
  "MEMO: Schnapp- und Schaukelatmung gelten als Atemstillstand.", 60)
S("Was machst du bei einer bewusstlosen Person mit normaler Atmung?", ["Stabile Seitenlage", "Herzdruckmassage", "Beine hochlagern und warten", "Defibrillieren"], [0],
  "Hält die Atemwege offen.", 62)
L("Das Anheben des Unterkiefers mit beiden Händen heißt ___-Handgriff.", ["Esmarch"], "Bei HWS-Verletzung unter Halten des Kopfes.", 61)
F("Wie überprüfen Laien die Vitalfunktionen und wann beginnen sie mit der CPR?", "Bewusstsein (ansprechen, rütteln) und Atmung (sehen, hören, fühlen) prüfen; nicht ansprechbar + keine normale Atmung → CPR",
  "Pulskontrolle nur für Profis.", 65)
S("Wie lange darf der komplette Diagnostikblock (Bewusstsein, Atmung, Kreislauf) bei Profis dauern?", ["Höchstens 10 Sekunden", "1 Minute", "30 Sekunden", "2 Minuten"], [0], "", 64)
S("Was passiert nach einem Defibrillator-Schock?", ["Sofort 2 Minuten weiter CPR", "Puls 1 Minute lang tasten", "Patient in Seitenlage bringen", "Sofort zweiter Schock"], [0],
  "Nach 2 Minuten Rhythmusanalyse.", 70)


# ---------------------------------------------------------------- 3 Angiologie
K("3")
S("Welche Risikofaktoren der Arteriosklerose sind UNVERÄNDERBAR?", ["Alter", "Geschlecht", "Rauchen", "Bewegungsmangel"], [0, 1],
  "Unveränderbar: Geschlecht, Alter, genetische Disposition.", 74)
F("Nenne die klassischen (beeinflussbaren) Risikofaktoren der Arteriosklerose.",
  "Rauchen, Bluthochdruck, Dyslipidämie, Diabetes mellitus, Übergewicht/Adipositas, Bewegungsmangel, Stress, Hyperurikämie", "", 74)
L("Dyslipidämie ist eine ___; Hyperurikämie ist ein dauerhaft erhöhter ___ im Blut.", ["Fettstoffwechselstörung", "Harnsäurespiegel"], "Beides Risikofaktoren der Arteriosklerose.", 74)
S("Warum sind Männer häufiger von Arteriosklerose/KHK betroffen?", ["Östrogenschutz der Frauen und gefährlicherer Lebensstil der Männer", "Männer haben kleinere Gefäße",
  "Männer haben mehr Blut", "Männer haben einen langsameren Puls"], [0], "", 14)
S("Wie viele Österreicher:innen sterben jährlich an den Folgen des Rauchens?", ["ca. 14.000", "ca. 1.400", "ca. 140.000", "ca. 5 Millionen"], [0],
  "Weltweit ca. 5 Millionen.", 76)
L("Kohlenmonoxid bindet ca. ___-mal besser an Hämoglobin als Sauerstoff.", ["250"], "Folge: Sauerstoffmangel, das Herz muss mehr arbeiten.", 79)
F("Welche drei schädlichen Hauptbestandteile des Tabakrauchs nennt das Skript?", "Nikotin (macht abhängig), Kohlenmonoxid (verdrängt Sauerstoff), Teer/Rauchinhalts- und Reizstoffe",
  "Teer zerstört die Flimmerhärchen.", 77)
S("Welche körperlichen Effekte hat Nikotin?", ["Gefäßverengung", "Anstieg von Blutdruck und Herzfrequenz", "Senkung des Blutdrucks", "Steigerung des Hungergefühls"], [0, 1],
  "Nikotin verringert das Hungergefühl und wirkt nach 10 s im Gehirn.", 78)
S("Was zerstören Teer und Rauchinhaltsstoffe in den Atemwegen?", ["Die Flimmerhärchen", "Die Bronchialknorpel", "Das Zwerchfell", "Die Lungenkapillaren"], [0],
  "Folge: Nährboden für Bakterien, Bronchitis, Emphysem, Krebs.", 80)
S("Was ist laut Skript die erfolgreichste Art, mit dem Rauchen aufzuhören?", ["Sofortiger Rauchstopp", "Langsames Reduzieren", "Nikotinpflaster allein", "Hypnose"], [0],
  "„Dissonante Raucher“ wollen aufhören, wissen aber nicht wie.", 81)
L("Ein gesundes Endothel produziert ___ (Stickstoffmonoxid), das die Gefäße erweitert (___).", ["NO", "Vasodilatation"], "Endotheldysfunktion → weniger NO → Vasokonstriktion.", 82)
S("*Was ist die Claudicatio intermittens?", ["Die „Schaufensterkrankheit“ – Symptom der pAVK", "Eine Venenentzündung", "Ein Aortenriss", "Eine Herzrhythmusstörung"], [0],
  "Betroffene müssen beim Gehen immer wieder stehen bleiben.", 83)
F("Nenne mögliche Anzeichen einer pAVK.", "Kühle, blasse, marmorierte Haut; trockene Haut; Schmerzen beim Gehen (Wade, Oberschenkel, Gesäß); Verhornung; langsam wachsende Nägel; Haarverlust an den Beinen; schlecht heilende Wunden; Erektionsstörungen",
  "", 84)
S("Warum ist die pAVK ein Warnsignal?", ["Sie kann Vorbote von Herzinfarkt und Schlaganfall sein", "Sie verkürzt die Lebenserwartung um ca. 8 Jahre",
  "Sie heilt immer von selbst", "Sie betrifft nur junge Menschen"], [0, 1], "Mortalität doppelt so hoch wie in der Gesamtbevölkerung.", 85)
S("*Ab welchem Knöchel-Arm-Index (ABI) liegt eine pAVK vor?", ["< 0,9", "< 1,5", "> 1,0", "< 0,5"], [0],
  "Bsp.: Knöchel 100, Arm 125 → 100:125 = 0,8 → leichte pAVK.", 86)
S("Welches pAVK-Stadium bedeutet Schmerzen in Ruhe, besonders im Liegen?", ["Stadium III", "Stadium I", "Stadium IIa", "Stadium IV"], [0],
  "I keine Beschwerden; II Belastungsschmerz (IIa ≥ 200 m, IIb < 200 m); III Ruheschmerz; IV Gewebeschäden/Geschwüre.", 87)
L("Bei pAVK Stadium IIa beträgt die schmerzfreie Gehstrecke ___, bei IIb ___.", ["200 m und mehr", "weniger als 200 m"], "", 87)
F("Nenne Therapieoptionen bei pAVK.", "Risikofaktoren bekämpfen, Gehtraining, Medikamente (z. B. Prostanoide), Angioplastie/Stent, Ausschälung, Bypass-OP, Amputation", "", 88)
F("*Nenne die 6 P's der akuten Beinischämie.", "Pain (Schmerz), Paleness (Blässe), Paraesthesia (Gefühlsstörung), Paralysis (Lähmung), Pulselessness (kein Puls), Prostration (Schock)",
  "Nach 6–12 h droht Rhabdomyolyse (Zerstörung von Muskelfasern).", 89)
S("Wie wird das Bein beim akuten arteriellen Verschluss gelagert?", ["Tief", "Hoch", "Gestreckt in Kälte", "Mit Kompressionsverband"], [0],
  "Außerdem Watteverband, Schmerzmittel, Anti-Thrombotika, Schockprophylaxe.", 90)
L("Ein Aneurysma ist eine ___ eines Gefäßes, über ___ mm oder über das 1,5-Fache des Normaldurchmessers.", ["Aufweitung", "30"], "Mortalität bei Ruptur 65–85 %.", 91)
S("Ab welcher Größe wird ein Bauchaortenaneurysma (AAA) operiert bzw. mit Stent versorgt?", ["> 5,5 cm", "> 3 cm", "> 4,5 cm", "> 10 cm"], [0],
  "< 4,5 cm: Ultraschall alle 6 Monate; 4,5–5,5 cm: alle 3 Monate.", 92)
S("Was unterscheidet die Aortendissektion von der Aneurysmaruptur?", ["Bei der Dissektion reißt nur die innere Schicht und Blut fließt in die Gefäßwand", "Bei der Dissektion reißen alle Schichten",
  "Die Dissektion betrifft nur Venen", "Es gibt keinen Unterschied"], [0], "", 93)
F("Welche drei Mechanismen sorgen für den venösen Rückstrom aus den Beinen?", "Venenklappen, Muskelpumpe, Arterienpulswelle", "Muskelpumpe und Pulswelle fehlen im oberflächlichen Venensystem.", 94)
S("Wie viel Prozent des Blutes befinden sich in den Venen?", ["ca. 80 %", "ca. 20 %", "ca. 50 %", "ca. 95 %"], [0], "Venen haben schwache Wände.", 94)
S("Was ist eine Phlebothrombose?", ["Thrombose der tiefen Beinvenen", "Entzündung oberflächlicher Venen", "Erweiterung oberflächlicher Venen", "Arterienverschluss"], [0],
  "Varikositas = Krampfadern; Thrombophlebitis = oberflächliche Venenentzündung.", 95)
L("Die Varikositas ist eine irreversible Erweiterung ___ Venen.", ["oberflächlicher"], "Umgangssprachlich: Krampfadern.", 95)
F("Nenne Symptome der Varikositas.", "Schweregefühl, Schwellneigung, nächtliche Wadenkrämpfe, Jucken; spät: Ödeme, trophische Störungen, Ulcus cruris venosum", "", 97)
F("Nenne Risikofaktoren für eine Thrombose.", "Bewegungsmangel (Flug, Bettlägerigkeit), Pille + Rauchen, Übergewicht, Flüssigkeitsmangel, Krebs, frühere Thrombosen, Schwangerschaft, Vorhofflimmern, Drogen",
  "Ursache: verlangsamter Blutfluss und Blutverdickung.", 98)
S("*Welche Zeichen sprechen für eine tiefe Beinvenenthrombose?", ["Einseitige Schwellung mit Schmerzen", "Überwärmung und Spannungsgefühl", "Beidseitig kalte, blasse Füße", "Schmerz bessert sich beim Tieflagern"], [0, 1],
  "Seitenungleichheit + dickeres Bein tut weh → wahrscheinlich Thrombose. Linderung bei Hochlagerung.", 99)
S("Welches Medikament ist bei der Thrombosetherapie UNWIRKSAM?", ["ASS (Aspirin)", "Heparin", "DOAK", "Vitamin-K-Antagonisten"], [0],
  "Außerdem: Kompression, Mobilisierung, ausreichend Flüssigkeit.", 100)
L("Eine Lungenembolie ist der Verschluss eines Lungenarterienastes durch einen verschleppten ___; Quelle sind in ca. 70 % ___.", ["Thrombus (Embolus)", "Becken-Bein-Thrombosen"],
  "Kardiovaskulärer Notfall mit hoher Letalität.", 101)
S("Was ist das häufigste Symptom der Lungenembolie?", ["Dyspnoe (Atemnot)", "Bluthusten", "Husten", "Synkope"], [0], "Dyspnoe 82 %, Tachypnoe 60 %, Brustschmerz 49 %.", 102)
S("Welcher Laborwert wird bei Verdacht auf Lungenembolie bestimmt?", ["D-Dimer", "HbA1c", "TSH", "Kreatinin"], [0], "Außerdem Scores, Echo, Kontrastmittel-CT.", 102)

# ---------------------------------------------------------------- 4 Pulmologie
K("4")
S("Was misst die Spirometrie?", ["Lungen- und Atemvolumina", "Sauerstoffgehalt im Blut", "Herzrhythmus", "Blutzucker"], [0],
  "Einsatz bei Asthma/COPD: Diagnose, Verlaufskontrolle, Medikamenteneinstellung.", 106)
S("Was bedeutet eine Obstruktion in der Spirometrie?", ["Problem der Atemwege – genug Luft, aber Problem beim Transport", "Die Lunge kann sich nicht ausdehnen", "Zu viel Sauerstoff", "Herzschwäche"], [0],
  "Obstruktiv: z. B. Asthma, COPD. Restriktion = Ausdehnung eingeschränkt.", 107)
F("Welche Aufgaben haben obere und untere Atemwege?", "Obere: Abwehr von Bakterien, Pollen, Abgasen, Rauch, Staub (Flimmerhärchen); untere: Gasaustausch (O2-Aufnahme, CO2-Abgabe)", "Die Lunge hat ständigen Kontakt zur Außenwelt.", 105)
S("*Was kennzeichnet Asthma bronchiale?", ["Variable und reversible Atemwegsverengung", "Chronische Entzündung der Bronchialschleimhaut", "Irreversible Zerstörung der Alveolen", "Immer bakterielle Ursache"], [0, 1],
  "Übererregbarkeit der Bronchien, z. B. nach Allergenkontakt → Schleimhaut schwillt an.", 108)
F("Nenne Formen von Asthma.", "Exogen-allergisch, endogen, Mischform, Analgetika-Asthma, Anstrengungsasthma (belastungsinduziert)", "Exogen = äußerer Auslöser.", 108)
S("Wann tritt Asthma-Atemnot typischerweise besonders auf?", ["In den frühen Morgenstunden", "Nur mittags", "Nur beim Essen", "Nie nach Anstrengung"], [0],
  "Außerdem Atemnot nach Anstrengung, Engegefühl, glasig-zäher Auswurf.", 109)
F("*Wie verhältst du dich bei einem akuten Asthmaanfall?", "1–2 Hübe kurzwirksames Bronchienspray, Ruhe bewahren, Entspannungsposition, Lippenbremse; keine Besserung nach 5 min → Notarzt",
  "", 110)
L("Bei keiner Besserung eines Asthmaanfalls innerhalb von ___ Minuten wird der Notarzt gerufen; die Atmung erfolgt über die ___.", ["5", "Lippenbremse"], "", 110)
S("Wofür steht COPD?", ["Chronic Obstructive Pulmonary Disease", "Chronic Obesity Pulmonary Disorder", "Cardiac Obstructive Pulse Disease", "Chronic Oxygen Pressure Deficit"], [0],
  "Chronisch obstruktive Lungenerkrankung durch eingeatmete Schadstoffe.", 111)
L("Akute Verschlechterungen bei COPD heißen ___.", ["Exazerbationen"], "Meist infektgetriggert.", 111)
S("Welche Aussagen zu COPD stimmen?", ["Häufig, verhinderbar und behandelbar", "Meist Folge von Schadstoffinhalation (v. a. Rauchen)", "Vollständig reversibel wie Asthma", "Betrifft nur Kinder"], [0, 1],
  "COPD ist progressiv und chronisch-entzündlich.", 111)
S("Was ist ein Lungenemphysem?", ["Irreversible Zerstörung der Alveolarwände", "Wasser in der Lunge", "Bakterielle Lungenentzündung", "Lungenkrebs"], [0], "", 113)
F("Nenne die drei Diagnosekriterien der COPD.", "A) Leitsymptome (chronischer Husten ± Sputum, Dyspnoe, Exazerbationen); B) Exposition gegenüber Noxen (Rauch, Arbeitsplatz); C) Lungenfunktion FEV1/FVC < 70 % und FEV1 < 80 % des Sollwertes",
  "", 114)
F("Was bedeutet COPD für Betroffene im Alltag?", "Häufige Atemnot, Invalidisierung, soziale Isolation, wiederholte Krankenhausaufenthalte, Angst vor Ersticken", "Wichtig für die Ergotherapie (Teilhabe).", 115)
L("Die Pneumonie ist eine Entzündung des ___.", ["Lungenparenchyms (Lungengewebes)"], "Erreger: Bakterien, Viren, Pilze, Parasiten oder chemisch-irritativ.", 116)
F("Nenne die Diagnosekriterien einer Pneumonie.", "2 von 4: typischer Auskultationsbefund, Fieber, Husten, Auswurf; plus Tachykardie/Tachypnoe, neues Infiltrat im Röntgen, Entzündungszeichen im Labor",
  "", 117)
S("Was sieht man bei einer Lungenentzündung im Röntgenbild?", ["Ein Infiltrat (Gewebeverdichtung)", "Ein Aneurysma", "Eine Fraktur", "Freie Luft im Bauch"], [0],
  "Infiltrat = etwas ist dort, wo es nicht hingehört.", 118)
F("Nenne Therapiemaßnahmen bei Pneumonie.", "Atemgymnastik, viel trinken, Antibiotika, Schleimlöser, Schmerztherapie, frühe Mobilisierung", "Bettlägerigkeit so kurz wie möglich.", 119)
S("*Wann spricht man von einer nosokomialen Pneumonie?", ["Später als 48 Stunden nach Krankenhausaufnahme", "Bis 14 Tage nach Krankenhausentlassung", "Innerhalb der ersten 12 Stunden zu Hause", "Nur bei Kindern"], [0, 1],
  "Erreger oft resistent gegen typische Antibiotika.", 120)
S("Was ist der wichtigste Risikofaktor für eine nosokomiale Pneumonie?", ["Maschinelle Beatmung", "Rauchen", "Übergewicht", "Junges Alter"], [0],
  "89 % der nosokomialen Pneumonien bei beatmeten Patienten.", 121)
S("Welche ist die häufigste Krankenhausinfektion?", ["Harnwegsinfekt", "Pneumonie", "Wundinfektion", "Sepsis"], [0],
  "Die Pneumonie ist die zweithäufigste, aber häufigste Todesursache unter den Krankenhausinfektionen.", 121)
S("Wie viel Prozent der primären Lungentumoren sind Karzinome?", ["90 %", "50 %", "10 %", "100 %"], [0], "Männer : Frauen = 2 : 1; Gipfel 60.–70. Lebensjahr.", 123)
S("*Ab wann muss ein trockener anhaltender Husten abgeklärt werden?", ["Länger als 4 Wochen", "Länger als 3 Tage", "Länger als 1 Jahr", "Nie"], [0],
  "Weitere Symptome: atemabhängige Schmerzen, Heiserkeit, Hämoptysen, Gewichtsverlust.", 124)
L("Hämoptysen bedeutet ___.", ["Bluthusten"], "Symptom bei Lungenkrebs und Lungenembolie.", 102)


# ---------------------------------------------------------------- 5 Gastroenterologie
K("5")
L("GERD steht für ___ und bezeichnet den krankhaften Rückfluss von Magensäure in die ___.", ["Gastro Esophageal Reflux Disease", "Speiseröhre"],
  "Schließmuskel schließt nicht gut → Säure verätzt die Speiseröhre.", 128)
S("*Welcher Gastritis-Typ ist am häufigsten?", ["Typ B – bakteriell (Helicobacter pylori)", "Typ A – autoimmun", "Typ C – chemisch-toxisch", "Alle gleich häufig"], [0],
  "A 5 %, B 85 %, C 10 %.", 129)
S("Welche Folge hat die Typ-A-Gastritis (autoimmun)?", ["Vitamin-B12-Mangel / perniziöse Anämie", "Teerstuhl", "Laktoseintoleranz", "Leberzirrhose"], [0], "", 129)
S("Wodurch entsteht eine Typ-C-Gastritis?", ["Chemisch-toxisch: Alkohol, Medikamente, Gallenreflux", "Helicobacter pylori", "Autoimmunprozess", "Gluten"], [0], "", 129)
F("Nenne Symptome einer Gastritis.", "Druck/Schmerz im linken Oberbauch (nach dem Essen verstärkt), Übelkeit, Erbrechen, Appetitlosigkeit, Bluterbrechen, Teerstuhl", "", 131)
L("Hämatemesis bedeutet ___, Meläna bedeutet ___.", ["Bluterbrechen", "Teerstuhl (Blut im Stuhl)"], "", 131)
S("Was bedeutet HP-Eradikation?", ["Ausrottung von Helicobacter pylori mit PPI + Antibiotika", "Entfernung des Magens", "Magenspiegelung", "Gabe von Vitamin B12"], [0],
  "Dauer: zumindest 1 Woche.", 133)
L("PPI steht für ___, umgangssprachlich ___.", ["Protonenpumpenhemmer", "Magenschutztabletten"], "", 133)
S("Welche Komplikationen hat ein Magen-/Zwölffingerdarmgeschwür?", ["Blutung", "Perforation", "Laktoseintoleranz", "Hepatitis"], [0, 1],
  "Weitere: Penetration in Nachbarorgane (z. B. Pankreas), Karzinom.", 134)
S("Was ist eine Penetration beim Ulcus?", ["Durchbruch in ein Nachbarorgan (z. B. Pankreas)", "Durchbruch in die freie Bauchhöhle", "Blutung in den Magen", "Narbenbildung"], [0],
  "Perforation = Durchbruch in die Bauchhöhle.", 134)
F("Nenne Ursachen des Magenkarzinoms.", "Nitrosamine (Pökeln), vitaminarme Ernährung, Alkohol, Nikotin, chronische Gastritis, chronische Ulcera, Magenpolypen, Z. n. Teilresektion", "", 138)
S("Wie viele Patient:innen haben bei Entdeckung eines Magenkarzinoms schon Metastasen?", ["ca. 70 %", "ca. 10 %", "ca. 30 %", "fast keine"], [0],
  "Kurative Therapie: Gastrektomie (Magen entfernen).", 138)
S("Welche Unverträglichkeit ist eine IgE-vermittelte immunologische Reaktion?", ["Nahrungsmittelallergie", "Zöliakie", "Laktoseintoleranz", "Lebensmittelvergiftung"], [0],
  "Zöliakie ist IgE-unabhängig (IgA/IgG).", 139)
S("*Was ist der Unterschied zwischen Maldigestion und Malabsorption?", ["Maldigestion = schlechte Aufspaltung; Malabsorption = schlechte Aufnahme", "Maldigestion = schlechte Aufnahme; Malabsorption = schlechte Aufspaltung",
  "Beides bedeutet Durchfall", "Malabsorption betrifft nur den Magen"], [0], "Bei Malabsorption nimmt man ab, bei Maldigestion (z. B. Laktoseintoleranz) meist nicht.", 140)
L("Laktase spaltet Laktose (Milchzucker) in ___ und ___.", ["Galaktose", "Glukose"], "Häufigste Ursache: erworbener Laktasemangel.", 141)
S("Welche Symptome passen NICHT zur Laktoseintoleranz?", ["Gewichtsabnahme", "Blut im Stuhl", "Blähungen", "Durchfall"], [0, 1],
  "Typisch: Bauchkrämpfe, Übelkeit, Blähungen, plätschernde Darmgeräusche, Durchfall.", 142)
S("Womit wird eine Laktoseintoleranz diagnostiziert?", ["H2-Atemtest", "Laktosetest (Bluttest)", "Koloskopie", "Spirometrie"], [0, 1], "", 143)
S("Welche Lebensmittel sind bei laktosearmer Diät meist KEIN Problem?", ["Hartkäse", "Butter", "Frischmilch", "Joghurt"], [0, 1], "Frischmilchprodukte reduzieren.", 144)
L("Ursache der Histaminintoleranz ist ein Mangel an ___ (DAO) im Dünndarm.", ["Diaminoxidase"], "", 145)
F("Nenne histaminreiche Lebensmittel bzw. Histaminliberatoren.", "Rotwein, Sekt, Weizenbier, gereifter Käse (Emmentaler, Parmesan), Salami, Schinken; Liberatoren: Schokolade, Zitrusfrüchte, Nüsse", "", 146)
S("*Was ist die Behandlung der Zöliakie?", ["Lebenslange glutenfreie Ernährung", "Laktosefreie Diät", "Antibiotika", "Operation"], [0],
  "Gluten (Weizenkleberprotein) führt zu Zottenatrophie im Dünndarm.", 147)
S("Welche Getreide sind bei Zöliakie ERLAUBT?", ["Reis", "Mais", "Dinkel", "Gerste"], [0, 1], "Erlaubt: Buchweizen, Hirse, Mais, Reis. Verboten: Weizen, Gerste, Roggen, Dinkel.", 148)
L("Bei Zöliakie verändert sich die Dünndarmschleimhaut: es kommt zur ___.", ["Zottenatrophie"], "Folge: Malabsorption.", 147)
S("Welches Risiko besteht bei therapieresistenter (refraktärer) Zöliakie?", ["Lymphomrisiko", "Herzinfarkt", "Diabetes Typ 1", "Lungenembolie"], [0], "Durch die chronische Entzündung.", 149)
F("Wie lauten die Kriterien des Reizdarmsyndroms?", "> 6 Monate; mind. 3 Tage/Monat in den letzten 3 Monaten Bauchschmerzen + mind. 2 von: Besserung nach Stuhlgang, Änderung der Stuhlfrequenz, Änderung der Stuhlkonsistenz",
  "Rome-III-Kriterien.", 150)
S("Was ist eine Gastroskopie?", ["Spiegelung von Magen und Zwölffingerdarm über den Mund", "Dickdarmspiegelung", "Enddarmspiegelung", "Lungenspiegelung"], [0],
  "Endoskopie kann auch gleich therapeutisch handeln.", 153)
L("Die beiden Hauptformen der CED sind ___ und ___.", ["Morbus Crohn", "Colitis ulcerosa"], "CED = chronisch entzündliche Darmerkrankungen, verlaufen in Schüben.", 154)
S("*Welche Aussagen treffen auf Morbus Crohn zu?", ["Kann den gesamten Verdauungstrakt betreffen", "Entzündung aller Wandschichten, segmental", "Nur Dickdarm und Rektum betroffen", "Durchgehende Entzündung ab dem Enddarm"], [0, 1],
  "Colitis ulcerosa: nur Dickdarm/Rektum, nur Schleimhaut, kontinuierlich ab Enddarm.", 155)
S("*Welche Symptome sind typisch für Colitis ulcerosa?", ["Blutig-schleimige Durchfälle", "Schmerzhafter Stuhldrang (Tenesmus)", "Fisteln und Abszesse", "Schmerzen v. a. im rechten Unterbauch"], [0, 1],
  "Morbus Crohn: Durchfall meist ohne Blut, Schmerzen rechter Unterbauch, Fisteln.", 157)
S("Welche Komplikation ist typisch für Colitis ulcerosa?", ["Toxisches Megakolon", "Fisteln", "Analfissuren", "Stenosen im Dünndarm"], [0], "", 155)
L("Darmkrebs entsteht häufig über die ___-Karzinom-Sequenz.", ["Polyp"], "Gesunde Schleimhaut → Wucherung → kleiner → großer Polyp → Karzinom.", 158)
F("Wie kann man Darmkrebs vorbeugen?", "Nicht rauchen, wenig Alkohol, kein Übergewicht, Bewegung; nicht täglich rotes Fleisch, ballaststoff- und vitaminreich, 5 Portionen Obst/Gemüse; Vorsorge", "", 159)
S("Wie stark senkt die Vorsorge das Risiko, an Darmkrebs zu versterben?", ["Von ca. 2 % auf ca. 0,2 %", "Von ca. 6 % auf ca. 3 %", "Gar nicht", "Von ca. 50 % auf 10 %"], [0], "Erkrankungsrisiko von ~6 % auf ~0,6 %.", 160)
S("Wie hoch ist die Heilungschance bei Darmkrebs im Stadium III?", ["50–70 %", "> 90 %", "ca. 80 %", "< 10 %"], [0],
  "Stadium I > 90 %, II ca. 80 %, IV < 10 %.", 162)
F("Nenne Aufgaben der Leber.", "Entgiftung, Gallenproduktion, Zucker-/Glykogenspeicher, Cholesterin- und Aminosäuresynthese, Hormone/Enzyme, Vitaminaufnahme", "", 163)
L("Chronische Leberschädigung verläuft von der ___ über die ___ zur ___.", ["Steatose (Fettleber)", "Fibrose", "Zirrhose"], "Komplikationen: Lebertumor, Blutungen.", 164)
S("Was ist laut Skript „der Schmerz der Leber“?", ["Müdigkeit", "Bauchkrämpfe", "Kopfschmerzen", "Rückenschmerzen"], [0],
  "Frühsymptome fehlen oft → Leberwerte bestimmen.", 165)
S("Was ist die häufigste Lebererkrankung?", ["Fettleber", "Hepatitis C", "Leberkrebs", "Leberzirrhose"], [0], "Ursachen: Alkohol, Übergewicht, Diabetes, Medikamente.", 168)
L("Freie Flüssigkeit im Bauch nennt man ___.", ["Aszites"], "Im Ultraschall schwarz; Zeichen der Leberzirrhose.", 167)
S("Gegen welche Hepatitis-Formen gibt es eine Impfung?", ["Hepatitis A", "Hepatitis B", "Hepatitis C", "Keine"], [0, 1], "Hepatitis C → Medikamententherapie.", 169)
S("Wie wird Hepatitis A übertragen?", ["Über verunreinigte Lebensmittel", "Über Blut", "Nur sexuell", "Über Zeckenbisse"], [0],
  "„Reisehepatitis“ – cook it, peel it or leave it.", 170)
S("Welche Hepatitis heilt in bis zu 90 % NICHT aus?", ["Hepatitis C", "Hepatitis A", "Hepatitis B", "Hepatitis E"], [0],
  "Übertragung über Blut; seit 2015 Heilungsraten bis 95 % mit Medikamenten.", 172)
L("Hepatitis B wird über ___ und ___ übertragen.", ["Blut", "Geschlechtsverkehr"], "85 % heilen aus, 10–15 % werden chronisch.", 171)
F("Nenne Zeichen der Leberzirrhose im Spätstadium.", "Gelbsucht, Aszites, Hautveränderungen, Gefäßzeichnung, Schleimhautveränderungen, Umgehungskreisläufe", "", 174)
F("Nenne Risikofaktoren für ein hepatozelluläres Karzinom (HCC).", "Chronische Hepatitis B/C, Alkohol, Aflatoxine, Hämochromatose, Übergewicht/Diabetes (NASH), Leberzirrhose", "", 176)

# ---------------------------------------------------------------- 6 Nephrologie
K("6")
S("Wo liegen die Nieren?", ["Im Retroperitoneum – außerhalb der Bauchhöhle", "In der Bauchhöhle", "Im Brustkorb", "Im kleinen Becken"], [0], "", 179)
F("Nenne Aufgaben der Niere.", "Blut von harnpflichtigen Substanzen reinigen, Blutdruck regulieren, Wasser-/Salzhaushalt, Glukoneogenese, Hormone (Erythropoetin, Renin, Calcitriol)", "", 180)
S("Welches Hormon der Niere steuert die Blutbildung?", ["Erythropoetin", "Renin", "Insulin", "Calcitriol"], [0], "Renin → Blutdruck, Calcitriol (Vit. D) → Knochen.", 180)
F("Nenne Krankheitszeichen der Niere.", "Gestörte Harnproduktion/-ausscheidung, Urinveränderungen, Flankenschmerzen, Ödeme/nephrotisches Syndrom, Hypertonie, renale Anämie", "", 181)
L("Nephrolithiasis ist die ___, Zystitis die ___.", ["Nierensteinkrankheit", "Harnblasenentzündung"], "", 182)
S("Was bedeutet Urämie?", ["Harnvergiftung", "Nierenentzündung", "Harnröhrenentzündung", "Nierensteine"], [0], "", 182)
S("Was bedeutet Urethritis?", ["Harnröhrenentzündung", "Harnblasenentzündung", "Nierenbeckenentzündung", "Nierenschwäche"], [0], "", 182)
S("Welche Form des akuten Nierenversagens ist am häufigsten?", ["Intrarenal (85 %)", "Prärenal (5 %)", "Postrenal (10 %)", "Alle gleich"], [0], "Intrarenal v. a. akute Tubulusnekrose.", 183)
S("*Was ist die Hauptursache für Dialysepflicht?", ["Diabetes mellitus", "Nierensteine", "Harnwegsinfekte", "Hepatitis"], [0], "Chronische Niereninsuffizienz.", 184)
S("Welches Stadium der chronischen Niereninsuffizienz zeigt Urämiesymptome (Übelkeit, Juckreiz, Ödeme)?", ["Stadium III – präterminal", "Stadium I", "Stadium II", "Kein Stadium"], [0],
  "IV terminal: Perikarditis, Lungenödem, Koma, Tod.", 185)
F("Nenne die beiden Formen der Nierenersatztherapie.", "Dialyse (Blutwäsche), Nierentransplantation", "Bei unheilbaren Nephropathien.", 186)


# ---------------------------------------------------------------- 7 Endokrinologie & Stoffwechsel
K("7")
S("*Was ist der Unterschied zwischen Diabetes Typ 1 und Typ 2?", ["Typ 1: Insulinmangel; Typ 2: Insulinresistenz", "Typ 1: Insulinresistenz; Typ 2: Insulinmangel",
  "Typ 1 betrifft nur Erwachsene", "Typ 2 ist immer angeboren"], [0], "Typ 2: genug Insulin, aber Rezeptoren reagieren nicht ausreichend.", 188)
L("Diabetes mellitus bedeutet wörtlich „___“.", ["honigsüßes Hindurchfließen"], "Krankhafte Erhöhung des Blutzuckerspiegels.", 188)
S("Was ist die Ursache von Diabetes Typ 1?", ["Insulin fehlt (angeboren oder Autoimmunerkrankung)", "Zu viel Insulin", "Insulinresistenz durch Übergewicht", "Schilddrüsenüberfunktion"], [0], "", 188)
S("*Welche Symptome passen zur HYPERglykämie?", ["Vermehrter Durst und Harndrang", "Schlecht heilende Wunden", "Schweißausbruch und Zittern", "Krampfanfälle"], [0, 1],
  "Hypoglykämie: Gereiztheit, Herzklopfen, Schweiß, Kopfschmerzen, Krampfanfälle.", 189)
S("*Welche Symptome passen zur HYPOglykämie?", ["Herzklopfen und Schweißausbrüche", "Gereiztheit und Krampfanfälle", "Vermehrter Durst", "Juckreiz"], [0, 1], "Hypo = zu wenig Zucker im Blut.", 189)
L("Hyperglykämie bedeutet ___ Zucker im Blut, Hypoglykämie ___ Zucker im Blut.", ["zu viel", "zu wenig"], "", 189)
S("Wie lange dauert es bei Typ-2-Diabetes oft bis zur Diagnose?", ["5–7 Jahre", "wenige Tage", "1 Monat", "20 Jahre"], [0], "Oft keine Beschwerden → nur durch Messen erkennbar.", 189)
S("*Wie hoch ist der normale Nüchternblutzucker?", ["< 100 mg/dl", "< 126 mg/dl", "< 200 mg/dl", "< 70 mg/dl"], [0], "100–125 mg/dl = Prädiabetes.", 190)
S("*Ab welchem HbA1c-Wert liegt ein Diabetes vor?", ["≥ 6,5 %", "≥ 5,7 %", "≥ 9 %", "≥ 4 %"], [0], "Prädiabetes: 5,7–6,4 %.", 190)
L("Der HbA1c ist der ___; für die Diagnose muss man ___ messen.", ["Langzeitzuckerwert", "2×"], "", 190)
F("Nenne die Diagnosekriterien des Diabetes mellitus.", "Nüchtern-BZ 2× > 126 mg/dl; beliebig gemessen 2× > 200 mg/dl; oGTT 2-h-Wert > 200 mg/dl; HbA1c ≥ 6,5 %", "", 190)
S("Bei wem wird ein oGTT typischerweise gemacht?", ["Bei Schwangeren", "Bei Verdachtspersonen", "Bei jedem Arztbesuch", "Nur bei Kindern"], [0, 1], "oGTT = oraler Glukosetoleranztest (75 g Glukose).", 190)
S("*Was ist eine Makroangiopathie?", ["Schaden an großen Blutgefäßen (KHK, pAVK, Schlaganfall)", "Schaden an kleinen Blutgefäßen (Augen, Niere, Nerven)", "Ein Augenleiden", "Eine Hormonstörung"], [0],
  "Mikroangiopathie: Sehstörungen, Nieren- und Nervenfunktionsstörungen.", 191)
F("*Nenne Spätschäden des Diabetes mellitus.", "Makroangiopathie (KHK, pAVK, Schlaganfall), Mikroangiopathie (Augen, Niere, Nerven), diabetischer Fuß, Hypo-/Hyperglykämie", "Entstehen über ca. 10 Jahre.", 191)
S("Was ist das Hauptproblem beim diabetischen Fuß?", ["Wundheilungsstörung", "Gelenkentzündung", "Knochenbruch", "Pilzbefall"], [0], "", 191)
F("Nenne Maßnahmen zu Vorbeugung und Therapie von Diabetes.", "Ernährungsumstellung, Gewichtsreduktion, Bewegung, Medikamente, Rauchstopp, Blutdruck niedrig-normal, regelmäßige Kontrollen (HbA1c, Augen, Nieren, Beine, Nerven)",
  "Medikamente muss man laut Mitschrift nicht wissen.", 193)
L("Adipositas ist ein Ungleichgewicht zwischen ___ und ___.", ["Energiezufuhr", "Energieverbrauch"], "In Industrienationen > 50 % übergewichtig.", 194)
F("Nenne Ursachen der Adipositas.", "Genetische Disposition, Ernährung/Lebensweise/Bewegungsmangel, seelische Faktoren (Stress, Einsamkeit, Frust), Krankheiten (Schilddrüsenunterfunktion, Cushing, Hirntumor)",
  "Meist Zusammenspiel von Disposition und Lebensgewohnheiten.", 195)
L("Der BMI berechnet sich aus ___ geteilt durch ___ zum Quadrat.", ["Gewicht (kg)", "Größe (m)"], "", 196)
S("*Ein BMI von 32 entspricht …", ["Adipositas I", "Übergewicht", "Adipositas II", "Normalgewicht"], [0],
  "Normal 20–25, Übergewicht 25–30, Adipositas I 30–35, II 35–40, III > 40.", 196)
S("Welche Bauchumfänge gelten als Grenzwerte?", ["Männer < 102 cm", "Frauen < 88 cm", "Männer < 120 cm", "Frauen < 70 cm"], [0, 1], "In Klammern strenger: 94 cm / 80 cm.", 196)
F("Woraus besteht das metabolische Syndrom?", "Hypertonie, Diabetes mellitus, erhöhte Blutfette und Harnsäure, Übergewicht, Bewegungsmangel → Insulinresistenz", "Auch Syndrom X genannt.", 197)
S("Was sind „Abnehmspritzen“?", ["GLP-1-Analoga", "Insulin", "Statine", "Cortison"], [0], "Bariatrische Chirurgie = Operationen zur Gewichtsreduktion.", 198)
L("Kohlenhydrate liefern ___ % der Energie, Fette ___ %, Proteine ___ %.", ["50–60", "25–35", "12–15"], "", 201)
S("Welche Nährstoffe müssen als „essenziell“ über die Nahrung zugeführt werden?", ["Bestimmte Aminosäuren", "Glykogen", "Cholesterin", "Glukose"], [0], "Proteine bestehen aus Aminosäuren.", 202)
S("*Welcher Cholesterinwert gilt als „gut“?", ["HDL", "LDL", "Triglyzeride", "Gesamtcholesterin"], [0], "HDL > 45 mg/dl; LDL („schlecht“) < 160 mg/dl; Gesamt < 200 mg/dl.", 204)
L("1 kg Körperfett entspricht ca. ___ kcal.", ["7000"], "Laut Folie: 20 Leberkäsesemmeln.", 205)
F("Nenne die drei Säulen der langfristigen Gewichtsreduktion.", "Ernährung, Training, Verhaltenstherapie", "Grundlage: negative Energiebilanz.", 206)
F("Beschreibe den Regelkreis der Schilddrüse.", "Hypothalamus → TRH → Hypophyse → TSH → Schilddrüse → T3/T4; T3/T4 hemmen Hypothalamus und Hypophyse (negative Rückkopplung)", "", 208)
S("Was kennzeichnet eine LATENTE Schilddrüsenstörung?", ["TSH verändert, T3/T4 normal", "TSH, T3 und T4 verändert", "Nur T3 verändert", "Alle Werte normal"], [0], "Manifest: TSH, T3 und T4 verändert.", 208)
S("*Welche Laborwerte passen zur Hypothyreose (Unterfunktion)?", ["TSH erhöht, T3/T4 erniedrigt", "TSH erniedrigt, T3/T4 erhöht", "Alle Werte erhöht", "Alle Werte erniedrigt"], [0], "", 213)
S("*Welche Laborwerte passen zur Hyperthyreose (Überfunktion)?", ["TSH erniedrigt, T3/T4 erhöht", "TSH erhöht, T3/T4 erniedrigt", "Nur TSH erhöht", "Alle Werte normal"], [0], "", 214)
F("Nenne Symptome der Schilddrüsenunterfunktion.", "Müde, matt, antriebslos; Bradykardie, Hypotonie, Verstopfung; kühle, trockene Haut; Myxödem", "Differentialdiagnose: Depression.", 213)
L("Eine Struma ist ein ___ (vergrößerte Schilddrüse).", ["Kropf"], "Stadium I tastbar, II sichtbar, III mit mechanischen Komplikationen.", 211)
S("Welche Therapie gibt es bei Hyperthyreose?", ["Radiojodtherapie mit Jod-131", "Medikamente bis zur Euthyreose", "Jodmangeldiät allein", "Insulin"], [0, 1], "OP nur in Euthyreose; danach Hormonsubstitution.", 214)
S("Wie viele Erwachsene über 45 haben laut Skript bereits eine Schilddrüsenerkrankung?", ["Jede/r 2.", "Jede/r 10.", "Jede/r 4.", "Fast niemand"], [0], "Jede/r 4. hat Knoten.", 209)
S("Welche Hormone bildet das Nebennierenmark?", ["Katecholamine (Adrenalin, Noradrenalin)", "Aldosteron", "Cortisol", "Insulin"], [0], "Rinde: Aldosteron, Glukokortikoide, Androgene.", 215)
L("Die Zona glomerulosa der Nebennierenrinde bildet ___, die Zona fasciculata vorwiegend ___.", ["Aldosteron (Mineralokortikoide)", "Glukokortikoide"], "Zona reticularis: Androgene.", 215)

# ---------------------------------------------------------------- 8 Hämatologie
K("8")
S("Wie verteilt sich das Blut auf feste Bestandteile und Plasma?", ["45 % feste Bestandteile, 55 % Plasma", "55 % feste Bestandteile, 45 % Plasma", "10 % / 90 %", "50 % / 50 %"], [0], "", 216)
L("Erythrozyten dienen dem ___, Leukozyten der ___, Thrombozyten der ___.", ["Sauerstofftransport", "Abwehr", "Gerinnung"], "", 216)
S("Wofür steht der Begriff Leukozyten im Alltag?", ["Weiße Blutkörperchen", "Rote Blutkörperchen", "Blutplättchen", "Blutplasma"], [0], "Im Test ist Fachbegriff oder Alltagswort meist egal.", 216)
S("Was ist eine Anämie?", ["Mangel an roten Blutkörperchen", "Zu viele weiße Blutkörperchen", "Gerinnungsstörung", "Zu viele Blutplättchen"], [0], "„Blutarmut“.", 217)
S("*Welche Anämie ist in Österreich am häufigsten?", ["Eisenmangelanämie", "Vitamin-B12-Mangelanämie", "Hämolytische Anämie", "Renale Anämie"], [0], "Eisenhaushalt bei Frauen sensibler (Periode).", 217)
S("Wo erkennt man eine Blässe bei Anämie am besten?", ["An den Schleimhäuten, z. B. Innenseite des Augenlids", "An den Fußsohlen", "Am Haar", "An den Zähnen"], [0], "", 217)
F("Nenne Symptome einer Eisenmangelanämie.", "Kurzatmigkeit, Müdigkeit/Leistungsknick, Haarausfall, brüchige Nägel, eingerissene Mundwinkel, Kälteempfindlichkeit", "", 219)
F("Nenne Ursachen von Anämien.", "Chronische Blutverluste, Eisenmangel, Vitaminmangel (B12, Folsäure), Hämolyse, Nierenerkrankungen, Knochenmarksstörungen", "Therapie: Ursache suchen und behandeln.", 218)
S("Warum wird in der Schwangerschaft oft Folsäure ergänzt?", ["Sie ist für den Zellaufbau wichtig und wird vom Fötus viel gebraucht", "Sie verhindert Übelkeit", "Sie senkt den Blutdruck", "Sie ersetzt Eisen"], [0], "", 218)
S("Was ist eine Leukämie?", ["Bösartige Erkrankung blutbildender Zellen mit zu vielen (meist funktionslosen) weißen Blutkörperchen", "Mangel an weißen Blutkörperchen", "Gerinnungsstörung", "Eisenmangel"], [0],
  "Knochenmark bildet zu wenig rote Blutkörperchen → Anämie.", 220)
L("Fieber, Nachtschweiß und Gewichtsverlust bezeichnet man als ___.", ["B-Symptomatik"], "Typisch bei Leukämien und Lymphomen.", 220)
L("Hepatosplenomegalie ist die Vergrößerung von ___ und ___.", ["Leber", "Milz"], "", 220)
F("*Nenne die vier Leukämie-Varianten und was sie bedeuten.", "AML = akut & Knochenmark (myeloisch); CML = chronisch & Knochenmark; ALL = akut & lymphatisches System; CLL = chronisch & lymphatisches System",
  "Im Skript als Prüfungsfrage markiert.", 221)
S("*Was bedeutet CLL?", ["Chronisch lymphatische Leukämie – vom lymphatischen System ausgehend", "Chronisch myeloische Leukämie – vom Knochenmark ausgehend",
  "Akute lymphatische Leukämie", "Akute myeloische Leukämie"], [0], "Myeloisch = vom Knochenmark; lymphatisch = vom lymphatischen System.", 221)
S("*Was unterscheidet akute von chronischen Leukämien?", ["Akut: rasche Proliferation, akutes Krankheitsbild; chronisch: schleichender Beginn", "Akut: schleichender Beginn; chronisch: rasch",
  "Akut betrifft nur Kinder", "Chronisch ist immer gutartig"], [0], "", 221)
S("Was ist das Leitsymptom eines Lymphoms?", ["Schmerzlose, nicht verschiebbare Lymphknotenschwellung", "Schmerzhafte, verschiebbare Lymphknotenschwellung", "Bluthusten", "Gelbsucht"], [0],
  "Entzündete Lymphknoten sind schmerzhaft und verschiebbar.", 222)
S("Was ist die Hämophilie?", ["Bluterkrankheit (verminderte Gerinnung)", "Thromboseneigung", "Blutarmut", "Blutkrebs"], [0], "", 223)
F("Nenne gerinnungsverändernde Medikamente.", "Thrombozytenaggregationshemmer (ASS), Antikoagulantien (Phenprocoumon, NOAK/DOAK), Heparin („Thrombosespritzen“)", "", 223)

# ---------------------------------------------------------------- 9 Infektiologie & Allergien
K("9")
F("Nenne Maßnahmen zur Prophylaxe von Infektionskrankheiten.", "Händehygiene, Wunden desinfizieren, Kontakt mit Körperflüssigkeiten meiden (Handschuhe, Kondom), Impfungen, gesunder Lebensstil", "", 226)
S("*Was ist der Unterschied zwischen aktiver und passiver Immunisierung?", ["Aktiv: Erregerteile werden gegeben, der Körper bildet selbst Antikörper; passiv: Antikörper werden gegeben",
  "Aktiv: Antikörper werden gegeben; passiv: Erregerteile werden gegeben", "Es gibt keinen Unterschied", "Passiv wirkt lebenslang"], [0], "", 227)
L("Eine Auffrischungsimpfung heißt auch ___.", ["Booster"], "Nach der Grundimmunisierung.", 227)
S("Was ist der Unterschied zwischen Impfreaktion und Impfkomplikation?", ["Reaktion: z. B. Rötung an der Einstichstelle; Komplikation: schwerer Zwischenfall wie Eiweißschock", "Beides ist gleich",
  "Reaktion ist gefährlicher", "Komplikation tritt immer auf"], [0], "", 227)
S("Welche Krankheit gilt durch Impfung als ausgerottet?", ["Pocken", "Masern", "Mumps", "Keuchhusten"], [0], "Tabelle selbst muss man laut Mitschrift nicht lernen.", 228)
S("*Ab welcher Temperatur spricht man (rektal gemessen) von Fieber?", ["> 38,0 °C", "> 37,0 °C", "> 37,5 °C", "> 39,0 °C"], [0], "Axillär > 37,5 °C.", 231)
L("Fieber entsteht durch Verstellung des Temperatur-Sollwertes im ___.", ["Hypothalamus"], "Zytokinregulierte Erhöhung der Körpertemperatur.", 231)
S("Was ist KEIN Fieber, sondern eine Hyperthermie?", ["Überhitzung durch Sonne oder zu warme Kleidung", "Erhöhte Temperatur bei ausgiebiger Bewegung", "Temperaturanstieg bei Pneumonie", "Temperaturanstieg bei Mumps"], [0, 1],
  "Häufigste Fieberursache: Infektionskrankheiten.", 232)
F("*Nenne die fünf Kardinalsymptome der Entzündung.", "Dolor (Schmerz), Calor (Überwärmung), Rubor (Rötung), Tumor (Schwellung), Functio laesa (eingeschränkte Funktion)", "", 233)
L("Rubor bedeutet ___, Calor bedeutet ___.", ["Rötung", "Überwärmung"], "", 233)
S("*Was bedeutet der Infektionsweg „parenteral“?", ["Direkt ins Blut", "Über den Darm", "Über die Haut", "Über die Atemwege"], [0], "Wichtig für Prüfung!", 234)
S("*Was bedeutet „permukös“?", ["Über die Schleimhäute", "Über die Haut", "Über das Blut", "Über den Darm"], [0], "Perkutan = über die Haut.", 234)
L("*Fäkal-oral bedeutet: Erreger aus ___ gelangen durch den ___ in den Körper, z. B. über verunreinigtes Trinkwasser.", ["Darm/Fäkalien", "Mund"], "Wichtig für Prüfung!", 234)
F("*Nenne Infektionswege.", "Enteral, fäkal-oral, parenteral, perkutan, permukös, Inhalation, urogenital, genital, intrauterin", "Im Skript als wichtig für die Prüfung markiert.", 234)
S("Was ist die häufigste registrierte Erkrankung weltweit?", ["Die ambulant erworbene Pneumonie", "Malaria", "AIDS", "Tuberkulose"], [0], "", 235)
S("Ab welchem Alter wird die Pneumokokkenimpfung für Erwachsene empfohlen?", ["Ab dem 51. Lebensjahr", "Ab 18", "Ab 65", "Ab 80"], [0], "Auch für Raucher und Risikopersonen jeden Alters.", 236)
S("*Was sind die häufigsten nosokomialen Infektionen?", ["Harnwegsinfektionen", "Pneumonien", "Wundinfektionen", "Magen-Darm-Infekte"], [0], "Frauen : Männer = 4 : 1.", 237)
L("Eine Entzündung des Nierenbeckens heißt ___ (obere HWI), eine Entzündung der Harnblase ___ (untere HWI).", ["Pyelonephritis", "Zystitis"], "Pyelonephritis: Fieber, Flankenschmerz.", 238)
F("Nenne Prophylaxe-Maßnahmen gegen Harnwegsinfekte.", "Viel trinken, Unterkühlung vermeiden, Blase vollständig entleeren, keine übertriebene Genitalhygiene, Miktion nach Geschlechtsverkehr, Obstipation behandeln", "Cranberries: umstritten.", 239)
S("Welche Komplikation ist bei Mumps typisch?", ["Hodenentzündung mit Sterilitätsgefahr", "Rötelnembryopathie", "Koplik'sche Flecken", "Erythema migrans"], [0], "Mumps = schmerzhafte Entzündung der Speicheldrüsen.", 241)
S("Woran erkennt man Masern typischerweise?", ["Weiße Flecken an der Wangenschleimhaut (Koplik'sche Flecken)", "Grobfleckiger Hautausschlag", "Wanderröte", "Schwellung der Ohrspeicheldrüse"], [0, 1],
  "Komplikationen: Lungenentzündung, Mittelohr-, Gehirnentzündung.", 242)
S("*Warum sind Röteln für Schwangere gefährlich?", ["Rötelnembryopathie: Schäden an Augen, Ohren, Herz des Kindes", "Sie lösen Diabetes aus", "Sie verursachen Hodenentzündung", "Sie sind nicht gefährlich"], [0], "", 243)
S("Was ist typisch für Windpocken (Varizellen)?", ["Bläschen in allen Stadien nebeneinander", "Gehört zu den Herpesviren", "Bakterielle Erkrankung", "Keine Ansteckungsgefahr"], [0, 1], "", 244)
S("Wer ist bei Influenza besonders gefährdet?", ["Menschen ab 65 Jahren", "Jugendliche", "Sportler", "Niemand"], [0], "500–1.000 Todesfälle/Jahr in Österreich.", 245)
S("*Welche Aussagen zur Borreliose stimmen?", ["Bakterielle Erkrankung, Therapie mit Antibiotika", "Erstes Zeichen: Erythema migrans (Wanderröte)", "Es gibt eine Impfung dagegen", "Wird durch Mücken übertragen"], [0, 1],
  "Übertragung durch Zecken; Stadien: Wanderröte → Neuroborreliose → Lyme-Arthritis.", 246)
L("Eine Allergie ist eine ___ Reaktion des Immunsystems auf eigentlich harmlose Stoffe; Allergene sind meist ___.", ["überschießende", "Eiweiße (Proteine)"], "", 247)
F("Nenne Arten von Allergenen mit Beispielen.", "Inhalation (Pollen, Hausstaub, Tierhaare), Kontakt (Nickel, Duftstoffe), Nahrungs-/Arzneimittel (Milch, Eier, Fisch, Antibiotika), Insektengift (Biene, Wespe)", "", 247)
F("Nenne häufige klinische Bilder bei Allergien.", "Allergische Rhinitis/Konjunktivitis, Neurodermitis, allergisches Asthma, Nahrungsmittelallergie, Urtikaria (Nesselsucht)", "", 248)


# ---------------------------------------------------------------- Ausgabe + Prüfung
fehler = []
nrn = [k[0] for k in KAPITEL]
for i, f in enumerate(fragen, 1):
    f["id"] = f"kim-{i:03d}"
    if f["typ"] == "mc":
        if len(f["optionen"]) < 3 or not f["richtig"] or max(f["richtig"]) >= len(f["optionen"]):
            fehler.append(f"{f['id']}: mc ungültig")
    if not 2 <= f["seite"] <= 249:
        fehler.append(f"{f['id']}: Seite {f['seite']}")
fehler += [f"doppelt: {t}" for t, n in collections.Counter(f["frage"] for f in fragen).items() if n > 1]
fehler += [f"Kapitel ohne Frage: {k}" for k in nrn if not any(f["kapitel"] == k for f in fragen)]
if fehler:
    print("\n".join(fehler)); sys.exit(1)

reihenfolge = ["id", "kapitel", "typ", "frage", "optionen", "richtig", "luecken", "antwortKurz", "erklaerung", "seite", "prio"]
ziel.mkdir(exist_ok=True)
(ziel / "fragen.json").write_text("[\n" + ",\n".join(json.dumps({k: f[k] for k in reihenfolge if k in f}, ensure_ascii=False) for f in fragen) + "\n]\n", encoding="utf-8")
meta = {"id": "kim", "titel": "Klinische Innere Medizin", "kurz": "KIM", "datum": "2026-11-30", "aktiv": True,
        "form": "elektronisch: Ankreuzen (1–2 richtig), Lückentexte, Freitext in Stichworten",
        "kapitel": [{"nr": n, "titel": t} for n, t, _ in KAPITEL],
        "gruppen": [{"nr": n, "titel": t, "thema": th, "praefix": [n]} for n, t, th in KAPITEL]}
(ziel / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

c = collections.Counter
print(len(fragen), "Fragen")
print("Typen:", dict(c(f["typ"] for f in fragen)), "| mc mit 2 richtig:", sum(1 for f in fragen if f["typ"] == "mc" and len(f["richtig"]) > 1))
print("Kapitel:", dict(c(f["kapitel"] for f in fragen)), "| prio hoch:", sum(f["prio"] == "hoch" for f in fragen))
