#tehtävä 6
import random
import math

'''
a=ympyrä
b=neliö
n=pisteiden kokonaismäärä
testikaava: x**2+y**2<1
pi
'''
N = int(input('Anna pisteiden määrä: '))
n = 0
counter = N

while counter>0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    counter = counter-1
    if x**2+y**2<1:
        n = n+1
print(f'Pistäitä arvioitu yhteensä {N}, joista {n} on ympyrän sisällä.')
pi = 4*n/N
print(f'Piin likiarvo on {pi}')