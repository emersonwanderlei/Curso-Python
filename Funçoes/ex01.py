# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total


multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)