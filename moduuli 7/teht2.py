# moduuli 7 tehtävä 2

nimet = set()
nimi = input("Anna nimi, tyhjä kenttä lopettaa toiminnon: ")

while nimi != "":
    if nimi in nimet:
        print("Nimi on jo listassa")
    else:
        print("Nimi on uusi")
        nimet.add(nimi)
    nimi = input("Anna nimi, tyhjä kenttä lopettaa toiminnon: ")

for x in nimet:
    print(x)
