user_input = input("Écrire quelque chose : ")

# ERREURS
if user_input == "" or " ":
    print("ERREUR : vous n'avez rien écrit.")
    exit(1)

# retourner la phrase
index = - 1; longueur = len(user_input) - 1; argument = ""
while index != longueur:
    argument += f"{user_input[longueur]}"
    longueur = longueur - 1

# afficher resultat
print(argument)