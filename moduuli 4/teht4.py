#tehtävä 4
import random

arvaus = int(input('Anna kokonaisluku väliltä 1-10: '))
genluku = random.randint(1, 10)

while arvaus!=genluku:
    if arvaus>genluku:
        arvaus = int(input('Liian suuri arvaus, anna uusi kokonaisluku väliltä 1-10: '))
    else:
        arvaus = int(input('Liian pieni arvaus, anna uusi kokonaisluku väliltä 1-10: '))
else:
    print('Oikein')
