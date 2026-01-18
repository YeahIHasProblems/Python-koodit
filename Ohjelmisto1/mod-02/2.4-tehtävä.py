luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

summa = (luku1+luku2+luku3)
tulo = (luku1*luku2*luku3)
lista = [luku1,luku2,luku3]

print("Laskujen summa on: " + str(summa))
print("Laskujen tulo on: " + str(tulo))
print("Laskujen keskiarvo on: " + str(sum(lista) / len(lista)))