nome = str(input('Digite seu nome completo: ')).title().strip()
print('Analisando seu nome ....')
print('O seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('O seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
snome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(snome[0], len(snome[0])))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))
#print('O nome completo possui {} letras'.format(len(''.join(snome))))



'''snome = nome.replace(' ', '')
n3 = len(snome)
print('Seu nome ao todo tem {} letras'.format(n3))
snome2 = nome.split()
n4 = len(snome2[0])
print('Seu primeiro nome é {} e ele tem {} letras.'.format(snome2[0], n4))'''
