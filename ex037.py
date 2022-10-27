n = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
[ 1 ] Conversão para BINÁRIO
[ 2 ] Conversão para OCTAL
[ 3 ] Conversão para HEXADECIMAL''')
opção = str(input('Sua opção: '))
if opção == '1':
    print('\033[1;33;40mO {} em binário é: {}\033[m'.format(n, bin(n)[2:]))
elif opção == '2':
    print('\033[1;34;40mO {} em octal é: {}\033[m'.format(n, oct(n)[2:]))
elif opção == '3':
    print('\033[1;36;40mO {} em hexadecimal é: {}\033[m'.format(n, hex(n)[2:]))
else:
    print('Opção invalida tente novamente.')

