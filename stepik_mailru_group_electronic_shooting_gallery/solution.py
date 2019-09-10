# -*- coding: UTF-8 -*-
import math

count_shut = int(input())
sum_points = 0
for _ in range(count_shut):
    x, y = map(float, input().split())
    r_xy = math.sqrt(x**2 + y**2)
    if r_xy < 1:
        sum_points += 10
    elif r_xy < 2:
        sum_points += 9
    elif r_xy < 3:
        sum_points += 8
    elif r_xy < 4:
        sum_points += 7
    elif r_xy < 5:
        sum_points += 6
    elif r_xy < 6:
        sum_points += 5
    elif r_xy < 7:
        sum_points += 4
    elif r_xy < 8:
        sum_points += 3
    elif r_xy < 9:
        sum_points += 2
    elif r_xy < 10:
        sum_points += 1
    elif r_xy >= 10:
        sum_points += 0


print(sum_points)

