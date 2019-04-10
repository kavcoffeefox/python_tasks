# -*- coding: UTF-8 -*-
# На вход программе мы подадим коэффициенты a, b и c -
# ваша цель напечатать 2 корня квадратного уравнения (каждый с новой строки).

import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b*b - 4*a*c
if d == 0:
    x1 = x2 = -1 * b/(2*a)
elif d > 0:
    x1 = (-1*b + math.sqrt(b*b-4*a*c)) / 2*a
    x2 = (-1*b - math.sqrt(b*b-4*a*c)) / 2*a
else:
    raise Exception("Корней нет")

print(int(x1))
print(int(x2))
