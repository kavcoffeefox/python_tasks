d = int(input())
dictionary = list()
wlist = list()
wrongset = set()
for i in range(d):
    dictionary.append(input().lower())
l = int(input())
for i in range(l):
    wlist.append(input().lower())
for i in wlist:
    for j in i.split():
        if j not in dictionary:
            wrongset.add(j)
for i in wrongset:
    print(i)
