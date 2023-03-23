class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print("Kirjan tiedot")
        print(f"Nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, "
            f"sivuja: {self.sivumäärä}.")
        return

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print("Lehden tiedot")
        print(f"Nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")
        return



lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()