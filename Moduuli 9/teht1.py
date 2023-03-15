class Auto:
    def __init__(self, rekkari, hnopeus):
        print(f'Uusi auto {rekkari}, luotu')
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.nopeus = 0
        self.matka = 0


auto1 = Auto("ABC-123", "142 km/h")
print(f"Auton {auto1.rekkari} huippunopeus on {auto1.hnopeus}, tämän hetkinen nopeus on {auto1.nopeus} ja kuljettu matka on {auto1.matka}")