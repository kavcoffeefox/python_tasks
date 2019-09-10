t1 = int(input())
t2 = int(input())
dt1, dt2 = list(), list()
if t1 == 1 or t2 == 1:
    print(t1 * t2)
else:
    i=2
    while True:
        if t1%i == 0:
            t1 = t1 / i
            dt1.append(i)
            if t1 == 1:
                break
            i = 2
        else:
            i = i + 1
    i=2
    while True:
        if t2%i == 0:
            t2 = t2 / i
            if i not in dt1:
                dt2.append(i)
            else:
                dt1.remove(i)
                dt2.append(i)
            if t2 == 1:
                break
            i = 2
        else:
            i = i + 1
    res = 1
    for i in dt2+dt1:
        res = res * i
    print(res)