class Auto:
    def __init__(self, rekisteritunnus,huippunopeus,tnopeus=0,matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tnopeus = tnopeus
        self.matka = matka

    def kulje(self,tunnit):
        self.matka += int(self.tnopeus*tunnit)

auto = Auto("ABC",120,60,2000)      
auto.kulje(1.5)
print(f"{auto.matka}")


        

