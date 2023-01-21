# # Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# # Пример:
# # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = []
# import random
# for _ in range(5):
#     my_list.append(random.randint(1,10))
# print('Список:')
# print(my_list)

# sum = 0
# for i in range(1,len(my_list),2):
#     sum += my_list[i]

# print(f'Сумма нечётных элементов: {sum}')


from random import randint as RI 
my_list = [RI(0,10) for _ in range(11)]

print(f'Исходный список: {my_list}')

my_list = list(x for x in my_list[1::2])

sum = 0
for item in my_list:
    sum += item

print(f'Сумма нечётных элементов: {sum}')
