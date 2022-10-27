carro = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilometros foram percorridos? '))
valor = (carro * 60) + (km * 0.15)
print('O valor do aluguel do carro foi de R${:.2f}'.format(valor))
