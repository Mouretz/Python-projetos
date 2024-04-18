casa = float(input('Informe o valor da casa '))
salario = float(input('Informe o Salario Mensal '))
parcela = int(input('Quantos anos quer pagar : '))

mensalidade = casa / (parcela * 12)# Conta para saber o valor da mensalidade = Prestacao / por ANO
possivel = salario * 0.30 # Conta de 30% do salario mensal para pagar emprestimo

print(f' Para pagar uma casa no valor de {casa}, em {parcela} anos a prestacao sera de {mensalidade}')


if possivel <= mensalidade: # Se 30% do salario nao pagar a parcela, emprestimo negado
    print('Emprestimo Negado ')
else:
    print('Emprestimo Aceito ')


