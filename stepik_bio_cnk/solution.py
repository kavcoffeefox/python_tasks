def C(n, k):
    res = 0
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return int(C(n - 1, k)) + int(C(n - 1, k - 1))


n, k = map(int, input().split())
print(C(n, k))
