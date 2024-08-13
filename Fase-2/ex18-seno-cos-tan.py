import math
n = float(input('Qual ângulo deseja calcular? '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.atan(math.radians(n))
print("O seno de {} é {:.2f}".format(n, sen))
print('O cosseno de {} é {:.2f}'.format(n, cos))
print('A tangente de {} é {:.2f}'.format(n, tan))