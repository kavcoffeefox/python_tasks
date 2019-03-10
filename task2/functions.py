#1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0

def bad_sum(value1, value2):
    try:
        if (value1 > 0) and (value2 > 0):
            return value1 + value2
        elif (value1 < 0) and (value2 < 0):
            return value1 - value2
        else:
            return 0;
    except TypeError as tp:
        print("Bad value")
        print(tp)



#2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, #вывести в консоль
def two_max(value1,value2, value3):
    if value1 > value2:
        if value2 > value3:
            return (value1, value2)
        else:
            return (value1, value3)
    else:
        if value1 > value3:
            return (value1, value2)
        else:
            return (value2, value3)
#
#3.Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка
def filter_evens_numbers(listWithNumber, flag = True):
    try:
        if flag == True:
            return list(i for i in listWithNumber if i%2 == 0)
        else:
            return list(i for i in listWithNumber if i%2 != 0)
    except TypeError as te:
        print("Error!")
        print(te)
    except:
        print("Error")

if __name__ == "__main__":
# Тестируем функции
    print("Test bad_sum")
    print(bad_sum(10,20))
    print(bad_sum(-10,-15))
    print(bad_sum("12",1))
    print(bad_sum(-10, 10))

    print("Test two_max")
    print(two_max(10,23,-10))
    print(two_max(100,-100,23))

    print("Test filter_evens_number")
    print(filter_evens_numbers(range(1,100)))
    print(filter_evens_numbers(range(1,100), False))

