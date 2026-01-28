import random

pisteet = int(input("Kuinka monta pistettä arvotaan? "))
numero = 0
kerrat = 0

while kerrat < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        numero = numero + 1
    kerrat = kerrat + 1

pi = 4 * numero / pisteet
print(f"Piin likiarvo: {pi}")
