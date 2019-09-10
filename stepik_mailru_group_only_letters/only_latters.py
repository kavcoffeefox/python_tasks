# -*- coding: UTF-8 -*-
from functools import reduce
def only_latter(input_str):
    set_with_letters = set()
    for i in input_str.lower():
        if i.isalpha():
            set_with_letters.add(i)

    print(reduce(lambda x,y: x+y, sorted(set_with_letters)))

def only_latter_2(input_str):
    print("".join(sorted([ch for ch in set(input_str.lower()) if ch.isalpha()])))

if __name__ == "__main__":
    only_latter(input())