'''
resposta = 'Ss'
while resposta in "Ss":
    ...........
'''
soma = quant = media = maior = menor = 0
op='S'
while op != 'N':
    num = int(input('digite um numero: '))
    soma += num
    quant += 1
    if quant ==1: # lendo da primeira pessoa
        maior = menor = num # a primeira vai ser o maior e menor numero
    else: # se nao for o primeiro laco
        if num > maior: # se o proximo numero for maior que o anterior 'maior'
            maior = num # maior se torna o que acabei de ler
        if num < menor:
            menor = num

    op = str(input('quer continuar? [S/N]')).upper().strip()[0] # 0 considerar primeira letra
media = soma / quant

print(f'voce digitou {quant} numeros , e a media foi {media}')
print(f'o maior valor foi {maior} e o menor foi { menor}')




