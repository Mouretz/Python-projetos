salar = float(input(' Informe o salario do funcionario '))
if salar > 1250.00:
    aumento = salar + (salar * 0.10) # Aumento e igual a salrio mais 10% do salario
    print(f'O aumento resulta em RS {aumento}')
if salar <= 1250.00:
    aumento = salar + (salar * 0.15) # Aumento e igual a salrio mais 15% do salario
    print(f'O aumento resulta em RS {aumento}')
