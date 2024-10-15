# pessoa = {
#     'nome': 'Emerson',
#     'sobrenome': 'Wanderlei',
#     'idade': '26',
#     'altura': 1.66,
#     'endereço': [
#         {'rua': 'Candido Reis', 'numero': 601},
#         {'rua': 'Estrada do Coelho', 'numero': 36}]
# }

# for chaves in pessoa:
#     print(chaves, pessoa[chaves])

#MANIPULÇÃO DE DICIONARIO
#*********CRUD***********

# pessoa = {} # Criar dicionario

# chave = 'nome'

# pessoa[chave] = 'Emerson' # Atualizar dicionario incluindo itens
# pessoa['sobrenome'] = 'Wanderlei' # Atualizar dicionario incluindo itens

# del pessoa['sobrenome'] # Apagar itens do dicionario
# print(pessoa)

pessoa = {
    'nome': 'Emerson',
    'sobrenome': 'Wanderlei',
    #'idade': 0,
}
chave = 'idade'
pessoa[chave] = 26

chave = 'endereço'
pessoa[chave] = 'Candido Reis, Coelho, São Gonçalo'

pessoa['endereço'] = 'Estrada do COELHO'
print(pessoa)

pessoa.update({
    'bairro': input('digite Coelho:')
})

for listagem in pessoa:
    print(listagem, pessoa[listagem])