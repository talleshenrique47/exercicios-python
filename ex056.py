somaage = 0
mediaage = 0
nameman = ''
ageman = 0
agegirl = 0
for data in range(1, 5):
    print('='*7, '{} Pessoa'.format(data), '='*7)
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip()
    somaage += age
    if data == 1:
        nameman = name
        ageman = age
    if age > ageman and gender in 'Mm':
        nameman = name
        ageman = age
    if age < 20 and gender in 'Ff':
        agegirl += 1
mediaage = somaage / 4
print('A média de idade do grupo é de {} anos.'.format(mediaage))
print('O homem mais velho tem a idade de {} anos e se chama {}.'.format(ageman, nameman))
print('Tem {} mulheres com menos de 20 anos.'.format(agegirl))
