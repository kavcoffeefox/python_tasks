# -*- coding: UTF-8 -*-
# Напишите реализацию функции closest_mod_5,
# принимающую в качестве единственного аргумента целое число x
# и возвращающую самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5
import sys


def closest_mod_5(x):
    return (5 - (x % 5)) + x if x % 5 is not 0 else x


if __name__ == "__main__":
    print(closest_mod_5(int(sys.argv[1])))
