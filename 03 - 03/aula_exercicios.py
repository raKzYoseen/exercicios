def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    return (f'{salario:.2f}')

# print(calcular_pagamento(qtd_horas=(float(input("Digite a quantidade de horas: "))),
#                          valor_hora=(float(input("Digite o valor da hora trabalhada: ")))))

def hello(meu_nome):
    print('Olá', meu_nome)
    return True

def calculo_imc(peso, altura):
    print(peso/altura**2)



def gorjeta(valor_conta):

   return (10*valor_conta)/100

print(gorjeta(100))