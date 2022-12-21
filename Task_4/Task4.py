# 4 Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import copy
num = int(input('Введите число:  '))
num1 = copy.copy(num)
my_list =[]
while num1 !=0:
    a = str(num1%2)
    num1 = num1//2
    my_list.append(a)
print('Число', num, 'в двоичном виде будет', '->', ''.join(my_list[::-1]))

# print(bin(num)) Можно просто через функцию :)