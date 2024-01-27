'''
Задача 15

Исправьте функцию, которая возвращает сумму квадратов чисел в списке.
'''

def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num - 2

