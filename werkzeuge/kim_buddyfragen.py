"""KIM-Buddyfragen 1:1 aus quellen/KIM_Fragenkatalog.md (Fragenkatalog_Innere Medizin.docx, F) und
quellen/KIM_Buddy.md (KIM.pdf, B) -> pruefungen/kim-buddy/.

Antworten gegen das KIM-Skript geprüft (seite = Skriptseite, 0 = nicht im Skript). Wo die Buddy-Antwort falsch
oder schwach war, ist die Antwort korrigiert und die Abweichung steht im Hinweis.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
ziel = root / "pruefungen/kim-buddy"
OK = "Buddy-Antwort passt zum Skript."

# (Quelle, Kapitel, Seite, Typ, Frage, Optionen/Lücken, richtig, Antwort, Hinweis)
FRAGEN = [
    ("F", "5", 168, "mc", "Welche der folgenden ist die häufigste Lebererkrankung in Mitteleuropa?",
     ["Fettleber", "Leberzirrhose", "Leberzellkarzinom", "Hepatitis B"], [0], "Fettleber", OK),
    ("F", "6", 184, "mc", "Welche der folgenden Erkrankungen ist die häufigste Ursache einer chronischen Niereninsuffizienz?",
     ["Zystennieren", "Diabetes mellitus", "Schmerzmittelmissbrauch", "Nephritis"], [1], "Diabetes mellitus", OK),
    ("F", "1", 22, "lueckentext", "Das bei der physikalischen Gesunden- und Krankenuntersuchung durchgeführte Abhorchen nennt man im Fachausdruck ___.",
     ["Auskultation"], None, "Auskultation", OK),
    ("F", "9", 242, "lueckentext", "Ein grobfleckiger Ausschlag über den ganzen Körper inkl. Wangenschleimhaut ist typisch für die „Kinderkrankheit“ ___.",
     ["Masern"], None, "Masern", OK),
    ("F", "1", 29, "lueckentext", "Wenn das Vorliegen einer bestimmten Erkrankung eine eigentlich geplante Behandlung einer anderen unmöglich macht, nennt man das eine ___.",
     ["(absolute) Kontraindikation"], None, "(absolute) Kontraindikation", OK),
    ("F", "4", 111, "lueckentext", "Chronischer Husten, Auswurf, fortschreitende Atemnot und akute Verschlechterung bei Infekten sind die Leitsymptome einer ___.",
     ["COPD"], None, "COPD", OK),
    ("F", "1", 23, "kurz", "Nennen Sie 4 verschiedene menschliche Materialien, die typischerweise im Labor untersucht werden.",
     None, None, "Blut, Urin, Stuhl, Sputum (ausgehustete Absonderung der Atemwegsschleimhaut), Liquor, Material von Punktionen und Abstrichen.", OK),
    ("F", "1", 32, "mc", "Frau X hatte einen Herzinfarkt, nun geht sie 2×/Woche in ein Zentrum, um zu trainieren. Die Krankenversicherung hat 90 Einheiten bewilligt. Um welche Phase der Rehabilitation handelt es sich?",
     ["I", "II", "III", "IV"], [2], "Phase III – ambulante Rehabilitation", OK),
    ("F", "1", 31, "mc", "Bei einem 54-Jährigen finden sich bei einer Blutabnahme erhöhte Blutzuckerwerte. Es wird eine Ernährungsoptimierung empfohlen. Dieses Vorgehen entspricht einer …",
     ["Rehabilitation", "Primärprävention", "Sekundärprävention", "Tertiärprävention"], [2], "Sekundärprävention",
     OK + " Sekundärprävention = Fortschreiten eines Frühstadiums verhindern."),
    ("F", "7", 196, "mc", "Nach einer Vermessung bei einer Diätologin wird die Diagnose Übergewicht gestellt. Für welchen errechneten Body-Mass-Index trifft diese Diagnose zu?",
     ["27", "43", "33", "38", "23", "18"], [0], "27", OK + " Übergewicht = BMI 25–30."),
    ("F", "8", 217, "lueckentext", "Die in Österreich häufigste Anämie ist die ___.",
     ["Eisenmangelanämie"], None, "Eisenmangelanämie", OK),
    ("F", "2", 56, "kurz", "Nennen Sie 3 Therapieoptionen bei Vorliegen einer Herzinsuffizienz.",
     None, None, "Trainingstherapie, Lifestyle-Änderung, Medikamente, Interventionen, Devices.", OK),
    ("F", "2", 35, "lueckentext", "Ein Sinusrhythmus mit einer Frequenz von 49/min wird kategorisiert als ___, ein anderer Rhythmus mit 121/min als ___.",
     ["Bradykardie", "Tachykardie"], None, "49/min = Bradykardie, 121/min = Tachykardie",
     OK + " Grenzen laut Skript: unter 55/min Bradykardie, über 100/min Tachykardie."),
    ("F", "5", 130, "mc", "Welche der folgenden ist die häufigste Ursache für die Entstehung einer Gastritis?",
     ["Bakterielle Infektion", "Autoimmunprozesse", "Psychische Belastung", "Chemisch-toxisch"], [0], "Bakterielle Infektion (Helicobacter pylori, Typ-B-Gastritis)", OK),
    ("F", "9", 227, "lueckentext", "Wenn man im Rahmen einer Infektion Antikörper verabreicht, nennt man das eine ___ Immunisierung.",
     ["passive"], None, "passive Immunisierung", OK),
    ("F", "2", 41, "kurz", "Welche Symptome können ein Hinweis auf einen deutlich erhöhten Blutdruck sein? Nennen Sie 2.",
     None, None, "Schwindel, Kopfschmerzen, Nasenbluten, Nervosität, Kribbeln in den Fingern, Atemnot, Angina pectoris (oft aber keine Symptome!).",
     "Die Buddy-Antwort (Atemnot, Angina pectoris) stimmt; das Skript nennt zuerst Schwindel, Kopfschmerzen und Nasenbluten."),
    ("F", "9", 247, "mc", "Bei Heuschnupfen kommt es oft zu einer IgE-vermittelten überschießenden Immunantwort. Welchem allergischen Reaktionstyp entspricht dies?",
     ["I – Inhalationsallergene", "II – Kontaktallergene", "III – Nahrungsmittel- oder Arzneimittelallergene", "IV – Insektenstich- und Injektionsallergene"], [0],
     "I – Inhalationsallergene (Gräserpollen)", OK),
    ("F", "5", 154, "lueckentext", "Die 2 häufigsten chronisch entzündlichen Darmerkrankungen (CED) sind ___ und ___, wobei ___ alle Darmabschnitte befallen kann.",
     ["Colitis ulcerosa", "Morbus Crohn", "Morbus Crohn"], None, "Colitis ulcerosa und Morbus Crohn; Morbus Crohn kann alle Darmabschnitte (Mund bis After) befallen.", OK),
    ("F", "7", 213, "mc", "Frau X schildert in der Anamnese Müdigkeit, Gewichtszunahme und kühle Haut. Zu welcher Auslenkung der Schilddrüse passt das?",
     ["Krebsentartung", "Überfunktion", "Normalfunktion", "Unterfunktion"], [3], "Unterfunktion (Hypothyreose)", OK),
    ("F", "7", 190, "kurz", "Wie kann man einen Diabetes mellitus im Blut diagnostizieren? Nennen Sie 2 Möglichkeiten.",
     None, None, "Nüchternblutzucker: wiederholt über 126 mg/dl.\noGTT (oraler Glukosetoleranztest): Blutzucker nach 2 Stunden über 200 mg/dl.\nHbA1c (Langzeitzucker): ab 6,5 %.",
     OK + " Das HbA1c ist laut Skript eine dritte Möglichkeit."),
    ("F", "2", 48, "mc", "Welche der folgenden Aussagen zur KHK (koronaren Herzkrankheit) ist richtig?",
     ["Wird überwiegend mit Bypassoperationen behandelt", "Äußert sich bei Frauen und Männern in gleicher Weise", "Angina pectoris ist bei KHK selten",
      "Entspricht der Arteriosklerose der Herzkranzgefäße", "Betrifft Frauen und Männer in gleicher Weise"], [3],
     "Entspricht der Arteriosklerose der Herzkranzgefäße",
     "Korrigiert: Im Buddy-Bogen ist auch „überwiegend mit Bypassoperationen behandelt“ markiert. Laut Skript (S. 53) wird vor allem per Herzkatheter gedehnt/gestentet, dazu Lyse und Medikamente – Bypass ist nicht der Regelfall."),
    ("F", "2", 62, "mc", "Warum werden bewusstlose Menschen mit normaler Atmung in die stabile Seitenlage gebracht?",
     ["Weil keine Herzdruckmassage notwendig ist, solange Herz und Atmung selbstständig funktionieren",
      "Damit Erbrochenes, Speichel und andere Flüssigkeiten austreten können und nicht die Atemwege blockieren"], [1],
     "Damit die Atemwege offen bleiben (Erbrochenes, Speichel können abfließen)", OK),
    ("F", "8", 222, "mc", "Welches der folgenden Symptome gehört NICHT zur sogenannten „B-Symptomatik“?",
     ["Fieber", "Nächtliche Schweißausbrüche", "Gewichtsabnahme", "Blutung"], [3], "Blutung", OK + " B-Symptome = Fieber, Nachtschweiß, Gewichtsverlust."),
    ("F", "7", 202, "kurz", "12–15 % des Energiebedarfs werden aus Eiweiß gewonnen. Was sind die 2 hauptsächlichen Funktionen von Eiweiß/Proteinen im Körper?",
     None, None, "Baustoff/Struktur – Körperzellen (z. B. Muskeln) bestehen großteils aus Eiweiß.\nTransport lebenswichtiger Stoffe.",
     "Passt; das Skript sagt allgemein „Struktur der Körperzellen“ statt „Muskeln und Knochen“."),
    ("F", "5", 140, "mc", "Wie nennt man die mangelhafte Aufnahme von Substraten aus dem bereits vorverdauten Speisebrei?",
     ["Malassimilation", "Malabsorption", "Intoleranz", "Reizdarmsyndrom"], [1], "Malabsorption", OK),
    ("F", "3", 89, "kurz", "Nennen Sie 4 Symptome, die auf einen akuten arteriellen Gefäßverschluss in einem Bein hinweisen.",
     None, None, "Die 6 P: Pain (plötzlicher heftiger Schmerz), Paleness (Blässe), Paraesthesia (Gefühlsstörung), Paralysis (Lähmung), Pulselessness (kein Puls), Prostration (Schock).",
     "Korrigiert: Die Buddy-Antwort (trockene Haut, Verhornung, langsam wachsende Nägel, Haarverlust …) sind die Anzeichen der chronischen pAVK (Skript S. 84). Für den AKUTEN Verschluss gelten die 6 P (S. 89) – so steht es auch im zweiten Buddy-Bogen."),
    ("F", "5", 138, "kurz", "Nennen Sie 4 Ursachen/Auslöser, die zu einem Magenkarzinom führen können.",
     None, None, "Nitrosamine (Pökeln), vitaminarme Ernährung, Alkohol, Nikotin, chronische Gastritis, chronische Ulcera, Magenpolypen, Zustand nach Teilresektion.", OK),
    ("F", "3", 101, "mc", "Welche der genannten ist die häufigste Ursache für eine Lungenembolie?",
     ["Kniestrümpfe", "Lungenentzündung", "Arteriosklerose der Becken-Bein-Arterien", "Blutverdünnende Medikamente", "Tiefe Beinvenenthrombose"], [4],
     "Tiefe Beinvenenthrombose", OK),
    ("F", "2", 39, "mc", "Welcher der folgenden Blutdruckwerte (in mmHg) ist normal?",
     ["130/80", "115/90", "95/45", "160/85"], [0], "130/80",
     OK + " Genau genommen liegt 130/80 laut Skript-Tabelle schon an der Grenze zu „hoch normal“, ist aber der einzige Wert ohne Hypertonie (115/90: diastolisch zu hoch) oder Hypotonie."),
    ("F", "2", 70, "mc", "Im Rahmen einer kardiopulmonalen Reanimation wird eine Defibrillation durchgeführt. Was soll unmittelbar danach geschehen?",
     ["EKG schreiben", "CPR weiterführen", "Wechsel auf biphasischen Defibrillator", "Puls tasten"], [1], "Sofort 2 Minuten CPR weiterführen", OK),
    ("F", "2", 78, "kurz", "Nennen Sie einen psychischen und einen körperlichen Effekt von Nikotin.",
     None, None, "Psychisch: erhöht kurzfristig die Konzentration, macht abhängig, setzt Botenstoffe frei, vermindert vorübergehend Stress, verringert Hunger.\nKörperlich: Adrenalinausschüttung, Gefäßverengung, Anstieg von Blutdruck, Herz- und Atemfrequenz, Stoffwechselaktivität steigt.", OK),
    ("F", "5", 153, "kurz", "Die Darmspiegelung wird allen ab 50 Jahren empfohlen; war sie unauffällig, die nächste nach (5–)10 Jahren. Worauf beruht diese Empfehlung?",
     None, None, "Darmkrebs entsteht langsam über Vorstufen: gesunde Schleimhaut → Wucherung → kleiner Polyp → großer Polyp → Krebs. Das dauert etwa 7–10 Jahre; Polypen lassen sich bei der Spiegelung gleich entfernen.", OK),

    ("B", "1", 25, "kurz", "Nennen Sie 3 Funktionsuntersuchungen im diagnostischen Vorgehen.",
     None, None, "EKG (Herz), Spirometrie (Lungenfunktion), Ergometrie (Belastungs-EKG), Spiroergometrie, Nervenleitgeschwindigkeit, EEG (Gehirnströme).", OK),
    ("B", "1", 31, "kurz", "Was versteht man unter Primärprävention?",
     None, None, "Maßnahmen zur Erhaltung und Förderung der Gesundheit sowie zur Vermeidung von Risikofaktoren (z. B. nicht rauchen, gesunde Ernährung).", OK),
    ("B", "2", 38, "kurz", "Was versteht man unter einem erhöhten Blutdruck? Geben Sie einen Beispielwert an.",
     None, None, "Das Blut wird mit dauerhaft zu hohem Druck in die Arterien gepumpt – schädigt die Gefäße.\nGrenzwert in der Ordination: ab 140/90 mmHg (Selbstmessung ab 135/85).", OK),
    ("B", "2", 47, "kurz", "Nennen Sie zumindest 4 Folgeerkrankungen der Arteriosklerose.",
     None, None, "Koronare Herzkrankheit, Herzinfarkt, Schlaganfall, pAVK (Durchblutungsstörung der Beine), Aortenaneurysma, Niereninsuffizienz, Erblindung.", OK),
    ("B", "2", 0, "mc", "Über welche Gefäße fließt das sauerstoffarme Blut zurück zum Herzen?",
     ["Lungenvenen", "Hohlvenen", "Lungenarterien", "Aorta"], [1], "Hohlvenen (obere und untere Hohlvene)",
     OK + " Lungenvenen bringen sauerstoffreiches Blut zum Herzen, Lungenarterien sauerstoffarmes Blut zur Lunge, die Aorta sauerstoffreiches Blut in den Körper."),
    ("B", "2", 49, "kurz", "Nennen Sie 4 charakteristische Merkmale einer Angina pectoris.",
     None, None, "Ziehen und Brennen im Brustkorb (evtl. ausstrahlend), Atemnot, Angstgefühl, Schweißausbruch, Übelkeit; dauert Sekunden bis Minuten.", OK),
    ("B", "2", 59, "kurz", "Verkehrsunfall, finster, niemand sonst da. Unfallstelle gesichert, Hilfe gerufen. Ein Opfer ist wach, das andere nicht. Wie lange haben Sie als Profi zur Untersuchung Zeit, um zu entscheiden, ob Sie reanimieren müssen?",
     None, None, "Nur wenige Sekunden (Bewusstsein, Atmung, Puls jeweils wenige Sekunden prüfen) – jede Sekunde ohne Sauerstoff schädigt das Gehirn.", OK),
    ("B", "2", 0, "mc", "Welche Aussage zur Folge eines Herz-Kreislauf-Stillstandes ist am ehesten zutreffend?",
     ["Zuerst kommt es zur Schnappatmung, danach verliert man das Bewusstsein", "Nach ca. 5 Minuten ist mit hypoxischen Hirnschäden zu rechnen",
      "Herzdruckmassage sofort im Verhältnis 15:2 beginnen", "Die Pulskontrolle ist rasch und einfach durchzuführen"], [1],
     "Nach ca. 5 Minuten ist mit hypoxischen Hirnschäden zu rechnen",
     OK + " Die anderen sind falsch: Verhältnis 30:2 (S. 58), Puls ist auch für Profis oft schwer zu tasten (S. 63). Die 5 Minuten stehen nicht ausdrücklich im Skript."),
    ("B", "3", 83, "mc", "Welche Aussage zur pAVK ist FALSCH?",
     ["Sie betrifft am ehesten die Becken- und Beinarterien", "Klinisches Hauptsymptom ist die Angina pectoris",
      "Männer sind häufiger betroffen als Frauen", "Therapie der Wahl in Stadium I–II ist das Gehtraining"], [1],
     "Falsch: „Hauptsymptom ist die Angina pectoris“ – Hauptsymptom ist die Claudicatio intermittens (Schaufensterkrankheit).", OK),
    ("B", "3", 89, "kurz", "Nennen Sie zumindest 4 Merkmale, die an einen akuten arteriellen Verschluss eines Beines denken lassen.",
     None, None, "Die 6 P: Pain (Schmerz), Paleness (Blässe), Paraesthesia (Gefühlsstörung), Paralysis (Lähmung), Pulselessness (kein Puls), Prostration (Schock).", OK),
    ("B", "3", 97, "kurz", "Welche Beschwerden haben Menschen mit Varikositas? Nennen Sie zumindest 3.",
     None, None, "Schweregefühl in den Beinen, Schwellneigung, krampfartige Wadenschmerzen (v. a. nachts), Jucken; im Spätstadium Ödeme, Hautveränderungen, offenes Bein (Ulcus cruris).", OK),
    ("B", "3", 101, "mc", "Welche der genannten ist die häufigste Ursache für eine Lungenembolie?",
     ["Blutverdünnende Medikamente", "Varikositas", "Tiefe Beinvenenthrombose", "Venenentzündungen"], [2],
     "Tiefe Beinvenenthrombose (verschleppter Bein-Becken-Thrombus)", OK),
    ("B", "4", 120, "kurz", "Warum ist die Unterscheidung zwischen ambulant erworbener und nosokomialer Lungenentzündung klinisch relevant?",
     None, None, "Ambulant erworben: Erreger außerhalb des Krankenhauses aufgenommen.\nNosokomial: ab 48 h nach Aufnahme oder bis 14 Tage nach Entlassung – meist resistente Krankenhauskeime, die auf die üblichen Antibiotika nicht ansprechen → andere Therapie; häufigste Todesursache unter den Krankenhausinfektionen (Letalität 30–50 %). Wichtigster Risikofaktor: maschinelle Beatmung.",
     "Ergänzt: Der Buddy-Bogen erklärt die Begriffe, aber nicht ganz, warum das wichtig ist – entscheidend ist die andere Antibiotika-Therapie wegen resistenter Erreger (Skript S. 120)."),
    ("B", "4", 0, "mc", "Welche der folgenden Maßnahmen wird bei der Behandlung einer Lungenentzündung üblicherweise NICHT angewandt?",
     ["Atemtherapie", "Antibiotika", "Entwässerung", "Schmerzmedikamente"], [2], "Entwässerung", OK),
    ("B", "5", 136, "mc", "Ein Patient klagt über laufende Übelkeit und Schwindel, seit gestern ist der Stuhl schwarz. Woran denken Sie?",
     ["Zöliakie", "Gastrointestinale Blutung", "Divertikulose", "Reizdarmsyndrom"], [1], "Gastrointestinale Blutung (verdautes Blut färbt den Stuhl schwarz)", OK),
    ("B", "5", 146, "kurz", "Nennen Sie 4 typische Nahrungsmittel, die bei Histaminintoleranz Beschwerden machen können.",
     None, None, "Rotwein, Sekt, Weizenbier, gereifter Käse (Emmentaler, Bergkäse, Parmesan), Salami/Schinken, Rotweinessig.", OK),
    ("B", "5", 153, "kurz", "Die Darmspiegelung wird allen ab 50 Jahren empfohlen, nach unauffälligem Befund die nächste in (5–)10 Jahren. Worauf beruht diese Empfehlung?",
     None, None, "In 7–10 Jahren entstehen zuerst Wucherungen, kleine und große Polypen, bevor daraus Krebs wird. Diese Vorstufen lassen sich bei der Spiegelung leicht entfernen.", OK),
    ("B", "5", 163, "kurz", "Nennen Sie 4 Aufgaben der gesunden Leber.",
     None, None, "Entgiftung, Speicherung von Glukose als Glykogen, Gallenproduktion, Cholesterinsynthese, Aminosäuresynthese, Hormon- und Enzymproduktion, Hilfe bei der Vitaminaufnahme.",
     "Passt bis auf „produziert Wachstumshormone“: Das Wachstumshormon kommt aus der Hirnanhangdrüse; das Skript sagt allgemein „Hormon- und Enzymproduktion“."),
    ("B", "5", 169, "mc", "Hepatitis ist eine Leberentzündung, meist durch Viren. Gegen welche Gruppen gibt es eine Impfung?",
     ["A, B", "B, C", "A, C", "B, D", "A, D"], [0], "Hepatitis A und B", OK),
    ("B", "7", 214, "kurz", "Frau X. erzählt, ihr Arzt habe gesagt, sie leide an einer latenten Hyperthyreose. An welchem Organ ist sie erkrankt?",
     None, None, "Schilddrüse (Überfunktion).", OK),
    ("B", "8", 216, "kurz", "Was ist der Hämatokrit? Geben Sie einen ungefähren Normalwert an.",
     None, None, "Anteil der festen Blutbestandteile (v. a. rote Blutkörperchen) am Blutvolumen.\nFrauen ca. 42 %, Männer ca. 46 % (Skript: feste Bestandteile ca. 45 %).", OK),
    ("B", "8", 217, "kurz", "a) Nennen Sie 3 Beschwerdebilder, die an eine Anämie denken lassen. b) Was ist in Österreich die häufigste Ursache einer Anämie?",
     None, None, "a) Blässe, Schwindel/Kreislaufschwäche, Atemnot, verminderte Leistungsfähigkeit.\nb) Eisenmangel (Eisenmangelanämie).", OK),
    ("B", "8", 222, "mc", "Welches der folgenden Symptome gehört NICHT zur B-Symptomatik?",
     ["Nachtschweiß", "Gewichtsabnahme", "Blutung", "Fieber"], [2], "Blutung", OK),
    ("B", "1", 0, "kurz", "Nennen Sie 4 ergotherapeutische Therapiemaßnahmen bei Osteoarthritis.",
     None, None, "Selbstständige Bewegungsübungen nach Anleitung, Feinmotorik-Übungen für die Finger, Beweglichkeitsübungen, Gelenkschutz-Schulung (schonende Bewegung), Hilfsmittel (Stöcke, Krücken, Einlagen).",
     "Nicht im Skript prüfbar – die Rheumatologie-Folien wurden durch Geriatrie ersetzt. Die Buddy-Antwort ist fachlich plausibel."),
    ("B", "9", 226, "mc", "Welche der folgenden Maßnahmen ist zur Prophylaxe von Infektionskrankheiten am wirkungsvollsten?",
     ["Krankenhauskleidung", "Gesichtsmaske", "Händedesinfektion", "Nasenabstrich"], [2], "Händedesinfektion", OK),
    ("B", "9", 246, "mc", "Für welche durch Zecken übertragbare Erkrankung gibt es eine Prophylaxe (Impfung)?",
     ["Lyme-Borreliose", "Frühsommer-Meningoenzephalitis (FSME)", "Erythema migrans", "Varizellen"], [1], "FSME",
     OK + " Gegen Borreliose (Erythema migrans = ihr 1. Stadium) gibt es keine Impfung."),
]

KAPITEL = json.loads((root / "pruefungen/kim/meta.json").read_text(encoding="utf-8"))["kapitel"]
BOGEN = {"F": "Fragenkatalog", "B": "KIM-Bogen"}

fragen = []
for i, (q, k, seite, typ, frage, extra, richtig, antwort, hinweis) in enumerate(FRAGEN, 1):
    f = {"id": f"kimbud-{i:03d}", "kapitel": k, "typ": typ, "frage": frage}
    if typ == "mc":
        f["optionen"], f["richtig"] = extra, richtig
    if typ == "lueckentext":
        f["luecken"] = extra
    f.update({"antwortKurz": antwort, "erklaerung": f"{hinweis} (Aus dem {BOGEN[q]}.)", "seite": seite, "prio": "hoch"})
    fragen.append(f)

assert {f["kapitel"] for f in fragen} <= {k["nr"] for k in KAPITEL}
ziel.mkdir(exist_ok=True)
(ziel / "fragen.json").write_text("[\n" + ",\n".join(json.dumps(f, ensure_ascii=False) for f in fragen) + "\n]\n", encoding="utf-8")
meta = {"id": "kim-buddy", "titel": "Klinische Innere Medizin – Buddyfragen", "kurz": "KIM-BUDDY", "datum": "2026-11-30", "aktiv": True,
        "form": "Fragen aus den Buddy-Bögen (Fragenkatalog + KIM-Bogen), Antworten mit dem Skript geprüft",
        "kapitel": KAPITEL, "gruppen": [{"nr": k["nr"], "titel": k["titel"], "thema": "", "praefix": [k["nr"]]} for k in KAPITEL]}
(ziel / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(len(fragen), "KIM-Buddyfragen;", sum(OK not in f["erklaerung"] for f in fragen), "korrigiert/ergänzt")
