vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel-80)*7
if vel >80:
    print('Você está acima do limite de velocidade. Você foi MULTADO!!')
    print('A sua multa vai custar R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!!')