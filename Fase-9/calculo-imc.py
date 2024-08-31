#Calculo de Massa Corporea

nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso:' ))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('{} tem {} de altura'.format(nome, altura))
print( 'pesa {} quilos e seu IMC é {:.2f}'.format(peso, imc))