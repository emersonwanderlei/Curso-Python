salario = float(input('Qual o seu salario? R$'))
novo = salario + (salario*15/100)
print ('Parabéns, você recebeu aumento de 15%, ou seja, você não receberá R${}, você passará a receber R${} reais'.format(salario, novo))