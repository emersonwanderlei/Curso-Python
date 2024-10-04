'''
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor especìfico.
Por padrão, funções Python retonan None (Não valor/nada)

Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.

Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

'''

# def soma (x, y):
#     print(x + y)

# soma(2, 8)

def soma (*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total += numero
        print('Total', total)
    print(total)

soma(1, 2, 3, 4, 5, 6)
