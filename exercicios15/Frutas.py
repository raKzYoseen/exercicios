frutas = []
valor1 = 1
for i in range (5):
    frutaX = input('Escreva o nome da fruta:')
    frutas.append(frutaX)

print(f'''
{frutas[0]} {valor1}
{frutas[1]} {valor1*2}
{frutas[2]} {valor1/2}
{frutas[3]} {((valor1/2)*3)}
{frutas[4]} {(((valor1/2)*3)/2)}''')