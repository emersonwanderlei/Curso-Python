import random # Coisas aleatorias

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9)) # randint é igual a random + int para numeros

contagem_regressiva = 10
resultado = 0
#CALCULDO PRIMEIRO DIGITO
for digito_1 in nove_digitos:
    resultado += int(digito_1) * contagem_regressiva
    contagem_regressiva -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

#CALCULO SEGUNDO DIGITO
dez_digitos = nove_digitos + str(digito_1)
contagem_regressiva = 11
resultado = 0
for digito_2 in dez_digitos:
    resultado += int(digito_2) * contagem_regressiva
    contagem_regressiva -= 1
digito_2 = (resultado * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0

cpf_gerado_pelo_calculo = dez_digitos + str(digito_2)

print(cpf_gerado_pelo_calculo)