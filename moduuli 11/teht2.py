import random
class Auto:
    def __init__(self, rekkari, hnopeus):
        print(f'Uusi auto {rekkari}, luotu')
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self):
        muutos = random.randrange(-10, 15)
        self.nopeus += muutos
        if self.nopeus<0:
            self.nopeus -= self.nopeus
        elif self.nopeus>self.hnopeus:
            self.nopeus = self.hnopeus
        else:
            return

    def kulje(self):
        self.matka += self.nopeus
        return

class Sähköauto(Auto):
    def __init__(self, rekkari, hnopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekkari, hnopeus)

class Polttomottoriauto(Auto):
    def __init__(self,rekkari, hnopeus, bensatankki):
        self.bensatankki= bensatankki
        super().__init__(rekkari, hnopeus)


#pääohjelma
sauto = Sähköauto("ABC-15", 180, 52.5)
pauto = Polttomottoriauto("ABC-123", 165, 32.3)
sauto.nopeus = 120
pauto.nopeus = 130
for i in range(3):
    sauto.kulje()
    pauto.kulje()

print(f"Pauto kulki kolmessa tunnissa {pauto.matka}km, nopeus mittarissa oli {pauto.nopeus}km/h")
print(f"Sauto kulki kolmessa tunnissa {sauto.matka}km, nopeus mittarissa oli {sauto.nopeus}km/h")
