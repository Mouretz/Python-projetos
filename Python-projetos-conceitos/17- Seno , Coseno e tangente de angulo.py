# 18 - Mostrar seno, coseno e tangente de um angulo
import math
from math import radians
ang = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(ang))
print('o angulo de {} tem o SENO de {}'.format(ang,seno))
cos = math.cos(math.radians(ang))
print('o angulo de {} tem o COSSENO de {}'.format(ang,cos))
tang = math.tan(math.radians(ang))
print('o angulo de {} tem a TANGENTE de {}'.format(ang,tang))

