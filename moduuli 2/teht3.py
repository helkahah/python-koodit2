#tehtävä 3
kanta_str = input('Anna suorakulmion kanta: ')
korkeus_str = input('Anna suorakulmion korkeus: ')
kanta = float(kanta_str)
korkeus = float(korkeus_str)
pinta_ala = kanta*korkeus
piiri = (kanta*2)+(korkeus*2)


print(f'Suorakulmion pinta-ala on: ' + str(pinta_ala))
print(f'suorakulmion piiri on: ' + str(piiri))