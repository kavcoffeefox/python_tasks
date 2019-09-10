step = int(input())
x, y = 0, 0
for i in range(step):
    command = input().split()
    if command[0] == "север":
        y = y + int(command[1])
    elif command[0] == "запад":
        x = x - int(command[1])
    elif command[0] == "юг":
        y = y - int(command[1])
    elif command[0] == "восток":
        x = x + int(command[1])
print("{} {}".format(x, y))
