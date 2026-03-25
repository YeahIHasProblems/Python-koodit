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

h = Hissi(0, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)