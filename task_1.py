#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.
test_list = [
    666, 'text', 66.6,
    ['список', 'это', 'изменяемый', 'массив'],
    ('кортеж', 'это', 'не изменяемый', 'массив'),
    {'словарь': 111, 'это': 222, 'ассоциативный': 333, 'массив': 444}
]
index = 0
while index < len(test_list):
    current_value = test_list[index]
    print(type(current_value))
    if isinstance(current_value, int):
        print('целое число')
    elif isinstance(current_value, str):
        print('строка')
    elif isinstance(current_value, float):
        print('вещественное число')
    elif isinstance(current_value, list):
        print('список')
    elif isinstance(current_value, tuple):
        print('кортеж')
    elif isinstance(current_value, dict):
        print('словарь')
    index += 1
