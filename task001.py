#Задача №1. Решение в группах
#Семинар 1. Ввод-вывод, операторы ветвления
#За день машина проезжает n километров. Сколько
#дней нужно, чтобы проехать маршрут длиной m
#километров? При решении этой задачи нельзя
#пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
#2

#rounded_up = math.ceil(number)
import math

n = int(input("Введите количество километров в день: "))
m = int(input("Введите длину маршрута: "))

days = math.ceil(m / n)
print(f"В пути {days} дня")

