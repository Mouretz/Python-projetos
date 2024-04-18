soma = 0 #somador com inicio 0
cont = 0 #acumulador de loop inicio 0
for c in range(1,7):
    num = int(input(f' Digite O {c} VALOR '))

    if num % 2 ==0:
        soma = soma + c
        cont = cont + 1  # cont = a cada loop coma 1 no contador de voltas
print(f' Voce me informou {cont} valores pares e a soma foi de {soma} .')
