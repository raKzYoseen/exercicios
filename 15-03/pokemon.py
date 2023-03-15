import random
class Pokemon:
    def __init__(self,nome,elemento,hp,habilidades):
        self.nome = nome
        self.elemento = elemento
        self.hp = hp
        self.habilidades = habilidades
    
    def batalha(self,oponente):
        
        print(f'{self.nome} X {oponente.nome}!')


        
        while True:
            jogador = int(input('''\n
    Escolha uma Habilidade!
    1 - Choque!
    2 - Slash!
    > '''))
            if jogador == 1:
                print(f'{self.nome} usou {list(self.habilidades.keys())[0]}!')
                print(f'O HP de {oponente.nome} agora é de {oponente.hp - list(self.habilidades.values())[0]}!')
                oponente.hp = oponente.hp - list(self.habilidades.values())[0]

            elif jogador == 2:
                print(f'{self.nome} usou {list(self.habilidades.keys())[1]}!')
                print(f'O HP de {oponente.nome} agora é de {oponente.hp - list(self.habilidades.values())[1]}!')
                oponente.hp = oponente.hp - list(self.habilidades.values())[1]
            
            else:
                print('Você escolheu um ataque que seu pokemon não aprendeu ainda!')

            if oponente.hp <= 0:
                print(f'\nO {oponente.nome} foi derrotado, {self.nome} venceu!\n')
                break

            print(f'Agora é o turno de {oponente.nome}!')
    

            oponenteatk = random.choice(range(1,2))

            if oponenteatk == 1:
                print(f'{oponente.nome} usou {list(oponente.habilidades.keys())[0]}!')
                print(f'O HP de {self.nome} agora é de {self.hp - list(oponente.habilidades.values())[0]}!')
                self.hp = self.hp - list(oponente.habilidades.values()[0])

            elif oponenteatk == 2:
                print(f'{oponente.nome} usou {list(oponente.habilidades.keys())[1]}!')
                print(f'O HP de {self.nome} agora é de {self.hp - list(oponente.habilidades.values())[1]}!')
                self.hp = self.hp - list(oponente.habilidades.values()[1])

            if self.hp <= 0:
                print(f'\nO {self.nome} foi derrotado, {oponente.nome} venceu!\n')

            print(f'Agora é o turno de {self.nome}!')
            break

Pikachu = Pokemon('Pikachu','Raio',10,{'Choque':2, 'Slash':3})
Charmander = Pokemon('Charmander','Fogo',10,{'Bola de fogo':2, 'Fire storm':3})


Pikachu.batalha(Charmander)