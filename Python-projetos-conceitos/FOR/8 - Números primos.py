num = int(input('Infome o numero que deseja sanber '))
tot = 0
for c in range(1, num+1):
    if num % c ==0: # Se o numero for divisivel pelo contador
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}')
print(f'O numero {num} foi divido {tot} vezes')