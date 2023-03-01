
# Questão 1

# for i in range(10):
#     print(f'A multiplicação de:',(i+1),'é igual a:',(i+1)*13)

# for i in range(10):
#     print(f'A divisão de:{(i+1)}é igual a:{((i+1)/13):,.2f}')

# for i in range(10):
#     print(f'A soma de:{(i+1)}é igual a:{(i+1)+13}')

# for i in range(10):
#     print(f'A subtração de:{(i+1)}é igual a:{(i+1)-13}')

# def questao1():

#     for i in range(1,11):
#         calculo: i*13
#         print(f'{i}. {i}x13 = {calculo}')

# questao1()




# Questão 2

# numero = []

# for i in range(10):
#     numerox = float(input("Digite um número:"))
#     numero.append(numerox)

# def questao2():
#     quantidade = 0
#     for i in range(10):
#         numero = int(input("Insira um número:"))

#         if numero >=10 and numero<=50:
#             quantidade = quantidade + 1
#             print(numero)

#     print("Quantidade de números dentro do intervalo é:", quantidade)

# questao2()


def questao3():

    # numero = []

    # for i in range(5):
    #     numero.append(int(input("Digite um número:")))

    # print(min(numero))

    menor = 0

    for i in range(5):
        numero = int(input("Insira um número:"))

        if menor == 0:
            menor = numero
        elif numero <= menor:
            menor = numero
    print("O menor número inserido é:", menor)
    
questao3()


    

