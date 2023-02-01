# Moduuli 6 tehtävä 4
'''
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen palauttaman summan.
'''


def lista_fun(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa

lista = [1, 5, 7, 4, 9]
tulos = lista_fun(lista)
print(tulos)

