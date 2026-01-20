luku = input("Anna luku: ")
lista = [luku]

while luku != "":
    luku = input("Anna luku: ")
    lista.append(luku)
    if luku == "":
        lista.remove("")
        print(f"Pienin luku: {min(lista)} Suurin luku: {max(lista)}")

    
    