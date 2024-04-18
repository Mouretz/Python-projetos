num = int(input(' Informe um numero qualquer: '))
print('-='*30)
conta = num % 2 # o resto de uma dividao por 2 de um numero: par e 0  e  1 se for impar
if conta == 0:
    print('Este numero e par')
else:
    print('numero Impar')


