# tehtävä 3
luku = input('Anna luku: ')
suurin = int(luku)
pienin = int(luku)
while luku!="":
    luku = int(luku)
    if luku>suurin:
        suurin = luku
        luku = input('Anna luku: ')
    elif luku<pienin:
        pienin = luku
        luku = input('Anna luku: ')
    else:
        luku = input('Anna luku: ')
if luku=="":
    print('Suurin luku on: ' + str(suurin))
    print('Pienin luku on ' + str(pienin))