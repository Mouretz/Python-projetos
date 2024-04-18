
num = [2,5,9,1]
num[2] = 3
print(num)
num.append(7) # ADICIONA AO FINAL DO INDICE
print(num)
num.sort() # ORGANIZA EM ORDEM
print(num)
num.sort(reverse=True) # ORGANIZA AO DO FIM PRO INICIO
print(num)
num.insert(2,0) # ADICIONA VALOR 0 NO INDICE 2
print(num)
num.pop() # Remove ultimo item
print(num)
num.pop(2) # REMOVE ITEM 2 da lista
print(num)
print(f'Esta lista em {len(num)} elementos!!!')
num.remove(3) # REMOVE DO INICIO ATE ACHAR O 3 MAIS PROXIMO DO INDICE, NAO variavel PARECIDA
print(num)
if 4 in num:
    num.remove(4)
else:
    print('NAO ACHEI O 4')

#

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for x in valores:  # PRA CADA VALOR EM VALOR _>
    print(f'{x}...',end='\n') # end='' comando para colocar na mesma linha

for c , v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

valores = list() # ou valores = []
for contador in range (0,5): # para uma contagem de intervalo entra 0 e 4
    (valores.append(int(input('Digite um valor para adicionar na lista'))))

for x , y in enumerate(valores):
    print(f'Na posicao {x} encontri o valor {y}!!!')
#
a = [1,6,3,8]
print(a)
b = a
b[2] =2 # b na posicao 2 recebe item 2
print(b)


# O SINAL DE = FAZ UMA LIGACAO DA LISTA E NAO UMA COPIA
