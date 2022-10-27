soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {}º Número: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números PARES e a soma deles é igual a {}.'.format(cont, soma))

