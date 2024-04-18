print('Condicao de P.A ')
print('-=' * 10)
primeiro = int(input('Digite um primeiro termo'))
razao = int(input('Digite uma razao '))
termo = primeiro
cont = 1 # Contar quantos termos

while cont <=10: # enquanto contador nao chegar a 10
    print(f' {termo} ->')
    termo = termo + razao
    cont += 1