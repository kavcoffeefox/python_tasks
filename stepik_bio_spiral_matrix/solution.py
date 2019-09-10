size = int(input())
res = []
for i in range(size):
    res.append([0 for j in range(size)])
tb = 1
bb = size - 1
lb = 0
rb = size - 1
counter = 0
i, j = 0, 0
flag = 0
while True:
    counter = counter + 1
    if flag == 0: # в право
        res[j][i] = counter
        i = i + 1
        if i == rb:
            rb = rb - 1
            flag = 1
    elif flag == 1: # вниз
        res[j][i] = counter
        j = j + 1
        if j == bb:
            bb = bb - 1
            flag = 2
    elif flag == 2: # влево
        res[j][i] = counter
        i = i - 1
        if i == lb:
            lb = lb + 1
            flag = 3
    elif flag == 3: # вверх
        res[j][i] = counter
        j = j - 1
        if j == tb:
            tb = tb + 1
            flag = 0
    if counter == size**2:
        break
for k in res:
    print(*k)

