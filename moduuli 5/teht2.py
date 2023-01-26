# moduuli 5 tehtävä 2

luvut = []

while True:
    luku = input('Anna seuraava luku:')
    if luku == "":
        break
    luvut.append(int(luku))

luvut.sort(reverse=True)

if len(luvut)<=5:
    print(luvut)
else:
    for i in range(5):
        print(luvut[i])