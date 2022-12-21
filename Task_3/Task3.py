# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
result_list = []
for i in my_list:
    result_list.append(round(i-int(i), 2))
print(max(result_list) - min(result_list))# можно так, но результат не совсем верный
# более точное решение ниже
my_min = result_list[0]
my_max = result_list[0]
for i in result_list:
    if i < my_min and i != 0:
        my_min = i
    elif i > my_max and i != 0:
        my_max = i
print(my_max-my_min)