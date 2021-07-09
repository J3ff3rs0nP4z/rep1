#############      programa principal      ###############
import os
os.system('cls')

import modulo_prog
from pacote.prog1 import var1,listacarros
from pacote.prog2 import lista_pares

print("#############      programa principal      ###############")


####  chama função soma

print(modulo_prog.soma(2,3))

#modulo_prog.chama_input()

print(modulo_prog.calcula_maximo(2,55,290))


lista_pares(100)
