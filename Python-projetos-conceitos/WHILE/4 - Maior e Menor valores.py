rep = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input(' digite um numero '))
    soma += num
    quant += 1
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

media = soma / num
print('ENCERRANDO...')




