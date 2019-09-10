lst = list(map(int, input().split()))
num = int(input())
res = list()
index = 0
for i in lst:
    if i == num:
        res.append(index)
    index = index + 1

if res:
    print(" ".join(map(str, res)))
else:
    print("Отсутствует")
