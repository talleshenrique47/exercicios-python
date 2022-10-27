from datetime import date
print('Qual é o seu sexo: ')
print('[1] Masculino')
print('[2] Feminino')
sexo = str(input('Sua opção: '))
if sexo == '1':
    nasc = int(input('Qual seu ano de nascimento? '))
    atual = date.today().year
    idade = atual - nasc
    print('Quem nasceu no ano de {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
        print('Seu alistamento será em {}.'.format(atual + saldo))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        saldo = idade - 18
        print('Você já DEVERIA ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(atual - saldo))
elif sexo == '2':
    print('Você está dispensada do serviço militar.')


