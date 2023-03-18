from sys import argv

# Creer la variable de sortie avec un type str
nom_de_fichier = ""

# decomposer argv en ses elements
for element in argv:
    # définir un index de depart pour lire les elements
    index_de_depart = len(element) - 1

    # afficher le résultat
    print(f"""
    Chaine : {element}
    Longueur : {index_de_depart}
    """)

    try:
        # tant que l'index n'est pas un séparateur backslash
        while element[index_de_depart] != '\\':
            # stocker l'élément de l'index dans le nom de fichier jusqu’à la fin de chaine
            nom_de_fichier = element[index_de_depart:]
            # soustraire 1 pour regarder index de gauche
            index_de_depart = index_de_depart - 1
    except IndexError:
        print()

# afficher le nom du fichier
print(nom_de_fichier)