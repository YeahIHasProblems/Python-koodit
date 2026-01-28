import random

def nopanheitto():
    return random.randint(1,tahkojenmaara)

tahkojenmaara = int(input("Anna tahkojen määrä: "))
while True:
    onkomaksimi = nopanheitto()
    print(onkomaksimi)
    if onkomaksimi == tahkojenmaara:
        break