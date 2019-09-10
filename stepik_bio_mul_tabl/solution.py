a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    if i == a:
        print(" " + " ".join(map(str,[ j for j in range(c,d+1)])))
    print(" ".join(map(str,[i] + [ j*i for j in range(c,d+1)])))