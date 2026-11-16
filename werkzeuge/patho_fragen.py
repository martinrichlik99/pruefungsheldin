"""Erzeugt pruefungen/patho/fragen.json + meta.json aus quellen/Pathologie.md (neu erstellte Fragen, nur Single/Multiple Choice).

S(frage, optionen, richtig_indizes, erklaerung, seite) -> typ "mc" (App mischt die Reihenfolge). * vor der Frage = prio "hoch".
"""
import json, sys, collections
from pathlib import Path

ziel = Path(__file__).resolve().parent.parent / "pruefungen/patho"

KAPITEL = [
    ("1", "Grundlagen", "Begriffe, Sonderfach, Arbeitsbereiche, Molekularpathologie"),
    ("2", "Tod & Obduktion", "Todesbegriffe, Todeszeichen, Totenbeschau, Obduktionsarten"),
    ("3", "Krankheitslehre", "Verlauf, Ätiologie, Pathogenese, Ursachen, Ausgänge"),
    ("4", "Zellpathologie", "Gewebearten, Anpassung, Zellschädigung, Nekrose"),
    ("5", "Entzündung & Wundheilung", "Kardinalsymptome, Exsudate, Abszess, Wundheilung"),
    ("6", "Tumorpathologie", "Dignität, Dysplasie, Grading, Nomenklatur, Metastasen, TNM"),
    ("7", "Kreislaufstörungen", "Ödem, Thrombose, Embolie, Schock, Blutung, Infarkt"),
    ("8", "Stoffwechsel & Gefäße", "Arteriosklerose, Diabetes, Hypertonie, Ikterus, Ileus"),
]

fragen, kap = [], None


def K(nr):
    global kap
    kap = nr


def S(frage, optionen, richtig, erkl, seite):
    fragen.append({"kapitel": kap, "typ": "mc", "frage": frage.lstrip("*"), "optionen": optionen, "richtig": richtig,
                   "antwortKurz": ", ".join(optionen[i] for i in richtig), "erklaerung": erkl, "seite": seite,
                   "prio": "hoch" if frage.startswith("*") else "normal"})


# ---------------------------------------------------------------- 1 Grundlagen
K("1")
S("Was bedeutet „Pathologie“?", ["Lehre vom Wesen der Krankheiten", "Lehre vom gesunden Körperbau", "Lehre von den Arzneimitteln", "Lehre vom Tod"], [0],
  "Pathos = Krankheit, Logie = Lehre.", 19)
S("Wie definiert die WHO Gesundheit?", ["Zustand völligen körperlichen, seelischen und sozialen Wohlbefindens", "Abwesenheit von Krankheit", "Normale Laborwerte", "Körperliche Leistungsfähigkeit"], [0], "", 21)
S("Zu welcher Gruppe medizinischer Sonderfächer gehört die Pathologie?", ["Diagnostische Fächer", "Konservative Fächer", "Chirurgische Fächer", "Theoretische Fächer"], [0],
  "Gemeinsam mit Radiologie, Labormedizin, Nuklearmedizin.", 24)
S("Welche Fächer gehören wie die Pathologie zu den diagnostischen Sonderfächern?", ["Radiologie", "Labormedizin", "Psychiatrie", "Urologie"], [0, 1], "", 24)
S("Welche zwei Arten von Diagnostik betreibt die Pathologie?", ["Intravitale Diagnostik", "Postmortale Diagnostik", "Pränatale Psychotherapie", "Chirurgische Therapie"], [0, 1],
  "Intravital = am Lebenden (z. B. Biopsie), postmortal = nach dem Tod (Obduktion).", 25)
S("*Welche gehören zu den Arbeitsbereichen der Pathologie?", ["Histologie", "Zytologie", "Radiotherapie", "Anästhesie"], [0, 1],
  "Arbeitsbereiche: Histologie, Zytologie, Bakteriologie, Molekularpathologie, Prosektur (Obduktion).", 27)
S("*Welche gehören ebenfalls zu den Arbeitsbereichen der Pathologie?", ["Bakteriologie/Mikrobiologie", "Molekularpathologie", "Physiotherapie", "Kardiochirurgie"], [0, 1], "Im Skript als Prüfungsfrage markiert.", 27)
S("Was untersucht die Histologie?", ["Gewebe feingeweblich mit dem Mikroskop (Biopsien, OP-Präparate)", "Einzelne Zellen aus Abstrichen", "DNA und RNA", "Bakterienkulturen"], [0],
  "Die Histologie „gibt der Erkrankung ihren Namen“.", 28)
S("Was untersucht die Zytologie?", ["Zellmaterial aus Abstrichen und punktierten Flüssigkeiten", "Ganze Organe bei der Obduktion", "Knochen im Röntgen", "Hormonspiegel"], [0],
  "Einsatz zum Screening und zur Frage: bösartig?", 29)
S("Welche Aufgabe hat die Bakteriologie/Mikrobiologie?", ["Nachweis und Klassifizierung belebter Krankheitserreger", "Prüfung von Medikamentenresistenzen", "Bestimmung der Blutgruppe", "Messung des Blutdrucks"], [0, 1], "", 30)
S("Was weist die Molekularpathologie nach?", ["DNA und RNA aus Geweben und Körperflüssigkeiten", "Nur Bakterienkulturen", "Organgewichte", "Hormone im Urin"], [0],
  "z. B. Veränderungen in Tumorgenen, Diagnostik von Infektionskrankheiten.", 31)
S("Welche Diagnose „gibt der Erkrankung ihren Namen“?", ["Die histologische Diagnose", "Die Anamnese", "Der Laborbefund", "Die Röntgenuntersuchung"], [0], "", 28)
S("Was ist MRSA?", ["Methicillin-resistenter Staphylococcus aureus – Problemkeim im Spital", "Ein Virus der Atemwege", "Ein Tumormarker", "Eine Autoimmunerkrankung"], [0],
  "Gefährlich, sobald er invasiv wird; Isolation im Einzelzimmer.", 5)
S("Wann ist MRSA besonders gefährlich?", ["Wenn er invasiv wird und Infektionen auslöst", "Solange er nur auf Haut/Nase sitzt", "Nur bei Kindern", "Nie"], [0],
  "Bloße Besiedelung (Kolonisation) ist ungefährlich.", 5)
S("Wozu dient die Mutationsanalyse eines Tumors in der Molekularpathologie?", ["Um die passende, individuelle Therapie zu finden", "Um die Tumorgröße zu messen", "Um den Todeszeitpunkt zu bestimmen", "Um Bakterien zu züchten"], [0],
  "Grundprinzip der personalisierten Medizin.", 5)
S("Was bedeutet eine RAS-Mutation beim Kolonkarzinom?", ["Der Tumor spricht auf EGFR-Hemmer nicht an", "Der Tumor ist gutartig", "Der Tumor wächst langsamer", "Der Patient ist geheilt"], [0],
  "Deshalb wird vor Therapiestart auf RAS getestet.", 6)
S("Was ist ein Nachteil der klassischen Chemotherapie?", ["Sie zerstört auch gesunde, sich schnell teilende Zellen (z. B. Knochenmark)", "Sie wirkt nur auf Bakterien", "Sie wirkt nur lokal", "Sie hat keine Nebenwirkungen"], [0],
  "Folge: z. B. Infektneigung.", 6)
S("Warum ist die PCR-Diagnostik bei Infektionen vorteilhaft?", ["Sie ist schneller als die klassische Plattenkultur", "Sie braucht keinen Erreger", "Sie ist billiger als jeder Test", "Sie zeigt Knochenbrüche"], [0], "", 5)

# ---------------------------------------------------------------- 2 Tod & Obduktion
K("2")
S("Was ist Thanatologie?", ["Wissenschaft vom Tod, Sterben und Bestattung", "Lehre von den Tumoren", "Lehre von den Entzündungen", "Lehre von den Blutungen"], [0], "", 33)
S("*Was kennzeichnet den klinischen Tod?", ["Durch Reanimation noch aufhebbar", "Funktion des ZNS noch erhalten", "Sichere Todeszeichen vorhanden", "Irreversibler Hirntod"], [0, 1],
  "Herz-Kreislauf- und Atemstillstand – Zeitfenster für Reanimation.", 34)
S("*Was ist der Individualtod?", ["Hirntod – irreversible Schädigung der Ganglienzellen des ZNS", "Herzstillstand mit erfolgreicher Reanimation", "Auftreten von Totenflecken", "Bewusstlosigkeit"], [0], "", 34)
S("*Woran erkennt man den biologischen Tod?", ["An den sicheren Todeszeichen", "Am Atemstillstand allein", "An der Bewusstlosigkeit", "Am fehlenden Puls"], [0], "", 34)
S("Wodurch wird der klinische Tod festgestellt?", ["Pulslosigkeit/fehlende Herztöne", "Fehlender Pupillen- und Kornealreflex", "Totenstarre", "Grünverfärbung des Bauches"], [0, 1],
  "Aufhören von Herz-Kreislauf-, Atem- und ZNS-Funktion.", 36)
S("Welche Kriterien gehören zur Feststellung des Hirntods?", ["Null-Linien-EEG", "Fehlen der Spontanatmung (Apnoetest)", "Erhöhte Körpertemperatur", "Vorhandene Reflexe"], [0, 1],
  "Außerdem Zirkulationsstillstand im Gehirn, Fehlen aller motorischen und vegetativen Reflexe.", 37)
S("Welche Regelung gilt in Österreich bei der Organspende?", ["Widerspruchslösung", "Zustimmungslösung", "Nur mit Testament", "Organspende ist verboten"], [0],
  "Jede:r ist Spender:in, außer im Widerspruchsregister eingetragen.", 7)
S("Warum sind Wachkoma-Patienten (Apalliker) keine Organspender?", ["Hirnstammfunktion und Spontanatmung sind erhalten – sie sind nicht hirntot", "Weil ihre Organe zu alt sind", "Weil sie immer Infektionen haben", "Weil das Herz stillsteht"], [0], "", 8)
S("*Welche sind sichere Todeszeichen?", ["Totenflecke", "Totenstarre", "Pulslosigkeit", "Atemstillstand"], [0, 1],
  "Sicher: Totenflecke, Totenstarre, späte Leichenerscheinungen (Autolyse, Fäulnis). Pulslosigkeit/Atemstillstand sind unsicher.", 38)
S("*Welche sind unsichere Todeszeichen?", ["Totenkälte", "Trübung der Hornhaut", "Totenflecke", "Fäulnis"], [0, 1],
  "Außerdem Pulslosigkeit, fehlende Herztöne, Atemstillstand.", 52)
S("Was gilt als sicheres Todeszeichen?", ["Fäulnis", "Bewusstlosigkeit", "Blässe", "Niedriger Blutdruck"], [0], "", 38)
S("*Wann treten Totenflecke erstmals auf?", ["Nach 10–30 Minuten", "Nach 6–8 Stunden", "Nach 2 Tagen", "Sofort im Moment des Todes"], [0], "", 39)
S("Wie entstehen Totenflecke?", ["Absinken des Blutes nach der Schwerkraft (Hypostase)", "Bakterielle Zersetzung", "Muskelkontraktion", "Austrocknung der Haut"], [0], "", 39)
S("Welche Farbe haben Totenflecke normalerweise?", ["Livid (blauviolett)", "Hellrot", "Grün", "Gelb"], [0], "Hellrot bei CO- oder Zyanidvergiftung sowie Kälte.", 39)
S("Hellrote Totenflecke können hinweisen auf …", ["Kohlenmonoxidvergiftung", "Zyanidvergiftung", "Herzinfarkt", "Diabetes"], [0, 1], "Auch bei Kälte.", 39)
S("Bis wann wandern Totenflecke bei Umlagerung vollständig?", ["Bis ca. 6 Stunden nach dem Tod", "Bis 30 Minuten", "Bis 48 Stunden", "Gar nicht"], [0],
  "Teilweise Verlagerung 6–12 h, Fixierung nach ca. 48 h.", 39)
S("Warum fehlen Totenflecke an Aufliegestellen?", ["Das Gewebe wird dort zusammengedrückt, Blut kann sich nicht ansammeln", "Dort ist die Haut dicker", "Dort gibt es keine Gefäße", "Weil die Leiche bewegt wurde"], [0], "", 40)
S("Wozu sind Totenflecke forensisch nützlich?", ["Rückschluss auf die Lage der Leiche", "Erkennen, ob die Leiche bewegt wurde", "Bestimmung der Blutgruppe", "Bestimmung der Todesursache Krebs"], [0, 1], "", 39)
S("*Warum entsteht die Totenstarre?", ["ATP wird nicht mehr regeneriert – Myosin-Aktin-Bindung löst sich nicht", "Blut sinkt ab", "Bakterien zersetzen die Muskeln", "Die Körpertemperatur steigt"], [0], "", 42)
S("*Wann beginnt die Totenstarre?", ["Nach ca. 30–60 Minuten", "Nach 10 Minuten", "Nach 12 Stunden", "Nach 3 Tagen"], [0], "Vollständig nach 6–8 h, Lösung nach 36–48 h.", 45)
S("Wann löst sich die Totenstarre wieder?", ["Nach ca. 36–48 Stunden", "Nach 1 Stunde", "Nach 6 Stunden", "Nie"], [0], "", 45)
S("Was besagt die Nysten'sche Regel?", ["Totenstarre bildet und löst sich vom Kiefer absteigend", "Totenflecke entstehen an der höchsten Stelle", "Fäulnis beginnt an den Füßen", "Totenkälte sinkt 5 °C pro Stunde"], [0], "", 45)
S("Wo beginnt die Fäulnis typischerweise?", ["Grünverfärbung im rechten Unterbauch", "An den Fingerspitzen", "Am Kopf", "Am Rücken"], [0], "Bakterien aus dem Darm; „Pseudomelanose“.", 46)
S("Was unterscheidet Autolyse von Fäulnis?", ["Autolyse ist abakteriell (zelleigene Enzyme), Fäulnis ist bakteriell", "Autolyse ist bakteriell, Fäulnis nicht", "Beides ist dasselbe", "Fäulnis tritt nur bei Kälte auf"], [0], "", 46)
S("Welche Zeichen gehören zur Fäulnis?", ["Durchschlagende Venennetzzeichnung", "Fäulnisblasen", "Hellrote Totenflecke", "Kältestarre"], [0, 1], "Außerdem Gasbildung, Auftreibung, Hautablösung.", 46)
S("Wann kommt es zur Mumifizierung?", ["Bei trockenem, gut belüftetem Klima", "Bei feuchter Wärme", "Im Wasser", "Bei Kohlenmonoxidvergiftung"], [0], "", 46)
S("Wie schnell kühlt ein Leichnam ungefähr ab?", ["Ca. 1 °C pro Stunde", "Ca. 5 °C pro Stunde", "Ca. 0,1 °C pro Tag", "Gar nicht"], [0], "Abhängig von Isolierung und Umgebung.", 8)
S("Wer muss in Österreich eine verstorbene Person beschauen?", ["Ein Totenbeschauarzt (im Spital Pathologe)", "Der Bestatter", "Die Polizei", "Die Angehörigen"], [0],
  "Feststellung des Todes und Ermittlung der Todesursache.", 54)
S("Ab wann ist eine Leiche für die Bestattung „frei“?", ["Mit der Sterbeurkunde vom Standesamt", "Sofort nach dem Tod", "Nach der Obduktion immer", "Nach 24 Stunden automatisch"], [0], "", 9)
S("*Wer beauftragt eine gerichtliche Obduktion?", ["Die Staatsanwaltschaft", "Die Angehörigen", "Der Hausarzt", "Die Krankenkasse"], [0],
  "Bei Verdacht auf Fremdverschulden, aufgefundenen Leichenteilen, Tod in Narkose.", 58)
S("*Wann wird eine sanitätsbehördliche Obduktion angeordnet?", ["Bei unklarer natürlicher Todesursache außerhalb einer öffentlichen Krankenanstalt", "Bei Mordverdacht", "Bei jedem Spitalstod", "Nur auf Wunsch der Familie"], [0],
  "Angeordnet durch die Sanitätsbehörde (Totenbeschauarzt), z. B. Tod im Pflegeheim.", 58)
S("*Was ist eine klinische Obduktion?", ["Obduktion von Patient:innen, die in einer öffentlichen Krankenanstalt an natürlicher Ursache verstorben sind", "Obduktion im Auftrag der Staatsanwaltschaft", "Obduktion bei Verkehrsunfällen", "Privat bezahlte Obduktion"], [0],
  "= Spitalsobduktion, durchgeführt von Patholog:innen.", 58)
S("Welche Aufgaben hat die klinische Obduktion?", ["Überprüfung der klinischen Diagnose und Behandlung", "Grundlage für Todesursachenstatistik", "Klärung von Fremdverschulden", "Ausstellung des Reisepasses"], [0, 1], "Außerdem Wissenschaft und Unterricht.", 59)
S("Wann darf in einer öffentlichen Krankenanstalt ohne Zustimmung der Angehörigen obduziert werden?", ["Bei diagnostischer Unklarheit", "Nach einem operativen Eingriff", "Immer, wenn es der Arzt möchte", "Nie"], [0, 1],
  "Auch zur medizinischen Ausbildung oder wenn angeordnet (Wr. KAG §40).", 57)
S("Wer darf eine Obduktion durchführen?", ["Ein Arzt/eine Ärztin mit Befugnis der Ärztekammer", "Jede Pflegeperson", "Der Bestatter", "Die Polizei"], [0], "", 56)

# ---------------------------------------------------------------- 3 Krankheitslehre
K("3")
S("Wie ist Krankheit laut Skript definiert?", ["Folge einer ungünstigen Änderung biologischer, psychischer oder sozialer Funktionsabläufe", "Jede Abweichung vom Durchschnitt", "Nur körperliche Schmerzen", "Fehlen von Wohlbefinden für einen Tag"], [0], "", 21)
S("*Was bezeichnet die Ätiologie?", ["Die eigentliche, die Krankheit auslösende Ursache", "Den Ablauf der Reaktion im Körper", "Das sichtbare Krankheitszeichen", "Die unerwünschte Folge"], [0], "", 71)
S("*Was bezeichnet die Pathogenese?", ["Den Ablauf der Reaktion des Organismus auf die Ursache", "Die Ursache der Krankheit", "Die Heilung", "Die Diagnose"], [0], "", 71)
S("Was ist eine Komplikation?", ["Eine unerwünschte Folge einer Krankheit", "Die Ursache einer Krankheit", "Ein Laborwert", "Eine Therapieform"], [0], "", 71)
S("Beim Rauchen als Ursache von Lungenkrebs ist die Metastasierung …", ["die Komplikation", "die Ätiologie", "die Pathogenese", "das Symptom"], [0],
  "Ätiologie: Rauchen; Pathogenese: Veränderung der Erbsubstanz; Symptom: Lungenkrebs.", 72)
S("Was ist bei chronischem Alkoholkonsum die Pathogenese?", ["Fettleber und Hepatitis bis zur Zirrhose", "Der Alkohol selbst", "Gelbsucht und Aszites", "Der Tod"], [0], "Ikterus, Aszites, Enzephalopathie sind Komplikationen.", 73)
S("*Was kennzeichnet einen perakuten Verlauf?", ["Schlagartiger Beginn, kurzer Verlauf, meist tödlich", "Schleichender Beginn", "Langsamer Verlauf über Jahre", "Immer folgenlose Heilung"], [0],
  "z. B. bakterielle Meningitis; auch „fulminant“ oder „foudroyant“.", 65)
S("Was ist ein typisches Beispiel für einen perakuten Verlauf?", ["Bakterielle Meningitis", "Grippaler Infekt", "Chronische Polyarthritis", "Arteriosklerose"], [0], "", 65)
S("Was kennzeichnet einen akuten Verlauf?", ["Rascher Beginn, symptomreich, kurze Dauer, häufig Heilung", "Beginn nicht feststellbar", "Immer tödlich", "Schübe mit Remissionen"], [0], "z. B. Pneumonie.", 65)
S("Welche Erkrankung verläuft typischerweise subakut?", ["Endokarditis", "Bakterielle Meningitis", "Grippaler Infekt", "Herzinfarkt"], [0], "Schwache Anfangssymptomatik, schleichender Beginn.", 65)
S("Was bedeutet „primär-chronisch“?", ["Beginn nicht sicher feststellbar, von Anfang an langsamer Verlauf", "Aus einer akuten Krankheit hervorgegangen", "Plötzlicher tödlicher Verlauf", "In Schüben verlaufend"], [0], "z. B. chronische Polyarthritis.", 65)
S("Was bedeutet „sekundär-chronisch“?", ["Aus einer nicht ausgeheilten akuten Erkrankung entstanden", "Von Geburt an vorhanden", "Schlagartig tödlich", "Durch Gene vererbt"], [0], "z. B. akute Bronchitis wird zum chronischen Husten.", 10)
S("Eine Infektion mit Streptokokken kann verschiedene Krankheiten auslösen. Welche?", ["Tonsillitis", "Rheumatisches Fieber", "Laktoseintoleranz", "Diabetes Typ 1"], [0, 1],
  "Außerdem Endokarditis, Glomerulonephritis, Chorea minor, Scharlach, Erysipel.", 74)
S("Wie entsteht das rheumatische Fieber nach Streptokokkeninfekt?", ["Antikörper gegen Bakterien greifen körpereigenes Gewebe an (Kreuzreaktion)", "Direkte Toxinwirkung im Hals", "Vererbung", "Durch Viren"], [0],
  "Betroffen: Herzklappen, Niere, Gelenke, Basalganglien. Frühe Antibiose senkt das Risiko.", 12)
S("Was ist die Chorea minor („kleiner Veitstanz“)?", ["Kreuzreaktion antibakterieller Antikörper mit Basalganglienzellen im Gehirn", "Eine Herzrhythmusstörung", "Eine Nierenentzündung", "Ein Hauttumor"], [0], "", 74)
S("Wie heißen kugelförmige Bakterien, die in Ketten angeordnet sind?", ["Streptokokken", "Staphylokokken", "Stäbchen", "Spirochäten"], [0], "Traubenförmig = Staphylokokken.", 12)
S("Welches Beispiel ist eine ANGEBORENE Krankheitsursache?", ["Trisomie 21", "BRCA-Mutation (Mammakarzinom)", "Arteriosklerose", "Trauma"], [0, 1], "", 76)
S("Welches Beispiel ist eine ERWORBENE Krankheitsursache?", ["Infektionskrankheit", "Lungenkrebs durch Rauchen", "Trisomie 21", "Dysmelie durch Thalidomid"], [0, 1], "", 76)
S("Dysmelie durch Thalidomid (Contergan) ist ein Beispiel für …", ["angeborene Erkrankung mit äußerer Ursache", "erworbene innere Ursache", "genetische Prädisposition", "Altersatrophie"], [0], "", 76)
S("Wofür steht eine BRCA-Mutation?", ["Genetische Prädisposition für Brust- und Eierstockkrebs", "Eine Virusinfektion", "Eine Stoffwechselstörung", "Eine Blutgerinnungsstörung"], [0],
  "BRCA ist ein DNA-Reparaturgen; bis zu ~90 % Lebenszeitrisiko für Brustkrebs.", 13)
S("Welche zählen zu den BELEBTEN äußeren Krankheitsursachen?", ["Bakterien", "Würmer", "Strom", "Hitze"], [0, 1], "Belebt = Krankheitserreger (Bakterien, Viren, Pilze, Würmer).", 78)
S("Welche zählen zu den UNBELEBTEN äußeren Krankheitsursachen?", ["Ernährungsstörungen", "Physikalische Ursachen (Hitze, Kälte, Strom)", "Viren", "Pilze"], [0, 1], "Außerdem chemische „Gifte“.", 79)
S("Was ist eine Disposition?", ["Neigung, an einer bestimmten Krankheit zu erkranken", "Eine sichere Diagnose", "Eine Komplikation", "Eine Therapie"], [0], "Kann angeboren oder erworben sein.", 85)
S("*Was ist eine Defektheilung?", ["Abnormer Dauerzustand, nicht völlig behebbares Leiden", "Völlige Wiederherstellung", "Tod", "Rückfall"], [0],
  "Ausgänge einer Krankheit: Heilung, Defektheilung, Tod.", 86)
S("Wann wird Pilzbefall (Candidose) typischerweise begünstigt?", ["Nach Breitband-Antibiotika", "Bei Immunsuppression", "Bei viel Bewegung", "Bei niedrigem Blutdruck"], [0, 1], "Pilze sind meist harmlose Standortflora.", 14)
S("Was ist das wichtigste Prinzip der Prävention laut Vorlesung?", ["Kontakt mit der bekannten Ursache vermeiden und Vorsorgeuntersuchungen nutzen", "Möglichst viele Medikamente nehmen", "Nur im Krankheitsfall zum Arzt gehen", "Impfungen vermeiden"], [0], "", 14)


# ---------------------------------------------------------------- 4 Zellpathologie
K("4")
S("Was ist das spezifische Organparenchym?", ["Die Zellen, die die eigentliche Organfunktion tragen (z. B. Leberzellen)", "Das Gefäßbindegewebe", "Die Organkapsel", "Das Fettgewebe um das Organ"], [0],
  "Unspezifisches Stroma = Interstitium = Gefäßbindegewebe.", 88)
S("*Welche Gewebe gehören zum Wechselgewebe?", ["Blutbildendes Knochenmark", "Schleimhautepithel", "Nervenzellen", "Herzmuskulatur"], [0, 1],
  "Wechselgewebe: ständiger Zyklus aus Neubildung und Untergang.", 92)
S("*Welche Gewebe gehören zum Ruhegewebe (nicht mehr neu bildbar)?", ["Ganglienzellen (Nervenzellen)", "Herzmuskulatur", "Leberzellen", "Hautepithel"], [0, 1], "", 92)
S("Leberzellen gehören zu welchem Gewebetyp?", ["Dauergewebe", "Wechselgewebe", "Ruhegewebe", "Stützgewebe"], [0], "Lange Lebensdauer, im Schadensfall neu bildbar.", 92)
S("Was ist ein Beispiel für physiologische Regeneration?", ["Der Menstruationszyklus (Abstoßung und Neuaufbau des Endometriums)", "Eine Herzinfarktnarbe", "Ein Hirninfarkt", "Eine Amputation"], [0], "", 93)
S("Was ist Adaptation?", ["Anpassung des Gewebes an Reize mit Erhaltung der Organfunktion", "Zelltod durch Sauerstoffmangel", "Bösartige Entartung", "Blutung ins Gewebe"], [0],
  "Bei Überschreitung der Anpassungsfähigkeit kommt es zur Zellschädigung.", 95)
S("*Was ist eine Atrophie?", ["Zell- bzw. Organverkleinerung", "Zellvergrößerung", "Zellvermehrung", "Ersatz eines Zelltyps durch einen anderen"], [0], "", 98)
S("*Was ist eine Hypertrophie?", ["Organvergrößerung durch Zellvergrößerung (Zellzahl gleich)", "Organvergrößerung durch Zellvermehrung", "Organverkleinerung", "Bösartiger Tumor"], [0], "", 104)
S("*Was ist eine Hyperplasie?", ["Organvergrößerung durch Zellvermehrung", "Organvergrößerung durch Zellvergrößerung", "Zellverkleinerung", "Zelltod"], [0], "Voraussetzung: teilungsfähige Zellen.", 110)
S("*Was ist eine Metaplasie?", ["Reversibler Ersatz eines reifen Zelltyps durch einen anderen reifen Zelltyp", "Irreversible Entdifferenzierung", "Zellvermehrung", "Zellverkleinerung"], [0],
  "Ursache: chronische Irritation.", 116)
S("Welche Ursachen hat eine Atrophie?", ["Inaktivität (z. B. Gips)", "Verminderte Blutversorgung", "Erhöhte Belastung", "Hormonelle Stimulation in der Schwangerschaft"], [0, 1],
  "Außerdem gestörte Innervation, weniger Hormone, Alter.", 98)
S("Ein Arm schrumpft nach 6 Wochen Gips. Das ist …", ["Inaktivitätsatrophie", "Hyperplasie", "Metaplasie", "Nekrose"], [0], "", 98)
S("Was sind Kennzeichen eines atrophen Organs?", ["Organverkleinerung", "Festere Konsistenz und Pigmentablagerung (bräunlich)", "Weichere Konsistenz und Rötung", "Vermehrte Zellteilung"], [0, 1], "Außerdem Vakatwucherung von Fettgewebe.", 99)
S("Was ist eine Vakatwucherung?", ["Fettgewebe füllt den frei werdenden Raum bei Atrophie", "Ein bösartiger Fetttumor", "Eine Narbe", "Eine Entzündung des Fettgewebes"], [0], "Keine echte Wucherung.", 99)
S("Wodurch entsteht die Muskelatrophie bei Poliomyelitis?", ["Viren zerstören Motoneuronen im Rückenmark (gestörte Innervation)", "Durch Gips", "Durch Hormonmangel", "Durch Bluthochdruck"], [0], "", 100)
S("Welche Beispiele sind Hypertrophien?", ["Herzmuskelvergrößerung bei Bluthochdruck", "Uterusvergrößerung in der Schwangerschaft", "Struma bei Jodmangel", "Prostatavergrößerung durch Zellvermehrung"], [0, 1],
  "Struma und Prostatavergrößerung sind Hyperplasien.", 104)
S("Was ist eine „Überlastungshypertrophie“ des Herzens?", ["Hypertrophie durch erhöhte Druckbelastung, z. B. Hypertonie oder Aortenklappenstenose", "Hypertrophie durch Ausdauersport", "Herzverkleinerung im Alter", "Herzmuskelentzündung"], [0], "", 105)
S("Ab welchem Herzgewicht spricht man vom kritischen Herzgewicht?", ["Ca. 500 g", "Ca. 250 g", "Ca. 350 g", "Ca. 1000 g"], [0],
  "Normal < 350 g; darüber wachsen die Herzkranzgefäße nicht mit → Sauerstoffmangel.", 107)
S("Warum ist eine pathologische Herzhypertrophie gefährlich?", ["Die Herzkranzgefäße wachsen nicht mit – Sauerstoffmangel bis Infarkt", "Das Herz wird zu leicht", "Die Herzfrequenz sinkt auf null", "Sie verursacht Krebs"], [0], "", 106)
S("Was gilt für das Sportherz (Ausdauer)?", ["Harmonische Vergrößerung aller Herzhöhlen", "Kritisches Herzgewicht wird nicht überschritten", "Konzentrische Hypertrophie durch Anabolika", "Funktion in Ruhe stark eingeschränkt"], [0, 1], "", 108)
S("Welche Beispiele sind Hyperplasien?", ["Struma bei Jodmangel (TSH-Stimulation)", "Leberregeneration nach Teilentfernung", "Muskelschwund durch Gips", "Plattenepithel im Bronchus"], [0, 1], "", 110)
S("Warum entsteht eine Struma bei Jodmangel?", ["Zu wenig Schilddrüsenhormon → mehr TSH → Schilddrüse bildet mehr Zellen", "Zu viel Jod verklebt die Zellen", "Bakterielle Entzündung", "Bösartiger Tumor"], [0], "", 113)
S("Die Prostatavergrößerung im Alter führt zu …", ["Einengung der Harnröhre und Problemen beim Blasenentleeren", "Atemnot", "Gelbsucht", "Herzrhythmusstörungen"], [0], "", 112)
S("*Was ist ein Beispiel für eine Metaplasie?", ["Ersatz des Flimmerepithels der Bronchien durch Plattenepithel bei Rauchern", "Barrett-Schleimhaut der Speiseröhre bei Reflux", "Vergrößerung des Herzens", "Schrumpfniere"], [0, 1], "", 116)
S("Was ist das Risiko der Barrett-Schleimhaut?", ["Erhöhtes Risiko für Speiseröhrenkrebs", "Erhöhtes Herzinfarktrisiko", "Nierenversagen", "Keines"], [0], "Ursache: chronischer Reflux von Magensäure.", 117)
S("Was passiert bei Plattenepithelmetaplasie im Bronchus?", ["Flimmerhärchen fallen weg, die Lunge reinigt sich schwerer", "Die Lunge wird größer", "Die Bronchien werden weiter", "Die Atmung wird leichter"], [0], "Ein Schritt näher zu Lungenkrebs.", 118)
S("*Was ist die wichtigste schädigende Noxe der Medizin?", ["Sauerstoffmangel (Hypoxie)", "Strahlung", "Bakterien", "Medikamente"], [0], "", 121)
S("Welche Ursachen hat Sauerstoffmangel (Hypoxie)?", ["Arteriosklerose (mangelhafte Blutversorgung)", "Anämie", "Zu viel Bewegung", "Zu viel Wasser"], [0, 1],
  "Außerdem geringe Oxygenierung (Höhe, Lungenfibrose) und CO-Vergiftung.", 122)
S("Was ist eine Ischämie?", ["Verlust der Blutversorgung in einem Gewebe – eine Ursache von Hypoxie", "Zu viel Blut im Gewebe", "Eine Blutung", "Eine Entzündung"], [0], "", 124)
S("Welche Schäden verursacht UV-Strahlung?", ["Hauttumore (Melanom, Basaliom, Plattenepithelkarzinom)", "Elastose (Schädigung des Hautbindegewebes)", "Leberzirrhose", "Diabetes"], [0, 1], "Ionisierende Strahlung schädigt die DNA.", 127)
S("Wie heißt eine reversible Zellschädigung?", ["Dystrophie", "Nekrose", "Apoptose", "Anaplasie"], [0], "Formen: trübe Schwellung, fettige und hyaline Dystrophie.", 129)
S("Was ist eine fettige Dystrophie?", ["Abnorme Einlagerung von Fett in den Zellen („Verfettung“)", "Abnorme Wassereinlagerung", "Abnorme Eiweißspeicherung", "Zelltod durch Fett"], [0], "Beispiel: Fettleber (Steatosis hepatis).", 132)
S("Was ist die hyaline Dystrophie?", ["Abnorme Speicherung von Proteinen in der Zelle", "Abnorme Fetteinlagerung", "Abnorme Wassereinlagerung", "Verkalkung"], [0], "", 132)
S("Wie sieht eine Fettleber (Steatosis hepatis) aus?", ["Groß und gelb", "Klein und schwarz", "Rot und hart", "Grün und weich"], [0], "Histologisch leere Bläschen (Fett ausgewaschen).", 133)
S("*Was ist der Unterschied zwischen Nekrose und Apoptose?", ["Nekrose: irreversibles, schädigungsbedingtes Absterben von Zellverbänden", "Apoptose: genetisch programmierter Tod einzelner Zellen", "Apoptose: immer krankhaft", "Nekrose: physiologische Zellmauserung"], [0, 1], "", 136)
S("Was ist die Apoptose?", ["Programmierter Zelltod einzelner Zellen – natürliche „Zellmauserung“", "Absterben eines ganzen Organbezirks", "Eine Entzündung", "Ein Tumor"], [0], "Gleichgewicht zwischen Zellvermehrung und Zellelimination.", 136)
S("*Welche Merkmale hat die Koagulationsnekrose?", ["Fest, trocken, lehmfarben", "Typisch bei Herz-, Milz- und Niereninfarkt", "Puddingartig verflüssigt", "Typisch im Gehirn"], [0, 1], "Eiweißgerinnung; Ursache plötzliche Ischämie, Säuren.", 140)
S("*Welche Merkmale hat die Kolliquationsnekrose?", ["Verflüssigung, puddingartig", "Typisch im Gehirn (Hirninfarkt), hinterlässt Hohlraum", "Fest und lehmfarben", "Typisch beim Herzinfarkt"], [0, 1],
  "Durch hydrolytische Enzyme; v. a. in lipidreichen, proteinarmen Geweben.", 145)
S("Welche Nekroseform tritt typischerweise beim Herzinfarkt auf?", ["Koagulationsnekrose", "Kolliquationsnekrose", "Käsige Nekrose", "Fettgewebsnekrose"], [0], "", 140)
S("Welche Nekroseform tritt typischerweise beim Hirninfarkt auf?", ["Kolliquationsnekrose", "Koagulationsnekrose", "Käsige Nekrose", "Trockene Gangrän"], [0], "", 145)
S("Was ist Autolyse?", ["Selbstverdauung durch zelleigene Enzyme", "Verdauung durch bakterielle Enzyme", "Verkalkung", "Narbenbildung"], [0], "Heterolyse = Verdauung durch fremde (z. B. bakterielle) Enzyme.", 145)
S("Was unterscheidet trockene von feuchter Gangrän?", ["Trocken: Austrocknung und Schwarzfärbung (Mumifizierung)", "Feucht: bakterielle Infektion mit Fäulniserregern", "Trocken: immer am Gehirn", "Feucht: ohne Bakterien"], [0, 1], "Meist an Extremitäten nach Gefäßverschluss.", 147)
S("Bei welcher Erkrankung tritt die Fettgewebsnekrose typisch auf?", ["Akute Pankreatitis", "Tuberkulose", "Herzinfarkt", "Hirninfarkt"], [0],
  "Lipase aus der Bauchspeicheldrüse; Fettsäuren + Calcium → kalkweiße Seifen.", 149)
S("Welche Ursachen hat eine akute Pankreatitis laut Skript?", ["Alkoholexzess", "Gallensteine", "Sonnenbrand", "Jodmangel"], [0, 1], "Abfluss am Gallengang blockiert.", 150)
S("*Die käsige Nekrose ist typisch für …", ["Tuberkulose", "Herzinfarkt", "Pankreatitis", "Diabetes"], [0], "Schnittfläche wie Hüttenkäse.", 151)
S("*Welches Schicksal kann eine Nekrose haben?", ["Narbenbildung", "Hohlraumbildung (Zyste, Abszess)", "Umwandlung in gesundes Gewebe bei großen Nekrosen", "Umwandlung in einen Tumor"], [0, 1],
  "Außerdem: vollständige Regeneration (nur sehr klein), Ulkusbildung, Verkalkung.", 152)
S("Was bleibt nach einem überlebten Herzinfarkt zurück?", ["Eine bindegewebige Narbe", "Ein Hohlraum", "Völlig gesundes Herzmuskelgewebe", "Ein Tumor"], [0], "", 152)
S("Was bleibt nach einem alten Hirninfarkt zurück?", ["Ein zystischer Hohlraum", "Eine feste Narbe wie im Herz", "Ein Abszess immer", "Nichts"], [0], "", 152)
S("Was ist ein Ulkus?", ["Substanzdefekt an einer Oberfläche nach Abräumung von Nekrosegewebe", "Ein gutartiger Tumor", "Eine Blutung in Gewebsspalten", "Ein Ödem"], [0], "Beispiel: Magengeschwür.", 152)
S("Welche Gefahren bestehen bei einem Magenulkus?", ["Perforation (Durchbruch)", "Blutung aus einem angegriffenen Gefäß", "Totenstarre", "Struma"], [0, 1], "", 155)

# ---------------------------------------------------------------- 5 Entzündung & Wundheilung
K("5")
S("Welche Endung kennzeichnet Entzündungen?", ["-itis", "-om", "-ose", "-ämie"], [0], "Ausnahmen: Rachitis ist keine Entzündung, Pneumonie ist eine.", 156)
S("Was ist die Entzündung?", ["Eine Verteidigungsreaktion des Organismus gegen schädigende Einwirkungen", "Immer eine bakterielle Infektion", "Ein Tumor", "Ein Zeichen des Todes"], [0], "", 157)
S("Was ist der Zweck einer Entzündung?", ["Beseitigung des Entzündungsreizes", "Ersatz des zugrunde gegangenen Gewebes", "Bildung von Metastasen", "Senkung der Körpertemperatur"], [0, 1], "", 158)
S("Welche Entzündungsreize sind „nicht lebend“?", ["Hitze, Kälte, Strahlen", "Säuren und Laugen", "Bakterien", "Würmer"], [0, 1], "", 159)
S("*Was ist „Rubor“?", ["Rötung", "Schmerz", "Schwellung", "Erwärmung"], [0], "Kardinalsymptome: Rubor, Calor, Tumor, Dolor, Functio laesa.", 160)
S("*Was ist „Functio laesa“?", ["Eingeschränkte Funktion", "Schwellung", "Erwärmung", "Schmerz"], [0], "", 160)
S("*Welche gehören zu den 5 Kardinalsymptomen der Entzündung?", ["Calor (Erwärmung)", "Dolor (Schmerz)", "Pallor (Blässe)", "Cyanose (Blaufärbung)"], [0, 1], "", 160)
S("Was bedeutet „Tumor“ als Entzündungszeichen?", ["Schwellung", "Krebs", "Rötung", "Fieber"], [0], "", 160)
S("Welche allgemeinen Reaktionen gehören zur Entzündung?", ["Fieber", "CRP-Erhöhung", "Absinken der Leukozyten auf null", "Senkung der Körpertemperatur"], [0, 1], "Außerdem Leukozytose und Vermehrung der Immunglobuline.", 162)
S("Was ist CRP?", ["Ein Akute-Phase-Protein aus der Leber, erhöht bei Entzündung", "Ein Hormon der Schilddrüse", "Ein Tumorgen", "Ein Bakterium"], [0], "C-reaktives Protein, aktiviert u. a. die Phagozytose.", 162)
S("Was schwächt die Entzündungsantwort ab?", ["Cortison", "Diabetes (verzögerte Reaktion)", "Gute Ernährung", "Gute Durchblutung"], [0, 1], "", 163)
S("Was ist eine rezidivierende Entzündung?", ["Ablauf in Schüben mit symptomfreien Intervallen", "Einmalige, kurze Entzündung", "Immer tödliche Entzündung", "Entzündung ohne Symptome"], [0],
  "Remission = symptomfrei, Exazerbation = Wiederaufflackern; z. B. Morbus Crohn.", 169)
S("Was bedeutet Exazerbation?", ["Wiederaufflackern der Entzündung", "Symptomfreies Intervall", "Heilung", "Narbenbildung"], [0], "", 169)
S("*Welches Exsudat ist dünnflüssig, klar bis blassgelb (z. B. rinnende Nase)?", ["Serös", "Fibrinös", "Eitrig", "Hämorrhagisch"], [0], "", 170)
S("*Bei welcher Entzündungsform bildet sich eine trockene „Matte“ aus Fibrin auf der Oberfläche?", ["Fibrinöse Entzündung", "Seröse Entzündung", "Eitrige Entzündung", "Serös-katarrhalische Entzündung"], [0], "z. B. Perikarditis.", 170)
S("Was ist eine serös-katarrhalische Entzündung?", ["Exsudat aus Serum, abgeschilferten Epithelien und Schleim (z. B. Atemwegsinfekt)", "Exsudat aus Eiter", "Exsudat mit vielen roten Blutkörperchen", "Exsudat aus Fibrin"], [0], "", 170)
S("Was ist eine hämorrhagische Entzündung?", ["Exsudat enthält viele Erythrozyten und erscheint blutig", "Exsudat ist klar und dünn", "Exsudat ist schleimig", "Exsudat ist käsig"], [0], "z. B. Grippepneumonie, Urämie (Harnblase).", 182)
S("Woraus besteht Eiter (Pus)?", ["Gewebsdetritus und Granulozyten", "Lebende oder abgestorbene Eitererreger", "Nur Wasser", "Nur rote Blutkörperchen"], [0, 1], "Farbe gelb bis grau-grünlich.", 172)
S("*Was ist ein Empyem?", ["Eiteransammlung in einem schon vorhandenen (präformierten) Hohlraum", "Eiteransammlung in einem durch Nekrose neu entstandenen Hohlraum", "Diffuse Eiterausbreitung im Gewebe", "Blutansammlung im Gewebe"], [0],
  "z. B. Brusthöhle, Bauchhöhle, Herzbeutel.", 173)
S("*Was ist ein Abszess?", ["Eiteransammlung in einem durch Nekrose neu entstandenen Hohlraum", "Eiter in einem präformierten Hohlraum", "Diffuse, nicht abgegrenzte Eiterausbreitung", "Ein gutartiger Tumor"], [0], "", 176)
S("*Was ist eine Phlegmone?", ["Diffuse, nicht abgegrenzte eitrige Entzündung im Gewebe", "Abgekapselte Eiteransammlung", "Eiter im Herzbeutel", "Blutung unter die Haut"], [0], "z. B. Streptokokkeninfektion unter der Haut.", 175)
S("Was bedeutet „Ubi pus, ibi evacua“?", ["Wo Eiter ist, muss er entfernt werden", "Eiter heilt von selbst", "Eiter immer mit Antibiotika behandeln", "Eiter nie berühren"], [0], "", 177)
S("Warum soll man einen Abszess nicht ausdrücken?", ["Man drückt Bakterien tiefer ins Gewebe", "Weil er sonst zu schnell heilt", "Weil Eiter steril ist", "Weil es eine Blutung auslöst"], [0], "", 176)
S("*Wo entsteht ein Dekubitus typischerweise?", ["Über Knochenvorsprüngen (z. B. Steißbein)", "Bei immobilisierten Patient:innen durch lange Druckeinwirkung", "Nur im Gesicht", "Nur bei Sportlern"], [0, 1],
  "Druck → Ischämie → Nekrose; Beginn schon nach wenigen Stunden möglich.", 181)
S("Was ist ein Granulom?", ["Knötchenförmig angeordnetes Granulationsgewebe", "Eine Eiteransammlung", "Eine Blutung", "Ein Ödem"], [0], "Typisches spezifisches Granulom: Tuberkulose.", 185)
S("*Was ist der Unterschied zwischen Regeneration und Reparation?", ["Regeneration: vollwertiger Ersatz durch Parenchymzellen", "Reparation: Ersatz durch kollagenes Bindegewebe (Narbe)", "Reparation: völlige Wiederherstellung", "Regeneration: immer Narbe"], [0, 1], "", 187)
S("*Was geschieht in der exsudativen Phase der Wundheilung (1.–3. Tag)?", ["Blut gerinnt und verschließt die Wunde provisorisch", "Granulozyten grenzen das nekrotische Gewebe ab", "Narbe wird weiß", "Haare wachsen nach"], [0, 1], "Außerdem Wundödem durch erhöhte Gefäßdurchlässigkeit.", 189)
S("*Wann findet die proliferative Phase der Wundheilung statt?", ["3.–10. Tag", "1.–3. Tag", "Ab der 6. Woche", "In der ersten Stunde"], [0], "Fibroblasten und Kapillaren bilden Granulationsgewebe.", 190)
S("Woher hat das Granulationsgewebe seinen Namen?", ["Kapillarsprossen erscheinen als kleine Körnchen (Granula)", "Es enthält Granulozyten", "Es ist körnig verkalkt", "Es ist ein Tumor"], [0], "", 190)
S("Warum ist eine frische Narbe rötlich und eine alte weiß?", ["Frisch viele Blutgefäße, alt fast nur Bindegewebsfasern", "Wegen Sonnenlicht", "Wegen Eiter", "Weil sich Pigment bildet"], [0], "", 192)
S("Was wird im Narbenbereich NICHT ersetzt?", ["Haare, Drüsen, Nägel (Hautanhangsgebilde)", "Melanozyten (kaum)", "Kollagenfasern", "Bindegewebe"], [0, 1], "Narbe ist heller und eingezogen.", 192)
S("*Was kennzeichnet die primäre Wundheilung (per primam intentionem)?", ["Wundränder verkleben direkt – zarte Narbe", "Typisch bei glatter OP-Wunde", "Heilung über Granulationsgewebe von unten", "Typisch beim Dekubitus"], [0, 1], "Dauer 1–2 Wochen, geringes Komplikationsrisiko.", 193)
S("*Was kennzeichnet die sekundäre Wundheilung (per secundam intentionem)?", ["Verzögerte Heilung über Granulationsgewebe", "Bei offenen oder infizierten Wunden", "Direktes Verkleben der Wundränder", "Immer innerhalb von 3 Tagen abgeschlossen"], [0, 1], "Dauer Wochen bis Monate, z. B. Dekubitus.", 193)
S("Was ist eine Wunddehiszenz?", ["Aufgehen der Wunde", "Flüssigkeitsansammlung in der Wunde", "Überschießende Narbe", "Nervenknoten in der Narbe"], [0], "", 198)
S("Was ist ein Serom?", ["Flüssigkeitsgefüllter Hohlraum im Wundgebiet", "Eine eitrige Wunde", "Eine dicke Narbe", "Ein Tumor"], [0], "", 198)
S("Was ist ein Keloid?", ["Überschießende, dicke Narbenbildung", "Eine Wundinfektion", "Ein Abszess", "Ein Nervenknoten"], [0], "", 198)
S("Welche Faktoren stören die Wundheilung?", ["Diabetes mellitus", "Cortisonpräparate", "Ausreichende Vitamin-C-Zufuhr", "Gute Durchblutung"], [0, 1], "Außerdem Alter, Arteriosklerose, Mangelernährung.", 203)
S("Ohne welches Vitamin gibt es keine Wundheilung?", ["Vitamin C", "Vitamin D", "Vitamin K", "Vitamin A"], [0], "", 203)


# ---------------------------------------------------------------- 6 Tumorpathologie
K("6")
S("*Was ist ein Neoplasma?", ["Irreversible, autonome Zellneubildung und -vermehrung", "Eine Entzündung", "Eine Flüssigkeitsansammlung", "Eine Narbe"], [0], "", 205)
S("Was passiert mit dem Tumorwachstum, wenn die auslösende Ursache wegfällt?", ["Es geht weiter – das Wachstum wird nicht eingestellt", "Es stoppt sofort", "Der Tumor bildet sich immer zurück", "Er wird gutartig"], [0],
  "Der Prozess ist in der DNA verankert.", 205)
S("Was bedeutet der Begriff „Tumor“ ursprünglich?", ["Schwellung – kann auch durch Entzündung entstehen", "Immer Krebs", "Immer gutartig", "Blutung"], [0], "", 206)
S("Was bezeichnet die Dignität eines Tumors?", ["Sein biologisches Verhalten (gutartig/bösartig)", "Seine Größe", "Seinen Ort", "Sein Gewicht"], [0], "", 207)
S("*Welche Merkmale hat ein BENIGNER Tumor?", ["Langsames, expansives (verdrängendes) Wachstum", "Scharf begrenzt, keine Metastasen", "Infiltratives Wachstum", "Häufige Rezidive"], [0, 1], "Nach Resektion geheilt.", 208)
S("*Welche Merkmale hat ein MALIGNER Tumor?", ["Infiltratives, destruierendes Wachstum", "Metastasen", "Scharf begrenzt mit Kapsel", "Nach Entfernung immer geheilt"], [0, 1], "", 208)
S("*Was ist DAS entscheidende Kriterium der Bösartigkeit?", ["Metastasierung", "Größe", "Farbe", "Schmerzhaftigkeit"], [0], "Metastasen sind ein eindeutiges Malignitätszeichen.", 208)
S("Was ist ein Leiomyom des Uterus?", ["Gutartiger Tumor der glatten Muskulatur", "Bösartiger Tumor der Gebärmutter", "Eine Entzündung", "Eine Zyste"], [0], "", 210)
S("Warum kann ein gutartiges Meningeom Probleme machen?", ["Es drückt auf das Gehirn", "Es metastasiert", "Es blutet immer", "Es ist ansteckend"], [0], "Symptome: Kopfschmerz, Schwindel, Krampfanfälle.", 211)
S("*Was ist eine Dysplasie?", ["Noch reversible Zellveränderung mit Differenzierungsverlust – fakultative Präkanzerose", "Irreversible Entdifferenzierung", "Ein Karzinom mit Metastasen", "Eine Entzündung"], [0],
  "z. B. Plattenepitheldysplasie der Cervix, Dickdarmadenom.", 212)
S("*Was ist eine Anaplasie?", ["Irreversible Entdifferenzierung – wichtigstes morphologisches Kennzeichen der Malignität", "Reversible Zellveränderung", "Zellvergrößerung", "Ersatz eines Zelltyps durch einen anderen"], [0], "", 216)
S("Welche Zellbefunde sprechen für Anaplasie?", ["Vergrößerte, vielgestaltige Zellkerne", "Irreguläre Zellformen", "Gleichmäßige kleine Kerne", "Normale Schichtung"], [0, 1], "Außerdem atypische Färbbarkeit.", 216)
S("Wofür wird der Pap-Abstrich eingesetzt?", ["Früherkennung von Dysplasien des Gebärmutterhalses", "Diagnose von Diabetes", "Bestimmung der Blutgruppe", "Messung des Blutdrucks"], [0], "Schwere Dysplasie = letzter Schritt vor dem invasiven Karzinom.", 214)
S("*Was bedeutet Grading Grad III?", ["Entdifferenzierter, anaplastischer, aggressiver Tumor", "Gut differenzierter, langsam wachsender Tumor", "Gutartiger Tumor", "Tumor ohne Metastasen"], [0],
  "Grad I = gut differenziert, ähnelt dem Ursprungsgewebe.", 218)
S("*Was beschreibt das Grading?", ["Den Differenzierungsgrad bzw. die Aggressivität eines malignen Tumors", "Die Ausbreitung (Größe, Lymphknoten, Metastasen)", "Die Lage im Körper", "Das Alter des Patienten"], [0],
  "Die Ausbreitung beschreibt das TNM-Staging.", 218)
S("Was ist ein okkultes Karzinom?", ["Metastasen gefunden, Primärtumor noch unbekannt", "Zufallsbefund bei der Obduktion ohne Symptome", "Klinisch diagnostiziertes Karzinom mit bekanntem Primärtumor", "Gutartiger Tumor"], [0], "", 220)
S("Was ist ein latentes Karzinom?", ["Symptomloser Zufallsbefund bei der Obduktion", "Karzinom mit unbekanntem Primärtumor", "Karzinom im Endstadium", "Karzinom in situ"], [0], "z. B. kleines Prostatakarzinom.", 220)
S("*Was sind Onkogene?", ["Mutierte, dauerhaft aktive Gene, die die Zellteilung antreiben", "Gene, die geschädigte Zellen in die Apoptose schicken", "Gene des Immunsystems", "Gene für Blutgruppen"], [0], "Entstehen aus Protoonkogenen durch Mutation.", 223)
S("*Was ist die Aufgabe von Tumorsuppressorgenen?", ["Unkontrollierte Teilung geschädigter Zellen unterdrücken", "Zellteilung dauerhaft antreiben", "Bakterien abwehren", "Hormone bilden"], [0], "Bei Defekt fällt die Kontrolle aus.", 223)
S("Was sind Protoonkogene?", ["Normale Gene (u. a. für Wachstum), die durch Mutation zu Onkogenen werden können", "Virusgene", "Defekte Reparaturgene", "Gene für Totenflecke"], [0], "", 223)
S("Welche zählen zu den krebserzeugenden Noxen (Karzinogenen)?", ["Chronische Gewebsreizung", "Bestimmte Viren (z. B. HPV)", "Vitamin C", "Ausreichend Schlaf"], [0, 1], "Außerdem Strahlen und genetische Defekte.", 226)
S("*Welches Virus kann ein Cervixkarzinom verursachen?", ["Humane Papillomaviren (Hochrisiko-HPV)", "Influenzavirus", "Hepatitis-A-Virus", "Masernvirus"], [0], "Dagegen gibt es eine Impfung.", 226)
S("Welcher Stoff ist ein spezieller Risikofaktor für das Pleuramesotheliom?", ["Asbest", "Zucker", "Kochsalz", "Koffein"], [0], "", 228)
S("Was ist die familiäre adenomatöse Polyposis (FAP)?", ["Erbliche APC-Mutation mit vielen Darmpolypen, die bösartig werden", "Eine Lungenerkrankung", "Eine Virusinfektion", "Eine Hauterkrankung"], [0],
  "Im jungen Erwachsenenalter wird der ganze Dickdarm entfernt.", 229)
S("*Wie heißt ein bösartiger Tumor des Epithels?", ["Karzinom", "Sarkom", "Lipom", "Lymphom"], [0], "z. B. Dickdarm-, Mamma-, Magenkarzinom.", 233)
S("*Wie heißt ein bösartiger mesenchymaler Tumor (Binde-/Stützgewebe)?", ["Sarkom", "Karzinom", "Adenom", "Naevus"], [0], "", 235)
S("Wie heißt der gutartige Tumor des Fettgewebes?", ["Lipom", "Liposarkom", "Fibrom", "Myom"], [0], "Bösartig: Liposarkom.", 235)
S("Wie heißt der bösartige Tumor des Knochengewebes?", ["Osteosarkom", "Osteom", "Chondrom", "Fibrom"], [0], "", 235)
S("Wie heißt der gutartige Tumor des Knorpelgewebes?", ["Chondrom", "Chondrosarkom", "Osteom", "Myom"], [0], "", 235)
S("Welche Tumoren sind bösartig?", ["Fibrosarkom", "Myosarkom", "Lipom", "Osteom"], [0, 1], "", 235)
S("Woran erkennt man ein Lipom?", ["Scharf umschrieben, zarte Kapsel, unter der Haut verschiebbar", "Diffus infiltrierend", "Immer schmerzhaft", "Metastasiert früh"], [0], "", 236)
S("Warum sind Lymphome meist nicht chirurgisch entfernbar?", ["Sie breiten sich im lymphatischen Gewebe aus, das überall verteilt ist", "Weil sie zu klein sind", "Weil sie gutartig sind", "Weil sie nur im Gehirn liegen"], [0], "", 237)
S("Was ist ein Meningeom?", ["Tumor der Hirnhäute", "Tumor der Nervenzellen", "Tumor der Glia", "Tumor der Haut"], [0], "Gliome = Zwischensubstanz; Neurinome = periphere Nervenscheiden.", 238)
S("Was ist ein Gliom?", ["Tumor der Zwischensubstanz (Glia) des Nervensystems", "Tumor der Hirnhäute", "Tumor der Muskulatur", "Tumor des Knochens"], [0], "", 238)
S("Was unterscheidet Naevus und Melanom?", ["Naevus (Muttermal) ist gutartig", "Melanom ist bösartig und metastasiert früh", "Naevus metastasiert früh", "Melanom ist immer harmlos"], [0, 1], "Melanom: Sonnenschädigung der Haut.", 240)
S("Was sind Metastasen?", ["Räumlich vom Primärtumor getrennte Tochtergeschwülste", "Der ursprüngliche Tumor", "Gutartige Tumoren", "Entzündungsherde"], [0], "Auch „Filiae“ oder „Secundaria“.", 242)
S("Wohin metastasiert ein Tumor lymphogen zuerst?", ["In die regionären Lymphknoten", "Direkt ins Gehirn", "In die Knochen", "In die Haut"], [0], "Dann weitere Lymphknoten, über den Ductus thoracicus ins Blut.", 246)
S("*Ein Bronchuskarzinom metastasiert nach dem arteriellen Typ typischerweise in …", ["Gehirn und Knochen", "Leber und Nebennieren", "Nur in die Lunge", "Nur in den Darm"], [0, 1], "Lunge → linkes Herz → großer Kreislauf.", 250)
S("*Ein Dickdarmkarzinom metastasiert nach dem Pfortadertyp zuerst in …", ["die Leber", "das Gehirn", "die Knochen", "die Haut"], [0], "Magen-Darm-Trakt → Pfortader → Leber → dann Lunge.", 256)
S("*Welche Tumoren metastasieren nach dem Hohlvenen-(Cava-)Typ zuerst in die Lunge?", ["Nierenkarzinom", "Mammakarzinom", "Dickdarmkarzinom", "Magenkarzinom"], [0, 1], "V. cava → rechtes Herz → Lunge. Auch Leberkarzinom.", 253)
S("Was bedeutet Metastasierung per continuitatem?", ["Direktes Durchwachsen in benachbarte Strukturen", "Ausbreitung über Lymphwege", "Ausbreitung über die Blutbahn", "Abtropfen in seröse Höhlen"], [0], "", 259)
S("Was ist eine Carcinosis peritonei?", ["Herdförmige Aussaat von Tumorzellen im Bauchfell", "Ein Bauchspeicheldrüsenkrebs", "Eine Entzündung der Leber", "Ein gutartiger Bauchtumor"], [0], "", 260)
S("*Wofür steht das „N“ in der TNM-Klassifikation?", ["Lymphknotenbefall (Nodus)", "Nekrose", "Normale Zellen", "Nervenbefall"], [0], "T = Tumorausdehnung, M = Fernmetastasen.", 264)
S("*Was bedeutet pT3N1M1?", ["Fortgeschrittener Tumor mit Lymphknoten- und Fernmetastasen", "Kleiner Tumor ohne Metastasen", "Gutartiger Tumor", "Tumor in situ"], [0], "", 264)
S("Was ist ein Carcinoma in situ?", ["Präinvasives Karzinom, das die Basalmembran nicht durchbricht", "Karzinom mit Fernmetastasen", "Gutartiger Tumor", "Entzündung"], [0], "", 265)
S("Was ist Tumorkachexie?", ["Starke Abmagerung von Muskel- und Fettgewebe", "Gewichtszunahme", "Fieber", "Haarausfall"], [0], "", 269)
S("Welche Folgen können maligne Tumoren haben?", ["Stenose/Verschluss von Hohlorganen (z. B. Darmverschluss)", "Erhöhte Infektanfälligkeit", "Verbesserte Abwehr", "Gewichtszunahme durch Muskelaufbau"], [0, 1], "Außerdem Perforation, Gefäßarrosion, Anämie.", 269)

# ---------------------------------------------------------------- 7 Kreislaufstörungen
K("7")
S("Was ist ein Ödem?", ["Einlagerung von Flüssigkeit aus dem Gefäßsystem ins Gewebe", "Eine Blutung", "Ein Blutgerinnsel", "Eine Eiteransammlung"], [0], "Nach Fingerdruck bleibt eine Delle.", 278)
S("*Welche Folge hat eine Linksherzinsuffizienz?", ["Lungenödem", "Beinödeme", "Aszites durch Leberzirrhose", "Hungerödeme"], [0], "Rechtsherzinsuffizienz → Ödeme im großen Kreislauf (Beine).", 281)
S("*Welche Folge hat eine Rechtsherzinsuffizienz?", ["Ödeme im großen Kreislauf, z. B. Beinödeme", "Lungenödem", "Hirnödem", "Keine Ödeme"], [0], "", 281)
S("Wodurch entstehen „Hungerödeme“?", ["Erniedrigung des onkotischen Drucks durch Eiweißmangel", "Erhöhter Blutdruck", "Lymphabflussstörung", "Entzündung"], [0], "", 284)
S("Welche Ursachen führen über Eiweißmangel zu Ödemen?", ["Zu geringe Proteinsynthese in der Leber", "Proteinverlust über die Niere", "Zu viel Eiweiß in der Nahrung", "Bluthochdruck"], [0, 1], "", 284)
S("Wovon hängt der osmotische Druck ab?", ["Von der Natriumkonzentration", "Von der Herzfrequenz", "Von der Körpergröße", "Von der Blutgruppe"], [0], "", 285)
S("Was ist ein iatrogenes Lymphödem?", ["Lymphödem durch ärztliche Maßnahmen, z. B. Entfernung oder Bestrahlung von Lymphknoten", "Angeborenes Lymphödem", "Lymphödem durch Parasiten", "Lymphödem bei Sport"], [0], "", 291)
S("*Was ist ein Hydrops?", ["Flüssigkeitsansammlung in präformierten Körperhöhlen", "Blut im Gewebe", "Eiter in der Haut", "Luft in der Lunge"], [0], "Hydrothorax, Hydroperikard, Aszites.", 287)
S("Was ist ein Aszites?", ["Flüssigkeitsansammlung in der Bauchhöhle", "Flüssigkeit im Herzbeutel", "Flüssigkeit im Pleuraraum", "Blut im Gelenk"], [0], "", 287)
S("Was ist ein Hydrothorax?", ["Pleuraerguss (Flüssigkeit in der Brusthöhle)", "Flüssigkeit in der Bauchhöhle", "Blut im Herzbeutel", "Luft im Bauch"], [0], "", 287)
S("Welche Ursachen hat ein Lungenödem?", ["Linksherzinsuffizienz", "Schock (Schocklunge)", "Rechtsherzinsuffizienz allein", "Jodmangel"], [0, 1], "Außerdem Urämie, Lungenentzündung.", 296)
S("Warum ist ein Hirnödem lebensbedrohlich?", ["Es kann zur Hirnkompression mit Atemlähmung führen", "Es verursacht Fieber", "Es führt zu Durchfall", "Es ist ansteckend"], [0], "", 299)
S("Was ist eine Thrombose?", ["Bildung eines Blutgerinnsels in einer Vene oder Arterie", "Verschleppung eines Gerinnsels", "Blutung ins Gewebe", "Flüssigkeit im Gewebe"], [0], "", 300)
S("*Welche Faktoren gehören zur Virchow-Trias der Thromboseentstehung?", ["Gefäßwandschaden", "Verlangsamte Strömung", "Gute Durchblutung", "Niedriger Hämatokrit"], [0, 1], "Dritter Faktor: veränderte Blutzusammensetzung (Humoralfaktor).", 302)
S("Was zählt zum Humoralfaktor der Thrombose?", ["Exsikkose", "Polyglobulie", "Atherosklerotische Plaque", "Bettlägerigkeit"], [0, 1], "Plaque = Gefäßwandfaktor, Bettlägerigkeit = Zirkulationsfaktor.", 302)
S("Was ist eine Embolie?", ["Verschleppung eines Embolus auf dem Blutweg und Steckenbleiben in einem kleineren Gefäß", "Bildung eines Gerinnsels an Ort und Stelle", "Eine Blutung", "Ein Ödem"], [0], "", 307)
S("Welche Arten von Embolie gibt es?", ["Fettembolie", "Luftembolie", "Lichtembolie", "Schallembolie"], [0, 1], "Außerdem Thrombo-, Fruchtwasser-, Tumor-, Fremdkörperembolie.", 307)
S("*Wohin führt eine venöse Embolie aus den Beinvenen?", ["In die Lungenarterien – Pulmonalembolie", "Ins Gehirn", "In die Nieren", "In die Beinarterien"], [0], "Beinvenen → V. cava → rechtes Herz → Lunge.", 308)
S("*Wohin kann eine arterielle Embolie aus dem linken Herzen führen?", ["Ins Gehirn (Hirninfarkt)", "In Milz und Nieren", "In die Lungenarterien", "In die Beinvenen"], [0, 1], "Ziel: Hirn, Milz, Nieren, Mesenterialarterien, Beinarterien → Infarkt.", 311)
S("Was ist Schock?", ["Zirkulationsinsuffizienz – Missverhältnis zwischen Blutvolumen und Gefäßkapazität", "Eine psychische Reaktion", "Ein Herzstillstand", "Ein hoher Blutdruck"], [0], "", 317)
S("*Welche Schockform entsteht durch Blutverlust oder Verbrennungen?", ["Hypovolämischer Schock", "Kardiogener Schock", "Anaphylaktischer Schock", "Neurogener Schock"], [0], "Hämorrhagischer Schock = hypovolämisch durch Blutverlust.", 319)
S("*Welche Ursachen hat ein kardiogener Schock?", ["Myokardinfarkt", "Perikardtamponade", "Bienenstich-Allergie", "Durchfall"], [0, 1], "Auch Myokarditis, Pulmonalembolie.", 320)
S("*Wodurch entsteht der anaphylaktische Schock?", ["IgE-vermittelte allergische Reaktion mit Histaminfreisetzung", "Bakterielle Toxine", "Blutverlust", "Schädel-Hirn-Trauma"], [0], "Gefäßerweiterung in der Peripherie.", 325)
S("Welche Schockform hat eine hohe Letalität und entsteht bei bakterieller Sepsis?", ["Septisch-toxischer Schock", "Neurogener Schock", "Hypovolämischer Schock", "Anaphylaktischer Schock"], [0], "", 323)
S("Wodurch entsteht ein neurogener Schock?", ["Schädigung der Vasomotoren, z. B. Schädel-Hirn-Trauma", "Blutverlust", "Allergie", "Herzinfarkt"], [0], "", 326)
S("*Was kennzeichnet Schockstadium I (Zentralisation)?", ["Blasse, kühle Haut, kalter Schweiß, Tachykardie", "Blutdruck wird noch aufrechterhalten", "Blutdruckabfall und Ohnmacht", "Koma und Pulslosigkeit"], [0, 1], "Herz und Gehirn werden noch versorgt.", 327)
S("*Was kennzeichnet Schockstadium II (Dezentralisation)?", ["Blutdruckabfall bei steigender Pulsfrequenz", "Drohendes Multiorganversagen", "Blutdruck normal", "Warme, rosige Haut"], [0, 1], "", 328)
S("Was kennzeichnet Schockstadium III?", ["Irreversibler Schock mit Zyanose, Pulslosigkeit, Koma", "Zentralisation", "Leichte Blässe", "Erhöhter Blutdruck"], [0], "", 330)
S("*Wie berechnet sich der Schockindex?", ["Pulsfrequenz geteilt durch systolischen Blutdruck", "Systolischer Blutdruck geteilt durch Puls", "Puls mal Atemfrequenz", "Diastolischer durch systolischen Blutdruck"], [0],
  "Normal ≤ 0,5; beginnender Schock ab 1,0; schwerer Schock > 1,5.", 329)
S("Ein Schockindex von 1,6 bedeutet …", ["Schwerer Schock", "Normalbefund", "Beginnender Schock", "Hypertonie"], [0], "", 329)
S("Wie heißt die Schocklunge?", ["ARDS (adult respiratory distress syndrome)", "COPD", "Pneumothorax", "Asthma"], [0], "Schockfolge: Multiorganversagen.", 331)
S("Was sind Petechien?", ["Punktförmige Blutungen", "Flächenhafte Blutungen", "Geschlossene Blutmassen", "Blutungen aus der Nase"], [0], "", 338)
S("Was ist ein Hämatom?", ["Dreidimensionale, geschlossene Blutansammlung im Gewebe", "Punktförmige Blutung", "Flächige Blutung", "Bluthusten"], [0], "", 338)
S("Was sind Suffusionen?", ["Flächenhaft ausgebreitete Blutungen", "Punktförmige Blutungen", "Blutungen ins Gelenk", "Bluterbrechen"], [0], "", 338)
S("Was ist Epistaxis?", ["Nasenbluten", "Bluthusten", "Bluterbrechen", "Blut im Harn"], [0], "", 342)
S("Wie sieht Blut bei Hämoptysen (Bluthusten) aus?", ["Hellrot und schaumig (mit Luft gemischt)", "Schwarz und kaffeesatzartig", "Teerartig", "Dunkelbraun und fest"], [0], "Ursachen: Lungeninfarkt, Tuberkulose, Bronchuskarzinom.", 344)
S("*Wie sieht Bluterbrechen aus einer Magenblutung aus?", ["Schwarz, kaffeesatzartig", "Hellrot, schaumig", "Klar", "Grün"], [0], "Aus dem Ösophagus eher blaurot.", 345)
S("*Was ist Meläna?", ["Schwarzer Teerstuhl durch Blutung im oberen Verdauungstrakt", "Hellrotes Blut im Stuhl aus dem Enddarm", "Blut im Harn", "Nasenbluten"], [0], "", 350)
S("Was ist Hämatochezie?", ["Blutige Stühle aus unterem Dickdarm/Rektum", "Teerstuhl", "Bluterbrechen", "Bluthusten"], [0], "Ursachen: Karzinom, Divertikel, Hämorrhoiden.", 352)
S("Was ist Hämaturie?", ["Blut im Harn", "Blut im Stuhl", "Blut im Gelenk", "Blut im Auswurf"], [0], "", 359)
S("Was ist ein Hämarthros?", ["Blutung in ein Gelenk", "Blutung in den Herzbeutel", "Blutung in die Brusthöhle", "Blutung in die Bauchhöhle"], [0], "Hämatothorax = Brusthöhle, Hämatoperikard = Herzbeutel.", 362)
S("Was ist eine Menorrhagie?", ["Zu lange und zu starke Regelblutung", "Zu seltene Regelblutung", "Blutung außerhalb der Regel", "Zu häufige Regelblutung"], [0], "Metrorrhagie = Blutung außerhalb der Regel.", 361)
S("Was ist eine hämorrhagische Diathese?", ["Erhöhte Blutungsneigung", "Erhöhte Thromboseneigung", "Eine Form des Schocks", "Ein Ödem"], [0], "Koagulopathien und Thrombozytopathien (z. B. durch Aspirin).", 365)
S("Welche Folge hat ein langsamer, wiederholter Blutverlust?", ["Blutungsanämie", "Hypovolämischer Schock", "Thrombose", "Ödem"], [0], "Rascher, hoher Verlust → hypovolämischer Schock.", 366)
S("Welche Folge hat eine chronische arterielle Mangeldurchblutung?", ["Parenchymatrophie (z. B. Schrumpfniere)", "Akute Nekrose", "Blutung", "Hyperplasie"], [0], "", 370)
S("Was ist eine TIA?", ["Transitorische ischämische Attacke – vorübergehende Durchblutungsstörung im Gehirn", "Ein Herzinfarkt", "Eine Thrombose im Bein", "Ein Tumor"], [0], "", 371)
S("Wozu führt eine länger dauernde Ischämie im Versorgungsgebiet einer verschlossenen Arterie?", ["Ischämischer Infarkt (Nekrose)", "Hyperplasie", "Ödem", "Hypertrophie"], [0], "Ursachen: Thrombose, Embolie, Gefäßligatur.", 372)
S("Wie sieht ein Organ bei venöser Stauung aus?", ["Vergrößert, schwer, dunkelblaurot", "Klein und blass", "Gelb und weich", "Unverändert"], [0], "", 373)
S("Was ist eine hämorrhagische Infarzierung?", ["Blutige Gewebszerstörung nach plötzlichem Verschluss einer großen Organvene", "Arterieller Infarkt ohne Blutung", "Gutartiger Tumor", "Ödem"], [0], "z. B. Mesenterialvenen, Hirnsinus.", 375)

# ---------------------------------------------------------------- 8 Stoffwechsel & Gefäße
K("8")
S("Was ist Arteriosklerose?", ["Systemische Verhärtung der Arterienwand mit Ablagerungen", "Venenentzündung", "Ein Herzklappenfehler", "Eine Blutgerinnungsstörung"], [0], "", 377)
S("*Welche sind Risikofaktoren der Arteriosklerose?", ["Hyperlipidämie", "Diabetes mellitus", "Untergewicht", "Viel Bewegung"], [0, 1], "Außerdem Hypertonie, Rauchen, Bewegungsmangel, Adipositas.", 378)
S("Womit beginnt die Entstehung der Arteriosklerose?", ["Endothelzellschaden der Arterienintima", "Verkalkung der Venen", "Blutung in die Wand", "Bakterieller Infektion"], [0], "Dann Einwanderung von Monozyten, Entzündung, Cholesterin → atheromatöse Plaque.", 379)
S("Wo entsteht Arteriosklerose bevorzugt?", ["An Gefäßteilungsstellen und Abgängen", "An Krümmungen im Gefäßverlauf", "In Kapillaren", "In Venenklappen"], [0, 1], "Auch bei hartem Widerlager (Wirbelsäule).", 380)
S("Welche Folgekrankheiten hat die Arteriosklerose?", ["Myokardinfarkt", "Hirninfarkt", "Laktoseintoleranz", "Struma"], [0, 1], "Außerdem Mesenterialinfarkt, Gangrän, Claudicatio, Organatrophie.", 384)
S("*Ab welchem Nüchternblutzucker liegt Diabetes mellitus vor?", ["≥ 126 mg/dl (7 mmol/l)", "≥ 100 mg/dl", "≥ 200 mg/dl", "≥ 90 mg/dl"], [0], "oGTT oder Zufallswert ≥ 200 mg/dl.", 385)
S("*Was ist die Ursache von Diabetes Typ I?", ["Autoimmunzerstörung der Beta-Zellen im Pankreas", "Insulinresistenz", "Zu viel Insulin", "Jodmangel"], [0], "„Juveniler Diabetes“.", 386)
S("*Was ist die Ursache von Diabetes Typ II?", ["Insulinresistenz durch ständig erhöhte Glukose- und Insulinspiegel", "Autoimmunzerstörung der Beta-Zellen", "Virusinfektion", "Leberzirrhose"], [0], "„Altersdiabetes“.", 386)
S("Was bedeuten Polyurie und Polydipsie?", ["Viel Harn und viel Durst", "Wenig Harn und wenig Durst", "Blut im Harn und Fieber", "Zucker im Stuhl"], [0], "Weitere Symptome: Hyperglykämie, Glukosurie.", 388)
S("Ab welchem Blutzucker wird Glukose im Harn ausgeschieden (Glukosurie)?", ["Über ca. 150 mg%", "Über 50 mg%", "Über 500 mg%", "Nie"], [0], "", 388)
S("Was ist die diabetische Mikroangiopathie?", ["Verdickung und Einengung kleiner Gefäße", "Verkalkung großer Arterien", "Bildung von Krampfadern", "Herzklappenentzündung"], [0], "Folgen: Retinopathie (Auge), Nephropathie (Niere).", 391)
S("Welche Folgekrankheiten hat Diabetes mellitus?", ["Polyneuropathie (Gefühllosigkeit)", "Retinopathie und Nephropathie", "Schutz vor Infektionen", "Niedriger Blutdruck"], [0, 1], "Außerdem verstärkte Atherosklerose, Gangrän, Infekte.", 391)
S("Wie entsteht das ketoazidotische Koma?", ["Absoluter Insulinmangel → Fettabbau → Ketonkörper → Azidose", "Zu viel Insulin", "Zu viel Wasser", "Durch Bakterien"], [0], "Hyperosmolares Koma: extrem hoher Blutzucker, Flüssigkeit aus den Zellen.", 396)
S("*Wie viel Prozent der Hypertoniker haben eine primäre (essentielle) Hypertonie?", ["90–95 %", "10–20 %", "50 %", "100 %"], [0], "Ätiologie unklar, Ausschlussdiagnose.", 399)
S("Was sind Ursachen einer sekundären Hypertonie?", ["Nierenerkrankungen (Renin-Angiotensin-Aldosteron)", "Hormonelle Ursachen (z. B. Nebennierentumor)", "Unbekannte Ursache", "Zu viel Schlaf"], [0, 1], "", 401)
S("Was ist das metabolische Syndrom („tödliches Quartett“)?", ["Insulinresistenz, Hypertonie, Fettstoffwechselstörung, abdominelle Adipositas", "Fieber, Husten, Schnupfen, Kopfschmerz", "Vier Arten von Krebs", "Vier Schockformen"], [0], "", 413)
S("Was gehört zum metabolischen Syndrom?", ["Erniedrigtes HDL", "Erhöhte Triglyzeride", "Niedriger Blutdruck", "Untergewicht"], [0, 1], "", 413)
S("Was ist ein Cor pulmonale?", ["Hypertrophie und Dilatation des rechten Ventrikels", "Linksherzhypertrophie", "Lungenentzündung", "Lungenkrebs"], [0], "Folge einer pulmonalen Hypertonie.", 417)
S("*Was ist eine typische Ursache einer portalen Hypertension?", ["Leberzirrhose", "Nierensteine", "Asthma", "Diabetes"], [0], "Normaler Pfortaderdruck 5–10 mmHg.", 419)
S("*Welche Folgen hat die portale Hypertension?", ["Ösophagusvarizen", "Aszites und Splenomegalie", "Hypothyreose", "Lungenödem"], [0, 1], "Außerdem Caput medusae.", 420)
S("Ab welchem Wert spricht man von Hypotonie?", ["Unter 105/60 mmHg", "Unter 140/90 mmHg", "Unter 120/80 mmHg", "Unter 80/40 mmHg"], [0], "", 422)
S("*Woher stammt das Bilirubin?", ["Aus dem Abbau der roten Blutkörperchen", "Aus der Nahrung", "Aus der Schilddrüse", "Aus den Muskeln"], [0], "", 424)
S("Ab welcher Bilirubinkonzentration wird ein Ikterus meist sichtbar?", ["Ab ca. 2 mg/dl", "Ab 0,1 mg/dl", "Ab 20 mg/dl", "Ab 100 mg/dl"], [0], "Hyperbilirubinämie ab > 1 mg/dl.", 423)
S("*Was ist ein prähepatischer Ikterus?", ["Gelbsucht durch vermehrte Hämolyse", "Gelbsucht durch Gallenstein", "Gelbsucht durch Leberzirrhose", "Gelbsucht durch Sonnenbrand"], [0], "", 427)
S("*Was ist ein posthepatischer Ikterus?", ["Gelbsucht durch Abflussbehinderung in den Gallengängen (Stein, Tumor)", "Gelbsucht durch Hämolyse", "Gelbsucht durch Hepatitis", "Gelbsucht beim Neugeborenen immer"], [0], "Hepatisch: Zirrhose, Hepatitis, Vergiftung.", 427)
S("Welche Symptome hat ein Ileus?", ["Krampfartige Bauchschmerzen", "Stuhlerbrechen (Miserere), kein Stuhl", "Durchfall", "Bluthusten"], [0, 1], "", 428)
S("Was ist ein Bridenileus?", ["Mechanischer Darmverschluss durch bindegewebige Verwachsungen", "Lähmung der Darmmuskulatur", "Darmverdrehung", "Darmkrebs"], [0], "Spätfolge von Peritonitis oder Bauch-OPs.", 430)
S("Was ist ein paralytischer Ileus?", ["Darmverschluss durch Lähmung der Darmwandmuskulatur", "Verschluss durch Verwachsungen", "Verschluss durch Fremdkörper", "Verschluss durch Tumor"], [0], "Reaktion auf Entzündung, Durchblutungsstörung, Toxine.", 432)


# ---------------------------------------------------------------- Ausgabe + Prüfung
fehler = []
for i, f in enumerate(fragen, 1):
    f["id"] = f"pat-{i:03d}"
    if len(f["optionen"]) < 3 or not f["richtig"] or max(f["richtig"]) >= len(f["optionen"]):
        fehler.append(f"{f['id']}: mc ungültig")
    if not 2 <= f["seite"] <= 435:
        fehler.append(f"{f['id']}: Seite {f['seite']}")
fehler += [f"doppelt: {t}" for t, n in collections.Counter(f["frage"] for f in fragen).items() if n > 1]
fehler += [f"Kapitel ohne Frage: {k}" for k, _, _ in KAPITEL if not any(f["kapitel"] == k for f in fragen)]
if fehler:
    print("\n".join(fehler)); sys.exit(1)

reihenfolge = ["id", "kapitel", "typ", "frage", "optionen", "richtig", "antwortKurz", "erklaerung", "seite", "prio"]
ziel.mkdir(exist_ok=True)
(ziel / "fragen.json").write_text("[\n" + ",\n".join(json.dumps({k: f[k] for k in reihenfolge}, ensure_ascii=False) for f in fragen) + "\n]\n", encoding="utf-8")
meta = {"id": "patho", "titel": "Pathologie – neu erstellte Fragen", "kurz": "PATHO", "datum": "2026-11-30", "aktiv": True,
        "form": "schriftlich: MC-Test (Single und Multiple Choice)",
        "kapitel": [{"nr": n, "titel": t} for n, t, _ in KAPITEL],
        "gruppen": [{"nr": n, "titel": t, "thema": th, "praefix": [n]} for n, t, th in KAPITEL]}
(ziel / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

c = collections.Counter
print(len(fragen), "Fragen | Single:", sum(len(f["richtig"]) == 1 for f in fragen), "| Multiple:", sum(len(f["richtig"]) > 1 for f in fragen))
print("Kapitel:", dict(c(f["kapitel"] for f in fragen)), "| prio hoch:", sum(f["prio"] == "hoch" for f in fragen))
