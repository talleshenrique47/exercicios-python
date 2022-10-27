n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centeza: {}'.format(c))
print('Milhar:  {}'.format(m))

'''n = str(input('Digite um número de 0 a 9999: ')).zfill(4).strip()
print('Unidade: {}'.format(n[3]))
print('Dezena:  {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar:  {}'.format(n[0]))'''




