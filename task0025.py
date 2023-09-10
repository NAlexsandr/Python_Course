"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

lst = input("Введите символы через пробел: ").split()
res = {}
#print(type(res))
for i in lst:
    if i in res:
        print(f"{i}_{res[i]}", end=' ')
    else:
        print(i, end=' ')
    res[i] = res.get(i, 0) + 1


#dct = {1: [1, 2, 3], 2: True}
#dct[1] = None

letter_string = "a a a b c a a d c d d"

def letter_counter(handsome_list):
    counts = {}
    output_string = ""

    for letter in handsome_list.split():
        counts[letter] = counts.get(letter, 0) + 1
        output_string += f"{letter}_{counts[letter] - 1} " if counts[letter] > 1 else f"{letter} "

    return output_string


some_string = input("Введите строку ")
print(letter_counter(some_string))

