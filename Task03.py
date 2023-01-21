# # Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# # [2, 3, 4, 5, 6] => [12, 15, 16];
# # [2, 3, 5, 6] => [12, 15]

# my_list = []
# import random
# import math
# for _ in range(6):
#     my_list.append(random.randint(1,10))
# print('Список:')
# print(my_list)

# product_list = []
# for i in range(math.ceil(len(my_list)/2)):
#     product_list.append(my_list[i]*my_list[-i-1])

# print('Произведения пар значений списка:')
# print(product_list)

from random import randint as RI
my_list = [RI(0, 10) for _ in range(11)]
print(f'Исходный список: {my_list}')

new_list = list(zip(my_list, list(x for x in my_list[::-1])))
new_list = list(x[1]
                for x in list(enumerate(new_list)) if x[0] < len(new_list)//2)
mult_list = list(map(lambda x: x[0]*x[1], new_list))
print(f'Произведения пар: {mult_list}')
