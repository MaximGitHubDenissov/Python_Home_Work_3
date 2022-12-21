# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

n = int(input('Введите число: '))
first = 0
second = 1
my_list = [first, second]
for i in range (n-1):
    sum = first-second
    first = second
    second = sum
    my_list.append(sum)
my_list = my_list[::-1]
first = 0
second = 1
my_list.append(second)
for i in range (n-1):
    sum = first+second
    first = second
    second = sum
    my_list.append(sum)
print(my_list)    