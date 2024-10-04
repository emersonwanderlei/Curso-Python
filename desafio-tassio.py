senha_permitida = 'Wander7!'
caracter_especiais = '!@#$%^&*()'

def login():
    while True:
        senha_digitada = input('Digite sua senha: ')

        if senha_digitada in senha_permitida:
            print('Login permitido')
        if senha_digitada != senha_permitida:
            print('Senha não confere, digite novamente')
            continue
        if len(senha_digitada) == 8:
            print('Login permitido')
        else:
            print('Digite pelo menos 1 caracter especial')
                


login()