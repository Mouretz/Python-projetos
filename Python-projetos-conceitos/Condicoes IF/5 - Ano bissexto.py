ano = int(input(' Qual o ano que deseja saber se e bissexto? '))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano e bissexto')
else:
    print('Ano nao e bissexto')
"""
#PEGANDO ANO ATUAL DA MAQUINA IMPORTANTISSIMO#
from datetime import date
ano = int(input(' Qual o ano que deseja saber se e bissexto? '))
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    ano = date.today().year # ano recebe ano atual do modulo data.today().year
    print('O ano e bissexto')
else:
    print('Ano nao e bissexto')
"""

"""
#Acho que finalmente entendi:
"ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.
"""
