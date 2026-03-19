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


        


auto = Auto("ABC-123",120)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(auto.tnopeus)
auto.kiihdytä(-200)
print(auto.tnopeus)