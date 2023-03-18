from sys import argv
from sys import exit


# ERREURS
if len(argv) != 2:
    print("Vous devez saisir l'heure au format hh:mm")
    exit(1)

arg = argv[1]

if len(arg) != 5:
    print("Vous devez saisir l'heure au format hh:mm")
    exit(1)

# VARIABLES
h1 = arg[0]
h2 = arg[1]
hh = f"{h1}{h2}"
separateur = ":"
mm = f"{arg[-2]}{arg[-1]}"
am_pm = ""
horloge_24 = f"{hh}{separateur}{mm}"
horloge_12 = f"{hh}{separateur}{mm}{am_pm}"
heure_reference = horloge_24[0:2]

# ERREUR
try:
    heure_reference = int(heure_reference)
    hh = int(hh)
except ValueError:
    print("Vous devez saisir l'heure au format hh:mm")
    exit(1)


# CONDITIONS
if 12 < heure_reference < 24:
    hh = hh - 12
    am_pm = "PM"
    horloge_12 = f"{hh}{separateur}{mm}{am_pm}"
    if len(str(hh)) == 1:
        am_pm = "PM"
        horloge_12 = f"0{hh}{separateur}{mm}{am_pm}"
    print(horloge_12)
    exit(0)

if 1 <= heure_reference < 12:
    am_pm = "AM"
    horloge_12 = f"{horloge_24}{am_pm}"
    print(horloge_12)
    exit(0)

if heure_reference == 12:
    am_pm = "PM"
    horloge_12 = f"{horloge_24}{am_pm}"
    print(horloge_12)
    exit(0)

heure_reference = str(heure_reference)
if heure_reference[0] == "0" or heure_reference[1] == "4":
    am_pm = "AM"
    horloge_12 = f"12:00{am_pm}"
    print(horloge_12)
    exit(0)