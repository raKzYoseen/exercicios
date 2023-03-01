while True:
    try:
        cpf = int(input("Insira seu CPF:"))
        
        if len(str(cpf)) !=11:
            print("O CPF deve ter 11 digitos. Tente novamente!")

        else:
            break
    except:
        print("Você digitou algo inválido!")