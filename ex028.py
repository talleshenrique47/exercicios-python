from random import randint
from time import sleep
n = randint(0,5) #faz o computador "PENSAR
print('-=-'*20)
print('Descubra o número que eu estou pensando entre 0 e 5...')
print('-=-'*20)
r = int(input('Em que número eu estou pensando? ')) #jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(2)
if r == n:
    print('PARABENS VOCÊ GANHOU!!!')
else:
    print('O VENCEDOR FOI A MAQUINA!!!')
    print('Eu estava pensando no número {}'.format(n))