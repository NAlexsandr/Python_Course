# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.


i1 = n % 10
n = n // 10
i2 = n % 10
n = n // 10
i3 = n % 10
n = n // 10
i4 = n % 10
n = n // 10
i5 = n % 10
n = n // 10
i6 = n % 10

if (i1 + i2 + i3) == (i4 + i5 + i6):
    print("YES")
else:
    print("NO")
