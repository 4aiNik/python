# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех
# элементов списка.
from functools import reduce
from random import randint


def create_new_list(n):
    i = 0
    while i <= n:
        rand_number = int(randint(100, 1000))
        if rand_number % 2 == 1:
            rand_number += 1
        yield rand_number
        i += 1


list_length = input('Ввод длины генерируемого списка: ')
if not list_length.isdigit():
    print('Не числовое значение')
else:
    list_length = int(list_length)
    generator = create_new_list(list_length)
    base_list = [next(generator) for i in range(list_length)]
    print(base_list)
    result = reduce(lambda x, y: x * y, base_list)
    print(result)
