from random import choice
print('Iremos fazer um sorteio, digite 4 nomes')
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
sorteio = [n1, n2, n3, n4]
escolhido = choice(sorteio)
print('O escolhido foi {}'.format(escolhido))
