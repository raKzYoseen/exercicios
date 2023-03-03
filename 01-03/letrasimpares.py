nome = str(input("Digite um nome: "))
letrasimpares = []

for x in range(len(nome)):
    if (x+1) % 2 != 0:
        letrasimpares.append(nome[x])

print(letrasimpares)