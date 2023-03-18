from sys import argv
from sys import exit


# ERROR MANAGEMENT
if len(argv) > 2:
    print("Erreur, vous avez saisi trop d'arguments.")
    exit(1)
if len(argv) < 2:
    print("Erreur, vous devez ecrire quelque chose.")
    exit(1)
nombre = argv[1]
try:
    nombre = int(nombre)
except ValueError:
    print("Erreur, vous devez saisir un nombre entier.")


# FUNCTIONS
def racine_carre(x):
    y = x ** 0.5
    if y == int(y):
        y = int(y)
        print(f"{y} est la racine carre de {x}")
    else:
        y_float = round(float(y), ndigits=2)
        y = int(y)
        print()
        print(f"{y} est la racine carre la plus proche de {x}")
        print()
        print(f"Plus precisement, la racine de {x} est {y_float}")
    return y


# RESULT
racine_carre(nombre)