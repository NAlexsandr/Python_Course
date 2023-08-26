"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

# вариант 1
lst = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(lst)))

# вариант 2
lst = [1, 1, 2, 0, -1, 3, 4, 4]

count_unic = []
for i in lst:
    if i not in count_unic:
        count_unic.append(i)

# вариант 3
some_list = [1, 5, 2, 0, -1, 3, 4, 4]
some_dictionary = {}

for item in some_list:
    if item not in some_dictionary:
        some_dictionary[item] = item

print(len(some_dictionary))
