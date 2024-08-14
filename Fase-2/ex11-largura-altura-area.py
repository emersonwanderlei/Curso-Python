larg = float(input("Qual a largura da parede? "))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print('De acordo que a medida {} x {} sua area é de {}'.format(larg, alt, area))
tinta = area/2
print('Você precisa de {} litros de tinta para pintar a parede'.format(tinta))