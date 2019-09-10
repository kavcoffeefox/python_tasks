# -*- coding: UTF-8 -*-
import numpy as np
inp_list = input().split()
if len(inp_list) < 1:
    pass
elif len(inp_list) == 1:
    Z = np.zeros(int(inp_list[0]))
elif inp_list[-1].isdigit():
    Z = np.zeros(list(map(int, inp_list)))
else:
    Z = np.zeros(list(map(int, inp_list[:-1])), dtype=inp_list[-1])
