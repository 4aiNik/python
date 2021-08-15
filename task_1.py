#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.
def numbers_division(first_number, second_number):
    """
    Операция деления
    :param first_number: int
    :param second_number: int
    :return: float | none
    """
    result = None
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
    return result


first_number = input('Ввод первого числа: ')
second_number = input('Ввод второго числа: ')
if not first_number.isdigit() or not second_number.isdigit():
    print('Введены не числовые значения')
else:
    result = numbers_division(int(first_number), int(second_number))
    print(f'Результат: {result}')
