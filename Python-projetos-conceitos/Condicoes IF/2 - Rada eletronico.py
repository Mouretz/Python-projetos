Vcarro = float(input(' Informe a velocidade do carro? '))

if Vcarro > 80.0:
    print('Voce foi multado')
    multa = (Vcarro - 80)*7 # ultrapassar 80 , a multa e de 7 reais por km rodado [Vl - 80 km  * Reais]
    print(f'O valor da sua multa foi de {multa} Reais')


