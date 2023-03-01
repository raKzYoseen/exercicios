print('Bem vindo ao mundo Pokemon!')
print('\n Você esta caminhando em direção a sua casa quando ouvi um pedido de socorro... \n')

escolha1 =print(input('''\n
1. Ir na direção do grito...
2. Ignorar e continuar no seu caminho...\n'''))

if escolha1 == 1:
    print('\nVocê avista uma mulher sendo atacada por um pokemon selvagem.\n')
elif escolha1 == 2:
    print('\nUma mulher corre na sua direção e você nota que ela esta sendo perseguida por um pokemon selvagem.\n ')
else:
    print(escolha1)