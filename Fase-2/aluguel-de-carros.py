km = float(input('Quantos Km vai percorrer? '))
dias = int(input('Quantos dias vai alugar? '))
diariaCarro = dias * 60.00
kmRodado = km * 0.15
preco = diariaCarro + kmRodado
print('Para {} km e {} dias... o total é de R${}'.format(km, dias, preco))
