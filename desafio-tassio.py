


def contem_caracteres_especiais(senha):
    caracter_especiais = '!@#$%^&*()'

    for letra in senha:
        if letra in caracter_especiais:
            return True

    return False

def contem_letra_maiscula(senha):

    for letra_mais in senha:
        if letra_mais.isupper():
            return True
    return False

def contem_letra_miniscula(senha):

    for letra_minis in senha:
        if letra_minis.islower():
            return True
    return False

def contem_numeros(senha):

    for numero in senha:
        if numero.isdigit():
            return True
    return False

def login():
    while True:
        senha = input('Digite sua senha com 8 digitos, 1 caracter especial, 1 letra maiuscula, 1 letra minuscula: ')
        if len(senha) == 8 and contem_caracteres_especiais(senha) and contem_letra_maiscula(senha) and contem_letra_miniscula(senha) and contem_numeros(senha):
            print('Senha Valida.')
            break
        else:
            print('Senha Invalida!')    

print('VALIDADOR DE SENHA')      
login()