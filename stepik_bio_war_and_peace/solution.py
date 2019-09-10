string = input()
res = dict()
for i in string.lower().split():
    if i in res.keys():
        res[i] = res[i] + 1
    else:
        res[i] = 1
for i in res.keys():
    print("{} {}".format(i, res[i]))
