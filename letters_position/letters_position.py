# -*- coding: UTF-8 -*-
import re

str1 = input().lower()
str2 = re.sub(r"[^a-z]", '', input().lower())

array_with_result = {}

for a in str2:
    array_with_result[a] = []

for a in array_with_result.keys():
    count = 0
    for b in str1:
        count += 1
        if a == b:
            array_with_result[a].append(count)

for a in array_with_result:
    if len(array_with_result[a]) != 0:
        print(a, *array_with_result[a])
    else:
        print(a, "None")

# Альтернативное решение из интернета
# s1 = input().lower()
# s2 = input().lower()
# checked = set()
# for ch in s2:
#    if ch.isalpha() and ch not in checked:
#        checked.add(ch)
#        indices = ' '.join(str(i+1) for i,v in enumerate(s1) if v == ch)
#        print(ch, indices or 'None')