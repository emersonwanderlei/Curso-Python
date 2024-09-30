"""
Calculo do primeiro dígito do CPF                                       Calculo do segundo dígito do CPF
CPF: 746.824.890-70                                                     CPF: 746.824.890-70 
Colete a soma dos 9 primeiros dígitos do CPF                            Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma                               MAIS O PRIMEIRO DIGITO,
contagem regressiva começando de 10                                     multiplicando cada um dos valores por uma    
a                                                                       contagem regressiva começando de 11
  Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0                                           Ex.:  746.824.890-70 (7468248907)
                                                                        11 10  9  8  7  6  5  4  3  2
                                                                    *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
                                                                        77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:                                              Somar todos os resultados:                                
70+36+48+56+12+20+32+27+0 = 301                                         77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10                                 Multiplicar o resultado anterior por 10
301 * 10 = 3010                                                         363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11                       Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7                                                           3630 % 11 = 0
Se o resultado anterior for maior que 9:                                Se o resultado anterior for maior que 9:
    resultado é 0                                                       resultado é 0
contrário disso:                                                        contrário disso:
    resultado é o valor da conta                                        resultado é o valor da conta

O primeiro dígito do CPF é 7                                             O segundo dígito do CPF é 0

"""
import re
import sys
# cpf = '746.824.890-70'\
#     .replace('.', '')\
#     .replace('-', '')\
#     .replace(' ', '') #Substitur valores por outros
#ou AULA 102 CURSO DE PYTHON
cpf = re.sub(
    r'[^0-9]',
    '',
    '746.824.890-70'
)

entrada_sequencial = cpf == cpf[0] * len(cpf)
if entrada_sequencial:
    print('Você digitou valores iguais')
    sys.exit()
    
nove_digitos = cpf[:9] #fatiamento de str
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

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print(f'{cpf} é inválido')