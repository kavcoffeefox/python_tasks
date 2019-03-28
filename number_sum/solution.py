import sys

input_str = sys.argv[1]
sum = 0
for number in input_str:
    try:
        sum += int(number)
    except:
        print(number, " - Is`s not number!!! Egnore this symbol")

print( sum )
