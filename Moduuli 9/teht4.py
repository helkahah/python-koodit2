import random


class Auto:
    def __init__(self, rekkari, hnopeus):
        print(f'Uusi auto {rekkari}, luotu')
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.nopeus = 0
        self.matka = 0

    def Kiihdytä(self):
        muutos = random.randrange(-10, 15)
        self.nopeus += muutos
        if self.nopeus<0:
            self.nopeus -= self.nopeus
        elif self.nopeus>self.hnopeus:
            self.nopeus = self.hnopeus
        else:
            return

    def Kulje(self, tunti):
        self.matka += self.nopeus * tunti

autot = []

for i in range(10):
    autot.append(Auto("ABC-"+str(i+1), random.randint(100, 200)))

aika = 0
kilpailu = True
while kilpailu:
    aika +=1
    for auto in autot:
        auto.Kiihdytä()
        auto.Kulje(1)
        if auto.matka>=10000:
            print(f"Auto {auto.rekkari} Klki 10000km ensimmäisenä, aikaa kului {aika} tuntia")
            print("")
            kilpailu = False
        else:
            pass

print("Kilpailijoiden tiedot:")
for auto in autot:
    print(f"Auto {auto.rekkari}, kulki {auto.matka}km, auton huippunopeus on {auto.hnopeus}km/h, nykyinen nopeus on {auto.nopeus}km/h")