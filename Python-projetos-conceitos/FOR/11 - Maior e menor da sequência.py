
maior = 0
menor = 0

for p in range(1,5): # para pessoas em um intervalo de 1 a 6
    peso = float(input(f'Peso da {p}a pessoa :' ))
    if p == 1: # se o pesso da primeira pessoa foi utilizado a contadora p verifica se e 1
        maior = peso
        menor = peso
    else:
        if peso > maior: # Se peso verificado for maior que o maior peso que tenho, maior do q o maior
            maior = peso # Maior peso se torna o peso que acabei de ler
        if peso < menor: # SE o peso for menor do que o menor peso
            menor = peso # o menor peso passa a ser o peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')

#lista_pessoas = []
#for c in range(5):
#    peso = int(input("Digite o peso atual"))
#    lista_pessoas.append(peso)
#lista_pessoas.sort()
#print("=" *40 )
#print("A pessoa mais PESADA tem: ",lista_pessoas[-1],"Kg")
#print("A pessoa mais LEVE tem: ,",lista_pessoas[0],"Kg")