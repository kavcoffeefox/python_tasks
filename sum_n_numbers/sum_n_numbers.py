# Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.
# Вашей программе на вход подается последовательность строк.
# Первая строка содержит число n (1 ≤ n ≤ 100).
# В следующих n строках содержится по одному целому числу.
count = int(input())
sum_numbers = 0
for i in range(count):
    sum_numbers += int(input())

print(sum_numbers)