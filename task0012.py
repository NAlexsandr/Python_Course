# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math

s = int(input("Введите cумму двух загаданных натуральных чисел S: "))
p = int(input("Введите произведение двух загаданных натуральных чисел P: "))

discriminant = s * s - 4 * p
if discriminant < 0:
    print("Нет решения")

if discriminant == 0:
    x = s / 2
    if int(x) + int(s - x) == s and int(x) * int(s - x) == p and 0 < x <= 1000 and 0 < s - x <= 1000:
        print(f"Первое число = {x} Второе число {s - x}")
    else:
        print("Нет решения")

if discriminant > 0:
    x1 = (s + math.sqrt(discriminant)) / 2
    x2 = (s - math.sqrt(discriminant)) / 2
    solution = False
    if int(x1) + int(s - x1) == s and int(x1) * int(s - x1) == p and 0 < x1 <= 1000 and 0 < s - x1 <= 1000:
        print(f"Первое число = {int(x1)} Второе число {int(s - x1)}")
        solution = True
    if int(x2) + int(s - x2) == s and int(x2) * int(s - x2) == p and 0 < x2 <= 1000 and 0 < s - x2 <= 1000 and x2 != s - x1:
        print(f"Первое число = {x2} Второе число {s - x2}")
        solution = True
    if solution == False:
        print("Нет решения")



