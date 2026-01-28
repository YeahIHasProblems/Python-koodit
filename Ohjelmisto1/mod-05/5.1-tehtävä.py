import random

arpakuutiot = int(input("Anna arpakuutioiden määrä: "))
lista = []

for x in range(arpakuutiot):
    arpakuutio = random.randint(1,6)
    lista.append(arpakuutio)

print(sum(lista))