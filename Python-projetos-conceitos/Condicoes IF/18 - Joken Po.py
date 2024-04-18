from random import randint

print('''
INFORME SUAS OPCOES
[1] Papel
[2] Tesoura
[3] Pedra
''')
opcao = int(input(' Informe uma opcao :'))
print(' JOKEN --- PO')
pc = randint(1,3)
print(pc)
if opcao ==1 and pc ==2:
    print('Voce perdeu para TESOURA')
elif opcao ==1 and pc ==3:
    print('Voce ganhou da PEDRA')
elif opcao ==2 and pc ==1:
    print('Voce ganhou DO PAPEL')
elif opcao ==2 and pc ==3:
    print('Voce perdeu para PEDRA')
elif opcao ==3 and pc ==1:
    print('Voce Perdeu para PAPEL')
elif opcao ==3 and pc==2:
    print(' Voce ganhou da TESOURA')
else:
    print('DEU empate')



