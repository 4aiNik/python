# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.
from random import random


def create_new_list(n):
    i = 0
    while i <= n:
        rand_number = int(random() * 100)
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
    new_list = [base_list[i] for i in range(len(base_list)) if i != 0 and base_list[i] > base_list[i - 1]]
    print(new_list)
