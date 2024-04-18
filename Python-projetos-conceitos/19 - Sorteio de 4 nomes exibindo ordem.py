# 20 - Sorteio de 4 nomes exibindo ordem
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista) # embaralha os numeros apenas
print(f'O Aluno sorteado foi {lista}')

