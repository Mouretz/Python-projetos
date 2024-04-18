

n = int(input('Digite um valor '))
c = n
f = 1
while c > 0:
    print(f'{c}')

    f *= c # CALCULO DE FATORIAL
    c = c - 1 # C recebe ele -1 e atualizada/recebe novo C
print(f'O fatorial de {n} e {f}')


