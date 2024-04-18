frase = str(input('Digite a frase ou nome: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um PALINDROMO')
else:
    print('A PALAVA E NORMAL')