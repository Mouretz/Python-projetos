

n1 = float(input(' Informe o numero 1: '))
n2 = float(input(' Informe o numero 2: '))
op = 0
while op != 5:
    print('''
    [1] - SOMAR
    [2] - MUTIPLIAR
    [3] - MAIOR
    [4] - NOVOS NUMEROS
    [5] - SAIR DO PROGRAMA
    ''')
    op = int(input(' QUAL SUA OPCAO? '))

    if op == 1:
        produto = n1 + n2
        print(produto)
    elif op == 2:
        muti = n1*n2
        print(muti)
    elif op == 3:
        if n1 > n2:
            maior = print(f'o Numero {n1} e maior que {n2}')
        else:
            print(f'o Numero {n2} e maior que {n1}')
    elif op ==4:
        n1 = int(input('Novo valor de n1'))
        n2 = int(input('Novo valor de n2'))
        novo = print(f' n1 agora vale {n1} e n2 {n2}')
    elif op ==5:
        print('ENCERRANDO ...')
    else:
        print('OPCAO INVALIDA')




