"""
n = 1
while n != 0: # Enquanto n  nao for zero ->
    n = int(input('Digite um valor ')) # Recebe valor inteiro
print('FIM')
"""
"""
r = 'S'
while r == 'S': # JA COMECA COM O VALOR VERDADEIRO E REALIZA _>
    n = int(input('Digite um valor ')) #Input do usuario enquanto ->
    r = str(input('Quer continuar [S/N] ')).upper() # R = receber outro valor FALSO diferente de S
print('Fim')

"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor '))
    if n % 2 ==0:
        par += 1
    else:
        impar += 1
print(f'Voce digitou {par} numeros pares, e {impar} numeros impares ')
