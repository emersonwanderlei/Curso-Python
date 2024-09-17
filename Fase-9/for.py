'''
For + Range
range -> range(start, stop, step)
------------------------------------
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu interador
'''


nome = 'Emerson Wanderlei'

novo_nome = ''
for texto in nome:
    novo_nome += f'*{texto}'

print(novo_nome)