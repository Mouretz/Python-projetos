# 08 - Leia valor em metros, e exiba em cm e milimetros.
#Vl/ valor em  metros recebe do usuario um numero real
Vl = float(input('Digite valor em metros:  '))
#cm variavel de centimetros recebe a conversao de metros
cm = (Vl*100)
#ml variavel de milimetros recebe a conversao de metros
ml = (Vl*1000)
#mostra na tela uma saida formatada da variavel cm e ml
print(f'Sua medida em cm corresponde a : {cm} \n Sua medida em milimetros corresponde a {ml}')

