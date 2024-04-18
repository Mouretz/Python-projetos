# 10 - Ler quantos R$ tem na carteira e quantos dolar pode comprar U$ a 3,27
Real = float(input(f'Qual o valor em Reais na sua carteira? R$  '))
Dolar = Real/3.27
print(f'Com R$ {Real:.2f} voce pode comprar U${Dolar:.2f}')# para limitar 2 casa deciamis {variavel :.2f}