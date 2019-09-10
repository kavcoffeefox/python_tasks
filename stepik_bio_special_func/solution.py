def f(x):
    return x
# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.

count = int(input())
rez = list()
arg = dict()
for _ in range(count):
    x = int(input())
    if x in arg.keys():
        rez.append(arg[x])
    else:
        r = f(x)
        rez.append(r)
        arg[x] = r

for i in rez:
    print(i)
