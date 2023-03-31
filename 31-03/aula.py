import json


def pegarListaAtualizada():
    with open("funcionario.json", 'r') as funcionariosJson:
        lista = json.load(funcionariosJson)
    return lista

def inserirFuncionario():
    lista = pegarListaAtualizada()

    funcionario = {"Nome": '', "CPF": '', "Salario": '', "Cargo": '', "Departamento": ''}
    
    for dado in funcionario.keys():
        try:
            add = input(f'Insira o {dado} do Funcionario a ser cadastrado: ')

            if dado == "Salario":
                add = float(add)

            funcionario[dado] = add
        except ValueError:
            print('Valor Invalido!')


        listaFuncionarios = pegarListaAtualizada()
        listaFuncionarios.append(funcionario)

        with open("funcionario.json", 'w') as funcionariosJson:
            json.dump(listaFuncionarios, funcionariosJson, indent=2)
        




def verFuncionarios():

    listaFuncionarios = pegarListaAtualizada()

    if len(listaFuncionarios) == 0:
        print('A lista atualmente esta Vazia! Insira um cadastro de funcionário!')
    else:
        print("Lista de Funcionários: ")

        print("Nome | CPF | Salario | Cargo | Departamento")

        for funcionario in listaFuncionarios:

            print(
                f'{funcionario["Nome"]} | {funcionario["CPF"]} | {funcionario["Salario"]} | {funcionario["Cargo"]} | {funcionario["Departamento"]}')

        input()





def atualizarFuncionario():

    listaFuncionarios = pegarListaAtualizada()
    if len(listaFuncionarios) == 0:
        print('A lista atualmente esta Vazia! Insira um cadastro de funcionário!')
    else:
        print('Lista de Funcionarios: ')

        for i,funcionario in enumerate(listaFuncionarios):
            print(f'{i+1} - {funcionario["Nome"]}')
        try:
            att = int(input('Qual cadastro de funcionario você deseja atualizar?\n > '))

            if att == 1:
                print(f'\n 1- {listaFuncionarios[att-1]["Nome"]}\n 2- {listaFuncionarios[att-1]["CPF"]}\n 3- {listaFuncionarios[att-1]["Salario"]}\n 4- {listaFuncionarios[att-1]["Cargo"]}\n 5- {listaFuncionarios[att-1]["Departamento"]}')
            
                escolha = int(input('Qual informação você deseja alterar/atualizar?'))

                if escolha == 1:
                    listaFuncionarios[att-1]["Nome"] = input('Insira o nome: ')

                elif escolha == 2:
                    listaFuncionarios[att-1]["CPF"] = input('Insira o CPF: ')

                elif escolha == 3:
                    listaFuncionarios[att-1]["Salario"] = float(input('Insira o Salario: '))

                elif escolha == 4:
                    listaFuncionarios[att-1]["Cargo"] = input('Insira o Cargo: ')

                elif escolha == 5:
                    listaFuncionarios[att-1]["Departamento"] = input('Insira o Departamento: ')
        except ValueError:
            print('Valor Invalido!')
            
        with open("funcionario.json", 'w') as funcionariosJson:
            json.dump(listaFuncionarios, funcionariosJson, indent=2)


def removerFuncionario():
    listaFuncionarios = pegarListaAtualizada()
    if len(listaFuncionarios) == 0:
        print('A lista atualmente esta Vazia! Insira um cadastro de funcionário!')
    else:
        print('Lista de Funcionarios: ')

        for i,funcionario in enumerate(listaFuncionarios):
            print(f'{i+1} - {funcionario["Nome"]}')
        try:
            att = int(input('Qual cadastro de funcionario você deseja deletar?\n > '))

            del listaFuncionarios[att-1]
        except ValueError:
            print('Valor Invalido!')

        with open("funcionario.json", 'w') as funcionariosJson:
            json.dump(listaFuncionarios, funcionariosJson, indent=2)



while True:

    print('''
    Bem vindo a Empresa XYZ
    Menu:
    1. Ver Funcionários
    2. Inserir Funcionário
    3. Alterar/Atualizar Funcionário
    4. Remover Funcionário
    0. Sair
    
    ''')
    try:
        op = input("Escolha uma opção: ")

        match op:
            case "1":
                verFuncionarios()
            case "2":
                inserirFuncionario()
            case "3":
                atualizarFuncionario()
            case "4":
                removerFuncionario()
            case "0":
                print("Saindo do Programa...")
                break
    except ValueError:
        print('Valor Invalido')