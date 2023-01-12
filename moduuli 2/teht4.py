#tehtävä 4

koko1_str = input('Anna ensimmäinen kokonaisluku: ')
koko2_str = input('Anna toinen kokonaisluku: ')
koko3_str = input('Anna kolmas kokonaisluku: ')

koko1 = float(koko1_str)
koko2 = float(koko2_str)
koko3 = float(koko3_str)

summa = koko1+koko2+koko3
tulo = koko1*koko2*koko3
keskiarvo = (koko1+koko2+koko3)/2

print('Kokonaislukujen summa on: ' + str(summa))
print('Kokonaislukujen tulo on: ' + str(tulo))
print('Kokonaislukujen keskiarvo on: ' + str(keskiarvo))