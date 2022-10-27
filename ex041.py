from datetime import date
nasc = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria MIRIM.')
elif idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade <= 19:
    print('Você está na categoria JÚNIOR.')
elif idade <= 25:
    print('Você está na categoria SÊNIOR.')
elif idade > 25:
    print('Você está na categoria MASTER.')