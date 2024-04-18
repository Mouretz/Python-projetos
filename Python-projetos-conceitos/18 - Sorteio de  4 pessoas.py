# 19 - Sorteio de 4 nomes exibindo nome
from random  import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista) # escolhido recebe uma escolha dentro da lista
print(f'O Aluno sorteado foi {escolhido}')

