from math import sqrt, pow, hypot
opo = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
#hip = (pow(opo, 2))+(pow(adj, 2))
hip = hypot(opo, adj)
#hip = (opo**2)+(adj**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))