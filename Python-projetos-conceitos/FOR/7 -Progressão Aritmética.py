print('   10 TERMOS DE 1 PA     ')

primeiro = 0
razao = 2
decimo = primeiro + (10-1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f'{c}',end=' ')
print('ACABOU')


