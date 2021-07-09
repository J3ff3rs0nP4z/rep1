import os
os.system('cls')

#Crie 1 list comprehension listando valores impares em um range de números.

#lista_ordem = ['A' : 1 , 'B' : 2 , 'C' : 3 , 'D' : 4 , 'E' : 5 , 'F' : 6]

for n in range(8):
    if n%2 == 1:
        print(n)
    
num_impares = [n for n in range(20) if n %2 == 1]
print(num_impares)