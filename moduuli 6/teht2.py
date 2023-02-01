# moduuli 6 tehtävä 2
import random

tahko = int(input('Anna tahkojen maksimimäärä: '))
def heitto(tahko):
    return random.randint(1, tahko)

päällä = True

while päällä:
    tulos = heitto(tahko)
    print(f'{tulos}')
    if tulos == tahko:
        päällä = False
        print('Toiminto lopetettu')