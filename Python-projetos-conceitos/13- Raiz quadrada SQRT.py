# - Calcular raiz quadrada usando biblioteca SQRT
import math #Todos modulos de matematica
num = int(input('Digite um Numero: '))
raiz = math.sqrt(num) #funcao de raiz quadrada biblioteca math[matematica] sqrt [raiz quadrada]
print('A raiz de {} e igual a {} '.format(num, raiz)) #exibir  raiz quadrada
print('A raiz de {} e igual a {} '.format(num, math.ceil(raiz))) #Funcao math.ceil arredonda para cima
print('A raiz de {} e igual a {:.2f} '.format(num, math.floor(raiz))) #Funcao math.floor arredonda para baixo
#OU
#from math import sqrt,floor #Modulo apenas de raiz e arredondamento para baixo(floor)
#num = int(input('Digite um Numero: '))
#raiz = sqrt(num) #funcao  sqrt [raiz quadrada]
#print('A raiz de {} e igual a {} '.format(num, floor(raiz)))#exibir  raiz quadrada arredondada para baixo