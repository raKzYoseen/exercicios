# diasdasemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado"]
# # print(type(diasdasemana))
# # print(diasdasemana)
# # print(len(diasdasemana))
# # print(diasdasemana[4])



# for i in diasdasemana:
#     diasdasemana.append(input("Digite um nome:"))
#     print (diasdasemana)
#     break

# diasdasemana.remove('dia de folga')
# print(diasdasemana)

# diasdasemana.pop(6)
# print (diasdasemana)

# print("Texto".count('t'))


# notas = []
# soma = 0
# # n = print (input('Insira a quantidade de número que deseja adicionar a lista:'))

# for i in range(0,3):
#     notas = print(input(f'Digite o {i+1}º número:'))

# # for nota in notas:
# #     soma += nota
# # print (soma)

# print(notas)


# notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

# soma_das_notas = 0
# for nota in notas:
#     soma_das_notas += nota

# print(soma_das_notas)


# notas = []
# soma_das_notas = 0
# n = int(input('Digite a quantidade de notas que quer adicionar: '))
# for i in range(n):
#     notas.append(int(input('Digite uma nota: ')))

# for nota in notas:
#      soma_das_notas += nota

# print (soma_das_notas)


# def multiply_list(items):
# 	    tot = 1
# 	    for x in items:
# 	        tot *= x
# 	    return tot
# print(multiply_list([1,2,-8]))

# notas = []

# mult_das_notas = 1
# n = int(input('Digite a quantidade de notas que quer adicionar: '))
# for i in range(n):
#      notas.append(int(input('Digite uma nota: ')))

# for nota in notas:
#      mult_das_notas *= nota

# print (mult_das_notas)

nome = [input('Digite seu nome: ')]

for i in nome:
    numeroletras = len(i) - nome.count(" ")
    print(numeroletras)
    print (i[0])
    # print (i[::-1])

i.__reversed__()
print (*i)

