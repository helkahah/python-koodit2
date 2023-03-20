class Hissi:
    def __init__(self, akerros, ykerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.kerros = akerros
        print(f"Uusi hissi luotu ja hissi on kerroksessa {self.kerros}")

    def kerros_ylös(self):
        if self.kerros != self.ykerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            return

    def kerros_alas(self):
        if self.kerros != self.akerros:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            return

    def siiry_kerrokseen(self, number):
        if number > self.kerros:
            number -= self.kerros
            for n in range(number):
                self.kerros_ylös()
        elif number < self.kerros:
            numbers = self.kerros - number
            for n in range(numbers):
                self.kerros_alas()
        else:
            return

class Talo:
    def __init__(self, akerros: int, ykerros: int, hissit: int):
        self.akerros = akerros
        self.ykerros = ykerros
        self.hissit = []
        for n in range(hissit):
            uusi_hissi = Hissi(akerros, ykerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissi_nro: int, kerros: int):
        self.hissit[hissi_nro-1].siiry_kerrokseen(kerros)

    def palohälytys(self):
        kerrat = 0
        for n in self.hissit:
            self.aja_hissiä(kerrat, self.akerros)
            kerrat += 1
            print(" ")
        print("Kaikki hissit ovat alimmassa kerroksessa")


talo = Talo(0,5,5)
talo.aja_hissiä(3, 4)
print(" ")
talo.aja_hissiä(2, 5)
print(" ")
talo.aja_hissiä(5, 2)
print("")
print("Seuraavaksi palohälytys")
print("")

talo.palohälytys()