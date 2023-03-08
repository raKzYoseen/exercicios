def potencia (base, expoente):
    resultado = 1

    for numero in range(1,expoente+1):
        resultado *= base
    return resultado
#print (potencia(3,5))


def f3 (a):
    y = x + 1
    print(a+y)


x = 4
#f3(2)

# if simbolo == +
numero1 = int(input('Insira o primeiro número: '))
simbolos = input('Digite uma operação: ')
numero2 = int(input('Insira o segundo número: '))


def main():
        if simbolos == '+':
                print(somatorio())
        elif simbolos == '-':
                print(subtra())
        elif simbolos == '/':
                print(div())
        elif simbolos == 'x':
                print(multip())
        else:
            return "Error - Você escolheu uma operação errada!"


def somatorio():

        resultado = numero1 + numero2
        resultado = (f'{resultado:.2f}')
        return resultado
    

def multip():
        resultado = numero1*numero2
        resultado = (f'{resultado:.2f}')
        return resultado
    

def subtra():
        resultado = numero1-numero2
        resultado = (f'{resultado:.2f}')
        return resultado
    

def div():
        if numero2 == 0:
             return "Não é possível dividir por 0!"
        else:
            resultado = numero1/numero2
            resultado = (f'{resultado:.2f}')
        return resultado


    
print(main())