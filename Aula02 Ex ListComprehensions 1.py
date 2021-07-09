import os
os.system('cls')

#Crie 1 list comprehension executando algumas operação matemática


lista_comprehen = [('vlr1' , 10),('vlr2' , 20),('vlr3' , 30),('vlr4' , 40)]

nova_lista = {c : v/2 for c, v in lista_comprehen}
print(nova_lista.values())

