from sys import argv
from sys import exit

arg = argv[1:]
numbers_list = []


# FUNCTIONS
def is_sort(x):
    for i in range(len(x)):
        while i != len(x):
            j = i + 1
            if x[i] < x[j]:
                i += 1

            if x[i] > x[j]:
                resultat = f"This list is not sort"
                print(resultat)
                exit(0)

            if i >= len(x)-1:
                resultat = f"This list is sort"
                print(resultat)
                exit(0)


# ERRORS
try:
    for n in arg:
        n = int(n)
        numbers_list.append(n)
except ValueError:
    print("Error, you have to put integers numbers")
    exit(1)


is_sort(numbers_list)