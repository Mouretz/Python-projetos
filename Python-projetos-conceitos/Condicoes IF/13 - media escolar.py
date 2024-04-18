nota1 = float(input(' INFORME A NOTA 1 '))
nota2 = float(input(' INFORME A NOTA 2 '))

media = (nota1 + nota2) /2

if media >=5 and media < 7:  # IF FUNCAO ENTRE 2 NUMEROS
    # OU if 7 > media >= 5: # PYTHON ACEITA IMPORTANTISSIMO
    print(' o aluno esta em RECUPERACAO')
elif media < 5: # menor que reprovado
    print(' esta reprovado')
elif media >= 7: # 7 ou mais
    print(' APROVADO')




