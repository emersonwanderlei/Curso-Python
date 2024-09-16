#CALCULADORA USANDO WHILE

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Qual operação: (+-*/) ')

    numero_valido = 0

    try:
        num1_float = float(n1)
        num2_float = float(n2)
        numero_valido = True
    except:
        numero_valido = None
        
    if numero_valido is not True:
        print('Um ou ambos os números são invalidos. Digite novamente!')
        continue

    if operador == '+':
        print(f'{num1_float} + {num2_float}=', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float}=', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float}=', num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float}=', num1_float / num2_float)
    else:
        print('Digite um operador válido')
        continue
    sair = input('Quer sair [s]im [n]ão: ')
    if sair == 'sim' or sair == 's':
        break
    else:
        continue
