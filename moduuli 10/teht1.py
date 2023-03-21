class Hissi:
    def __init__(self, akerros, ykerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.kerros = akerros
        print(f"Uusi hissi luotu ja hissi on kerroksessa {self.kerros}")

    def kerros_ylös(self):
        if self.kerros < self.ykerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            return

    def kerros_alas(self):
        if self.kerros > self.akerros:
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


h = Hissi(1, 8)
h.siiry_kerrokseen(5)
print("Hissi palaa alimpaan kerrokseen")
h.siiry_kerrokseen(h.akerros)

