"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'perfume'
letra_acertada = ''
tentativa = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativa += 1

    if len(letra_digitada) > 1:
        print('Apenas um letra. digite outra vez')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!!')
        print(f'Sua palavra secreta é {palavra_secreta}')
        print(f'Tentativas {tentativa}')

        








'''
palavra_secreta = 'exercito'
letra_acertada = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').lower()
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada:{palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letra_acertada = ''
        tentativas = 0
'''