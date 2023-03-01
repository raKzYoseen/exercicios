dicionario = {"Nome":'Victor',"Sobrenome":'Sena',"Idade":'25',"Curso":'Programação',"Bairro":'Aldeota'}


print(dicionario.items())
print(dicionario)
print(dicionario["Nome"])
print(dicionario["Sobrenome"])
print(dicionario["Idade"])
print(dicionario["Curso"])
print(dicionario["Bairro"])
del dicionario["Curso"]
dicionario["Sobrenome"] = 'Lopes'
print(dicionario)
print(dicionario["Bairro"])
dicionario2 = dicionario.copy()
dicionario2["Nome"] = 'André'
dicionario2["Idade"] = '28'
print(dicionario2)