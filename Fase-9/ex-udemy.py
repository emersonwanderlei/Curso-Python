nome = str(input('Digite seu nome: '))
idade = int(input('Qual sua idade: '))
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém {nome.count(' ')} espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você  deixou campos vazios')