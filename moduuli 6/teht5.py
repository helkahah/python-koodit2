# moduuli 6 tehtävä 5

def lista_fun(lista):
    for i in lista:
        if i%2 != 0:
            lista.remove(i)

lista = [1, 2, 3, 4, 5]
lista2 = lista.copy()
lista_fun(lista)
print(lista)
print(lista2)

