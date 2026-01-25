suurin = 0
pienin = 0
luku = 0
while True:
    luku = input("Anna luku :")
    if luku == "":
        break
    luku = int(luku)
    if (luku > suurin):
        suurin = luku
    if (luku < pienin):
        pienin = luku
print(f"Pienin luku on {pienin} ja suurin luku on {suurin}")