# moduuli 5 tehtävä 1
import random

nopat = []
heitot = int(input('Anna arpakuutioiden lukumäärä: '))

for heitot in range(heitot):
    noppa = random.randint(1, 6)
    nopat.append(noppa)

print(nopat)