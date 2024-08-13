import math
n = float(input('Qual ângulo deseja calcular? '))
sen = math.sin(n)
cos = math.cos(n)
tan = math.atan(n)
print("O seno de {} é {:.2f}".format(n, sen))
print('O cosseno de {} é {:.2f}'.format(n, cos))
print('A tangente de {} é {:.2f}'.format(n, tan))