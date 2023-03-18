"""
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un
retour à la ligne.

Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle.
"""
# recuperer l'index ascii de "a" et "z" dans des variables
a = 97
z = 123

# pour chacun des index compris entre "a" et "z"
for i in range(a, z):
    # affiche le caractère contenu dans l'index
    alphabet = chr(i)  # sur une ligne et sans espaces
    print(alphabet, end="")
# inclure un retour à la ligne
print()



