frase = str(input('Digite uma frase: ')).upper().strip()
print('Nessa frase apareceram {} letras "A"'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('A')+1))