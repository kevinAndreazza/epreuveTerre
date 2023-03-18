from sys import argv
from sys import exit


# ERREUR
if len(argv) > 2:
    print("Vous devez saisir un nombre entier.")
    exit(1)
if len(argv) < 2:
    print("Vous devez saisir un nombre entier.")
    exit(1)

arg = argv[1]

try:
    arg = int(arg)
except ValueError:
    print("Vous devez saisir un nombre entier.")
    exit(1)


# FONCTIONS
def est_premier(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# RESULTAT
if est_premier(arg):
    print(f"Le nombre {arg} est premier.")
else:
    print(f"Le nombre {arg} n'est pas premier.")