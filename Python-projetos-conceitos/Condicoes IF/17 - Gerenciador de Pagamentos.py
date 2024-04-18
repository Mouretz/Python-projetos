preco = float(input(' Informe o preco normal do produto: '))
print(''' FORMAS DE PAGAMENTO
[1] A VISTA
[2] A VISTA NO CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS
''')
opcao = int(input(' qual a opcao?'))

vista = preco - (preco*0.10)
vista_cartao = preco - (preco*0.05)
juros2 = preco/2
juros3 = preco + (preco * 0.20) # valor de preco + juros de 20% = juros 3



if opcao == 1:
    print(f'O valor a vista fica {vista}')
elif opcao == 2:
    print(f'O valor 1x no cartao fica {vista_cartao}')
elif opcao ==3:
    print(f'O valor ficara em 2 vezes de {juros2}')
elif opcao ==4:
    totparc = int(input('QUANTAS PARCELAS?'))
    real = juros3 / totparc # JUROS3 ou total com juros de 20, divido por parcela = mensalidade
    print(f'sua compra de {totparc}vezes ficara no total de {real}')
    print(f'o total da sua compra que era {preco} ficara {juros3}') # {}preco e {}preco mais juros




