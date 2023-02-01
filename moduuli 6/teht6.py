'''
Pinta-ala = (arvo)/math.pi*(halkaisija)**2
'''
import math

def lasku(halkaisija, hinta):
        neliömetri = (halkaisija / math.pi * 4 ** 2)/1000
        ykhinta = neliömetri / hinta
        return ykhinta

halkaisija = float(input('Anna pizzan halkaisija: '))
hinta = float(input('Anna pizzan hinta: '))
pizza1 = lasku(halkaisija,hinta)

halkaisija = float(input('Anna toisen pizzan halkaisija: '))
hinta = float(input('Anna toisen pizzan hinta: '))
pizza2 = lasku(halkaisija, hinta)

if pizza2<pizza1:
    print('Toinen pizza antaa paremman vastineen rahalle.')
else:
    print('Ensimmäinen pizza antaa paremman vastineen rahalle.')


'''
neliösentti = 4/math.pi*4**2
neliömetri = neliösentti/1000
print(neliömetri)
'''
