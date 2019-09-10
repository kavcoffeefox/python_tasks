al = input()
mal = input()
str_o = input()
str_c = input()
a = {al[i]: mal[i] for i in range(len(al))}
b = {mal[i]: al[i] for i in range(len(al))}
print("".join([a[i] for i in str_o]))
print("".join([b[i] for i in str_c]))
