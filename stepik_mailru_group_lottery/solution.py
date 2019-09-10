# поместите ваше решение здесь, модуль random уже импортирован
number = int(input())
last_tiket = input()

numbers_tiket = int(last_tiket.split()[0])
serial_tiket = last_tiket.split()[1]

winner = list()

if number > numbers_tiket:
    number = numbers_tiket

while (len(winner) != number):
    s = random.randint(1, numbers_tiket)
    if s not in winner:
        winner.append(s)
        print("Победитель номер %s - " % (winner.index(s) + 1) + "\"" + " ".join(
            [str(s).zfill(6), serial_tiket.upper()]) + "\"")


