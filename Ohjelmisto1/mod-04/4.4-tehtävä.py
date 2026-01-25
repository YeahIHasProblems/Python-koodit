import random

arvausluku = random.randint(1,10)
arvaus = ("")

while arvaus != arvausluku:
    arvaus = int(input("Arvaa luku 1-10: "))
    if arvaus < arvausluku:
        print("Liian pieni arvaus")
    elif arvaus > arvausluku:
        print("Liian suuri arvaus")
    else:
        print("Oikein")
    
