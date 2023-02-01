# moduuli 6 tehtävä 3

user_input = float(input('Anna gallonamäärä: '))

def gallon_to_litre(user_input):
    litra = user_input * 3.785
    return litra

while user_input>=0:
    tulos = gallon_to_litre(user_input)
    print(tulos)
    user_input = float(input('Anna gallonamäärä: '))

else:
    print('Toiminto lopetettu')