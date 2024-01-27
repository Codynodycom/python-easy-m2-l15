'''
Задача 8

Исправьте функцию, которая печатает все простые числа до заданного числа N.
'''

def print_primes(n):
    for num in range(2, n):
        prime = True
        for i in range(2, num):
            if num - i == 0:
                prime = False
        if prime:
            print num

