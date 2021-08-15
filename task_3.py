#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.
def get_max_sum(*numbers):
    """
    Сложение двух наибольших чисел
    :param numbers: tuple
    :return: int
    """
    numbers = list(numbers)
    numbers.sort(reverse=True)
    return numbers[0] + numbers[1]


first_number = input('Ввод первого числа: ')
second_number = input('Ввод второго числа: ')
third_number = input('Ввод третьего числа: ')
if not first_number.isdigit() or not second_number.isdigit() or not third_number.isdigit():
    print('Введены не числовые значения')
else:
    result = get_max_sum(int(first_number), int(second_number), int(third_number))
    print(f'Результат: {result}')
