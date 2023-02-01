# moduuli 6 tehtävä 1
import random

def heitto():
    return random.randint(1, 6)

päällä = True

while päällä:
    tulos = heitto()
    print(f'{tulos}')
    if tulos == 6:
        päällä = False

'''
# funktion sisällä toimiva koodi:

def heitto():
    päällä = True
    while päällä:
        tulos = random.randint(1, 6)
        print(f'{noppa}')
        if tulos == 6:
            print('Maksimi silmäluku tuli')
            päällä = False

heitto()
'''



