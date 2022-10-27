s = float(input('Digite o salario do funcionario para receber o reajuste de 15%: R$'))
s2 = (s*15/100)+s
print('O seu aumento foi de R${:.2f} e seu novo salario é: R${:.2f}'.format(s*0.15, s2))