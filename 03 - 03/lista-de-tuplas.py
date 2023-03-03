lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# def inverter(x):
#     return x[1]


# listainversa = sorted(lista, key=inverter)
# print (listainversa)


# listainversa = sorted(lista, key=lambda x:x[1])
# print (listainversa)

listanova = []

for tupla in lista:
    listanova.append(tupla[::-1])
listanova.sort()
print(listanova)
lista.clear()
for tupla in listanova:
    lista.append(tupla[::-1])
print(lista)
