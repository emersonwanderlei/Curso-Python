import math
o = float(input("Qual o comprimento do cateto oposto? "))
a = float(input('Qual o compimento do cateto adjacente? '))
h = math.hypot(o, a)
print('Tendo em vista que o cateto oposto é {} e o cateto adjacente é {}. O comprimento da hipotenusa é {:.2f}'.format(o, a, h))
3