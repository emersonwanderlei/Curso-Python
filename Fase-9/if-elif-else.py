#Introdução ao If |   elif    | else
#              se | se não se | se não
entrada = input('Você quer "entrar" ou "sair"? : ').lower()

if entrada == "entrar":
    print("Bem-vindo! Você acessou o sistema.")
elif entrada == "sair":
    print('Você saiu do sistema')
else:
    print('ERRO. Você não digitou nem "entrar" e nem "sair"')
