#CALCULADOR COM WHILE

while True:
    n1 = (input('Digite um número: '))
    n2 = (input('Digite outro número: '))

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    escolha = int(input(('Qual operação deseja realizar: ')))

    soma = n1 + n2
    subtracao = n1 - n2
    multplicacao = n1 * n2
    divisao = n1 / n2
    numeros_validos = None
    sair = 'sim' or 's'
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True 
    except:
        numeros_validos = None

    if numeros_validos is None:
        print(' Um ou ambos os valores são invalidos, digite um numero válido')
        continue

    if escolha == 1:
        print(f'{n1_float} + {n2_float} é = {soma}')
    elif escolha == 2:
        print(f'{n1_float} + {n2_float} é = {subtracao}')
    elif escolha == 3:
        print(f'{n1_float} + {n2_float} é = {subtracao}')
    elif escolha == 4:
        print(f'{n1_float} + {n2_float} é = {subtracao}')
    else:
        print('Não entendi. Qual operação deseja realizar: ')

    print('Quer sair [s]im [n]ão')
    if sair is True:
        break



