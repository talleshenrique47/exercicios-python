lar = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
m2 = lar * alt
tinta = m2/2
print('A sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(lar, alt, m2))
print('Para pintar sua parede você precisara de {}l de tinta.'.format(tinta))
