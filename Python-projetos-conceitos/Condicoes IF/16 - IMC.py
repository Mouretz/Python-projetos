peso = float(input(' Inorme seu PESO '))
altura = float(input('Infome sua ALTURA '))
imc = peso / (altura*altura)

if imc < 18.5:
    print(' Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print(' Peso Ideal ')
elif imc >= 25 and imc< 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print(' OBESIDADE MORBIDA')

"""
PODERIA SER:
elif 25 <= imc < 30:
elif 30 <= imc <40:
"""
