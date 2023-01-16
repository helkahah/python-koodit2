'''
tehtävä 1
tässä alkeellinen versio:

luku_max = 999
luku = 0

while luku<luku_max:
    luku=luku+3
    print(luku)
'''

num = 0

while num < 1000:
    while num%3 == 0:
        print(num)
        num = num + 1
    else:
        num = num + 1