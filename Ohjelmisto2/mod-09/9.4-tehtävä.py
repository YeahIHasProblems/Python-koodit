import random
class Auto:
    def __init__(self, rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tnopeus = 0
        self.matka = 0

    def kiihdytä(self,nopeus):
        self.tnopeus += nopeus
        if self.tnopeus > self.huippunopeus:
            self.tnopeus = self.huippunopeus
        if self.tnopeus <= 0:
            self.tnopeus = 0

    def kulje(self,tunnit):
        self.matka += int(self.tnopeus*tunnit)

autot = []
for i in range(1, 11):
    huippu = random.randint(100, 200)
    rek = (f"ABC-{str(i)}")
    autot.append(Auto(rek,huippu))

loppu = False
while True:
    if loppu == True:
        break
    for auto in autot:
        if auto.matka > 10000:
            loppu = True
        auto.kiihdytä(random.randint(-10,15))
        auto.kulje(1)

for auto in autot:
    print(f"Rekisterinumero: {auto.rekisteritunnus} Kuljettu matka: {auto.matka}")


