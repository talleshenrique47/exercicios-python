print('='*19)
print('10 RAZÕES DE UMA PA')
print('='*19)
termo = int(input('1º termo: '))
razao = int(input('Razão: '))
decimo = termo+(10-1)*razao
for c in range(termo, decimo+1, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')