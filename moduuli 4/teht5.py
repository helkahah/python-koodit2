#tehtävä 5

O_tunnus = str('python')
O_salasana = str('rules')
yritys = 5



while yritys>0:
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')

    if tunnus!=O_tunnus or salasana!=O_salasana:
        print('Käyttäjätunnus tai salasana on väärin.')
        yritys = yritys-1
    elif tunnus==O_tunnus and salasana==O_salasana:
        print('Tervetuloa')
        break

if yritys==0 and (tunnus!=O_tunnus or salasana!=O_salasana):
    print('Pääsy evätty')