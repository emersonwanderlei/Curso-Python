entrada = input('[E]ntrar [S]air: ')
senha_digitada = int(input('Senha: '))

senha_permitida = int('12345')

if entrada == 'E' and entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    

#Exercicios de aplicacão do OR e AND