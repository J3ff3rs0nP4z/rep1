import os
os.system('cls')

#Crie 2 dicionários de dados como valores distintos e execute a função zip nos valores dos dicionário e
# imprima os valores.

dic1 = {1 : 'amora' , 2 : 'banana' , 3 : 'caju' , 4 : 'mamão'}

dic2 = {1 : 'Ana' , 2 : 'Carla' , 3 : 'Junior' , 4 : 'Igor'}

uniao = list(zip(dic1.values(), dic2.values()))

print(uniao)
