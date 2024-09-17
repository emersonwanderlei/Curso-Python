senha_salva = '123456'
senha_digitada = ''
repetições = 0

while True:
    senha_digitada = input('Qual sua senha: ')
    if senha_digitada != senha_salva:
        print(f'Senha não confere {repetições}. Digite novamente: ')
        repetições += 1
        continue
    else:
        print('Você está logado')
        break
