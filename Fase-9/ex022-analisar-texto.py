'''nome = (input('Favor, digite seu nome para fazermos uma análise: ')).strip() #strip == retirar espaços antes ou depois da palavra
ma = nome.upper()
mi = nome.lower()
separar = len(nome) - nome.count(' ') #remover espaço entre uma palavra
print('Seu nome em maiusculo fica {}'.format(ma))
print('Seu nome em minisculo fica {}'.format(mi))
print('Ao todo o nome {} tem {} letras'.format(nome, separar))
primeiroNome = nome.find(' ')
print('Seu primeiro nome tem {} letras'.format(primeiroNome))
'''
#REFAZER QUANDOR VISUALIZAR NOVAMENTE

nome = str(input('Digite seu nome pra fazer uma analise ?')).strip()
print("Seu nome em maisculo é {}".format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('O nome {} tem {} letras'.format(nome, len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
n = nome.split()
print('Seu ultimo nome é {}'.format(n[len(n)-1]))
