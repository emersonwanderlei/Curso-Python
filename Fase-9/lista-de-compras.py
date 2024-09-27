"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print(10*'-', 'LISTA DE COMPRAS', 10*'-')
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        for indice, listagem in enumerate(lista):
            print(indice, listagem)
        indice_str = input('Digite o indice para apagar: ')

        try:
            indice_int = int(indice_str)
            del lista[indice_int]

        except:
            print('Digite novamente.')
        
    elif opcao == 'l':
        os.system('cls')
        for indice, listagem in enumerate(lista):
            print(indice, listagem)
        
    else:
        os.system('cls')
        print('Atenção!!!')
        print('apenas i, a ou l')
