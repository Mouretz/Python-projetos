# 17 - Calcular Hipotenusa de um triangulo retangulo
from math import pow,sqrt
Co = float(input('Digite o valor do Cateto Oposto: '))
Ca = float(input('Digite o valor do Cateto Adjacente: '))
h = pow(Co,2) + pow(Ca, 2)
r = sqrt(h)
print(f'A hipotenusa do triangulo retangulo e: {r:.2f}')
#OU math.hypot(Co, Ca)