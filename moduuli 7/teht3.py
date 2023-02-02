# moduuli 7 teht 3

def lisaa():
    tunnus = input("Anna lentoaseman tunnus: ")
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[tunnus] = nimi
    return

def hae():
    tunnus = input('Anna lentoaseman ICAO-koodi:')
    if tunnus in lentoasemat:
        print(f'Koodin {tunnus} vastaava lentokenttä on {lentoasemat[tunnus]}')
    return

def tulosta():
    for asema in lentoasemat:
        print(f"{asema}")
    return

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema"}

toiminto = -1

while toiminto != 3:
    print("0 = tulosta lentoasemien tiedot")
    print("1 = lisää uusi lentoasema")
    print("2 = hae lentoasema")
    print("3 = lopeta")

    toiminto = int(input("Valitse toiminto: "))
    if toiminto == 0:
        tulosta()
    elif toiminto == 1:
        lisaa()
    elif toiminto == 2:
        hae()
    elif toiminto == 3:
        print('Toiminto lopetetaan.')
        break
    else:
        print('Yritäppä uudelleen, paksusormi.')

print("Kiitos ja näkemiin")