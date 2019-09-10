str_c = input()
mal = input()
al = "abcdefghijklmnopqrstuvwxyz"
a = {al[i]:mal[i] for i in range(len(al))}
b = {mal[i]:al[i] for i in range(len(al))}
res = ""
for i in str_c:
    if i in b:
        res = res + b[i]
    else:
        res = res + i
print(res)

