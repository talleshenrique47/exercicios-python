v1 = float(input('Primeiro Valor: '))
v2 = float(input('Segundo Valor: '))
v3 = float(input('Terceiro Valor: '))
lado1 = (v2 - v3) < v1 < (v2 + v3)
lado2 = (v1 - v3) < v2 < (v1 + v3)
lado3 = (v1 - v2) < v3 < (v1 + v2)
if lado1 and lado2 and lado3:
    print('Com esses valores é POSSIVEL formar um triângulo ', end='')
    if v1 == v2 == v3:
        print('EQUILÁTERO que possui os três lados iguais.')
    elif v1 != v2 != v3 != v1:
        print('ESCALENO que possui os três lados diferentes.')
    else:
        print('ISÓSCELES que possui dois lados iguais.')
else:
    print('Com esses valores é IMPOSSIVEL formar um triângulo.')