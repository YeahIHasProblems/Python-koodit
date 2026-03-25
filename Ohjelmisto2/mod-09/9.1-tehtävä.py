class Auto:
    def __init__(self, rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tnopeus = 0
        self.matka = 0


auto = Auto("ABC-123",120)
print(f"Auton rekisteri tunnus on {auto.rekisteritunnus} \nHuippunopeus on {auto.huippunopeus}km/h\nTämän hetkinen nopeus on {auto.tnopeus}\nKuljettu matka on {auto.matka}")