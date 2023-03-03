# Questão 1
def duplicatas():
    duplicatas = [5,5,4,4,3,3,2,2,1,1]

    lista = list(dict.fromkeys(duplicatas))

    print(lista)



# Questão 2
def listadetuplas():
    lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    # Forma 1:
    def inverter(x):
        return x[1]


    listainversa = sorted(lista, key=inverter)
    print (listainversa)

    # Forma 2:
    listainversa = sorted(lista, key=lambda x:x[1])
    print (listainversa)

    # Forma 3:
    listanova = []

    for tupla in lista:
        listanova.append(tupla[::-1])

    listanova.sort()

    print(listanova)

    lista.clear()

    for tupla in listanova:
        lista.append(tupla[::-1])

    print(lista)



# Questão 3
def listavazia():

    lista = [1]

    if len(lista) == 0:
        print ('A lista esta vazia!')
    else:
        print ('A lista não esta vazia!')



# Questão 4
def copiarlista():
    lista = [8,7,9]

    copialista = []

    copialista = lista.copy()

    print (copialista)


# Questão 5
def palavramaior():
    lista = ['Vermelho', 'Verde', 'Branco', 'Preto', 'Rosa', 'Amarelo']
    maior = ""

    for nome in lista:
        if len(nome) > len(maior):
            maior = nome

    print (maior)


# Questão 6
def removerpares():
    lista = [1,2,3,4,5,6,7,8,9,10]
    novalista = []

    for i in range(len(lista)):
        if i % 2 != 0:
            novalista.append(i)
    print (novalista)
        

# Questão 7
lista = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lista)):
    if i < len(lista):
        lista.pop(i % 2 == 0)
print (lista)