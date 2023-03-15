class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dizerOla(self):
        print('Olá, meu nome é', self.nome,'e meu salario é',self.salario)

funcionario1 = Funcionario('Jonas','+ de 8000')

funcionario2 = Funcionario('Marcos',2000)

funcionario1.dizerOla()
funcionario2.dizerOla()