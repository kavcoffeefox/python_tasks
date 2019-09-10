s = input()
res = str()
counter = 0
smb = str()
for i in s:
    if smb != i:
        res = res + smb + str(counter)
        smb = i
        counter = 1
    else:
        counter = counter + 1
res = res + smb + str(counter)
print(res[1:])
