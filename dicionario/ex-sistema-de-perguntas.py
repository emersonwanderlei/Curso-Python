# Exercício - sistema de perguntas e respostas

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]
#------------------------------------------------------------------------------------------------------

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['5', '10', '30', '2'],
        'Resposta': '5',
    },
]
qtd_acertou = 0
for pergunta in perguntas:
    questoes = pergunta['Pergunta']
    print(questoes)
    print()

    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i})', opcoes)
    resposta = input('Escolha qual opção: ')
    
    resposta_int = None
    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int >= 0 and resposta_int <= len(opcoes):
        acertou = False
        if resposta_int == pergunta['Resposta']:
            acertou = True
        if acertou:
            print('Você ACERTOU!')
        else:
            print('Você ERROU')
    break