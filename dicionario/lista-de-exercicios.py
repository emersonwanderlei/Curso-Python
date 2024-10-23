# 1- Crie um dicionário que represente informações sobre uma pessoa,
# como nome, idade, cidade natal e profissão.

pessoa = {
    'nome': 'Emerson',
    'idade': 26,
    'cidade natal' : 'São Gonçalo-RJ',
    'profissão': 'Militar',
}

pessoa['nome'] = 'Matheus'
pessoa.update({
    'email': 'emerson.wanderlei03@gmail.com',
    'cor': 'Negão',
})

for lista in pessoa:
    print(lista, pessoa[lista])