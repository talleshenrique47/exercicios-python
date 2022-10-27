d = float(input('Quanto de dinheiro tem na sua carteira? R$'))
dolar = d / 5.88
euro = d / 6.96
print('Com R$ {:.2f} você pode comprar US${:.2f}'.format(d, dolar))
print('Com R$ {:.2f} você pode comprar €{:.2f}'.format(d, euro))