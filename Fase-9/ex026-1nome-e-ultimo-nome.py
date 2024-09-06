frase = str(input('Digite uma frase: ')).upper().strip()
print('Essa frase tem {} letras "A"'.format(frase.count('A')))
print('O primeiro "A" está na {}ª posição'.format(frase.find('A')+1))
print('A ultima letra "A" está na {}ª posição'.format(frase.rfind('A')+1))