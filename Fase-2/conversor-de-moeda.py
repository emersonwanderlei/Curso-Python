real = float(input('Quanto você tem na carteira? R$'))
dolar = real/5.51
print('Com R${} reais você pode comprar US${:.2f} dolar'.format(real, dolar))