n = int(input())
number = n
if n > 100:
    n = n % 100
if (n > 4 and n < 20) or n % 10 > 4 or n % 10 == 0:
    print(str(number) + " программистов")
elif n % 10 == 1:
    print(str(number) + " программист")
elif n % 10 <= 4:
    print(str(number) + " программиста")

