print(f'''CARDAPIO:
{'100 - Cachorro quente'} {'R$1,10'}
{'101 - Bauru simples'} {'R$1,30'}
{'102 - Bauru c/ovo'} {'R$1,50'}
{'103 - Hamburger'} {'R$1,10'}
{'104 - Cheeseburger'} {'R$1,30'}
{'105 - Refrigerante'} {'R$1,00'}''')
while True:
    codigo = input('\nDigite o codigo do seu pedido:')
    codigos =  ('100,101,102,103,104,105')
    valor = 0

    
    if codigo in codigos:
        quantidade =int((input('\nDigite a quantidade: ')))
        if codigo == '100':
            nome = ('Cachorro quente')
            valor = 1.10

        elif codigo == '101':
            nome = ('Bauru simples')
            valor = 1.30

        elif codigo == '102':
            nome = ('Bauru c/ ovo')
            valor = 1.50

        elif codigo == '103':
            nome = ('Hamburger')
            valor = 1.10

        elif codigo == '104':
            nome = ('Cheeseburger')
            valor = 1.30

        elif codigo == '105':
            nome = ('Refrigerante')
            valor = 1.00

        valortotal = valor * quantidade
        print(f'\nVocê pediu: {nome}\nQuantidade: {quantidade}\nValor a pagar: {valortotal:,.2f}')
        break
    else:
            print('Insira um código valido')

