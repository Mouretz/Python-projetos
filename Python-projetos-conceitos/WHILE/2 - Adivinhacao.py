from random import randint

numero = randint(0,10)
palpite = 0
tentativa = int(input(' Digite o numero de 0 a 10 que acha ... '))
while tentativa != numero:
    tentativa = int(input(' QUAL SEU NOVO PALPITE? :'))
    palpite += 1
print('Voce ACERTOU')
print(f' Foram necessaria {palpite} tentativas ')
