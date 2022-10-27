print('{:=^40}'.format(' LOJAS BABIDI '))
valor = float(input('Digite o valor das compras: R$ '))
print('Escolha a forma de pagamento.')
print('''[1] à vista dinheiro ou cheque.
[2] à vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão.''')
opção = int(input('Sua opção: '))
if opção == 1:
    preço = valor - (valor * 10/100)
elif opção == 2:
    preço = valor - (valor * 5/100)
elif opção == 3:
    preço = valor
    parcela = valor / 2
    print('Sua compra será parcelada em 2x e ficará por R${:.2f} SEM JUROS.'.format(parcela))
elif opção == 4:
    preço = valor + (valor * (20/100))
    totparc = int(input('Quantas parcelas? '))
    parcela = preço / totparc
    print('Sua compra será parcelada em {}x e ficará por R${:.2f} COM JUROS.'.format(totparc, parcela))
else:
    preço = valor
    print('\033[1;31mOpção INVALIDA de pagamento, tente novamente!\033[m')
print('Sua compra no valor de R${:.2f} custará R${:.2f} no final.'.format(valor, preço))
