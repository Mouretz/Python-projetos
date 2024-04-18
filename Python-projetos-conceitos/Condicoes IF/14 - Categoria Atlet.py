nasc = int(input(' Informe ano de nascimento do atleta: '))

from datetime import date
ano = date.today().year   # Recebendo ano atual da maquina

idade = ano - nasc # Calculo de idade atual
print(f'o atleta tem {idade}anos')
if idade <= 9:
    print(' MIRIM ')
elif idade <= 14:
    print(' INFANTIL ')
elif idade <= 19:
    print(' JUNIOR ')
elif idade <= 25:
    print(' SENIOR ')
else:
    print('MASTER')


