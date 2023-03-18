user_input = input("Saisir 2 nombres entier : ")

argument = ""; arguments = []
for caractere in user_input:
    if caractere != " ":
        argument += caractere
    else:
        arguments.append(argument)
        argument = ""
arguments.append(argument)

if len(arguments) > 2:
    print("Vous avez saisi trop d'argument")
    exit(1)
elif len(arguments) <= 1:
    print("Vous n'avez pas saisi assez d'argument.")
    exit(1)

nombre_1 = arguments[0]
nombre_2 = arguments[1]

try:
    nombre_1 = int(nombre_1)
    nombre_2 = int(nombre_2)

    resultat = nombre_1 / nombre_2
    if resultat > 1:
        resultat = int(resultat)
    else:
        print("Erreur! Résultat inférieur à 1")
        exit(1)

    reste = nombre_1 % nombre_2

    print(f"""
    Résultat = {resultat}
    Reste = {reste}""")

except ValueError:
    print("""ATTENTION !! Vous avez saisi une chaîne de caractères.
Veuillez saisir une entrée valide de 2 nombres entiers séparés par un espace.""")
    exit(1)
except ZeroDivisionError:
    print("Division par Zéro impossible")
    exit(1)