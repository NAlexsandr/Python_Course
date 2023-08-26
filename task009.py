# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# Решение № 1
n = 5
factorial = 1

while n > 1:
    factorial = factorial * n
    n = n - 1

print(factorial)

# Решение № 2
n = int(input("Введите значение n: "))

result = 1
current_num = 1

while current_num <= n:
    result *= current_num
    current_num += 1

print(f"{n}! = {result}")