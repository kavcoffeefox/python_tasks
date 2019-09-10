with open("data.txt", "r") as f:
    data = f.readline()
number = 0
res = ''
for i in data:
    if i.isdigit():
        if number == 0:
            number = int(i)
        else:
            number = number*10 + int(i)
    else:
        if number != 0:
            res = res + number * character
            number = 0
        character = i
print(res)
