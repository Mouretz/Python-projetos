"""
n = int(input('Digite Valor inteiro para laco'))
for c in range (0,n+1):
    print(c)
print('FIM')

inicio = int(input('Digite Valor de inicio'))
fim = int(input('Digite Valor de fim'))
passo = int(input('Digite Valor de passos'))
for x in range(inicio,fim+1,passo):
    print(x)

s = 0 # valor inicial para incremento zero / false
for c in range(0,4): # para um intervalo de 0 a 3( 4 numeros ) faca: 
    n = int(input('Digite o numero para soma: ')) # 4 input de n
    s = s + n # ou  s += n # Valor de incrementeo recebe = ele 0(zero) soma ao n(inputs de usuario)
print(f'A soma dos 4 numeros foi : {s}') # printa a soma dos inputs guardados em s

for c in range(10,0,-1): # de 10 a 1 tirando 1
    print(c)
"""



"""
empresa = 'Canva'

ranking = 0
for c in range(1,7):
    n = str(input(f'INFORME {c}(o) DADO VAZADO ')).upper().split()[0] # Pega primeira frase escrita
    empresa = empresa + '-'+ n # recebe o nome da empresa e soma cada input do loop

dados_vazados = [empresa] # Recebendo todos os inputs de Lista de dados vazados


if 'SENHA' in dados_vazados:
    ranking += 1000000
if 'DICA' in dados_vazados:
    ranking += 100000
if 'NUMERO' or 'NÚMERO' in dados_vazados:
    ranking += 1000
if 'NOMES' or 'NOME' in dados_vazados:
    ranking += 100
if 'EMAIL' or 'E-MAIL' in dados_vazados:
    ranking += 10
if '..' or '//' or f'{float}' in dados_vazados:
    ranking += 1

print(ranking)
print(dados_vazados)
"""





"""
empresa = 'canva'
ranking = 0

for c in range (1,7):
    n = str(input(f'Informe o {c}(o) DADO VAZADO ')).split()
    empresa = empresa + f'{n}'

dados_vazados = [empresa] # Recebendo todos os inputs de Lista de dados vazados


if 'SENHA' in dados_vazados:
    ranking = 40
elif 'DICA' in dados_vazados:
    ranking = 30
elif 'NUMERO' or 'NÚMERO' in dados_vazados:
    ranking = 20
elif 'NOMES' or 'NOME' in dados_vazados:
    ranking = 10
elif 'EMAIL' or 'E-MAIL' in dados_vazados:
    ranking = 5
elif '..' or '//' or f'{float}' in dados_vazados:
    ranking = 1


print(ranking)
print(dados_vazados)

li = list.copy([dados_vazados])

print(li)


"""

