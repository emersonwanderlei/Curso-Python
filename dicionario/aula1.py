pessoa = {
    'nome': 'Emerson',
    'sobrenome': 'Wanderlei',
    'idade': '26',
    'altura': 1.66,
    'endereço': [
        {'rua': 'Candido Reis', 'numero': 601},
        {'rua': 'Estrada do Coelho', 'numero': 36}]
}

for chaves in pessoa:
    print(chaves, pessoa[chaves])