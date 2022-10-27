from time import sleep
from random import randint
print('\033[1;35m{:=^40}\033[m'.format(' JO KEN PO '))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
escolha = int(input('Sua escolha é: '))
jokenpo = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
if escolha == 0 or escolha == 1 or escolha == 2:
    print('\033[1;36mJO\033[m')
    sleep(1)
    print('\033[1;36mKEN\033[m')
    sleep(1)
    print('\033[1;36mPO\033[m')
    sleep(1)
    print('-=' * 20)
    print('Computador jogou {}'.format(jokenpo[maquina]))
    print('Jogador jogou {}'.format(jokenpo[escolha]))
    print('-=' * 20)
    papel = (maquina == 'Papel' and escolha == 'Pedra')
    pedra = (maquina == 'Pedra' and escolha == 'Tesoura')
    tesoura = (maquina == 'Tesoura' and escolha == 'Papel')
    if papel or pedra or tesoura == True:
        print('\033[1;31mMÁQUINA VENCE.\033[m')
    elif maquina == escolha:
            print('\033[1;33mEMPATE.\033[m')
    else:
            print('\033[1;32mJOGADOR VENCE.\033[m')
else:
    print('Opção não existente, tente novamente.')
