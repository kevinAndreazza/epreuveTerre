from sys import argv
from sys import exit

if len(argv) != 4:
    print("Erreur vous devez saisir 3 nombres entiers positifs.")
    exit(1)

nombre_1 = argv[1]
nombre_2 = argv[2]
nombre_3 = argv[3]

try:
    nombre_1 = int(nombre_1)
    nombre_2 = int(nombre_2)
    nombre_3 = int(nombre_3)
except ValueError:
    print("ERREUR ! Vous devez saisir une suite de 3 nombres entiers positifs")
    exit(1)
except TypeError:
    print("ERREUR ! Vous devez saisir 3 nombres entiers positifs.")

# créer une liste avec les nombres et une liste vide
liste_de_base = [nombre_1, nombre_2, nombre_3]
liste_nombres = []

# plus petit nombre des trois
if nombre_1 < nombre_2 and nombre_1 < nombre_3:
    liste_nombres.append(nombre_1)
if nombre_2 < nombre_1 and nombre_2 < nombre_3:
    liste_nombres.append(nombre_2)
if nombre_3 < nombre_1 and nombre_3 < nombre_2:
    liste_nombres.append(nombre_3)

# plus grand nombre des 3
if nombre_1 > nombre_2 > nombre_3:
    liste_nombres.append(nombre_1)
if nombre_2 > nombre_1 and nombre_2 > nombre_3:
    liste_nombres.append(nombre_2)
if nombre_3 > nombre_1 and nombre_3 > nombre_2:
    liste_nombres.append(nombre_3)

# nombre restant
for n in liste_de_base:
    if n not in liste_nombres:
        print(n)



