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
my_list = [RI(0,10) for _ in range(10)]
print(f'Исходный список: {my_list}')

new_list = list(zip(my_list,list(x for x in my_list[::-1])))

print(new_list)
if len(new_list)%2 != 0:
    new_list.pop(len(new_list)//2)
    
mult_list = list(map(lambda x: x[0]*x[1], new_list))
print(mult_list)