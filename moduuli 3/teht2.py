hyttilk = str(input('Laivalla on neljä hytti luokkaa: LUX, A, B, C. Mikä on hyttiluokkasi: '))
if hyttilk == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella')
elif hyttilk == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella')
elif hyttilk == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella')
elif hyttilk == 'C':
    print('C on ikkunaton hytti autokannen alapuolella')
else:
    print('Virhellinen hyttiluokka.')