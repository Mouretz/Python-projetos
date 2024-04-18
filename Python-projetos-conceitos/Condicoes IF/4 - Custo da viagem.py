distancia = float(input('Qual a distancia percorrida? '))
# ATE 200 KM conta == 0.50 X KM , acima de 200km conta == 0.45 x KM
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O valor da sua passagem ficou RS {preco:.2f}')






