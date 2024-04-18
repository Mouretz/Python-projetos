somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0
for p in range(1,5):
    print(f'---- {p}a PESSOA ------')
    nome = str(input('Nome: '))
    idade = int(input('IDADE: '))
    sexo = str(input('GENERO [M/F] ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': # in Mm igual a .upper -- se le ou M maiusc/ m Minusculo
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1 # para guardar o numero de mulheres com menos de 20.
mediaidade = somaidade /4
print(f'A media de idades e de: {mediaidade}')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho} ')
print(f'Sao {totmulher} mulheres com menos de 20 anos!!!')

