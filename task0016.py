"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai .
Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""

import array as arr

n = int(input("Введите кол-во элементов в массиве N = "))
lst = list(map(int, input(f"Введите {n} целых чисел: ").split(" ")))

print(lst)
x = int(input("Введите число, которое будем искать в массиве X = "))

index = 0
for el in lst:
    if el == x:
        index = index + 1

print(f"Кол-во раз, которое встречается число {x} в массиве = {index}")




