a = float(input(' Informe o primeiro valor:  '))
b = float(input(' Informe o segundo valor:  '))
c = float(input(' Informe o terceiro valor:  '))
#Verificar menor numero
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    c = menor
#VERIFICANDO MAIOR
maior  = a
if b > a and b > c:
    maior = b                   # Nao pode alterar a ordem de recebimento  if b = maior nao vai
if c > a and c > b:
    maior = c
print(f'O Menor numero foi {menor}')
print(f'O Maior numero foi {maior}')

