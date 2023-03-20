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

class Kilpailu:
    def __init__(self, nimi, kilometrit, autolkm):
        self.autot = []
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.aika = 0
        self.kilpailu_päällä = True
        for i in range(autolkm):
            self.autot.append(Auto("ABC-" + str(i + 1), random.randint(100, 200)))

    def tunti_kuluu(self):
        self.aika += 1
        for i in self.autot:
            i.kiihdytä()
            i.kulje()
        return

    def tulosta_tilanne(self):
        print("Kilpailijoiden tiedot:")
        for auto in self.autot:
            print(f"Auto {auto.rekkari}, on kulkenut {auto.matka}km, auton huippunopeus on {auto.hnopeus}km/h, nykyinen nopeus on {auto.nopeus}km/h")


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrit:
                self.kilpailu_päällä = False
                print(f"Auto {auto.rekkari} Kulki 8000km ensimmäisenä, aikaa kului {self.aika} tuntia")
                print("")
                print("Lopputilanne")
                self.tulosta_tilanne()
                return
            else:
                pass

#pääkoodi
kilpailu = Kilpailu("Suuri romuralli", 8000, 10)
kierros = 0
while kilpailu.kilpailu_päällä:
    print(f"Kierros {kierros}")
    if kilpailu.aika % 10 == 0:
        kilpailu.tulosta_tilanne()
    else:
        pass
    kilpailu.tunti_kuluu()
    kilpailu.kilpailu_ohi()
    print("")
    kierros += 1