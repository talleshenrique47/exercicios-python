from time import sleep
print('-=-'*23)
print('Digite o valor de 3 lados para saber se dará pra formar um triângulo.')
print('-=-'*23)
v1 = float(input('Primeiro Valor: '))
v2 = float(input('Segundo Valor: '))
v3 = float(input('Terceiro Valor:'))
print('Analisando...')
sleep(2)
if (v2 - v3) < v1 < (v2 + v3) and (v1 - v3) < v2 < (v1 + v3) and (v1 - v2) < v3 < (v1 + v2):
    print('Com esses valores É POSSIVEL formar um triângulo!')
else:
    print('Com esses valores NÃO É POSSIVEL formar um triângulo!')

