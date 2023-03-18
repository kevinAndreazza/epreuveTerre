from sys import argv
import sys


# generate alphabet as reference
a = ord("a"); z = ord("{"); alphabet = ""
for i in range(a, z):
    i = chr(i)
    alphabet += f"{i}"

# error management
if len(argv) != 2:
    print("Attention, vous devez au moins ecrire quelque chose.")
    sys.exit(1)
arg = argv[1]

if len(arg) != 1:
    print("""Attention, vous ne pouvez pas saisir 2 caracteres a la suite.""")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("""Attention, vous avez saisi trop d'arguments.""")
    sys.exit(1)
elif arg not in alphabet:
    print("Attention, vous devez saisir une lettre minuscule")
    sys.exit(1)

# result
else:
    arg = ord(arg) + 1
    for i in range(arg, z):
        print(chr(i), end="")
sys.exit(0)