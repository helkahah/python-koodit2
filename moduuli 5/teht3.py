# moduuli 5 tehtävä 3

luku = int(input('Anna kokonaisluku: '))
alkuluku = True

for i in range(2, luku):
    if luku%i==0:
        print('Luku ei ole alkuluku')
        alkuluku = False
        break
if alkuluku:
    print('Luku on alkuluku')