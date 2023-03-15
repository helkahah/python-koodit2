class Auto:
    def __init__(self, rekkari, hnopeus):
        print(f'Uusi auto {rekkari}, luotu')
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.nopeus = 0
        self.matka = 0

    def Kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus<0:
            self.nopeus -= self.nopeus
        elif self.nopeus>self.hnopeus:
            self.nopeus = self.hnopeus
        else:
            return

    def Kulje(self, tunti):
        self.matka += self.nopeus * tunti


# tehtävä 1
auto1 = Auto("ABC-123", 145)
print(f"Auton {auto1.rekkari} huippunopeus on {auto1.hnopeus}km/h, tämän hetkinen nopeus on {auto1.nopeus} ja kuljettu matka on {auto1.matka}")
# tehtävä 2
auto1.Kiihdytä(30)
auto1.Kiihdytä(70)
auto1.Kiihdytä(50)
print(f"Auton tämän hetkinen nopeus on {auto1.nopeus}km/h")
auto1.Kiihdytä(-200)
print(f"Auton tämän hetkinen nopeus on {auto1.nopeus}km/h")
# tehtävä 3
auto1.Kiihdytä(80)
auto1.Kulje(2)
print(f"Auto on kulkenut {auto1.matka}km")