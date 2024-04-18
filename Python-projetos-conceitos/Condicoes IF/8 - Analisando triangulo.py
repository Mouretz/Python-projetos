ra = int(input('Raio 1 '))
rb = int(input('Raio 2 '))
rc = int(input('Raio 3 '))

if ra < rb + rc and rb < ra + rc and  rc < ra + rb:
    print('O triangulo pode ser contruido')
else:
    print(' Nao podera haver triangulo')



