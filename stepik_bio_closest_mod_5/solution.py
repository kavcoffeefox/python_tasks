# -*- coding: UTF-8 -*-
import sys


def closest_mod_5(x):
    return (5 - (x % 5)) + x if x % 5 is not 0 else x


if __name__ == "__main__":
    print(closest_mod_5(int(sys.argv[1])))
