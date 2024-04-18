# 11 - Ler altura e largura e dar area pintada com tinta 1LITRO que faz 2mquadrados
L = float(input(f'Digite a largura da parede: '))
Al = float(input(f'Digite a altura da parede: '))
A = L*Al
LT = (A/2) # a cada 2 metros quadrados 1 litro de tinta
print(f'Para pintar a parede sera necessario {LT:.1f}L de tinta!')