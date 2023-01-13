import math

luoti_mää = input('Anna luotien määrä: ')
naula_mää = input('Anna naulojen määrä: ')
leiviskä_mää = input('Anna leivisköjen määrä: ')

luoti = 13.3
naula = 32*luoti
leiviskä = 20*naula

luoti_str = float(luoti_mää)
naula_str = float(naula_mää)
leiviskä_str = float(leiviskä_mää)

massa_gr = (leiviskä*leiviskä_str)+(naula*naula_str)+(luoti*luoti_str)
massa_kg = math.floor(massa_gr/1000)

print(f'Massa nykymittojen mukaan: {massa_kg:3.0f} kilogrammaa ja ' + str(round(massa_gr-massa_kg*1000, 2)) + ' grammaa.')