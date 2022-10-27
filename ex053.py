frase = str(input('Digite uma frase: ')).upper() .strip() .split()
junção =''.join(frase)
inverso = junção[::-1]
print('A Frase que vc escreveu é {} e o inverso dela é {}.'.format(junção, inverso))
if junção == inverso:
    print('Essa frase é um PALÍNDROMO.')
else:
    print('Essa frase não é um PALÍNDROMO.')