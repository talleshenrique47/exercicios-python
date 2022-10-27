valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu sálario? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
parcela = valor / (anos * 12)
mensal = salario * (30/100)
print('A casa no valor de R${:.2f} em {:.0f} anos a prestação ficará em R${:.2f}'.format(valor, anos, parcela))
if mensal <= parcela:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo ACEITO!')
print('omparando parcela {} mensal {}'.format(parcela, mensal))