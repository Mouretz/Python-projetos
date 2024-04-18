import random
num = random.randint(1, 5) # Gerar numero inteiro entre 1 e 5
tentativa = int(input('Digite o numero que deseja adivinhar entre 1 e 5 '))
print('-=' * 30)
if tentativa == num:
    print('Voce acertou!!!')
else:
    print('Voce errou')
    print('-=' * 30)
    print(f'Eu pensei no {num} nao no {tentativa}')
