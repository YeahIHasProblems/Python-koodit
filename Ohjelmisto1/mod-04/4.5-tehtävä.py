kayttajatunnus = ""
salasana = ""
kerrat = 0

while True:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    kerrat = kerrat + 1

    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    elif kerrat == 5:
        print("Pääsy evätty")
        break