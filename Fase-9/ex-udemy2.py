"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''n1 = int(input('Digite um número inteiro: '))

if n1 % 2 == 0:
    print('Este é um número par')
else:
    print('Este é um numero impar')
'''
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = int(input('Quantas horas? '))

if entrada >= 0 and entrada <=11:
    print('Bom dia!')
elif entrada >= 12 and entrada <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""