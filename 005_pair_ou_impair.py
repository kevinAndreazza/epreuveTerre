# FONCTION
def est_pair(x):
    if x % 2 == 1:
        print("Le nombre est impair")
    else:
        print("Le nombre est pair")
    return


nombre = input("Saisir un nombre entier : ")
# Concaténer les caractères en argument et ranger les arguments dans une liste
argument = ""; arguments = []
for caractere in nombre:
    if caractere != " ":
        argument += caractere
    else:
        arguments.append(argument)
        argument = ""
arguments.append(argument)

# Gérer les erreurs
if len(arguments) > 1:
    print("Vous avez saisi trop de caractère.")
    exit(1)
elif len(arguments) < 1:
    print("Vous n'avez pas saisi suffisamment d'argument.")
    exit(1)
else:
    nombre = arguments[0]
    try:
        nombre = int(nombre)
    except ValueError:
        print("Vous devez saisir un nombre entier.")
        exit(1)

# déterminer si le nombre est pair
est_pair(nombre)