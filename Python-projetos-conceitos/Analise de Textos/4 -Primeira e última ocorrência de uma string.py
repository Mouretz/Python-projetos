frase = str(input('Digite a frase ')).upper().strip() # upper deixar em maisuculo e strip tirar espaco
print(f'a letra A aparece {frase.count("A")}')
print(f'a letra A aparece {frase.find("A")+1}') # primeira posicao da letra A , +1 para retirar a contagem ZERO
print(f'a letra A aparece {frase.rfind("A")+1}') # rfind - procura apartir do lado direito!

