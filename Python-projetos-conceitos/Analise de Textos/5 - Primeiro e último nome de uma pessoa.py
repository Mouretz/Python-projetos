n = str(input(' Digite seu nome completo ')).strip().upper()
nome = n.split() # separa os indices de n em uma lista ['','','']
print(f'o primeiro nome  {nome[0]}')
print(f'o ultimo nome  {nome[len(nome)-1]}') # nome menos quantidade deposicao -1 tirando a posicao zero


