# 16 - Calcule numero real e exiba parte inteira
from math import floor,ceil
num = float(input('Digite um Numero Real: '))
print(f'O numero tem sua porcao inteira como {num:.0f}') #Exemplo automatico de numero inteiro usando formatacao :.
iB = floor(num) #exemplo automatico de numero inteiro usando formatacao floor arredonda para baixo
ic = ceil(num)#exemplo automatico de numero inteiro usando formatacao ceil arredonda para cima
print('O numero tem sua porcao inteira arredondada para baixo no valor de {}'.format(iB))
print('O numero tem sua porcao inteira arredondada para cima no valor de {}'.format(ic))

#poderia utilizar int (num) no final da respota ou biblioteca math.trunc(num)