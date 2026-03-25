class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def siirry_kerrokseen(self, kohde):
        print("\n")
        while self.nykyinen < kohde:
            self.kerros_ylös()
        while self.nykyinen > kohde:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissim):
        self.hissit = []
        for _ in range(hissim):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        print(f"\nHissi {hissin_numero} Liikkuu")
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("\nPALOHÄLYTYS!")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin)
            
talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)   
talo.aja_hissia(2, 8)
talo.aja_hissia(1, 1)
talo.palohalytys()