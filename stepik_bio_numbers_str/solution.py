n = int(input())
res = list()
for i in range(1,n+1):
    res = res + [i for _ in range(i)]
    if len(res) >= n:
        print(" ".join(map(str,res[:n])))
        break