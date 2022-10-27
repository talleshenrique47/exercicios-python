sal = float(input('Qual é o seu salário: R$'))
if sal > 1250.00:
    print('voce recebeu 10% de aumento e seu novo salário é: R${:.2f}'.format(sal*(10/100)+sal))
else:
    print('voce recebeu 15% de aumento e seu novo salário é: R${:.2f}'.format(sal*(15/100)+sal))