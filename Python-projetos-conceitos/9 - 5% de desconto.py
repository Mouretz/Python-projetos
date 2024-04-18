# 12 - Ler valor e exibir valor com 5% de desconto
P = int(input('Digite o preco R$ '))
# ou D = P -(P *5/100)
R = P *5/100
D = P - R
print(f'Com desconto fica R$ {D:.2F}')