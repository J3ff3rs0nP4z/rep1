
#Crie 1 dict comprehension através de uma lista de inteiros executando uma operação matemática.

dic_nomes = [('Diego', 6) , ('Fabio', 4) , ('Lara', 2) , ('Artur', 3)]

op_matematica = {c:(v+1) for c,v in dic_nomes}
print(op_matematica)



