l = list(map(int, input().split()))
res = list()
if len(l) > 1:
    for i in range(len(l)-1):
        res.append(l[i+1]+l[i-1])
    res.append(l[0]+l[-2])
else:
    res.append(l[0])
print(*res)
