
#Найдите сумму цифр трехзначного числа n.

#Результат сохраните в перменную res.

# Программа

n = int(input("Введите трехзначное число: "))
i1 = n % 10
n = n // 10
i2 = n % 10
n = n // 10
i3 = n % 10

res = i1 + i2 + i3
print(res)
