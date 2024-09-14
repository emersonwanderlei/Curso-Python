#CALCULADOR COM WHILE

while True:
    print('CALCULADOR USANDO O WHILE')
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('-' * 20)
    print('Digite o número de 1 a 4, referente a operação')
    operador = input(('Qual operação deseja realizar: '))
    
    numeros_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True 
    except:
        numeros_validos = None

    if numeros_validos is None:
        print(' Um ou ambos os valores são invalidos, digite um numero válido')
        continue

    if operador == '1':
        print(f'{n1_float} + {n2_float} é = ', n1_float + n2_float)
    elif operador == '2':
        print(f'{n1_float} - {n2_float} é = ', n1_float - n2_float)
    elif operador == '3':
        print(f'{n1_float} * {n2_float} é = ', n1_float * n2_float)
    elif operador == '4':
        print(f'{n1_float} / {n2_float} é = ', n1_float / n2_float)
    else:
        print('Não entendi. Qual operação deseja realizar: ')
        continue

    sair = str(input('Quer sair [s]im [n]ão: '))
    if sair == 'sim' or sair == 's':
        print('Você saiu...')
        break
    else:
        continue



