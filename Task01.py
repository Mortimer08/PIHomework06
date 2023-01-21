# # Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# # Пример:
# # Для n=4 -> [2, 2.25, 2.37, 2.44]
# # Сумма 9.06

# number = int(input('Введите целое число: '))
# sum = 0

# sequence = []
# for i in range(1, number+1):
#     sequence.append(round((1+1/i)**i, 2))
#     sum += sequence[i-1]

# print(f'Для n={number} -> {sequence}')
# print(f'Сумма {sum}')

number = int(input('Введите целое число: '))
sequence = [round((1+1/n)**n, 2) for n in range(1, number+1)]
sum = 0
for item in sequence:
    sum += item
print(f'Для n={number} -> {sequence}')
print(f'Сумма {sum}')
