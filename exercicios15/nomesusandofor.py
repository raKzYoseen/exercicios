nomes = []
n = int(input("Digite a quantidade de nomes que deseja cadastrar:"))

for i in range(n):
    nomesX = str(input("Digite o nome:"))
    nomes.append(nomesX)

for i in range(len(nomes)):
    print(nomes[i])
