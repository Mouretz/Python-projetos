nome =str(input(' Digite o nome completo ')).strip() # nome vai ser str cortando o espacos 'strip'
print(f'Seu nome Em maiuscula {nome.upper()} \n e seu nome Em minuscula {nome.lower()}')
print(f'numeros de letras {len(nome) - nome.count(" ")} ') # quantidade geral menos espacos count
print(f' numero de primeiro nome {nome.find(" ")} ') #encontre primeiro espaco





