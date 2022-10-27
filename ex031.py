viagem = float(input('Qual a distancia da viagem?'))
print('Você fará um viagem de {}Km.'.format(viagem))
#preço = viagem*0.50 if viagem <=200 else viagem*0.45
if viagem <= 200:
    preço = viagem*0.50
else:
    preço = viagem*0.45
print('A viagem custará R${:.2f}'.format(preço))
print('Boa Viagem!!')