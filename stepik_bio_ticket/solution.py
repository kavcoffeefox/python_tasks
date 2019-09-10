tiket = input()
if sum([int(i) for i in tiket[0:3]]) == sum([int(i) for i in tiket[3:]]):
    print("Счастливый")
else:
    print("Обычный")
