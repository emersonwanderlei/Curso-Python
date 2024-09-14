'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

Operadores de atribuição
= += -= *= /= //= **= %=

contador = 0

while contador <= 10:
    print(contador)
    contador += 1
print('Acabou')
'''
nome = 'Emerson'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
print('REFAZER QUANDO VISUALIZAR')