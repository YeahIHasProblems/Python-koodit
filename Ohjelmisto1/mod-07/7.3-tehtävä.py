def lisää(lentoasemat):
    ICAO = input("Kerro ICAO koodi: ")
    nimi = input("Lentoaseman nimi: ")
    lentoasemat[ICAO] = nimi
def hae(lentoasemat):
    ICAO = input("Kerro ICAO koodi: ")
    print (lentoasemat[ICAO])
def tulosta_valikko():
    print("\n1 = Lisää uusi lentoasema")
    print("2 = Tulosta lentoaseman nimi")
    print("9 = Lopeta")


lentoasemat = {"EFHK": "Helsinki-Vantaa"}

tulosta_valikko()
toiminto = int(input("Anna toiminto: "))

while toiminto != 9:
    if toiminto == 1:
        lisää(lentoasemat)
    elif toiminto == 2:
        hae(lentoasemat)
    else:
        print("Tuntematon toiminto")
    tulosta_valikko()