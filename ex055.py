maior = 0
menor = 0
for p in range(1, 6):
    weight = float(input('Peso da {}º pessoa em Kg: '.format(p)))
    if p == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))

