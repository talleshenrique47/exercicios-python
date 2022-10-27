prod = float(input('Digite o preço do produto para geral o novo valor com desconto: R$'))
desc = prod-(prod*5/100)
print('O seu novo valor com 5% de desconto é: R${:.2f}'.format(desc))
