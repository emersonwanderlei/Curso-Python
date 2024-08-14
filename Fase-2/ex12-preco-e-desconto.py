preco = float(input('Qual o preço do produto? R$'))
desc = preco * 0.05
print('Parabéns, você acabou de receber 5% de desconto, de R${:.2f} você vai pagar somente R${:.2f}'.format(preco, preco - desc))
