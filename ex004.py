algo = input('Digite algo:')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanúmetico?', algo.isalnum())
print('Esta em maiúsculas?', algo.isupper())
print('Esta em minúsculas?', algo.islower())
print('Esta capitalizada?', algo.istitle())
