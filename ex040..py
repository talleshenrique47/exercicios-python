nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('Sua média foi de {:.1f}'.format(média))
if média < 5:
    print('Você está REPORVADO.')
elif 5 <= média <= 6.9:
    print('Você está de RECUPERAÇÃO.')
elif média >= 7:
    print('Você está APROVADO.')

