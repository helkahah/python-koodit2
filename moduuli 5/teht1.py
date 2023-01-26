# moduuli 5 tehtävä 1
import random

heitot = int(input('Anna arpakuutioiden lukumäärä: '))
total = 0

for heitot in range(heitot):
    noppa = random.randint(1, 6)
    total = total+noppa

print(f'Silmälukujen summa on: {total}')