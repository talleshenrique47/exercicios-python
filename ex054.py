from datetime import date
ano = date.today().year
contplus = 0
contless = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    age = ano - nasc
    if age > 18:
        contplus += 1
    else:
        contless += 1
print('Das 7 pessoas {} são MAIORES de idade e {} são MENORES de idade.'.format(contplus, contless))

'''for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    if nasc +18 <= ano:
        cont += 1
    elif nasc +18 >= ano:
        cont1 += 1
print('Das 7 pessoas {} são MAIORES de idade e {} são MENORES de idade.'.format(cont, cont1))'''
