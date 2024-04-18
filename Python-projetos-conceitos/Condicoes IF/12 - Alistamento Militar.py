nasc = int(input(' Informe ano de nascimento seu: '))

from datetime import date
ano = date.today().year   # Recebendo ano atual da maquina

idade = ano - nasc # Calculo de idade atual

if idade >= 18:
    print(' Voce ainda nao precisa se apresetar ')
elif idade == 17:
    print(' Falta 1 ano para se apresentar')
else:
    print('Ainda nao e o momento de se apresentar')





