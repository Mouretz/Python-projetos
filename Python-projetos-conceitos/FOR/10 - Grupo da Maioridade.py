
from _datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0
for pessoas in range(1,8):
    nasc = int(input('Informe o ano de nascimento : '))
    idade = atual - nasc
    print(f' Esta pessoa tem {idade} anos!!!')

    if idade >= 21:
        print('DE MAIOR')

        totmaior += 1 # Se >= a 21 e mais 1 pessoa de maior
    else:
        print('DE MENOR')
        totmenor += 1 #Se nao e mais uma pessoa de menor
print(f' Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f' Ao todo tivemos {totmenor} pessoas menores de idade')

# maiores = 0
#for c in range(7):
    #ano_nascimento = int(input("Digite a idade"))
    #    if ano_nascimento >= 18:
#       maiores += 1

#print(f" Maiores : {maiores}")
#menores =  7 - maiores
#print(f"Menores : {menores}")
