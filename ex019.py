from random import choice
a1 = str(input('Digite o nome do primeiro aluno :'))
a2 = str(input('Digite o nome do segundo aluno:'))
a3 = str(input('Digite o nome do terceiro aluno:'))
a4 = str(input('Digite o nome do quarto aluno:'))
lista = [a1, a2, a3, a4]
esc = choice(lista)
#esc = choice([a1, a2, a3, a4])
print('O aluno que vai ter que apagar o quadro é o {}'.format(esc))
