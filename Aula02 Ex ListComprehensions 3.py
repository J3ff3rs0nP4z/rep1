import os
os.system('cls')

#Crie 1 dict comprehension através de uma lista de strings
nomes = ['Diego' , 'Fabio' , 'Lara' , 'Artur']
dic_nomes = [('Diego', 6) , ('Fabio', 4) , ('Lara', 2) , ('Artur', 3)]

a1 = {i: valor for i, valor in dic_nomes}
print(a1)