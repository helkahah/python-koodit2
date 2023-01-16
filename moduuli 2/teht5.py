import math

luoti_mää = float(input('Anna luotien määrä: '))
naula_mää = int(input('Anna naulojen määrä: '))
leiviskä_mää = int(input('Anna leivisköjen määrä: '))

luoti = 13.3
naula = 32*luoti
leiviskä = 20*naula

#luoti_str = float(luoti_mää)
#naula_str = float(naula_mää)
#leiviskä_str = float(leiviskä_mää)

massa_gr = (leiviskä*leiviskä_mää)+(naula*naula_mää)+(luoti*luoti_mää)
massa_kg = massa_gr//1000#math.floor(massa_gr/1000)

print(f'Massa nykymittojen mukaan: {massa_kg:3.0f} kilogrammaa ja ' + str(round(massa_gr-massa_kg*1000, 2)) + ' grammaa.')