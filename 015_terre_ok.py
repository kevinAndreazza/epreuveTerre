from sys import argv
from sys import exit
print(len(argv))

if len(argv) != 2:
    print("Error, tou have to put just one argument")

arg = argv[1]
arg = str(arg)

try:
    arg = int(arg)
    if arg == int(arg):
        print("Error, you have to wright your name")
        exit(1)
except ValueError:
    print()


answer = input(f"""
Avez-vous finit tous les exercices des epreuves de la Terre ? [Y/N] """)


if answer.lower() in ["y", "yes"]:
    print(f"Congratulation {arg}, you finished earth test")
    exit(0)

if answer.lower() in ["n", "No"]:
    print(f"One more effort {arg}, you're almost there")
    exit(0)

else:
    print("Error, you have to enter Yes or No")
    exit(1)
