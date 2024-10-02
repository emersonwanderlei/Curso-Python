


cpf = '17538584706'
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado = int(digito) * contador_regressivo
    contador_regressivo -= 1
print(resultado)
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0
print(digito_1)