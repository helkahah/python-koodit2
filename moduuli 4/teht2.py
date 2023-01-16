# tehtävä 2

tuuma = float(input('Anna tuumat: '))
while tuuma>0:
    sentti = tuuma * 2.54
    print(str(tuuma) + ' tuumaa on ' + str(sentti) + ' senttimetriä.')
    tuuma = float(input('Anna tuumat: '))

else:
    print('ERROR')
