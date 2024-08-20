nome = (input('Favor, digite seu nome para fazermos uma análise: ')).strip() #strip == retirar espaços antes ou depois da palavra
ma = nome.upper()
mi = nome.lower()
separar = len(nome) - nome.count(' ') #remover espaço entre uma palavra
print('Seu nome em maiusculo fica {}'.format(ma))
print('Seu nome em minisculo fica {}'.format(mi))
print('Ao todo o nome {} tem {} letras'.format(nome, separar))
primeiroNome = nome.find(' ')
print('Seu primeiro nome tem {} letras'.format(primeiroNome))