from sys import argv
from sys import exit


if len(argv) < 3:
    print("Erreur, trop peu d'argument saisis.")
    exit(1)
if len(argv) > 3:
    print("Erreur, trop d'argument saisis.")
    exit(1)

nombre = argv[1]
exposant = argv[2]


try:
    nombre = int(argv[1])
    exposant = int(argv[2])
    if exposant < 0:
        print("Erreur, l'exposant doit etre un nombre entier positif.")
        exit(1)
except ValueError:
    print("Erreur, vous devez saisir 2 nombres entier.")
    exit(1)

nombre = int(nombre)
exposant = int(exposant)
resultat = nombre ** exposant
print(resultat)