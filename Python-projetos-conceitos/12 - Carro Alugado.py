# 15 - kM Percorrido , dias alugado  ( 60 reias/dia e r$0,15 por km rodado)
Km = float(input('Digite Km percorrido '))
D = int(input('Digite os dias Alugados '))
P = (Km * 0.15) + (D * 60)
print(f'O valor a se pagar pelo carro e de R${P:.2f}')