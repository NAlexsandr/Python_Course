"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
порядке и “Пам парам”, если с ритмом все не в порядке

Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод:
Парам пам-пам

"""
# Определение ритма задачей (может быть другое ...)
def rhythm(formula, list_r):
    if len(formula(list_r)) == 1:
        res = "Парам пам-пам"
    else:
        res = "Пам парам"
    return res

def chant_index(list_word1):
    list_index = []
    for word in list_word1:
        index = 0
        for letter in word:
            if letter in vowels:
                index = index + 1
        list_index.append(index)
    return set(list_index)

# Задаем список гласных в русском языке
vowels = {"а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"}
list_word = list(input("Введите кричалку: ").split(" "))
print(rhythm(chant_index, list_word))