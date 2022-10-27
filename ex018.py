from math import sin, cos, tan, radians
a = float(input('Digite o ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tang = tan(radians(a))
print('O ângulo de {} tem como: Seno de: {:.4f} Cosseno de: {:.4f} Tangente de: {:.4f}'.format(a, sen, cos, tang))
