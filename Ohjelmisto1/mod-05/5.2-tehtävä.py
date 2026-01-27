luku = 0
lista = []

while luku != "":
    luku = (input("Anna luku: "))
    if luku != "":
        luku = int(luku)
    lista.append(luku)
    if luku == "":
        lista.pop()
    lista.sort(reverse=True)
    listasuurimmat = lista[0:5]
print(listasuurimmat)