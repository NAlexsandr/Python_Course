"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""
# Первое решение
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 2
    while fib_next <= a:

        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)

# Второе решение
a = 8
if a == 0:
    print("Число не соответствует условиям")
else:
    fib_1, fib_2 = 0, 1
    n = 2
    while fib_2 <= a:
        if fib_2 == a:
            print(n)
            break
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        n += 1
    else:
        print(-1)