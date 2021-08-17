# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
from random import random


def create_new_list(n):
    i = 0
    while i <= n:
        rand_number = int(random() * 10)
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
    no_repeat = []
    new_list = [number for number in base_list if number not in no_repeat and no_repeat.append(number)]
    print(no_repeat)
